# -*- coding: utf-8 -*-
from fourPillar_tool import getFourPillar # 日期，四柱，時間資訊取得

from sixYao_data import  * # baGuaAllDict 取得
from guaMatch import  *    # 小工具取得
from combineDataMain import  * # 整理輸入資料

from sanHo_work import  *    # 三合局


# 屬性速查表
#  
# "金":"乾為天、天風姤、天山遯、天地否、風地觀、山地剝、火地晉、火天大有",
# "水":"坎為水、水澤節、水雷屯、水火既濟、澤火革、雷火豐、地火明夷、地水師",
# "土":"艮為山、山火賁、山天大畜、山澤損、火澤睽、天澤履、風澤中孚、風山漸",
# "木":"震為雷、雷地豫、雷水解、雷風恆、地風升、水風井、澤風大過、澤雷隨",
# "木":"巽為風、風天小畜、風火家人、風雷益、天雷無妄、火雷噬嗑、山雷頤、山風蠱",
# "火":"離為火、火山旅、火風鼎、火水未濟、山水蒙、風水渙、天水訟、天火同人",
# "土":"坤為地、地雷復、地澤臨、地天泰、雷天大壯、澤天夬、水天需、水地比",
# "金":"兌為澤、澤水困、澤地萃、澤山咸、水山蹇、地山謙、雷山小過、雷澤歸妹"
#  
## 取得六親中沒有出現的項目，屬於那一種五行，再由該五行的本卦取得預設的六親和納甲的排序，再把該項目獨立的找出來

# 六沖
six_antiList = ["乾為天","坎為水","艮為山","震為雷","巽為風","離為火","坤為地","兌為澤","天雷無妄","雷天大壯"]

# 六合
six_matchList =["雷地豫","地雷復","山火賁","火山旅","水澤節","澤水困","天地否","地天泰"]



# 進神
# 變爻與正爻五行同，而本爻向前十二地支一位；亥變子、寅變卯、巳變午、申變酉。
# 四庫土，形成丑變辰、辰變未、未變戌、戌變丑。
# 丑變辰，雖是進神，也有化墓之缺。
forwardGod_Dict = { "亥":"子" , "寅":"卯" , "巳":"午" , "申":"酉" , "丑":"辰" , "辰":"未" , "未":"戌" , "戌":"丑" }

# 退神
# 動爻與變爻支形成子變亥、卯變寅、午變巳、酉變申。
# 四庫土，由辰變丑、未變辰、戌變未、丑變戌。
backGod_Dict =    { "子":"亥" , "卯":"寅" , "午":"巳" , "酉":"申" , "辰":"丑"  , "未":"辰", "戌":"未" , "丑":"戌" }



## 六沖
anti_dict =  { "子":"午" ,  "丑":"未" , "寅":"申" , "卯":"酉" , "辰":"戌" , "巳":"亥" , "午":"子" , "未":"丑" , "申":"寅" , "酉":"卯" , "戌":"辰" , "亥":"巳"}

## 六合
match_dict =  { "子":"丑" , "寅":"亥" , "卯":"戌" , "辰":"酉" , "巳":"申" , "午":"未" , "未":"午" , "申":"巳" , "酉":"辰" , "戌":"卯" , "亥":"寅" , "丑":"子" }

## 相刑
kill_dict = {   "寅":"申" , "巳":"寅" , "申":"巳" , "丑":"未" , "未":"戌" , "戌":"丑" , "子":"卯" , "卯":"子" }

## 暗動


## 所有的納甲(伏神本爻變爻)的地支全挖出來
def getAllDeeZi(home_naGiaBuf=None, hide_naGiaBuf=None, changeIdIndexBuf=None, change_naGiaBuf=None):
	def getDeeZi(naGia):
		return naGia[-1] if naGia != 'X' else None

	allDeeziSet = set()

	if home_naGiaBuf:
		for naGia in home_naGiaBuf:
			dz = getDeeZi(naGia)
			if dz:
				allDeeziSet.add(dz)

	if hide_naGiaBuf:
		for naGia in hide_naGiaBuf:
			dz = getDeeZi(naGia)
			if dz:
				allDeeziSet.add(dz)

	if changeIdIndexBuf and change_naGiaBuf:
		for idx, flag in enumerate(changeIdIndexBuf):
			if flag == 'O':
				naGia = change_naGiaBuf[idx]
				dz = getDeeZi(naGia)
				if dz:
					allDeeziSet.add(dz)

	return list(allDeeziSet)


# home_naGia  = ['甲子', '甲寅', '甲辰', '辛未', '辛巳', '辛卯']
# hide_naGia  = ['X', 'X', '辛酉', 'X', 'X', 'X']
# changeIdIndex  = ['O', 'X', 'X', 'X', 'X', 'X']
# change_naGia  = ['辛丑', '辛亥', '辛酉', '辛未', '辛巳', '辛卯']

# allDeeziList = getAllDeeZi(home_naGia, hide_naGia, changeIdIndex, change_naGia)
# print(allDeeziList)













## 

				# 組成的字元 , 數字的位數
				# "01@X" , 6
def loopMaker( elementString , num ):
	from itertools import permutations
	totalList = []
	elemBuf = ""
	for i in elementString:
		for j in range(num):
			elemBuf += i
			# print( elemBuf )
	elemBuf = "000000111111X@"
	add = 0
	for each in list( set( permutations( elemBuf , num ) )  ):
		print( ''.join(each) )
		totalList.append(''.join(each) )
		add+=1
	print( "Total:" , add )
	return totalList

# loopMaker( "01@X" , 6 )


