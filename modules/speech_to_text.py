import whisper

def transcribe_audio(video_path):
    model = whisper.load_model("base") # M1/M2라면 "base"도 충분히 빠릅니다
    result = model.transcribe(video_path)
    return result['segments'] # [{start, end, text}, ...] 형식 반환