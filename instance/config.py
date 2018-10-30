class BaseConfig:
    """Default configuration. Details from this configuration class are shared across all environments  """
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """Development configuraion. Loads development configuration data when the app is in the development environment"""
    DEBUG = True
    TESTING = False
    DATABASE_URL = 'postgres://postgres@localhost/store'
    
class TestingConfig(BaseConfig):
    """Testing configuraion. Loads Test configuration data when the app is in the Test environment"""
    DEBUG = True
    TESTING = True

class ProductionConfig(BaseConfig):
    """Production configuraion. Loads Production configuration data when the app is in the Production environment"""
    DEBUG = False
    TESTING = False

app_config = {
            "Development":DevelopmentConfig,
            "Testing":TestingConfig,
            "Production":ProductionConfig
            }