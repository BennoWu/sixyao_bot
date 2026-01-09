# -*- coding: utf-8 -*-
from ocr_work import getPicData
from combineDataMain import sixYaoMain,unifiedData

from logBackup import uploadCsvToGoogleSheet
from logBackup import ( logDataFun as logBK_logDataFun )
# from supabase_io import *
from supabase_io import get_user_data,supabase_health_check
from cloudinary_helper import delete_older_than

from flexLayout_tool import ganZiList_fun , yearListFlexLayout , getFlexMessage_GZ , getDrawRiceGua , howToUse , howToUseDate

from fourPillar_tool import checkYear,getNowTime
from fourPillar_tool import ganZhi_Dict ## 六十甲子的字典

from flexLayout_tool import sSixZnUi ## 小六壬


from lineSend import *

from iching_flexLayout import * ## 易經卦UI

from sixYaoJsonDataClass import *

import os , threading , re
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

# ## 讓所有print都失效
# import builtins
# builtins.print = lambda *args, **kwargs: None




app = Flask(__name__)





from dotenv import load_dotenv
load_dotenv()




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

# 在檔案最上方，import 後面加
line_bot_api.get_bot_info()  # 啟動時就初始化 LINE SDK

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


# addToJson( linebotId = "U21eaaf32db85b983a842d9a9da81d8f1" )
rtn = googleToJson()
pushMsg("✈️ start now...", user_id = None )

# ## 多線程 - 刪除圖庫中過期的圖檔
# def delayed_cleanup(days):
# 	try:
# 		print(f"🧹 delayed_cleanup start for {days} days", flush=True)
# 		delete_older_than(folder="line_temp", days=days)
# 		print("✅ delayed_cleanup done", flush=True)
# 		# pushMsg( "殺完圖檔" )
# 	except Exception as e:
# 		print("delayed_cleanup error:", e, flush=True)


## 多線程 - 儲存LOG至GOOGLE
# def delayed_upLog():
# 	try:
# 		print(f"🧹 log upload to google sheet", flush=True)
# 		uploadCsvToGoogleSheet()
# 		# pushMsg( "上傳log完成" )
# 	except Exception as e:
# 		print("delayed_upLog error:", e, flush=True)

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


from datetime import datetime

# 天干地支列表
TEN = "甲乙丙丁戊己庚辛壬癸"
ZHI = "子丑寅卯辰巳午未申酉戌亥"

def parse_ganzhi_input(inputMsg):
	"""
	輸入範例：
	干支/日/2025/08/31/15/48/戌
	干支/日/10
	干支/日/2025/08/31/15/48
	干支/日/10/戌
	干支/日/2025/08/31/15/48/戌
	"""

	parts = [p.strip() for p in inputMsg.split("/") if p.strip()]

	if len(parts) < 2:
		raise ValueError("格式錯誤，至少要有 干支/日")

	# 固定前兩個
	cmdType = parts[0]
	dayMode = parts[1]

	runtime = None
	indexBuf = ""
	dateParts = []

	# 從第三個開始解析
	for item in parts[2:]:
		# 純數字 → runtime 或日期段
		if item.isdigit():
			num = int(item)
			if len(dateParts) == 0 and num >= 1000:
				# 第一個大於1000的數字當作年份 → 日期開始
				dateParts.append(num)
			elif len(dateParts) > 0:
				# 日期的後續部分
				dateParts.append(num)
			else:
				# 單獨數字 → runtime
				runtime = num
		elif any(c in TEN+ZHI for c in item):
			# 含天干地支 → index
			indexBuf = item
		else:
			# 其他情況 → 忽略或補強
			pass

	# runtime 預設值
	if runtime is None:
		runtime = 9

	# 日期組合成字串
	dateBuf = ""
	if dateParts:
		dateBuf = "/".join(str(d).zfill(2) if i>0 else str(d) for i,d in enumerate(dateParts))

	return cmdType, dayMode, runtime, dateBuf, indexBuf




import re

TIME_MODES = ["日", "時", "月", "節氣"]

