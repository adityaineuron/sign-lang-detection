import os,sys
import shutil
from dataclasses import dataclass
from signLanguage.logger import logging
from signLanguage.exception import SignException



@dataclass
class DataValidationConfig:

    data_validation_artifacts_path: str = os.path.join("artifacts", "DataValidationArtifacts")

    valid_status_file: str = os.path.join("artifacts", "DataValidationArtifacts", "status.txt")

    feature_store_file_path: str = os.path.join("artifacts", "DataIngestionArtifacts", "FeatureStore")

    required_file_list = ["train", "test", "data.yaml"]

    zip_file_path: str = os.path.join("artifacts", "DataIngestionArtifacts", "Sign_language_data.zip")


class DataValidation:
    def __init__(self) -> None:
        self.validation_config = DataValidationConfig()


    def validate_all_files_exist(self)-> bool:
        logging.info("Entered validate_all_files_exist method of DataValidation class")
        try:
            validation_status = None

            all_files = os.listdir(self.validation_config.feature_store_file_path)

            for file in all_files:
                if file not in self.validation_config.required_file_list:
                    validation_status = False
                    os.makedirs(self.validation_config.data_validation_artifacts_path, exist_ok=True)
                    with open(self.validation_config.valid_status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    os.makedirs(self.validation_config.data_validation_artifacts_path, exist_ok=True)
                    with open(self.validation_config.valid_status_file, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            logging.info("Exited validate_all_files_exist method of DataValidation class")
            return validation_status

        except Exception as e:
            raise SignException(e, sys)  
        

    def initiate_data_validation(self) -> None: 
        logging.info("Entered initiate_data_validation method of DataValidation class")
        try:
            status = self.validate_all_files_exist()

            logging.info("Exited initiate_data_validation method of DataValidation class")

            if status:
                shutil.copy(self.validation_config.zip_file_path, os.getcwd())

        except Exception as e:
            raise SignException(e, sys)
