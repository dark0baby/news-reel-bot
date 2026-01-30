import asyncio
import edge_tts

async def generate(text):
    communicate = edge_tts.Communicate(text, voice="en-IN-NeerjaNeural")
    await communicate.save("voice.mp3")

def make_voice(text):
    asyncio.run(generate(text))
    return "voice.mp3"
