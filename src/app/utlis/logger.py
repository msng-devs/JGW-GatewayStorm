import logging
from src.app.configs.config import settings


FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
if settings.CONFIG_NM == "local" or settings.CONFIG_NM == "test":
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

elif settings.CONFIG_NM == "product":
    logging.basicConfig(format=FORMAT, level=logging.INFO)

logger = logging.getLogger()