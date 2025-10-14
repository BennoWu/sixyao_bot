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



	# import os
	# import json
	# import pygsheets

	# credentials_json = os.environ.get('GOOGLE_CREDENTIALS')

	# if credentials_json:
	#     # 在 Render 上：使用環境變數
	#     credentials_dict = json.loads(credentials_json)
	#     gc = pygsheets.authorize(custom_credentials=credentials_dict)
	# else:
	#     # 在本地開發：使用檔案
	#     gc = pygsheets.authorize(service_file='googleSheetKey/sixyao-data-8f0c712298cd.json')

	# globalSheet = gc.open_by_url(
	#     'https://docs.google.com/spreadsheets/d/1Zlj55gQ5N75lWJYAyZ5Es6WTM_LS6SeFumZWlpLo6-0/edit?usp=sharing'
	# )


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








if __name__ == '__main__':
	# addToJson (  linebotId ="U21eaaf32db85b983a842d9a9da81d8f1"	,UserName = "Benno"	,logInTime ="2023-2-1 23:52",command =	"時盤-2023-02-01-21-51"	,runtime = 1	,signUpTime = "2023-2-1 11:18",  userImage ="https://profile.line-scdn.net/0m03d2961a72519e9ae023945979128659aaf19ece8932"	 ,uiStyle ="A"	,subDataMode ="Lite"	,switch = "ON")
	# loadAllJson()
	# print(googleToJson())
	print(jsonToGoogle())
	# logToGoogle()

	# setItemData ( "CCC" , "temp" , "inData" )


	# addToJson("BENNO","aaaaab","eeeecc",uiStyle = "C")
	# print( getItemData ( "BENNO","signUpTime"))
	# print( uiSetting( "U21eaaf32db85b983a842d9a9da81d8f1","set full a")  )
	# setItemData ( "BENNO" , "switch" , "WW" )