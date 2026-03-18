import sys
import os

# 현재 app.py가 있는 폴더의 절대 경로를 계산해서 sys.path의 0번(최우선)에 넣습니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)




import streamlit as st
from auto_editor import auto_edit




st.set_page_config(page_title="AI 영상 편집기")

st.title("🎬 AI 자동 영상 편집기")

# 업로드
video = st.file_uploader("영상 파일 업로드", type=["mp4", "mov", "avi"])

if video:

    # uploads 폴더 없으면 생성
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    video_path = "uploads/input.mp4"

    with open(video_path, "wb") as f:
        f.write(video.read())

    st.video(video_path)

    if st.button("✨ 자동 편집 시작"):

        with st.spinner("AI가 영상 편집 중입니다..."):

            result = auto_edit(video_path)

        st.success("편집 완료!")

        st.video(result)

        with open(result, "rb") as file:
            st.download_button(
                label="📥 영상 다운로드",
                data=file,
                file_name="highlight.mp4"
            )
