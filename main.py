

bot = telebot.TeleBot(5524495145:AAGY40iUAlrdRI464ITzLsWwZ4kWbdNh7F4)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def boten(message):
	 
	 def send_welcome(message):
	 	bot.reply_to(message,f'''*- Hi Boss 👋
- Bot Check User Telegram 🤖
- Send /StHe
- Coded By : @W_2_X 📢*''',parse_mode="markdown")

@bot.message_handler(commands=['StHe'])
def send_tool(message):
    key = types.ReplyKeyboardMarkup(row_width=1)
    but1 = types.KeyboardButton('• Check - 3 -')
    but2 = types.KeyboardButton('• Check - 4 -')
    but3 = types.KeyboardButton('• Check User - 5 -')
    
    key.add(but1,but2,but3)
    send = bot.send_message(message.chat.id , "*Hi Boss*" ,reply_markup = key,parse_mode="markdown")
@bot.message_handler(func=lambda m: True)
def trakos(message):
	global bad,hit,key
	if message.text == "• Check - 3 -":	
		start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=start done").json()
		id_msg	=(start_msg['result']["message_id"])
		while True:
		          user = 'QWERTYUIOPASDFGHJKLZXCVNBM'
		          us = str("".join(random.choice(user)for i in range(3)))
		          username = us+'bot'
		          url = f"https://t.me/{username}"
		          req = requests.get(url)
		          if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
		                    hit+=1
		                    bot.send_message(message.chat.id, text=f"*Hi New User : @{username}*",parse_mode="markdown")
		          else:
		                bad+=1
		                requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=• Hi Check Username Bot\n<~>~>~>~>~>~>~>~>~>\n• Error User : {bad}\n• Done User : {hit}\n• In User : @{username}\n<~>~>~>~>~>~>~>~>~>\n• From : @E_E_2 - @W_2_X")		               
#===============#
	if message.text == "• Check - 4 -":	
		start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=start done").json()
		id_msg	=(start_msg['result']["message_id"])
		while True:
		          user = 'QWERTYUIOPASDFGHJKLZXCVNBM1234567890'
		          us = str("".join(random.choice(user)for i in range(4)))
		          username = us+'bot'
		          url = f"https://t.me/{username}"
		          req = requests.get(url)
		          if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
		                    hit+=1
		                    bot.send_message(message.chat.id, text=f"*Hi New User : @{username}*",parse_mode="markdown")
		          else:
		                bad+=1
		                requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=• Hi Check Username Bot\n<~>~>~>~>~>~>~>~>~>\n• Error User : {bad}\n• Done User : {hit}\n• In User : @{username}\n<~>~>~>~>~>~>~>~>~>\n• From : @E_e_2 - @W_2_X")
#===============#
	if message.text == "• Check User - 5 -":	
		start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=start done").json()
		id_msg	=(start_msg['result']["message_id"])
		while True:
		          user = 'QWERTYUIOPASDFGHJKLZXCVNBM1234567890'
		          us = str("".join(random.choice(user)for i in range(1)))
		          uss = str("".join(random.choice(user)for i in range(1)))
		          username = us+'_'+uss+uss+'_'+us
		          url = f"https://t.me/{username}"
		          req 
