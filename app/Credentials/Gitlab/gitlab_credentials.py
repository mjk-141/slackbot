import boto3
import os
import requests
import gitlab
from dotenv import load_dotenv

# 환경 변수 설정
load_dotenv(verbose=True)

GITLAB_URL = os.getenv("GITLAB_URL")
PRIVATE_TOKEN = os.getenv("GITLAB_TOKEN")

# GitLab 클라이언트 생성
gl = gitlab.Gitlab(GITLAB_URL, private_token=PRIVATE_TOKEN)

def get_all_projects_in_group(group_id):
        # 그룹 정보 가져오기
        group = gl.groups.get(group_id)
        
        # 하위 그룹과 프로젝트 목록 저장할 리스트
        projects_list = []

        # 그룹 내의 모든 프로젝트 가져오기
        projects = group.projects.list(all=True)
        for project in projects:
            projects_list.append(project)

        # 하위 그룹 가져오기
        subgroups = group.subgroups.list(all=True)
        for subgroup in subgroups:
            # 하위 그룹 내의 모든 프로젝트 가져오기
            sub_projects = get_all_projects_in_group(subgroup.id)
            projects_list.extend(sub_projects)

        return projects_list

def fetch_gitlab_repositories_options(group_id):
    projects = get_all_projects_in_group(group_id)
    options = [{'text': project.name, 'value': str(project.id)} for project in projects]
    return options


## 모든 그룹의 merge를 확인하기
def look_merge_request_in_Company(group_id):
    
    # 그룹 정보 가져오기
    group = gl.groups.get(group_id)
    
    ## 그룹에 대한 병합 요청을 나열
    mrs = group.mergerequests.list()
    
    return mrs