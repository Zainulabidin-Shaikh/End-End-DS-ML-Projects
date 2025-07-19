# =============================================
# logger.py – Handles logging of all executions
# =============================================

"""
This module sets up a logging system to record events, errors, 
and progress throughout the pipeline.

What does it do?
- Creates a 'logs' folder (if not exists)
- Creates a .log file named by current date and time
- Logs everything in a standard readable format
"""

# ✅ Standard Library Imports
import logging               # For logging messages (info, errors, etc.)
import os                    # To work with folders, paths
from datetime import datetime  # To get current time for timestamping log file names

# ✅ Create a unique log file name using the current datetime
# Example: "07_19_2025_21_32_40.log"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# ✅ Define the folder path where logs should be stored
# os.getcwd() gives current working directory like: D:\End-To-End ML Projects
logs_path = os.path.join(os.getcwd(), "logs")

# ✅ Create the "logs" folder if it doesn't already exist
# exist_ok=True avoids crashing if folder already exists
os.makedirs(logs_path, exist_ok=True)

# ✅ Full path to the log file: e.g., D:\End-To-End ML Projects\logs\07_19_2025_21_32_40.log
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# ✅ Set up the logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,                   # All logs will be saved to this file
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # FORMAT:
    #   - %(asctime)s → Time of log
    #   - %(lineno)d → Line number where the log was called
    #   - %(name)s   → Module name
    #   - %(levelname)s → Level of log (INFO, ERROR, etc.)
    #   - %(message)s → Your log message
    level=logging.INFO                        # Minimum level to log (INFO or higher)
)

# ✅ OPTIONAL: Quick test to confirm logger works
# if __name__ == "__main__":
#     logging.info("Logging system initialized successfully!")
