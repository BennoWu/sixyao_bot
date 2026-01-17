import os
import json
from dotenv import load_dotenv
load_dotenv()  # 載入 .env 檔案





## 讀取JSON中的資料，輸入 id , item可以取得數值
def getItemData ( linebotId , itemName ):
	if os.path.isfile("__sixYoSet__.json") == True: ## 如果檔案存在

		with open('__sixYoSet__.json') as f:
			dataDict = json.load(f)

		if linebotId in dataDict.keys(): ## 如果已經有這個id
			return  dataDict[ linebotId ][itemName]



## 給值，id , item , data
# def setItemData ( linebotId , itemName , inData ):
# 	if os.path.isfile("__sixYoSet__.json") == True: ## 如果檔案存在

# 		with open('__sixYoSet__.json') as f:
# 			dataDict = json.load(f)

# 		if linebotId in dataDict.keys(): ## 如果已經有這個id
# 			# return  dataDict[ linebotId ][itemName]
# 			dataDict[ linebotId ][itemName] = inData

# 		with open('__sixYoSet__.json','w') as f:
# 			json.dump(dataDict, f, indent = 4)



def setItemData(linebotId, itemName, inData):
	json_file = "__sixYoSet__.json"
	
	# 如果檔案存在就讀取，否則新建空字典
	if os.path.isfile(json_file):
		with open(json_file, 'r', encoding="utf-8") as f:
			dataDict = json.load(f)
	else:
		dataDict = {}

	# 更新資料
	if linebotId not in dataDict:
		dataDict[linebotId] = {}
	dataDict[linebotId][itemName] = inData

	# 存回 JSON，中文直接顯示
	with open(json_file, 'w', encoding="utf-8") as f:
		json.dump(dataDict, f, indent=4, ensure_ascii=False)


# line id	
# user name	
# user image	
# login time	
# signup time	
# command	
# runtime	
# ui style	
# sub data mode	
# utc	

# notion auth token	
# notion page id

# switch	
# temp

