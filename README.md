# BankFlow
## BankFlow is an ETL pipeline that takes messy Excel reports and turns them into clean, structured data. It’s built for the real world—where spreadsheets pile up and you need something reliable to pull it all together.

# What it does
## Watches for new files – drop an Excel file in the right folder, and BankFlow picks it up automatically.

## Validates as it goes – checks for missing fields, weird data types, and things that don’t add up (like a negative loan amount).

## Keeps everything in one place – no more hunting through shared drives. Data ends up in a proper SQL database.

## Shows you what matters – a simple Streamlit dashboard with actual KPIs, not just raw tables.

## Actually testable – there are unit tests, linting, and it’s set up to play nice with CI/CD.

## How it’s put together
## The code is split into clear pieces so it’s easy to tweak later:

## Ingestion – uses watchdog to spot new .xlsx or .csv files.

## Transformation – pandas does the heavy lifting with business rules and validation.

## Storage – SQLAlchemy handles talking to the database (SQLite for dev, PostgreSQL in production).

## Visualization – Streamlit + Plotly turn the data into something you can actually use.

# Tech stack
Python 3.10+

pandas, openpyxl

SQLite / PostgreSQL

watchdog

Streamlit, Plotly

pytest, flake8