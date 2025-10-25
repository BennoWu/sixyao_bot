# from combineData import *
from ocr_work import *
from combineDataMain import *
from logBackup import *
from  supabase_io import *
import threading

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


from dotenv import load_dotenv
load_dotenv()  # 載入 .env 檔案
# cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME')


## 裝卦初號機
line_bot_api = LineBotApi(os.environ.get('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.environ.get('LINE_CHANNEL_SECRET'))





import logging
from flask import Flask

app = Flask(__name__)

# 設定 logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()



## 傳送PUSH訊息
from linebot.v3.messaging import MessagingApi, PushMessageRequest, TextMessage

def pushMsg(msg, user_id = None):
	my_id = "U21eaaf32db85b983a842d9a9da81d8f1"
	if user_id is None:
		user_id = my_id
	try:
		messaging_api = MessagingApi(line_bot_api)  # api_client 是你初始化的 LineBotApiClient
		messaging_api.push_message(
			PushMessageRequest(
				to=user_id,
				messages=[TextMessage(text=msg)]
			)
		)
	except Exception as e:
		print("pushMsg error:", e)


# --- 延遲清除執行緒 ---
def delayed_cleanup( days ):
	time.sleep(5)
	pushMsg(f"🧹 開始清理 {days} 天前的圖片…")
	num = delete_older_than(folder="line_temp", days = days )
	pushMsg(f"✅ {num} 張圖清理完成。")




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


	returnMsg = ""

	# print( unifiedData( inputMsg , strong_sep='//', sep_for_app= "||") )
	## json建立
	jsonData = jsonDataClass( linebotId = user_id  ,
								linebotUserName = displayName ,
								userImage = picUrl ,
								command = inputMsg )

	userData = {
		"linebotId"     : jsonData.linebotId,
		"linebotUserName"      : jsonData.linebotUserName,
		"utc"  : jsonData.utc,        
		"tipsMode"  : jsonData.tipsMode,  
		"notionToken_pageId"    : jsonData.notionToken_pageId
	}

	print( "userData:" , userData )




# def connect_db(cfg):
#     print(f"Connecting to {cfg['user']}@{cfg['host']}:{cfg['port']}/{cfg['dbname']}")

# db_config = {
#     "host": "localhost",
#     "port": 5432,
#     "user": "admin",
#     "password": "1234",
#     "dbname": "mydb"
# }

# connect_db(db_config)




	# 如果不是ON，就代表權限被OFF掉了，程式中止
	if jsonData.switch.upper() != "ON": ## user的switch項如果不是ON，表示權限關閉狀態
		print ( "404" )
		exit()

	# 設定模式
	elif ("set" in inputMsg.lower())  or ("utc" in inputMsg.lower()) :
		returnMsg = jsonData.uiJsonSetting( inputMsg )
		# lineSend_fun( replyUrl )
		returnMsg =  returnMsg
		# return returnMsg


	elif inputMsg == "id":
		inputMsg = user_id +"//" +displayName +"//"+picUrl


	## 測試是否可運作
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

				# # 回覆訊息
				returnMsg = "Notion Ready"
				# line_bot_api.reply_message(
				# 	event.reply_token,
				# 	TextSendMessage(text= "Notion Ready" ))
		else:
			returnMsg = "❌Notion not Ready" 
			# line_bot_api.reply_message(
			# 	event.reply_token,
			# 	TextSendMessage(text= "❌Notion not Ready" ))				

	
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

	# ## setting
	# elif  "set" in inputMsg.lower():
	# 	# jsonData = jsonDataClass( linebotId = user_id ) ## class建立

	# 	returnMsg = jsonData.uiJsonSetting( inputMsg )
	# 	# 回覆訊息
	# 	line_bot_api.reply_message(
	# 		event.reply_token,
	# 		TextSendMessage(text= returnMsg  )
	# 	)


	# 裝卦圖片上傳
	elif inputMsg.startswith("+"):

		img_high, img_low  = sixYaoMain ( inputMsg ,  userData )
		
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


		# 背景清理：延遲執行，不影響主流程
		threading.Thread(
			target=lambda: delayed_cleanup( 15 ),
			daemon=True
		).start()




	## 裝卦UI
	elif  "//" in unifiedData(inputMsg):

		ui_cmd_dict = sixYaoMain ( inputMsg , userData )

		# ui_cmd_dict = sixYaoMain ( inputMsg , 
		# 				lineBotId = user_id , 
		# 				lineBotName = displayName , 
		# 				userImage = picUrl )


		# jsonData = jsonDataClass( linebotId = user_id ) ## class建立
		# jsonData.uiJsonSetting("set temp " + inputMsg ) ## 取完之後刪除
		# save_json_data(  user_id, "temp", None , json_path='__sixYoSet__.json' ) ## json 直接存取

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
	elif inputMsg[0] in [ ">","#",":" ]: #字的開頭如果是這些就進入
		changeNote = inputMsg[1:]
		# jsonData = jsonDataClass( linebotId = user_id ) ## class建立
		# uiCommand = jsonData.temp ## 取得temp的暫存ui command
		# print( jsonData.temp )		
		uiCommand = get_json_item_data( user_id, "temp" )

		newCommand = uiCommand.replace( "no title" , changeNote )
		new_flex_json = sixYaoMain( newCommand , userData ) # 取得起盤介面的json

		# jsonData.uiJsonSetting("set temp none") ## 取完之後刪除
		save_json_data(  user_id, "temp", None , json_path='__sixYoSet__.json' ) ## json 直接存取

		line_bot_api.reply_message(
			event.reply_token,
			FlexSendMessage(
				alt_text = '< OCR裝卦UI >',
				contents = new_flex_json   # 直接放轉好的 dict
			)
		)

	## 執行程式用
	elif inputMsg[0:4] == "____":
		inputMsg = inputMsg[ 4: ].lower()
		# backMsg = ""
		if inputMsg in ["up","upload"]:
			returnMsg = jsonToGoogle()
		elif inputMsg in  ["dn","download"]:
			returnMsg = googleToJson()
		elif inputMsg in ["logup","uplog" ]:
			returnMsg = uploadCsvToGoogleSheet()
		elif inputMsg in ["show","list"]:
			showDict = get_all_user_flex()

			line_bot_api.reply_message(
				event.reply_token,
				FlexSendMessage(
					alt_text='< list all >',
					contents= showDict   # 直接放轉好的 dict
				)
			)

		else:
			returnMsg = "No command - " + inputMsg

		# line_bot_api.reply_message(
		# 	event.reply_token,
		# 	TextSendMessage( text= backMsg  )
		# )

	else:
		returnMsg = "未知指令:  " + inputMsg 

	# 回覆訊息
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage( text= returnMsg  )
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
	# profile = line_bot_api.get_profile(user_id)
	# # ## 用戶line上面的名字
	# displayName = profile.display_name 
	# ## 取得用戶的頭貼
	# picUrl = profile.picture_url
	# ##收到的訊息
	# # inputMsg = event.message.text  


	content = line_bot_api.get_message_content(message_id)
	# 讀取所有圖片的 bytes 
	image_bytes = content.content

	## 丟入OCR判斷後取得裝卦UI的json
	## 取得標準格式 2025/9/4/11/35 // 00010$ 
	ui_command = getPicData(image_bytes) ## OCR

	print (">>>>>", ui_command )
	# 回覆訊息
	# line_bot_api.reply_message(
	# 	event.reply_token,
	# 	TextSendMessage(text= ui_command  )
	# )

	ui_cmd_dict = sixYaoMain ( ui_command , userSetting = None )

	# ui_cmd_dict = sixYaoMain ( ui_command , 
	# 				lineBotId = user_id , 
	# 				lineBotName = displayName , 
	# 				userImage = picUrl )

	# print( "XXX ", ui_command )	
	# jsonData = jsonDataClass( linebotId = user_id ) ## class建立
	# jsonData.uiJsonSetting("set temp " + ui_command ) ## 取完之後刪除


	save_json_data(  user_id, "temp", ui_command , json_path='__sixYoSet__.json')


	# print( "@@@ ", jsonData.temp )
	print( "UI") 
	print( ui_cmd_dict )
	
	## 把message id和裝卦命令存到該使用者的json的temp中
	# jsonData = jsonDataClass( linebotId = user_id ) ## class建立
	# jsonData.uiJsonSetting( f"set temp {ui_command}" )



	# Flex message的容器，把寫好的json放入就可以變成介面，之前的寫法太土，這次改好看一點
	line_bot_api.reply_message(
		event.reply_token,
		FlexSendMessage(
			alt_text='< OCR裝卦UI >',
			contents= ui_cmd_dict   # 直接放轉好的 dict
		)
	)
















#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################





# 接收 postback
@handler.add(PostbackEvent)
def handle_postback(event):

	# from jsonFun import get_user_data

	postDataMsg = event.postback.data
	user_id = event.source.user_id 
	# profile = line_bot_api.get_profile(user_id)
	# displayName = profile.display_name 
	# picUrl = profile.picture_url

	data = postDataMsg.replace('\u200b', '')

	## 取得字典
	userData = get_user_json_data( user_id  ) 

	print( "@@@ userData:" , userData )
# @@@ userData: { 'linebot_Id': 'U21eaaf32db85b983a842d9a9da81d8f1', 
# 				'user_name': 'Benno', 
# 				'user_utc_hour': 8, 
# 				'user_tipsMode': 'ON', 
# 				'user_notion': None}





	# 如果是 richmenu 切換的 postback，就直接忽略
	if data.startswith("change-to-"):
		return


	# Notion處理
	elif data.startswith("n+"):
		# notion_url = sixYaoMain(data)

		notion_url = sixYaoMain ( data , userSetting = userData  )

		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text= notion_url )
		)



	# 裝卦完成圖片處理
	elif data.startswith("+"):
		print( "INNNN" )
		# img_high, img_low = sixYaoMain(data)
		img_high, img_low  = sixYaoMain ( data , userSetting = userData )

		print( img_high, img_low )
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

	else:
		# fallback
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(text="未知指令格式")
		)








# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))


if __name__ == "__main__":
	app.run()
	