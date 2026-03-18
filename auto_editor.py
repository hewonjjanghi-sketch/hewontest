import sys
import os

# 1. 현재 파일(auto_editor.py)의 절대 경로를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 이 경로를 검색 리스트 맨 앞에 추가합니다.
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# 3. 이제 'modules.파일명'으로 불러옵니다.
from modules.audio_extractor import extract_audio
from modules.speech_to_text import transcribe
from modules.highlight_detector import detect_highlights
from modules.video_editor import cut_video, merge_videos

import streamlit as st

def auto_edit(video_path):

    audio_path = "audio.wav"

    print("1. 오디오 추출 중...")
    extract_audio(video_path, audio_path)

    print("2. 자막 생성 중...")
    segments = transcribe(audio_path)

    print("3. 하이라이트 탐지 중...")
    highlights = detect_highlights(segments)

    clips = []

    print("4. 영상 자르는 중...")
    for i, (start, end) in enumerate(highlights):
        output = f"clip_{i}.mp4"
        cut_video(video_path, start, end, output)
        clips.append(output)

    print("5. 영상 합치는 중...")
    final_video = "outputs/highlight.mp4"
    merge_videos(clips, final_video)

    print("완료!")
    return final_video