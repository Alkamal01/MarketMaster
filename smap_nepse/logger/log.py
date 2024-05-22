import os
import json
import logging.config

__author__ = "Aliyu Kamal"
__copyright__ = ""
__credits__ = ["Semanta Bhandari","Sameer Rai","Sumit Shrestha","Sankalpa Timilsina"]
__license__ = ""
__version__ = "0.1"
__email__ = "kamalaliyu212@gmail.com"

def setup_logging(
    default_path='logging.json', 
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration
    
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

if __name__== '__main__':
    setup_logging()
    logger = logging.getLogger()
    logger.info('checking info ::abc')
    logger.error('checking error::error goes here')

