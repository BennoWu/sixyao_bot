def sendMessage( text = "test" ):

	from linebot import LineBotApi
	from linebot.models import TextSendMessage
	from linebot.exceptions import LineBotApiError
	token = 'XlA8e+hOI4ALuTIoXU+72w+oR8eF7JlZ7GC9JPPVZFgkGCGXUkcRMHLUylMGzaVSMvFDLaQPlSUP33mypYCcWIw49ZDe71btRr6E9cMyVsgurdlBko9yAqP/0tYy4jKUFMfjNTDe8NzslS+wA7ZBqQdB04t89/1O/w1cDnyilFU='
	my_id = 'U21eaaf32db85b983a842d9a9da81d8f1'
	line_bot_api = LineBotApi( token )

	message = text
	line_bot_api.push_message('U21eaaf32db85b983a842d9a9da81d8f1', TextSendMessage(text = message))

#	os.system("shutdown -s -f")

if __name__ == '__main__':
	sendMessage()









# def showTime():
# 	import time
# 	now = time.localtime()
# 	ampm=""
# 	if now[3]<12:
# 		ampm="am"
# 	else:
# 		ampm="pm"
# 	return ("%s- %i:%02d:%02ds."% (
# 		ampm,
# 		now[3],
# 		int(now[4]),
# 		int(now[5])
# 		))