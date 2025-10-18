# -*- coding: utf-8 -*-


allDataDict = {'inputGua': ['1', '0', '1', '1', '1', '@'], 'yearGanZi': '甲辰', 'monthGanZi': '甲戌', 'dayGanZi': '甲子', 'hourGanZi': '丙寅', 'jeChi': '霜降>>立冬', 'week': '(日)', 'time': '04:42', 'flower_po': '酉', 'horse_po': '寅', 'guan_po': '寅', 'helpful_po': '丑未', 'yangKnife_po': '卯', 'changeIdIndex': ['X', 'X', 'X', 'X', 'X', 'O'], 'inputGuaList': ['1', '0', '1', '1', '1', '@'], 'mainGuaName': '同人之革卦', 'vs_type': '火>>水', 'home_number': '13', 'home_up': '天火', 'home_dn': '同人', 'home_title': '天火同人', 'home_upGua': '乾', 'home_dnGua': '離', 'home_inOutGua': '乾離', 'home_rowType': '火', 'home_shiYao': '3', 'home_innYao': '6', 'home_guaBody': '寅', 'home_naGia': ['卯', '丑', '亥', '午', '申', '戌'], 'home_kongWang': ['X', 'X', 'O', 'X', 'X', 'O'], 'home_naGiaType': ['木', '土', '水', '火', '金', '土'], 'home_family': ['父母', '子孫', '官鬼', '兄弟', '妻財', '子孫'], 'home_sixAnimal': ['青龍', '朱雀', '勾陳', '螣蛇', '白虎', '玄武'], 'home_lostFamily': [], 'hide_family': ['X', 'X', 'X', 'X', 'X', 'X'], 'hide_naGia': ['X', 'X', 'X', 'X', 'X', 'X'], 'change_number': '49', 'change_up': '澤火', 'change_dn': '革', 'change_title': '澤火革', 'change_upGua': '兌', 'change_dnGua': '離', 'change_inOutGua': '兌離', 'change_rowType': '水', 'change_shiYao': '4', 'change_innYao': '1', 'change_guaBody': '卯', 'change_naGia': ['卯', '丑', '亥', '亥', '酉', '未'], 'change_kongWang': ['X', 'X', 'O', 'O', 'X', 'X'], 'change_naGiaType': ['木', '土', '水', '水', '金', '土'], 'change_family': ['子孫', '官鬼', '兄弟', '兄弟', '父母', '官鬼'], 'change_sixAnimal': ['青龍', '朱雀', '勾陳', '螣蛇', '白虎', '玄武']}

	## MAIN
	############################################################################################################	
# def lineNotifyImg( fullPath ):
# 	import time,os,sys
# 	import requests
# 	# from PIL import Image
# 	# import PIL.ImageGrab
# 	# import tempfile
# 	# opts, args = getopt.getopt(sys.argv[1:], "hsi:m:", ["help","shutdown","image=","message="])
# 	print(  sys.argv[0])

# 	token = "uFlyMzEHke5E3dZOf6W9s1X9hijHmGmm319sddL6LBj" # 阿貓
# 	# token = "OQUgT1QbPYkCo8pEhLoatan9tdUdSmXspwva2ZSkw4e" # 小花
# 	url = "https://notify-api.line.me/api/notify"
# 	headers = {"Authorization": "Bearer " + token}

# 	# payload = {'message': fullPath }

# 	payload = {'message': ".."}
# 	jpgFile = open( fullPath , 'rb')
# 	files = {'imageFile': jpgFile}
# 	resp=requests.post(url, headers=headers, data=payload , files = files)

# 	# resp=requests.post(url, headers=headers, data=payload )
# 	# try:
# 	# 	resp=requests.post(url, headers=headers, data=payload )
# 	# except:
# 	# 	print( "notify error")






# def uploadImgur( imagePath ):
# 	# from  PIL  import  Image
# 	import  PIL.ImageGrab
# 	from  imgurpython  import  ImgurClient
# 	import  datetime ,os

# 	imagePath = imagePath.strip()
# 	filename = imagePath.split("\\")[-1].split(".")[0].replace("__ttmp" , "")

# 	# If you already have an access/refresh pair in hand
# 	# bennoworksohard
# 	album = 'FhfzevH'
# 	client_id= '53177fc1be648f6'
# 	client_secret= 'cb996df2cf01b82305aceb9e5c9d258a46a7b084'
# 	access_token = '44428b7d1cc740be9b475a0cb866a99e3fe44045'
# 	refresh_token = '7e5df6de118669ead4a29cc5e51b4e6a6e123b54'

# 	# okitsmelah
# 	# album = 'QJ9O30v'
# 	# client_id = '206006b59b5e288'
# 	# client_secret = '5462ad1712851c001d7e17d5698be23ff662a273'
# 	# access_token = 'de8be15be384009bad899cbbac766deb28c5120e'
# 	# refresh_token = 'ed4e4763250f8d12ecfcfb7d88015d85ecfa4a66'

# 	# Note since access tokens expire after an hour, only the refresh token is required (library handles autorefresh)
# 	try:
# 		client = ImgurClient(client_id, client_secret, access_token, refresh_token)
# 	except Exception as e:
# 		print( "Imgur Clint error - ",e )

# 	config = {
# 		'album': album,
# 		'name':  filename,
# 		'title': 'render',
# 		'description': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# 	}

# 	# imagePath = imagePath.encode('utf-8') # encode to utf-8 format
# 	# print ( imagePath )

# 	try:
# 		image = client.upload_from_path( imagePath, config = config, anon = False )

# 	except:
# 		image = client.upload_from_path( imagePath,  anon = False )
# 		lineNotify( msg = "備用\n" + image ['link'] )

# 	finally:
# 		if  "image" in locals().keys():
# 			# print ( image )
# 			print (image ['link'])
# 			return (image ['link'])
# 		else:
# 			return( None )





def get_cutoff_index(text, target_weight=16):
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










# # 將 PIL 圖片轉換為字節流
# def image_to_byte_array(image):
# 	from io import BytesIO
# 	img_byte_arr = BytesIO()  # 創建字節流對象
# 	image.save(img_byte_arr, format='PNG')  # 保存圖片為 PNG 格式
# 	img_byte_arr.seek(0)  # 重置字節流的指針
# 	return img_byte_arr




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

def getTypeColor( inputItem ):

	colorType = inputItem[1]    ## Pc 的 c
	threeHoType = inputItem[0]  ## Pc 的 P

	threeHo_colorA = "#a3c4b4"
	threeHo_colorB = "#d39f9f"
	threeHo_colorC = "#bfbfbf"
	threeHo_colorD = "#8caec4"

	lite_colorA = "#d3e2da"
	lite_colorB = "#d8c0c0"
	lite_colorC = "#d3d3d3"
	lite_colorD = "#ccd9e2"


	if threeHoType in ("O"):
		if inputItem[1] == "a":
			return threeHo_colorA
		if inputItem[1] == "b":
			return threeHo_colorB		
		if inputItem[1] == "c":
			return threeHo_colorC
		if inputItem[1] == "d":
			return threeHo_colorD
	else:
		if inputItem[1] == "a":
			return lite_colorA
		if inputItem[1] == "b":
			return lite_colorB		
		if inputItem[1] == "c":
			return lite_colorC
		if inputItem[1] == "d":
			return lite_colorD		







										  # "uiStyle" = "CB", "fontStyle" = "Fb","tipsMode" = "ON"

def drawUi_v2( allDataDict = allDataDict , fontStyle = "Fb", tipsMode = "ON", uiStyle = "CA" ,  show = True , savePic = False , notion = False ):



# def drawUi_v2( allDataDict = allDataDict , uiFont = "B", uiDataMode = "full", uiColor = "colorA" ,  show = False , savePic = False ):

	from PIL import Image,ImageFont,ImageDraw,ImageFilter,ImageChops 

	# note = "台北林小姐"

	screenWidth = 1070 # 1080
	screenHight = 1420

# 1070/1545
	# https://www.behance.net/gallery/58084819/24-china-24-solar-terms
	# https://www.geeksforgeeks.org/python-pil-imagedraw-draw-text/

	# 创建一张底图,用来绘制
	bgColor = (255,255,255)
# Image.open('paper02.jpg')
	# img = Image.open('papper_bg_02.jpg').convert("RGB")
	img = Image.open('papper_bg_02.jpg').convert("RGB")

	# img = Image.new("RGB", (screenWidth, screenHight), bgColor )
	# img = Image.new("RGBA", (screenWidth, screenHight), (0, 0, 0, 0))  # 全透明背景
	userDefineHight = 0

