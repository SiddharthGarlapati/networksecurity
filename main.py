from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig


import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Intiate the data ingestion ")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation is completed")
        print(dataingestionartifact)
        datavalidationconfig = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("Initiate the data validation")
        datavalidationartifact = data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(datavalidationartifact)
        datatransformationconfig = DataTransformationConfig(trainingpipelineconfig)
        logging.info("Data transformation started")
        data_transformation = DataTransformation(datavalidationartifact,datatransformationconfig)
        datatransformationartifact = data_transformation.initiate_data_transformation()
        print(datatransformationartifact)
        logging.info("Data transformation completed ")
        modeltrainerconfig = ModelTrainerConfig(trainingpipelineconfig)
        logging.info(" Model Trainer started")
        modeltrainer = ModelTrainer(datatransformationartifact,modeltrainerconfig)
        modeltrainerartifact = modeltrainer.initiate_model_trainer()
        print(modeltrainerartifact)
        logging.info("Model Trainer completed ")


        
    except Exception as e:
        raise NetworkSecurityException(e,sys)