typeDict =[
		{ "head" : "乾" , "type":"金" , "item":["乾為天",  "天風姤",    "天山遯",  "天地否",  "風地觀",  "山地剝",  "火地晉",  "火天大有"]},
		{ "head" : "坎" , "type":"水" , "item":["坎為水",  "水澤節",    "水雷屯",  "水火既濟","澤火革",  "雷火豐",  "地火明夷", "地水師"]},
		{ "head" : "艮" , "type":"土" , "item":["艮為山",  "山火賁",    "山天大畜","山澤損",  "火澤睽",  "天澤履",  "風澤中孚", "風山漸"]},
		{ "head" : "震" , "type":"木" , "item":["震為雷",  "雷地豫",    "雷水解",  "雷風恆",  "地風升",  "水風井",  "澤風大過", "澤雷隨"]},
		{ "head" : "巽" , "type":"木" , "item":["巽為風",  "風天小畜",  "風火家人","風雷益",   "天雷無妄","火雷噬嗑","山雷頤",   "山風蠱"]},
		{ "head" : "離" , "type":"火" , "item":["離為火",  "火山旅",    "火風鼎",  "火水未濟","山水蒙",  "風水渙",   "天水訟",   "天火同人"]},
		{ "head" : "坤" , "type":"土" , "item":["坤為地",  "地雷復",    "地澤臨",  "地天泰",  "雷天大壯","澤天夬",   "水天需",   "水地比"]},
		{ "head" : "兌" , "type":"金" , "item":["兌為澤",  "澤水困",    "澤地萃",  "澤山咸",  "水山蹇",  "地山謙",   "雷山小過", "雷澤歸妹"]}
		]




def getRowTypeHead( guaName , lostItemList = [] ):
	# guaName = "乾為天"
	# lostItemList = ['官鬼','子孫']
	typeHeadDict = {"乾": "01","坤": "02","坎": "29","離": "30","震": "51","艮": "52","巽": "57","兌": "58"}
	newList = [ "X","X","X","X","X","X"]
	newNaGiaType = [ "X","X","X","X","X","X"]
	for roType in typeDict:
		if guaName in roType["item"] :
			# print( typeHeadDict[ roType["item"][0][0] ] ) ## 57
			idNum = typeHeadDict[ roType["item"][0][0] ]
			print( ">>> 符頭: %s ID: %s  "%(   roType["item"][0][0]   , typeHeadDict[ roType["item"][0][0] ]) )## 兌  58
			# lostItemList = ['子孫','官鬼']

			for baGuaItem in baGuaAllDict:
				if baGuaItem['number'] == idNum:   ## 找到符合的號碼ID後
					# print ( baGuaItem['title'] )					
					# print ( baGuaItem['family'] )
					# print ( baGuaItem['naGiaType'] )
					# print ( baGuaItem['binary'] )
					for showItem in lostItemList:
						## showItem - 需要秀出來的項目名稱 '子孫'
						print ("需要秀出來的項目 ", showItem ,baGuaItem['family']) # 
						print ( baGuaItem['family'].index( showItem )) # 4

						showItemName = showItem  
						indexId = baGuaItem['family'].index( showItem ) ## list中的順位，4
						newList[ indexId ] = showItem  ### 把項目名稱依照順序id存進newList中，取代該位置的X		 newList的第四個元素換成"子孫"

						newNaGiaType[ indexId ] = baGuaItem['naGia'][  baGuaItem['family'].index( showItem ) ]	## 取得納甲list中，和六親list項目的順位id相同的項目				
	# print (newList )
	# print (newNaGiaType )	
	# newList
	# ['X', 'X', '官鬼', 'X', '子孫', 'X'] 
	# newNaGiaType
	# ['X', 'X', '酉', 'X', '巳', 'X']
	return  newList , newNaGiaType 





## 取得六親
# 						木 , ['甲子', '甲寅', '甲辰', '丙戌', '丙子', '丙寅']
def checkFamilyType( element_type  , all_ement  ):

	Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
	ZhiId = {"子": "水" , "丑": "土" , "寅": "木", "卯": "木", "辰": "土", "巳": "火", "午": "火", "未": "土", "申": "金", "酉": "金", "戌": "土", "亥": "水"}
	element_Dist = { "木" : "" , "火" : "" , "土" : "" , "金" : "" , "水" : "" }

	burnList = [ "木","火","土","金","水" ]
	attactList = [ "木","土","水","火","金"  ]	

	## 先從帶頭的八純卦中取得主要五行，先訂出兄弟才能定其他六親
	## 定義 element_Dist 中屬 element_type 為兄弟 Exp: element_Dist["水"] = "兄弟"
	element_Dist[element_type] = "兄弟" 					

	## 定義 element_Dist 中屬 element_type 代入burnList中得到被我生的為子孫   Exp: element_Dist["木"] = "子孫"
	elem_type_z = burnList [ (burnList.index( element_type )+1)%5 ]  # 子孫
	element_Dist[elem_type_z] = "子孫"

	elem_type_z = burnList [ (burnList.index( element_type )+4)%5 ]  # 父母
	element_Dist[elem_type_z] = "父母"

	elem_type_z = attactList [ (attactList.index( element_type )+1)%5 ]  # 妻財
	element_Dist[elem_type_z] = "妻財"

	elem_type_z = attactList [ (attactList.index( element_type )+4)%5 ]  # 官鬼
	element_Dist[elem_type_z] = "官鬼"

	# print(all_ement)
	# print( element_Dist )
	typeBuf = []
	familyList = []
	for elemBuf in all_ement:
		# print( elemBuf )
		deeZuBuf = elemBuf[-1]
		elemType = ZhiId[ deeZuBuf ]  ## 取得五行 Exp: ZhiId = {"子": "水" , "丑": "土" , "寅": "木".....}
		# print(  elemType )
		# print( element_Dist[ elemType ] )
		# print("")
		typeBuf.append( elemType )
		familyList.append( element_Dist[ elemType ] )

	return typeBuf , familyList
	# ('火木土水金土', ['妻財', '子孫', '官鬼', '兄弟', '父母', '官鬼'])