def addToJson ( linebotId = None  ,
				UserName = None ,
				signUpTime = None  ,
				logInTime = None ,
				command = None ,
				runtime = None ,
				userImage = None  ,
				uiStyle = None,
				fontStyle = None,
				tipsMode = None,
				subDataMode = None,
				utc = None,

				notionToken_pageId	= None,

				switch = None ,
				temp = None 
				):

	dataDict = {}

	# 🔥 修改：如果 JSON 檔案不存在，先執行 googleToJson() 建立檔案
	if os.path.isfile("__sixYoSet__.json") == False:
		print("⚠️ JSON 檔案不存在，正在從 Google Sheet 同步資料...")
		try:
			result = googleToJson()
			print(result)
		except Exception as e:
			print(f"⚠️ 從 Google Sheet 同步失敗: {e}")
			print("將建立新的空白 JSON 檔案")

	# 現在檔案應該存在了（無論是從 Google 同步或準備新建）
	if os.path.isfile("__sixYoSet__.json") == True:
		with open('__sixYoSet__.json', 'r', encoding="utf-8") as f:
			dataDict = json.load(f)
			
		if linebotId in dataDict.keys():  # 如果已經有這個 id
			print( "GET google user ID")
			# 更新現有用戶資料
			if UserName != None:
				dataDict[linebotId]["userName"] = UserName
			if userImage != None:
				dataDict[linebotId]["userImage"] = userImage
			if logInTime != None:
				dataDict[linebotId]["logInTime"] = logInTime
			if signUpTime != None:
				dataDict[linebotId]["signUpTime"] = signUpTime
			if (command != None): 
				dataDict[linebotId]["command"] = command
			if runtime != None:
				dataDict[linebotId]["runtime"] = runtime
			if uiStyle != None:
				dataDict[linebotId]["uiStyle"] = uiStyle
			if fontStyle != None:
				dataDict[linebotId]["fontStyle"] = fontStyle
			if tipsMode != None:
				dataDict[linebotId]["tipsMode"] = tipsMode
			if subDataMode != None:
				dataDict[linebotId]["subDataMode"] = subDataMode
			if utc != None:
				dataDict[linebotId]["utc"] = utc

			# if notionToken_pageId != None:
			# 	dataDict[linebotId]["notionToken_pageId"] = notionToken_pageId
			# if notionToken_pageId == "off":
			# 	dataDict[linebotId]["notionToken_pageId"] = None

			if notionToken_pageId != None:
				# 將 "TRUE"/"FALSE" 字串轉成 python Boolean
				if isinstance(notionToken_pageId, str):
					if notionToken_pageId.upper() == "TRUE":
						dataDict[linebotId]["notionToken_pageId"] = True
					elif notionToken_pageId.upper() == "FALSE":
						dataDict[linebotId]["notionToken_pageId"] = False
					else:
						dataDict[linebotId]["notionToken_pageId"] = notionToken_pageId
				else:
					dataDict[linebotId]["notionToken_pageId"] = notionToken_pageId

			# 特別處理 off
			if notionToken_pageId == "off":
				dataDict[linebotId]["notionToken_pageId"] = None





			if switch != None:
				dataDict[linebotId]["switch"] = switch
			if temp != None:
				dataDict[linebotId]["temp"] = temp

		else:  # 如果沒有表示第一次登入，建立新的
			dataDict[linebotId] = {}
			dataDict[linebotId]["userName"] = UserName
			dataDict[linebotId]["userImage"] = userImage
			dataDict[linebotId]["logInTime"] = logInTime
			dataDict[linebotId]["signUpTime"] = logInTime
			dataDict[linebotId]["command"] = command
			dataDict[linebotId]["runtime"] = runtime
			dataDict[linebotId]["uiStyle"] = uiStyle
			dataDict[linebotId]["fontStyle"] = fontStyle			
			dataDict[linebotId]["tipsMode"] = tipsMode
			dataDict[linebotId]["subDataMode"] = subDataMode
			dataDict[linebotId]["utc"] = utc		
			dataDict[linebotId]["notionToken_pageId"] = notionToken_pageId	
			dataDict[linebotId]["switch"] = switch
			dataDict[linebotId]["temp"] = temp

	else:  # 如果連檔案都不存在（googleToJson 也失敗了），建立新的
		dataDict[linebotId] = {}
		dataDict[linebotId]["userName"] = UserName
		dataDict[linebotId]["userImage"] = userImage
		dataDict[linebotId]["logInTime"] = logInTime
		dataDict[linebotId]["signUpTime"] = logInTime
		dataDict[linebotId]["command"] = command
		dataDict[linebotId]["runtime"] = runtime
		dataDict[linebotId]["uiStyle"] = uiStyle
		dataDict[linebotId]["fontStyle"] = fontStyle
		dataDict[linebotId]["tipsMode"] = tipsMode		
		dataDict[linebotId]["subDataMode"] = subDataMode
		dataDict[linebotId]["utc"] = utc		
		dataDict[linebotId]["notionToken_pageId"] = notionToken_pageId		
		dataDict[linebotId]["switch"] = switch
		dataDict[linebotId]["temp"] = temp

	# 存回 JSON，中文直接顯示
	with open('__sixYoSet__.json', 'w', encoding="utf-8") as f:
		json.dump(dataDict, f, indent=4, ensure_ascii=False)
# line id	
# user name	
# user image	
# login time	
# signup time	
# command	
# runtime	
# ui style	
# sub data mode	
# utc	

# notion auth token	
# notion page id

# switch	
# temp



def loadAllJson(jsonFile="__sixYoSet__.json"):
	values_all = []
	if os.path.isfile(jsonFile):
		with open(jsonFile, 'r', encoding="utf-8") as f:
			dataDict = json.load(f)

		for eachUser in dataDict:
			values = [eachUser]
			for eachValue in dataDict[eachUser]:
				# 🔥 修改這裡:如果是 None 就改成空字串
				value = dataDict[eachUser][eachValue]
				values.append('' if value is None else value)
			values_all.append(values)
	return values_all