################################################################
################################################################


	# # GenJyuuRegular = "font/GenJyuuGothic-Monospace-Regular.ttf"
	# # GenJyuuMedium = "font/GenJyuuGothic-Monospace-Medium.ttf"	
	# GenJyuuBold = "font/GenJyuuGothic-Monospace-Bold.ttf"

	GenJyuuOrgMedium = "font_v02/GenJyuuGothic-Medium.ttf"	## 中圓
	GenJyuuOrgNormal = "font_v02/GenJyuuGothic-Normal.ttf"		

	GenJyuuOrgBold = "font_v02/GenJyuuGothic-Bold.ttf"	## bold 粗圓


	# GenShinMedium = "font/nouse/GenShinGothic-Monospace-Medium.ttf"	## Mid黑體
	# GenShinReg = "font/nouse/GenShinGothic-Monospace-Regular.ttf"	## reg黑體
	GenShinBold = "font_v02/GenShinGothic-Monospace-Bold.ttf"     ## bold黑體




	# guaFont = "font/nouse/seguisym.ttf"     ## 64卦字型


	# textOtherFont = "font/儷中宋.TTC"
	# textSubFont = "font/儷粗宋.TTC"

	# textRegularFont = "./font/SourceHanSerif-Bold.ttc" ## 粗明體
	# textSubFont =    "./font/SourceHanSerif-Bold.ttc" ## 粗明體


	# liHeyFont = "font/華康儷粗黑.TTC"
	# msjheyFont = "font/msjhbd.ttc" ## 微軟正黑體
	# mainFontA = GenShinBold

	dateNumberFont_A = "./font_v02/iskpota.ttf" ## 阿拉伯數字

	dateNumberFont_B = "./font_v02/gadugi.ttf" ## 阿拉伯數字B


 
	SourceHanSerif =    "./font_v02/SourceHanSerif-Bold.ttc" ## 粗明體
	SourceSans3 =    "./font_v02/SourceSans3-Medium.ttf" ## 分數小字



	# fontStyle = "Fb      ## 字型模式設定
	# fontsizeFix = 0     ## 字體大小

	poFix_y = 0         ## 字的高低調整
	wordingSize = 56    ## 字體大小
	wordingScale = 1        ## 字體大小比例
	subWordingSize = 54 # 爻內文字
	rankSize = 29

	titleY = 0
	titleOrgY = 0
	dateTextSize = 78   ## 左上方日期字的大小
	dateY_adj = 6       ## 左上方日期字的高度

	chineseDateY = 110 ## 中文干支高度
	fixWordingY = 0     ## 月柱和日柱字的高低修正( 乙和己太高 )
	

	if tipsMode.lower() == "on":
	# if uiDataMode.lower() == "full":
		noteSwitch = True  ## 專家模式不開啟提示
	else:
		noteSwitch = False

	if fontStyle.lower() == "fa":
	# if uiFont == "A": ## 明體
		textRegularFont = SourceHanSerif

		textSubFont =  SourceHanSerif
		month_day_pillar_font = SourceHanSerif
		chineseDateY = 107 ## 中文干支高度
		fixWordingY = 2


	elif fontStyle.lower() == "fb":
	# elif uiFont == "B": ## 圓體
		textRegularFont = GenJyuuOrgMedium
		textSubFont =  GenJyuuOrgBold  ## 月 日
		month_day_pillar_font = GenJyuuOrgMedium
		dateNumberFont_A=  dateNumberFont_B
		wordingScale = 1.01		
		poFix_y = 0.04
		subWordingSize = 57 # 字的大小53
		titleY = 2
		dateTextSize = 70
		dateY_adj = -2
		chineseDateY = 113 ## 中文干支高度
		fixWordingY = 2





	draw = ImageDraw.Draw(img)
	# mainColor = (25,40,71)
	darkBlue = ( 23,80,107 )
	mainColor = ( 32,75,127 )
	# ( 46,100,137)
	skyBlue = ( 39,105,192 )
	purpleGray = ( 136,131,155 )
	outGray=( 113,120,144 )

	mainYellow = (252,163,45)


	mainLitGray = ( 133,158,157 )


	iconLitGray = ( 185,198,198 )	
	mainVeryLitGray = ( 225,225,225 )
	mainWhiteGray = ( 215,215,215 )	
	mainMidGray = ( 130,130,130 )	

	darkGray = ( 110,110,110 )
	darkDarkGray = ( 85,85,85 )	

	# titleGray = ( 120,120,130 )	


	mainBlack = (0,0,0)
	BG_lineWidth = 3



	skyBlue = "#015095" ## 淺藍色	

	oldBlue = (40,75,107) ## 綻藍色

	mainBlue = (31,59,106) ## 深藍色	

	subGray =  "#a4adc0" 	
	ignoreColor = "#8e98ac"
	# colorAdj_A = "#8e98ac" # 比subgray深一號
	# colorAdj_B = "#738093" # 比subgray深兩號
# "#aeb9cb"
	mainColor = mainBlue


# uiStyle 決定介面顏色與排版
# fontStyle 字型 宋體圓體黑體
# tipsMode  小抄提示功能

	# if uiStyle.lower() == "ca": ## color a
	# 	mainColor =
	# 	subColor = 

	# elif uiStyle.lower() == "cb": ## color b
	# 	mainColor =
	# 	subColor = 

	# elif uiStyle.lower() == "cc": ## color c
	# 	mainColor =
	# 	subColor = 
	# else:
	# 	mainColor = 
	# 	subColor = 		








	# mainDarkGray = ( 130,140,160 )		
	## 藍色外框
	def draw_SquareFull ( offset = 10  , width = screenWidth , hight = screenHight  , color = mainColor, outlineColor = mainColor , lineWidth = 7 ):
		# draw.rectangle(( offset   ,   offset    ,  width-offset,  hight-offset ), fill= None , outline= outlineColor ,  width = lineWidth )

		lineOffset = 16
		cubeSize = 8

		draw.rectangle(( offset  ,offset , width-offset , hight-offset  ), fill= None , outline= color ,  width = lineWidth )


## 斷線小框
	def draw_SquareMark_lit ( x = 100  , y = 500  , squareSize = 60 , space = 30  , outlineColor = subGray , lineWidth = 2 , switch = noteSwitch ):
		if switch == True:

			# points = [(50, 50), (150, 50), (150, 150)]
			# space = 30
			sq_x = lineWidth*0.5
			l_Uppp =  ( x+sq_x +sq_x, y +sq_x)
			l_Down =  ( x+sq_x +sq_x, y+sq_x + squareSize)
			r_Uppp =  ( x-sq_x + squareSize , y )
			r_Down =  ( x-sq_x + squareSize , y + squareSize )

			points_L_up = [( l_Uppp[0] , l_Uppp[1]+squareSize*0.5-space*0.5 + sq_x ), l_Uppp , (  l_Uppp[0]+ squareSize*0.5-space*0.5 , l_Uppp[1])]

			points_L_dn = [(  l_Down[0]+ squareSize*0.5-space*0.5 , l_Down[1]), l_Down , ( l_Down[0] , l_Down[1]-squareSize*0.5+space*0.5 -sq_x) ]

			points_R_up = [( r_Uppp[0] - squareSize*0.5+space*0.5, r_Uppp[1] ), r_Uppp , (  r_Uppp[0] , r_Uppp[1]+ squareSize*0.5-space*0.5 + sq_x)]

			points_R_dn = [(  r_Down[0] , r_Down[1]- squareSize*0.5+space*0.5-sq_x), r_Down , ( r_Down[0] - squareSize*0.5+space*0.5 , r_Down[1] ) ]


			# draw.rectangle(( x , y , x + squareSize , y + squareSize ), fill= None , outline= outlineColor ,  width = lineWidth )
			# 加上 joint 設定
			draw.line(points_L_up, fill= outlineColor , width= 2, joint="bevel join")   # "curve" 會讓轉角變圓"curve"圓角連接（round join）尖角連接（miter join）斜切連接（bevel join）
			draw.line(points_L_dn, fill= outlineColor , width= 2, joint="bevel join") 
			draw.line(points_R_up, fill= outlineColor , width= 2, joint="bevel join") 
			draw.line(points_R_dn, fill= outlineColor , width= 2, joint="bevel join") 

	## 畫缺角方形
	def draw_SquareCut(  x = 100, y = 500, squareSize = 60, cut = 10, outlineColor = "black", fillColor = None, lineWidth = 2 ):
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

	# draw_SquareMark_lit()





	## 字小框
	def draw_SquareMark ( x = 100  , y = 200  , squareSize = 50   , outlineColor = subGray , lineWidth = 2 ):
		draw.rectangle(( x , y , x + squareSize , y + squareSize ), fill= None , outline= outlineColor ,  width = lineWidth )

	
