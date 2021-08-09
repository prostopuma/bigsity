import telebot
from config import TOKEN, admin_id
from main import result

g = 'Ghbdtn lox'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	for item in result():
		bot.reply_to(message, item[0])

if __name__ == '__main__':
    bot.polling()