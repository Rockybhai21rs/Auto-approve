import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import filters  # Corrected import for filters
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Get the API Token from environment variables
API_TOKEN = os.getenv("API_TOKEN")

# Function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("hui")

# Function to check bio and approve request
def check_bio(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username

    # Getting the user's bio
    user_info = context.bot.get_chat_member(update.message.chat_id, user_id)
    bio = user_info.user.bio

    # Check if bio contains "@Real_Pirates"
    if "@Real_Pirates" in bio:
        # Accept the request
        context.bot.approve_chat_member(update.message.chat_id, user_id)
        update.message.reply_text("Welcome, @Real_Pirates!")
    else:
        # Decline the request
        context.bot.kick_chat_member(update.message.chat_id, user_id)
        update.message.reply_text("Sorry, you must have `@Real_Pirates` in your bio to join.")

# Main function to start the bot
def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(API_TOKEN)
    dp = updater.dispatcher

    # Add the /start command handler
    dp.add_handler(CommandHandler("start", start))

    # Register the new chat members handler to check bios
    dp.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, check_bio))  # Corrected filter usage

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