# ==========================================================================================================
# ==========================================================================================================
# ==========================================================================================================


	# 分割橫線
	def draw_H_line ( hight = 427  , size = 1000 , color = mainColor , LineWidth = 1 ):
		draw.line(( screenWidth*0.5 - size*0.5 , hight ,screenWidth*0.5 + size*0.5 , hight ), fill= color, width = LineWidth )







	# 直槓 |||||||
	def draw_InfoLine ( center =0  , hight = 270   , size = wordingSize  , color = mainColor ,lineWidth= 5 ):
		draw.line(( center ,  hight+size+2 ,  center , hight ), fill= color , width= lineWidth )




	# 主要字型
	def makeMainDateText ( text , x , y, wordingSize = 50 , dateFont = textRegularFont , color = mainColor , fixY = poFix_y , lite = False , double = True ):
		other_style = ImageFont.truetype( dateFont , wordingSize*wordingScale, encoding="utf-8")
		# draw.text(( x+5 , y+5 - wordingSize*0.25 ), text , fill= (245,245,245) , font = other_style )
		
		draw.text(( x , y - wordingSize*0.25 + wordingSize * fixY ), text , fill= color , font = other_style )
		if lite == False:
			draw.text(( x , y - wordingSize*0.25 + wordingSize * fixY ), text , fill= color , font = other_style )	

		if double == True:
			draw.text(( x-1 , y - wordingSize*0.25  + wordingSize * fixY ), text , fill= color , font = other_style )
			# draw.text(( x-2 , y - wordingSize*0.25  + wordingSize * fixY ), text , fill= color , font = other_style )












	## makePoint,circle
	def makePoint ( x , y , radious , pointColor = None , lineColor = None , LineWidth = 0 , switch = True ):
		# print( LineWidth )
		# print(pointColor )

		if switch == True:
			draw.ellipse(    (  ( x,y ) , ( x+radious , y+radious )  ) , fill = pointColor , outline = lineColor , width = LineWidth ) 





	## ball text 圓圈字
	## text_x_adj 微調文字x方向
	def makeBallText( text_buf = "" , x_buf = 270 , text_x_adj = 0 , text_y_adj = 0, y_buf = 1189 , wordingSize_buf = 36 ,wordingColor_Buf = "#f9f9f9",  color_buf = subGray , font_buf = GenJyuuOrgMedium , LineWidth_buf = 0 , extra_size = 0 , lineColor_buf = None , invertMode = False , double = False ): ## GenJyuuOrgNormal
		# makePoint ( x = 260  , y = 1186 , radious = 40 ,pointColor = subGray , lineColor = subGray , LineWidth = 2 )
		if invertMode == False:
			makePoint ( x = x_buf-wordingSize_buf/18 - extra_size*0.5 , y = y_buf-wordingSize_buf/12-extra_size*0.5 , radious = wordingSize_buf*1.111+extra_size , pointColor = color_buf ,LineWidth = LineWidth_buf , lineColor = lineColor_buf )
			
			# if double == True:
			# 	makePoint ( x = x_buf-wordingSize_buf/18 - extra_size*0.5-4 , y = y_buf-wordingSize_buf/12-extra_size*0.5-4 , radious = wordingSize_buf*1.111+extra_size+8 , pointColor = color_buf ,LineWidth = 2 , lineColor = lineColor_buf )




			wordingColor =  wordingColor_Buf ## 字白色
		
		else:
			wordingColor = color_buf

		makeMainDateText (  text_buf , x_buf+text_x_adj , y_buf + text_y_adj, wordingSize = wordingSize_buf  , dateFont = font_buf ,color = wordingColor , fixY = 0 , lite = True , double = False  ) # GenJyuuOrgMedium




	## TITLE
	# wording = "隨之革卦"
	titleWording = allDataDict['mainGuaName']
	## 大標
	titleWordingSize = 57




	 ##   ##   #####   ##   ##  ######   ##   ##           #####      ##     ##  ##
	 ### ###  ##   ##  ###  ##  # ## #   ##   ##            ## ##    ####    ##  ##
	 #######  ##   ##  #### ##    ##     ##   ##            ##  ##  ##  ##   ##  ##
	 #######  ##   ##  ## ####    ##     #######            ##  ##  ##  ##    ####
	 ## # ##  ##   ##  ##  ###    ##     ##   ##            ##  ##  ######     ##
	 ##   ##  ##   ##  ##   ##    ##     ##   ##            ## ##   ##  ##     ##
	 ##   ##   #####   ##   ##   ####    ##   ##           #####    ##  ##    ####

	month_buf = allDataDict['monthGanZi'] ## 月
	# month_buf = "亥" ## 月
	dat_buf = allDataDict['dayGanZi']	  ## 日


	mainDate_offset = -8
	sdw_offset = 2
	sdw_color = ( 170,170,170 )
	date_pillarSize = 86





	makeMainDateText ( "月", 267 +8 + mainDate_offset , 287-1 , wordingSize = 42  , dateFont = textSubFont  , double = False )

	# 月
	if month_buf[0] in ["乙","己"]: ## 修正字型的高低
		makeMainDateText ( month_buf[0], 313 +8 + mainDate_offset , 241+ titleOrgY   + titleY + fixWordingY , wordingSize = date_pillarSize  , dateFont = month_day_pillar_font , double = False )
	else:
		makeMainDateText ( month_buf[0], 313 +8 + mainDate_offset , 241+ titleOrgY   + titleY, wordingSize = date_pillarSize  , dateFont = month_day_pillar_font , double = False )	


	if month_buf[1] in ["巳"]: ## 修正字型的高低
		makeMainDateText ( month_buf[1], 313 +8+ date_pillarSize + mainDate_offset , 241+ titleOrgY   + titleY +fixWordingY, wordingSize = date_pillarSize  , dateFont = month_day_pillar_font , double = False )
	else:
		makeMainDateText ( month_buf[1], 313 +8+ date_pillarSize + mainDate_offset , 241+ titleOrgY   + titleY , wordingSize = date_pillarSize  , dateFont = month_day_pillar_font , double = False )
	# makeMainDateText ( month_buf, 313 + mainDate_offset , 241  + titleY, wordingSize = 93  , dateFont = textRegularFont)


	# draw_InfoLine ( center =  screenWidth*0.5-5  , hight = 0   , size = 3000  , color = mainColor ,lineWidth= 1 )
	makePoint ( x = screenWidth*0.5-12 , y = 280-1+ titleOrgY , radious = 14 , pointColor = mainColor )  ## 中間大點點

	## 日
	makeMainDateText ( "日", 554+14 + mainDate_offset , 285-1+ titleOrgY  , wordingSize = 42  , dateFont = textSubFont  , double = False )



	if dat_buf[0] in ["乙","己"]: ## 修正字型的高低
		makeMainDateText ( dat_buf[0] , 596+14 + mainDate_offset , 241 + titleOrgY + titleY + fixWordingY , wordingSize = date_pillarSize  , dateFont = month_day_pillar_font   , double = False )
	else:
		makeMainDateText ( dat_buf[0] , 596+14 + mainDate_offset , 241 + titleOrgY + titleY, wordingSize = date_pillarSize  , dateFont = month_day_pillar_font   , double = False )		

	if dat_buf[1] in ["巳"]: ## 修正字型的高低
		makeMainDateText ( dat_buf[1] , 596+14+ date_pillarSize + mainDate_offset , 241 + titleOrgY + titleY + fixWordingY , wordingSize = date_pillarSize  , dateFont = month_day_pillar_font  , double = False  )
	else:
		makeMainDateText ( dat_buf[1] , 596+14+ date_pillarSize + mainDate_offset , 241 + titleOrgY + titleY + fixWordingY , wordingSize = date_pillarSize  , dateFont = month_day_pillar_font  , double = False  )



	draw_SquareFull()


	## 直槓 橫槓
	## --------------------------------------
	draw_H_line( hight = 214+userDefineHight*0.8 , LineWidth = 2 )
	# draw_H_line( hight = 1195 , LineWidth = 4 )	
	draw_H_line( hight = 352+userDefineHight*0.3+titleOrgY*0.7 , LineWidth = 2 )


	# ## 本卦變卦分隔線
	# draw_H_line( hight = 1160+10+userDefineHight*0.3 , LineWidth = 1 )

	# draw_H_line( hight = 1250+10+userDefineHight*0.3 , LineWidth = 1 )

	# ## |||||||||||||||||||||||||||||
	# # draw_InfoLine ( center =  27  , hight = 1168   , size = 75  , color = mainColor ,lineWidth= 1 )
	# draw_InfoLine ( center =  107  , hight = 1168   , size = 75  , color = mainColor ,lineWidth= 1 )
	# draw_InfoLine ( center =  527  , hight = 1168   , size = 75  , color = mainColor ,lineWidth= 1 )
	# draw_InfoLine ( center =  605  , hight = 1168   , size = 75  , color = mainColor ,lineWidth= 1 )






	 ##   ##    ##      ####    ##   ##           #####      ##     ######   #######
	 ### ###   ####      ##     ###  ##            ## ##    ####    # ## #    ##   #
	 #######  ##  ##     ##     #### ##            ##  ##  ##  ##     ##      ## #
	 #######  ##  ##     ##     ## ####            ##  ##  ##  ##     ##      ####
	 ## # ##  ######     ##     ##  ###            ##  ##  ######     ##      ## #
	 ##   ##  ##  ##     ##     ##   ##            ## ##   ##  ##     ##      ##   #
	 ##   ##  ##  ##    ####    ##   ##           #####    ##  ##    ####    #######
	dateColor = mainColor
	userDefine = allDataDict["user_define"]
	if userDefine == True:
		makeMainDateText (  "日辰自訂", 48 , 240 + titleOrgY  , wordingSize = 40  , color= mainColor , dateFont = GenJyuuOrgNormal )
		draw.rectangle(  ( 45 , 238  ,  210 , 284 )  , fill= None , outline= mainColor ,  width = 2 )
		# makeMainDateText (  allDataDict['jeChi'][0]+ "→" + allDataDict['jeChi'][2], 48 , 162 , color = dateColor , wordingSize = 34  , dateFont = textRegularFont )
		dateColor = ignoreColor ## 如果日辰是自訂，上面的日期時間資料就淡化



	# 上標日期
	# 2024/10/28/00:49
	def makeDateText ( text , x , y, fontSize = dateTextSize , wordFont = dateNumberFont_A , color= dateColor ):
		other_style = ImageFont.truetype(  wordFont, fontSize , encoding="utf-8")
		draw.text(( x  , y ), text , fill= color , font = other_style )
		# draw.multiline_text(( x+screenWidth*0.5- wordingSize*0.5+x  , y ), text , fill= color , font = other_style , spacing=0, align='left')
		## 納甲五行

	makeDateText ( allDataDict['fullDate'] , 47 , 26 + dateY_adj )



	## 銅錢
	def makeCircle ( x = 650 , y = 120 , radious = 120 , lineColor  = subGray , lineWidth= 5 ):
		draw.ellipse(    (  ( x - int(radious*0.5) , y - int(radious*0.5) ) , ( x + int(radious*0.5) , y + int(radious*0.5) )  ) , fill= None , outline=lineColor ,width= lineWidth )
	# def draw_SquareFull ( offset = 8  , width = screenWidth , hight = screenHight  , color = mainColor, outlineColor = darkBlue , lineWidth = 20  ):
		draw.rectangle(  ( x - int(radious*0.16) , y - int(radious*0.16)  ,  x + int(radious*0.16) , y + int(radious*0.16) )  , fill= None , outline= lineColor ,  width = lineWidth )
	spaceAdd = 138
	x_po = 680
	y_po = 106
	makeCircle( 690,y_po )
	makeCircle( 690+spaceAdd,y_po )
	makeCircle( 690+spaceAdd+spaceAdd,y_po )


	## 爻內字型 

	def makeSubInfoText ( text , x , y, color = mainColor , dateFont = textRegularFont , fixY = poFix_y , wordingSize = 40 , double = True , switch = True ):
		other_style = ImageFont.truetype( dateFont, wordingSize, encoding="utf-8")
		# draw.text(( x+2  , y+2 - wordingSize*0.25 ), text , fill= (245,245,245) , font = other_style )
		if switch == True:
			draw.text(( x  , y - wordingSize*0.23  + wordingSize * fixY ), text , fill= color , font = other_style )
			if double == True :
				draw.text(( x-1  , y - wordingSize*0.23  + wordingSize * fixY ), text , fill= color , font = other_style )





	# makeSubInfoText (  allDataDict['fullDarkDate'] + "  -  " + allDataDict['hourGanZi'] + "時" , 145 , chineseDateY+2  , color = dateColor  , double = False )

	## 甲辰 | 十一月十六
	makeSubInfoText ( allDataDict['yearGanZi']  , 47 , chineseDateY  , wordingSize = 40  , color = dateColor  , double = False ) ## 年干支
	if allDataDict['hourGanZi'] != "X":
		makeSubInfoText (  allDataDict['fullDarkDate'] +" ・ "  + allDataDict['hourGanZi'] + "時", 145 , chineseDateY   , wordingSize = 40  , color = dateColor  , double = False )
	else:
		makeSubInfoText (  allDataDict['fullDarkDate'] +" ・ "  + "某時", 145 , chineseDateY   , wordingSize = 40  , color = dateColor  , double = False )



	# makeSubInfoText (  " - "  + allDataDict['hourGanZi'] + "時", 435 , chineseDateY   , wordingSize = 40  , color = dateColor  , double = False )
	draw_InfoLine ( center =  134  , hight = chineseDateY + 2   , size = 36  , color = dateColor , lineWidth= 2 )

	## 節氣
	if allDataDict['jeChi'][1] == "!":
		makeSubInfoText ( "["+ allDataDict['jeChi'][0]+ "] → " + allDataDict['jeChi'][2], 48 , chineseDateY+49 ,color = dateColor , wordingSize = 37  , dateFont = textRegularFont  , double = False )
	else:
		makeSubInfoText (  allDataDict['jeChi'][0]+ " → " + allDataDict['jeChi'][2], 48 , chineseDateY+49 , color = dateColor , wordingSize = 37  , dateFont = textRegularFont  , double = False )









	## 64卦小圖
	# makeMainDateText ( allDataDict['home_symbol'] + "" + allDataDict['change_symbol'] , 600, 1290 , wordingSize = 66  , dateFont = guaFont , color = sdw_color) ## "䷃.䷄"



	## 男問工作運勢
	# makeSubInfoText (  allDataDict['note'] , 120 , 1304+11  , wordingSize = 42 )
	# makeSubInfoText(*( (allDataDict['note'][:14] + '\n' + allDataDict['note'][14:], x, 1315 - 10) if len(allDataDict['note']) > 14 else (allDataDict['note'], x, y) ))

	import re
	if allDataDict['note'] != "XXX":
		# def has_three_digit_prefix(s):
		# 	return bool(re.match(r'^\d\.\d\.\d ', s[:6]))

		## 中文全型算一個字，其他算半個字，統計長度用
		def is_chinese(char):
			add = 0
			for word in char:
				if '\u4e00' <= word <= '\u9fff':
					add += 1
				else:
					add += 0.5
			# print(add)
			return int(add)

		# allDataDict['note'] = allDataDict['note'].replace("/",",")


		wordingAdj = 16 ## 斷行字數

		# if calculate_text_weight( allDataDict['note'] ) > 16:
		# if has_three_digit_prefix( allDataDict['note'] ) == True:
		# if is_chinese(allDataDict['note']) > 16:


		noteSize = 40
		wordingAdj = 100

		w_index = get_cutoff_index( allDataDict['note'] )
		if w_index != None:
			wordingAdj = w_index
			noteSize = 34



		makeSubInfoText(*( (allDataDict['note'][:wordingAdj ] + '\n' + allDataDict['note'][ wordingAdj:], 127 , 1315 - 17 ) if len(allDataDict['note']) > wordingAdj else (allDataDict['note'], 115 , 1315) ) , dateFont = textRegularFont , double = False , wordingSize = noteSize )
		## 內文超過14個字就換行，並把Y往上調整17		
		# text_value = allDataDict['note'][:wordingAdj] + '\n' + allDataDict['note'][wordingAdj:]

	# else:
	# 	makeSubInfoText( allDataDict['fullDate'] + allDataDict['mainGuaName'], 125 , 1315  , dateFont = textRegularFont , double = False , wordingSize = 42 )

	## "占" 字
	# makeBallText( text_buf = "占"  , x_buf = 48 , text_x_adj = 0, text_y_adj=-1 , y_buf = 1302  , wordingSize_buf = 50 , color_buf = None , font_buf = GenShinBold , LineWidth_buf = 5 , extra_size = 10 , wordingColor_Buf = "#9EA8BA" ,lineColor_buf = "#9EA8BA" , invertMode = False )
	makeBallText(   text_buf =  "占"  ,
					x_buf =  48  ,
					text_x_adj =  0  ,
					text_y_adj =  -1  ,
					y_buf =  1302 +11 ,
					wordingSize_buf =  50  ,
					color_buf =  None  ,
					font_buf =  GenShinBold  ,
					# font_buf =  GenJyuuOrgBold  ,					
					# font_buf =  textRegularFont,					
					LineWidth_buf =  5  ,
					extra_size =  8  ,
					wordingColor_Buf =  "#8894A5"  ,
					lineColor_buf =  "#8894A5"  ,
					invertMode =  False  
				)
	noteWordingSize = 34
	wordSpace = 55
	startPo = 767
	up_heght = 1289
	dn_hight = 1358


	# allDataDict['allDeeziList']
	# makeMainDateText ( "身", startPo  , up_heght  , wordingSize = noteWordingSize  , dateFont = textRegularFont , double = False ,)
	# makeMainDateText ( "|", startPo +16 , 1329 , wordingSize = 17  , dateFont = textRegularFont , double = False )
	# makeMainDateText ( allDataDict['home_guaBody'], startPo  , dn_hight , wordingSize = noteWordingSize  , dateFont = textRegularFont , color = subGray , double = False )

	# allDataDict['allDeeziList'] = ['戌', '亥', '午', '寅', '巳', '辰', '酉', '未']
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

		makeMainDateText ( title , startPo  , up_heght  , wordingSize = noteWordingSize  , dateFont = textRegularFont , double = False ,)
		if title == "貴":

			makeMainDateText ( godItem[0], startPo  , dn_hight -noteWordingSize+1 , wordingSize = noteWordingSize  , dateFont = textRegularFont , color = subGray , double = False )	
			makeMainDateText ( godItem[1], startPo  , dn_hight , wordingSize = noteWordingSize  , dateFont = textRegularFont , color = subGray , double = False )			

		else:


			makeMainDateText ( "|", startPo +16 , 1327 , wordingSize = 17  , dateFont = textRegularFont , double = False )
			makeMainDateText ( godItem , startPo  , dn_hight , wordingSize = noteWordingSize  , dateFont = textRegularFont , color = subGray , double = False )
		if count == 5:
			break
		count += 1
		startPo += wordSpace




	draw_InfoLine ( center =  740  , hight = up_heght   , size = 100  , color = mainColor ,lineWidth= 2 )






	titleHight = 385 # 大標高度

	# subWordingSize = 53 # 字的大小53
	insideSpace = -115 # 上下行距
	startLineHight =  1062  # 起始基礎高度(最低)
	hightBuf = 8


	kongWangStart = 927
	kongWangSpace = 49
	kongWangWordingSize = 44


	def drawSubLine ( x = 930, hight = 290  , size = 88 , color = mainColor , LineWidth = 1 ):
		draw.line(( x , hight ,x+size , hight ), fill= color, width = LineWidth )


	kongWangX_adj = -5
	makeMainDateText ( allDataDict['home_kongWang'][0], kongWangStart , 240 + kongWangX_adj +titleOrgY, wordingSize = kongWangWordingSize  , dateFont = textRegularFont  , double = False )
	makeMainDateText ( allDataDict['home_kongWang'][1], kongWangStart + kongWangSpace , 240 + kongWangX_adj +titleOrgY, wordingSize = kongWangWordingSize  , dateFont = textRegularFont  , double = False )
	drawSubLine( x = 926, hight = 288 + kongWangX_adj +titleOrgY , size = 92 , LineWidth = 2 )
	makeMainDateText ( "空", kongWangStart , 292 + kongWangX_adj +titleOrgY, wordingSize = kongWangWordingSize  , dateFont = textRegularFont , double = False )
	makeMainDateText ( "亡", kongWangStart + kongWangSpace , 292 + kongWangX_adj+titleOrgY , wordingSize = kongWangWordingSize  , dateFont = textRegularFont , double = False )	
	## ∅∅∅∅









	 ######    ####      ####            ######    ####    ######   ####     #######
	  ##  ##    ##      ##  ##           # ## #     ##     # ## #    ##       ##   #
	  ##  ##    ##     ##                  ##       ##       ##      ##       ## #
	  #####     ##     ##                  ##       ##       ##      ##       ####
	  ##  ##    ##     ##  ###             ##       ##       ##      ##   #   ## #
	  ##  ##    ##      ##  ##             ##       ##       ##      ##  ##   ##   #
	 ######    ####      #####            ####     ####     ####    #######  #######

	## 大標

	wording_4 = -37
	wording_5 = -56
	wording_6 = -80


	print( "mainGuaName: " ,allDataDict['mainGuaName'])
	if len(allDataDict['mainGuaName']) == 4:
		makeMainDateText ( "【 "  , 365 + wording_4 , titleHight+1 , wordingSize = 62  , dateFont = textRegularFont )
		makeMainDateText (  allDataDict['mainGuaName'] , 441 + wording_4 , titleHight , wordingSize = 62  , dateFont = textRegularFont )
		makeMainDateText ( "】", 699 + wording_4 , titleHight , wordingSize = 62  , dateFont = textRegularFont )
	elif len(allDataDict['mainGuaName']) == 5:
		makeMainDateText ( "【 " , 357 + wording_5 , titleHight , wordingSize = 62  , dateFont = textRegularFont )		
		makeMainDateText (  allDataDict['mainGuaName'] , 428 + wording_5 , titleHight , wordingSize = 62  , dateFont = textRegularFont )
		makeMainDateText ( "】", 746 + wording_5 , titleHight , wordingSize = 62  , dateFont = textRegularFont )
	else:
		makeMainDateText ( "【" , 346+ wording_6 , titleHight , wordingSize = 62  , dateFont = textRegularFont )
		makeMainDateText (  allDataDict['mainGuaName'] , 415+ wording_6 , titleHight , wordingSize = 62  , dateFont = textRegularFont )
		makeMainDateText (  "】", 792+ wording_6 , titleHight , wordingSize = 62  , dateFont = textRegularFont )
