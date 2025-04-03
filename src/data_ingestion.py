import os
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_name = self.config["bucket_file_name"]
        self.train_test_ratio = self.config["train_ratio"]

        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info(f"Data Ingestion initialized with bucket: {self.bucket_name}, file: {self.file_name}")

    def download_csv_from_gcp(self):
        try:
            # ✅ Use service account credentials
            service_account_path = "C:/Users/Asus/Downloads/beaming-team-447617-k7-15028f5f7927.json"
            client = storage.Client.from_service_account_json(service_account_path)

            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(self.file_name)

            blob.download_to_filename(RAW_FILE_PATH)

            logger.info(f"✅ CSV file successfully downloaded to {RAW_FILE_PATH}")
            logger.info(f"📦 File size: {os.path.getsize(RAW_FILE_PATH)} bytes")

        except Exception as e:
            logger.error(f"❌ Error while downloading the CSV file: {e}")
            raise CustomException(f"Failed to download CSV file: {e}")

    def split_data(self):
        try:
            logger.info("📊 Starting data splitting process...")

            data = pd.read_csv(RAW_FILE_PATH)
            logger.info(f"✅ Raw data loaded. Shape: {data.shape}")
            logger.info(f"🔍 Preview:\n{data.head()}")

            train_data, test_data = train_test_split(
                data, test_size=1 - self.train_test_ratio, random_state=42
            )

            train_data.to_csv(TRAIN_FILE_PATH, index=False)
            test_data.to_csv(TEST_FILE_PATH, index=False)

            logger.info(f"📁 Train data saved to {TRAIN_FILE_PATH}, shape: {train_data.shape}")
            logger.info(f"📁 Test data saved to {TEST_FILE_PATH}, shape: {test_data.shape}")

        except Exception as e:
            logger.error(f"❌ Error while splitting data: {e}")
            raise CustomException(f"Failed to split data into train/test sets: {e}")

    def run(self):
        try:
            logger.info("🚀 Starting the data ingestion process...")
            self.download_csv_from_gcp()
            self.split_data()
            logger.info("✅ Data ingestion completed successfully.")
        except CustomException as ce:
            logger.error(f"❌ CustomException: {str(ce)}")
        except Exception as e:
            logger.error(f"❌ Unexpected Error: {str(e)}")
            raise CustomException("Unexpected error during data ingestion", e)
        finally:
            logger.info("📦 Data ingestion process ended (with or without errors).")

if __name__ == "__main__":
    config_data = read_yaml(CONFIG_PATH)
    data_ingestion = DataIngestion(config_data)
    data_ingestion.run()
