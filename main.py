from fetch_news import get_news
from make_script import make_script
from make_voice import make_voice
from make_video import make_video
from upload_instagram import upload_reel
import random, time

def random_delay():
    delay = random.randint(60, 1800)  # wait 1–30 min
    time.sleep(delay)

def run():
    random_delay()
    news = get_news()
    if not news:
        print("No new news found")
        return

    script = make_script(news)
    audio = make_voice(script)
    video = make_video(audio, script)
    upload_reel(video, script)

if __name__ == "__main__":
    run()
