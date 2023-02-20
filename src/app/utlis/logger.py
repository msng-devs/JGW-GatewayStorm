import logging
from app.configs.config import settings


FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

if settings.CONFIG_NM == "local" or settings.CONFIG_NM == "test":
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

elif settings.CONFIG_NM == "product":
    logging.basicConfig(format=FORMAT, level=logging.INFO)

logger = logging.getLogger()