import random
import vk_api
import schedule
import time
from vk_api.longpoll import VkLongPoll

token = ''
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

def job():
    print("Отправлено")
    vk.messages.send(
        chat_id='1',
        random_id=random.randint(1, 10000),
        message='msg'
    )

schedule.every(random.randint(8, 13)).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
