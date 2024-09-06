import os
import boto3
from dotenv import load_dotenv

# 환경 변수 설정
load_dotenv(verbose=True)

def fetch_aws_repositories(options_data):
    
    session = boto3.Session(
        aws_access_key_id=os.getenv(f'{options_data}_AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv(f'{options_data}_AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv(f'AWS_DEFAULT_REGION')
    )
    
    codecommit_client = session.client('codecommit')
    response = codecommit_client.list_repositories()
    
    repositories = response['repositories']
    
    options = [{'text': repo['repositoryName'], 'value': repo['repositoryName']} for repo in repositories]
    
    return options