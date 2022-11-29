import logging
from app.main import Setting


FORMAT: str = "%(levelname)s [%(asctime)s - %(name)s] :  %(message)s"
if(Setting.CONFIG_NM == "local" or Setting.CONFIG_NM == "test" ):
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
elif(Setting.CONFIG_NM == "product"):
    logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger()