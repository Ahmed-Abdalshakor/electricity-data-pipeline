
# ⚡ Electricity Data Pipeline

A simple Data Engineering pipeline that collects monthly electricity demand data for Egypt, transforms it using Python and Pandas, validates the data, and loads it into Microsoft SQL Server.

## Architecture

Ember Energy API
        ↓
    Extract
        ↓
    Raw JSON
        ↓
   Transform
        ↓
  Processed CSV
        ↓
    Validate
        ↓
      Load
        ↓
   SQL Server

## Technologies

- Python
- Pandas
- Requests
- SQLAlchemy
- PyODBC
- Microsoft SQL Server
- Git & GitHub

## Pipeline Steps

### 1. Extract

Fetches monthly electricity demand data for Egypt from the Ember Energy API.

### 2. Transform

Uses Pandas to:

- Clean the data
- Convert dates
- Add year and month
- Remove duplicate dates
- Handle missing values

### 3. Validate

Checks:

- Empty dataset
- Missing values
- Duplicate dates
- Invalid demand values
- Required columns

### 4. Load

Loads the processed data into SQL Server.

The pipeline also prevents duplicate records when it runs again.

## Data

The project uses monthly electricity demand data for Egypt.

The current dataset contains 125 records covering:

- 2016 to May 2026
- Monthly demand
- Demand measured in TWh

## Project Structure

```text
electricity-data-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── ingestion/
│   │   └── extract.py
│   ├── transformation/
│   │   └── transform.py
│   ├── loading/
│   │   └── load.py
│   ├── validation.py
│   └── pipeline.py
│
├── tests/
├── logs/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