def loadAllJson(jsonFile="__sixYoSet__.json"):
	"""
	讀取 JSON 並按照固定順序輸出，確保和 Google Sheet 欄位順序一致
	Google Sheet 欄位順序：
	line id | user name | user image | login time | sign up time | command | 
	runtime | ui style | font style | tips mode | sub data mode | utc | 
	notion token/page id | switch | temp
	"""
	values_all = []
	
	if not os.path.isfile(jsonFile):
		return values_all
	
	with open(jsonFile, 'r', encoding="utf-8") as f:
		dataDict = json.load(f)
	
	# 🔥 定義欄位順序（必須和 Google Sheet 的欄位順序完全一致）
	field_order = [
		"userName",
		"userImage",
		"logInTime",
		"signUpTime",
		"command",
		"runtime",
		"uiStyle",
		"fontStyle",
		"tipsMode",
		"subDataMode",
		"utc",
		"notionToken_pageId",
		"switch",
		"temp"
	]
	
	for eachUser in dataDict:
		# 第一個是 user ID
		values = [eachUser]
		
		# 按照固定順序取值
		for field in field_order:
			value = dataDict[eachUser].get(field)
			# 🔥 None 轉成空字串
			if value is None:
				values.append("")
			else:
				values.append(value)
		
		values_all.append(values)
	
	return values_all


# ============================================
# 配套的 jsonToGoogle 函數
# ============================================

def jsonToGoogle():
	import os
	import pygsheets
	
	# ---- 載入 Google 金鑰 ----
	credentials_json = os.environ.get('GOOGLE_CREDENTIALS')
	if credentials_json:
		gc = pygsheets.authorize(service_account_env_var='GOOGLE_CREDENTIALS')
	else:
		gc = pygsheets.authorize(service_file='googleSheetKey/sixyao-data-8f0c712298cd.json')
	
	globalSheet = gc.open_by_url(
		'https://docs.google.com/spreadsheets/d/1Zlj55gQ5N75lWJYAyZ5Es6WTM_LS6SeFumZWlpLo6-0/edit?usp=sharing'
	)
	
	sheetName = "userID_list"
	wks = globalSheet.worksheet_by_title(sheetName)
	print(">> A")
	print(wks)
	
	all_values = wks.get_all_values()
	
	if len(all_values) == 0:
		print("工作表完全是空的")
		return "Error: 工作表沒有任何資料"
	
	headers = all_values[0]
	print(">> 標題列:", headers)
	
	allDataList = wks.get_all_records() if len(all_values) > 1 else []
	print(">> B")
	print(allDataList)
	
	totalNum = len(allDataList)
	print(">> 現有資料筆數:", totalNum)
	
	valuesList = loadAllJson()  # 取得 JSON 資料（已經處理好順序和 None）
	updateNum = 0
	newNum = 0
	
	# ---- 🔥 保持正確的資料類型，並處理可能被誤認為公式的字串 ----
	def clean_and_fix_row(values, expected_fields=15):
		new_values = []
		for v in values:
			# None 或空字串保持空字串
			if v is None or v == "":
				new_values.append("")
			# 數字保持數字類型
			elif isinstance(v, (int, float)):
				new_values.append(v)
			# 字串：檢查是否可能被誤認為公式
			else:
				v_str = str(v)
				# 🔥 如果以 +, -, =, @ 開頭，加上單引號前綴防止被當成公式
				if v_str and v_str[0] in ['+', '-', '=', '@']:
					new_values.append("'" + v_str)
				else:
					new_values.append(v_str)
		
		# 只補齊到指定欄位數（用空字串）
		if len(new_values) < expected_fields:
			new_values += [""] * (expected_fields - len(new_values))
		elif len(new_values) > expected_fields:
			new_values = new_values[:expected_fields]
		
		return new_values
	
	for values in valuesList:
		eachId = values[0]
		print(">", eachId)
		
		# 清理、保持數字類型，防止公式注入，處理 15 欄
		values = clean_and_fix_row(values, expected_fields=15)
		print(">> 寫入資料:", values)
		
		sheetNum = None
		newItem = True
		
		# 判斷是否已存在
		for index, item in enumerate(allDataList):
			if item['line id'] == eachId:
				sheetNum = index
				newItem = False
				break
		
		if not newItem:
			# 更新現有資料
			row_number = sheetNum + 2
			print(eachId, " - UPDATE at row", row_number)
			wks.update_values('A' + str(row_number), [values])
			updateNum += 1
		else:
			# 新增資料到最後一行
			new_row_number = totalNum + 2
			print(eachId, " - NEW at row", new_row_number)
			wks.update_values('A' + str(new_row_number), [values])
			totalNum += 1
			newNum += 1
	
	return ("🆗 Json data to GoogleSheet\nUpdate: %d New: %d" % (updateNum, newNum))




