import json,os

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
				other = None,

				switch = None ,
				temp = None 
				):

	# userDict = {
	# 	linebotId : {
	# 		"userName" : UserName,
	# 		"logInTime" : logInTime,
	# 		"command" : command,
	# 		"signUpTime" : signUpTime,
	# 		"userImage" : userImage,
	# 		"uiStyle" : uiStyle,
	# 		"subDataMode" : subDataMode,
	# 		"runtime" : runtime,
	# 		"switch" : switch,
	# 	}
	# }
	dataDict = {}

	if os.path.isfile("__sixYoSet__.json") == True: ## 如果檔案存在

		# with open('__sixYoSet__.json') as f:
		# 	dataDict = json.load(f)
		with open('__sixYoSet__.json', 'r', encoding="utf-8") as f:
			dataDict = json.load(f)
			

		if linebotId in dataDict.keys(): ## 如果已經有這個id
			# dataDict[ linebotId ] = userDict[ linebotId ] ## 把已記錄的id中的資料更新
			# print(dataDict)

			# dataDict[ linebotId ] = {}
			if UserName != None:
				dataDict[ linebotId ]["userName"] = UserName
			if userImage != None:
				dataDict[ linebotId ] ["userImage"] = userImage
			if logInTime != None:
				dataDict[ linebotId ]["logInTime"] = logInTime
			if signUpTime != None:
				dataDict[ linebotId ] ["signUpTime"] = signUpTime
			if command != None:
				dataDict[ linebotId ] ["command"] = command
			if runtime != None:
				dataDict[ linebotId ] ["runtime"] = runtime
			if uiStyle != None:
				dataDict[ linebotId ] ["uiStyle"] = uiStyle

			if fontStyle != None:
				dataDict[ linebotId ] ["fontStyle"] = fontStyle

			if tipsMode != None:
				dataDict[ linebotId ] ["tipsMode"] = tipsMode


			if subDataMode != None:
				dataDict[ linebotId ] ["subDataMode"] = subDataMode
			if utc != None:
				dataDict[ linebotId ] ["utc"] = utc



			if notionToken_pageId != None:
				dataDict[ linebotId ] ["notionToken_pageId"] = notionToken_pageId

			if other != None:
				dataDict[ linebotId ] ["other"] = other


			if switch != None:
				dataDict[ linebotId ] ["switch"] = switch
			if temp != None:
				dataDict[ linebotId ] ["temp"] = temp

			# print(dataDict)

		# 如果沒有表示第一次登入，建立新的
		else:	
			dataDict[ linebotId ] = {}
			# dataDict[ "linebotId" ] = {}
			dataDict[ linebotId ]["userName"] = UserName
			dataDict[ linebotId ] ["userImage"] = userImage
			dataDict[ linebotId ] ["logInTime"] = logInTime
			dataDict[ linebotId ] ["signUpTime"] = logInTime
			dataDict[ linebotId ] ["command"] = command
			dataDict[ linebotId ] ["runtime"] = runtime
			dataDict[ linebotId ] ["uiStyle"] = uiStyle

			dataDict[ linebotId ] ["fontStyle"] = fontStyle			
			dataDict[ linebotId ] ["tipsMode"] = tipsMode

			dataDict[ linebotId ] ["subDataMode"] = subDataMode
			dataDict[ linebotId ] ["utc"] = utc		


			dataDict[ linebotId ] ["notionToken_pageId"] = notionToken_pageId	
			dataDict[ linebotId ] ["other"] = other	

			dataDict[ linebotId ] ["switch"] = switch
			dataDict[ linebotId ] ["temp"] = temp
			# print(dataDict)
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

	## 如果連檔案都不存在，建立新的
	else:
		dataDict[ linebotId ] = {}
		# dataDict[ "linebotId" ] = {}
		dataDict[ linebotId ]["userName"] = UserName
		dataDict[ linebotId ] ["userImage"] = userImage
		dataDict[ linebotId ]["logInTime"] = logInTime
		dataDict[ linebotId ] ["signUpTime"] = logInTime
		dataDict[ linebotId ] ["command"] = command
		dataDict[ linebotId ] ["runtime"] = runtime
		dataDict[ linebotId ] ["uiStyle"] = uiStyle

		dataDict[ linebotId ] ["fontStyle"] = fontStyle
		dataDict[ linebotId ] ["tipsMode"] = tipsMode		

		dataDict[ linebotId ] ["subDataMode"] = subDataMode
		dataDict[ linebotId ] ["utc"] = utc		


		dataDict[ linebotId ] ["notionToken_pageId"] = notionToken_pageId		
		dataDict[ linebotId ] ["other"] = other		

		dataDict[ linebotId ] ["switch"] = switch
		dataDict[ linebotId ] ["temp"] = temp

	# print(dataDict)
	# with open('__sixYoSet__.json','w') as f:
	# 	json.dump(dataDict, f, indent = 4)
	with open('__sixYoSet__.json', 'w', encoding="utf-8") as f:
		json.dump(dataDict, f, indent=4, ensure_ascii=False)


