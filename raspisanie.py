import telebot
import datetime
from telebot import types

bot = telebot.TeleBot('722998100:AAEOn6OK74dP1uMX8a_JjeEsPmVD7tsoD68')
keyboard1=types.ReplyKeyboardMarkup(True)
keyboard1.row('/start','Hello')
keyboard2=types.ReplyKeyboardMarkup(True)
keyboard2.row('Понедельник',"Вторник")
keyboard2.row("Среда", "Четверг")
keyboard2.row("Пятница","Другая неделя")
week_number = int(datetime.date.today().isocalendar()[1]+1)

@bot.message_handler(commands = ['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Привет, выбери день недели, расписание которого тебе надо узнать', reply_markup=keyboard2)
		
@bot.message_handler(content_types=['text'])
def send_text(message):
    week_number = int(datetime.date.today().isocalendar()[1]+1)
    if week_number % 2 == 1:
        #нечетные недели
        if message.text.lower() == 'понедельник':
            bot.send_message(message.chat.id, 'Прикладная механика(5423) — 11:40\nФизкультура — 13:45\nПр в MatLab(2430) — 15:35')
        elif message.text.lower() == 'вторник':
            bot.send_message(message.chat.id, 'Экономика организации(6209) — 11:40\nЭО пр.(6208) — 13:45\nФизика пр.(6204) — 15:35')
        elif message.text.lower() == 'среда':	
            bot.send_message(message.chat.id, 'МатАнализ(3132) — 13:45\nМатАнализ пр. — 15:35')
        elif message.text.lower() == 'четверг':
            bot.send_message(message.chat.id, 'Физика лаб. — 11:40\nФизические основы микро- и наноэлектроники(5419) — 13:45\nТеоретические основы электроники(1246) — 15:35\nИностранный язык — 17:25')
        elif message.text.lower() == 'пятница':
            bot.send_message(message.chat.id, 'ФОМНЭ пр. — 9:50\nТОЭ пр. — 11:40\nФизика(3107) — 13:45\nФизкультура — 15:35')
        #elif message.text.lower() == 'другая неделя':
        #   bot.send_message(message.chat.id, 'Вы выбрали другую неделю')
            
        else:
            bot.send_message(message.chat.id, 'Я тебя не понимаю')

    else:
        #четные недели
    	if message.text.lower() == 'понедельник':
        	bot.send_message(message.chat.id, 'Экология(5423) — 11:40\nФизкультура — 13:45\nПр в MatLab(2430) — 15:35')
    	elif message.text.lower() == 'вторник':
    		bot.send_message(message.chat.id, 'Экономика организации(6209) — 11:40\nЭО пр.(6208) — 13:45\nЭкология пр.(6312) — 15:35\nПриклМех пр.(6201) — 17:25')
    	elif message.text.lower() == 'среда':	
    		bot.send_message(message.chat.id, 'МатАнализ(3132) — 13:45\nМатАнализ пр. — 15:35')
    	elif message.text.lower() == 'четверг':
    		bot.send_message(message.chat.id, 'Физика лаб. — 11:40\nФизические основы микро- и наноэлектроники(5419) — 13:45\nТеоретические основы электроники(1246) — 15:35\nИностранный язык — 17:25')
    	elif message.text.lower() == 'пятница':
    		bot.send_message(message.chat.id, 'ФОМНЭ лаб.(5471) — 9:50\nТОЭ пр. — 11:40\nФизика(3107) — 13:45\nФизкультура — 15:35')
    	else:
    		bot.send_message(message.chat.id, 'Я тебя не понимаю')
bot.polling()