## 把google sheet資料備回json
def googleToJson():
	import os
	import pygsheets
	
	# 從環境變數讀取金鑰
	credentials_json = os.environ.get('GOOGLE_CREDENTIALS')
	
	# 金鑰位置
	if credentials_json:
		gc = pygsheets.authorize(service_account_env_var='GOOGLE_CREDENTIALS')
	else:
		gc = pygsheets.authorize(service_file='googleSheetKey/sixyao-data-8f0c712298cd.json')
	
	# 開啟sheet檔案
	globalSheet = gc.open_by_url(
		'https://docs.google.com/spreadsheets/d/1Zlj55gQ5N75lWJYAyZ5Es6WTM_LS6SeFumZWlpLo6-0/edit?usp=sharing'
	)
	
	dataDict = {}
	sheetName = "userID_list"
	wks = globalSheet.worksheet_by_title(sheetName)
	allDataList = wks.get_all_records()  # 取得所有資料，字典檔
	totalNum = len(allDataList)  # 現有總共的項目數量
	print(allDataList)
	
	# 🔥 清理資料的函數：處理空字串、公式前綴、布林值等
	def clean_value(value):
		"""
		清理從 Google Sheets 讀取的值
		- 空字串 → None
		- 去除公式前綴（單引號開頭）
		- 保持數字類型
		- 🔥 將 "TRUE"/"FALSE" 轉換為布林值
		"""
		# 空字串轉 None
		if value == "" or value is None:
			return None
		
		# 🔥 新增：處理布林值字串
		if isinstance(value, str):
			if value.upper() == "TRUE":
				return True
			elif value.upper() == "FALSE":
				return False
			# 如果以單引號開頭（我們加的公式保護），去除單引號
			elif value.startswith("'"):
				return value[1:]
		
		# 其他保持原樣
		return value
	
	for eachData in allDataList:
		linebotId = eachData['line id']
		dataDict[linebotId] = {}
		
		# 🔥 使用 clean_value 處理每個欄位
		dataDict[linebotId]["userName"] = clean_value(eachData['user name'])
		dataDict[linebotId]["userImage"] = clean_value(eachData['user image'])
		dataDict[linebotId]["logInTime"] = clean_value(eachData['login time'])
		dataDict[linebotId]["signUpTime"] = clean_value(eachData['sign up time'])
		dataDict[linebotId]["command"] = clean_value(eachData['command'])
		dataDict[linebotId]["runtime"] = clean_value(eachData['runtime'])
		dataDict[linebotId]["uiStyle"] = clean_value(eachData['ui style'])
		dataDict[linebotId]["fontStyle"] = clean_value(eachData['font style'])
		dataDict[linebotId]["tipsMode"] = clean_value(eachData['tips mode'])
		dataDict[linebotId]["subDataMode"] = clean_value(eachData['sub data mode'])
		dataDict[linebotId]["utc"] = clean_value(eachData['utc'])
		dataDict[linebotId]["notionToken_pageId"] = clean_value(eachData['notion token/page id'])
		dataDict[linebotId]["switch"] = clean_value(eachData['switch'])
		dataDict[linebotId]["temp"] = clean_value(eachData['temp'])
	
	# 存回 JSON
	with open('__sixYoSet__.json', 'w', encoding='utf-8') as f:
		json.dump(dataDict, f, indent=4, ensure_ascii=False)
	
	return ("🆗 Google Sheet data to Json\nTotal:%d" % len(allDataList))
# def googleToJson():
# 	import os
# 	import pygsheets
	