# print(checkFamilyType())





		



## 空亡 - 日干支
## 六獸 - 日干

	## 桃花位 ## 日支
	## 驛馬 ## 日支
	## 祿位 ## 日干
	## 貴人 ## 日干
	## 羊刃 ## 日干
	## 月破 ## 月支








## 從納甲的地支中，依照日干支檢查是否有空亡

def checkKongWang( checkItemList , dayGanZi ): ## 空亡  日干支

	# checkItemList = ['子', '寅', '辰', '午', '申', '戌']
# 己巳
	# checkItemList = ['卯', '丑', '亥', '未', '巳', '卯']
	kongWangList = [ "X","X","X","X","X","X"]

	dayKongWang = getKongWang( dayGanZi ) ## 日空亡
	# print( "dayKongWang:",dayKongWang)

	print(">>>>>>>>>>>>>>  ", dayGanZi , dayKongWang)
	# print ( "checkItemList , dayGanZi", checkItemList , dayGanZi )
	# print(checkItemList)
	gia_id = 0
	# print(checkItemList , dayGanZi)
	for gia in checkItemList:
		print( "gia: ",gia )

		if gia in dayKongWang:
			# print( ">日空亡",dayKongWang )
			# print(gia)
			# id = checkItemList.index( gia_id )
			kongWangList[gia_id] = "O"
		gia_id+=1

	return kongWangList


# 日支
# 桃花位  - 寅午戌-卯  "亥卯未-子  "申子辰-酉  巳酉丑-午
flower_po = { "寅":"卯", "亥":"子" , "申":"酉" , "巳":"午","午":"卯", "卯":"子" , "子":"酉" , "酉":"午","戌":"卯", "未":"子" , "辰":"酉" , "丑":"午" }

# 日支
# 驛馬  -  寅午戌-申  亥卯未-巳  申子辰-寅  巳酉丑-亥
horse_po = {"寅":"申", "亥":"巳" , "申":"寅" , "巳":"亥","午":"申", "卯":"巳" , "子":"寅" , "酉":"亥","戌":"申", "未":"巳" , "辰":"寅" , "丑":"亥"}

# 日干
# 祿位
guan_po = {"甲":"寅" , "乙":"卯" , "丙":"巳" , "丁":"午" , "戊":"巳" , "己":"午" , "庚":"申" ,"辛":"酉", "壬":"亥" , "癸":"子"}

# 日干
# 甲戊庚牛羊 乙己鼠猴鄉 丙丁豬雞位 壬癸蛇兔藏 六辛逢虎馬 此是貴人方
# 貴人   甲戊庚-丑未    乙己-子申    丙丁-酉亥    辛-寅午    壬癸-巳卯
helpful_po = {"甲":"丑未" , "乙":"子申" , "丙":"酉亥" , "丁":"酉亥", "戊":"丑未" , "己":"子申" , "庚":"丑未"  , "辛":"寅午", "壬":"巳卯"  , "癸":"巳卯" }


# 日干
# 羊刃  甲 - 卯 , 乙 - 寅 , 丙戊-  午 , 丁己-  巳 , 庚 - 酉 , 辛 - 申 , 壬 - 子 , 癸 - 亥
yangKnife_po = {"甲":"卯" , "乙":"X" , "丙":"午" , "丁":"X" , "戊":"午" , "己":"X" , "庚":"酉" , "辛":"X" , "壬":"子" , "癸":"X" }

matchMode_dict = { "X":"六沖","O":"六合","--": "" }


# 天喜方位依季節判定： ( 月支 )
# 春（寅卯辰）之戌：春季出生者，天喜在戌。
# 夏（巳午未）之丑：夏季出生者，天喜在丑。
# 秋（申酉戌）之辰：秋季出生者，天喜在辰。
# 冬（亥子丑）之未：冬季出生者，天喜在未。
godHappy_po = { "寅" : "戌" , "卯" : "戌" , "辰" : "戌" , "巳" : "丑" , "午" : "丑" , "未" : "丑" , "申" : "辰" , "酉" : "辰" , "戌" : "辰" , "亥" : "未" , "子" : "未" , "丑" : "未" }


# 長生，帝旺， 墓，構成三合局
# 亥    卯    未  木局
# 寅    午    戌  火局
# 巳    酉    丑  金局
# 申    子    辰  水局
############################################################################################################################
############################################################################################################################

# def panBuilderMain(  msg = ""  , lineBotId = "" , lineBotName = "" , userImage = "" , note = "" , testMode = False ):
# from jsonDataFunc import *
# from jsonDataClass import *

