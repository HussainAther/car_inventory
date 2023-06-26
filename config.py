# Configuration settings for the Car Collection API

# Development Configuration
class DevelopmentConfig:
    DEBUG = True
    SECRET_KEY = 'your-secret-key'
    DATABASE_URI = 'sqlite:///dev_database.db'
    ALLOW_REGISTRATION = True
    FEATURE_FLAG = 'beta'
    # Add other configuration variables as needed

# Production Configuration
class ProductionConfig:
    DEBUG = False
    SECRET_KEY = 'your-secret-key'
    DATABASE_URI = 'postgresql://user:password@localhost:5432/prod_database'
    ALLOW_REGISTRATION = False
    FEATURE_FLAG = 'stable'
    # Add other configuration variables as needed

# Select the appropriate configuration based on the environment
# Change 'DevelopmentConfig' to 'ProductionConfig' when deploying to production
config = DevelopmentConfig

