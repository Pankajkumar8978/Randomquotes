import telebot
import requests

# Set up Telegram bot
bot = telebot.TeleBot("YOUR_BOT_TOKEN")

# URL for fetching random quotes
random_quotes_url = "https://api.quotable.io/random"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I'm a Random Quote Generator Bot. Use /quote to get a random quote.")

@bot.message_handler(commands=['quote'])
def send_random_quote(message):
    try:
        response = requests.get(random_quotes_url)
        if response.status_code == 200:
            quote_data = response.json()
            quote = f'"{quote_data["content"]}" - {quote_data["author"]}'
            bot.reply_to(message, quote)
        else:
            bot.reply_to(message, "Failed to fetch a random quote. Please try again later.")
    except Exception as e:
        bot.reply_to(message, "An error occurred. Please try again later.")

bot.polling()
