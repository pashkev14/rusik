import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id


TOKEN = 'ef945ff25f70fd0434fc50668ce96b4083c28ab1f4893ca0da45bcbcfc38bdbfa5b7149153a3660f2a84f'
VK_SESSION = vk_api.VkApi(token=TOKEN)
VK = VK_SESSION.get_api()
VK_LP = VkLongPoll(VK_SESSION)


def send(id, msg):
    VK.messages.send(user_id=id, message=msg, random_id=get_random_id())


def main():
    for event in VK_LP.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.text != '' and event.from_user:
                send(event.obj.from_id, 'Ну что, будем тренироваться?')


if __name__ == '__main__':
    main()
