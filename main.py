import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


TOKEN = 'ef945ff25f70fd0434fc50668ce96b4083c28ab1f4893ca0da45bcbcfc38bdbfa5b7149153a3660f2a84f'


def main():
    bot = vk_api.VkApi(token=TOKEN)
    lp = VkLongPoll(bot)
    for event in lp.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print(event)


if __name__ == '__main__':
    main()
