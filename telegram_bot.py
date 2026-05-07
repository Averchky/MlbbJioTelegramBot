from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os
import logging

# Enable logging to see errors
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Get token from environment variable
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("ERROR: TOKEN environment variable not set!")
    exit(1)

print(f"Bot token found: {TOKEN[:20]}...")

# REPLACE WITH YOUR TELEGRAM USERNAME (without @)
ALLOWED_USER = "kyriosky"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Only responds to allowed user"""
    
    try:
        sender_username = update.message.from_user.username
        
        if sender_username != ALLOWED_USER:
            return
        
        user_message = update.message.text
        
        if "MLBB????" in user_message:
            tagged_message = (
                "MLBB GAME TIME! 🎮\n\n"
                "@kyriosky @jasonieeee @l_n_w5 @jianrongggg @roderlol @ongysys\n\n"
                "Let's go! 💪"
            )
            await update.message.reply_text(tagged_message)
            print(f"Replied to {sender_username}")
    except Exception as e:
        print(f"Error in handle_message: {e}")

def main():
    """Start the bot"""
    try:
        application = Application.builder().token(TOKEN).build()
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        print("🤖 Bot is running... (Only responds to @kyriosky)")
        application.run_polling()
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
