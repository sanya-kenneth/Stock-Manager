import os

class BaseConfig:
    """Default configuration. Details from this configuration class are shared across all environments  """
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'postgres://postgres:psql@localhost:5432/store'
    SECRET = 'shdsjhdjsdjbcnxcxhusdsjkdjskdjsdjksjdsjbcbjxcjhsjdsjdhsjhdsjhdjshd'

class DevelopmentConfig(BaseConfig):
    """Development configuraion. Loads development configuration data when the app is in the development environment"""
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'postgres://postgres:psql@localhost:5432/store'
    ENV = 'Development'

class TestingConfig(BaseConfig):
    """Testing configuraion. Loads Test configuration data when the app is in the Test environment"""
    DEBUG = True
    TESTING = True
    DATABASE_URI = 'postgres://postgres:psql@localhost:5432/test_store'
    ENV = 'Testing'

class ProductionConfig(BaseConfig):
    """Production configuraion. Loads Production configuration data when the app is in the Production environment"""
    DEBUG = False
    TESTING = False
    ENV = 'Production'
    DATABASE_URI = 'postgres://nuqulvckxqqpdw:b3c27cd42143a3b75bac9bff94b673c914f5009bc22b9bb3ecd694ec7c924b7a@ec2-50-19-249-121.compute-1.amazonaws.com:5432/d8a8v4ger4cv7r'

app_config = {
            "Development":DevelopmentConfig,
            "Testing":TestingConfig,
            "Production":ProductionConfig
            }