import sys
from signLanguage.exception import SignException
from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.components.data_validation import DataValidation
from signLanguage.components.model_trainer import ModelTrainer
from signLanguage.components.model_pusher import ModelPusher


class TrainPipeline:
    def __init__(self) -> None:

        self.data_ingestion = DataIngestion()

        self.data_validation = DataValidation()

        self.model_trainer = ModelTrainer()

        self.model_pusher = ModelPusher()


    def run_pipeline(self):
        try:
            self.data_ingestion.initiate_data_ingestion()

            self.data_validation.initiate_data_validation()

            self.model_trainer.initiate_model_trainer()

            self.model_pusher.initiate_model_pusher()


        except Exception as e:
            raise SignException(e, sys)