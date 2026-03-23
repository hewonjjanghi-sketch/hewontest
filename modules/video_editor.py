import subprocess

def create_simple_srt(text, duration, srt_path="temp.srt"):
    """하나의 클립을 위한 1줄짜리 임시 자막 파일을 만듭니다."""
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int(duration % 60)
    millis = int((duration - int(duration)) * 1000)
    end_time_str = f"{hours:02}:{minutes:02}:{seconds:02},{millis:03}"
    
    # 0초부터 클립의 끝(duration)까지 텍스트를 띄웁니다.
    srt_content = f"1\n00:00:00,000 --> {end_time_str}\n{text}\n"
    
    with open(srt_path, "w", encoding="utf-8") as f:
        f.write(srt_content)
    return srt_path

def cut_video(input_video, start, end, text, output):
    duration = end - start
    srt_file = create_simple_srt(text, duration, "temp.srt")

    command = [
        "ffmpeg", "-y",
        "-i", input_video,
        "-ss", str(start),
        "-to", str(end),
        "-vf", f"subtitles={srt_file}",
        "-c:v", "libx264",
        "-c:a", "copy",
        output
    ]

    subprocess.run(command)

def merge_videos(video_list, output):

    with open("list.txt", "w") as f:
        for video in video_list:
            f.write(f"file '{video}'\n")

    command = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", "list.txt",
        "-c", "copy",
        output
    ]

    subprocess.run(command)
    