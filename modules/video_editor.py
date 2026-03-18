import subprocess

def cut_video(input_video, start, end, output):

    command = [
        "ffmpeg",
        "-i", input_video,
        "-ss", str(start),
        "-to", str(end),
        "-c", "copy",
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
    