# etl_script.py
import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Add this block:
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def run_etl():
    logger.info("Starting ETL process...")

    try:
        logger.info("Extracting data...")
        time.sleep(2)

        logger.info("Transforming data...")
        time.sleep(2)

        logger.info("Loading data...")
        time.sleep(2)

        logger.info("ETL process completed successfully!")
    except Exception as e:
        logger.error(f"ETL process failed: {e}")