def mainFunction( inputData = "1X10@1" , noteText = None , user_mouthZi = "" , user_dayGanZi = "" , userDefineDate = "" ):
						## 卦的符號模式	 問卦的的內文	    自訂月干支:癸亥月     自訂日干支:乙酉日	      日期 2017/2/27/2/45

	inputData = inputData.replace( "$" , "@")





	# jsonData = jsonDataClass( lineBotId , lineBotName , userImage ) 
















	if noteText == None:
		noteText = inputData

	three_pillar = False
	if user_dayGanZi == "":
		if  "<" in userDefineDate:  ## 如果只有三柱
			userDefineDate = userDefineDate[:-1]
			three_pillar = True

	## 日期時間四柱取得
	dateBuf_list =  getFourPillar(  fullDate = userDefineDate , detail = True )
	print( dateBuf_list )


	# ('2024/12/23/03:30', '2024/11/23', ['甲辰', '丙子', '辛酉', '庚寅'], ['冬至', '>', '小寒'], '(一)', '03:30')
	yangDateData , innDateData , fourPillarList , jeChi , week , nowTime = dateBuf_list

	yearGanZi   =  fourPillarList[0]      ## 年干支
	monthGanZi  =  fourPillarList[1]     ## 月干支
	dayGanZi    =  fourPillarList[2]       ## 日干支
	hourGanZi   =  fourPillarList[3]       ## 時干支	
	# jeChi_buf = jeChi
	# noteText = "測試測試一二三四五六七"


	# 輸入的爻，0-少陰  1-少陽   @-老陽  X-老陰
	# inputData = "1X10@1"
	orgGua , changeGua , changeIdIndex , inputGuaList = checkMainData( inputData )
	print( orgGua , changeGua , changeIdIndex , inputGuaList )
	print("\n")
	print ( "		inputData:          %s" %  inputData )
	print ( "		inputGuaList:       %s" %  inputGuaList )
	print ( "		orgGua:             %s" %  orgGua )
	print ( "		changeGua:          %s" %  changeGua )
	print ( "		changeIdIndex:      %s" %  changeIdIndex )
	print("\n")


	if changeGua == orgGua: ## 如果變卦和本卦相同，代表沒有變卦
		changeGua = "X"

	mainDataDict = {
		"inputGua" : None,
		"fullDate" : None,
		"fullDarkDate" : None,
		"yearGanZi" : None,
		"monthGanZi" : None,
		"dayGanZi" : None,
		"hourGanZi" : None,

		"user_define": False,
		"user_mouthZi" : None,
		"user_dayGanZi" : None,



		"jeChi" : None,
		"week":None,
		"time":None,
		"allDeeziList":None,
		"note":None,

		"flower_po" : None,           #桃花位
		"horse_po" : None,            #驛馬
		"guan_po" : None,             #祿位
		"helpful_po" : None,          #貴人
		"yangKnife_po" : None,        #羊刃
		"godHappy_po" : None,		  #天喜
		# "month_broken_po" : None,     #月破		
		'changeIdIndex':None,           # id 指引
		'inputGuaList':None,


		"mainGuaName": None, # 總掛名 Exp: 家人之大畜卦
		"vs_type" : None, # 本卦與變卦的生剋 Exp: 木>>土

		"home_number" : None ,
		"home_up" : None ,
		"home_dn" : None ,
		"home_title" : None ,
		"home_upGua" : None ,
		"home_dnGua" : None ,
		"home_inOutGua" : None ,
		"home_rowType" : None ,
		'home_rowHead' : None ,

		"home_sort" : None ,		
		"home_shiYao" : None ,
		"home_innYao" : None ,
		"home_guaBody" : None ,
		"home_naGia" : None ,
		"home_symbol" : None , ## symbol



		"home_naGia_rank" : None , ## 納甲的分數

		"homeThreeHoId" : None,   ## 本爻三合局的指引
		"changeThreeHoId" : None, ## 變爻三合局指引	
		"month_day_ThreeHoId" : None, ## 月,日,三合局指引	





		"home_kongWang" : None ,
		"home_kongWangId" : None ,
		"home_naGiaType" : None ,
		"home_family" : None ,
		"home_sixAnimal" : None ,
		"home_lostFamily" : None ,

		"home_mode": "--" ,
		"home_forwardBack" : [ "X" , "X" , "X" , "X" , "X" , "X" ], ## 退進神

		"hide_family" : None ,
		"hide_naGia" : None ,

		'hide_naGia_rank': None , ## 伏神的納甲分數

		"change_number" : None ,
		"change_up" : None ,
		"change_dn" : None ,
		"change_title" : None ,
		"change_upGua" : None ,
		"change_dnGua" : None ,
		"change_inOutGua" : None ,
		"change_rowType" : None ,
		'change_rowHead' : None ,
		"change_sort" : None ,		
		"change_shiYao" : None ,
		"change_innYao" : None ,
		"change_guaBody" : None ,
		"change_naGia" : None ,
		"change_symbol" : None , ## symbol

		"change_kongWang" : None ,		
		"change_kongWangId" : None ,

		"change_naGiaType" : None ,
		"change_naGia_rank" : None ,

		"change_family" : None ,
		"change_sixAnimal" : None ,
		"change_mode" : None
	}

	# {'number': '64', 'title': '火水', 'body': '未濟', 'outGua': '離', 'inGua': '坎', 'rowType': '火', 'sort': '三爻', 'shiYao': '3', 'innYao': '6', 'guaBody': '申', 'naGia': '寅辰午酉未巳', 'naGiaType': '木土火金土火', 'family': .get( '父母', '子孫', '兄弟', '妻財', '子孫', '兄弟' ) , 'binary': '010101'},


	mainDataDict['inputGua' ] = inputGuaList

	mainDataDict['fullDarkDate' ] = innDateData              ## 陰曆	

	mainDataDict['yearGanZi' ]  = fourPillarList[0]      ## 年干支
	mainDataDict['monthGanZi' ]  = fourPillarList[1]     ## 月干支
	mainDataDict['dayGanZi' ]  = fourPillarList[2]       ## 日干支

	if three_pillar == True:
		mainDataDict['hourGanZi' ] = "X"       ## 時干支⊠
		mainDataDict['fullDate' ] = "/".join( yangDateData.split("/")[:-1]) + "/ -- --"          ## 陽曆		 如果只有年月日柱，時間欄就空著

	else:
		mainDataDict['fullDate' ] = yangDateData             ## 陽曆
		mainDataDict['hourGanZi' ] = fourPillarList[3]       ## 時干支


	if len(user_mouthZi) == 3: ## 如果月的輸入為三個字( 甲戌月 )
		mainDataDict['user_mouthZi'] = user_mouthZi[:-1]        ## 自訂月支  輸入為三個字時， 甲戌月 -> 甲戌 
	else:
		mainDataDict['user_mouthZi'] = user_mouthZi             ## 自訂月支	輸入為兩個字，   辰月 or 乙丑

		   ## 自訂日干支

	if len(user_dayGanZi) == 3: ## 如果日的輸入為三個字( 乙丑日 )
		mainDataDict['user_dayGanZi'] = user_dayGanZi[:-1]
	else:
		mainDataDict['user_dayGanZi'] = user_dayGanZi		





	if (mainDataDict['user_mouthZi'] != "" ) and (mainDataDict['user_dayGanZi'] != "" ):
		mainDataDict['monthGanZi' ]  = mainDataDict['user_mouthZi']     ## 月干
		mainDataDict['dayGanZi' ]  = mainDataDict['user_dayGanZi']		## 日干支
		mainDataDict['user_define' ] = True
		print("月干支 remark!")

	mainDataDict['jeChi' ] = jeChi  ## 節氣
	mainDataDict['week' ] = week    ## 星期
	mainDataDict['time' ] = nowTime ## 時間
	
	# print("新的日干支",mainDataDict['dayGanZi' ])
	## 桃花位 ## 日支
	mainDataDict['flower_po'] =  flower_po.get( mainDataDict['dayGanZi' ][1] )  
	
	## 驛馬 ## 日支
	mainDataDict['horse_po'] =  horse_po.get( mainDataDict['dayGanZi' ][1] )  
	
	## 祿位 ## 日干
	mainDataDict['guan_po'] =  guan_po.get( mainDataDict['dayGanZi' ][0] )  
	
	## 貴人 ## 日干
	mainDataDict['helpful_po'] =  helpful_po.get( mainDataDict['dayGanZi' ][0] )  
	
	## 羊刃 ## 日干
	mainDataDict['yangKnife_po'] = yangKnife_po.get( mainDataDict['dayGanZi' ][0] )  


	## 天喜  月支
	if mainDataDict['monthGanZi'][-1] in "子丑寅卯辰巳午未申酉戌亥":
		mainDataDict['godHappy_po'] = godHappy_po.get( mainDataDict['monthGanZi'][-1] )
	elif mainDataDict['monthGanZi'][0] in "子丑寅卯辰巳午未申酉戌亥":
		mainDataDict['godHappy_po'] = godHappy_po.get( mainDataDict['monthGanZi'][0] )		





	# ## 月破 ## 月支
	# Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]


	# if mainDataDict['monthGanZi'][1] in Zhi: # 癸卯月，癸卯
	# 	mainDataDict['month_broken_po'] = Zhi[(Zhi.index( mainDataDict['monthGanZi'][1]) + 6)%12]
	# 	## 月破的意思是月支相沖的地支，所以先取出月支的排序之後加6，則得到對沖的地支

	# 	# print( "@@@", mainDataDict['monthGanZi'])
	# 	# print( "@@", (Zhi.index( mainDataDict['monthGanZi'][1]) + 6) )
	# 	# print( "@@", Zhi[(Zhi.index( mainDataDict['monthGanZi'][1]) + 6)%12] )
	# 	print("月破", mainDataDict['month_broken_po'] )


	# elif mainDataDict['monthGanZi'][0] in Zhi:  ## 卯月
	# 	# print( "@@@", mainDataDict['monthGanZi'])		
	# 	mainDataDict['month_broken_po'] = Zhi[(Zhi.index( mainDataDict['monthGanZi'][0]) + 6)%12]



	# 	print("月破", mainDataDict['month_broken_po'] )
	# else:
	# 	print("no 月破")


	## 變爻ID指引
	mainDataDict['changeIdIndex'] =  changeIdIndex
	## 搖卦結果
	mainDataDict['inputGuaList'] =  inputGuaList


	for baGuaItem in baGuaAllDict:
		if orgGua == baGuaItem.get( 'binary' ) : ## 本卦
			print("=====================================================================")
			## 卦編號1-64
			mainDataDict['home_number'] = baGuaItem.get( 'number' )
			
			## 上名 exp: 風火
			mainDataDict['home_up'] = baGuaItem.get( 'title' )
			
			## 下名 exp: 家人
			mainDataDict['home_dn'] = baGuaItem.get( 'body' )		


			## 卦名 exp: 風火家人	
			# mainDataDict['home_title'] = baGuaItem.get( 'title' ) + baGuaItem.get( 'body' )
			mainDataDict['home_title'] = (lambda aa, bb: baGuaItem.get( 'title' ) + "為" + baGuaItem.get( 'body' ) if len(baGuaItem.get( 'title' ) + baGuaItem.get( 'body' )) == 2 else baGuaItem.get( 'title' ) + baGuaItem.get( 'body' ))("A", "B")
