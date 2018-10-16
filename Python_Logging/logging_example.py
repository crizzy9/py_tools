import logging

# using basicConfig
#FORMAT = '%(asctime)-15s [%(levelname)s] %(name)-8s %(message)s - %(appid)s'
#logging.basicConfig(level=logging.DEBUG, format=FORMAT)
#logging.info("what the shit", extra={'appid': 'lalala'})

# Using handlers
logger = logging.getLogger(__name__)

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)

c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

print(logger.getEffectiveLevel())

logger.debug('this is a debug')
logger.info('this is a info')
logger.warning('This is a warning')
logger.error('This is an error')
logger.critical('This is mission critical. Get Ready Boys')

# Other way
#logger = logging.getLogger()
#handler = logging.StreamHandler()
#formatter = logging.Formatter(
#        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
#handler.setFormatter(formatter)
#logger.addHandler(handler)
#logger.setLevel(logging.DEBUG)


logger.debug('often makes a very good meal of %s', 'visiting tourists')
