import sys
from dataclasses import dataclass
from signLanguage.utils.s3_operations import S3Operation
from signLanguage.exception import SignException
from signLanguage.logger import logging


@dataclass
class ModelPusherConfig:

    trained_model_file_path = "yolov5/best.pt"

    bucket_name: str = "sign-lang-23"

    s3_model_key_path: str = "best.pt"


class ModelPusher:
    def __init__(self) -> None:
        self.pusher_config = ModelPusherConfig()
        self.s3_operation = S3Operation()

    def initiate_model_pusher(self):

        """
        Method Name :   initiate_model_pusher

        Description :   This method initiates model pusher. 
        
        """
        logging.info("Entered initiate_model_pusher method of ModelTrainer class")
        try:
            # Uploading the best model to s3 bucket
            self.s3_operation.upload_file(
                self.pusher_config.trained_model_file_path,
                self.pusher_config.s3_model_key_path,
                self.pusher_config.bucket_name,
                remove=False,
            )
            logging.info("Uploaded best model to s3 bucket")
            logging.info("Exited initiate_model_pusher method of ModelTrainer class")

        except Exception as e:
            raise SignException(e, sys) from e