def normalize_time_command(inputMsg):
	msg = inputMsg.strip()
	result = {
		"normalized": None,
		"mode": None,
		"runtime": None,
		"matched": False,
	}

	# 移除空白（不動其他符號，讓後面 parse 吃）
	msg = re.sub(r"\s+", "", msg)

	for mode in TIME_MODES:
		# 規則：
		# 1. 可有「干支」
		# 2. mode 後可接數字
		# 3. mode 後面若有 /xxx 就保留
		pattern = rf"^(?:干支)?{mode}(?:(\d+))?(.*)$"
		m = re.match(pattern, msg)

		if not m:
			continue

		runtime = m.group(1)
		tail = m.group(2) or ""

		# runtime 預設（只有單一「日 / 時 / 月 / 節氣」）
		if runtime is None:
			runtime = "10"

		normalized = f"干支/{mode}/{runtime}{tail}"

		result.update({
			"normalized": normalized,
			"mode": mode,
			"runtime": int(runtime),
			"matched": True
		})
		return result

	return result





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




# @app.route("/", methods=['GET'])
# def home():
#     return "Bot is running", 200



bufList = ["坤為地","山地剝","水地比","風地觀","雷地豫","火地晉","澤地萃","天地否","地山謙","艮為山","水山蹇","風山漸","雷山小過","火山旅","澤山咸","天山遯","地水師","山水蒙","坎為水","風水渙","雷水解","火水未濟","澤水困","天水訟","地風升","山風蠱","水風井","巽為風","雷風恆","火風鼎","澤風大過","天風姤","地雷復","山雷頤","水雷屯","風雷益","震為雷","火雷噬嗑","澤雷隨","天雷無妄","地火明夷","山火賁","水火既濟","風火家人","雷火豐","離為火","澤火革","天火同人","地澤臨","山澤損","水澤節","風澤中孚","雷澤歸妹","火澤睽","兌為澤","天澤履","地天泰","山天大畜","水天需","風天小畜","雷天大壯","火天大有","澤天夬","乾為天"]








@app.route("/")
def home():
	# current_time = time.time()
	logger.debug("收到 GET / 請求")
	return 'home OK'



## 上傳備份用，從uptimerobot呼叫 https://web-production-e20a6.up.railway.app/upload-csv-task
## Render用的 https://sixyao-bot.onrender.com/upload-csv-task
## 12小時備份一次
@app.route('/upload-csv-task', methods=['GET'])
def upload_csv_task():
	try:
		# 直接執行，不用管時間邏輯
		print( jsonToGoogle() )
		print( uploadCsvToGoogleSheet() )
		print( delete_older_than(folder="line_temp", days= 15 ) )
		
		print(f"上傳任務執行成功")
		pushMsg(f"上傳任務執行成功", user_id = None )
		return 'OK', 200
		
	except Exception as e:
		print(f"上傳任務失敗: {str(e)}")
		return f'Error: {str(e)}', 500


# 24小時叫一次
# 新增:專門保持 Supabase 活躍的輕量端點
@app.route('/health', methods=['GET'])
def health():
	return supabase_health_check()


	

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




# 設定管理員的 User ID（可以從 LINE Bot 後台或 event 中取得）
ADMIN_USER_ID = "YOUR_ADMIN_USER_ID"


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
	inputMsg = inputMsg.strip()
	
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
	if user_id != my_id:
		sendMessage( text = displayName + ":" + inputMsg  )
	# # if user_id == my_id:
	# try:
	# 	sendMessage( text = displayName + ":" + inputMsg  )
	# 	# pushMsg( displayName + ":" + inputMsg , user_id = "U21eaaf32db85b983a842d9a9da81d8f1" )
	# except Exception as e:
	# 	pushMsg( e )


	print("userData:", userData)

	linebotId = userData["linebotId"]
	linebotUserName = userData["linebotUserName"]
