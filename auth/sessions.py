from os import getenv
from boto3 import Session as Boto3Session


class CustomSession:

    def __init__(self):
        pass

    @staticmethod
    def aws_session() -> object:
        return Boto3Session(
            aws_access_key_id=getenv('ACCESS_KEY'),
            aws_secret_access_key=getenv('SECRET_KEY'),
            region_name=getenv('REGION')
        )
