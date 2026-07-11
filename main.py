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

# Trigger phrases that activate the per-user reply
TRIGGER_PHRASES = ["GU YES", "MLBB SUCKS"]

MENTIONS = "@kyriosky @jasonieeee @l_n_w5 @jianrongggg @Quan1921 @ongysys\n\n"

USER_REPLIES = {
    "kyriosky": "Come mlbb with my No1 Silvanna 🤮",
    "jasonieeee": "MY GLOO WIN RATE IS JOVER",
    "l_n_w5": "Next game i play tank ok",
    "jianrongggg": "NEED VISA IS IT",
    "Quan1921": "WHERE IS MY TEAM, WHY SO MANY PPL HERE WHY",
    "ongysys": "Yall dont rotate ownself settle the fat mm later",
}


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages"""
    try:
        sender_username = update.message.from_user.username or ""
        user_message = update.message.text or ""

        # Easter egg: "10 + 9" -> "21"
        if user_message.strip() == "whats 10 + 9":
            await update.message.chat.send_message("2️⃣ 1️⃣")
            print(f"✅ Bot sent '21' triggered by {sender_username}")
            return
            
         if user_message.strip() == "WHATS GU":
            await update.message.chat.send_message("ra's al GU YES")
            print(f"✅ Bot sent 'GU' triggered by {sender_username}")
            return

        # Per-user trigger replies
        if any(phrase in user_message for phrase in TRIGGER_PHRASES):
            reply_line = USER_REPLIES.get(sender_username)
            if reply_line:
                await update.message.chat.send_message(MENTIONS + reply_line)
                print(f"✅ Bot sent message triggered by {sender_username}")
            else:
                print(f"⚠️ Trigger matched but no reply configured for {sender_username}")

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
