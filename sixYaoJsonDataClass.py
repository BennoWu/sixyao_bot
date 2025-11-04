import json,os

from jsonFun import *

# from logBackup import ( logDataFun as logBK_logDataFun,    uploadCsvToGoogleSheet as logBK_uploadCsv  )



from datetime import datetime,timezone,timedelta

## 檢查NOTION帳號資料是否可執行
from notion_client import Client
def checkNotionAcc(token, pageId):
	# return True
	try:
		notion = Client(auth=token)
		notion.pages.retrieve(pageId)
		print( "notion check ok" )
		return True
	except Exception as e:
		print(f"notion check錯誤: {e}")
		return False







class jsonDataClass:

	def __init__( self, linebotId , linebotUserName = None , userImage = None , command = "", sheetName = "userID_list" ):



		# If JSON does not exist yet, sync first
		if not os.path.isfile("__sixYoSet__.json"):
			try:
				print("⚠️ No JSON found. Syncing from Google...")
				googleToJson()
			except:
				print("⚠️ Google sync failed, will create new JSON")

		# logInTime = datetime.now ( timezone ( timedelta ( hours = int(self.utc) ) ) ).strftime( "%Y/%m/%d/%H/%M" ) ## '2025/06/14/12/46'
		# command = command.replace( "​","")

		## 取得現在時間
		logInTime = datetime.now ( timezone ( timedelta ( hours = 8 ) ) ).strftime( "%Y/%m/%d/%H/%M" ) ## '2025/06/14/12/46'
		# logBK_logDataFun( linebotId , linebotUserName , logInTime , command  )
		self.newItem = True

		if os.path.isfile("__sixYoSet__.json") == True: ## 如果檔案存在
			# with open('__sixYoSet__.json') as f:
			# 	dataDict = json.load(f)
				
			with open('__sixYoSet__.json', 'r', encoding="utf-8") as f:
				dataDict = json.load(f)

				if linebotId in dataDict.keys(): ## 如果已經有這個id
					self.newItem = False



		self.linebotId = linebotId
		self.linebotUserName = linebotUserName
		# "User ID"	"User Name"	 "Log in Time"	"Last Data" "UI Color Style" "UI Word Style" "Run"		


		

		if self.newItem == False: # 如已經有資料就load資料填入
			print("OLD..")


			self.userImage = userImage
			self.logInTime = logInTime
			self.signUpTime = dataDict[ linebotId ] ["signUpTime"]
			
			self.command = command
			self.runtime = dataDict[ linebotId ] ["runtime"]
			self.uiStyle = dataDict[ linebotId ] ["uiStyle"]## 顏色模式 CA  CB  CC
			self.fontStyle = dataDict[ linebotId ] ["fontStyle"]       ## 字型模式 FA宋體  FB圓體  FC黑體
			self.tipsMode = dataDict[ linebotId ] ["tipsMode"]        ## 提示用小字 ON , OFF
			self.subDataMode = dataDict[ linebotId ] ["subDataMode"]
			self.utc = dataDict[ linebotId ] ["utc"]

			self.notionToken_pageId = dataDict[ linebotId ] ["notionToken_pageId"]
			# self.other = dataDict[ linebotId ] ["other"]

			self.switch = dataDict[ linebotId ] ["switch"]

			self.temp = dataDict[ linebotId ] ["temp"]		


	
	# linebotId         ## linebot上的ID
	# linebotUserName   ## line上面的名字
	# userImage	        ## 使用者頭貼圖片路徑
