import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv


def extract_data():
    # Load environment variables
    load_dotenv()

    api_key = os.getenv("EMBER_API_KEY")

    if not api_key:
        raise ValueError("EMBER_API_KEY was not found in .env")

    # Ember API endpoint
    url = "https://api.ember-energy.org/v1/electricity-demand/monthly"

    # Request parameters
    params = {
        "entity_code": "EGY",
        "api_key": api_key,
    }

    # Send request
    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    # Raise error if request failed
    response.raise_for_status()

    # Convert JSON response
    data = response.json()

    # Create raw data directory
    raw_data_dir = Path("data/raw")
    raw_data_dir.mkdir(parents=True, exist_ok=True)

    # Output file
    output_file = raw_data_dir / "egypt_electricity_demand_monthly.json"

    # Save raw data
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print("Data extraction completed!")
    print(f"Raw data saved to: {output_file}")

    return output_file