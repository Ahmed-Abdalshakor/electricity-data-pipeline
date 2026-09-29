import pandas as pd
from sqlalchemy import create_engine, text


def load_data():
    # SQL Server connection
    database_url = (
        "mssql+pyodbc://@localhost/ElectricityDB"
        "?driver=ODBC+Driver+18+for+SQL+Server"
        "&Trusted_Connection=yes"
        "&TrustServerCertificate=yes"
    )

    engine = create_engine(database_url)

    # Processed data
    input_file = (
        "data/processed/egypt_electricity_demand_monthly.csv"
    )

    # Read CSV
    df = pd.read_csv(input_file)

    # Convert date
    df["date"] = pd.to_datetime(df["date"])

    print(f"Records extracted from CSV: {len(df)}")

    # Get existing dates from SQL Server
    with engine.connect() as connection:
        existing_dates = pd.read_sql(
            text("SELECT date FROM electricity_demand"),
            connection
        )

    # Convert database dates
    existing_dates["date"] = pd.to_datetime(
        existing_dates["date"]
    )

    # Keep only new records
    new_records = df[
        ~df["date"].isin(existing_dates["date"])
    ].copy()

    print(f"New records to load: {len(new_records)}")

    # Load new records
    if not new_records.empty:
        new_records.to_sql(
            "electricity_demand",
            con=engine,
            if_exists="append",
            index=False
        )

        print("New records loaded successfully!")
    else:
        print("No new records to load.")

    # Final count
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT COUNT(*) FROM electricity_demand")
        )

        total_records = result.scalar()

    print(f"Total records in SQL Server: {total_records}")

    return total_records