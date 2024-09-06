import sys
import os
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(parent_dir)

# 환경 변수 설정
load_dotenv(verbose=True)

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from app.views.templates.elements import *
from app.views.templates.block_json import *

## 채널
CHANNEL_NAME = os.getenv('CHANNEL_NAME_DEV')

## 그룹 ID
Devops_groups = os.getenv('DEVOPS_GROUPS')

############################################### 메시지 업데이트 #####################################################
def update_message(client: WebClient, channel_id: str, message_ts: str, option_blocks,logger):
    try:
        client.chat_update(
            channel=channel_id,
            ts=message_ts,
            blocks= option_blocks
        )
    except SlackApiError as e:
        logger.error(f"Error updating message: {e.response['error']}")

################################################ 알림 전달 ########################################################
def send_thread_notification(client: WebClient, channel_id: str, thread_ts: str, title: str, applicant: str, logger):
    try:
        client.chat_postMessage(
            channel=channel_id,
            thread_ts=thread_ts,
            text=f"<!subteam^{Devops_groups}> {title} 요청이 있습니다.\n신청자: {applicant}"
        )
    except SlackApiError as e:
        logger.error(f"Error sending notification: {e.response['error']}")