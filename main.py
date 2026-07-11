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