# ## 取得json所有檔案
# def loadAllJson( jsonFile = "__sixYoSet__.json" ):
# 	values_all = []
# 	if os.path.isfile(jsonFile) == True: ## 如果檔案存在

# 		with open(jsonFile) as f:
# 			dataDict = json.load(f)
# 		for eachUser in dataDict.keys():
# 			values =[]
# 			values.append( eachUser )
# 			for eachValue in dataDict[eachUser]:
# 				values.append( dataDict[eachUser][eachValue] )

# 			values_all.append( values )
# 	return values_all

def loadAllJson(jsonFile="__sixYoSet__.json"):
	values_all = []
	if os.path.isfile(jsonFile):
		# 用 UTF-8 讀取
		with open(jsonFile, 'r', encoding="utf-8") as f:
			dataDict = json.load(f)

		for eachUser in dataDict:
			values = [eachUser]
			for eachValue in dataDict[eachUser]:
				values.append(dataDict[eachUser][eachValue])
			values_all.append(values)
	return values_all


## 把json資料備回google sheet
# # https://www.youtube.com/watch?v=tPfllMdhCUE&list=PL072M7JLb0r4sanE111yySXvoO_fRv3x6&index=64
# def jsonToGoogle():
# 	import pygsheets
# 	# 金鑰位置
# 	gc = pygsheets.authorize( service_file='googleSheetKey/sixyao-data-8f0c712298cd.json')
# 	# e mail id : sixyao-id@sixyao-data.iam.gserviceaccount.com

# 	# 開啟sheet檔案
# 	globalSheet = gc.open_by_url(
# 	# 'https://docs.google.com/spreadsheets/d/1Mx2Xzv-WJnQuE0AyCo-DGHMVdmOrLAr7akrf8_rwwL4/'
# 	# 'https://docs.google.com/spreadsheets/d/1XlXKCz4GmhpoTvM8HnMLVIqpCK853FAVyS4tSPcE_kM/'
# 	'https://docs.google.com/spreadsheets/d/1Zlj55gQ5N75lWJYAyZ5Es6WTM_LS6SeFumZWlpLo6-0/edit?usp=sharing' ## 六爻 sheet
# 	)
# 	sheetName = "userID_list"
# 	wks = globalSheet.worksheet_by_title(sheetName)
# 	print(">> A")
# 	print(wks)
# 	allDataList = wks.get_all_records() # 取得所有資料，字典檔
# 	print(">> B")
# 	print(allDataList)

# 	totalNum = totalNumber = len( allDataList ) # 現有總共的項目數量
# 	print(">> A")
# 	print(totalNum)
# 	# print(allDataList[0].keys())
# 	# headers = wks.get_row(1)

# 	valuesList = loadAllJson() ## 取得的json資料，會以json的順序，所以GOOGLE表單和JSON的資料順序要一樣，兜上去才會對

# 	updateNum = 0
# 	newNum = 0
# 	for values in valuesList:
# 		eachId = values[0]
# 		print( ">",eachId )
# 		sheetNum = None
# 		newItem = True
# 		add = 0
# 		for item in allDataList:  # 跑一輪找出這個id的順序數字
# 			# print( ">>>",item ,"\n", item['User ID'])
# 			# print( item['User ID'],eachId )
# 			# print( item['User ID'] == eachId)

# 			if item['line id'] == eachId: ## 判斷這個名字在GOOGLE表單上是否已經存在
# 				sheetNum = add
# 				newItem = False
# 				break
# 				# print( "newItem:" , newItem )
# 				# print( "sheetNum" , sheetNum )
# 			add += 1
# 		# print( "user::",eachId ,  "    newItem:" , newItem  )

