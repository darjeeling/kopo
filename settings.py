class Config(object):
    """Default config"""
    DEBUG = True
    APP_SECRET_KEY = '1234567890'
    PO_STORAGE_PATH = "/Users/dj/po_path"

class ProductionConfig(Config):
    DEBUG = False
    APP_SECRET_KEY = ''
