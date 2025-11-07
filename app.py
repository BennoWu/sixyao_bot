# -*- coding: utf-8 -*-
from ocr_work import getPicData
from combineDataMain import sixYaoMain,unifiedData

from logBackup import uploadCsvToGoogleSheet
# from supabase_io import *
from supabase_io import get_user_data
from cloudinary_helper import delete_older_than

from flexLayout_tool import ganZiList_fun , yearListFlexLayout , getFlexMessage_GZ

from fourPillar_tool import checkYear
from fourPillar_tool import ganZhi_Dict ## 六十甲子的字典




from sixYaoJsonDataClass import *

import os , threading
from flask import Flask, request, abort


# ⭐ LINE Bot SDK v3 imports
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, PostbackEvent, TextMessageContent, ImageMessageContent , StickerMessageContent
from linebot.v3.messaging import (
	Configuration,
	ApiClient,
	MessagingApi,
	MessagingApiBlob,  # 🔥 新增這個
	ReplyMessageRequest,
	PushMessageRequest,
	TextMessage,
	ImageMessage as ImageMessageType,
	FlexMessage,
	FlexContainer,
	StickerMessage
)

app = Flask(__name__)





from dotenv import load_dotenv
load_dotenv()


# 在檔案最上方，import 後面加
line_bot_api.get_bot_info()  # 啟動時就初始化 LINE SDK


# ⭐ v3 初始化方式
configuration = Configuration(
	access_token=os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')
)
api_client = ApiClient(configuration)
line_bot_api = MessagingApi(api_client)
blob_api = MessagingApiBlob(api_client)  # 🔥 新增這行 - 處理圖片下載
handler = WebhookHandler(os.environ.get('LINE_CHANNEL_SECRET'))

import time
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


# ⭐ pushMsg 改用 v3
def pushMsg(msg, user_id=None):
	my_id = "U21eaaf32db85b983a842d9a9da81d8f1"
	if user_id is None:
		user_id = my_id
	try:
		line_bot_api.push_message(
			PushMessageRequest(
				to=user_id,
				messages=[TextMessage(text=msg)]
			)
		)
	except Exception as e:
		print("pushMsg error:", e)


## 多線程 - 刪除圖庫中過期的圖檔
def delayed_cleanup(days):
	try:
		print(f"🧹 delayed_cleanup start for {days} days", flush=True)
		delete_older_than(folder="line_temp", days=days)
		print("✅ delayed_cleanup done", flush=True)
		# pushMsg( "殺完圖檔" )
	except Exception as e:
		print("delayed_cleanup error:", e, flush=True)


## 多線程 - 儲存LOG至GOOGLE
def delayed_upLog():
	try:
		print(f"🧹 log upload to google sheet", flush=True)
		uploadCsvToGoogleSheet()
		# pushMsg( "上傳log完成" )
	except Exception as e:
		print("delayed_upLog error:", e, flush=True)

	# # 背景備份
	# t = threading.Thread(target=delayed_upLog)
	# t.start()


## 多線程 - 儲存JSON至GOOGLE
def delayed_upJson():
	try:
		print(f"🧹 user setting json upload to google sheet", flush=True)
		jsonToGoogle()
		# pushMsg( "上傳json完成" )
	except Exception as e:
		print("delayed_upJson error:", e, flush=True)

# 	# 建立兩個執行緒
# 	t1 = threading.Thread( target=delayed_upLog )
# 	t2 = threading.Thread( target=delayed_upJson )

# # 啟動執行緒
# 	t1.start()
# 	t2.start()

# # 等待兩個執行緒都結束
# 	t1.join()
# 	t2.join()



## 取出字典檔中的命令
def getZhuangGuaData(ui_dict):
	def dfs(obj):
		if isinstance(obj, dict):
			# 找 button + label = 裝卦
			if obj.get("type") == "button":
				action = obj.get("action", {})
				if action.get("label") == "裝卦":
					return action.get("data")

			# 繼續往下找
			for v in obj.values():
				result = dfs(v)
				if result:
					return result

		elif isinstance(obj, list):
			for item in obj:
				result = dfs(item)
				if result:
					return result

		return None

	return dfs(ui_dict)

