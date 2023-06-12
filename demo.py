from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.components.data_validation import DataValidation
from signLanguage.components.model_trainer import ModelTrainer


data_ingestion = DataIngestion()

data_ingestion.initiate_data_ingestion()


data_validation = DataValidation()

data_validation.initiate_data_validation()


model_trainer = ModelTrainer()

model_trainer.initiate_model_trainer()


