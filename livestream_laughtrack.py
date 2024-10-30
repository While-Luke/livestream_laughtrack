import pytchat
import time
import os
from playsound import playsound

#https://www.soundfishing.eu/sound/group-laugh

chat = pytchat.create(video_id="qdczJpv8RCc")
print("Starting")

laugh_emotes = ["草の字", "草"]

num_chats = 0
num_laughs = 0
moving_average = 0
rate_factor = 0.8

while chat.is_alive():
    start = time.time()

    for c in chat.get().sync_items():
        if any(laugh in c.message for laugh in laugh_emotes):
            num_laughs += 1
        num_chats += 1
        #print(f"{c.datetime} [{c.author.name}]- {c.message}")

    if time.time() - start > 0.5:
        moving_average = rate_factor*num_laughs/num_chats + (1-rate_factor)*moving_average
        moving_average *= 0.95
        print(moving_average)

        if moving_average > 0.15:
            try:
                audio_file = os.path.dirname(__file__) + 'medium_laugh.mp3'
                playsound(audio_file, block = False)
            except:
                print("Error playing sound")

        num_chats = 0
        num_laughs = 0