import urllib.request
import numpy as np
import time
import os

from initialize.initialize_backend.initialize import initialize as init_backend
from backend.image.image import Image
from backend.model.model import MODEL


def start(token, backend, filename, MODEL_NAME, SIZE):
    bot = init_backend(token, backend)
    image = Image()
    if os.path.exists(os.path.join(os.getcwd(), '{}.meta'.format(MODEL_NAME))):
        MODEL.load(MODEL_NAME)

    print('Start')
    
    while True:
        messages = bot.get_unread_messages()
        if messages["count"] >= 1:
            id, message_id, body, url = bot.get_message_ids_image(messages)
            try:

                try:
                    image_url = bot.check_image_url(messages)
                except IndexError:
                    bot.send_message(id, "Пришлите картинку")
                    time.sleep(1)
                    continue

                urllib.request.urlretrieve(image_url, filename)

                data = image.prepare_image(filename, SIZE)

                outputs = MODEL.predict(data)
                label = np.argmax(outputs)
                image_class = 'кот/кошка' if label == 0 else 'собака'

                bot.send_message(id, f"Это {image_class}")
            except Exception as e:
                print(e)
                bot.send_message(id, f"Я вас не понимаю")

        time.sleep(1)
