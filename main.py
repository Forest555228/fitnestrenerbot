import telebot
from telebot import types
from credits import TELEGRAM_TOKEN


bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой фитнес помощник бот!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Подкачка')
        btn7 = types.KeyboardButton('Вопрос-Ответ')
        btn2 = types.KeyboardButton('Донат')
        btn3 = types.KeyboardButton('Обратная связь')
        markup.add(btn1, btn7, btn3, btn2)
        bot.send_message(message.from_user.id, 'Выбери интересующую тему', reply_markup=markup)

    elif message.text == 'Донат':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Отправить донат нам можно по этой ссылке: https://www.donationalerts.com/r/forest555', reply_markup=markup)

    elif message.text == 'Обратная связь':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Почта для связи: fitnestrenerbot@yandex.ru', reply_markup=markup)

    elif message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Подкачка')
        btn7 = types.KeyboardButton('Вопрос-Ответ')
        btn2 = types.KeyboardButton('Донат')
        btn3 = types.KeyboardButton('Обратная связь')
        markup.add(btn1, btn7, btn3, btn2)
        bot.send_message(message.from_user.id, 'Выбери интересующую тему', reply_markup=markup)

    elif message.text == 'Бицепс':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться на главную')
        btn2 = types.KeyboardButton('Подкачка')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "5 лучших упражнение для прокачки бецепса: https://www.iphones.ru/iNotes/5-moshchnyh-uprazhneniy-na-bicepsy-kotorye-uvelichat-ih-v-dva-raza-08-23-2020", reply_markup=markup)


    elif message.text == 'Подкачка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Бицепс')
        btn2 = types.KeyboardButton('Плечи и трицепс')
        btn3 = types.KeyboardButton('Ноги')
        btn4 = types.KeyboardButton('Спина')
        btn5 = types.KeyboardButton('Шея')
        btn6 = types.KeyboardButton('Грудь')
        btn7 = types.KeyboardButton('Вернуться на главную')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, 'Выбери интересующие упражнения', reply_markup=markup)


    elif message.text == 'Плечи и трицепс':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться на главную')
        btn2 = types.KeyboardButton('Подкачка')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Ошибки и Упражнение для прокачки плеч и трицепса: https://www.iphones.ru/iNotes/editrial-best-shoulder-workout", reply_markup=markup)

    elif message.text == 'Ноги':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться на главную')
        btn2 = types.KeyboardButton('Подкачка')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Упражнения для накачивания ног дома: https://lifehacker.ru/kak-nakachat-nogi-doma/", reply_markup=markup)

    elif message.text == 'Спина':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться на главную')
        btn2 = types.KeyboardButton('Подкачка')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Упражнения для укрепления спины: https://lifehacker.ru/luchshie-uprazhneniya-dlya-spiny/", reply_markup=markup)

    elif message.text == 'Шея':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться на главную')
        btn2 = types.KeyboardButton('Подкачка')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Упражнения для укрепления шеи дома: https://lifehacker.ru/neck-exercises/", reply_markup=markup)

    elif message.text == 'Грудь':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться на главную')
        btn2 = types.KeyboardButton('Подкачка')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Упражнения для накачивания грудных мышц: https://lifehacker.ru/uprazhneniya-na-grud/", reply_markup=markup)

    elif message.text == 'Вопрос-Ответ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться на главную')
        btn2 = types.KeyboardButton('Зачем создан данный бот')
        btn3 = types.KeyboardButton('Почему мы лучше остальных?')
        btn4 = types.KeyboardButton('Будут ли ещё добавляться упражнения?')
        btn5 = types.KeyboardButton('В чём смысл разработчиков работать над этим ботом, если им за этоне платят?')
        markup.add(btn2, btn3, btn4, btn5, btn1)
        bot.send_message(message.from_user.id, "Нажмите на вопрос, который вам интересен", reply_markup=markup)

    elif message.text == 'Зачем создан данный бот':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться на главную')
        btn2 = types.KeyboardButton('Вернуться на Вопрос-Ответ')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Данный бот создан для упрощения поиска упражнений дляя подкачки вашего тела.", reply_markup=markup)

    elif message.text == 'Почему мы лучше остальных?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться на главную')
        btn2 = types.KeyboardButton('Вернуться на Вопрос-Ответ')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Наш бот абсолютно бесплатен и постоянно обновляется", reply_markup=markup)

    elif message.text == 'Будут ли ещё добавляться упражнения?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться на главную')
        btn2 = types.KeyboardButton('Вернуться на Вопрос-Ответ')
        btn3 = types.KeyboardButton('Обратная связь')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Наш бот новый из-за чего его количество упражнений в нём ограничено, но он постоянно обновляется, чтобы радовать наших пользователей. Так же вы можете оставить свои пожелания или жалобы нажав по кнопке Обратная связь.", reply_markup=markup)

    elif message.text == 'Вернуться на Вопрос-Ответ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться на главную')
        btn2 = types.KeyboardButton('Зачем создан данный бот')
        btn3 = types.KeyboardButton('Почему мы лучше остальных?')
        btn4 = types.KeyboardButton('Будут ли ещё добавляться упражнения?')
        btn5 = types.KeyboardButton('В чём смысл разработчиков работать над этим ботом, если им за этоне платят?')
        markup.add(btn2, btn3, btn4, btn5, btn1)
        bot.send_message(message.from_user.id, "Нажмите на вопрос, который вам интересен", reply_markup=markup)

    elif message.text == 'В чём смысл разработчиков работать над этим ботом, если им за этоне платят?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться на главную')
        btn2 = types.KeyboardButton('Вернуться на Вопрос-Ответ')
        btn3 = types.KeyboardButton('Донат')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Мы пытались найти разные сервисы, в которых будет всё для накачивания мышц, но так как таких БЕСПЛАТНЫХ сервисов нет, мы решили что создание такого бота может быть интересно людям. Так же если вам нравится продукт, то можно отправить нам донат.", reply_markup=markup)

bot.polling(none_stop=True, interval=0)


