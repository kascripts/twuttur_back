import os

db_URI = os.getenv('DATABASE_URL', 'postgresql://localhost:5432/tweets_db')
secret = os.getenv('SECRET', 'Hereisfantasticscretn123')