# 【】【】


	gua_wordingSize = 40
	downGuaHight_h = 1214

	guaNoteSize = 38

	## 本卦變卦分隔線
	draw_H_line( hight = downGuaHight_h -24  + userDefineHight*0.3 , LineWidth = 2 )

		## |||||||||||||||||||||||||||||
	draw_InfoLine ( center =  107  , hight = downGuaHight_h - 15   , size = 66  , color = mainColor ,lineWidth= 2 )
	draw_InfoLine ( center =  529  , hight = downGuaHight_h - 15   , size = 66  , color = mainColor ,lineWidth= 2 )
	draw_InfoLine ( center =  605  , hight = downGuaHight_h - 15   , size = 66  , color = mainColor ,lineWidth= 2 )

	draw_H_line( hight =  downGuaHight_h + 60  + userDefineHight*0.3 , LineWidth = 2 )

	makeMainDateText ( "本", 48 , downGuaHight_h -3  , wordingSize = gua_wordingSize+2  , dateFont = textRegularFont , double = False )


	## 本卦卦名 ######################################################################
	makeMainDateText ( allDataDict['home_title']   , 127 , downGuaHight_h- 2  , wordingSize = gua_wordingSize  , dateFont = textRegularFont , double = False)

	colorAdj_A = "#8e98ac" # 比subgray深一號
	colorAdj_B = "#738093" # 比subgray深兩號
	
	## 本卦五行屬性
	if allDataDict['home_rowHead'] in ["離","震","坤"]:
		makeBallText( text_buf = allDataDict['home_rowHead']  , x_buf = (len(allDataDict['home_title']) * gua_wordingSize ) +127 +14  , y_buf = downGuaHight_h + 2  , wordingSize_buf = guaNoteSize , color_buf = colorAdj_A , font_buf = GenJyuuOrgMedium , invertMode = False )
	else:
		makeBallText( text_buf = allDataDict['home_rowHead']  , x_buf = (len(allDataDict['home_title']) * gua_wordingSize ) +127 +14  , y_buf = downGuaHight_h + 2  , wordingSize_buf = guaNoteSize , color_buf = colorAdj_A , font_buf = GenJyuuOrgMedium , invertMode = False )


	## 沖合( 六沖，六合 )
	if allDataDict['home_mode'] != "":
		# print( ">>>>> "+allDataDict['home_mode'] )
		if len(allDataDict['home_title'] ) == 4: ## 卦名如果是四個字，整個向右挪一點
			makeBallText( text_buf = allDataDict['home_sort'] +"•"+ allDataDict['home_mode']  , x_buf = 350, y_buf = downGuaHight_h + 2   , wordingSize_buf = guaNoteSize , color_buf = colorAdj_A , font_buf = GenJyuuOrgMedium , invertMode = True  )
		
		else: ## 三個字就正常擺
			## 本卦順位( 二爻，三爻，遊魂...)
			makeBallText( text_buf = allDataDict['home_sort']  , x_buf = 410 - len(allDataDict['home_mode'])*gua_wordingSize-15 , y_buf = downGuaHight_h + 2   , wordingSize_buf = guaNoteSize , color_buf = colorAdj_A , font_buf = GenJyuuOrgMedium , invertMode = True  )
			## 沖合( 六沖，六合 )
			makeBallText( text_buf = "• " + allDataDict['home_mode']  , x_buf = 410 -10, y_buf = downGuaHight_h + 2   , wordingSize_buf = guaNoteSize , color_buf = colorAdj_A , font_buf = GenJyuuOrgMedium , invertMode = True  )
	else:
		## 無沖合，本卦順位( 二爻，三爻，遊魂...)
		makeBallText( text_buf = allDataDict['home_sort']  , x_buf = 370 + ( len(allDataDict['home_title'])-3)*gua_wordingSize*0.5 , y_buf = downGuaHight_h + 2   , wordingSize_buf = guaNoteSize , color_buf = colorAdj_A , font_buf = GenJyuuOrgMedium , invertMode = True  )
																			## 依照字數調整向右移半個字

	# makeMainDateText ( "⊗．•‧˙﹒¯ˉ＊⊠⛒•¦|↹⇆㊎ ㊍ ㊌ ㊋ ㊏", 50 , 1360 , wordingSize = 25  , dateFont = textRegularFont )	

	x_offset = 503
	makeMainDateText ( "變", 547 , downGuaHight_h - 2  , wordingSize = gua_wordingSize  , dateFont = textRegularFont , double = False)

	## 變卦卦名 ######################################################################	
	if allDataDict['change_number'] == None:	
		makeMainDateText ( "—  —  — ", 745 , downGuaHight_h-7 , wordingSize = gua_wordingSize  , dateFont = textRegularFont , double = False)
	else:
		## 本卦五行屬性
		if allDataDict['change_rowHead'] in ["離","震","坤"]:
			makeBallText( text_buf = allDataDict['change_rowHead']  , x_buf = (len(allDataDict['change_title']) * gua_wordingSize ) +130 +15   + x_offset , y_buf = downGuaHight_h + 2   , wordingSize_buf = guaNoteSize , color_buf = colorAdj_A , font_buf = GenJyuuOrgMedium , invertMode = False )
		else:
			makeBallText( text_buf = allDataDict['change_rowHead']  , x_buf = (len(allDataDict['change_title']) * gua_wordingSize ) +130 +15   + x_offset , y_buf = downGuaHight_h + 2   , wordingSize_buf = guaNoteSize , color_buf = subGray , font_buf = GenJyuuOrgMedium , invertMode = False )


		makeMainDateText ( allDataDict['change_title'], 128 + x_offset , downGuaHight_h- 2  , wordingSize = gua_wordingSize  , dateFont = textRegularFont , double = False)
		## 風火家人
	
		
		## 沖合( 六沖，六合 )
		if allDataDict['change_mode'] != "":
			# print( ">>>>> "+allDataDict['change_mode'] )
			if len(allDataDict['change_title'] ) == 4: ## 卦名如果是四個字，整個向右挪一點
				makeBallText( text_buf = allDataDict['change_sort'] +"•"+ allDataDict['change_mode']  , x_buf = 360 + x_offset , y_buf = downGuaHight_h   , wordingSize_buf = guaNoteSize , color_buf = colorAdj_A , font_buf = GenJyuuOrgMedium , invertMode = True  )
			
			else: ## 三個字就正常擺
				## 本卦順位( 二爻，三爻，遊魂...)
				makeBallText( text_buf = allDataDict['change_sort']  , x_buf = 420 - len(allDataDict['change_mode'])*gua_wordingSize-15  + x_offset , y_buf = downGuaHight_h + 2   , wordingSize_buf = guaNoteSize , color_buf = colorAdj_A , font_buf = GenJyuuOrgMedium , invertMode = True  )
				## 沖合( 六沖，六合 )
				makeBallText( text_buf = "• " + allDataDict['change_mode']  , x_buf = 420 -10 + x_offset , y_buf = downGuaHight_h + 2   , wordingSize_buf = guaNoteSize , color_buf = colorAdj_A , font_buf = GenJyuuOrgMedium , invertMode = True  )
		else:
			## 無沖合，本卦順位( 二爻，三爻，遊魂...)
			makeBallText( text_buf = allDataDict['change_sort']  , x_buf = 370 + ( len(allDataDict['change_title'])-3)*gua_wordingSize*0.5  + x_offset , y_buf = downGuaHight_h + 2   , wordingSize_buf = guaNoteSize , color_buf = colorAdj_A , font_buf = GenJyuuOrgMedium , invertMode = True  )
			






	threeHo_color = "#cbd0d8"
	if noteSwitch == True:
		## 三合 月 日
		if allDataDict['month_day_ThreeHoId'][0][0] in ( "O", "P" ):

			monthColor = getTypeColor( allDataDict['month_day_ThreeHoId'][0] ) ## 月

			if allDataDict[ "monthGanZi" ][-1] == "月":
				draw_SquareMark(  x = 313    , y = 243+ titleOrgY    , squareSize = 86  , outlineColor = monthColor  )
				# draw_SquareMark_lit (  x = 313    , y = 243+ titleOrgY     , squareSize = 84 , space = 46  , outlineColor = monthColor , lineWidth = 4 )
			else:
				draw_SquareMark( x = 313  + date_pillarSize   , y = 243+ titleOrgY     , squareSize = 86  , outlineColor = monthColor  )
				# draw_SquareMark_lit (  x = 313  + date_pillarSize   , y = 246+ titleOrgY     , squareSize = 84 , space = 46  , outlineColor = monthColor , lineWidth = 4 )


		if allDataDict['month_day_ThreeHoId'][1][0] in ( "O", "P" ):
			dayColor = getTypeColor( allDataDict['month_day_ThreeHoId'][1] ) ## 日

			draw_SquareMark(    x = 603  + date_pillarSize   , y = 243+ titleOrgY      , squareSize = 86  , outlineColor = dayColor  )
			# draw_SquareMark_lit (  x = 603  + date_pillarSize   , y = 246+ titleOrgY     , squareSize = 84 , space = 46  , outlineColor = dayColor , lineWidth = 4 )



	for row_id in  range(6):
		adj_hight = startLineHight + hightBuf
		# draw_HightLine( center = 0 , hight = adj_hight )


		home_naGia_adj = -22
		# home_naGiaType_adj = -14
		inputGua_adj = 0
		home_innYao_adj = 2
		home_shiYao_adj = 2

		home_family_adj = 10
		home_sixAnimal_adj = home_family_adj

		change_naGia_adj = 0
		change_family_adj = 0

		hideGodAdj_x = 25




		if  allDataDict['hide_family'].count("X") == 6  and  allDataDict['changeIdIndex'].count("X") != 6: ## 沒伏神，有變卦
			# print( "沒伏神，有變卦")
			home_naGia_adj = -12
			# home_naGiaType_adj = 0
			# inputGua_adj = 0
			# home_innYao_adj = 0
			# home_shiYao_adj = 0
			home_family_adj = -6
			home_sixAnimal_adj = -6

			change_naGia_adj = 0
			change_family_adj = 0

		# if  allDataDict['hide_family'].count("X") != 6  and  allDataDict['changeIdIndex'].count("X") == 6: ## 有伏神，沒變卦
		# 	# print("有伏神，沒變卦")
		# 	home_naGia_adj = -20
		# 	home_naGiaType_adj = 0
		# 	inputGua_adj = 0
		# 	home_innYao_adj = 0
		# 	home_shiYao_adj = 0
		# 	home_family_adj = 0
		# 	home_sixAnimal_adj = 0

		# 	change_naGia_adj = 0
		# 	change_family_adj = 0

		if  allDataDict['hide_family'].count("X") == 6  and  allDataDict['changeIdIndex'].count("X") == 6: ## 既沒伏神也沒變卦
			# print( "既沒伏神也沒變卦" )
			home_naGia_adj = -2
			# home_naGiaType_adj = 0
		# 	inputGua_adj = 0
			# home_innYao_adj = 5
			# home_shiYao_adj = 5
			home_family_adj = -18
			home_sixAnimal_adj = -18

			# change_naGia_adj = 0
		# 	change_family_adj = 0

		# if row_id < 5:
		# 	draw_H_line( hight =adj_hight -23 , color = subGray , LineWidth = 1 )

		## 納甲 取得 ['甲子', '甲寅', '甲辰', '壬午', '壬申', '壬戌'] 中的地支 [-1]
		# makeYaoText ( allDataDict['home_naGia'][row_id][-1] , 153 + home_naGia_adj , adj_hight , color = mainLitGray )





		## 納甲 + 納甲五行
		## 納甲 + 納甲五行
		## 納甲 + 納甲五行
		## 納甲 + 納甲五行
		## 納甲 + 納甲五行
		## ㊊㊋㊌㊍㊎㊏㊐㊑㊒㊓㊔㊕㊖㊗㊘㊙㊚㊛㊜㊝㊞㊟㊠㊡㊢㊣㊤㊥㊦㊧㊨㊩㊪㊫㊬㊭㊮㊯㊰  ◌  ¤ × ✕ ⇤⇥ ←→ ⋮︙☼ ⚠︎
		makeSubInfoText ( allDataDict['home_naGia'][row_id][-1], 660+13 + home_naGia_adj , adj_hight ,wordingSize = subWordingSize )
		makeSubInfoText ( allDataDict['home_naGiaType'][row_id] , 719+13 + home_naGia_adj , adj_hight ,wordingSize = subWordingSize )

		# if (allDataDict['dayGanZi'][-1] == allDataDict['home_naGia'][row_id][-1]) or (allDataDict['monthGanZi'][-1] == allDataDict['home_naGia'][row_id][-1]):

		 ## 如果納甲地支和日月支相同，則為日辰入卦, 底線效果
		if allDataDict['home_naGia'][row_id][-1] in allDataDict['dayGanZi']  or allDataDict['home_naGia'][row_id][-1] in allDataDict['monthGanZi'] :

			draw.line((  678 + home_naGia_adj , adj_hight + subWordingSize + 8 , 725 + home_naGia_adj  , adj_hight + subWordingSize + 8 ), fill= subGray , width = 3 )




		## 分數小字 
		makeSubInfoText ( allDataDict['home_naGia_rank'][row_id]  , 715+53+18 + home_naGia_adj , adj_hight-8 , dateFont = SourceSans3 ,wordingSize = rankSize, color = subGray ,double = False , switch = noteSwitch )
		# makeSubInfoText ( "㊊"  , 715+53+13 + home_naGia_adj , adj_hight , dateFont = GenJyuuOrgMedium ,wordingSize = rankSize, color = subGray ,double = False , switch = noteSwitch )


 # homeThreeHoId = ['-', '-', '-', 'Pa2', '-', 'Oa1']
 # changeThreeHoId = ['-', '-', 'Oa0', '-', '-', '-']
 # month_day_ThreeHoId = ['-', '-']

		if noteSwitch == True:
			## 三合局小方框
			if allDataDict['homeThreeHoId'][row_id][0] in ("O"):	
				homeThreeHoColor = getTypeColor( allDataDict['homeThreeHoId'][row_id] )
				draw_SquareMark( x = home_naGia_adj + 672 , y = adj_hight    , squareSize = 58  , outlineColor = homeThreeHoColor  )

			if allDataDict['homeThreeHoId'][row_id][0] in ("P"):	
				homeThreeHoColor = getTypeColor( allDataDict['homeThreeHoId'][row_id] )
				draw_SquareCut(  x = home_naGia_adj + 672+1, y = adj_hight   , squareSize = 58  , cut = 12, outlineColor = homeThreeHoColor, fillColor = None, lineWidth = 2 )
				# draw_SquareMark_lit (  x = home_naGia_adj + 658+12  , y = adj_hight -2     , squareSize = 60 , space = 32  , outlineColor = homeThreeHoColor , lineWidth = 1 )





		if allDataDict['home_naGia'][row_id][-1]  in allDataDict['home_kongWang']:
			## 空亡的圈
			makePoint ( x = 637+13 +home_naGia_adj , y = adj_hight + 35 , radious = 20 ,pointColor = None , lineColor = subGray , LineWidth = 3 , switch = noteSwitch )







		## 卦身
		if allDataDict['home_naGia'][row_id][-1]  in allDataDict['home_guaBody']:
			print( "本卦卦身")			
			print( allDataDict['home_naGia'][row_id][-1]  )
			makePoint ( x = 642+15 + home_naGia_adj, y = adj_hight + 40 , radious = 10 , switch = noteSwitch )

			# makePoint ( x = 637+25 +home_naGia_adj , y = adj_hight + 35 , radious = 20 ,pointColor = None , lineColor = subGray , LineWidth = 3 )











		# mainColor = (82,157,211) ## 淺藍版主色


		# if allDataDict['home_naGia'][row_id][-1] in allDataDict['home_kongWang']:
		# 	makeIconText ( "⨯" , 123 + home_naGiaType_adj , adj_hight+25 , fontSize = 40 , color = iconLitGray )

		## 六獸
		makeSubInfoText ( allDataDict['home_sixAnimal'][row_id] , 272 +1 + home_sixAnimal_adj , adj_hight , wordingSize = subWordingSize, color = mainColor )
		## 分割直槓
		draw_InfoLine ( center =  home_sixAnimal_adj+338 +1  , hight = adj_hight+2   , size = 51  , color = mainColor ,lineWidth= 2 )

		## 六親
		makeSubInfoText ( allDataDict['home_family'][row_id],     348 +1 + home_family_adj , adj_hight ,wordingSize = subWordingSize )



		def makeCircle ( x=650 , y = 86 , radious = 50 , lineColor  = mainColor , lineWidth= 2):
			draw.ellipse(    (  ( x - int(radious*0.5) , y - int(radious*0.5) ) , ( x + int(radious*0.5) , y + int(radious*0.5) )  ) , fill= None , outline=lineColor ,width= lineWidth )


		# noise_layer  = Image.open('noise.png').convert('RGBA')
		## 世爻應爻圖片
		# inYao_layer  = Image.open('inYaoBlue.png').convert('RGBA') # 叠加的透明PNG图片，需要读取为RGBA，4通道的格式
		# shiYao_layer  = Image.open('siYaoBlue.png').convert('RGBA') # 叠加的透明PNG图片，需要读取为RGBA，4通道的格式
		# shiYao_layer  = Image.open('siYao.png').convert('L').resize(img.size)	

		siIn_x = 574

		## 應爻
		if allDataDict['home_innYao'] == str(row_id+1) :
			# makeCircle( home_naGia_adj + 630, adj_hight +28)
			# img.paste(inYao_layer, ( siIn_x + home_innYao_adj , adj_hight+1 )  , inYao_layer ) # 在bg图像上叠加/合成layer图像
			makeBallText( text_buf = "應"  , x_buf = siIn_x + home_innYao_adj , text_x_adj = -1, y_buf = adj_hight+4  , wordingSize_buf = 50 , color_buf = subGray , font_buf = GenJyuuOrgMedium , LineWidth_buf = 0 , lineColor_buf = subGray ,extra_size = 2 , invertMode = False )
