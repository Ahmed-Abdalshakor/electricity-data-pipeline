import logging
from pathlib import Path

from ingestion.extract import extract_data
from transformation.transform import transform_data
from loading.load import load_data
from validation import validate_data


# Create logs directory
LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)


# Configure logging
logging.basicConfig(
    filename=LOG_DIR / "pipeline.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def run_pipeline():

    logger.info("Pipeline started")

    print("=" * 50)
    print("Starting Electricity Data Pipeline")
    print("=" * 50)

    try:

        # Step 1: Extract
        print("\n[1/4] Extracting data...")
        logger.info("Starting extraction")

        extract_data()

        logger.info("Extraction completed successfully")


        # Step 2: Transform
        print("\n[2/4] Transforming data...")
        logger.info("Starting transformation")

        transform_data()

        logger.info("Transformation completed successfully")


        # Step 3: Validate
        print("\n[3/4] Validating data...")
        logger.info("Starting data validation")

        processed_file = (
            "data/processed/egypt_electricity_demand_monthly.csv"
        )

        validate_data(processed_file)

        logger.info("Data validation completed successfully")


        # Step 4: Load
        print("\n[4/4] Loading data...")
        logger.info("Starting loading")

        load_data()

        logger.info("Loading completed successfully")


        print("\n" + "=" * 50)
        print("Pipeline completed successfully!")
        print("=" * 50)

        logger.info("Pipeline completed successfully")


    except Exception as error:

        logger.exception("Pipeline failed")

        print("\n" + "=" * 50)
        print("Pipeline failed!")
        print(f"Error: {error}")
        print("=" * 50)


if __name__ == "__main__":
    run_pipeline()