import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(parent_dir)

from app.blocks.section.datepicker import Datepicker
from app.blocks.Action.button import Button
from app.blocks.section.mrkdwn import MarkDown
from app.blocks.Divider.divider import Divder
from app.blocks.input.multiLine import multiLine
from app.blocks.input.staticSelect import Static_Select
from app.blocks.input.plain_text import Plain_text
from app.blocks.input.checkboxes import Checkboxes
from app.views.templates.elements import *
from app.views.Attachment.Attachment import *

## input
def create_staticSelect_json(label_text1,text1,action_id1,option_datas):
    staticSelect = Static_Select(label_text=label_text1,text=text1,action_id=action_id1,options_data=option_datas)
    return staticSelect.body

## aws 파이프라인
def create_aws_staticSelect_json(label_text1,text1,action_id1,options_datas):
    staticSelect = Static_Select(label_text=label_text1,text=text1,action_id=action_id1,options_data = options_datas)
    return staticSelect.body

## 깃랩 파이프라인
def create_gitlab_staticSelect_json(label_text1,text1,action_id1,option_datas):
    staticSelect = Static_Select(label_text=label_text1,text=text1,action_id=action_id1,options_data=option_datas)
    return staticSelect.body

def create_input_json(label,id,text1):
    inputLine = Plain_text(label_text=label,action_id=id,text=text1)
    return inputLine.body

def create_multiLine_json(label_text1,action_id1,text1):
    multiline = multiLine(label_text=label_text1,action_id=action_id1,text=text1)
    return multiline.body

def create_checkboxes_json(label,id,options):
    checkBoxes = Checkboxes(label_text = label,action_id=id, options_data=options)
    return checkBoxes.body

## not input
def create_markdown_json(msg):
    markDown = MarkDown(msg=msg)
    return markDown.body

def create_divider_json():
    divider = Divder()
    return divider.body

def create_datepicker_json(action_id,markdown_text):
    datepicker = Datepicker(action_id=action_id, markdown_text=markdown_text)
    return datepicker.body

def create_button_json(elements):
    button = Button(elements_data=elements)
    return button.body

## 입력값을 메시지 블록으로 추출 및 꾸미기
def format_input_values_message(title, applicant, input_values, blocks):
    values_lines = []
    values_lines.append(["Applicant",applicant])
    for action_id, value in input_values.items():
        label = None
        
        # `element`와 `action_id`가 있는 블록 찾기
        for block in blocks:
            if "element" in block and block["element"].get("action_id") == action_id:
                label = block["label"]["text"]
                break
        
        if label:
            values_lines.append([label, value])

    attachment = Attachment(*values_lines)

    option_blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"{title}\n{attachment.body[0]['text']}"
            }
        }
    ]
    return option_blocks