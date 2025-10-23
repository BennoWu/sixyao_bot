# from combineData import *
from ocr_work import *
from combineDataMain import *
from logBackup import *
from  supabase_io import *


from flexLayout_tool import *
import os
from flask import Flask, request, abort

from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import (
	MessageEvent, 
	TextMessage, 
	TextSendMessage, 
	StickerMessage,
	StickerSendMessage,
	ImageMessage,
	ImageSendMessage,
	LocationMessage,
	ImagemapSendMessage,
	BaseSize,
	URIImagemapAction,
	MessageImagemapAction,
	ImagemapArea,
	TemplateSendMessage,
	ImageCarouselTemplate,
	ImageCarouselColumn,
	PostbackEvent,
	PostbackTemplateAction,
	FlexSendMessage, 
	BubbleContainer, 
	ImageComponent, 
	Sender 
)


app = Flask(__name__)

## 裝卦初號機
line_bot_api = LineBotApi(os.environ.get('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.environ.get('LINE_CHANNEL_SECRET'))





import logging
from flask import Flask

app = Flask(__name__)

# 設定 logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()





@app.route("/")
def home():
	logger.debug("收到 GET / 請求")  # 這行應該會在 Dashboard 出現
	return 'home OK'

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
	# get X-Line-Signature header value
	signature = request.headers['X-Line-Signature']

	# get request body as text
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)

	# handle webhook body
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		print("Invalid signature. Please check your channel access token/channel secret.")
		abort(400)

	return 'OK'



# # 處理訊息
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):




#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text))


# import time


# last_time = [time.time()]  # 用 list 包起來避免 scope 問題
# def get_time():
#     current = time.time()
#     elapsed = current - last_time[0]
#     last_time[0] = current
#     return round(elapsed, 2)

# # 使用
# total = []
# total.append(get_time())  # 0
# time.sleep(1.5)
# total.append(get_time())  # 1.5
# time.sleep(0.75)
# total.append(get_time())  # 0.75

# print(total)
# result = " - ".join(map(str, total))




