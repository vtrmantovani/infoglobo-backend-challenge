import logging
import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False

    LOGS_LEVEL = logging.INFO
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JSON_AS_ASCII = False
    FEED_URL = os.environ.get('FEED_URL', '')
    FEED_TIMEOUT = os.environ.get('FEED_TIMEOUT', 30)


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOGS_LEVEL = logging.DEBUG
    SECRET_KEY = 'b21032d50cbf2bbfe56a'
    FEED_URL = 'http://revistaautoesporte.globo.com/rss/ultimas/feed.xml'


class StagingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass
