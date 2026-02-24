"""
Дослідницький аналіз даних та прості моделі.
Розподіли за регіоном, типом фінансування, роком реєстрації; проста групова статистика.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.load_data import load_uni_data
import pandas as pd


def run_analysis():
    df = load_uni_data()

    report = []
    report.append("=== Дослідницький аналіз ===\n")

    # 1. Топ регіонів за кількістю закладів
    by_region = df["region_name_u"].value_counts().head(10)
    report.append("1. Топ-10 регіонів за кількістю закладів:")
    for region, count in by_region.items():
        report.append(f"   - {region}: {count}")
    report.append("")

    # 2. Державні vs приватні
    by_fin = df["university_financing_type_name"].value_counts()
    report.append("2. Розподіл за типом фінансування:")
    for fin, count in by_fin.items():
        report.append(f"   - {fin}: {count}")
    report.append("")

    # 3. Рік реєстрації: розподіл по десятиліттям
    df["decade"] = (df["registration_year"] // 10 * 10).astype("Int64")
    by_decade = df.groupby("decade", dropna=False).size().sort_index()
    report.append("3. Кількість зареєстрованих закладів по десятиліттям:")
    for dec, count in by_decade.items():
        report.append(f"   - {dec}s: {count}")
    report.append("")

    # 4. Проста "модель": середній рік реєстрації по типу фінансування
    report.append("4. Середній рік реєстрації за типом фінансування (проста агрегація):")
    agg = df.groupby("university_financing_type_name")["registration_year"].agg(["mean", "count"])
    for fin in agg.index:
        report.append(f"   - {fin}: сер. рік {agg.loc[fin, 'mean']:.0f}, n={int(agg.loc[fin, 'count'])}")

    return "\n".join(report)


if __name__ == "__main__":
    print(run_analysis())