# 		if newItem != True:
# 			print( eachId , " - get OLD\n")
# 			wks.update_values('A'+str( sheetNum+2 ), [ values ]) # 橫的
# 		# 	# sheet_test01.update_values('B2', [['A', 'B', 'C', 'D']]) # 從B2開始向後填入'A', 'B', 'C', 'D'
# 			updateNum += 1


# 		else: ## 新的就加在最下面
# 			print( eachId , " - get NEW\n")
# 			wks.update_values('A'+str( totalNum+2 ), [ values ]) # 橫的
# 			newNum += 1

# 	return ( "Json data to GoogleSheet\nUpdate: %d New: %d"% ( updateNum,newNum ) )

def jsonToGoogle():





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


	# gc = pygsheets.authorize(service_file='googleSheetKey/sixyao-data-8f0c712298cd.json')
	# # e mail id : sixyao-id@sixyao-data.iam.gserviceaccount.com
	# # 開啟sheet檔案
	# globalSheet = gc.open_by_url(
	# 	'https://docs.google.com/spreadsheets/d/1Zlj55gQ5N75lWJYAyZ5Es6WTM_LS6SeFumZWlpLo6-0/edit?usp=sharing'  ## 六爻 sheet
	# )
	sheetName = "userID_list"
	wks = globalSheet.worksheet_by_title(sheetName)
	print(">> A")
	print(wks)
	
	# 修正：先取得所有值，包含標題
	all_values = wks.get_all_values()
	
	# 檢查是否有資料
	if len(all_values) == 0:
		print("工作表完全是空的")
		return "Error: 工作表沒有任何資料"
	
	# 取得標題列
	headers = all_values[0]
	print(">> 標題列:", headers)
	
	# 取得資料列（排除標題）
	if len(all_values) > 1:
		# 有資料行，使用 get_all_records
		allDataList = wks.get_all_records()
	else:
		# 只有標題，沒有資料
		allDataList = []
		print(">> 只有標題列，沒有資料")
	
	print(">> B")
	print(allDataList)
	
	totalNum = len(allDataList)  # 現有總共的項目數量（不含標題）
	print(">> 現有資料筆數:", totalNum)
	
	valuesList = loadAllJson()  ## 取得的json資料
	updateNum = 0
	newNum = 0
	
	for values in valuesList:
		eachId = values[0]
		print(">", eachId)
		sheetNum = None
		newItem = True
		
		# 跑一輪找出這個id的順序數字
		for index, item in enumerate(allDataList):
			if item['line id'] == eachId:  ## 判斷這個名字在GOOGLE表單上是否已經存在
				sheetNum = index  # 記錄在 allDataList 中的索引位置
				newItem = False
				break
		
		if not newItem:
			# 更新現有資料
			# sheetNum 是在 allDataList 中的索引（從 0 開始）
			# 實際在 sheet 中的行數是 sheetNum + 2（第1行是標題，所以+2）
			row_number = sheetNum + 2
			print(eachId, " - UPDATE at row", row_number)
			wks.update_values('A' + str(row_number), [values])
			updateNum += 1
		else:
			# 新增資料到最後一行
			# totalNum 是現有資料筆數，新資料應該放在 totalNum + 2 行
			# （第1行標題 + totalNum行資料 + 1）
			new_row_number = totalNum + 2
			print(eachId, " - NEW at row", new_row_number)
			wks.update_values('A' + str(new_row_number), [values])
			totalNum += 1  # 重要：增加總數，避免下一筆新資料覆蓋這筆
			newNum += 1
	
	return ("Json data to GoogleSheet\nUpdate: %d New: %d" % (updateNum, newNum))