## =============================================================
	# logInTime   ## 最後登入時間
	# signUpTime  ## 首次登入時間
	# command     ## 最後一次的指令
	# runtime     ## 使用次數，計數用

	# uiStyle     ## ui顏色
	# fontStyle   ## 字型
	# tipsMode    ## 是否有小字提示, ON , OFF

	# subDataMode  ## 未來可能要補充功能預留
	# utc          ## 時區，台灣為+8東八區
	# switch       ## 控制權限 ON, OFF
	# temp         ## 補充資訊用



		# 如果沒有就新建一組
		else:                      
			print("NEW")

			#這兩項在上面定義過
				# linebotId
				# UserName

			# ## 取得現在時間 上面也定義過了...
			# logInTime = datetime.now ( timezone ( timedelta ( hours = 8 ) ) ).strftime( "%Y/%m/%d/%H/%M" ) ## '2025/06/14/12/46'		

			# 🔥 修改這裡：先檢查 JSON 中是否已有資料（可能是從 Google 同步來的）
			if os.path.isfile("__sixYoSet__.json"):
				with open('__sixYoSet__.json', 'r', encoding="utf-8") as f:
					dataDict = json.load(f)
					
				# 🔥 如果 JSON 中已有這個用戶的資料（從 Google 同步），使用 JSON 中的值
				if linebotId in dataDict:
					existing_data = dataDict[linebotId]
					
					self.userImage = userImage if userImage else existing_data.get("userImage")
					self.logInTime = logInTime
					self.signUpTime = existing_data.get("signUpTime", logInTime)
					self.command = command
					self.runtime = existing_data.get("runtime", 1)
					self.uiStyle = existing_data.get("uiStyle", "UA")
					self.fontStyle = existing_data.get("fontStyle", "FB")
					self.tipsMode = existing_data.get("tipsMode", "ON")
					self.subDataMode = existing_data.get("subDataMode", "Full")
					self.utc = existing_data.get("utc", 8)
					
					# 🔥 關鍵：從 JSON 讀取 notionToken_pageId（可能是 True/False/None）
					self.notionToken_pageId = existing_data.get("notionToken_pageId", None)
					
					self.switch = existing_data.get("switch", "ON")
					self.temp = existing_data.get("temp", None)
				else:
					# 真正的新用戶，使用預設值
					self._set_default_values(userImage, logInTime, command)
			else:
				# JSON 檔案不存在，使用預設值
				self._set_default_values(userImage, logInTime, command)
																											
		addToJson ( linebotId = self.linebotId  ,
					UserName = self.linebotUserName  ,

					userImage = self.userImage ,
					signUpTime = self.signUpTime  ,
					logInTime = self.logInTime   ,
					command =  self.command  ,
					runtime = self.runtime+1 ,

					uiStyle = self.uiStyle ,
					fontStyle = self.fontStyle ,
					tipsMode = self.tipsMode ,

					subDataMode = self.subDataMode ,
					utc = self.utc ,

					notionToken_pageId	= self.notionToken_pageId,
					# other = self.other,

					switch = self.switch, 

					temp = self.temp

					)


	def _set_default_values(self, userImage, logInTime, command):
		"""設定預設值的輔助函數"""
		self.userImage = userImage
		self.logInTime = logInTime
		self.signUpTime = logInTime
		self.command = command
		self.runtime = 1
		self.uiStyle = "UA"
		self.fontStyle = "FB"
		self.tipsMode = "ON"
		self.subDataMode = "Full"
		self.utc = 8
		self.notionToken_pageId = False
		self.switch = "ON"
		self.temp = None




	# 設定界面模式,ABC模式, 完整版與簡版
	def uiJsonSetting ( self ,  command ):
		org_command = command
		command = command.strip().replace("  ","/").replace(",","/").replace(" ","/").replace(".","/")
		rtn_message = ""
		comList = command.split( "/" )
		print( "> Set:",command , comList )

		if "utc" in command.lower():   # set utc 5
			print ( "Set:" , comList[1] , comList[2]   )
			try:
				if str(abs(int( comList[2] ))).isdigit() == True:
					self.utc = int( comList[2] )
					rtn_message =  "utc - {}".format(self.utc)
			except:
				print( comList[1] + "要是數字")


		elif "temp" in command.lower():   # set temp xxxxxx
			fullCmd = org_command.replace( "set temp ","" )
			print ( "Set:" , comList[1] , "---", fullCmd   )

			if comList[2] == "none":
				self.temp = "-"
				rtn_message =  "temp clear"
			else:
				self.temp =  fullCmd


		elif "set" in comList[0].lower():
			# print( comList[1] )
			# if comList[-1].lower() in ["ua","ub","uc","fa","fb","fc","on","off","full","lite"]:
			
			if comList[-1].lower() in ["ua","ub","uc"]:  # set ca
				self.uiStyle = comList[1].upper()	
				print( "Set:" , self.uiStyle )
				rtn_message =  "uiStyle - {}".format(self.uiStyle)

			elif comList[-1].lower() in ["fa","fb","fc"]:  ## set fa
				self.fontStyle = comList[1].upper()	
				print( "Set:" , self.fontStyle )
				rtn_message =  "fontStyle - {}".format(self.fontStyle)

			elif "tips" in comList:     ## set tips on
				self.tipsMode = comList[-1].upper()
				print( "Set:" , self.tipsMode )
				rtn_message =  "tipsMode - {}".format(self.tipsMode)

			elif comList[-1].lower() in ["full","lite"]:  ## set full
				self.subDataMode = comList[1].upper()
				print( "Set:" , self.subDataMode )
				rtn_message =  "subDataMode - {}".format(self.subDataMode)

			# "set nt tokentoken,pageId"
			elif  comList[1].lower() in  [ "nt" , "notion"]: ## set notion

				import  supabase_io
				if comList[2] == "none":
					supabase_io.delete_user_token( self.linebotId )
					self.notionToken_pageId = "off"
					rtn_message =  "Notion — Canceled"

				else:
					if len( comList ) == 4:
						token_buf = comList[2]   ## get token
						pageId_buf = comList[3] ## get page


						## ====== 如果token和page id都通過notion的測試 ======
						if checkNotionAcc( token_buf , pageId_buf ) == True:
							self.notionToken_pageId = True
							rtn_message =  "Notion — Success"

							## ===== 就寫入資料庫 =====
							supabase_io.save_user_data(
								user_id = self.linebotId,
								notion_token = token_buf,
								page_id = pageId_buf
							)


						## ====== 否則回傳打槍訊息 ======
						else:
							rtn_message =  "API token is invalid....請檢查notion資料"
					else:
						rtn_message =  "輸入資料格式錯誤"

			elif "switch" in comList:
				## set U21eaaf32db85b983a842d9a9da81d8f1 switch on
				user_id = comList[1]
				item =  comList[2]
				value =  comList[3]
				rtn =  save_json_data( user_id , item , value.upper() )
				# print( ">>##" , rtn )
				if rtn == True:
					rtn_message =  f"set {user_id} - {item} - {value}"
				else:
					rtn_message =  f"set {user_id} - {item} - {value} 失敗"




				# self.other = pageId_buf
			else:
				print ( ">> command error")
				rtn_message =  ">> seeting command error"




		# addToJson (  linebotId = self.linebotId  , uiStyle = self.uiStyle , fontStyle = self.fontStyle ,  tipsMode = self.tipsMode ,  subDataMode = self.subDataMode  , utc = self.utc )

		addToJson (  linebotId = self.linebotId  , 
						uiStyle = self.uiStyle , 
						fontStyle = self.fontStyle ,  
						tipsMode = self.tipsMode ,  
						subDataMode = self.subDataMode  , 
						utc = self.utc ,
						notionToken_pageId	= self.notionToken_pageId,
						# other = None,
						temp = self.temp
						 )

		return rtn_message

		# addToJson ( linebotId = None  ,
		# 				UserName = None ,
		# 				signUpTime = None  ,
		# 				logInTime = None ,
		# 				command = None ,
		# 				runtime = None ,
		# 				userImage = None  ,
		# 				uiStyle = None,
		# 				fontStyle = None,
		# 				tipsMode = None,
		# 				subDataMode = None,
		# 				utc = None,

		# 				# notionToken_pageId	= None,
		# 				# other = None,

		# 				switch = None ,
		# 				temp = None 
		# 				):