# "#a2aabd"
		## 世爻
		if allDataDict['home_shiYao'] == str(row_id+1) :
			# makeCircle( home_naGia_adj + 630, adj_hight +28)
			# img.paste(shiYao_layer, ( 575 + home_shiYao_adj , adj_hight+1 )  , shiYao_layer ) # 在bg图像上叠加/合成layer图像
			# img.paste(shiYao_layer, ( siIn_x + home_shiYao_adj , adj_hight+1 )  , shiYao_layer ) # 在bg图像上叠加/合成layer图像
			makeBallText( text_buf = "世"  , x_buf = siIn_x + home_innYao_adj , text_x_adj = -1 , y_buf = adj_hight+4  , wordingSize_buf = 50 , color_buf = subGray , font_buf = GenJyuuOrgMedium , LineWidth_buf = 0 , lineColor_buf = subGray ,extra_size = 2 , invertMode = False )
			# img2 = Image.new("RGB", shiYao_layer.size , mainColor )
			# img= Image.composite(img, img2 , shiYao_layer)

# mask = Image.open('data/src/horse.png').convert('L').resize(im1.size)
# im = Image.composite(im1, im2, mask)



		

		## 伏神
		if allDataDict['hide_naGia'][row_id]!="X":
		# 	## 伏神納甲							
			makeSubInfoText ( allDataDict['hide_naGia'][row_id][-1]  , 50+hideGodAdj_x + home_naGia_adj , adj_hight ,wordingSize = subWordingSize )

			## 伏神六親
			makeSubInfoText (  allDataDict['hide_family'][row_id]    , 115+hideGodAdj_x + home_naGia_adj , adj_hight ,wordingSize = subWordingSize )

			## 分數小字
			makeSubInfoText ( allDataDict['hide_naGia_rank'][row_id]  , 226 +hideGodAdj_x + home_naGia_adj , adj_hight-8 ,dateFont = SourceSans3, wordingSize = rankSize, color = subGray , double = False , switch = noteSwitch )
			## 分隔直槓	
			draw_InfoLine ( center =  110+hideGodAdj_x + home_naGia_adj  , hight = adj_hight+2   , size = 51  , color = mainColor ,lineWidth= 2 )

			if allDataDict['hide_naGia'][row_id][-1]  in allDataDict['home_kongWang']:
				## 空亡圈圈
				makePoint ( x = 28 + hideGodAdj_x + home_naGia_adj , y = adj_hight + 35 , radious = 20 ,pointColor = None , lineColor = subGray , LineWidth = 3 , switch = noteSwitch )



			


		## 變卦
		if allDataDict['changeIdIndex'][row_id] == "O":

			changeGuaNaGia = 831