## 訊息進入起點
# 處理訊息
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

	# 取得用戶的id
	user_id = event.source.user_id 
	profile = line_bot_api.get_profile(user_id)
	# ## 用戶line上面的名字
	displayName = profile.display_name 
	## 取得用戶的頭貼
	picUrl = profile.picture_url
	##收到的訊息
	inputMsg = event.message.text

	inputMsg = inputMsg.replace( '\u200b' , '' )
	print ( ">:" , inputMsg )
	print ( unifiedData(inputMsg) )

	# print( unifiedData( inputMsg , strong_sep='//', sep_for_app= "||") )
	## json建立
	jsonData = jsonDataClass( linebotId = user_id  ,
								linebotUserName = displayName ,
								userImage = picUrl ,
								command = inputMsg )


	if inputMsg == "id":
		inputMsg = user_id +"//" +displayName +"//"+picUrl



	elif inputMsg.lower() == "notion" :

		# 測試讀取 (會回傳字典)
		data = get_user_data( user_id )
		if data:
			print(f"Token: {data['notion_token']}")
			print(f"Page ID: {data['page_id']}")
			token_buf  = data['notion_token']
			pageId_buf = data['page_id']

			## 測試取得的token和page id是否正確
			notionAccount = checkNotionAcc( token_buf , pageId_buf )
			if notionAccount == True:
				# 回覆訊息
				line_bot_api.reply_message(
					event.reply_token,
					TextSendMessage(text= "Notion Ready" ))
		else:
			line_bot_api.reply_message(
				event.reply_token,
				TextSendMessage(text= "❌Notion not Ready" ))				

	
	# ========= 干支列表 =========
	elif inputMsg[:3] == "干支/":	
		Zhi = "子丑寅卯辰巳午未申酉戌亥"
		dateMode = ""
		runTimeBuf = ""
		indexBuf = ""
		dateBuf = ""
		ganZiiList = inputMsg.split("/")

		# 干支/時/15
		if len( ganZiiList ) == 3:
			dateMode = ganZiiList[1]
			runTimeBuf = ganZiiList[2]

		# 干支/時/15/2026,02,18
		elif len( ganZiiList ) == 4:
			dateMode = ganZiiList[1]
			runTimeBuf = ganZiiList[2]
			if ganZiiList[3] in Zhi:
				indexBuf = ganZiiList[3]
			else:
				dateBuf = ganZiiList[3]				

		# 干支/時/15/2026,02,18/寅
		elif len( ganZiiList ) == 5:
			dateMode = ganZiiList[1]
			runTimeBuf = ganZiiList[2]

			if ganZiiList[3] in Zhi:
				indexBuf,dateBuf = ganZiiList[3],ganZiiList[4]
			else:
				indexBuf,dateBuf = ganZiiList[4],ganZiiList[3]

		ganZi_flexMsgJson_dict = ganZiList_fun( currentTime = dateBuf , dayMode = dateMode , index = indexBuf , runtime = int(runTimeBuf) ) ## 取得起盤介面的json


		# Flex message的容器，把寫好的json放入就可以變成介面
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(
				alt_text='< 干支list >',
				# contents= ganZi_flexMsgJson   # 直接放轉好的 dict
				contents = ganZi_flexMsgJson_dict  # 改用 dict
			)
		)

	## setting
	elif  "set" in inputMsg.lower():
		# jsonData = jsonDataClass( linebotId = user_id ) ## class建立

		returnMsg = jsonData.uiJsonSetting( inputMsg )
		# 回覆訊息
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text= returnMsg  )
		)



	# LINE圖片處理
	elif inputMsg.startswith("+"):
		# img_high, img_low = sixYaoMain(data)

		img_high, img_low  = sixYaoMain ( inputMsg , 
							lineBotId = user_id , 
							lineBotName = displayName , 
							userImage = picUrl )

		
		# 回覆訊息：同時回傳文字 + 圖片
		line_bot_api.reply_message(
			event.reply_token,
			[
				# TextSendMessage(text = "收到"),  # 第一個訊息 可有可無
				ImageSendMessage(             # 第二個訊息 (圖片)
					original_content_url = img_high,
					preview_image_url = img_low
				)
			]
		)



	## 裝卦UI
	elif  "//" in unifiedData(inputMsg):
		ui_cmd_dict = sixYaoMain ( inputMsg , 
						lineBotId = user_id , 
						lineBotName = displayName , 
						userImage = picUrl )

		# jsonData = jsonDataClass( linebotId = user_id ) ## class建立
		jsonData.uiJsonSetting("set temp " + inputMsg ) ## 取完之後刪除
		# exec( cmd )
		print( "UI") 
		print( ui_cmd_dict )
		if inputMsg != "error":

			# Flex message的容器，把寫好的json放入就可以變成介面，之前的寫法太土，這次改好看一點
			line_bot_api.reply_message(
				event.reply_token,
				FlexSendMessage(
					alt_text = '< 裝卦UI >',
					contents = ui_cmd_dict   # 直接放轉好的 dict
				)
			)

	## 修改Title
	elif inputMsg[0] in [ ">","@",":" ]: #字的開頭如果是這些就進入
		changeNote = inputMsg[1:]
		# jsonData = jsonDataClass( linebotId = user_id ) ## class建立
		uiCommand = jsonData.temp ## 取得temp的暫存ui command
		print( jsonData.temp )		

		newCommand = uiCommand.replace( "no title" , changeNote )
		new_flex_json = sixYaoMain( newCommand ,
							lineBotId = user_id , 
							lineBotName = displayName , 
							userImage = picUrl ) # 取得起盤介面的json

		jsonData.uiJsonSetting("set temp none") ## 取完之後刪除
		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(
				alt_text = '< OCR裝卦UI >',
				contents = new_flex_json   # 直接放轉好的 dict
			)
		)

	## 執行程式用
	elif inputMsg[0:4] == "____":
		inputMsg = inputMsg[ 4: ]
		backMsg = ""
		if inputMsg == "up":
			backMsg = jsonToGoogle()
		elif inputMsg == "dn":
			backMsg = googleToJson()
		elif inputMsg == "logup":
			backMsg = uploadCsvToGoogleSheet()
		elif inputMsg == "show":
			pass

		else:
			backMsg = "No command - " + inputMsg

		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage( text= backMsg  )
		)



	else:
		# 回覆訊息
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text= "未知指令: " + inputMsg  )
		)





