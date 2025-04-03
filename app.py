import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import filters  # Corrected import for filters
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Get the API Token from environment variables
API_TOKEN = os.getenv("API_TOKEN")

# Function to handle the /start command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("hui")

# Function to check bio and approve request
async def check_bio(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username

    # Getting the user's bio
    user_info = await context.bot.get_chat_member(update.message.chat_id, user_id)
    bio = user_info.user.bio

    # Check if bio contains "@Real_Pirates"
    if "@Real_Pirates" in bio:
        # Accept the request
        await context.bot.approve_chat_member(update.message.chat_id, user_id)
        await update.message.reply_text("Welcome, @Real_Pirates!")
    else:
        # Decline the request
        await context.bot.kick_chat_member(update.message.chat_id, user_id)
        await update.message.reply_text("Sorry, you must have `@Real_Pirates` in your bio to join.")

# Main function to start the bot
async def main() -> None:
    # Create the Application and pass it your bot's token
    application = Application.builder().token(API_TOKEN).build()

    # Add the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Register the new chat members handler to check bios
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, check_bio))

    # Start the Bot
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
