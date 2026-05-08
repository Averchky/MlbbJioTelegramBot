from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os
import logging
import asyncio

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("ERROR: TOKEN environment variable not set!")
    exit(1)

print(f"Bot token found: {TOKEN[:20]}...")

IGNORE_USER = "kyriosky"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages"""
    try:
        sender_username = update.message.from_user.username or ""
        user_message = update.message.text
        
        # ONLY respond if it's from kyriosky, IGNORE everyone else
        if sender_username != IGNORE_USER:
            return
        
        # Only respond to MLBB????
        if "2167?" in user_message:
            # Send message to the group (don't reply, just send)
            await update.message.chat.send_message(
                "@kyriosky @jasonieeee @l_n_w5 @jianrongggg @roderlol @ongysys\n\n"
                "VISA TIME"
            )
            print(f"✅ Bot sent message to group")
    except Exception as e:
        print(f"Error: {e}")

async def post_init(application: Application) -> None:
    """Clean up old sessions on startup"""
    try:
        await application.bot.delete_webhook(drop_pending_updates=True)
        print("✅ Cleared old sessions and webhooks")
        await asyncio.sleep(1)
    except Exception as e:
        print(f"Error clearing sessions: {e}")

def main():
    """Start the bot"""
    try:
        application = Application.builder().token(TOKEN).build()
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        application.post_init = post_init
        
        print("🤖 Bot is starting...")
        application.run_polling(
            allowed_updates=Update.ALL_TYPES,
            drop_pending_updates=True,
            timeout=30,
            read_timeout=30,
            write_timeout=30,
            connect_timeout=30
        )
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
