import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from constants import *
from random import *
import json

VK_SESSION = vk_api.VkApi(token=TOKEN)
VK = VK_SESSION.get_api()
VK_LP = VkLongPoll(VK_SESSION)
DICTIONARY = json.loads(WORDS_ORTHOEPY)


def send(id, msg, key=None):
    if key:
        VK.messages.send(user_id=id, message=msg, random_id=randint(0, 2 ** 64), keyboard=key)
    else:
        VK.messages.send(user_id=id, message=msg, random_id=randint(0, 2 ** 64))


def create_keyboard(training=False):
    keyboard = VkKeyboard(one_time=True)
    if training:
        keyboard.add_button()
    else:
        keyboard.add_button("Тренировка 💪🏻", color=VkKeyboardColor.PRIMARY)
        keyboard.add_button("Инфо ⓘ", color=VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()


def main():
    training = False
    correct = 0
    cards = 0
    for event in VK_LP.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            keyboard = create_keyboard()
            message = event.text.lower().split()[0]
            if message == 'начать':
                send(event.user_id, 'Привет! Я - Ян Гус, давай учить нудную часть русского языка вместе со мной!')
                send(event.user_id, 'Ну что, будем тренироваться?', keyboard)
            if message == 'тренировка':
                training = True
                keyboard = create_keyboard()
            elif message == 'инфо':
                send(event.user_id, INFO)
                send(event.user_id, 'Ну что, будем тренироваться?', keyboard)
            elif message == 'закончить':
                training = False
            else:
                send(event.user_id, 'Ну что, будем тренироваться?', keyboard)


if __name__ == '__main__':
    main()