## 圖片訊息接收
## OCR
@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
	# user_id = event.source.user_id  ##利用reply取得id存至user_id中
	# # 取得 LINE 傳來的圖片 stream
	message_id = event.message.id
		# 取得用戶的id
	user_id = event.source.user_id 
	profile = line_bot_api.get_profile(user_id)
	# ## 用戶line上面的名字
	displayName = profile.display_name 
	## 取得用戶的頭貼
	picUrl = profile.picture_url
	##收到的訊息
	# inputMsg = event.message.text  


	content = line_bot_api.get_message_content(message_id)

	# ui_command = getPicData (content.raw)
	# flexMsgJson = sixYaoMain( ui_command ) # 取得起盤介面的json
	# 讀取所有 bytes
	image_bytes = content.content  # 這才是圖片的 bytes

	ui_command = getPicData(image_bytes)
	print (">>>>>", ui_command )
	# 回覆訊息
	# line_bot_api.reply_message(
	# 	event.reply_token,
	# 	TextSendMessage(text= ui_command  )
	# )
	ui_cmd_dict = sixYaoMain ( ui_command , 
					lineBotId = user_id , 
					lineBotName = displayName , 
					userImage = picUrl )

	# print( "XXX ", ui_command )	
	jsonData = jsonDataClass( linebotId = user_id ) ## class建立
	jsonData.uiJsonSetting("set temp " + ui_command ) ## 取完之後刪除
	# print( "@@@ ", jsonData.temp )
	print( "UI") 
	print( ui_cmd_dict )
	
	## 把message id和裝卦命令存到該使用者的json的temp中
	jsonData = jsonDataClass( linebotId = user_id ) ## class建立
	jsonData.uiJsonSetting( f"set temp {ui_command}" )

	# Flex message的容器，把寫好的json放入就可以變成介面，之前的寫法太土，這次改好看一點
	line_bot_api.reply_message(
		event.reply_token,
		FlexSendMessage(
			alt_text='< OCR裝卦UI >',
			contents= ui_cmd_dict   # 直接放轉好的 dict
		)
	)











## 傳送PUSH訊息
from linebot.v3.messaging import MessagingApi, PushMessageRequest, TextMessage

def pushMsg(msg, user_id = None):
	my_id = "U21eaaf32db85b983a842d9a9da81d8f1"
	if user_id is None:
		user_id = my_id
	try:
		messaging_api = MessagingApi(api_client)  # api_client 是你初始化的 LineBotApiClient
		messaging_api.push_message(
			PushMessageRequest(
				to=user_id,
				messages=[TextMessage(text=msg)]
			)
		)
	except Exception as e:
		print("pushMsg error:", e)








# 接收 postback
@handler.add(PostbackEvent)
def handle_postback(event):

	postDataMsg = event.postback.data
	# user_id = event.source.user_id
	
	user_id = event.source.user_id 
	profile = line_bot_api.get_profile(user_id)
	displayName = profile.display_name 
	picUrl = profile.picture_url

	data = postDataMsg.replace('\u200b', '')

	# 如果是 richmenu 切換的 postback，就直接忽略
	if data.startswith("change-to-"):
		return


	# Notion處理
	elif data.startswith("n+"):
		notion_url = sixYaoMain(data)

		notion_url = sixYaoMain ( data , 
				lineBotId = user_id , 
				lineBotName = displayName , 
				userImage = picUrl )

		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text= notion_url )
		)



	# LINE圖片處理
	elif data.startswith("+"):
		print( "INNNN" )
		# img_high, img_low = sixYaoMain(data)
		img_high, img_low  = sixYaoMain ( data , 
							lineBotId = user_id , 
							lineBotName = displayName , 
							userImage = picUrl )

		print( img_high, img_low )
		# 回覆訊息：同時回傳文字 + 圖片
		line_bot_api.reply_message(
			event.reply_token,
			[
				TextSendMessage(text = "收到"),  # 第一個訊息 可有可無
				ImageSendMessage(             # 第二個訊息 (圖片)
					original_content_url = img_high,
					preview_image_url = img_low
				)
			]
		)



	else:
		# fallback
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text="未知指令格式")
		)





	# # 呼叫你的程式
	# # image_url = sixYaoMain( postDataMsg )

	# # 呼叫上傳notion的程式
	# # sixYaoMain( data )
	# # pushToNotion( apiToken , pageId , imageUrl , titleText )

	# if postDataMsg[0] == "+":
	# 	imageUrl_high, imageUrl_low = sixYaoMain( postDataMsg ) # 取得盤面的高解析與低解析圖片連結


	# 	# if ( "https:" not in imageUrl_high ) or ( "https:" not in imageUrl_low )   :
	# 	# 	reply_message = "圖床錯誤"
	# 	# 	line_bot_api.reply_message(
	# 	# 			event.reply_token,
	# 	# 			TextSendMessage( text= reply_message )
	# 	# 	)
	# 	# else:
	# 	# 	img_message = ImageSendMessage(
	# 	# 			original_content_url= imageUrl_high,  ## 高解析
	# 	# 			preview_image_url= imageUrl_low		  ## 低解析
	# 	# 	)
	# 	# 	line_bot_api.reply_message( event.reply_token, img_message )


	# 	# 回覆訊息：同時回傳文字 + 圖片
	# 	line_bot_api.reply_message(
	# 		event.reply_token,
	# 		[
	# 			TextSendMessage(text="收到"),  # 第一個訊息 可有可無
	# 			ImageSendMessage(             # 第二個訊息 (圖片)
	# 				original_content_url=imageUrl_high,
	# 				preview_image_url=imageUrl_low
	# 			)
	# 		]
	# 	)

































# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))


if __name__ == "__main__":
	app.run()
	