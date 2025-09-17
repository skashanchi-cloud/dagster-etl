
from dagster import asset
from dagster import asset, get_dagster_logger

logger = get_dagster_logger()

@asset
def extract():
    return [1, 2, 3]

@asset
def transform(extract):
    return [x * 10 for x in extract]

@asset
def load(transform):
    logger.info(f"Loaded data: {transform}")

