import random
import vk_api
import schedule
import time
from vk_api.longpoll import VkLongPoll

token = 'vk1.a.i8QkOGMxgBk06rMQOuN3Hpv99bGZvumIWAyA0gfzxC7IrpWtXbnIsrtmz-HMpGvTbO3EwnmX5DVYiDPG0KJA6eoEUWgi-j-40MDyNI7Q8V6vi3bPURcfOP2rr-Y87g7KO0og9zkib_Og0MEJnjITuPyQmxiiuFAcCNdb5jt0LcSvIV1cvmFb0x_Br09tAASU'
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

def job():
    print("Отправлено")
    vk.messages.send(
        chat_id='1',
        random_id=random.randint(1, 10000),
        message='Кинуть https://vk.com/am_am_ammmm 1'
    )

schedule.every(random.randint(9, 14)).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
