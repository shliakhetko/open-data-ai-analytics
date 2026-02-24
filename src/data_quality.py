"""
Перевірка якості даних реєстру закладів вищої освіти.
Звіт: пропуски, дублікати, узгодженість регіонів (region_name vs region_name_u).
"""

import sys
from pathlib import Path

# дозволити запуск з кореня репо або з src
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.load_data import load_uni_data


def run_quality_checks():
    df = load_uni_data()

    report = []
    report.append("=== Звіт якості даних ===\n")

    # 1. Пропуски
    missing = df.isnull().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    report.append("1. Пропуски (колонки з хоча б одним пропуском):")
    if len(missing) == 0:
        report.append("   Немає пропусків.")
    else:
        for col, count in missing.items():
            report.append(f"   - {col}: {count} ({100 * count / len(df):.1f}%)")
    report.append("")

    # 2. Дублікати за ключовими полями
    dup_id = df.duplicated(subset=["university_id"], keep=False).sum()
    dup_edrpou = df.duplicated(subset=["university_edrpou"], keep=False).sum()
    report.append("2. Дублікати:")
    report.append(f"   - За university_id: {dup_id} рядків у дублікатах")
    report.append(f"   - За university_edrpou: {dup_edrpou} рядків у дублікатах")
    report.append("")

    # 3. Узгодженість регіонів (registration address vs actual address)
    region_mismatch = (df["region_name"].fillna("") != df["region_name_u"].fillna("")).sum()
    report.append("3. Невідповідність регіонів (region_name ≠ region_name_u):")
    report.append(f"   Рядків: {region_mismatch} ({100 * region_mismatch / len(df):.1f}%)")
    report.append("")

    report.append(f"Всього записів: {len(df)}")
    return "\n".join(report)


if __name__ == "__main__":
    print(run_quality_checks())