# value = getZhuangGuaData(ui_cmd_dict)
# print(value)


@app.route("/")
def home():
    current_time = time.time()
    return f"Bot is alive! {current_time}"






@app.route("/")
def home():
	logger.debug("收到 GET / 請求")
	return 'home OK'


@app.route("/callback", methods=['POST'])
def callback():
	signature = request.headers['X-Line-Signature']
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)

	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		print("Invalid signature. Please check your channel access token/channel secret.")
		abort(400)

	return 'OK'


# ⭐ v3 的 handler 寫法
@handler.add(MessageEvent, message=TextMessageContent )
def handle_message(event):
	my_id = "U21eaaf32db85b983a842d9a9da81d8f1"
	# 取得用戶資訊
	user_id = event.source.user_id
	
	# ⭐ v3 取得 profile 的方式
	profile = line_bot_api.get_profile( user_id )
	displayName = profile.display_name
	picUrl = profile.picture_url
	
	# ⭐ v3 取得訊息內容
	inputMsg = event.message.text
	inputMsg = inputMsg.replace('\u200b', '')
	
	print(">:", inputMsg)
	print( unifiedData(inputMsg) )

	returnMsg = ""

	# 建立 jsonData
	jsonData = jsonDataClass(
		linebotId = user_id,
		linebotUserName = displayName,
		userImage = picUrl,
		command = inputMsg
	)

	userData = {
		"linebotId": jsonData.linebotId,
		"linebotUserName": jsonData.linebotUserName,
		"utc": jsonData.utc,
		"tipsMode": jsonData.tipsMode,
		"notionToken_pageId": jsonData.notionToken_pageId
	}

	print("userData:", userData)

	# 權限檢查
	if jsonData.switch.upper() != "ON"  and  user_id != my_id:	
	# if jsonData.switch.upper() != "ON":
		print("404")

		# V3 回覆貼圖
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[
					StickerMessage(
						package_id="8522",
						sticker_id="16581285"
					)
				]
			)
		)
		return

	# 設定模式
	if ("set" in inputMsg.lower()) or ("utc" in inputMsg.lower()):
		returnMsg = jsonData.uiJsonSetting(inputMsg)



	elif inputMsg == "id":
		returnMsg = f"{user_id}//{displayName}//{picUrl}"



	# 歲次干支 - 輸入年份 - 輸入干支取得
	elif ( inputMsg.isdigit() == True ) or ( inputMsg in ganZhi_Dict.values() ):
	# elif inputMsg == "西元年","民國年","年干支":
		ui_cmd_dict = getFlexMessage_GZ ( checkYear ( yearData = inputMsg ) )
		# ⭐ v3 的 Flex Message
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[
					FlexMessage(
						alt_text='< 歲次UI >',
						contents=FlexContainer.from_dict(ui_cmd_dict)
					)
				]
			)
		)
		return


	elif inputMsg.startswith("--"):
		ui_cmd_dict = yearListFlexLayout( inputMsg[2:] ) 

		# ⭐ v3 的 Flex Message
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[
					FlexMessage(
						alt_text='< 年干支UI >',
						contents=FlexContainer.from_dict(ui_cmd_dict)
					)
				]
			)
		)
		return



	# 測試 Notion
	elif inputMsg.lower() == "notion":
		data = get_user_data(user_id)
		if data:
			print(f"Token: {data['notion_token']}")
			print(f"Page ID: {data['page_id']}")
			token_buf = data['notion_token']
			pageId_buf = data['page_id']

			notionAccount = checkNotionAcc(token_buf, pageId_buf)
			if notionAccount == True:
				returnMsg = "Notion Ready"
		else:
			returnMsg = "⚠Notion not Ready"

	# 干支列表
	elif inputMsg[:3] == "干支/":
		Zhi = "子丑寅卯辰巳午未申酉戌亥"
		dateMode = ""
		runTimeBuf = ""
		indexBuf = ""
		dateBuf = ""
		ganZiiList = inputMsg.split("/")

		if len(ganZiiList) == 2:
			dateMode = ganZiiList[1]
			runTimeBuf = 6
		elif len(ganZiiList) == 3:
			dateMode = ganZiiList[1]
			runTimeBuf = ganZiiList[2]
		elif len(ganZiiList) == 4:
			dateMode = ganZiiList[1]
			runTimeBuf = ganZiiList[2]
			if ganZiiList[3] in Zhi:
				indexBuf = ganZiiList[3]
			else:
				dateBuf = ganZiiList[3]
		elif len(ganZiiList) == 5:
			dateMode = ganZiiList[1]
			runTimeBuf = ganZiiList[2]
			if ganZiiList[3] in Zhi:
				indexBuf, dateBuf = ganZiiList[3], ganZiiList[4]
			else:
				indexBuf, dateBuf = ganZiiList[4], ganZiiList[3]

		ganZi_flexMsgJson_dict = ganZiList_fun(
			currentTime=dateBuf,
			dayMode=dateMode,
			index=indexBuf,
			runtime=int(runTimeBuf)
		)

		# ⭐ v3 的 Flex Message 回覆方式
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[
					FlexMessage(
						alt_text='< 干支list >',
						contents=FlexContainer.from_dict(ganZi_flexMsgJson_dict)
					)
				]
			)
		)
		return

	# PIL圖片上傳
	elif inputMsg.startswith("+"):
		img_high, img_low = sixYaoMain( inputMsg, userData )

		# ⭐ v3 的圖片訊息回覆
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[
					ImageMessageType(
						original_content_url=img_high,
						preview_image_url=img_low
					)
				]
			)
		)

		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", flush=True)

		# 背景清理
		t = threading.Thread(target=delayed_cleanup, args=(15,))
		t.start()
		return







	# 卦象UI
	elif "//" in unifiedData(inputMsg):
		ui_cmd_dict = sixYaoMain(inputMsg, userData)

		print("UI")
		# print(ui_cmd_dict)
		if "Untitled" in inputMsg:
			save_json_data(user_id, "temp", ui_command )
		
		if inputMsg != "error":
			# ⭐ v3 的 Flex Message
			line_bot_api.reply_message(
				ReplyMessageRequest(
					reply_token=event.reply_token,
					messages=[
						FlexMessage(
							alt_text='< 卦象UI >',
							contents=FlexContainer.from_dict(ui_cmd_dict)
						)
					]
				)
			)
			return

	# 修改Title
	elif inputMsg[0] in [">", "#", ":", "@", "#"]:
		changeNote = inputMsg[1:]
		changeNote = changeNote.replace(' ', '')
		# changeNote = changeNote.replace('\n', '^')
		print( "change note === " , changeNote )
		uiCommand = get_json_item_data(user_id, "temp")

		if uiCommand:
			newCommand = uiCommand.replace("Untitled", changeNote)
			new_flex_json = sixYaoMain( newCommand, userData )


			## 修改完UI之後就把json中的暫存清空
			save_json_data(user_id, "temp", None, json_path='__sixYoSet__.json')

			# ⭐ v3 的 Flex Message
			line_bot_api.reply_message(
				ReplyMessageRequest(
					reply_token=event.reply_token,
					messages=[
						FlexMessage(
							alt_text='< OCR卦象UI >',
							contents=FlexContainer.from_dict(new_flex_json)
						)
					]
				)
			)
			return
		else:
			returnMsg = "請先傳送圖片或卦象"

	# 執行程式用
	elif inputMsg[0:4] == "____":
		inputMsg = inputMsg[4:].lower()
		
		## ========== upload data ==========
		if inputMsg in ["up", "upload"]:
			returnMsg = jsonToGoogle()

		## ========== download data ==========
		elif inputMsg in ["dn", "download"]:
			returnMsg = googleToJson()

		## ========== upload log ==========
		elif inputMsg in ["logup", "uplog"]:
			returnMsg = uploadCsvToGoogleSheet()

		## ========== show all user data ==========
		elif inputMsg in ["show", "list"]:
			showDict = get_all_user_flex()

			# ⭐ v3 的 Flex Message
			line_bot_api.reply_message(
				ReplyMessageRequest(
					reply_token=event.reply_token,
					messages=[
						FlexMessage(
							alt_text='< list all >',
							contents=FlexContainer.from_dict(showDict)
						)
					]
				)
			)

		# 	# 建立兩個執行緒
		# 	t1 = threading.Thread( target=delayed_upLog )
		# 	t2 = threading.Thread( target=delayed_upJson )

		# # 啟動執行緒
		# 	t1.start()
		# 	t2.start()

		# # 等待兩個執行緒都結束
		# 	t1.join()
		# 	t2.join()

			return
		else:
			returnMsg = f"No command - {inputMsg}"

	else:
		returnMsg = f"未知指令: {inputMsg}"

	# 統一回覆文字訊息
	if returnMsg:
		# ⭐ v3 的文字訊息回覆
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[TextMessage(text=returnMsg)]
			)
		)