# ## 把google sheet資料備回json
# def googleToJson():
# 	import pygsheets
# 	# 金鑰位置
# 	# gc = pygsheets.authorize( service_file='googleSheetKey/august-tesla-375921-2b2637e4e305.json')
# 	gc = pygsheets.authorize( service_file='googleSheetKey/sixyao-data-8f0c712298cd.json')
# 	# 開啟sheet檔案
# 	globalSheet = gc.open_by_url(
# 	# 'https://docs.google.com/spreadsheets/d/1Mx2Xzv-WJnQuE0AyCo-DGHMVdmOrLAr7akrf8_rwwL4/'
# 	# 'https://docs.google.com/spreadsheets/d/1XlXKCz4GmhpoTvM8HnMLVIqpCK853FAVyS4tSPcE_kM/'
# 	'https://docs.google.com/spreadsheets/d/1Zlj55gQ5N75lWJYAyZ5Es6WTM_LS6SeFumZWlpLo6-0/edit?usp=sharing' ## 六爻 sheet
# 	)
# 	dataDict = {}
# 	sheetName = "userID_list"
# 	wks = globalSheet.worksheet_by_title(sheetName)
# 	allDataList = wks.get_all_records() # 取得所有資料，字典檔

# 	totalNum = totalNumber = len( allDataList ) # 現有總共的項目數量
# 	print(allDataList)
# 	# valuesList = loadAllJson()
# 	for eachData in allDataList:
# 		linebotId = eachData['line id']
# 		dataDict[ linebotId ] = {}
# 		# dataDict[ "linebotId" ] = {}
# 		dataDict [ linebotId ] [ "userName" ]        = eachData['user name']
# 		dataDict [ linebotId ] [ "userImage" ]       = eachData['user image']
# 		dataDict [ linebotId ] [ "logInTime" ]       = eachData['login time']
# 		dataDict [ linebotId ] [ "signUpTime" ]      = eachData['sign up time']
# 		dataDict [ linebotId ] [ "command" ]         = eachData['command']
# 		dataDict [ linebotId ] [ "runtime" ]         = eachData['runtime']
# 		dataDict [ linebotId ] [ "uiStyle" ]         = eachData['ui style']
# 		dataDict [ linebotId ] [ "subDataMode"]      = eachData['sub data mode']
# 		dataDict [ linebotId ] [ "utc" ]             = eachData['utc']	

# 		dataDict [ linebotId ] [ "notionToken_pageId" ] = eachData['notion token/page id']	
# 		dataDict [ linebotId ] [ "other" ]    = eachData['other']


# 		dataDict [ linebotId ] [ "switch" ]          = eachData['switch']
# 		dataDict [ linebotId ] [ "temp" ]            = None	
		
# 	with open('__sixYoSet__.json','w') as f:
# 		json.dump(dataDict, f, indent = 4)
		
# 	return ("Google Sheet data to Json\nTotal:%d"% len(allDataList))


## 把google sheet資料備回json
def googleToJson():
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
	
	for eachData in allDataList:
		linebotId = eachData['line id']
		dataDict[linebotId] = {}
		dataDict[linebotId]["userName"] = eachData['user name']
		dataDict[linebotId]["userImage"] = eachData['user image']
		dataDict[linebotId]["logInTime"] = eachData['login time']
		dataDict[linebotId]["signUpTime"] = eachData['sign up time']
		dataDict[linebotId]["command"] = eachData['command']
		dataDict[linebotId]["runtime"] = eachData['runtime']
		dataDict[linebotId]["uiStyle"] = eachData['ui style']
		dataDict[linebotId]["fontStyle"] = eachData['font style']
		dataDict[linebotId]["tipsMode"] = eachData['tips mode']

		dataDict[linebotId]["subDataMode"] = eachData['sub data mode']
		dataDict[linebotId]["utc"] = eachData['utc']
		dataDict[linebotId]["notionToken_pageId"] = eachData['notion token/page id']
		dataDict[linebotId]["other"] = eachData['other']
		dataDict[linebotId]["switch"] = eachData['switch']
		dataDict[linebotId]["temp"] = None
	
	# 關鍵修正：加上 ensure_ascii=False 和 encoding='utf-8'
	with open('__sixYoSet__.json', 'w', encoding='utf-8') as f:
		json.dump(dataDict, f, indent=4, ensure_ascii=False)
	
	return ("Google Sheet data to Json\nTotal:%d" % len(allDataList))













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
				{"type": "separator", "margin": "md"}
			]
		}
		contents.append(user_box)

	# Total 前面加一條 separator
	contents.append({"type": "separator", "margin": "xs"})

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
	return True

