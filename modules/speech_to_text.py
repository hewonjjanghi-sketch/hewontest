import whisper
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def transcribe(audio_path):
    model = whisper.load_model("base") # M1/M2라면 "base"도 충분히 빠릅니다
    result = model.transcribe(audio_path)
    return result['segments'] # [{start, end, text}, ...] 형식 반환