# ⭐ v3 的圖片訊息處理
@handler.add(MessageEvent, message = ImageMessageContent)
def handle_image_message(event):
	message_id = event.message.id
	user_id = event.source.user_id
	userData = get_user_json_data(user_id)


	# 🔥 改用 blob_api 取得圖片內容
	message_content = blob_api.get_message_content(message_id)
	image_bytes = message_content
	
	# OCR 處理
	ui_command = getPicData(image_bytes)
	print(">>>>>", ui_command)
	if ui_command == False:
		ui_command = getPicData(image_bytes)
		print(">>>>> AGAIN")		

	## ======== ocr 判斷不出時 =========
	if ui_command == False: 

		# ⭐ v3 的文字訊息回覆
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[TextMessage(text= "OCR error")]
			)
		)
	## ======== ocr 判斷正確時 =========
	else:
		ui_cmd_dict = sixYaoMain( ui_command , userData )

		save_json_data(user_id, "temp", ui_command, json_path='__sixYoSet__.json')

		print("UI")
		print(ui_cmd_dict)

		# ⭐ v3 的 Flex Message 回覆
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[
					FlexMessage(
						alt_text='< OCR卦象UI >',
						contents=FlexContainer.from_dict(ui_cmd_dict)
					)
				]
			)
		)





