"""
Скрипт завантаження даних реєстру закладів вищої освіти.
Джерело: data.gov.ua — Реєстр суб'єктів освітньої діяльності.
"""

from pathlib import Path

import pandas as pd


def get_data_path() -> Path:
    """Шлях до CSV (відносно кореня репозиторію)."""
    repo_root = Path(__file__).resolve().parent.parent
    return repo_root / "raw" / "uni_data.csv"


def load_uni_data() -> pd.DataFrame:
    """Завантажує таблицю закладів вищої освіти з data/uni_data.csv."""
    path = get_data_path()
    if not path.exists():
        raise FileNotFoundError(f"Файл даних не знайдено: {path}")
    return pd.read_csv(path)


if __name__ == "__main__":
    df = load_uni_data()
    print("Завантажено записів:", len(df))
    print("Колонок:", len(df.columns))
    print("\nПерші колонки:", list(df.columns[:8]))
    print("\nПриклад (перший рядок, назва та регіон):")
    print(df[["university_name", "region_name_u", "registration_year"]].head(2).to_string())