# 	# 從環境變數讀取金鑰
# 	credentials_json = os.environ.get('GOOGLE_CREDENTIALS')
	
# 	# 金鑰位置
# 	if credentials_json:
# 		gc = pygsheets.authorize(service_account_env_var='GOOGLE_CREDENTIALS')
# 	else:
# 		gc = pygsheets.authorize(service_file='googleSheetKey/sixyao-data-8f0c712298cd.json')
	
# 	# 開啟sheet檔案
# 	globalSheet = gc.open_by_url(
# 		'https://docs.google.com/spreadsheets/d/1Zlj55gQ5N75lWJYAyZ5Es6WTM_LS6SeFumZWlpLo6-0/edit?usp=sharing'
# 	)
	
# 	dataDict = {}
# 	sheetName = "userID_list"
# 	wks = globalSheet.worksheet_by_title(sheetName)
# 	allDataList = wks.get_all_records()  # 取得所有資料，字典檔
# 	totalNum = len(allDataList)  # 現有總共的項目數量
# 	print(allDataList)
	
# 	# 🔥 清理資料的函數：處理空字串、公式前綴等
# 	def clean_value(value):
# 		"""
# 		清理從 Google Sheets 讀取的值
# 		- 空字串 → None
# 		- 去除公式前綴（單引號開頭）
# 		- 保持數字類型
# 		"""
# 		# 空字串轉 None
# 		if value == "" or value is None:
# 			return None
		
# 		# 如果是字串且以單引號開頭（我們加的公式保護），去除單引號
# 		if isinstance(value, str) and value.startswith("'"):
# 			return value[1:]  # 去掉第一個字元（單引號）
		
# 		# 其他保持原樣
# 		return value
	
# 	for eachData in allDataList:
# 		linebotId = eachData['line id']
# 		dataDict[linebotId] = {}
		
# 		# 🔥 使用 clean_value 處理每個欄位
# 		dataDict[linebotId]["userName"] = clean_value(eachData['user name'])
# 		dataDict[linebotId]["userImage"] = clean_value(eachData['user image'])
# 		dataDict[linebotId]["logInTime"] = clean_value(eachData['login time'])
# 		dataDict[linebotId]["signUpTime"] = clean_value(eachData['sign up time'])
# 		dataDict[linebotId]["command"] = clean_value(eachData['command'])
# 		dataDict[linebotId]["runtime"] = clean_value(eachData['runtime'])
# 		dataDict[linebotId]["uiStyle"] = clean_value(eachData['ui style'])
# 		dataDict[linebotId]["fontStyle"] = clean_value(eachData['font style'])
# 		dataDict[linebotId]["tipsMode"] = clean_value(eachData['tips mode'])
# 		dataDict[linebotId]["subDataMode"] = clean_value(eachData['sub data mode'])
# 		dataDict[linebotId]["utc"] = clean_value(eachData['utc'])
# 		dataDict[linebotId]["notionToken_pageId"] = clean_value(eachData['notion token/page id'])
# 		dataDict[linebotId]["switch"] = clean_value(eachData['switch'])
# 		dataDict[linebotId]["temp"] = clean_value(eachData['temp'])  # 🔥 改成從 Google Sheet 讀取
	
# 	# 存回 JSON
# 	with open('__sixYoSet__.json', 'w', encoding='utf-8') as f:
# 		json.dump(dataDict, f, indent=4, ensure_ascii=False)
	
# 	return ("🆗 Google Sheet data to Json\nTotal:%d" % len(allDataList))









# line id	
# user name	
# user image	
# login time	
# signup time	
# command	
# runtime	
# ui style	
# sub data mode	
# utc	

# notion auth token	
# notion page id

# switch	
# temp





## 上傳log至google sheet

