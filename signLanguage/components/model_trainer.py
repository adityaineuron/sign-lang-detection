import os,sys
import yaml
from dataclasses import dataclass
from signLanguage.utils.main_utils import read_yaml_file
from signLanguage.logger import logging
from signLanguage.exception import SignException


@dataclass
class ModelTrainerConfig:

    model_trainer_artifacts_path: str = os.path.join("artifacts", "ModelTrainerArtifacts")

    weight_name: str = "yolov5s.pt"

    no_epochs: int = 10

    batch_size: int = 16


class ModelTrainer:
    def __init__(self) -> None:
        self.trainer_config = ModelTrainerConfig()


    def initiate_model_trainer(self,):
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")
            os.system("unzip Sign_language_data.zip")

            with open("artifacts/DataIngestionArtifacts/FeatureStore/data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])
            
            model_config_file_name = self.trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")

            config['nc'] = int(num_classes)

            with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)


            os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.trainer_config.batch_size} --epochs {self.trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.trainer_config.weight_name} --name yolov5s_results  --cache")
            os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
            os.makedirs(self.trainer_config.model_trainer_artifacts_path, exist_ok=True)
            os.system(f"cp yolov5/runs/train/yolov5s_results/weights/best.pt {self.trainer_config.model_trainer_artifacts_path}/")

            os.system("rm -rf yolov5/runs")

            os.system("rm -rf train")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")

            trained_model_file_path = "yolov5/best.pt",

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            return trained_model_file_path

        except Exception as e:
            raise SignException(e, sys)