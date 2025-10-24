# -*- coding: utf-8 -*-


allDataDict = {'inputGua': ['1', '0', '1', '1', '1', '@'], 'yearGanZi': '甲辰', 'monthGanZi': '甲戌', 'dayGanZi': '甲子', 'hourGanZi': '丙寅', 'jeChi': '霜降>>立冬', 'week': '(日)', 'time': '04:42', 'flower_po': '酉', 'horse_po': '寅', 'guan_po': '寅', 'helpful_po': '丑未', 'yangKnife_po': '卯', 'changeIdIndex': ['X', 'X', 'X', 'X', 'X', 'O'], 'inputGuaList': ['1', '0', '1', '1', '1', '@'], 'mainGuaName': '同人之革卦', 'vs_type': '火>>水', 'home_number': '13', 'home_up': '天火', 'home_dn': '同人', 'home_title': '天火同人', 'home_upGua': '乾', 'home_dnGua': '離', 'home_inOutGua': '乾離', 'home_rowType': '火', 'home_shiYao': '3', 'home_innYao': '6', 'home_guaBody': '寅', 'home_naGia': ['卯', '丑', '亥', '午', '申', '戌'], 'home_kongWang': ['X', 'X', 'O', 'X', 'X', 'O'], 'home_naGiaType': ['木', '土', '水', '火', '金', '土'], 'home_family': ['父母', '子孫', '官鬼', '兄弟', '妻財', '子孫'], 'home_sixAnimal': ['青龍', '朱雀', '勾陳', '螣蛇', '白虎', '玄武'], 'home_lostFamily': [], 'hide_family': ['X', 'X', 'X', 'X', 'X', 'X'], 'hide_naGia': ['X', 'X', 'X', 'X', 'X', 'X'], 'change_number': '49', 'change_up': '澤火', 'change_dn': '革', 'change_title': '澤火革', 'change_upGua': '兌', 'change_dnGua': '離', 'change_inOutGua': '兌離', 'change_rowType': '水', 'change_shiYao': '4', 'change_innYao': '1', 'change_guaBody': '卯', 'change_naGia': ['卯', '丑', '亥', '亥', '酉', '未'], 'change_kongWang': ['X', 'X', 'O', 'O', 'X', 'X'], 'change_naGiaType': ['木', '土', '水', '水', '金', '土'], 'change_family': ['子孫', '官鬼', '兄弟', '兄弟', '父母', '官鬼'], 'change_sixAnimal': ['青龍', '朱雀', '勾陳', '螣蛇', '白虎', '玄武']}

def get_cutoff_index(text , target_weight = 14 ):
	"""
	從0開始累加字符權重，找到累加到目標權重的截止索引
	
	權重規則：
	- 中文字符 = 1.0
	- 空格 = 0.5
	- 半形符號 ()[] = 0.5
	- 數字 = 0.5
	- 標點 .,; 等 = 0.2
	- 英文字母 = 0.5
	
	Args:
		text (str): 輸入的文字字串
		target_weight (float): 目標權重值，預設16
		
	Returns:
		int or None: 達到目標權重的字符索引，如果整個字串權重不足則返回None
	"""
	current_weight = 0.0
	
	for i, char in enumerate(text):
		char_weight = get_char_weight(char)
		
		# 檢查加上這個字符後是否會達到或超過目標權重
		if current_weight + char_weight >= target_weight:
			return i
		
		current_weight += char_weight
	
	# 如果整個字串都沒有達到目標權重，返回None
	return None


def get_char_weight(char):
	"""
	根據字符類型返回對應權重
	"""
	if is_chinese_char(char):
		return 0.9
	elif char == ' ':  # 空格
		return 0.5
	elif char in '()[]{}':  # 半形符號
		return 0.5
	elif char.isdigit():  # 數字
		return 0.5
	elif char in '.,;:!?。，；：！？':  # 標點符號
		return 0.2
	elif char.isalpha():  # 英文字母
		return 0.5
	else:  # 其他字符
		return 0.5


def is_chinese_char(char):
	"""
	判斷字符是否為中文字符
	"""
	chinese_ranges = [
		(0x4E00, 0x9FFF),   # CJK統一漢字
		(0x3400, 0x4DBF),   # CJK擴展A
		(0x20000, 0x2A6DF), # CJK擴展B
		(0x2A700, 0x2B73F), # CJK擴展C
		(0x2B740, 0x2B81F), # CJK擴展D
		(0x2B820, 0x2CEAF), # CJK擴展E
		(0x2CEB0, 0x2EBEF), # CJK擴展F
	]
	
	char_code = ord(char)
	for start, end in chinese_ranges:
		if start <= char_code <= end:
			return True
	return False










# 將 PIL 圖片轉換為字節流
def image_to_byte_array(image):
	from io import BytesIO
	img_byte_arr = BytesIO()  # 創建字節流對象
	image.save(img_byte_arr, format='PNG')  # 保存圖片為 PNG 格式
	img_byte_arr.seek(0)  # 重置字節流的指針
	return img_byte_arr




# # 上傳圖片到 Imgur ## 字節流模式
# def uploadImgurIO( image_byte_array ):
# 	import datetime
# 	import requests
# 	# from PIL import Image, ImageDraw
# 	from io import BytesIO
# 	from imgurpython import ImgurClient

# 	# 將圖片轉換為字節流
# 	img_byte_arr = image_to_byte_array(image_byte_array)

# 	# 設定 Imgur 認證信息
# 	album_id = 'FhfzevH'
# 	client_id= '53177fc1be648f6'
# 	client_secret= 'cb996df2cf01b82305aceb9e5c9d258a46a7b084'
# 	access_token = '44428b7d1cc740be9b475a0cb866a99e3fe44045'
# 	refresh_token = '7e5df6de118669ead4a29cc5e51b4e6a6e123b54'