# current_time = time.time()
	## 所有的輸入都寫入log 
	if inputMsg[0:4] != "____":
		logBK_logDataFun( userID = linebotId  , userName = linebotUserName , logTime = getNowTime( utc_hour = 8 ) , inputData = inputMsg )

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
		jsonToGoogle()

		# logBK_logDataFun( userID = linebotId  , userName = linebotUserName , logTime = "", inputData = inputMsg )



	# elif inputMsg.lower() == "id":
	# 	returnMsg = f"{user_id}//{displayName}//{picUrl}"


	# elif inputMsg.lower() == "info":
	# 	returnMsg = get_user_info(user_id)

	elif inputMsg.lower() == "help":
		how_dict = howToUse()
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[
					FlexMessage(
						alt_text='< 使用說明 >',
						contents=FlexContainer.from_dict(how_dict)
					)
				]
			)
		)
		return


	elif inputMsg.lower() == "datehelp":
		how_dict = howToUseDate()
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[
					FlexMessage(
						alt_text='< 日期干支說明 >',
						contents=FlexContainer.from_dict(how_dict)
					)
				]
			)
		)
		return





	elif ("["  in inputMsg )  and ("]"  in inputMsg ):
		returnMsg = "⚠ 六十四卦資料待補"



	elif inputMsg.startswith("#"):

		iching_dict = ichingGuaUI( inputMsg )
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[
					FlexMessage(
						alt_text='< 易經卦說明 >',
						contents=FlexContainer.from_dict(iching_dict)
					)
				]
			)
		)
		return






	# 歲次干支 - 輸入年份 - 輸入干支取得
	## 兩位數(民國) ，四位數(西元) 可通過
	# elif (  bool(re.fullmatch(r'\d{2}|\d{4}',  str(returnMsg).strip())) ) or ( inputMsg in ganZhi_Dict.values() ):
	elif (inputMsg.isdigit() and 1 < int(inputMsg) < 3000) or (inputMsg in ganZhi_Dict.values()):		
	# elif inputMsg == "西元年","民國年","年干支":
		print ( "干支模式")
		ui_cmd_dict = getFlexMessage_GZ ( checkYear ( yearData = inputMsg ) )
		# logBK_logDataFun( userID = linebotId  , userName = linebotUserName , logTime = "", inputData = inputMsg )
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

	## 年列表
	elif inputMsg.startswith("--"):
		ui_cmd_dict = yearListFlexLayout( inputMsg[2:] ) 

		# logBK_logDataFun( userID = linebotId  , userName = linebotUserName , logTime = "", inputData = inputMsg )
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
				returnMsg = "\udbc0\udc93 Notion Ready"
		else:
			returnMsg = "\udbc0\udc91 Notion not Ready"
			save_json_data(user_id, "notionToken_pageId", None ) 
# ⚠


	# 干支列表
	# elif inputMsg[:2] == "干支":
	# 	Zhi = "子丑寅卯辰巳午未申酉戌亥"
	# 	dateMode = ""
	# 	runTimeBuf = ""
	# 	indexBuf = ""
	# 	dateBuf = ""
	# 	_, dayModeBuf, runtimeBuf, dateBuf, indexBuf = parse_ganzhi_input(unifiedData(inputMsg))
