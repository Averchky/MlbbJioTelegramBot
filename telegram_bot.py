from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os

# Get token from environment variable (safer than hardcoding)
TOKEN = os.getenv("TOKEN", "YOUR_BOT_TOKEN_HERE")

# REPLACE WITH YOUR TELEGRAM USERNAME (without @)
ALLOWED_USER = "kyriosky"  # Change this to YOUR username

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Only responds to allowed user"""
    
    # Get the username of who sent the message
    sender_username = update.message.from_user.username
    
    # Check if sender is the allowed user
    if sender_username != ALLOWED_USER:
        return  # Ignore messages from other users
    
    user_message = update.message.text
    
    # Check if message contains "MLBB????"
    if "MLBB????" in user_message:
        # Tagged message with all your friends
        tagged_message = (
            "MLBB GAME TIME! 🎮\n\n"
            "@kyriosky @jasonieeee @l_n_w5 @jianrongggg @roderlol @ongysys\n\n"
            "Let's go! 💪"
        )
        await update.message.reply_text(tagged_message)

def main():
    """Start the bot"""
    application = Application.builder().token(TOKEN).build()
    
    # Add handler for all text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🤖 Bot is running... (Only responds to @kyriosky)")
    application.run_polling()

if __name__ == '__main__':
    main()
