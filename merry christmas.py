import time
import png
import pyqrcode
import pyautogui
print("О нет! Кажется дед Мороз упал в Узбекистан, что же нам делать?")
time.sleep(2)
print("А, кстати мы его олени, если ты думаешь что в этом нету ничего плохо то ты ошибаешся, ведь его заберут в подвал!")
gotov=input("ты готов нам помочь спасти деда Мороза?")
if gotov=="да" or gotov=="конечно":
    print("Тогда нужно пойти для начала подойти к их нему главному войну которого зовут Пьер Дун и попробовать договориться с ним")
    a=input("Что ты ему предложишь взамен на деда Мороза?")
    if a=="семечки" or a=="мышь живую" or a=="сухарик":
        print("Красавчик! Теперь можешь посмотреть на рабочий стол там подарок от деда Мороза тебе на новый год, (но твой загаданый он тоже принесёт) удачи!")
        my_qr = pyqrcode.create("https://yandex.ru/video/preview/11319759679846784555")
        my_qr.png('Подарочек',scale=20)
        print("я тебе помогу выйти)")
        pyautogui.moveTo(0,1920)
        time.sleep(2)
        pyautogui.click(button = "left")
    else:
        print("Деда Мороза зожгли на шашлых(((")
if gotov=="нет":
    print("Эх.... Ну ладно, но всё равно получи свой подарок на рабочем столе!")
    my_qr = pyqrcode.create("https://yandex.ru/video/preview/11843531504909666715")
    my_qr.png('Тот самый подарок)))',scale=20)
    print("Картинка сгенерирована")
