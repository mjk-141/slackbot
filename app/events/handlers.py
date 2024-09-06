import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(parent_dir)

from dotenv import load_dotenv
from slack_sdk import WebClient
from app.events.message_utils import *
from app.views.templates.all_templates import *
from app.events.input_handler import *
load_dotenv(verbose=True)

SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
CHANNEL_NAME = os.getenv('CHANNEL_NAME')

client = WebClient(token=SLACK_BOT_TOKEN)
channel = CHANNEL_NAME

## ACTION_ID
ACTION_ID = ["Pipeline","awsPipeline","GitlabPipeline","Repository","awsIam", 
             "awsIamPermission", "awsEC2", "awsS3", "awsELB", "Migration",
             "awsRDS", "awsElasticSearch", "awsParameterStore","inquiryEtc",
             "company_aws_pipeline", "company_gitlab_pipeline"]

## 깃랩과 AWS 회사 ID 모음집
AWS_COMPANY_ID = ["DGMONG","HAMALAB","CUBALTO","UMAY","WIKIFOKI", 
             "SINSA", "CMB", "SAFESCHOOL", "MANAGEON", "ION","PPNTALK"]

GITLAB_COMPANY_ID = ["203","199","88","58","46","45", "43", "2"]

GITLAB_COMPANY_DICT = {
    "PRONE": "203",
    "CARGOLAB": "199",
    "ION": "88",
    "SINSA": "58",
    "Dgmong": "46",
    "CUBALTO": "45",
    "CMB": "43",
    "HAMALAB": "2"
}

## AWS 파이프라인 선택창에서 레포가 어떤건지 가르켜주는 전역 변수
REPOSITORY = ["AWS","GITLAB"]

## 전역변수로 action_id in AWS_COMPANY_ID에서 action_id를 저장하는 용도로 사용됨
COMPANY_ID = None

def generate_blocks(action_id):
    global COMPANY_ID
    # 각 action_id에 대해 블록을 생성하는 로직을 구현
    if action_id == "awsIam":
        return awsIam()
    elif action_id == "awsIamPermission":
        return awsIamPermission()
    elif action_id == "awsEC2":
        return awsEC2()
    elif action_id == "awsS3":
        return awsS3()
    elif action_id == "awsELB":
        return awsELB()
    elif action_id == "awsRDS":
        return awsRDS()
    elif action_id == "Migration":
        return Migration()
    elif action_id == "awsElasticSearch":
        return awsElasticSearch()
    elif action_id == "awsParameterStore":
        return awsParameterStore()
    elif action_id == "inquiryEtc":
        return inquiryEtc()
    elif action_id == "Pipeline":
        return Pipeline()
    elif action_id =="Repository": ## 이건 그냥 생성
        return Repository()
    elif action_id =="company_aws_pipeline": ## 회사 목록
        return AWS_Company_List()
    elif action_id =="company_gitlab_pipeline": ## 회사 목록
        return Gitlab_Company_List()
    elif action_id in AWS_COMPANY_ID: ## 내부 파이프라인 생성
        COMPANY_ID = action_id
        return Select_Kinds_of_Repository()
    elif action_id in REPOSITORY: ## 어떤 레포 사용했는지 선택
        if action_id == "AWS":
            return awsPipeline(COMPANY_ID)
        else:
            if COMPANY_ID in GITLAB_COMPANY_DICT:
                value = GITLAB_COMPANY_DICT[COMPANY_ID]
                return awsPipeline(value)
            else:
                return not_Found_Repo()
    elif action_id in GITLAB_COMPANY_ID: ## 내부 파이프라인 생성
        return GitlabPipeline(action_id)

def handle_func(body, ack, client, logger):
    ack()
    channel_id = body["channel"]["id"]
    action_id = body["actions"][0]["action_id"]
    message_ts = body["container"]["message_ts"]
    
    blocks = generate_blocks(action_id)
    
    # 메시지 업데이트
    update_message(client, channel_id, message_ts, blocks, logger)

def register_handlers(app):
    for action in ACTION_ID: ## action 등록
        app.action(action)(handle_func)

    for action in AWS_COMPANY_ID: ## action 등록
        app.action(action)(handle_func)
        
    for action in GITLAB_COMPANY_ID: ## action 등록
        app.action(action)(handle_func)

    for action in REPOSITORY: ## action 등록
        app.action(action)(handle_func)

    ## 완료 버튼 구현
    @app.action("input")
    def handle_input(body, ack, client, logger):
        ack()
        channel_id = body["channel"]["id"]
        state_values = body["state"]["values"]
        message_ts = body["message"]["ts"]
        blocks = body["message"]["blocks"]
        user_id = body["user"]["id"]
        
        print(f'state_values : \n {state_values}')
        
        text = extract_mrkdwn_text(blocks[0])
        
        title = f"{text}"
        applicant = f"<@{user_id}>"
        
        # input 블록에서 입력값 추출
        input_values,errors = extract_input_values(state_values)
        
        multiline = has_multiline_input(state_values)

        # multiline 입력값이 없는 경우 처리
        if multiline == False:
            # 사용자에게 multiline 입력이 필요하다는 에러 메시지 전송
            client.chat_postEphemeral(
                channel=channel_id,
                user = user_id,
                thread_ts=message_ts,
                text="목적이 필요합니다. 목적을 입력해주세요."
            )
        elif errors:
            # 필수 입력값이 누락된 경우 에러 메시지 전송
            error_message = "\n".join(errors)
            client.chat_postEphemeral(
                channel=channel_id,
                user=user_id,
                thread_ts=message_ts,
                text=f"*[내용이 부족합니다]*\n{error_message}"
            )
        else:   
            # 메시지 업데이트 블록 생성
            option_blocks = format_input_values_message(title, applicant, input_values, blocks)
            
            # 메시지 업데이트 진행
            update_message(client, channel_id, message_ts, option_blocks, logger)
            
            # 알림 전달 기능 구현
            send_thread_notification(client, channel_id, message_ts, title, applicant, logger)
    
    def handle_back_generic(body, ack, client, logger, blocks_func):
        ack()
        channel_id = body["channel"]["id"]
        message_ts = body["message"]["ts"]
        blocks = blocks_func()
        update_message(client, channel_id, message_ts, blocks, logger)

    @app.action("back")
    def handle_back(body, ack, client, logger):
        handle_back_generic(body, ack, client, logger, first_view)

    @app.action("back_list")
    def handle_back_list(body, ack, client, logger):
        handle_back_generic(body, ack, client, logger, Pipeline)

    @app.action("back_aws_list")
    def handle_back_aws_list(body, ack, client, logger):
        handle_back_generic(body, ack, client, logger, AWS_Company_List)

    @app.action("back_gitlab_list")
    def handle_back_gitlab_list(body, ack, client, logger):
        handle_back_generic(body, ack, client, logger, Gitlab_Company_List)