# lambda baGuaItem: baGuaItem.get('title') + "為" + baGuaItem.get('body') if len(baGuaItem.get('title') + baGuaItem.get('body')) == 2 else baGuaItem.get('title') + baGuaItem.get('body')

			## 外卦(上卦) exp: 巽
			mainDataDict['home_upGua'] =  baGuaItem.get( 'outGua' )
			
			## 內卦(下卦) exp: 離
			mainDataDict['home_dnGua'] = baGuaItem.get( 'inGua' ) 
			
			## 上下卦 exp: 巽離
			mainDataDict['home_inOutGua'] = baGuaItem.get( 'outGua' ) + baGuaItem.get( 'inGua' ) 
			
			## 五行屬性 exp: 木 
			mainDataDict['home_rowType'] = baGuaItem.get( 'rowType' )

			## 屬於那一個八卦( 乾，兌，離，震....)
			mainDataDict['home_rowHead'] = next((d["head"] for d in typeDict if mainDataDict['home_title'] in d["item"]), None)

			## 卦在屬性中的排序 exp: 歸魂
			mainDataDict['home_sort'] = baGuaItem.get( 'sort' )




			
			## 世爻 exp: 2 (由下往上數1-5)
			mainDataDict['home_shiYao'] = baGuaItem.get( 'shiYao' )
			
			## 應爻 exp: 5 (由下往上數1-5) 
			mainDataDict['home_innYao'] = baGuaItem.get( 'innYao' )
			
			## 卦身 exp: 未 
			mainDataDict['home_guaBody'] = baGuaItem.get( 'guaBody' ) 
			
			## 納甲 exp: ['辛丑', '辛亥', '辛酉', '癸丑', '癸亥', '癸酉']
			mainDataDict['home_naGia'] = baGuaItem.get( 'naGia' )

			## symbol
			mainDataDict['home_symbol'] = baGuaItem.get( 'symbol' )			

			print(mainDataDict['home_naGia'],type(mainDataDict['home_naGia']))
			mainDataDict['home_naGia_rank'] = naGiaRanking( 
															naGia_inList  = mainDataDict['home_naGia'] ,
															# dateGanZiList = [ mainDataDict['monthGanZi'][-1],mainDataDict['dayGanZi'][-1],mainDataDict['monthGanZi'][0],mainDataDict['dayGanZi'][0]] 
															dayGanZiList = [ mainDataDict['dayGanZi'][-1],mainDataDict['dayGanZi'][0]], ## 日支，日干
															monthGanZiList = [ mainDataDict['monthGanZi'][-1],mainDataDict['monthGanZi'][0]], ## 月支，月干	
															rankType = "home" ## 本卦以home為標籤
															)
			print( mainDataDict['home_naGia_rank'])


			# mainDataDict['home_naGia_rank'] = ['⁺0°', '⁻4', '⁺4', '⁺0', '⁺8', '⁺4^']
			# mainDataDict['changeIdIndex'] =   ['X', 'O', 'X', 'X', 'O', 'X'] 
			## 如個有暗動，就把changeIdIndex暗動爻位的X改成D
			for i, val in enumerate(mainDataDict['home_naGia_rank']):  
				if "^" in val:
					# print( ">>>>>>",mainDataDict['changeIdIndex'] )
					if mainDataDict['changeIdIndex'][i] == "X":
						mainDataDict['changeIdIndex'][i] = "D"






			## 空亡
			mainDataDict['home_kongWang'] = getKongWang( mainDataDict['dayGanZi' ] )
			# print( mainDataDict['home_naGia'] )
			# print( mainDataDict['dayGanZi' ]  )
			# print(checkKongWang( baGuaItem.get( 'naGia' ) ,mainDataDict['dayGanZi' ] ))
			## 空亡 exp: ['X', 'O', 'X', 'X', 'X', 'X']	
			mainDataDict['home_kongWangId'] = checkKongWang( baGuaItem.get( 'naGia' ) ,mainDataDict['dayGanZi' ] )
			
			## 納甲五行 exp:['木', '土', '水', '土', '火', '木']
			mainDataDict['home_naGiaType'] = baGuaItem.get( 'naGiaType' )
			
			## 六親 exp:	['兄弟', '妻財', '父母', '妻財', '子孫', '兄弟']
			mainDataDict['home_family'] = baGuaItem.get( 'family' )
			
			## 六獸 exp:	['玄武', '青龍', '朱雀', '勾陳', '螣蛇', '白虎']	

			mainDataDict['home_sixAnimal'] = getSixAnimal( mainDataDict['dayGanZi' ] )

			# mainDataDict['home_mode'] = baGuaItem.get( 'mode' ) ## 沖 or 合

			## 六沖 六合 無
			mainDataDict['home_mode'] = matchMode_dict.get( baGuaItem.get( 'mode' ))



			
			## 沒出現的六親 exp:	['官鬼']
			mainDataDict['home_lostFamily'] = checkNon( baGuaItem.get( 'family' ))
			print( ">> 現有的六親 ",baGuaItem.get( 'family' ))
			print( ">> 缺少的六親 ",checkNon( baGuaItem.get( 'family' )))
			# print ( ">>",mainDataDict['home_lostFamily'])	

			# getRowTypeHead( guaName = "乾為天" , lostItemList = ['子孫','官鬼'] ):
			## 伏神六親 exp:['X', 'X', '官鬼', 'X', '子孫', 'X'] 
			## 伙神納甲 exp:['X', 'X', '酉', 'X', '巳', 'X'] 
			mainDataDict['hide_family'],mainDataDict['hide_naGia'] = getRowTypeHead( baGuaItem.get( 'title' ) + baGuaItem.get( 'body' )  , checkNon( baGuaItem.get( 'family' )  )  )
			##																														    ## 輸入現有的六親，再和全部都有的六親比對，列出缺少的六親項目
			## 取得六親中沒有出現的項目，屬於那一種五行，再由該五行的本卦取得預設的六親和納甲的排序，再把該項目獨立的找出來
			mainDataDict['hide_naGia_rank'] = naGiaRanking( naGia_inList = mainDataDict['hide_naGia'] , 														 	
															dayGanZiList = [ mainDataDict['dayGanZi'][-1],mainDataDict['dayGanZi'][0]], ## 日支，日干
															monthGanZiList = [ mainDataDict['monthGanZi'][-1],mainDataDict['monthGanZi'][0]] ## 月支，月干	 
															)


