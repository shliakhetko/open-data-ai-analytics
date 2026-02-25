# Звіт з лабораторної роботи: Git та open-data-ai-analytics

## Мета роботи

Опанувати роботу з системою контролю версій Git у контексті проєкту аналітики відкритих даних: створення структури репо, робота з гілками, merge, розв’язання конфліктів, тегування.

## Виконані кроки

**1. Репозиторій.** Створено та підключено репозиторій open-data-ai-analytics на GitHub.

**2. Структура проєкту.** Додано файли та каталоги: README.md, .gitignore, data/README.md, notebooks/, src/, reports/figures/.

**3. .gitignore.** Налаштовано ігнорування __pycache__/, .ipynb_checkpoints/, .venv/, .env, data/raw/. Зроблено окремий коміт.

**4. README.md.** Заповнено назву та мету проєкту, джерело відкритих даних (Реєстр суб'єктів освітньої діяльності, data.gov.ua), три гіпотези для аналізу (регіональний розподіл, державні/приватні заклади, типи закладів і рік реєстрації). Зроблено коміт.

**5–6. Гілка feature/data_load.** Створено гілку feature/data_load, додано скрипт завантаження даних src/load_data.py (завантаження CSV з data/uni_data.csv). Гілку змерджено в main.

**7. Дві feature-гілки.** Створено feature/data_quality_analysis (код перевірки якості: пропуски, дублікати, узгодженість регіонів) та feature/data_research (аналіз даних, агрегації за регіоном, типом фінансування, десятиліттям).

**8. Мердж через PR/MR.** Обидві гілки змерджено в main; при мерджі вказано опис «що зроблено».

**9. Merge-конфлікт.** Обидві гілки змінювали одну секцію README («Що зроблено»). При мерджі feature/data_research виник конфлікт; розв’язано коректно — залишено обидва пункти в секції.

**10. Гілка feature/visualization.** Створено гілку feature/visualization, додано код візуалізації (src/visualization.py): графіки за регіонами, типом фінансування, реєстрацією по десятиліттям. Гілку змерджено в main.

**11. CHANGELOG та тег.** Додано CHANGELOG.md з описом змін. Створено тег v0.1.0 і запушено його на віддалений репозиторій.

## Результат

- Репозиторій має передбачену структуру, історію комітів і мерджів з feature-гілок, коректно розв’язаний конфлікт у README, тег v0.1.0.
- У проєкті є скрипти: завантаження даних, перевірка якості, дослідницький аналіз, візуалізація; дані — реєстр закладів вищої освіти з data.gov.ua.

## Висновок

В рамках лабораторної роботи я опанував навичками використання системи контролю версій Git. Створено репозиторій з заданою структурою, налаштовано .gitignore та оформлено README з метою, джерелом даних і гіпотезами. Робота виконувалася в feature-гілках: завантаження даних, перевірка якості, дослідницький аналіз, візуалізація. Гілки зливались у main через merge (або Pull Request), з описом «що зроблено». Створено merge-конфлікт у README між двома гілками і коректно його розв’язано. Додано CHANGELOG.md і створено тег v0.1.0. Закріплено роботу з гілками, merge, розв’язанням конфліктів і тегуванням у Git.

```
open-data-ai-analytics main ? ✗ git log --oneline --graph --decorate --all
* 5db3daa (HEAD -> main, tag: v0.1.0, origin/main, origin/HEAD) Add CHANGELOG.md for v0.1.0
* 45829bc (feature/visualization) Add data visualization (top regions, financing, registration by decade)
*   80175ef Merge pull request #2 from shliakhetko/feature/data_research
|\  
| *   0038ea6 (origin/feature/data_research) Merge branch 'main' into feature/data_research
| |\  
| |/  
|/|   
* |   0a3c06a Merge pull request #1 from shliakhetko/feature/data_quality_analysis
|\ \  
| * | bf040d5 (origin/feature/data_quality_analysis, feature/data_quality_analysis) Add data quality checks; update Що зроблено
| | * 5eb4fd6 (feature/data_research) Add data research and simple aggregations; update Що зроблено
| |/  
| * f2a8874 Add section Що зроблено to README
|/  
* a7179d2 (feature/data_load) Add load data script
* 03fca20 Fill README: project goal, data source, 3 analysis hypotheses
* 0bb3452 Add project structure and .gitignore (notebooks, src, reports/figures, data/raw)
* 0b35eec (master) Initial commit
```