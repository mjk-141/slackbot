### 이제 돌고돌아 니가 문제구나 tablutate
## 으니 하나 break하면 어나더 코드가 break하는 대단한 프로그래밍 세상
## 즐겁다 하하하
from tabulate import tabulate

class Attachment:
    def __init__(
        self,
        *args: list,
        color: str = "#36a64f",
    ) -> None:
        self.matrix = [arg for arg in args]
        self.body = [dict(color=color, text=f"```{self.to_table(self.matrix)}```")]

    def to_table(self, data):
        # None 값을 빈 문자열로 처리하고, 모든 값을 문자열로 변환합니다.
        processed_data = [(label, str(value) if value is not None else '') for label, value in data]
        
        # 각 라벨과 값의 최대 길이를 찾습니다.
        max_label_length = max(len(label) for label, _ in processed_data)
        max_value_length = max(len(value) for _, value in processed_data)
        
        lines = []
        for label, value in processed_data:
            # 라벨과 값의 문자열을 '|' 문자를 기준으로 정렬합니다.
            label_formatted = label.ljust(max_label_length)
            lines.append(f"{label_formatted} | {value}")
        return "\n".join(lines)

    @property
    def dict(self):
        return self.body