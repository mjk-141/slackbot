# def extract_input_values(state_values):
#     input_values = {}

#     for block_data in state_values.values():
#         for action_id, action_data in block_data.items():
#             input_type = action_data["type"]
#             if input_type == "plain_text_input":
#                 if action_data.get("multiline", False):
#                     input_values[action_id] = action_data["value"]
#                 else:
#                     input_values[action_id] = action_data["value"]
#             elif input_type == "static_select":
#                 input_values[action_id] = action_data["selected_option"]["text"]["text"]
#             elif input_type == "checkboxes":
#                 selected_options = action_data["selected_options"]
#                 input_values[action_id] = ", ".join(option["text"]["text"] for option in selected_options)
#     return input_values



# def log_input_values(input_values, blocks, logger):
#     for action_id, value in input_values.items():
#         label = next(block["label"]["text"] for block in blocks if block["element"]["action_id"] == action_id)
#         logger.info(f"{label}: {value}")


        
def extract_input_values(state_values):
    input_values = {}
    errors = []
    error_flags = {
        "static_select": False,
        "checkboxes": False
    }
    
    for block_data in state_values.values():
        for action_id, action_data in block_data.items():
            input_type = action_data["type"]
            if input_type == "plain_text_input":
                if action_data.get("multiline", False):
                    input_values[action_id] = action_data["value"]
                else:
                    input_values[action_id] = action_data["value"]
            elif input_type == "static_select":
                selected_option = action_data.get("selected_option")
                if selected_option:
                    input_values[action_id] = selected_option["text"]["text"]
                else:
                    if not error_flags["static_select"]:
                        errors.append("선택해야 하는 항목이 있습니다!")
                        error_flags["static_select"] = True
            elif input_type == "checkboxes":
                selected_options = action_data["selected_options"]
                if selected_options:
                    input_values[action_id] = ", ".join(option["text"]["text"] for option in selected_options)
                else:
                    if not error_flags["checkboxes"]:
                        errors.append("체크박스에서 선택해야 하는 항목이 있습니다!")
                        error_flags["checkboxes"] = True

    return input_values, errors


def extract_mrkdwn_text(block):
    text = ""

    if block["type"] == "section" and "text" in block:
        text_block = block["text"]
        if text_block["type"] == "mrkdwn":
            text = text_block["text"]
    
    return text

## 목적값이 있는지 여부 확인
## 너 떔에 내가 이고생을...
## 쿠버네티스 강좌 듣다가 이게 머니...
## 너떔에 흥 다깨졌잖아 책임져! 슬랙!
def has_multiline_input(state_values):
    for block_data in state_values.values():
        for action_id, action_data in block_data.items():
            if action_id == 'Purpose' or action_id == 'inquiry':
                return bool(action_data.get('value'))
    return False