############################################################################################################################
############################################################################################################################

		if changeGua == baGuaItem.get( 'binary' ) : ## 變卦
			# print("變卦", baGuaItem.get( 'binary' ),baGuaItem.get( 'number' ) )
			
			## 卦編號1-64
			mainDataDict['change_number'] = baGuaItem.get( 'number' )
			
			## 上名 exp: 風火
			mainDataDict['change_up'] = baGuaItem.get( 'title' )
			
			## 下名 exp: 家人
			mainDataDict['change_dn'] = baGuaItem.get( 'body' )	

			## 卦名 exp: 風火家人
			# mainDataDict['change_title'] = baGuaItem.get( 'title' ) + baGuaItem.get( 'body' )
			mainDataDict['change_title'] = (lambda aa, bb: baGuaItem.get( 'title' ) + "為" + baGuaItem.get( 'body' ) if len(baGuaItem.get( 'title' ) + baGuaItem.get( 'body' )) == 2 else baGuaItem.get( 'title' ) + baGuaItem.get( 'body' ))("A", "B")
		

			## 外卦(上卦) exp: 巽
			mainDataDict['change_upGua'] =  baGuaItem.get( 'outGua' )
			
			## 內卦(下卦) exp: 離
			mainDataDict['change_dnGua'] = baGuaItem.get( 'inGua' ) 
			
			## 上下卦 exp: 巽離
			mainDataDict['change_inOutGua'] = baGuaItem.get( 'outGua' ) + baGuaItem.get( 'inGua' ) 
			
			## 五行屬性 exp: 木 
			mainDataDict['change_rowType'] = baGuaItem.get( 'rowType' )

			## 屬於那一個八卦( 乾，兌，離，震....)
			mainDataDict['change_rowHead'] = next((d["head"] for d in typeDict if mainDataDict['change_title'] in d["item"]), None)		

			## 卦在屬性中的排序 exp: 歸魂
			mainDataDict['change_sort'] = baGuaItem.get( 'sort' )
			
			## 世爻 exp: 2 (由下往上數1-5)
			mainDataDict['change_shiYao'] = baGuaItem.get( 'shiYao' )
			
			## 應爻 exp: 5 (由下往上數1-5)
			mainDataDict['change_innYao'] = baGuaItem.get( 'innYao' )
			
			## 卦身 exp: 未
			mainDataDict['change_guaBody'] = baGuaItem.get( 'guaBody' ) 
			
			## 納甲 exp: ['丁巳', '丁卯', '丁丑', '癸丑', '癸亥', '癸酉']
			mainDataDict['change_naGia'] = baGuaItem.get( 'naGia' ) 

			## symbol
			mainDataDict['change_symbol'] = baGuaItem.get( 'symbol' ) 			


			## 空亡
			mainDataDict['change_kongWang'] = getKongWang( mainDataDict['dayGanZi' ] )
			
			## 空亡 exp: ['X', 'O', 'X', 'X', 'X', 'X']	
			mainDataDict['change_kongWangId'] = checkKongWang( baGuaItem.get( 'naGia' ) , mainDataDict['dayGanZi' ] )
			
			## 納甲五行 exp:['木', '土', '水', '土', '火', '木']
			mainDataDict['change_naGiaType'] = baGuaItem.get( 'naGiaType' )
			
			# ## 六親 exp:	['兄弟', '妻財', '父母', '妻財', '子孫', '兄弟']
			# mainDataDict['change_family'] = baGuaItem.get( 'family' )
			
			## 六獸 exp:	['玄武', '青龍', '朱雀', '勾陳', '螣蛇', '白虎']
			mainDataDict['change_sixAnimal'] = getSixAnimal( mainDataDict['dayGanZi' ] )

			# mainDataDict['change_mode'] =  baGuaItem.get( 'mode' ) ## 沖 or 合
			## 六沖 六合 無
			mainDataDict['change_mode'] = matchMode_dict.get( baGuaItem.get( 'mode' ))

			mainDataDict['change_naGia_rank'] = naGiaRanking( naGia_inList = mainDataDict['change_naGia'] ,
															dayGanZiList = [ mainDataDict['dayGanZi'][-1],mainDataDict['dayGanZi'][0]], ## 日支，日干
															monthGanZiList = [ mainDataDict['monthGanZi'][-1],mainDataDict['monthGanZi'][0]], ## 月支，月干	
															rankNum = True )

		# 六親 exp:	['兄弟', '妻財', '父母', '妻財', '子孫', '兄弟']


		mainDataDict['note'] = noteText
		if changeGua == "X":
			mainDataDict['mainGuaName'] = "%s卦"% ( mainDataDict['home_title'] )
		else:
			if mainDataDict['home_dn'] != None  and  mainDataDict['change_dn'] != None:	
				if (( mainDataDict['home_sort'] == "純卦" )  and  ( mainDataDict['change_sort']	== "純卦")):	
					mainDataDict['mainGuaName'] = "%s之%s卦"% (mainDataDict['home_up'],mainDataDict['change_up']	)					
					# print("---A")
				elif (( mainDataDict['home_sort'] == "純卦" )  and  ( mainDataDict['change_sort']	!= "純卦")):	
					mainDataDict['mainGuaName'] = "%s之%s卦"% (mainDataDict['home_up'],mainDataDict['change_dn']	)
					# print("---B")

				elif 	mainDataDict['change_sort']	== "純卦":	
					mainDataDict['mainGuaName'] = "%s之%s卦"% (mainDataDict['home_dn'],mainDataDict['change_up']	)
					# print("---C")
				else:
					mainDataDict['mainGuaName'] = "%s之%s卦"% (mainDataDict['home_dn'],mainDataDict['change_dn']	)
					# print("---D")


		# print ( mainDataDict['home_up']  )
		# print ( mainDataDict['change_up'])
	# print( "@@@@ ",mainDataDict['home_rowType']  )
	# print( "@@@@@ ",mainDataDict['change_naGia']  )
	# print( "@@@",mainDataDict['home_naGia'],mainDataDict['changeIdIndex'],mainDataDict['change_naGia'])

	# 三合局ID
	# mainDataDict["homeThreeHoId"],mainDataDict["changeThreeHoId"] =  checkThreeHo( dateGanZiList   = mainDataDict['home_naGia'],
	# 																				changeIdList =  mainDataDict['changeIdIndex'],
	# 																				changeNaGiaList = mainDataDict['change_naGia'] 	)   
