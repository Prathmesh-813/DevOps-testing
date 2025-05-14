import os
import logging
from flask import Flask
from etl.etl_script import run_etl  # Import the ETL function from the script

# Setup logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    """
    Home route that displays a message.
    This will show in the browser when accessed.
    """
    return "<h1>Welcome to the Main Application!</h1><p>This is a simple web service running on ECS.</p>"

@app.route('/run_etl')
def trigger_etl():
    """
    Route that manually triggers the ETL process when accessed.
    """
    logger.info("Triggering the ETL job...")
    try:
        run_etl()  # Run the ETL process
        return "<h1>ETL Job Triggered Successfully!</h1><p>The ETL job has been triggered.</p>"
    except Exception as e:
        logger.error(f"Error triggering ETL: {e}")
        return f"<h1>Error Triggering ETL</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    # Run the Flask app on port 5000 (default)
    app.run(host="0.0.0.0", port=5000)