## 853-22
			# change_naGia_adj
			# change_family_adj

			makeSubInfoText (  allDataDict['change_naGia'][row_id][-1]   , changeGuaNaGia + change_naGia_adj , adj_hight ,  wordingSize = subWordingSize )

			## 分數小字
			makeSubInfoText ( allDataDict["change_naGia_rank"][row_id]  , changeGuaNaGia +155+20+3 + change_naGia_adj , adj_hight -8 ,dateFont = SourceSans3, wordingSize = rankSize, color = subGray , double = False , switch = noteSwitch )

 
			# ## 三合局小方框
			# if allDataDict['changeThreeHoId'][row_id] == "O":	
			# 	draw_SquareMark( x =changeGuaNaGia + change_naGia_adj -20+20  , y = adj_hight +2  , squareSize = 54   )

			if noteSwitch == True:
				## 三合局小方框
				if allDataDict['changeThreeHoId'][row_id][0] in ( "O", "P", "H" ):		
					changeThreeHoColor = getTypeColor( allDataDict['changeThreeHoId'][row_id] )

					draw_SquareMark( x = changeGuaNaGia + change_naGia_adj -2 , y = adj_hight   , squareSize = 58 , outlineColor = changeThreeHoColor  )

					# draw_SquareMark_lit (  x = changeGuaNaGia + change_naGia_adj -4 , y = adj_hight-2     , squareSize = 60 , space = 32  , outlineColor = changeThreeHoColor , lineWidth = 1 )


			# ## 變卦卦身
			# if allDataDict['change_naGia'][row_id][-1]  in allDataDict['home_guaBody']:
			# 	print("變卦卦身")		
			# 	print( allDataDict['change_naGia'][row_id][-1] )
			# 	makePoint (x = changeGuaNaGia -15 + change_naGia_adj  , y = adj_hight + 40 , radious = 10 , switch = noteSwitch )



			# makeYaoText ( allDataDict['change_naGia'][row_id][-1] , -69 + changeGua_x_adj , adj_hight , color = mainLitGray )	
			# if allDataDict['change_naGia'][row_id][-1] in allDataDict['home_kongWang']:
			# 	# makeYaoText ( "›" ,  -97 + changeGua_x_adj , adj_hight-26 , fontSize = 80 , color = mainVeryLitGray )
			# 	makeIconText ( "⨯" , -98 + changeGua_x_adj , adj_hight+25 , fontSize = 40 , color = iconLitGray  )
			
			## 變卦六親
			makeSubInfoText (  allDataDict['change_family'][row_id]  , changeGuaNaGia+67 + change_family_adj , adj_hight ,wordingSize = subWordingSize )			
			# makeYaoText ( allDataDict['change_family'][row_id] ,  changeGua_x_adj , adj_hight , color = darkDarkGray ) 
			## 分隔直槓	
			draw_InfoLine ( center =  changeGuaNaGia+61 + change_naGia_adj , hight = adj_hight+2  , size = 51  , color = mainColor ,lineWidth= 2 )

			# makeSubInfoText (  "←→↼⇀⥒⥓"   , changeGuaNaGia + change_naGia_adj - subWordingSize + 5 , adj_hight+7 ,dateFont = dateNumberFont_B ,wordingSize = subWordingSize-4 , color = ( "#CEDAE0") , switch = noteSwitch )
			## 化進小點點
			if allDataDict['home_forwardBack'][row_id]  == "FW":

				makePoint ( x = changeGuaNaGia + change_naGia_adj + 24   , y = adj_hight + -12 , radious = 8 , pointColor = subGray )
				# makePoint ( x = changeGuaNaGia -11 +change_naGia_adj, y = adj_hight + 2 , radious = 10 )
