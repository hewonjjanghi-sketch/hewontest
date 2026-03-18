import ffmpeg
import os

def extract_audio(video_path, output_path="audio.wav"):
    try:
        # 기존 파일 삭제 (덮어쓰기 문제 방지)
        if os.path.exists(output_path):
            os.remove(output_path)

        # ffmpeg 실행 (오디오만 추출)
        (
            ffmpeg
            .input(video_path)
            .output(output_path, format='wav', acodec='pcm_s16le', ac=1, ar='16000')
            .run(quiet=True)
        )

        print(f"✅ 오디오 추출 완료: {output_path}")
        return output_path

    except ffmpeg.Error as e:
        print("❌ FFmpeg 오류 발생")
        print(e.stderr.decode())
        return None

    except Exception as e:
        print("❌ 일반 오류 발생:", str(e))
        return None