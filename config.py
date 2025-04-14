import os
import datetime

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    # JWT Configs
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_COOKIE_PATH = '/'
    JWT_REFRESH_COOKIE_PATH = '/auth/refresh'
    JWT_COOKIE_CSRF_PROTECT = False 
    JWT_COOKIE_SECURE = False
    JWT_SESSION_COOKIE = False
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 60  # 1 hour
    JWT_REFRESH_TOKEN_EXPIRES = 30 * 24 * 60 * 60  # 30 days