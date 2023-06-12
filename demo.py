from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.components.data_validation import DataValidation


data_ingestion = DataIngestion()

data_ingestion.initiate_data_ingestion()


data_validation = DataValidation()

data_validation.initiate_data_validation()