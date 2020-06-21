from os import environ

MONGO_DBNAME = environ.get('MONGO_DBNAME', 'ImageClassifierDB')
MONGO_URI = environ.get('MONGO_URI', 'mongodb://127.0.0.1:27017/ImageClassifierDB')