# ⭐ v3 的 Postback 處理
@handler.add(PostbackEvent)
def handle_postback(event):
	postDataMsg = event.postback.data
	user_id = event.source.user_id

	data = postDataMsg.replace('\u200b', '')

	userData = get_user_json_data(user_id)
	print("@@@ userData:", userData)

	# richmenu 切換
	if data.startswith("change-to-"):
		return

	# Notion 處理
	elif data.startswith("n+"):
		notion_url = sixYaoMain(data, userSetting=userData)

		# ⭐ v3 文字訊息回覆
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[TextMessage(text=notion_url)]
			)
		)

	# 文字版UI 處理
	elif data.startswith("t+"):
		text_UI = sixYaoMain( data , userSetting=userData)

		# ⭐ v3 文字訊息回覆
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[TextMessage(text= text_UI)]
			)
		)


	# 卦象完成圖片處理
	elif data.startswith("+"):
		img_high, img_low = sixYaoMain(data, userSetting=userData)

		print("image url:")
		print(img_high, img_low)
		
		# ⭐ v3 圖片訊息回覆
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[
					ImageMessageType(
						original_content_url=img_high,
						preview_image_url=img_low
					)
				]
			)
		)

		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", flush=True)

		# 背景清理
		t = threading.Thread(target=delayed_cleanup, args=(15,))
		t.start()

	else:
		# ⭐ v3 fallback 回覆
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[TextMessage(text="未知指令格式")]
			)
		)





@handler.add(MessageEvent, message=StickerMessageContent)
def handle_sticker_message(event):
	user_id = event.source.user_id
	stk_id = event.message.package_id + "-" + event.message.sticker_id
	
	# V3 回覆貼圖
	line_bot_api.reply_message(
		ReplyMessageRequest(
			reply_token=event.reply_token,
			messages=[
				StickerMessage(
					package_id="8522",
					sticker_id="16581280"
				)
			]
		)
	)

if __name__ == "__main__":
	app.run()