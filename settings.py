class BaseConfig(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class ProdConfig(BaseConfig):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevConfig(BaseConfig):
    DEBUG = True
    SERVER_NAME = '127.0.0.1:8765'

class TestConfig(BaseConfig):
    TESTING = True

configs = {
    'dev'  : DevConfig,
    'test' : TestConfig,
    'prod' : ProdConfig,
    'default' : BaseConfig
}
