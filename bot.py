import telebot
from config import token
from logic import get_class

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['photo']) #указывает, что следующая функция будет обрабатывать сообщения, содержащие фотографии
def send_message(message):

    file_info = bot.get_file(message.photo[-1].file_id) #пригодится тебе для получения информации о последнем изображении в сообщении

    file_name = file_info.file_path.split('/')[-1] #так ты сможешь извлечь имя файла из полного пути к файлу, который возвращает Telegram

    downloaded_file = bot.download_file(file_info.file_path) #Открывает новый файл в бинарном режиме записи ('wb')

    with open(file_name, 'wb') as new_file:

        new_file.write(downloaded_file) #Записывает загруженные данные в новый файл

    result = get_class(file_name)

    bot.reply_to(message, result)

bot.infinity_polling()






