# monthGanZi
# dayGanZi
# home_naGiaList
# changeIdList
# changeNaGiaList
# hide_naGia

# monthGanZi
# dayGanZi
# home_naGia
# changeIdIndex
# change_naGia
# hide_naGia

	mainDataDict["homeThreeHoId"],mainDataDict["changeThreeHoId"],mainDataDict["month_day_ThreeHoId"] = threeHoTest(
																													monthGanZi = mainDataDict[ "monthGanZi" ],			## 甲申
																													dayGanZi = mainDataDict[ "dayGanZi" ],				## 己未
																													home_naGia = mainDataDict[ "home_naGia" ],		## ['乙未', '乙巳', '乙卯', '壬午', '壬申', '壬戌']
																													changeIdIndex = mainDataDict[ "changeIdIndex" ],		## ['戊寅', '戊辰', '戊午', '辛未', '辛巳', '辛卯']
																													change_naGia = mainDataDict[ "change_naGia" ],	## ['X', 'O', 'X', 'O', 'X', 'X']
																													hide_naGia = mainDataDict[ "hide_naGia" ]			## ['甲子', 'X', 'X', 'X', 'X', 'X']
																													)
																													# monthGanZi, 
																													# dayGanZi, 
																													# home_naGia, 
																													# changeIdIndex, 
																													# change_naGia, 
																													# hide_naGia

	# print ( "三合:",mainDataDict["homeThreeHoId"],mainDataDict["changeThreeHoId"],mainDataDict["month_day_ThreeHoId"]  )

	# ['X', 'X', 'Oc', 'Oc', 'X', 'Oc'] ['X', 'X', 'X', 'Oc', 'X', 'Oc'] ['X', 'X']


	if mainDataDict['change_naGia'] != None:
		mainDataDict['change_family'] = checkFamilyType( mainDataDict['home_rowType']  , mainDataDict['change_naGia']  )[-1]	

