import os
import sys
import streamlit as st


# 예외 처리(try-except)도 우선 지워서 순수하게 부릅니다.
from modules.audio_extractor import extract_audio
from modules.speech_to_text import transcribe
from modules.highlight_detector import detect_highlights
from modules.video_editor import cut_video, merge_videos


def auto_edit(video_path):

    audio_path = "audio.wav"

    print("1. 오디오 추출 중...")
    extract_audio(video_path, audio_path)

    print("2. 자막 생성 중...")
    segments = transcribe(audio_path)

    print("3. 하이라이트 탐지 중...")
    # 수정 1: video_path와 segments 두 개를 모두 넘겨줍니다.
    highlights = detect_highlights(video_path, segments) 

    clips = []

    print("4. 영상 자르는 중...")
    # 수정 2: 딕셔너리 형태에 맞게 데이터를 안전하게 꺼내옵니다.
    for i, highlight in enumerate(highlights):
        start = highlight['start']
        end = highlight['end']
        text = highlight['text']

        output = f"clip_{i}.mp4"
        cut_video(video_path, start, end, text, output)
        clips.append(output)

    print("5. 영상 합치는 중...")
    
    # 안전하게 outputs 폴더 만들기
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
        
    final_video = "outputs/highlight.mp4"
    merge_videos(clips, final_video)
    
    print("완료!")
    return final_video