import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


TOKEN = 'ef945ff25f70fd0434fc50668ce96b4083c28ab1f4893ca0da45bcbcfc38bdbfa5b7149153a3660f2a84f'
VK_SESSION = vk_api.VkApi(token=TOKEN)
VK = VK_SESSION.get_api()
VK_LP = VkLongPoll(VK_SESSION)


def send(id, msg):
    VK.messages.send(user_id=id, message=msg, random_id=1)


def create_keyboard():
    keyboard = VkKeyboard(one_time=False)
    #False Если клавиатура должна оставаться откртой после нажатия на кнопку
    #True если она должна закрваться

    keyboard.add_button("Закрыть", color=VkKeyboardColor.PRIMARY)
    keyboard.add_button("Кнопка", color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()#Обозначает добавление новой строки
    keyboard.add_button("Кнопка", color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button("Кнопка", color=VkKeyboardColor.PRIMARY)
    keyboard.add_button("Кнопка", color=VkKeyboardColor.PRIMARY)

    return keyboard.get_keyboard()
    #Возвращает клавиатуру


def main():
    training = False
    for event in VK_LP.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.from_user:
                keyboard = create_keyboard()
                send(event.user_id, 'Ну что, будем тренироваться?')


if __name__ == '__main__':
    main()