# {
#   "type": "bubble",
#   "size": "kilo",
#   "body": {
#     "type": "box",
#     "layout": "vertical",
#     "contents": [
#       {
#         "type": "box",
#         "layout": "horizontal",
#         "contents": [
#           {
#             "type": "text",
#             "text": "六爻排盤:",
#             "weight": "bold",
#             "color": "#6A8B91",
#             "size": "lg"
#           },
#           {
#             "type": "text",
#             "text": "霜降→立冬",
#             "weight": "regular",
#             "color": "#666666",
#             "size": "lg",
#             "align": "end",
#             "action": {
#               "type": "message",
#               "label": "action",
#               "text": "干支/節氣/6/2025-10-25"
#             },
#             "gravity": "center"
#           }
#         ],
#         "margin": "none"
#       },
#       {
#         "type": "separator",
#         "margin": "none",
#         "color": "#cccccc"
#       },
#       {
#         "type": "box",
#         "layout": "horizontal",
#         "contents": [
#           {
#             "type": "text",
#             "text": "乙巳",
#             "weight": "bold",
#             "size": "xl",
#             "margin": "none",
#             "wrap": true,
#             "flex": 0,
#             "color": "#000001"
#           },
#           {
#             "type": "text",
#             "text": "|",
#             "size": "xl",
#             "margin": "none",
#             "color": "#cccccc",
#             "flex": 0,
#             "gravity": "top",
#             "offsetTop": "-2px"
#           },
#           {
#             "type": "text",
#             "text": "丙戌",
#             "weight": "bold",
#             "size": "xl",
#             "margin": "none",
#             "wrap": true,
#             "flex": 0,
#             "action": {
#               "type": "message",
#               "label": "action",
#               "text": "干支/月/6/2025-10-25"
#             },
#             "color": "#000002"
#           },
#           {
#             "type": "text",
#             "text": "|",
#             "size": "xl",
#             "margin": "none",
#             "color": "#cccccc",
#             "flex": 0,
#             "gravity": "top",
#             "offsetTop": "-2px"
#           },
#           {
#             "type": "text",
#             "text": "丁卯",
#             "weight": "bold",
#             "size": "xl",
#             "margin": "none",
#             "wrap": true,
#             "flex": 0,
#             "action": {
#               "type": "message",
#               "label": "action",
#               "text": "干支/日/6/2025-10-25"
#             },
#             "color": "#000002"
#           },
#           {
#             "type": "text",
#             "text": "|",
#             "size": "xl",
#             "margin": "none",
#             "color": "#cccccc",
#             "flex": 0,
#             "gravity": "top",
#             "offsetTop": "-2px"
#           },
#           {
#             "type": "text",
#             "text": "庚子",
#             "weight": "bold",
#             "size": "xl",
#             "margin": "none",
#             "wrap": true,
#             "flex": 0,
#             "action": {
#               "type": "message",
#               "label": "action",
#               "text": "干支/時/6/2025-10-25-0-24"
#             },
#             "color": "#000003"
#           }
#         ],
#         "spacing": "none",
#         "margin": "xs",
#         "cornerRadius": "7px",
#         "justifyContent": "space-between"
#       },
#       {
#         "type": "box",
#         "layout": "horizontal",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "國曆: 2025/10/25(六)",
#                 "size": "sm",
#                 "color": "#444443",
#                 "wrap": true,
#                 "weight": "regular",
#                 "margin": "none",
#                 "align": "start",
#                 "offsetTop": "2px"
#               },
#               {
#                 "type": "text",
#                 "text": "農曆: 九月初五",
#                 "size": "sm",
#                 "color": "#444443",
#                 "wrap": true,
#                 "weight": "regular",
#                 "margin": "none"
#               }
#             ],
#             "margin": "none",
#             "flex": 0,
#             "height": "40px"
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "|",
#                 "size": "xxl",
#                 "margin": "none",
#                 "color": "#dddddd",
#                 "align": "end"
#               }
#             ],
#             "width": "15px",
#             "offsetTop": "-5px",
#             "offsetStart": "7px"
#           },
#           {
#             "type": "text",
#             "text": "00:24",
#             "size": "xxl",
#             "color": "#FCA32D",
#             "align": "end",
#             "weight": "regular"
#           }
#         ],
#         "margin": "none"
#       },
#       {
#         "type": "separator",
#         "margin": "none",
#         "color": "#aaaaaa"
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "weight": "bold",
#                     "color": "#ffffff",
#                     "size": "xl",
#                     "text": "占",
#                     "contents": [],
#                     "gravity": "center",
#                     "align": "center",
#                     "offsetTop": "-1px"
#                   }
#                 ],
#                 "backgroundColor": "#9BB0CE",
#                 "width": "30px",
#                 "height": "30px",
#                 "cornerRadius": "20px"
#               },
#               {
#                 "type": "text",
#                 "color": "#333333",
#                 "size": "lg",
#                 "wrap": true,
#                 "text": "占找A店家維修,能否順利修好電腦保住資料",
#                 "margin": "sm",
#                 "contents": [],
#                 "gravity": "center"
#               }
#             ],
#             "margin": "sm"
#           }
#         ],
#         "spacing": "none",
#         "margin": "sm"
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [],
#                 "width": "251px",
#                 "margin": "none",
#                 "spacing": "none",
#                 "offsetStart": "sm"
#               }
#             ],
#             "height": "5px"
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "box",
#                     "layout": "vertical",
#                     "contents": [],
#                     "width": "40px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "⚊",
#                         "size": "xxl",
#                         "align": "center",
#                         "offsetBottom": "7px",
#                         "weight": "regular",
#                         "gravity": "bottom"
#                       }
#                     ],
#                     "width": "30px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "－",
#                         "size": "md",
#                         "offsetTop": "-4px",
#                         "align": "center",
#                         "gravity": "center",
#                         "color": "#999999"
#                       }
#                     ],
#                     "width": "90px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "上爻",
#                         "size": "lg",
#                         "weight": "regular",
#                         "color": "#333333",
#                         "gravity": "top"
#                       }
#                     ],
#                     "flex": 2
#                   }
#                 ],
#                 "margin": "xs",
#                 "height": "35px",
#                 "offsetTop": "5px"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "box",
#                     "layout": "vertical",
#                     "contents": [],
#                     "width": "40px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "✕",
#                         "size": "xl",
#                         "align": "center",
#                         "weight": "bold",
#                         "offsetBottom": "7px",
#                         "gravity": "bottom"
#                       }
#                     ],
#                     "width": "30px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "－",
#                         "size": "md",
#                         "offsetTop": "-4px",
#                         "align": "center",
#                         "gravity": "center",
#                         "color": "#999999"
#                       }
#                     ],
#                     "width": "90px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "五爻",
#                         "size": "lg",
#                         "weight": "regular",
#                         "color": "#333333",
#                         "gravity": "top"
#                       }
#                     ],
#                     "flex": 2
#                   }
#                 ],
#                 "margin": "xs",
#                 "height": "35px",
#                 "offsetTop": "5px"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "box",
#                     "layout": "vertical",
#                     "contents": [],
#                     "width": "52px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "⚋",
#                         "size": "xxl",
#                         "align": "center",
#                         "offsetBottom": "7px",
#                         "weight": "regular",
#                         "gravity": "bottom"
#                       }
#                     ],
#                     "width": "30px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "－",
#                         "size": "md",
#                         "offsetTop": "-4px",
#                         "align": "center",
#                         "gravity": "center",
#                         "color": "#999999"
#                       }
#                     ],
#                     "width": "90px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "四爻",
#                         "size": "lg",
#                         "weight": "regular",
#                         "color": "#333333",
#                         "gravity": "top"
#                       }
#                     ],
#                     "flex": 2
#                   }
#                 ],
#                 "margin": "xs",
#                 "height": "35px",
#                 "offsetTop": "5px"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "box",
#                     "layout": "vertical",
#                     "contents": [],
#                     "width": "52px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "〇",
#                         "size": "xl",
#                         "align": "center",
#                         "weight": "bold",
#                         "offsetBottom": "7px",
#                         "gravity": "bottom"
#                       }
#                     ],
#                     "width": "30px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "－",
#                         "size": "md",
#                         "offsetTop": "-4px",
#                         "align": "center",
#                         "gravity": "center",
#                         "color": "#999999"
#                       }
#                     ],
#                     "width": "90px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "三爻",
#                         "size": "lg",
#                         "weight": "regular",
#                         "color": "#333333",
#                         "gravity": "top"
#                       }
#                     ],
#                     "flex": 2
#                   }
#                 ],
#                 "margin": "xs",
#                 "height": "35px",
#                 "offsetTop": "5px"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "box",
#                     "layout": "vertical",
#                     "contents": [],
#                     "width": "52px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "✕",
#                         "size": "xl",
#                         "align": "center",
#                         "weight": "bold",
#                         "offsetBottom": "7px",
#                         "gravity": "bottom"
#                       }
#                     ],
#                     "width": "30px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "－",
#                         "size": "md",
#                         "offsetTop": "-4px",
#                         "align": "center",
#                         "gravity": "center",
#                         "color": "#999999"
#                       }
#                     ],
#                     "width": "90px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "二爻",
#                         "size": "lg",
#                         "weight": "regular",
#                         "color": "#333333",
#                         "gravity": "top"
#                       }
#                     ],
#                     "flex": 2
#                   }
#                 ],
#                 "margin": "xs",
#                 "height": "35px",
#                 "offsetTop": "5px"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "box",
#                     "layout": "vertical",
#                     "contents": [],
#                     "width": "52px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "⚋",
#                         "size": "xxl",
#                         "align": "center",
#                         "offsetBottom": "7px",
#                         "weight": "regular",
#                         "gravity": "bottom"
#                       }
#                     ],
#                     "width": "30px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "－",
#                         "size": "md",
#                         "offsetTop": "-4px",
#                         "align": "center",
#                         "gravity": "center",
#                         "color": "#999999"
#                       }
#                     ],
#                     "width": "90px"
#                   },
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "初爻",
#                         "size": "lg",
#                         "weight": "regular",
#                         "color": "#333333",
#                         "gravity": "top"
#                       }
#                     ],
#                     "flex": 2
#                   }
#                 ],
#                 "margin": "xs",
#                 "height": "35px",
#                 "offsetTop": "5px"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [],
#                 "height": "10px",
#                 "width": "251px",
#                 "margin": "none",
#                 "spacing": "none",
#                 "offsetStart": "sm"
#               }
#             ],
#             "height": "10px"
#           }
#         ],
#         "margin": "sm",
#         "cornerRadius": "10px",
#         "backgroundColor": "#CECCCA"
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [],
#                 "width": "8px"
#               },
#               {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "艮為山",
#                     "align": "center",
#                     "size": "md",
#                     "weight": "bold"
#                   }
#                 ]
#               },
#               {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "•",
#                     "align": "center",
#                     "size": "md",
#                     "color": "#bbbbbb"
#                   }
#                 ],
#                 "width": "20px"
#               },
#               {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "風水渙",
#                     "align": "center",
#                     "size": "md",
#                     "weight": "bold"
#                   }
#                 ]
#               },
#               {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [],
#                 "width": "10px"
#               }
#             ],
#             "offsetTop": "xs"
#           }
#         ],
#         "margin": "md",
#         "cornerRadius": "10px",
#         "borderColor": "#bbbbbb",
#         "borderWidth": "2px",
#         "height": "31px"
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "margin": "xs",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "contents": [
#               {
#                 "type": "button",
#                 "style": "secondary",
#                 "action": {
#                   "type": "postback",
#                   "label": "裝卦",
#                   "data": "+2025/10/25/0/24 // 0X$0X1 // 占找A店家維修,能否順利修好電腦保住資料",
#                   "displayText": "2025/10/25/0/24 - 0X$0X1\n占找A店家維修,能否順利修好電腦保住資料"
#                 },
#                 "color": "#91A4BC",
#                 "margin": "none",
#                 "height": "md"
#               }
#             ],
#             "margin": "xs"
#           }
#         ],
#         "cornerRadius": "10px",
#         "offsetTop": "3px"
#       }
#     ],
#     "backgroundColor": "#F2F1F0"
#   },
#   "styles": {
#     "footer": {
#       "separator": true
#     }
#   }
# }



if __name__ == '__main__':
	# addToJson (  linebotId ="U21eaaf32db85b983a842d9a9da81d8f1"	,UserName = "Benno"	,logInTime ="2023-2-1 23:52",command =	"時盤-2023-02-01-21-51"	,runtime = 1	,signUpTime = "2023-2-1 11:18",  userImage ="https://profile.line-scdn.net/0m03d2961a72519e9ae023945979128659aaf19ece8932"	 ,uiStyle ="A"	,subDataMode ="Lite"	,switch = "ON")
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
	flex_dict = get_all_user_flex()
	print(json.dumps(flex_dict, ensure_ascii=False, indent=4))