# # https://blog.csdn.net/lilongsy/article/details/80242427
	

	def showData( self ):
		print( "                 id: " ,self.linebotId )
		print( "               name: " ,self.linebotUserName )
		print( "              image: " ,self.userImage )		
		print( "            regTime: " ,self.signUpTime )
		print( "          loginTime: " ,self.logInTime )		
		print( "            command: " ,self.command )
		print( "            runtime: " ,self.runtime )

		print( "            uiStyle: " ,self.uiStyle )
		print( "          fontStyle: " ,self.fontStyle )
		print( "           tipsMode: " ,self.tipsMode )
		print( "        subDataMode: " ,self.subDataMode )
		print( "            utcHour: " ,self.utc )	

		print( "notion token/pageId: " ,self.notionToken_pageId )	
		# print( "              other: " ,self.other )	

		print( "             switch: " ,self.switch )
		print( "               temp: " ,self.temp )		

if __name__ == '__main__':
	# aa = jsonDataClass ("PPP" , "WWWWWW")
	# aa.postSetting(  "時盤-2050-1-30-2-25" , "2050-1-30-2-18" )
	# aa.showData()
	# print(aa.uiJsonSetting( "set lite"))
	# aa.timeStepJump( "+1")
	# aa.showData()




	lineBotId = "Temp123"
	lineBotName = "BBB"
	userImage = "www.xyz.com/aa/5465465.png"

	# fullDataInput = "set utc 7"
	# fullDataInput = "set ub"
	# fullDataInput = "Set tips ON"
	fullDataInput = "Set tips OFF"
	# fullDataInput = "set nt none"
	# fullDataInput = "set temp yyyyyyyyyyyyyyy"
	# fullDataInput = "set temp none"	
	# fullDataInput = "set nt notion_token/page_id"
	# from datetime import datetime,timezone,timedelta

	# ## 取得現在時間
	# logInTime_buf = datetime.now ( timezone ( timedelta ( hours = 8 ) ) ).strftime( "%Y/%m/%d/%H/%M" ) ## '2025/06/14/12/46'

	fullDataInput = fullDataInput.strip() ## 清除頭尾空格

	# jsonData = jsonDataClass( lineBotId , lineBotName , userImage  , fullDataInput ) ## class建立
	jsonData = jsonDataClass( lineBotId  ) ## class建立


	jsonData = jsonDataClass(
		linebotId = lineBotId,
		linebotUserName = lineBotName,
		userImage = userImage,
		command = "inputMsg"
	)
	# utc_hour =  jsonData.utc:	

	# # 如果不是ON，就代表權限被OFF掉了，程式中止
	# if jsonData.switch.upper() != "ON": ## user的switch… 如果不是ON，表示權限關閉狀態
	# 	print ( "404" )
	# 	exit()

	# # 設定模式
	# if ("set" in fullDataInput.lower())  or ("utc" in fullDataInput.lower()) :
	# 	returnMsg = jsonData.uiJsonSetting( fullDataInput )
	# 	# lineSend_fun( replyUrl )
	# 	# print ( returnMsg )

	jsonData.showData()
	print( jsonData.utc )