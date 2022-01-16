import logging

# level = logging.[DEBUG | INFO | WARNING(default) | ERROR | CRITICAL]

logging.basicConfig(filename='example.log', 
                    format='%(name)s %(levelname)s %(funcName)s %(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    encoding='utf-8', 
                    level=logging.INFO)
# logging.getLogger().setLevel(logging.DEBUG
logging.warning('warning')
logging.debug('debug')

logging.debug('as')