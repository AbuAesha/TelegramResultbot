from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

# ================== STUDENT DATA ==================
students = {
    "SU1701058": {
        "name": "EDRIS KEDIR MEKLA",
        "sex": "M",
        "mid_exam": 22,
        "group": 8,
        "indi": 8,
        "total_ca": 38
    },

    # PASTE ALL YOUR OTHER STUDENTS HERE
}

# ================== START COMMAND ==================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎓 Student Result Bot\n\n"
        "Use:\n"
        "/grade STUDENT_ID\n\n"
        "Example:\n"
        "/grade SU1701058"
    )

# ================== GRADE COMMAND ==================
async def grade(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/grade STUDENT_ID\n\n"
            "Example:\n/grade SU1701058"
        )
        return

    sid = context.args[0].upper()

    if sid not in students:
        await update.message.reply_text(
            "❌ Student ID not found."
        )
        return

    s = students[sid]

    await update.message.reply_text(
        f"""
🎓 ET CONTINUOUS ASSESSMENT RESULT

👤 Name: {s['name']}
🆔 Student ID: {sid}
⚧ Sex: {s['sex']}

📝 Mid Exam (30%): {s['mid_exam']}
👥 Group Assignment (10%): {s['group']}
📄 Individual Assignment (10%): {s['indi']}

✅ Total CA Mark: {s['total_ca']}/50
"""
    )

# ================== MAIN ==================
def main():

    if not TOKEN:
        raise ValueError("BOT_TOKEN environment variable not set")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("grade", grade))

    print("Telegram Result Bot is running...")

    app.run_polling()

if __name__ == "__main__":
    main()