# 	url = "https://api.imgur.com/3/upload"
# 	headers = {
# 		"Authorization": f"Bearer {access_token}"  # 使用 access_token 進行身份驗證
# 	}
# 	files = {
# 		'image': img_byte_arr
# 	}
# 	data = {
# 		'album': album_id  # 指定上傳到的相簿 ID
# 	}

# 	# 發送 POST 請求上傳圖片
# 	response = requests.post(url, headers=headers, files=files, data=data)
	
# 	# 如果成功，返回圖片的 URL
# 	if response.status_code == 200:
# 		data = response.json()
# 		print(f"圖片上傳成功，圖片網址：{data['data']['link']}")
# 	else:
# 		print(f"圖片上傳失敗，錯誤信息：{response.status_code}, {response.text}")



def loopFun():
	item = [ "0","1","X","@"]
	import itertools
	digitsList = [ "@X0000","@X1000","@X1100","@X1110","@X1111","011100","@X11X0"]
	# digitsList = [ "@X0000","@X1000"]
	res = []
	for a in digitsList:
		# digits = '@X0000'
		permutations = itertools.permutations(a)
		buf =  [''.join(p) for p in permutations]
		buf = list( set( buf ))
		res += buf
	print(res)
	print( len(res ))
	return res



# > ['-', 'Ob0', '-', 'Pa2', '-', 'Oa1']
# > ['-', '-', 'Oa0', '-', 'Ob2', '-']

def getTypeColorC( inputItem ):

	colorType = inputItem[1]    ## Pc 的 c
	threeHoType = inputItem[0]  ## Pc 的 P

	threeHo_colorA = "#a3c4b4"
	threeHo_colorB = "#d39f9f"
	threeHo_colorC = "#aaaaaa"
	threeHo_colorD = "#8caec4"


	lite_colorA = "#a3c4b4"
	lite_colorB = "#d39f9f"
	lite_colorC = "#aaaaaa"
	lite_colorD = "#8caec4"


	# lite_colorA = "#d3e2da"
	# lite_colorB = "#d8c0c0"
	# lite_colorC = "#bbbbbb"
	# lite_colorD = "#ccd9e2"




	# print( "^^^^^", colorType ,threeHoType )

	if threeHoType == "O":
		if inputItem[1] == "a":
			return threeHo_colorA
		if inputItem[1] == "b":
			return threeHo_colorB		
		if inputItem[1] == "c":
			return threeHo_colorC
		if inputItem[1] == "d":
			return threeHo_colorD
	else:
		if inputItem[1] == "a":  ## 木
			return lite_colorA
		if inputItem[1] == "b":  ## 火
			return lite_colorB		
		if inputItem[1] == "c":  ## 金
			return lite_colorC
		if inputItem[1] == "d":  ## 水
			return lite_colorD		
























										  # "uiStyle" = "CB", "fontStyle" = "Fb","tipsMode" = "ON"

def drawUi_v1( allDataDict = allDataDict , tipsMode = "on" ,  show = True , savePic = False , notion = False ):


	if tipsMode.lower() == "on":
		noteSwitch = True 
	else:
		## 專家模式不開啟提示
		noteSwitch = False



	print( "allDataDict ->> ", allDataDict )
	# print( "fontStyle ->> ", fontStyle )
	print( "tipsMode ->> ", tipsMode )
	# print( "uiStyle ->> ", uiStyle )








	from PIL import Image,ImageFont,ImageDraw,ImageFilter,ImageChops 

	# note = "台北林小姐"

	screenWidth = 1024 # 1080
	screenHight = 1750

# 1070/1545
	# https://www.behance.net/gallery/58084819/24-china-24-solar-terms
	# https://www.geeksforgeeks.org/python-pil-imagedraw-draw-text/

	# 创建一张底图,用来绘制
	# bgColor = "#F9F9F9"
# Image.open('paper02.jpg')
	img = Image.open('paper_1800.jpg').convert("RGB")
	# img = Image.open('papper_bg_02.jpg').convert("RGB")

	bgColor = (255,255,255)
	# img = Image.new("RGB", (screenWidth, screenHight), bgColor )
	# img = Image.new("RGBA", (screenWidth, screenHight), (0, 0, 0, 0))  # 全透明背景
	userDefineHight = 0

