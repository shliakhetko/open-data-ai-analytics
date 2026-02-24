"""
Візуалізація даних реєстру закладів вищої освіти.
Зберігає графіки в reports/figures/.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.load_data import load_uni_data
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")
plt.rcParams["figure.figsize"] = (10, 6)


def get_figures_dir() -> Path:
    repo_root = Path(__file__).resolve().parent.parent
    out = repo_root / "reports" / "figures"
    out.mkdir(parents=True, exist_ok=True)
    return out


def plot_top_regions(df: pd.DataFrame, top_n: int = 12) -> Path:
    """Стовпчикова діаграма: топ регіонів за кількістю закладів."""
    by_region = df["region_name_u"].value_counts().head(top_n)
    fig, ax = plt.subplots()
    by_region.plot(kind="barh", ax=ax, color="steelblue", edgecolor="navy", alpha=0.85)
    ax.set_xlabel("Кількість закладів")
    ax.set_ylabel("Регіон")
    ax.set_title("Топ регіонів за кількістю закладів вищої освіти")
    plt.tight_layout()
    path = get_figures_dir() / "top_regions.png"
    fig.savefig(path, dpi=120, bbox_inches="tight")
    plt.close()
    return path


def plot_financing(df: pd.DataFrame) -> Path:
    """Кругова діаграма: державні vs приватні."""
    by_fin = df["university_financing_type_name"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(by_fin.values, labels=by_fin.index, autopct="%1.1f%%", startangle=90, colors=["#2ecc71", "#e74c3c"])
    ax.set_title("Розподіл за типом фінансування")
    plt.tight_layout()
    path = get_figures_dir() / "financing_pie.png"
    fig.savefig(path, dpi=120, bbox_inches="tight")
    plt.close()
    return path


def plot_registration_by_decade(df: pd.DataFrame) -> Path:
    """Стовпчикова діаграма: кількість закладів по десятиліттям реєстрації."""
    df = df.dropna(subset=["registration_year"])
    df["decade"] = (df["registration_year"] // 10 * 10).astype(int)
    by_decade = df.groupby("decade").size().sort_index()
    fig, ax = plt.subplots()
    by_decade.plot(kind="bar", ax=ax, color="teal", edgecolor="darkgreen", alpha=0.8)
    ax.set_xlabel("Десятиліття (рік реєстрації)")
    ax.set_ylabel("Кількість закладів")
    ax.set_title("Реєстрація закладів по десятиліттям")
    plt.xticks(rotation=45)
    plt.tight_layout()
    path = get_figures_dir() / "registration_by_decade.png"
    fig.savefig(path, dpi=120, bbox_inches="tight")
    plt.close()
    return path


def run_all():
    df = load_uni_data()
    paths = []
    paths.append(plot_top_regions(df))
    paths.append(plot_financing(df))
    paths.append(plot_registration_by_decade(df))
    print("Збережено графіки:")
    for p in paths:
        print(" ", p)
    return paths


if __name__ == "__main__":
    run_all()
