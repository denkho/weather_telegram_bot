from threading import Thread
import telebot
import time
import schedule
import constants
import yandex_api

bot = telebot.TeleBot(constants.TELEBOT_API)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Это бот для автоматической отправки погоды в выбранный чат")


def send_forecasts():
	data = yandex_api.get_info_from_api()
	bot.send_message(constants.CHAT_ID, yandex_api.current_weather_output(data))
	for n in range(len(data['forecast']['parts'])):
		bot.send_message(constants.CHAT_ID, yandex_api.weather_forecast_output(data, n))
	
	
def schedule_checker():
	while True:
		schedule.run_pending()
		time.sleep(1)


if __name__ == "__main__":
	schedule.every().day.at("07:00").do(send_forecasts)
	schedule.every().day.at("12:00").do(send_forecasts)
	schedule.every().day.at("20:00").do(send_forecasts)
	Thread(target=schedule_checker).start()
	bot.infinity_polling()