################################################################
################################################################


	pf_TC_light   = "font_v01/PingFangTC-Light.otf"	        ## 細
	pf_TC_regular = "font_v01/PingFangTC-Regular.otf"	    ## 標準
	pf_TC_medium  = "font_v01/PingFangTC-Medium.otf"		## 中
	pf_TC_bold    = "font_v01/PingFangTC-Semibold.otf"	    ## 粗

	myriad_reg = "font_v01/MyriadPro-Regular.otf"	    ## 時間數字
	SourceSans3 =    "font_v01/SourceSans3-Medium.ttf" ## 分數小字



	titleGray =  "#B1B1B1"  ## 四柱用的灰色
	timeColor = "#F9AE3B"  ## 右上時間橘黃色

	subGray = "#656565"



	sixYoSymbol = "#65728E"  ## 爻的符號 - + o x

	siIn_color = "#859099"  ## 世應的底色
	blue_color = "#2C5F83"

	lightGray = "#E4E7EA"


	midGray = "#B1B1B1"

	draw = ImageDraw.Draw(img)

	mainColor = "#080C30"   ## "#092A3F" #"#000000"
	lineColor = subGray
	twoSideSpace = 70


	## 藍色外框
	def draw_SquareFull ( hight = 560 , hightSize = 926 , sideSpace = twoSideSpace , roundSize = 35 , fillColor = lightGray , outlineColor = None ,  LineWidth = 0 ):
		draw.rectangle([ sideSpace , hight , screenWidth - sideSpace  , hight + hightSize ], fill = fillColor, width = LineWidth , outline = outlineColor )



		# 分割橫線
	def draw_H_line ( hight = 427  , sideSpace = twoSideSpace , color = lineColor , LineWidth = 2 ):
		draw.line((  sideSpace , hight , screenWidth - sideSpace , hight ), fill= color, width = LineWidth )

	draw_H_line ( hight = 155 )
	draw_H_line ( hight = 422 )
	draw_H_line ( hight = screenHight - 130 )

	# # 直槓 |||||||
	# def draw_InfoLine ( center =0  , hight = 270   , size = wordingSize  , color = mainColor ,lineWidth= 5 ):
	# 	draw.line(( center ,  hight+size+2 ,  center , hight ), fill= color , width= lineWidth )

	def roundSquare (  hight = 560 , hightSize = 926 , sideSpace = twoSideSpace , roundSize = 35 , fillColor = lightGray , outlineColor = None ,  LineWidth = 0 ):
		# (x0, y0, x1, y1), radius=圓角半徑
		draw.rounded_rectangle([ sideSpace , hight , screenWidth - sideSpace  , hight + hightSize ], radius = roundSize , fill = fillColor, width = LineWidth , outline = outlineColor )



	## 畫缺角方形
	def draw_SquareCut(  x = 100, y = 500, squareSize = 60, cut = 10, outlineColor = "black", fillColor = None, lineWidth = 3 ):
		"""
		畫一個左上角被切掉的方形
		:param draw: PIL.ImageDraw.Draw 對象
		:param x, y: 方形左上角座標
		:param squareSize: 方形邊長
		:param cut: 切角大小
		:param outlineColor: 邊框顏色
		:param fillColor: 填色
		:param lineWidth: 邊框寬度
		"""
		# 定義五個點（順時針）
		polygon = [
			(x + cut, y),                  # 上邊切角後
			(x + squareSize-lineWidth, y),           # 右上
			(x + squareSize-lineWidth, y + squareSize), # 右下
			(x, y + squareSize),           # 左下
			(x, y + cut)                   # 左邊切角後
		]
		# 畫多邊形
		draw.polygon(polygon, outline=outlineColor, fill=fillColor)
		# 再畫邊框線條（控制寬度）
		draw.line(polygon + [polygon[0]], fill=outlineColor, width=lineWidth)
	## 字小框
	def draw_SquareMark ( x = 100  , y = 200  , squareSize = 50   , outlineColor = subGray , lineWidth = 3 ):
		draw.rectangle(( x , y , x + squareSize , y + squareSize ), fill= None , outline= outlineColor ,  width = lineWidth )




###############################################################################################################################
###############################################################################################################################
###############################################################################################################################

