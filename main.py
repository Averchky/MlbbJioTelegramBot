from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("ERROR: TOKEN environment variable not set!")
    exit(1)

print(f"Bot token found: {TOKEN[:20]}...")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages"""
    try:
        user_message = update.message.text
        sender = update.message.from_user.first_name
        
        # Check if message contains "MLBB????"
        if "MLBB????" in user_message:
            tagged_message = (
                "MLBB GAME TIME! 🎮\n\n"
                "@kyriosky @jasonieeee @l_n_w5 @jianrongggg @roderlol @ongysys\n\n"
                "Let's go! 💪"
            )
            await update.message.reply_text(tagged_message)
            print(f"✅ Bot replied to {sender}")
    except Exception as e:
        print(f"Error: {e}")

async def post_init(application: Application) -> None:
    """Delete webhook on startup (use polling instead)"""
    await application.bot.delete_webhook(drop_pending_updates=True)
    print("Webhook deleted, using polling mode")

def main():
    """Start the bot with polling"""
    try:
        application = Application.builder().token(TOKEN).build()
        
        # Set up handlers
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        # Clean up on startup
        application.post_init = post_init
        
        print("🤖 Bot is running... (Polling mode)")
        application.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