# 干支列表
	elif inputMsg.startswith("干支") or normalize_time_command(inputMsg)["matched"]:

		Zhi = "子丑寅卯辰巳午未申酉戌亥"
		dateMode = ""
		runTimeBuf = ""
		indexBuf = ""
		dateBuf = ""

		info = normalize_time_command(inputMsg)

		if info["matched"]:
			normalizedMsg = info["normalized"]
		else:
			normalizedMsg = unifiedData(inputMsg)

		_, dayModeBuf, runtimeBuf, dateBuf, indexBuf = parse_ganzhi_input(normalizedMsg)


		ganZi_flexMsgJson_dict = ganZiList_fun(
			currentTime=dateBuf,
			dayMode=dayModeBuf,
			index=indexBuf,
			runtime=int(runtimeBuf)
		)

		# ⭐ v3 的 Flex Message 回覆方式
		# logBK_logDataFun( userID = linebotId  , userName = linebotUserName , logTime = "", inputData = inputMsg )
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

		# # 建立兩個執行緒
		# t1 = threading.Thread( target=delayed_upLog )
		# # 啟動執行緒
		# t1.start()

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

	# 	print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", flush=True)

	# 	# # 背景清理超過15天的圖片
	# 	# t = threading.Thread(target=delayed_cleanup, args=(15,))
	# 	# t.start()
	# 	# return





	# # Notion 處理
	# elif inputMsg.startswith("n+")  or inputMsg.startswith("☕"):
	# 	if userData [ "notionToken_pageId" ] == True:
	# 		inputMsg = inputMsg.replace("☕ Uploading..." , "")

	# 		# s = re.sub(r'[\r\n]+', STRONG_TOKEN, s)

	# 		inputMsg = re.sub(r'[\r\n]+', '', inputMsg , count=1 )

	# 		print( "N command:" , inputMsg )
	# 		notion_url = sixYaoMain(inputMsg, userSetting=userData)
	# 		returnMsg = notion_url

	# 	else:
	# 		returnMsg = "\udbc0\udc2e Notion not Ready..."


	# 	# ⭐ v3 文字訊息回覆
	# 	# logBK_logDataFun( userID = linebotId  , userName = linebotUserName , logTime = "", inputData = inputMsg )
	# 	line_bot_api.reply_message(
	# 		ReplyMessageRequest(
	# 			reply_token=event.reply_token,
	# 			messages=[TextMessage(text = returnMsg)]
	# 		)
	# 	)









	# # 文字版UI 處理
	# elif inputMsg.startswith("t+"):
	# 	text_UI = sixYaoMain( inputMsg , userSetting=userData)
	# 	# logBK_logDataFun( userID = linebotId  , userName = linebotUserName , logTime = "", inputData = inputMsg )
	# 	# ⭐ v3 文字訊息回覆
	# 	line_bot_api.reply_message(
	# 		ReplyMessageRequest(
	# 			reply_token=event.reply_token,
	# 			messages=[TextMessage(text= text_UI)]
	# 		)
	# 	)








	# 修改Title
	elif inputMsg[0] in [ ">" , ":" , "@",  "：" , "！" , "!", "/","*" ]:
		if inputMsg.startswith((">>" , "::" , "@@", "：：" , "！！" , "!!", "//","**"  )):
			changeNote = inputMsg[2:]
		else:
			changeNote = inputMsg[1:]
		changeNote = changeNote.replace(' ', '')
		# changeNote = changeNote.replace('\n', '^')
		# print( "@@@@@@@ change note === " , changeNote )
		uiCommand = get_json_item_data(user_id, "temp")
		# print( ">>>>> ", uiCommand )
		if uiCommand:
			if uiCommand[0] == "+":
				uiCommand = uiCommand[1:]
			newCommand = uiCommand.replace("Untitled", changeNote)
			print( "NEW COMMAND: " , newCommand )
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

		elif inputMsg in ["restart", "re"]:
			# ⭐ v3 文字訊息回覆
			line_bot_api.reply_message(
				ReplyMessageRequest(
					reply_token=event.reply_token,
					messages=[TextMessage(text= "🔄 正在重啟 Bot..." )]
				)
			)

			os.execv(sys.executable, ['python'] + sys.argv)







	





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















	elif ("//" not in inputMsg) and ("$" not in inputMsg) and ("X" not in inputMsg) and ("0" not in inputMsg) and ("占" in inputMsg ) :

		gridFlexDict = getDrawRiceGua(inputMsg)

		# ⭐ v3 的 Flex Message
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[
					FlexMessage(
						alt_text='< 亂數取卦 >',
						contents=FlexContainer.from_dict(gridFlexDict)
					)
				]
			)
		)











	# 卦象UI
	# elif "//" in unifiedData(inputMsg):
	else:
		rtn_buf = sixYaoMain( inputMsg, userData )

		if "錯誤" not in rtn_buf:
			print("UI mode")
			ui_cmd_dict = rtn_buf
			# print(ui_cmd_dict)
			# if "Untitled" in inputMsg:
			dictTxt = json.dumps(ui_cmd_dict, ensure_ascii=False, default=str) ## 變成人可以讀的中文
			# dictTxt = json.dumps( ui_cmd_dict , default=str)
			matchList = re.findall(r'&(.*?)&', dictTxt)

			if matchList:
				print( matchList[0] )
				## 命令中如果沒內容(Untitled)，才存進json
				if "Untitled" in matchList[0]: 
					save_json_data(user_id, "temp", matchList[0] ) 
					# +2025/11/10/21/55//1X$111//新主題  前面的+去掉才會進入UI模式，否則起卦模式到下面的flex格式是不行的

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
			# 建立執行緒
			t2 = threading.Thread( target=delayed_upJson )
			# 啟動執行緒
			t2.start()

			return

		else:
			# returnMsg = f"❌ 未知指令: {inputMsg}"
			returnMsg = rtn_buf

			# ⭐ v3 文字訊息回覆
			line_bot_api.reply_message(
				ReplyMessageRequest(
					reply_token=event.reply_token,
					messages=[TextMessage(text= returnMsg )]
				)
			)



	# else:
	# 	returnMsg = f"未知指令: {inputMsg}"

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

	elif ui_command[-2:] == "//": 

		# ⭐ v3 的文字訊息回覆
		line_bot_api.reply_message(
			ReplyMessageRequest(
				reply_token=event.reply_token,
				messages=[TextMessage(text= ui_command )]
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


# def handle_postback(event):
# 	try:  # ⭐ 加上這行
# 		print(f"📥 Postback: {event.postback.data}")  # ⭐ 加上這行，方便 debug
		
# 		# 你原本的邏輯保持不變
# 		data = event.postback.data
# 		# ... 你的處理邏輯 ...
# 		line_bot_api.reply_message(
# 			event.reply_token,
# 			TextMessage(text="...")
# 		)
		
# 	except Exception as e:  # ⭐ 加上這段
# 		print(f"❌ Postback 錯誤: {e}")  # ⭐ 錯誤會被印出來




# ⭐ v3 的 Postback 處理
@handler.add(PostbackEvent)
def handle_postback(event):

	try:  # ⭐ 加上這行
		postDataMsg = event.postback.data
		print(f"📥 Postback: { postDataMsg }")  # ⭐ 加上這行，方便 debug
		user_id = event.source.user_id

		data = postDataMsg.replace('\u200b', '')

		userData = get_user_json_data(user_id)
		print("@@@ userData:", userData)



		# time.sleep(2)
		# richmenu 切換
		if data.startswith("change-to-"):
			return
		elif data == "pass":
			return

		# 小六壬 處理
		elif data.startswith("s+"):

			data = data[2:]

			itemBuf = data.split(" // ")

			inList = []
			if len( itemBuf ) == 2:
				inList = [int(x) for x in itemBuf[0].split(",")]
				note = itemBuf[1]
				print ( inList , note )
				# inList = threeNum	
			else:
				note = data
				inList = [ 0,0,0 ]

			sixZn_UI = sSixZnUi( inList , title = note )
			## 過濾使用者
			# my_id = "U21eaaf32db85b983a842d9a9da81d8f1"
			# if user_id == my_id:

			# ⭐ v3 的 Flex Message
			line_bot_api.reply_message(
				ReplyMessageRequest(
					reply_token=event.reply_token,
					messages=[
						FlexMessage(
							alt_text='< 小六壬UI >',
							contents=FlexContainer.from_dict( sixZn_UI )
						)
					]
				)
			)

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

		# 文字版UI 處理
		elif data == "sendMe":
			
			pushMsg(  userData['linebotUserName'] + " push...", user_id = None )






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

			# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", flush=True)

			# # 背景清理
			# t = threading.Thread(target=delayed_cleanup, args=(15,))
			# t.start()

		else:
			# ⭐ v3 fallback 回覆
			line_bot_api.reply_message(
				ReplyMessageRequest(
					reply_token=event.reply_token,
					messages=[TextMessage(text="未知指令格式")]
				)
			)
	except Exception as e:  # ⭐ 加上這段
		print(f"❌ Postback 錯誤: {e}")  # ⭐ 錯誤會被印出來




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