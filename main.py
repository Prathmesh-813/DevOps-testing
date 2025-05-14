import os
import logging
from flask import Flask
from etl.etl_script import run_etl  # Import the ETL function from the script

# Setup logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Add handler if not already added (to avoid duplicate logs)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Main Application!</h1><p>This is a simple web service running on ECS.</p>"

@app.route('/run_etl')
def trigger_etl():
    logger.info("Triggering the ETL job...")
    try:
        run_etl()
        return "<h1>ETL Job Triggered Successfully!</h1><p>The ETL job has been triggered.</p>"
    except Exception as e:
        logger.error(f"Error triggering ETL: {e}")
        return f"<h1>Error Triggering ETL</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