def logToGoogle(  userId = "BB123", userName = "Benno", time = "2025/6/15/3/20" , userInput = "run12345" ):


	import os
	import pygsheets

	# # 從環境變數讀取金鑰
	credentials_json = os.environ.get('GOOGLE_CREDENTIALS')

	# # # 金鑰位置
	if credentials_json:
		# pygsheets 直接從環境變數讀取
		gc = pygsheets.authorize(service_account_env_var='GOOGLE_CREDENTIALS')
	else:
		# 本地開發用檔案
		gc = pygsheets.authorize(service_file='googleSheetKey/sixyao-data-8f0c712298cd.json')

	globalSheet = gc.open_by_url(
		'https://docs.google.com/spreadsheets/d/1Zlj55gQ5N75lWJYAyZ5Es6WTM_LS6SeFumZWlpLo6-0/edit?usp=sharing'
	)








	# import pygsheets
	# # 金鑰位置
	# gc = pygsheets.authorize( service_file='googleSheetKey/sixyao-data-8f0c712298cd.json')
	# # e mail id : sixyao-id@sixyao-data.iam.gserviceaccount.com

	# # 開啟sheet檔案
	# globalSheet = gc.open_by_url(
	# 'https://docs.google.com/spreadsheets/d/1Zlj55gQ5N75lWJYAyZ5Es6WTM_LS6SeFumZWlpLo6-0/edit?usp=sharing' ## 六爻 sheet
	# )
	
	sheetName = "log"
	wks = globalSheet.worksheet_by_title(sheetName)
	allDataList = wks.get_all_records() # 取得所有資料，字典檔
	totalNum = totalNumber = len( allDataList ) # 現有總共的項目數量
	
	wks.update_values('A'+str( totalNum + 2 ), [ [ userId , userName , time , userInput] ]) # 橫的










def get_user_json_data( user_id , json_path= '__sixYoSet__.json' ):
	"""
	從 JSON 取出指定使用者的資料，並組成指定格式字典。
	"""
	with open(json_path, encoding="utf-8") as f:
		data = json.load(f)

	user = data.get(user_id)
	if not user:
		return None  # 找不到使用者就直接返回 None

	userData = {
		"linebotId"         : user_id,
		"linebotUserName"   : user.get("userName"),
		"utc"               : user.get("utc"),
		"tipsMode"          : user.get("tipsMode"),
		"notionToken_pageId": user.get("notionToken_pageId"),
	}

	return userData




def get_user_info(user_id, json_path='__sixYoSet__.json'):
	with open(json_path, encoding="utf-8") as f:
		data = json.load(f)

	user = data.get(user_id)
	if not user:
		return f"⚠️ 找不到 ID：{user_id}"

	text = f"""使用者資料
ID：{user_id}
====================
""" + "\n".join([f"{k}：{v}" for k, v in user.items()])

	return text





def get_all_user_flex( json_path='__sixYoSet__.json' ):
	"""
	讀取 JSON 裡所有帳號資料，回傳 Flex Message dict
	- 每個帳號增加 runtime
	- bubble size=deca
	- Total 上方增加 separator
	"""
	with open(json_path, encoding="utf-8") as f:
		data = json.load(f)

	contents = []

	for user_id, user in data.items():
		user_box = {
			"type": "box",
			"layout": "vertical",
			"spacing": "sm",
			"margin": "md",
			"contents": [
				{"type": "text", "text": f"{user.get('userName', '')}", "weight": "bold", "size": "md"},
				{"type": "text", "text": f"utc: {user.get('utc')}", "size": "sm"},
				{"type": "text", "text": f"tipsMode: {user.get('tipsMode')}", "size": "sm"},
				{"type": "text", "text": f"notionToken_pageId: {user.get('notionToken_pageId')}", "size": "sm"},
				{"type": "text", "text": f"runtime: {user.get('runtime')}", "size": "sm"},
				{"type": "separator", "color": "#aaaaaa", "margin": "md"}
			]
		}
		contents.append(user_box)

	# Total 前面加一條 separator
	contents.append({"type": "separator","color": "#aaaaaa", "margin": "xs"})

	# 總數
	total_box = {
		"type": "text",
		"text": f"Total {len(data)} Item",
		"weight": "bold",
		"margin": "md",
		"align": "start",
		"size": "sm"
	}
	contents.append(total_box)

	flex_message = {
		"type": "bubble",
		"size": "deca",
		"body": {
			"type": "box",
			"layout": "vertical",
			"contents": contents
		}
	}

	return flex_message