# "#EAE9E8"
	## 淺色圓角大框底色"#E8E9EA"
	mainSquareHight = 560
	# roundSquare (  hight = mainSquareHight , hightSize = 873 , sideSpace = twoSideSpace+4 , fillColor = None , outlineColor = "#E8E9EA" , LineWidth = 2 ) 




	## 下方圓角橫框
	roundSquare (  hight = screenHight-268 , hightSize = 90 , sideSpace = twoSideSpace+3 , fillColor = None , outlineColor = "#777777" , LineWidth = 4 )

	## 最大邊框"#ACA899"
	# draw_SquareFull (  hight = 0 , hightSize = screenHight-2, sideSpace = 0 , fillColor = None , outlineColor = "#959799" , LineWidth = 18 )
	roundSquare (  hight = 8 , hightSize = screenHight-18, sideSpace = 8 ,roundSize = 30 ,   fillColor = None , outlineColor = "#959799" , LineWidth = 8 )




	# 直槓 |||||||
	def draw_InfoLine (  center = 100 , hight = 270   , size = 150  , lineColor = lightGray , lineWidth= 3 ):
		draw.line(( center ,  hight ,  center , hight + size ), fill= lineColor , width= lineWidth )
	

	# 主要字型
	def makeText ( text , x , y, wordingSize = 50 , wordingFont = pf_TC_regular , color = mainColor , fixY = 0 , noteSwitch = True  ):

		if noteSwitch == True: 
			other_style = ImageFont.truetype(  wordingFont , wordingSize, encoding="utf-8")
			draw.text(( x , y+ fixY ), text , fill= color , font = other_style )



	## makePoint,circle
	def makePoint ( x , y , radious , pointColor = None , lineColor = None , LineWidth = 0 , switch = True ):
		# print( LineWidth )
		# print(pointColor )

		if switch == True:
			draw.ellipse(    (  ( x,y ) , ( x+radious , y+radious )  ) , fill = pointColor , outline = lineColor , width = LineWidth ) 


			

	## 占問內容 zoo
	import string

	def is_english(ch):
		"""判斷是否為英文 A-Z / a-z"""
		return ch in string.ascii_letters



	noteSize = 55
	one_index = get_cutoff_index( allDataDict['note'] , target_weight = 15 )
	print( one_index )

	if allDataDict['note'] != "XXX":
		if one_index != None:



			wordingAdj = one_index 
		# text_value = allDataDict['note'][:wordingAdj] + '\n' + allDataDict['note'][wordingAdj:]
			# print(f"長字符: '{allDataDict['note'] [w_index]}'")

			note = allDataDict['note']
			indexAdj = 0
			if wordingAdj > 0 and wordingAdj < len(allDataDict['note']):
				prev_char = allDataDict['note'][wordingAdj-1]
				next_char = allDataDict['note'][wordingAdj]

				# print("prev:", repr(prev_char), prev_char.isalpha())
				# print("next:", repr(next_char), next_char.isalpha())


				print("prev:", repr(prev_char), prev_char.isalpha(), prev_char.isascii())
				print("next:", repr(next_char), next_char.isalpha(), next_char.isascii())

				# 如果斷在英文單字中間，就往前找到單字開頭
				if is_english(prev_char) and is_english(next_char):
					indexAdj = 1
					while wordingAdj - indexAdj > 0 and is_english(note[wordingAdj - indexAdj - 1]):
						indexAdj += 1
						print("+")

			final_index = wordingAdj - indexAdj

			print ( wordingAdj , indexAdj)
			if len( allDataDict['note'][ final_index:] ) == 1:
				makeText ( allDataDict['note'] , twoSideSpace -10 , 80-15 , wordingSize = noteSize-3 , wordingFont = pf_TC_light , color = mainColor )    
			else:
				makeText ( (allDataDict['note'][:final_index ] + '\n' + allDataDict['note'][ final_index:]) , twoSideSpace -10 , 72-35-15 , wordingSize = noteSize , wordingFont = pf_TC_light , color = mainColor )  



		else:
			makeText ( allDataDict['note'] , twoSideSpace -10 , 80-15 , wordingSize = noteSize , wordingFont = pf_TC_light , color = mainColor )  


	



	## 四柱大字 
	spaceBuf = 0
	basicHight = 155
	for pillar_id in range(4):

		if pillar_id == 0:
			if allDataDict['user_define'] == True:
				makeText ( "— —" , twoSideSpace + 30 + spaceBuf, 180 , wordingSize = 70 , wordingFont = pf_TC_bold , color = titleGray ) 	
			else:
				makeText ( allDataDict['yearGanZi'] , twoSideSpace + 13 + spaceBuf, basicHight , wordingSize = 91 , wordingFont = pf_TC_bold , color = titleGray )  
			makeText ( "年" , twoSideSpace -18 + spaceBuf , basicHight+60 , wordingSize = 38 , wordingFont = pf_TC_bold , color = midGray )  
		elif pillar_id == 1:

			## 三合 月 
			if allDataDict['month_day_ThreeHoId'][0][0] in ( "O", "P" )  and  noteSwitch == True:
				monthColor = getTypeColorC( allDataDict['month_day_ThreeHoId'][0] ) ## 月
				if allDataDict[ "monthGanZi" ][-1] == "月":
					draw_SquareMark( x = twoSideSpace + 12 + spaceBuf   , y =  basicHight + 18    , squareSize = 94  , outlineColor = monthColor  ) 
				else:
					draw_SquareMark( x = twoSideSpace + 102 + spaceBuf   , y =  basicHight + 18    , squareSize = 94  , outlineColor = monthColor  ) 


			makeText ( allDataDict['monthGanZi'] , twoSideSpace + 13 + spaceBuf, basicHight , wordingSize = 91 , wordingFont = pf_TC_bold , color = mainColor )  
			makeText ( "月" , twoSideSpace -18 + spaceBuf , basicHight+60 , wordingSize = 38 , wordingFont = pf_TC_bold , color = subGray )



		elif pillar_id == 2:
			## 三合  日
			if allDataDict['month_day_ThreeHoId'][1][0] in ( "O", "P" )  and  noteSwitch == True:
				dayColor = getTypeColorC( allDataDict['month_day_ThreeHoId'][1] ) ## 日
				draw_SquareMark( x = twoSideSpace + 102 + spaceBuf   , y =  basicHight + 18    , squareSize = 94  , outlineColor = dayColor  ) 

			makeText ( allDataDict['dayGanZi'] , twoSideSpace + 13 + spaceBuf, basicHight , wordingSize = 91 , wordingFont = pf_TC_bold , color = mainColor )  
			makeText ( "日" , twoSideSpace -18 + spaceBuf , basicHight+60 , wordingSize = 38 , wordingFont = pf_TC_bold , color = subGray ) 

		elif pillar_id == 3:




			if ( allDataDict['user_define'] == True )  or ( allDataDict['hourGanZi'] == "X" ):
				makeText ( "— —" , twoSideSpace + 30 + spaceBuf, 180 , wordingSize = 70 , wordingFont = pf_TC_bold , color = titleGray ) 
			else:
				makeText ( allDataDict['hourGanZi'] , twoSideSpace + 13+ spaceBuf , basicHight , wordingSize = 91 , wordingFont = pf_TC_bold , color = titleGray ) 
			makeText ( "時" , twoSideSpace -19 + spaceBuf , basicHight+60 , wordingSize = 38 , wordingFont = pf_TC_bold , color = midGray )  			 			

		spaceBuf += 227

	jeChiBuf = ""
	## 節氣
	if allDataDict['user_define'] == False: ## 日辰自訂模式時不秀節氣
		if allDataDict['jeChi'][1] == "!":
			jeChiBuf = "．" + "["+allDataDict['jeChi'][0]+ "]"+ "-" + allDataDict['jeChi'][2]
			# makeText ( "•"   , twoSideSpace + 300-10  , 358 , wordingSize = 30 , wordingFont = pf_TC_medium , color = midGray )

			# makeText ( "["+allDataDict['jeChi'][0]+ "]"+ "-" + allDataDict['jeChi'][2]   , twoSideSpace + 324-10  , 348 , wordingSize = 41 , wordingFont = pf_TC_medium , color = mainColor )
		else:
			jeChiBuf = "．" + allDataDict['jeChi'][0]+ " > " + allDataDict['jeChi'][2] 
			# makeText ( "•"   , twoSideSpace + 292  , 358 , wordingSize = 30 , wordingFont = pf_TC_medium , color = midGray )
			# makeText (  allDataDict['jeChi'][0]+ ">" + allDataDict['jeChi'][2]  , twoSideSpace + 318  , 348 , wordingSize = 41 , wordingFont = pf_TC_medium , color = mainColor )



	## 國曆
	makeText ( "國曆:                      " + allDataDict['week'] , twoSideSpace + 5 , 290 , wordingSize = 40 , wordingFont = pf_TC_medium , color = mainColor )  

	makeText (  "/".join(allDataDict['fullDate'].split("/")[:3]), twoSideSpace + 117 , 297 , wordingSize = 52 , wordingFont = myriad_reg , color = mainColor )  
	
	## 農曆
	makeText ( "農曆: "+allDataDict['fullDarkDate']  + jeChiBuf , twoSideSpace + 5 , 348 , wordingSize = 40 , wordingFont = pf_TC_medium , color = mainColor )  



	## 直槓
	draw_InfoLine (  center = 627 , hight = 298   , size = 101 , lineColor = titleGray , lineWidth= 4 )

	## 時間
	if ( allDataDict['user_define'] == True )  or ( allDataDict['hourGanZi'] == "X" ):
		makeText ("00:00" , twoSideSpace + 583 , 293 , wordingSize = 128 , wordingFont = myriad_reg , color = titleGray ) 
	else:
		makeText ( allDataDict['time'] , twoSideSpace + 583 , 293 , wordingSize = 128 , wordingFont = myriad_reg , color = timeColor ) 

	## 卦名
	makeText ( allDataDict['mainGuaName'] , screenWidth *0.5  - len(allDataDict['mainGuaName'])*0.5 * 74 -10 , 438 , wordingSize = 74 , wordingFont = pf_TC_regular , color = mainColor )  



	makeText ( allDataDict['home_kongWang'] ,855 , 438-2 , wordingSize = 40 , wordingFont = pf_TC_medium , color = mainColor )  
	makeText ( "空亡" ,855 , 485-2 , wordingSize = 40 , wordingFont = pf_TC_medium , color = mainColor ) 

	# 自由橫線
	def draw_free_line ( x,y  , size = 50 , color = lineColor , LineWidth = 2 ):
		draw.line((  x , y , x+size , y ), fill= color, width = LineWidth )

	draw_free_line ( 855 , 489-2  , size = 80 , color = subGray , LineWidth = 2 )

	## ball text 圓圈字
	## text_x_adj 微調文字x方向
	def makeBallText( text = "" , x = 270 , y  = 1189 , wordingSize = 36 ,  wordingColor = subGray , bt_font = pf_TC_medium , LineWidth = 2  ): 
		makePoint ( x = x-wordingSize*0.12 , y = y+wordingSize*0.1 , radious = wordingSize*1.25 , pointColor = None  ,LineWidth = LineWidth , lineColor = wordingColor )
		makeText (  text , x , y , wordingSize = wordingSize  , wordingFont = bt_font  ,color = wordingColor )



	## 下方小直槓
	draw_InfoLine (  center = twoSideSpace +95 , hight = screenHight - 250   , size = 56 , lineColor = midGray )      ## 左邊
	draw_InfoLine (  center = screenWidth*0.5 , hight = screenHight - 250   , size = 56 , lineColor = midGray )   ## 中間
	draw_InfoLine (  center = screenWidth*0.5 +85 , hight = screenHight - 250   , size = 56 , lineColor = midGray )   ## 中右





	## 本爻
	homeGuaSpace = 0
	## 本卦五行屬性
	makeText ( allDataDict['home_rowHead']  , twoSideSpace + 32 , screenHight-256 , wordingSize = 45 , wordingFont = pf_TC_medium , color = subGray ) 
	if allDataDict['home_mode'] == "六沖":
		homeGuaSpace += 14
		makeBallText( text = "沖" , x = screenWidth*0.5 + 25 -100 , y  = screenHight-255 , wordingSize = 45 ,  wordingColor = siIn_color , bt_font = pf_TC_bold , LineWidth = 4  )
	if allDataDict['home_mode'] == "六合":
		makeBallText( text = "合" , x = screenWidth*0.5 + 25 -100 , y  = screenHight-255 , wordingSize = 45 ,  wordingColor = siIn_color , bt_font = pf_TC_bold , LineWidth = 4  )
		homeGuaSpace += 14
	if len(allDataDict['home_title'] ) == 4:
		homeGuaSpace += 8

	## 卦名
	makeText ( allDataDict['home_title']  , twoSideSpace+37+140 - homeGuaSpace , screenHight-256 , wordingSize = 45 , wordingFont = pf_TC_medium , color = subGray ) 

	changeGuaSpace = 0
	if allDataDict['change_number'] == None:	
		makeText ( "—  —  — " , screenWidth*0.5 + 25 +125  , screenHight-256 , wordingSize = 45 , wordingFont = pf_TC_medium , color = subGray ) 
		makeText ( "×"  , screenWidth*0.5 + 25 , screenHight-256-12 , wordingSize = 56 , wordingFont = pf_TC_medium , color = subGray ) 		
	else:
		## 變卦五行屬性
		makeText ( allDataDict['change_rowHead']  , screenWidth*0.5 + 21 , screenHight-256 , wordingSize = 45 , wordingFont = pf_TC_medium , color = subGray ) 
		## 卦名

		## 變爻
		if allDataDict['change_mode'] == "六沖":
			makeBallText( text = "沖" , x = screenWidth*0.5 + 25 +343 , y  = screenHight-255 , wordingSize = 45 ,  wordingColor = siIn_color , bt_font = pf_TC_bold , LineWidth = 4  )
			changeGuaSpace += 10
		if allDataDict['change_mode'] == "六合":
			makeBallText( text = "合" , x = screenWidth*0.5 + 25 +343 , y  = screenHight-255 , wordingSize = 45 ,  wordingColor = siIn_color , bt_font = pf_TC_bold , LineWidth = 4  )
			changeGuaSpace += 10
		if len(allDataDict['change_title'] ) == 4:
			changeGuaSpace += 20	
	
		makeText ( allDataDict['change_title']  ,  screenWidth*0.5 + 25 + 150 - changeGuaSpace , screenHight-256 , wordingSize = 45 , wordingFont = pf_TC_medium , color = subGray ) 




	## makePoint,circle
	def makePoint ( x , y , radious = 8 , pointColor = None , lineColor = None , LineWidth = 0 , switch = True ):
		if switch == True:
			draw.ellipse(    (  ( x,y ) , ( x+radious , y+radious )  ) , fill = pointColor , outline = lineColor , width = LineWidth ) 

	# makePoint ( screenWidth*0.5 , 1532+45 , radious = 12 , pointColor = lightGray  , switch = True )







	# def draw_SquareMark ( x = 100  , y = 200  , squareSize = 50   , outlineColor = subGray , lineWidth = 2 ):

	def makeSquareText( text = "" , x = 270 , y  = 1189 , wordingSize = 36 ,wordingY_adj = 0 ,   wordingColor = "#ffffff" , squareColor = siIn_color, bt_font = pf_TC_bold   ): 
		squareOutSize = 2
		draw.rectangle(( x - squareOutSize , y + wordingSize * 0.2 - squareOutSize , x + wordingSize + squareOutSize , y + squareOutSize + wordingSize + wordingSize*0.2 ), fill= squareColor , outline= None ,  width = None )

		makeText (  text , x , y-1 + wordingY_adj , wordingSize = wordingSize  , wordingFont = bt_font  ,color = wordingColor )
























	wordSpace = 180
	startPo = twoSideSpace

	titleList = [
		# (allDataDict['home_guaBody'], "身"),
		(allDataDict['horse_po'],     "馬"),
		(allDataDict['flower_po'],    "桃"),
		(allDataDict['yangKnife_po'], "刃"),
		(allDataDict['godHappy_po'],  "喜"),
		(allDataDict['guan_po'],      "祿"),
		(allDataDict['helpful_po'],   "貴"),
	]
	count = 1
	for godItem, title in titleList:
		if godItem == "X":
			continue

		if  godItem == None:
			godItem = "X"



		if count == 5 and title == "祿":
			continue


		# print( "@@@@@@@----------" ,count ,godItem, title )
		makeText ( title +"-"+ godItem , startPo , screenHight-110 , wordingSize = 46 , wordingFont = pf_TC_medium , color = subGray )
		if count < 5:
			## 分隔小直槓
			draw_InfoLine (  center = startPo + 150 , hight = screenHight-102   , size = 48  , lineColor = midGray ,lineWidth = 2 ) 

		if count == 5:
			break
		count += 1
		startPo += wordSpace


	sixFamily_dict = {
		"兄弟": "兄",
		"妻財": "財",
		"父母": "父",
		"子孫": "孫",
		"官鬼": "官"
	}


	insideSpace = -140 # 上下行距
	startLineHight =  mainSquareHight + 870   # 起始基礎高度(最低)
	hightBuf = -14

	yaoFont = pf_TC_bold


	##  從最下面開始
	for row_id in  range(6):
		adj_hight = startLineHight + hightBuf

		if row_id != 0:
			## 大橫線
			# draw_H_line ( hight = adj_hight  , sideSpace = twoSideSpace+25 , color = subGray )
			draw_H_line ( hight = adj_hight  , sideSpace = twoSideSpace + 35 , color = lineColor , LineWidth = 1 )
		fixTextHight = insideSpace*0.5 -43

		if noteSwitch == True:
			## 三合局小方框
			if allDataDict['homeThreeHoId'][row_id][0] in ("O"):	
				homeThreeHoColor = getTypeColorC( allDataDict['homeThreeHoId'][row_id] )
				draw_SquareMark( x = screenWidth - 374 , y = adj_hight + fixTextHight +10    , squareSize = 68  , outlineColor = homeThreeHoColor  )

			if allDataDict['homeThreeHoId'][row_id][0] in ("P"):	
				homeThreeHoColor = getTypeColorC( allDataDict['homeThreeHoId'][row_id] )
				draw_SquareCut(  x = screenWidth - 374+1 , y = adj_hight + fixTextHight +10    , squareSize = 68  , cut = 15, outlineColor = homeThreeHoColor, fillColor = None )


		## 納甲
		makeText ( allDataDict['home_naGia'][row_id][-1]     , screenWidth - 370 , adj_hight + fixTextHight , wordingSize = 62 , wordingFont = yaoFont , color = mainColor ) 
		if noteSwitch == True:
			## 分數小字
			makeText ( allDataDict['home_naGia_rank'][row_id]  , screenWidth - 305 , adj_hight + fixTextHight - 5  , wordingSize = 32 , wordingFont = SourceSans3 , color = '#777777' ) 
			# makeText ( "–"  , screenWidth - 305 , adj_hight + fixTextHight -1  , wordingSize = 20 , wordingFont = pf_TC_bold , color = subGray ) 	
			# makeText ( "▽"  , screenWidth - 307 , adj_hight + fixTextHight + 2  , wordingSize = 20 , wordingFont = pf_TC_bold , color = subGray ) 		
