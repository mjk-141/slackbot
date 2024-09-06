import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(parent_dir)

from app.views.templates.block_json import * 

########################################################## 초기 화면 템플릿 ######################################################
def first_view():
    blocks = [
        create_markdown_json(":computer:*필요한 서비스를 클릭해주세요*"),
        create_divider_json(),
        create_markdown_json(":lower_left_fountain_pen: *CI/CD 서비스*"),
        create_divider_json(),
        create_button_json(elements1),
        create_markdown_json(":pencil: *기타 서비스*"),
        create_divider_json(),
        create_button_json(elements2),
        create_button_json(elements3),
        create_button_json(elements4),
        create_button_json(elements5),
        create_markdown_json(":thumbs_up_crying_cat: *기타 문의 사항*"),
        create_divider_json(),
        create_button_json(elements6)
    ]
    return blocks

########################################################## CI/CD 템플릿 ######################################################

def Pipeline(): ## 회사로 넘어 간다.
    blocks = [
        create_button_json(elements7),
        create_button_json(back)
    ]
    return blocks

def AWS_Company_List():
    blocks = [
        create_markdown_json(f":clipboard: *어떤 서비스인가요?*"),
        create_button_json(company_aws_pipeline),
        create_button_json(back_button)
    ]
    return blocks

## AWS pipeline에만 해당
def Select_Kinds_of_Repository():
    blocks = [
        create_markdown_json(f":clipboard: *어떤 Repository를 사용하십니까?*"),
        create_button_json(select_Kinds_of_Repository),
        create_button_json(back_aws_button)
    ]
    return blocks

def not_Found_Repo():
    blocks = [
        create_markdown_json(f"*해당 프로젝트 Repo는 깃랩에 없습니다."),
        create_button_json(back_aws_button)
    ]
    return blocks

def Gitlab_Company_List():
    blocks = [
        create_markdown_json(f":clipboard: *어떤 서비스인가요?*"),
        create_button_json(company_gitlab_pipeline),
        create_button_json(back_button)
    ]
    return blocks


def awsPipeline(action_id):
    GITLAB_COMPANY_ID = ["203","199","88","58","46","45", "43", "2"]
    text = None
    if action_id in GITLAB_COMPANY_ID:
        if action_id == "203":
            text = "PRONE"
        elif action_id == "199":
            text = "CARGOLAB"
        elif action_id == "88":
            text = "ION"
        elif action_id == "58":
            text = "SINSA"
        elif action_id == "46":
            text = "Dgmong"
        elif action_id == "45":
            text = "CUBALTO"
        elif action_id == "43":
            text = "CMB"
        elif action_id == "2":
            text = "HAMALAB"
    else:
        text=action_id
    blocks = [
        create_markdown_json(f":clipboard: *[신규,{text}] AWS PipeLine 생성*"),
        create_aws_staticSelect_json("Select repository","select a repository","Repository",action_id),
        create_staticSelect_json("Select Branch","select a Branch","Branch",branch),
        create_checkboxes_json("Stages","Stages",stages),
        create_input_json("Deploy Folder","DeployFolder","배포 폴더"),
        create_input_json("Deploy URL","DeployURL","배포 도메인"),
        create_multiLine_json("Purpose","Purpose","목적을 꼭 입력하세요!"),
        create_button_json(input_back_aws_button)
    ]
    return blocks

def GitlabPipeline(action_id):
    GITLAB_COMPANY_ID = ["203","199","88","58","46","45", "43", "2"]
    text = None
    if action_id in GITLAB_COMPANY_ID:
        if action_id == "203":
            text = "PRONE"
        elif action_id == "199":
            text = "CARGOLAB"
        elif action_id == "88":
            text = "ION"
        elif action_id == "58":
            text = "SINSA"
        elif action_id == "46":
            text = "Dgmong"
        elif action_id == "45":
            text = "CUBALTO"
        elif action_id == "43":
            text = "CMB"
        elif action_id == "2":
            text = "HAMALAB"
    blocks = [
        create_markdown_json(f":clipboard: *[신규,{text}] Gitlab PipeLine 생성*"),
        create_gitlab_staticSelect_json("Select repository","select a repository","Repository",action_id),
        create_staticSelect_json("Select Branch","select a Branch","Branch",branch),
        create_input_json("Deploy Folder","DeployFolder","배포 폴더"),
        create_input_json("Deploy URL","DeployURL","배포 도메인"),
        create_multiLine_json("Purpose","Purpose","목적을 꼭 입력하세요!"),
        create_button_json(input_back_gitlab_button)
    ]
    return blocks

def Repository():
    blocks = [
        create_markdown_json(":clipboard: *[신규] Repository 생성*"),
        create_staticSelect_json("Project","Select a Project","Project",Project),
        create_input_json("Repository Name","Repository","[서비스]-[언어]-[역할] 형식으로 작성"),
        create_multiLine_json("Purpose","Purpose","목적을 꼭 입력하세요!"),
        create_button_json(input_back_button)
    ]
    return blocks