# 使用範例
# flex_msg = get_all_user_flex()
# line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text="User List", contents=flex_msg))



def get_json_item_data(user_id, item, json_path='__sixYoSet__.json'):
	"""
	從 JSON 檔案中取得指定 user_id 的 item 值

	Args:
		user_id (str): 使用者 ID
		item (str): 欲取得的欄位名稱
		json_path (str, optional): JSON 檔案路徑. Default '__sixYoSet__.json'

	Returns:
		取得的值，如果找不到檔案/使用者/欄位，回傳 None
	"""
	if not os.path.exists(json_path):
		return None

	try:
		with open(json_path, 'r', encoding='utf-8') as f:
			data = json.load(f)

		# 確保使用者存在
		user_data = data.get(user_id)
		if not user_data:
			return None

		# 回傳 item 值
		return user_data.get(item)

	except Exception as e:
		print(f"Error reading JSON: {e}")
		return None






def save_json_data(user_id, item, value, json_path='__sixYoSet__.json'):
	"""只修改既有 JSON 中的值，不新增任何使用者或欄位。"""

	# 檢查檔案是否存在
	if not os.path.exists(json_path):
		print(f"⚠️ 找不到檔案：{json_path}")
		return False

	# 嘗試載入 JSON
	try:
		with open(json_path, 'r', encoding='utf-8') as f:
			data = json.load(f)
	except Exception as e:
		print(f"⚠️ JSON 讀取失敗：{e}")
		return False

	# 檢查 user 是否存在
	if user_id not in data:
		print(f"⚠️ 找不到使用者 {user_id}，不進行修改。")
		return False

	# 檢查欄位是否存在
	if item not in data[user_id]:
		print(f"⚠️ 使用者 {user_id} 沒有項目 '{item}'，不進行修改。")
		return False

	# 修改值
	old_value = data[user_id][item]
	data[user_id][item] = value

	# 寫回 JSON 檔
	with open(json_path, 'w', encoding='utf-8') as f:
		json.dump(data, f, ensure_ascii=False, indent=4)

	print(f"✅ 已更新 {user_id} 的 '{item}'：{old_value} → {value}")
	# if value in [ "uiStyle","fontStyle","tipsMode","subDataMode","utc","notionToken_pageId" ]:
	# 	jsonToGoogle()
	return True




## 檢查環境變數有沒有設好
def checkEnv():
	credentials_json = os.environ.get('GOOGLE_CREDENTIALS')
	try:
		# 嘗試解析 JSON
		credentials_dict = json.loads(credentials_json)
		
		print("✅ JSON 格式正確!")
		print(f"✅ project_id: {credentials_dict.get('project_id')}")
		print(f"✅ client_email: {credentials_dict.get('client_email')}")
		print("✅ 所有必要欄位都在")
		
	except json.JSONDecodeError as e:
		print(f"❌ JSON 格式錯誤: {e}")
		print(f"❌ 錯誤位置: 第 {e.pos} 字元")
		if credentials_json:
			print(f"❌ 附近內容: {credentials_json[max(0, e.pos-30):e.pos+30]}")
	except Exception as e:
		print(f"❌ 其他錯誤: {e}")