#△▽ ▲▼
			## 日月底線
			if allDataDict['home_naGia'][row_id][-1] in allDataDict['dayGanZi']  or allDataDict['home_naGia'][row_id][-1] in allDataDict['monthGanZi'] : ## 如果納甲地支和日月支相同，則為日辰入卦, 底線效果

				draw.line((  screenWidth - 367 , adj_hight + fixTextHight+85 , screenWidth - 374 +63 , adj_hight + fixTextHight +85), fill= midGray , width = 5 )


		## 六獸
		makeText ( allDataDict['home_sixAnimal'][row_id][-1] , twoSideSpace + 214 , adj_hight + fixTextHight , wordingSize = 62 , wordingFont = yaoFont , color = "#666666" )  

		## 小直線
		draw_InfoLine (  center =  twoSideSpace + 214+70 , hight = adj_hight + fixTextHight +11  , size = 64 , lineColor = midGray ,lineWidth  = 4 )      ## 下方本卦變卦中的小直槓

		## 六親
		makeText ( sixFamily_dict[ allDataDict['home_family'][row_id] ]   , twoSideSpace + 214+80 , adj_hight + fixTextHight , wordingSize = 62 , wordingFont = yaoFont , color = mainColor )  


		## 應爻
		if allDataDict['home_innYao'] == str(row_id+1) :
			makeSquareText( text = "應" , x = screenWidth*0.5 + 52 , y  = adj_hight + fixTextHight + 8 , wordingSize = 52 ,  wordingColor = "#ffffff" , squareColor = siIn_color, bt_font = pf_TC_regular   )
		## 世爻
		if allDataDict['home_shiYao'] == str(row_id+1) :
			makeSquareText( text = "世" , x = screenWidth*0.5 + 52 , y  = adj_hight + fixTextHight + 8 , wordingSize = 52 ,  wordingColor = "#ffffff" , squareColor = siIn_color, bt_font = pf_TC_regular   )


		if allDataDict['home_naGia'][row_id][-1]  in allDataDict['home_kongWang']:
			## 空亡的圈
			makePoint ( x = screenWidth*0.5 +113 , y = adj_hight + fixTextHight + 53  , radious = 22 ,pointColor = None , lineColor = subGray , LineWidth = 3 , switch = True )


		# ## 三合局小方框
		# if allDataDict['homeThreeHoId'][row_id][0] in ("O"):	
		# 	homeThreeHoColor = getTypeColorC( allDataDict['homeThreeHoId'][row_id] )
		# 	draw_SquareMark( x = home_naGia_adj + 669 , y = adj_hight -2    , squareSize = 60  , outlineColor = homeThreeHoColor  )





		## 伏神
		if allDataDict['hide_naGia'][row_id]!="X":
		# 	## 伏神納甲		
			makeText ( allDataDict['hide_naGia'][row_id][-1] , twoSideSpace + 35 , adj_hight + fixTextHight , wordingSize = 62 , wordingFont = yaoFont , color = mainColor ) 

			if noteSwitch == True:
				## 分數小字
				makeText ( allDataDict['hide_naGia_rank'][row_id]  , twoSideSpace + 156 , adj_hight + fixTextHight - 5  , wordingSize = 32 , wordingFont = SourceSans3 , color = '#777777' ) 



			# ## 伏神六親
			makeText ( sixFamily_dict[ allDataDict['hide_family'][row_id] ] , twoSideSpace + 98 , adj_hight + fixTextHight , wordingSize = 62 , wordingFont = yaoFont , color = mainColor ) 			

		if allDataDict['hide_naGia'][row_id][-1]  in allDataDict['home_kongWang']:
			## 空亡的圈
			makePoint ( x = twoSideSpace +14, y = adj_hight + fixTextHight + 53  , radious = 22 ,pointColor = None , lineColor = subGray , LineWidth = 3 , switch = True )





		## 變卦
		if allDataDict['changeIdIndex'][row_id] == "O":
			if noteSwitch == True:
				## 三合局小方框
				if allDataDict['changeThreeHoId'][row_id][0]  in ( "O", "P", "H" ):		
					changeThreeHoColor = getTypeColorC( allDataDict['changeThreeHoId'][row_id] )
					draw_SquareMark( x =  screenWidth -240 -5 , y = adj_hight + fixTextHight +10    , squareSize = 68  , outlineColor = changeThreeHoColor  )
				# draw_SquareMark( x =  screenWidth -238 , y = adj_hight + fixTextHight +11    , squareSize = 64  , outlineColor = subGray  )

				## 分數小字
				makeText ( allDataDict["change_naGia_rank"][row_id] , screenWidth -117 -5 , adj_hight + fixTextHight - 5  , wordingSize = 32 , wordingFont = SourceSans3 , color = '#777777' ) 

				## 化進小點點
				if allDataDict['home_forwardBack'][row_id]  == "FW":
					makeText ( "•"  , screenWidth -211 -6 , adj_hight + fixTextHight -22+4 , wordingSize = 28 , wordingFont = yaoFont , color = midGray ) 

				## 化退小點點
				elif allDataDict['home_forwardBack'][row_id] =="BK":
					makeText ( "•"  , screenWidth -211 -6 , adj_hight + fixTextHight +64+4 , wordingSize = 28 , wordingFont = yaoFont , color = midGray ) 

			## 變卦納甲
			makeText ( allDataDict['change_naGia'][row_id][-1]  , screenWidth -236 -5 , adj_hight + fixTextHight , wordingSize = 62 , wordingFont = yaoFont , color = mainColor ) 



			## 變卦六親
			makeText ( sixFamily_dict[ allDataDict['change_family'][row_id] ]  , screenWidth -174 -5 , adj_hight + fixTextHight , wordingSize = 62 , wordingFont = yaoFont , color = mainColor ) 

			if allDataDict['hide_naGia'][row_id][-1]  in allDataDict['home_kongWang']:
				## 空亡的圈
				makePoint ( x = screenWidth -265 -5 , y = adj_hight + fixTextHight + 53  , radious = 22 ,pointColor = None , lineColor = subGray , LineWidth = 3 , switch = True )
			

		centerAdj = -8
		
		lineWidth = 6
		fixHight = insideSpace*0.5

		if allDataDict['inputGuaList'][ row_id ] == "0":
			# 少陰
			def draw_litYoLine ( hight = adj_hight + fixHight  , center = centerAdj  ):
				lineLength = 70
				halfLength = lineLength*0.5

				draw.line((  screenWidth*0.5 - halfLength + center, hight , screenWidth*0.5-5 + center , hight   ), fill= sixYoSymbol , width= lineWidth )

				draw.line((  screenWidth*0.5 +5 + center      , hight , screenWidth* 0.5  + halfLength+center , hight   ), fill= sixYoSymbol , width= lineWidth )
			draw_litYoLine()


		if allDataDict['inputGuaList'][ row_id ] == "1":
				# 爻 少陽
			def draw_litYoLine ( hight = adj_hight + fixHight  , center = centerAdj ):
				lineLength = 70
				halfLength = lineLength*0.5
				draw.line((  screenWidth*0.5-halfLength+center, hight  , screenWidth*0.5+halfLength+center , hight   ), fill= sixYoSymbol , width= lineWidth )
			draw_litYoLine()

		if allDataDict['inputGuaList'][ row_id ] == "X":
			# 爻 老陰
			def draw_litDarkLine ( hight = adj_hight + fixHight , left = 70 , right = 70 , center = centerAdj ):
				lineLength = 45
				halfLength = lineLength*0.5
				draw.line((  screenWidth*0.5 -halfLength + center, hight-halfLength  , screenWidth*0.5 +halfLength + center, hight+halfLength ), fill= sixYoSymbol, width= lineWidth+1 )
				draw.line((  screenWidth*0.5 -halfLength + center, hight+halfLength  , screenWidth*0.5 +halfLength + center, hight-halfLength ), fill= sixYoSymbol, width= lineWidth+1 )		
			draw_litDarkLine()

		if allDataDict['inputGuaList'][ row_id ] == "@":
			# 老陽
			def draw_oldYoLine ( hight = adj_hight + fixHight  , left = 80 , right = 80 , circleRadius = 25 , center = centerAdj  ):
				draw.ellipse((  screenWidth*0.5 - circleRadius  + center, hight+1 - circleRadius , screenWidth*0.5 + circleRadius  + center , hight+1 + circleRadius ), outline= sixYoSymbol, width= lineWidth )
			draw_oldYoLine()

		hightBuf += insideSpace















