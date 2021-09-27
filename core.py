from pyrogram import Client, filters
from decouple import config
import time

API_ID = config('API_ID')
API_HASH = config('API_HASH')
PHONE_NUMBER = config('PHONE_NUMBER')
SESSION_NAME = config('SESSION_NAME', default = 'cestoda')
CHAT_NAMES_FOR_FEED = config('CHAT_NAMES_FOR_FEED').split('/')
CHAT_WORDS_TO_FILTER = config('CHAT_WORDS_TO_FILTER', default = '').split('/')
FEED_CHAT_ID = config('FEED_CHAT_ID')

app = Client(
  session_name=SESSION_NAME,
  api_id=API_ID,
  api_hash=API_HASH,
  phone_number=PHONE_NUMBER
)

def word_from_list_exists_in_string(string, list):
  if not ' ' in string: return None

  # TODO: shitcode. that should be way-way more better. Probably .sub or smth regexp based would work but i didnt try it
  words = string.replace(".", " ").replace(",", " ").replace(":", " ").replace(";", " ").replace("/", " ").lower().split(" ")
  for word in words:
    if word in list:
      return word

@app.on_message(filters.text & filters.channel)
def callback(client, message):
  chat = message.chat
  message_text = message.text

  if chat.username in CHAT_NAMES_FOR_FEED:
    client.read_history(chat.id, message.message_id)

    message_contains_word = word_from_list_exists_in_string(message_text, CHAT_WORDS_TO_FILTER)

    if not message_contains_word:
      client.send_message(
        chat_id=FEED_CHAT_ID,
        text=message_text,
        disable_notification=True
      )
    else:
      print("msg contained word: ", message_contains_word)
  else:
    # username or chat id
    print("filtered: ", message.chat.username)

  time.sleep(0.2)


if __name__ == '__main__':
  app.run()
