import pytchat
from datetime import datetime 

chat = pytchat.create(video_id="")
print("Starting")

laugh_emotes = ["lol"]

num_chats = 0
num_laughs = 0
moving_average = 0
rate_factor = 0.5

while chat.is_alive():
    start = datetime.now()

    for c in chat.get().sync_items():
        if any(laugh in c.message for laugh in laugh_emotes):
            num_laughs += 1
        num_chats += 1
        #print(f"{c.datetime} [{c.author.name}]- {c.message}")

    if (datetime.now() - start).total_seconds() > 1:
        moving_average = rate_factor*num_laughs/num_chats + (1-rate_factor)*moving_average
        moving_average *= 0.9
        print(moving_average)

        num_chats = 0
        num_laughs = 0