# # ⤫ ⤬╳↗ ↘╹ ╻▖▝✲⨯⦻⮾↑🡥🡦✖
# # ☹✳❄ꚰ⛶⁝⋮⊗☒☐．•‧˙﹒¯ˉ＊⊠ˍ‐‒⎺☰☱☲☳☴☵☶☷⛒⊗•¦|↹⇆

	if savePic == True:
		if allDataDict['note'] != "XXX":
			fileName = allDataDict['note'].replace("?","").replace("\\","").replace("/","").replace(":","").replace("*","").replace("<","").replace(">","").replace("|","") + ".jpg"
		else:
			fileName = allDataDict['fullDate'].replace("/","-").replace(":","-") + allDataDict['mainGuaName'] + ".jpg"
		img.save( fileName )
		print( "fileName >" , fileName)


	if show == True:
		img.show()
		print("SHOW")

	else:
		from cloudinary_helper import upload_image, delete_older_than

		## Notion模式
		if notion == True:
			## 存到"__image_hosting"檔案夾中
			res = upload_image( img , "__image_hosting" ) 
			high_res = res["url"]
			print( "上傳一張圖片至圖床")
			return high_res

		else:
			# preview_img = img.resize( (  int(screenWidth*0.4) , int(screenHight*0.4)  )   ,Image.BILINEAR  ) ## line縮圖預覽用圖
			# # 上傳圖片
			res = upload_image( img )
			high_res = res["url"]
			# print("連結：", res["url"])

			# res = upload_image( preview_img )
			# low_res = res["url"]
			# print("連結：", res["url"])
			return [ high_res , high_res ]