if __name__ == '__main__':
	# print("測試 jsonToGoogle:")
	# print(jsonToGoogle())
	
	# print("\n測試 googleToJson:")
	# print(googleToJson())

	# save_json_data("U21eaaf32db85b983a842d9a9da81d8f1", "notionToken_pageId", None ) 
	# print(get_user_info("U21eaaf32db85b983a842d9a9da81d8f1"))
	aa = get_user_json_data("U21eaaf32db85b983a842d9a9da81d8f1")
	print(aa['linebotUserName'])
	# print("\n測試 logToGoogle:")
	# logToGoogle()
	# addToJson (  linebotId ="U21eaaf32db85b983a842d9a9da81d8f1"	,UserName = "Benno"	,logInTime ="2023-2-1 23:52",command =	"時盤-2023-02-01-21-51"	,runtime = 1	,signUpTime = "2023-2-1 11:18",  userImage ="https://profile.line-scdn.net/0m03d2961a72519e9ae023945979128659aaf19ece8932"	 ,uiStyle ="A"	,subDataMode ="Lite"	,switch = "ON")
	
	# addToJson (  linebotId ="ttttt"	,UserName = "aaaa"	,logInTime ="2023-2-1 23:52",command =	"cooomm"	,runtime = 1	,signUpTime = "2023-2-1 11:18",  userImage ="https://profile.line-scdn.net/0m03d2961a72519e9ae023945979128659aaf19ece8932"	 ,uiStyle ="A"	,subDataMode ="Lite"	,switch = "ON")

	# loadAllJson()
	# print(googleToJson())
	# print(jsonToGoogle())
	# logToGoogle()

	# setItemData ( "CCC" , "temp" , "inData" )


	# addToJson("BENNO","aaaaab","eeeecc",uiStyle = "C")
	# print( getItemData ( "BENNO","signUpTime"))
	# print( uiSetting( "U21eaaf32db85b983a842d9a9da81d8f1","set full a")  )
	# setItemData ( "BENNO" , "switch" , "WW" )

	# print( get_user_data( "U21eaaf32db85b983a842d9a9da81d8f1" ))
	# save_json_data("U21eaaf32db85b983a842d9a9da81d8f1", "runtime", 12)

	# flex_dict = get_all_user_flex()
	# print(json.dumps(flex_dict, ensure_ascii=False, indent=4))




# https://console.cloud.google.com/firestore/databases?project=sixyao-data


# 想要做什麼,舊招 (JSON 檔案),新招 (Firestore 雲端)
# 找到檔案,f = open('user.json'),ref = db.collection('users').document('ID')
# 把資料存進去,"json.dump(data, f)","ref.set(data, merge=True)"
# 把資料拿出來,data = json.load(f),data = ref.get().to_dict()

# 💡 為什麼要用 merge=True？ (這是送你的小密技)
# 原本 JSON 存檔就像是把整本書重印一遍；而 Firestore 的 merge=True 就像是用立可白改其中一個字。它不會動到你沒傳進去的欄位，這對保護用戶資料超級好用！

# https://console.cloud.google.com/firestore/databases/-default-/data/panel/master_check/test?project=sixyao-data

# https://console.cloud.google.com/welcome/new?project=sixyao-data&cloudshell=false

# 左側導覽選單 (三條線)

# Firestore → 進去看資料庫

# IAM 與管理 → 進去管權限、找服務帳戶、下金鑰




# #####################################################################
# #################  儲存
# #####################################################################

# from google.cloud import firestore

# # 初始化 (這行全專案只要跑一次)
# db = firestore.Client(project='sixyao-data')

# def save_to_cloud(collection_name, doc_id, data_dict):
#     """
#     collection_name: 抽屜分類 (例如 'users' 或 'config')
#     doc_id: 檔案名字 (例如 linebotId)
#     data_dict: 你的字典資料
#     """
#     doc_ref = db.collection(collection_name).document(doc_id)
    
#     # merge=True 的意思是：如果檔案已存在，只蓋掉有變動的部分，其他保留
#     doc_ref.set(data_dict, merge=True)
#     print(f"✅ 已存入雲端：{collection_name} -> {doc_id}")

# # --- 使用範例 ---
# my_data = {"userName": "六爻大師", "power": 99}
# save_to_cloud("users", "user_001", my_data)


# #####################################################################
# #################  讀取
# #####################################################################

# def load_from_cloud(collection_name, doc_id):
#     """
#     回傳一個字典檔，如果找不到就回傳空字典 {}
#     """
#     doc_ref = db.collection(collection_name).document(doc_id)
#     doc = doc_ref.get()

#     if doc.exists:
#         print(f"📖 讀取成功：{doc_id}")
#         return doc.to_dict()  # 這就是你要的字典檔
#     else:
#         print(f"⚠️ 雲端找不到檔案：{doc_id}")
#         return {}

# # --- 使用範例 ---
# user_info = load_from_cloud("users", "user_001")
# print(user_info.get("userName")) # 會印出：六爻大師