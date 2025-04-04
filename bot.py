from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
TOKEN = '7509459901:AAHLb7yGn0YhHasiOVM8UdFioeZX0v9gnFY'

# Async function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Ahoy, sailor! The bot be startin’ its engines! 🏴‍☠️')

# Main function to set up the bot
def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Add command handler for /start
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()
