import sys
import os

# 1. 현재 파일(test_run.py)이 있는 위치를 파이썬 경로에 추가
current_path = os.path.dirname(os.path.abspath(__file__))
if current_path not in sys.path:
    sys.path.append(current_path)

# 2. 그 다음에 모듈을 불러옵니다.
from auto_editor import auto_edit

video_path = "test.mp4"
result = auto_edit(video_path)

print("결과 영상:", result)