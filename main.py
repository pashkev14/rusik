import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from constants import *
from random import randint


VK_SESSION = vk_api.VkApi(token=TOKEN)
VK = VK_SESSION.get_api()
VK_LP = VkLongPoll(VK_SESSION)


def send(id, msg, key=None):
    if key:
        VK.messages.send(user_id=id, message=msg, random_id=randint(0, 2 ** 64), keyboard=key)
    else:
        VK.messages.send(user_id=id, message=msg, random_id=randint(0, 2 ** 64))


def create_keyboard(training=False):
    keyboard = VkKeyboard(one_time=True)
    if training:
        pass
    else:
        keyboard.add_button("Тренировка 💪🏻", color=VkKeyboardColor.PRIMARY)
        keyboard.add_button("Инфо ⓘ", color=VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()


def main():
    training = False
    points = 0
    tasks = 0
    for event in VK_LP.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            keyboard = create_keyboard()
            message = event.text.lower().split()[0]
            if message == 'начать':
                send(event.user_id, 'Привет! Я - Ян Гус, давай учить нудную часть русского языка вместе со мной!')
                send(event.user_id, 'Ну что, будем тренироваться?', keyboard)
            if message == 'тренировка':
                training = True
            elif message == 'инфо':
                send(event.user_id, INFO)
                send(event.user_id, 'Ну что, будем тренироваться?', keyboard)
            else:
                send(event.user_id, 'Ну что, будем тренироваться?', keyboard)
            if training:
                keyboard = create_keyboard()


if __name__ == '__main__':
    main()
