# 🧪 QA Portfolio: Expense Tracker

**Sandbox project demonstrating the full QA cycle:** requirements analysis → test documentation → manual testing → bug reporting → UI automation → CI/CD → Allure reporting.

The application under test is a small Flask web app ("Expense Tracker") with intentionally embedded defects. I joined this project as a QA engineer: analyzed requirements, asked clarifying questions, found and reported bugs, then automated the critical scenarios.

## 🔗 Quick links

| Artifact | Link |
|---|---|
| 📊 Allure report (auto-published) | https://kyklina-irina.github.io/qa-portfolio-expense-tracker/ |
| 🐞 Bug reports | [GitHub Issues](https://github.com/Kyklina-Irina/qa-portfolio-expense-tracker/issues) |
| 🤖 CI pipeline | [GitHub Actions](https://github.com/Kyklina-Irina/qa-portfolio-expense-tracker/actions) |

![Autotests](https://github.com/Kyklina-Irina/qa-portfolio-expense-tracker/actions/workflows/autotests.yml/badge.svg) ![Python 3.12](https://img.shields.io/badge/python-3.12-3776AB?logo=python&logoColor=white) ![Playwright](https://img.shields.io/badge/automation-Playwright-2EAD33?logo=playwright&logoColor=white)

## 🛠️ Stack

- **Automation:** Python 3.12, Pytest, Playwright (sync API), Page Object Model
- **Reporting:** Allure (auto-deployed to GitHub Pages on every push)
- **CI/CD:** GitHub Actions
- **App under test:** Python Flask

## 📁 Project structure

    qa-portfolio-expense-tracker/
    ├── .github/
    │   ├── ISSUE_TEMPLATE/        # bug report template
    │   └── workflows/autotests.yml  # CI: tests + Allure + Pages
    ├── docs/
    │   ├── test_plan.md           # test plan
    │   └── checklist.md           # manual test checklist
    ├── tests/
    │   ├── pages/expense_page.py  # Page Object
    │   ├── conftest.py            # fixtures (auto-start app, browser)
    │   └── test_expense.py        # UI autotests
    ├── app.py                     # app under test (Flask)
    ├── requirements.txt
    ├── requirements_test.txt
    └── README.md

## 🐞 Key bugs found

| Bug | Severity |
|---|---|
| Server crash (HTTP 500) on amount values like `.` or `10.5.5` | Critical |
| Past-month expense is counted in the "current month" total | Major |
| Negative and zero amounts are accepted | Major |
| Empty required fields are accepted | Major |
| Free-text category instead of a fixed list | Major |

Full bug reports with steps to reproduce, expected/actual results — in [GitHub Issues](https://github.com/Kyklina-Irina/qa-portfolio-expense-tracker/issues).

## 📄 Test documentation

- [Test Plan](docs/test_plan.md)
- [Checklist](docs/checklist.md)

## ▶️ Run locally

    pip install -r requirements.txt -r requirements_test.txt
    python -m playwright install chromium
    python -m pytest tests/ -v

    # Visible browser mode (PowerShell):
    $env:HEADLESS="false"; python -m pytest tests/ -v

The Flask app is started and stopped automatically by a session fixture (`tests/conftest.py`).

## 🤖 CI/CD

On every push, GitHub Actions:
1. Installs Python and dependencies
2. Installs Playwright Chromium
3. Runs the test suite and collects `allure-results`
4. Builds the Allure report and deploys it to GitHub Pages

## 👩💻 About me

I'm Irina, a QA engineer. This project shows how I work: attention to requirements, structured bug reporting and clean automation. Open to feedback and opportunities!