# upload_image( r"D:\Dropbox\Python\linebot\六爻\work\834185e004190e75a5bfdb32019e51fb.jpg", folder="__image_hosting")

		# preview_img.show()

# ㊊㊋㊌㊍㊎㊏㊐



if __name__ == '__main__':

	from mainFun import  *

	# drawUi_v2( mainFunction( "@111X0"  , noteText =  "病" ) , fontStyle = "Fb", "tipsMode" = "ON", uiStyle = "CB"  , show = True  )



	# drawUi_v1( mainFunction( "@10010" ,noteText = "男問今年工作運勢", userDefineDate = "") , show = True ,)
	# drawUi_v1( mainFunction( "01X@@@" ,noteText = "男問今年工作運勢", userDefineDate = "") , show = True ,)
	# drawUi_v1( mainFunction( "01X$01" ,noteText = "男問今年工作運勢",user_mouthZi = "巳月" , user_dayGanZi = "己丑", userDefineDate = "") , show = True ,)	 ## 三合
	# drawUi_v1( mainFunction( "0X01X0" , noteText = "男問今年工作運勢" ) )
	drawUi_v1( mainFunction( "$111$0" ,noteText = "測測男問今年工作運勢,測測男問今年工", userDefineDate = "") , show = True ,) ## 5字

	# drawUi_v1( mainFunction( "10010$" ,noteText = "男問今年工作運勢", userDefineDate = "") , show = True ,)
	# drawUi_v1( mainFunction( "111@0X" ,noteText = "男問今年工作運勢", userDefineDate = "") , show = True ,) #6字


	# for e in loopMaker( "01@X" , 6 ):

	# 	print("\n\n>>>>> ", e )
	# 	drawUi_v2( mainFunction(  e ) )




# 〇〇⌤↖ ↘ ⤒ ⤓✲⎈⌫ ⟵
# ⌦ ⎀ , ⇤ ⇥ ⤒ ⤓ , ⇞ ⇟ ⎗ ⎘
# ← → ↑ ↓, ◀ ▶ ▲ ▼,




