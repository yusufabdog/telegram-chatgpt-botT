import telebot
import openai
import os

# Haal API keys uit omgevingsvariabelen
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Telegram bot initialiseren
bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

# Reactie op berichten
@bot.message_handler(func=lambda message: True)
def chatgpt_reply(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        bot.reply_to(message, response["choices"][0]["message"]["content"])
    except Exception as e:
        bot.reply_to(message, "Er is een fout opgetreden!")

# Start de bot
print("Bot is gestart...")
bot.polling()
