import logging
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = "8480382561:AAHy7ZyssFaEOBJ4pK9wk8yuTyGJNUAhEyU"
CHANNEL_ID = -1003142012885
OWNER_ID = 7240758433

logging.basicConfig(level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    btns = [
        [
            InlineKeyboardButton("📢 Join Channel", url="https://t.me/+r4kVLPJZKPAzMGY1")
        ],
        [
            InlineKeyboardButton("✅ I Joined, Give File", callback_data="check_join")
        ],
    ]

    await update.message.reply_text(
        "Welcome!\nJoin the channel to unlock the content.",
        reply_markup=InlineKeyboardMarkup(btns),
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "check_join":
        user_id = query.from_user.id

        try:
            member = await context.bot.get_chat_member(CHANNEL_ID, user_id)

            if member.status in ["member", "administrator", "creator"]:
                await query.edit_message_text("Joined verified! 🔓 Sending file...")

                await context.bot.send_message(
                    chat_id=user_id,
                    text="Here is your file:\nhttps://drive.google.com/drive/folders/1IWiMSFCdiFXaI5n3llXCy6HfxaIGEGhz",
                )
            else:
                await query.edit_message_text("❌ You must join first!")
        except:
            await query.edit_message_text("❌ You must join the channel first!")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot running on Railway...")
    app.run_polling()


if __name__ == "__main__":
    main()
  
