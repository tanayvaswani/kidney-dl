from kidney_dl.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from kidney_dl import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e