import logging

logger = logging.getLogger(__name__)

def my_function():
    logger.debug('this dubug')
    logger.info('this info')
    logger.warning('this warning')
    logger.error('this error')
    logger.critical('this critical')