# # 丑變辰，雖是進神，也有化墓之缺。
# forwardGod_Dict = { "亥":"子" , "寅":"卯" , "巳":"午" , "申":"酉" , "丑":"辰" , "辰":"未" , "未":"戌" , "戌":"丑" }

# # 退神
# # 動爻與變爻支形成子變亥、卯變寅、午變巳、酉變申。
# # 四庫土，由辰變丑、未變辰、戌變未、丑變戌。
# backGod_Dict =    { "子":"亥" , "卯":"寅" , "午":"巳" , "酉":"申" , "辰":"丑"  , "未":"辰", "戌":"未" , "丑":"戌" }


	if mainDataDict['change_naGia'] != None:
		naID = 0
		for each_naGia in mainDataDict['home_naGia']:

			if mainDataDict['change_naGia'][naID][1] == forwardGod_Dict.get(each_naGia[1]):
				print("FW")
				mainDataDict['home_forwardBack'][naID] = "FW"
			if mainDataDict['change_naGia'][naID][1] == backGod_Dict.get(each_naGia[1]):
				print("BK")
				mainDataDict['home_forwardBack'][naID] = "BK"

			naID += 1

		mainDataDict['vs_type'] = "%s>>%s"% (mainDataDict['home_rowType'],mainDataDict['change_rowType']	)

	## 取得所有的地支，判斷神煞是否秀出用
	mainDataDict['allDeeziList'] = getAllDeeZi( mainDataDict['home_naGia'], mainDataDict['hide_naGia'], mainDataDict['changeIdIndex'], mainDataDict['change_naGia'] )

	# # print(mainDataDict)
	# for e in mainDataDict.keys():
	# 	# print(e)
	# 	print( " %s%11s%s"% (e , " = ",mainDataDict[e]) )

	# print()
	# print()
	for e in mainDataDict.keys():
		if e in [ "monthGanZi", "dayGanZi", "changeIdIndex", "home_naGia", "hide_naGia", "change_naGia" ]:
			print( " %s%s%s"% (e , " = ",mainDataDict[e]) )

	print()
	for e in mainDataDict.keys():
		if e in [ "homeThreeHoId", "changeThreeHoId", "month_day_ThreeHoId" ]:
			print( " %s%s%s"% (e , " = ",mainDataDict[e]) )



	return mainDataDict
  




if __name__ == '__main__':
	# sixYaoMain( "27,71,42//占今年幾時換工作較好" )
	# mainFunction(  "010@X0" , user_mouthZi = "寅月" , user_dayGanZi = "辛酉日" )
	# mainFunction(  "111X01"  )

	# for e in loopMaker( "01@X" , 6 ):
	# 	mainFunction( e )

	mainFunction( "X001$0")
	# mainFunction( "1,0,11,0,00,1@2024 12 5 10 31@樂透會不會中獎?")
	# mainFunction( "1,0,11,0,00,1@乙月,丙子日@樂透會不會中獎?")

# combineData( "0,1,00,11,0,1@乙月,丙子日@占今年幾時換工作較好" )
# combineData( "0,1,00,11,0,1@2024 12 5 10 31@占今年幾時換工作較好" )
# combineData( "0,1,00,11,0,1@占今年幾時換工作較好" )
# combineData( "0,1,00,11,0,11" )
# 0,1,00,11,0,1@乙月,丙子日@占今年幾時換工作較好
# 0,1,00,11,0,1@2024 12 5 10 31@占今年幾時換工作較好














