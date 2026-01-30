from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
import random
import os

def make_video(audio_path, script):
    bg_files = os.listdir("assets/bg_videos")
    bg = random.choice(bg_files)

    video = VideoFileClip(f"assets/bg_videos/{bg}").subclip(0, 20)
    audio = AudioFileClip(audio_path)

    txt = TextClip(
        script,
        fontsize=50,
        color='white',
        size=video.size,
        method='caption'
    ).set_duration(20)

    final = CompositeVideoClip([video, txt]).set_audio(audio)
    final.write_videofile("output.mp4", fps=24)

    return "output.mp4"