########################################################### 기타 서비스 #######################################################

## IAM 계정 생성
def awsIam():
    blocks = [
        create_markdown_json(":clipboard: *[신규] IAM 계정 생성*"),
        create_staticSelect_json("Project","Select a Project","Project",Project),
        create_input_json("Email","Email","adadas@hamagroups.io"),
        create_staticSelect_json("Department","select department","input",departments),
        create_multiLine_json("Purpose","Purpose","목적을 꼭 입력하세요!"),
        create_button_json(input_back_button)
    ]
    return blocks

## IAM 권한 부여
def awsIamPermission(): 
    blocks = [
        create_markdown_json(":clipboard: *[IAM] 계정 권한 요청*"),
        create_staticSelect_json("Project","Select a Project","Project",Project),
        create_input_json("Email","Email","adadas@hamagroups.io"),
        create_input_json("Service","Service","ex) EC2, S3..."),
        create_input_json("Permission","Permission","ex) s3 객체 확인 및 다운로드 권한"),
        create_multiLine_json("Purpose","Purpose","목적을 꼭 입력하세요!"),
        create_button_json(input_back_button)
    ]
    return blocks

## EC2 생성 요청
def awsEC2():
    blocks = [
        create_markdown_json(":clipboard: *[신규] EC2 인스턴스 생성 요청*"),
        create_staticSelect_json("Project","Select a Project","Project",Project),
        create_staticSelect_json("Usage","Select a type","usage",usage),
        create_staticSelect_json("OS/dist","Select OS/dist","OS",operatingSystem),
        create_input_json("instance specification","specification","ex) t3.medium"),
        create_checkboxes_json("Make Other Region","Region",OX),
        create_checkboxes_json("Make Session Manager","SSM",OX),
        create_checkboxes_json("Elastic IP","Elastic",OX),
        create_checkboxes_json("Auto Scaling Group","Auto",OX),
        create_input_json("Storage","Storage","ex) 64GB"),
        create_multiLine_json("Purpose","Purpose","목적을 꼭 입력하세요!"),
        create_button_json(input_back_button)
    ]
    return blocks

def awsS3():
    blocks = [
        create_markdown_json(":clipboard: *[신규] S3 버킷 생성 요청*"),
        create_staticSelect_json("Project","Select a Project","Project",Project),
        create_input_json("Bucket","Bucket","버킷명 입력"),
        create_multiLine_json("Purpose","Purpose","목적을 꼭 입력하세요!"),
        create_button_json(input_back_button)
    ]
    return blocks

def awsELB():
    blocks = [
        create_markdown_json(":clipboard: *[신규] 로드밸런서 신규 요청*"),
        create_staticSelect_json("Project","Select a Project","Project",Project),
        create_input_json("Domain","Domain","도메인명 입력"),
        create_multiLine_json("Purpose","Purpose","목적을 꼭 입력하세요!"),
        create_button_json(input_back_button)
    ]
    return blocks

def awsRDS():
    blocks = [
        create_markdown_json(":clipboard: *[신규] RDS 생성 요청*"),
        create_staticSelect_json("Project","Select a Project","Project",Project),
        create_staticSelect_json("DB engine","Select a Engine","dbEngine",dbEngine),
        create_checkboxes_json("Multi A-Z","multiAZ",OX), 
        create_multiLine_json("Purpose","Purpose","목적을 꼭 입력하세요!"),
        create_button_json(input_back_button)
    ]
    return blocks

def awsElasticSearch():
    blocks = [
        create_markdown_json(":clipboard: *[신규] 엘라스틱 생성 요청*"),
        create_staticSelect_json("Project","Select a Project","Project",Project),
        create_staticSelect_json("Opensearch Engine","Select a Engine","opensearchEngine",opensearchEngine),
        create_multiLine_json("Purpose","Purpose","목적을 꼭 입력하세요!"),
        create_button_json(input_back_button)
    ]
    return blocks

def Migration():
    blocks = [
        create_markdown_json(":clipboard: *[신규] 마이그레이션 요청*"),
        create_staticSelect_json("Project","Select a Project","Project",Project),
        create_staticSelect_json("service","Select a service","service",migration_service),
        create_multiLine_json("Purpose","Purpose","목적을 꼭 입력하세요!"),
        create_button_json(input_back_button)
    ]
    return blocks

def awsParameterStore():
    blocks = [
        create_markdown_json(":clipboard: *[신규] 파라미터 스토어 요청*"),
        create_staticSelect_json("Project","Select a Project","Project",Project),
        create_input_json("Name","Name","Name 입력"), 
        create_multiLine_json("Purpose","Purpose","목적을 꼭 입력하세요!"),
        create_button_json(input_back_button)
    ]
    return blocks

def inquiryEtc():
    blocks = [
        create_markdown_json(":clipboard: *[기타] 문의사항*"),
        create_staticSelect_json("Project","Select a Project","Project",Project),
        create_multiLine_json("inquiry","inquiry","문의사항을 꼭 입력하세요!"),
        create_button_json(input_back_button)
    ]
    return blocks