from src.DS_Project.logger import logging
from src.DS_Project.exception import CustomException
import sys
from src.DS_Project.components.data_ingestion import DataIngestion
from src.DS_Project.components.data_ingestion import DataIngestionConfig


# I imported the logging functionality that I just made to use here

# To use the logging functionality
if __name__ == "__main__":
    logging.info("The execution has started")

    # Using Custom Exception
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info('Custom Exception')
        raise CustomException(e , sys)