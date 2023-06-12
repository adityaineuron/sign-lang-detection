import os
import sys
from six.moves import urllib
import zipfile
from dataclasses import dataclass
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.utils.s3_operations import S3Operation


@dataclass
class DataIngestionConfig:

    data_ingestion_artifacts_path: str = os.path.join("artifacts", "DataIngestionArtifacts")

    feature_store_file_path: str = os.path.join("artifacts", "DataIngestionArtifacts", "FeatureStore")

    zip_file_path: str = os.path.join("artifacts", "DataIngestionArtifacts", "Sign_language_data.zip")

    bucket_name: str = "sign-lang-23"

    bucket_file_name: str = "Sign_language_data.zip"



class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        self.s3_operations = S3Operation()


    def download_data(self, bucket_file_name: str, bucket_name: str, output_filepath: str)-> zip:
        """
        Fetch the data from the url
        
        """
        logging.info("Entered the get_data_from_s3 method of Data ingestion class")
        try:
            if not os.path.exists(output_filepath):
                self.s3_operations.read_data_from_s3(bucket_file_name,bucket_name,output_filepath)

            logging.info("Exited the get_data_from_s3 method of Data ingestion class")

        except Exception as e:
            raise SignException(e, sys)
        

    def extract_zip_file(self,zip_file_path: str)-> str:
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        try:
            feature_store_path = self.ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(feature_store_path)
            logging.info(f"Extracting zip file: {zip_file_path} into dir: {feature_store_path}")

            return feature_store_path

        except Exception as e:
            raise SignException(e, sys)
        

    def initiate_data_ingestion(self) -> str:
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")
        try:
            
            # Creating Data Ingestion Artifacts directory inside artifact folder
            os.makedirs(self.ingestion_config.data_ingestion_artifacts_path, exist_ok=True)
            logging.info(
                f"Created {os.path.basename(self.ingestion_config.data_ingestion_artifacts_path)} directory."
            )

            self.download_data(bucket_file_name=self.ingestion_config.bucket_file_name, bucket_name=self.ingestion_config.bucket_name, output_filepath=self.ingestion_config.zip_file_path)

            feature_store_path = self.extract_zip_file(zip_file_path=self.ingestion_config.zip_file_path)

            logging.info("Exited initiate_data_ingestion method of Data_Ingestion class")
            return feature_store_path

        except Exception as e:
            raise SignException(e, sys)