# ∇∆«»
				# makeSubInfoText (  "»"   , changeGuaNaGia + change_naGia_adj - subWordingSize + 72 , adj_hight -45 ,dateFont = GenJyuuOrgNormal ,wordingSize = subWordingSize-4 , color = subGray , double = False , switch = noteSwitch )
		# makeSubInfoText (  "↗︎"   , changeGuaNaGia + change_naGia_adj , adj_hight ,wordingSize = subWordingSize )
# ↘︎	↗︎↘︎↔←→↑	
			## 化退小點點
			elif allDataDict['home_forwardBack'][row_id]=="BK":
				makePoint ( x = changeGuaNaGia + change_naGia_adj + 24   , y = adj_hight + subWordingSize +6 , radious = 8 , pointColor = subGray )				
				# makePoint ( x = changeGuaNaGia -12 +change_naGia_adj, y = adj_hight + 40 , radious = 10 )
				# makeSubInfoText ( text , x , y, color= mainColor , dateFont = GenJyuuOrgNormal , fixY = poFix_y , wordingSize = 40 )
				# makeSubInfoText (  "・"[0]   , changeGuaNaGia + change_naGia_adj - subWordingSize + 57 , adj_hight +40 , dateFont = GenJyuuOrgNormal , wordingSize = subWordingSize-4 , color = subGray , double = False , switch = noteSwitch ) ##mainWhiteGray
				# makeSubInfoText (  "«"   , changeGuaNaGia + change_naGia_adj - subWordingSize + 72 , adj_hight -45 ,dateFont = GenJyuuOrgNormal ,wordingSize = subWordingSize-4 , color = subGray , double = False , switch = noteSwitch )

			# else:( "#CEDAE0") 
			# 	draw_HightLine( center = -35 + changeGua_x_adj , hight = adj_hight )

			if allDataDict['change_naGia'][row_id][-1]  in allDataDict['home_kongWang']:
				## 變卦空亡圈圈
				makePoint ( x = changeGuaNaGia -24 + change_naGia_adj , y = adj_hight + 35 , radious = 20 ,pointColor = None , lineColor = subGray , LineWidth = 3  , switch = noteSwitch )





