from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters, ChatMemberHandler

TOKEN = '7509459901:AAG_Hv8fvlE6LcGxThQXQ2aIkAmTjYViEVo'

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Ahoy! I’m here to auto-approve your requests! 🏴‍☠️')

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Arrr, I can approve join requests automatically!\n"
        "- Just join the group, and I’ll handle the rest! ⚓"
    )
    await update.message.reply_text(help_text)

# Auto-approve join requests
async def auto_approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_member = update.chat_member
    if chat_member.new_chat_member.status in ['member', 'administrator']:
        await context.bot.approve_chat_join_request(chat_id=update.effective_chat.id, user_id=chat_member.new_chat_member.user.id)
        await update.message.reply_text(f"Ahoy, {chat_member.new_chat_member.user.first_name}! You're approved! 🎉")

# Main bot setup
def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))

    # Chat member handler for join requests
    application.add_handler(ChatMemberHandler(auto_approve, ChatMemberHandler.MY_CHAT_MEMBER))

    # Run the bot continuously
    application.run_polling()

if __name__ == '__main__':
    main()
