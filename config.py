import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# database 접속주소
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 이벤트 처리 옵션
SECRET_KEY = "dev"