# ↑ ↓





		centerAdj = -7
		
		lineWidth = 4
		fixHight = 0
		if allDataDict['inputGuaList'][ row_id ] == "0":
			# 少陰
			def draw_litYoLine ( hight = adj_hight + fixHight  , center = centerAdj + inputGua_adj ):
				lineLength = 64
				halfLength = lineLength*0.5
				draw.line((  screenWidth*0.5-halfLength+center, hight+subWordingSize*0.5 , screenWidth*0.5-5 + center , hight+subWordingSize*0.5  ), fill= mainColor , width= lineWidth )

				draw.line((  screenWidth*0.5 +5 + center, hight+subWordingSize*0.5 , screenWidth*0.5+halfLength+center , hight+subWordingSize*0.5  ), fill= mainColor , width= lineWidth )
			draw_litYoLine()

		if allDataDict['inputGuaList'][ row_id ] == "1":
				# 爻 少陽
			def draw_litYoLine ( hight = adj_hight + fixHight  , center = centerAdj + inputGua_adj ):
				lineLength = 64
				halfLength = lineLength*0.5
				draw.line((  screenWidth*0.5-halfLength+center, hight+subWordingSize*0.5 , screenWidth*0.5+halfLength+center , hight+subWordingSize*0.5  ), fill= mainColor , width= lineWidth )
			draw_litYoLine()

		if allDataDict['inputGuaList'][ row_id ] == "X":
			# 爻 老陰
			def draw_litDarkLine ( hight = adj_hight + fixHight , left = 70 , right = 70 , center = centerAdj + inputGua_adj ):
				lineLength = 52
				halfLength = lineLength*0.5
				draw.line((  screenWidth*0.5 -halfLength + center, hight-halfLength +subWordingSize*0.5 , screenWidth*0.5 +halfLength + center, hight+halfLength +subWordingSize*0.5  ), fill= mainColor, width= lineWidth+1 )
				draw.line((  screenWidth*0.5 -halfLength + center, hight+halfLength +subWordingSize*0.5 , screenWidth*0.5 +halfLength + center, hight-halfLength +subWordingSize*0.5  ), fill= mainColor, width= lineWidth+1 )		
			draw_litDarkLine()

		if allDataDict['inputGuaList'][ row_id ] == "@":
			# 老陽
			def draw_oldYoLine ( hight = adj_hight + fixHight  , left = 80 , right = 80 , circleRadius = 28 , center = centerAdj + inputGua_adj ):
				draw.ellipse((  screenWidth*0.5 - circleRadius  + center, hight+1 - circleRadius + subWordingSize*0.5 , screenWidth*0.5 + circleRadius  + center , hight+1 + circleRadius + subWordingSize*0.5 ), outline= mainColor, width= lineWidth )
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








		# uploadImgurIO(img)              ## imgur台灣確定不能用了
		# uploadImgurIO(preview_img)	   ## imgur台灣確定不能用了



	## 如果show 等於true ，就秀出圖片，如果為flase則上傳網路並回傳圖片網址
	if show == True:
		img.show()
		print("SHOW")

	else:
		from cloudinary_helper import upload_image, delete_older_than

		## Notion模式
		if notion == True:
			res = upload_image( img , "__image_hosting" ) ## 存到"__image_hosting"檔案夾中
			high_res = res["url"]
			print( "上傳一張圖片至圖床")
			return high_res

		else:
			preview_img = img.resize( (  int(screenWidth*0.25) , int(screenHight*0.25)  )   ,Image.BILINEAR  ) ## line縮圖預覽用圖
			# # 上傳圖片
			res = upload_image( img )
			high_res = res["url"]
			# print("連結：", res["url"])

			res = upload_image( preview_img )
			low_res = res["url"]
			# print("連結：", res["url"])
			return [high_res , low_res]


# ㊊㊋㊌㊍㊎㊏㊐



if __name__ == '__main__':

	from mainFun import  *

	# drawUi_v2( mainFunction( "@111X0"  , noteText =  "病" ) , fontStyle = "Fb", "tipsMode" = "ON", uiStyle = "CB"  , show = True  )



	# drawUi_v2( mainFunction( "@10010" ,noteText = "男問今年工作運勢", userDefineDate = "") , show = True ,)
	# drawUi_v2( mainFunction( "01X@@@" ,noteText = "男問今年工作運勢", userDefineDate = "") , show = True ,)
	# drawUi_v2( mainFunction( "11X$01" ,noteText = "男問今年工作運勢",user_mouthZi = "巳月" , user_dayGanZi = "己丑", userDefineDate = "") , show = True ,)	 ## 三合
	# drawUi_v2( mainFunction( "110$0$" , noteText = "三合測試" ) )
	drawUi_v2( mainFunction( "11X0$X" ,noteText = "可否得到銀行offer", userDefineDate = "2025/06/05/21/22") , show = True ,)	
	# drawUi_v2( mainFunction( "X11001" ,noteText = "男問今年工作運勢", userDefineDate = "") , show = True ,) ## 5字	
	# drawUi_v2( mainFunction( "0X01X0" ,noteText = "男問今年工作運勢", userDefineDate = "") , show = True ,)
	# drawUi_v2( mainFunction( "111@0X" ,noteText = "男問今年工作運勢", userDefineDate = "") , show = True ,) #6字

	# for e in loopMaker( "01@X" , 6 ):

	# 	print("\n\n>>>>> ", e )
	# 	drawUi_v2( mainFunction(  e ) )




# 〇〇⌤↖ ↘ ⤒ ⤓✲⎈⌫ ⟵
# ⌦ ⎀ , ⇤ ⇥ ⤒ ⤓ , ⇞ ⇟ ⎗ ⎘
# ← → ↑ ↓, ◀ ▶ ▲ ▼,