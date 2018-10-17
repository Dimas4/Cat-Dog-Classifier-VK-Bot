from backend.generate_instance import generate_instance


class VkBot:
    def __init__(self, token):
        self.token = token
        self.vk, self.vk_upload = generate_instance(token)

    def get_unread_messages(self, offset=0, count=20):
        return self.vk.method("messages.getConversations", {"offset": offset, "count": count, "filter": "unread"})

    def send_message(self, id, message=None, attach=None):
        attach = 'doc%s_%s' % (attach['owner_id'], attach['id']) if attach else None
        data = {"peer_id": id, "message": message, 'attachment': attach}
        self.vk.method("messages.send", data)

    @staticmethod
    def check_image_url(messages):
        return messages["items"][0]["last_message"]["attachments"][0]['photo']['sizes'][0]['url']

    @staticmethod
    def get_message_ids_image(messages):
        file = messages["items"][0]["last_message"]['attachments']
        url = None
        if file and file[0].get('photo'):
            url = file[0]['photo']['sizes'][2]['url']
        return messages["items"][0]["last_message"]["from_id"], \
               messages["items"][0]["last_message"]["id"], \
               messages["items"][0]["last_message"]["text"], url
