import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
from events.handlers import register_handlers
from Credentials.Gitlab.gitlab_credentials import *
from views.templates.all_templates import first_view
import logging

# 환경 변수 설정
load_dotenv(verbose=True)

SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
CHANNEL_NAME = os.getenv('CHANNEL_NAME_PROD')
SLACK_APP_TOKEN = os.getenv('SLACK_APP_TOKEN')

logging.basicConfig(level=logging.DEBUG)

app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)

# 핸들러 등록
register_handlers(app)

# 초기 화면 도출을 위한 help-devops
@app.command("/help-devops")
def handle_some_action(body, ack, respond, client):
    ack()
    channel = CHANNEL_NAME
    user_id = body["user_id"]

    try:
        # 명령어를 수행했음을 응답하고 메시지 전송
        response = client.chat_postMessage(
            channel=channel,
            text=f":clipboard: 요청서가 생성되었습니다."
        )
        
        # 전송된 메시지를 스레드로 식별하기 위한 thread_ts 얻기
        thread_ts = response["ts"]
        
        # 스레드 내에 메시지 전송
        client.chat_postMessage(
            channel=channel,
            thread_ts=thread_ts,
            blocks=first_view()
        )

    except Exception as e:
        respond(f"Failed to send message: {e}")

# Flask 서버 실행(포트 필요 없다.)
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()