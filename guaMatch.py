
# print( baGuaAllDict )

# 【易經六十四卦】
# 乾宮八卦俱屬金：    
# 乾為天、天風姤、天山遯、天地否、風地觀、山地剝、火地晉、火天大有        
# 坎宮八卦俱屬水：    
# 坎為水、水澤節、水雷屯、水火既濟、澤火革、雷火豐、地火明夷、地水師        
# 艮宮八卦俱屬土：    
# 艮為山、山火賁、山天大畜、山澤損、火澤睽、天澤履、風澤中孚、風山漸    
# 震宮八卦俱屬木：    
# 震為雷、雷地豫、雷水解、雷風恆、地風升、水風井、澤風大過、澤雷隨        
# 巽宮八卦俱屬木：    
# 巽為風、風天小畜、風火家人、風雷益、天雷無妄、火雷噬嗑、山雷頤、山風蠱
# 離宮八卦俱屬火：    
# 離為火、火山旅、火風鼎、火水未濟、山水蒙、風水渙、天水訟、天火同人
# 坤宮八卦俱屬土：    
# 坤為地、地雷復、地澤臨、地天泰、雷天大壯、澤天夬、水天需、水地比    
# 兌宮八卦俱屬金：    
# 兌為澤、澤水困、澤地萃、澤山咸、水山蹇、地山謙、雷山小過、雷澤歸妹
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



## baGuaAllDict   周易六十四卦 
# 'number' --------第幾卦
# 'title' ---------卦名
# 'body' ----------組合代號
# 'outGua' --------外卦(上)
# 'inGua' ---------內卦(下)
# 'rowType' --------屬性宮位五行
# 'sort' -----------第幾爻
# 'shiYao' ---------世爻
# 'innYao' ---------應爻
# 'guaBody' --------卦身
# 'naGia' ----------納甲
# 'naGiaType' --------納甲五行
# 'family' --------六親
# 'binary' --------卦(由上而下)

#納音
naVoice = {
		"甲子":"海中金" ,"丙寅":"爐中火",
		"乙丑":"海中金" ,"丁卯":"爐中火",

		"戊辰":"大林木" ,"庚午":"路傍土",
		"己巳":"大林木" ,"辛未":"路傍土",

		"壬申":"劍鋒金" ,"甲戌":"山頭火",
		"癸酉":"劍鋒金" ,"乙亥":"山頭火",

		"丙子":"澗下水" ,"戊寅":"城頭土",
		"丁丑":"澗下水" ,"己卯":"城頭土",

		"庚辰":"白蠟金" ,"壬午":"楊柳木",
		"辛巳":"白蠟金" ,"癸未":"楊柳木",

		"甲申":"泉中水" ,"丙戌":"屋上土",
		"乙酉":"泉中水" ,"丁亥":"屋上土",

		"戊子":"霹靂火" ,"庚寅":"松柏木",
		"己丑":"霹靂火" ,"辛卯":"松柏木",

		"壬辰":"長流水" ,"甲午":"砂中金",
		"癸巳":"長流水" ,"乙未":"砂中金",

		"丁申":"山下火" ,"戊戌":"平地木",
		"丁酉":"山下火" ,"己亥":"平地木",

		"庚子":"壁上土" ,"壬寅":"金箔金",
		"辛丑":"壁上土" ,"癸卯":"金箔金",

		"甲辰":"覆燈火" ,"丙午":"天河水",
		"乙巳":"覆燈火" ,"丁未":"天河水",

		"戊申":"大驛土" ,"庚戌":"釵釧金",
		"己酉":"大驛土" ,"辛亥":"釵釧金",

		"壬子":"桑柘木" ,"甲寅":"大溪水",
		"癸丑":"桑柘木" ,"乙卯":"大溪水",

		"丙辰":"沙中土" ,"戊午":"天上火",
		"丁巳":"沙中土" ,"己未":"天上火",

		"庚申":"石榴木" ,"壬戌":"大海水",
		"辛酉":"石榴木" ,"癸亥":"大海水",
		}



# 過濾取出發動的爻,@-老陽  X-老陰
def checkMainData( inputData ="11@0X@"  ):
	# inputData ="1,0,11,0,00,1@樂透會不會中獎?" 
	inputData = inputData.replace( "$" , "@")
	org_Gua = ""
	new_Gua = ""
	change_index = 1
	changeGuide = []
	# inputData ="11@0X@" 
	outputDataList = []

	for yoo in inputData: 
		outputDataList.append(yoo)
		if yoo == "@":
			org_Gua += "1"
			new_Gua += "0"
			# print( "老陽:", change_index ,"爻")
			changeGuide.append( "O" )

		elif yoo == "X":
			org_Gua += "0"
			new_Gua += "1"
			# print( "老陰:" , change_index ,"爻" )
			changeGuide.append( "O" )

		else:
			org_Gua += yoo		
			new_Gua += yoo
			changeGuide.append( "X" )			
		change_index += 1

	# print ( "本卦:" , org_Gua )
	# print ( "變卦:" , new_Gua )
	# print ( "guide:" , changeGuide ,outputDataList)
	# % 正常
	# $ 變爻
	return org_Gua , new_Gua , changeGuide , outputDataList
	# ('111001', '110010', ['X', 'X', 'O', 'X', 'O', 'O'], ['1', '1', '@', '0', 'X', '@'])




# 取得六獸

# 六獸歌
# 甲乙起青龍,丙丁起朱雀,戊日起勾陳,己日起騰蛇,庚辛起白虎,
# 壬癸起玄武。

# 注意 對照天干為日天干,由下往上

def getSixAnimal( day_ganZi = "壬戌" ):

	day_tanGan = day_ganZi[0] # 只需天干
	print( "取得六獸的天干 - ",day_tanGan)
	sixAnimal_list = ["龍","雀","勾","蛇","虎","玄"]                 ## 由下往上排
	# sixAnimal_list = ["青龍","朱雀","勾陳","螣蛇","白虎","玄武"]	
	if day_tanGan in "甲乙":
		listBuf = sixAnimal_list
	if day_tanGan in "丙丁":
		listBuf = sixAnimal_list[1:] + sixAnimal_list[:1] 
	if day_tanGan in "戊":
		listBuf = sixAnimal_list[2:] + sixAnimal_list[:2] 
	if day_tanGan in "己":
		listBuf = sixAnimal_list[3:] + sixAnimal_list[:3] 
	if day_tanGan in "庚辛":
		listBuf = sixAnimal_list[4:] + sixAnimal_list[:4] 
	if day_tanGan in "壬癸":
		listBuf = sixAnimal_list[5:] + sixAnimal_list[:5] 
	# print( day_tanGan , listBuf )
	return listBuf
# getSixAnimal()

## 找出沒有出現的六親
def checkNon( in_list ): ## 輸入現有的六親，再和全部都有的六親比對，列出缺少的六親項目
	# in_list = ['父母','兄弟','官鬼']
	sixAnimal_list = ['父母','兄弟','官鬼', '妻財','子孫']
	backItemList = []

	for in_buf in sixAnimal_list:
		if in_buf not in in_list:
			# print(in_buf )
			backItemList.append( in_buf )
	return backItemList


## 找出干支的空亡, 需要日干支

def getKongWang( checkGanZi = ""):
	# checkGanZi = "辛未"
	# print(checkGanZi )
	kongWang_list = [
		{ "name" : "甲子,乙丑,丙寅,丁卯,戊辰,己巳,庚午,辛未,壬申,癸酉" , "kongWang" : "戌亥" },
		{ "name" : "甲戌,乙亥,丙子,丁丑,戊寅,己卯,庚辰,辛巳,壬午,癸未" , "kongWang" : "申酉" },
		{ "name" : "甲申,乙酉,丙戌,丁亥,戊子,己丑,庚寅,辛卯,壬辰,癸巳" , "kongWang" : "午未" },
		{ "name" : "甲午,乙未,丙申,丁酉,戊戌,己亥,庚子,辛丑,壬寅,癸卯" , "kongWang" : "辰巳" },
		{ "name" : "甲辰,乙巳,丙午,丁未,戊申,己酉,庚戌,辛亥,壬子,癸丑" , "kongWang" : "寅卯" },
		{ "name" : "甲寅,乙卯,丙辰,丁巳,戊午,己未,庚申,辛酉,壬戌,癸亥" , "kongWang" : "子丑" } 
		]
	for gz in kongWang_list:
		if checkGanZi in gz.get("name"):
			# print( "空亡:" + gz["kongWang"] )
			return gz["kongWang"]










## 納甲旺衰
# def naGiaRanking( naGia_inList = ["丙子", "丙丑", "丙寅", "丙卯", "丙辰"], dateGanZiList = ["丁","午"] , changeIdList = ['O', 'X', 'O', 'X', 'X', 'X'] , changeNaGiaList = ['丁巳', '丁卯', '丁丑', '癸丑', '癸亥', '癸酉']  , rankNum = True ):
# 									##納甲list									月支日支(月干也行)						變卦的ID														變卦的納甲

def naGiaRanking( naGia_inList = ["丙子", "丙丑", "丙寅", "丙卯", "丙辰"], dayGanZiList =  ["丁","丑"],  monthGanZiList = ["癸","丑"] , rankType = None , rankNum = True ):
# 									##納甲list									月支月干						日支日干				 ## 本卦以home為標籤        是否列出生剋的分數					

	filter_dizhi = lambda lst: [x for x in lst if x in "子丑寅卯辰巳午未申酉戌亥"]

	dayGanZiList = filter_dizhi( dayGanZiList )       ## 取出日的地支
	monthGanZiList = filter_dizhi( monthGanZiList )   ## 取出月的地支

	dateGanZiList = monthGanZiList + dayGanZiList


	## 六沖
	anti_dict =  { "子":"午" ,  "丑":"未" , "寅":"申" , "卯":"酉" , "辰":"戌" , "巳":"亥" , "午":"子" , "未":"丑" , "申":"寅" , "酉":"卯" , "戌":"辰" , "亥":"巳"}



	"子酉申亥辰戌丑未"

	## 六合
	match_dict =  { "子":"丑" , "寅":"亥" , "卯":"戌" , "辰":"酉" , "巳":"申" , "午":"未" , "未":"午" , "申":"巳" , "酉":"辰" , "戌":"卯" , "亥":"寅" , "丑":"子" }


	# 定義十二地支及其五行屬性
	deeZhi_type = {
		"子": "水", "丑": "土", "寅": "木", "卯": "木", "辰": "土", 
		"巳": "火", "午": "火", "未": "土", "申": "金", "酉": "金", 
		"戌": "土", "亥": "水"
	}

	# 定義天干及其五行屬性
	tanGan_type = {
		"甲": "木", "乙": "木", "丙": "火", "丁": "火", "戊": "土",
		"己": "土", "庚": "金", "辛": "金", "壬": "水", "癸": "水"
	}

	# 定義五行相生相剋規則
	wushi_relationship = {
		## 比和 +4
		("木", "木"): 4,  # 比和
		("火", "火"): 4,  # 比和
		("土", "土"): 4,  # 比和
		("金", "金"): 4,  # 比和
		("水", "水"): 4,  # 比和

		## 被生 +3
		("木", "火"): 3,  # 木生火  A生B
		("火", "土"): 3,  # 火生土  A生B
		("土", "金"): 3,  # 土生金  A生B
		("金", "水"): 3,  # 金生水  A生B
		("水", "木"): 3,  # 水生木  A生B

		## 生別人 -2
		("火", "木"): 0, # B生A
		("土", "火"): 0, # B生A
		("金", "土"): 0, # B生A
		("水", "金"): 0, # B生A
		("木", "水"): 0, # B生A

		## 剋別人 -2
		("土", "木"): 0,  # B剋A
		("金", "火"): 0,  # B剋A
		("水", "土"): 0,  # B剋A
		("木", "金"): 0,  # B剋A
		("火", "水"): 0,  # B剋A

		## 被剋 -4
		("木", "土"): -3,  # 木剋土  A剋B
		("火", "金"): -3,  # 火剋金  A剋B
		("土", "水"): -3,  # 土剋水  A剋B
		("金", "木"): -3,  # 金剋木  A剋B
		("水", "火"): -3,  # 水剋火  A剋B

	}
	result = []
	anti_star = ""
	match_star = ""

	for naGia in naGia_inList:
		anti_star = ""
		match_star = ""			
		if naGia == "X":
			result.append( "X" )
			continue

		totalRank = 0
		for dateGanZi in dateGanZiList:
			## 納甲五行
			gia_typeBuf = deeZhi_type.get( naGia[-1] ) ## 取得五行屬性 ("丙子", "丙丑", "丙寅" -> "子", "丑", "寅")
			## 日月五行
			date_typeBuf = deeZhi_type.get( dateGanZi ) ## 取得日柱月柱五行屬性 卯->木

			#日或月入爻
			if naGia[-1] == dateGanZi: ## 日或月和爻支相同，也就是日辰或月建入爻，超旺
				rankBuf = 5

			else:
				rankBuf = wushi_relationship.get( ( date_typeBuf , gia_typeBuf) )


			if ( type( rankBuf ).__name__ ==  'int' ):
				totalRank += rankBuf ## 加總分數

			# 如果納甲的地支，等於日月相衝
			if naGia[-1] == anti_dict.get( dateGanZi ):
				if naGia[-1] in "子酉申亥辰戌丑未":
					totalRank -= 3
					
				## 月沖
				if ( dateGanZi not in dayGanZiList ) and ( dateGanZi in monthGanZiList ): ## 判斷日沖月沖狀態
					anti_star = "ˣ"  # *ᴹ   ˣ          月沖


				## 日沖
				elif ( dateGanZi in dayGanZiList ) and ( dateGanZi not in monthGanZiList ):

					if rankType == "home": ## 如發生在本卦
						anti_star = "^" ##ᴰ *✝⚠︎☖^ᴿᴵᴾ  日沖
					else:
						anti_star = "ˣ"  # ˣᴹ             日沖

				## 雙衝		
				elif ( dateGanZi in dayGanZiList ) and ( dateGanZi in monthGanZiList ): ## 日月都沖
					anti_star = "ˣˣ"#ϟ

			# 與日月合
			if naGia[-1] == match_dict.get( dateGanZi ): ## 日合月合狀態
				match_star = "ᵒ" # °°°º


		if  rankNum == True:
			if totalRank >= 0: ## ⁺⁻°'³㊂③‼︎!
				totalRank = "+" + str( totalRank ) + match_star + anti_star
			else:
				totalRank = str( totalRank )  + match_star + anti_star
		else:
			totalRank = match_star + anti_star


		print( ">>" , totalRank )
		result.append( totalRank )
	return result








def checkSameItem( dateGanZiBuf = ["子", "申", "亥", "卯", "辰","未"] , orgHomeList =[ "-","-","-","-","-","-"] , orgChangeList =[ "-","-","-","-","-","-"]  ):
	homeGuideList = [ "X" , "X" , "X" , "X" , "X" , "X" ] 
	changeGuideList = [ "X" , "X" , "X" , "X" , "X" , "X" ] 
	threeHo_dict = {
		"木": [ "亥","卯","未" ],  
		"火": [ "寅","午","戌" ],  
		"金": [ "巳","酉","丑" ],  
		"水": [ "申","子","辰" ]
		}
	mode = ""
# 
	# print( ">>---",homeGuideList )
	print( "全部加入比對 - ",dateGanZiBuf )
	# print("====================================================================================")
	for key, values in threeHo_dict.items():
		common_elements = list(set(dateGanZiBuf) & set(values))
		# print ( len(common_elements) )
		if len(common_elements) >= 3: ## 如果同一個屬性超過三個
			print( key , common_elements )

			print(orgHomeList,orgChangeList)
			indexList = [orgHomeList.index(item) for item in common_elements if item in orgHomeList]
			indexChangeList = [orgChangeList.index(item) for item in common_elements if item in orgChangeList]

			print( ">>>changeGuide - ",changeGuideList )		# print( ">>>",homeGuideList , indexList )
			print( indexChangeList)
			for ind in indexList:
				homeGuideList[ ind ] = "O"
			for ind in indexChangeList:
				changeGuideList[ ind ] = "O"

			# print( orgHomeList , indexList )## [2, 5, 3])


			print( "homeGuide - ",homeGuideList )
			print( "changeGuide - ",changeGuideList )

			print("====================================================================================")
	return homeGuideList,changeGuideList




















# 引數為下列
# monthGanZi = "甲申"   or   monthGanZi = "申月"   月干支
# dayGanZi = "丙辰"	                             日干支

# dateGanZiList = ["丙午", "丙戌", "丙寅", "丙卯", "丙亥","丙未"]     本爻納甲，一到六爻內容 
# changeIdList = ['O', 'O', 'D', 'X', 'X', 'X']                     發動爻為O，未發動為X，暗動為D
# changeNaGiaList = ['丁巳', '丁卯', '丁戌', '癸丑', '癸亥', '癸酉']  動爻納甲
# hide_naGia =  ['己卯', 'X', '己亥', 'X', 'X', 'X']                 伏藏格式


# 原則:
# 比對的目標: 日支，月支，本爻六個地支，伏神，動爻的發動爻地支(暗動的爻沒有動爻)，也就是['O', 'O', 'D', 'X', 'X', 'X']中O的才算，D只看本爻
# threeHo_dict = {
# 	"木": [ "亥","卯","未" ],  
# 	"火": [ "寅","午","戌" ],  
# 	"金": [ "巳","酉","丑" ],  
# 	"水": [ "申","子","辰" ]
# 	}
# 三合的原則就是如果地符合這個字典中任一個組合，三合的狀態就成立，但現在容許值加大一點
# 就是只要符合三合組合中的兩個，就算成立，最後傳回下面三個數值,



# 木 → Oa / Pa / Xa

# 火 → Ob / Pb / Xb

# 金 → Oc / Pc / Xc

# 水 → Od / Pd / Xd

# 傳回
# homeSanHo_GuideList  ['O', 'X', 'P', 'X', 'O', 'X']    本爻標記，O為三合，X為非三合，P為三合之一但未發動，待用狀態
# changeSanHo_GuideList  ['X', 'X', 'X', 'X', 'X', 'O']  動爻標記  O為變爻中符合三合的地支
# month_day_GuideList [ "O" , "X"]                       月和日的標記[ 月,日 ] 

# 加上四種屬性之後，Oa Ob Oc Od Pa Pb Pc Pd 
# X代表未標記，不需要增加屬性


# 例如:
# monthGanZi = "甲申"
# dayGanZi = "戊戌"
# dateGanZiList = ["丙子", "丙戌", "丙寅", "丙卯", "丙辰","丙未"] 
# changeIdList = ['O', 'O', 'D', 'X', 'X', 'X']  
# changeNaGiaList = ['丁巳', '丁卯', '丁戌', '癸丑', '癸亥', '癸酉']
# hide_naGia = ['己卯', 'X', '己亥', 'X', 'X', 'X'] 伏藏格式

# 得 申子辰 水局
# month_day_GuideList [ "Od" , "X"]  
# homeSanHo_GuideList  ['Od', 'X', 'X', 'X', 'Od', 'X']
# changeSanHo_GuideList  ['X', 'X', 'X', 'X', 'X', 'X']




# monthGanZi = "乙巳"
# dayGanZi = "丙辰"
# dateGanZiList = ["丙子", "丙戌", "丙寅", "丙亥", "丙申","丙未"] 
# changeIdList = ['X', 'X', 'D', 'X', 'O', 'O']  
# changeNaGiaList = ['丁酉', '丁子', '丁戌', '癸卯', '癸亥', '癸酉']
# hide_naGia = ['X', 'X', '己亥', 'X', 'X', 'X']

# 得 亥卯未缺卯
# month_day_GuideList [ "X" , "X"]  
# homeSanHo_GuideList  ['X', 'X', 'X', 'X', 'X', 'O']
# changeSanHo_GuideList  ['X', 'X', 'X', 'X', 'O', 'X']






# def check_sanhe( monthGanZi, dayGanZi, dateGanZiList, changeIdList, changeNaGiaList ):
#     threeHo_dict = {
#         "木": ["亥", "卯", "未"],
#         "火": ["寅", "午", "戌"],
#         "金": ["巳", "酉", "丑"],
#         "水": ["申", "子", "辰"]
#     }

#     # 取地支（只留最後一字）
#     month_branch = monthGanZi[-1]
#     day_branch = dayGanZi[-1]
#     home_branches = [x[-1] for x in dateGanZiList]
#     change_branches = [
#         b[-1] if changeIdList[i] == "O" else None
#         for i, b in enumerate(changeNaGiaList)
#     ]

#     # 找出成立的三合組合（地支集合）
#     sanhe_sets = []
#     for group in threeHo_dict.values():
#         count = sum(branch in group for branch in [month_branch, day_branch] + home_branches + [b for b in change_branches if b])
#         if count >= 2:
#             sanhe_sets.append(group)

#     # 標記用的函數
#     def mark(branch, in_change=False):
#         for group in sanhe_sets:
#             if branch in group:
#                 # 若 group 中已有兩個命中 → O
#                 hits = sum(x in group for x in [month_branch, day_branch] + home_branches + [b for b in change_branches if b])
#                 if hits >= 2:
#                     return "O"
#                 else:
#                     return "P" if not in_change else "X"
#         return "X"

#     # 月、日
#     month_day_GuideList = [mark(month_branch), mark(day_branch)]

#     # 本爻
#     homeSanHo_GuideList = [mark(b) for b in home_branches]

#     # 動爻（只標記 changeIdList == "O" 的）
#     changeSanHo_GuideList = [
#         mark(change_branches[i], in_change=True) if changeIdList[i] == "O" else "X"
#         for i in range(len(changeIdList))
#     ]

#     return homeSanHo_GuideList, changeSanHo_GuideList, month_day_GuideList














## 檢查是否存在三合局, 之後會加入暗動和日月的判斷(未完成)
def checkThreeHo( dateGanZiList = ["丙午", "丙戌", "丙寅", "丙卯", "丙亥","丙未"] , changeIdList = ['O', 'O', 'D', 'X', 'X', 'X'] , changeNaGiaList = ['丁巳', '丁卯', '丁戌', '癸丑', '癸亥', '癸酉']  ):

	print( dateGanZiList,changeNaGiaList)
	if dateGanZiList== None:
		dateGanZiList = [ "-","-","-","-","-","-" ]

	if changeNaGiaList == None:
		changeNaGiaList = [ "-","-","-","-","-","-" ]
	dateZiBuf = [item[1:] for item in dateGanZiList ]     ## 去掉第一個字，留下後面的地支
	changeZiBuf = [item[1:] for item in changeNaGiaList ] ## 去掉第一個字，留下後面的地支

	dateGanZiBuf = [item for item, flag in zip( dateZiBuf, changeIdList) if flag == 'O']     ## 取得有發動的本爻的納甲
	changeNaGiaBuf = [item for item, flag in zip(changeZiBuf, changeIdList) if flag == 'O'] ## 取得有發動的變爻的納甲
	
	homeSanHoBuf,changeSanHoBuf = checkSameItem( dateGanZiBuf = dateGanZiBuf , orgHomeList = dateZiBuf   )  ## 本爻的發動爻，回傳標示用指引 ['O', 'O', 'O', 'X', 'X', 'O'] 

	homeSanHoGuideList   = [ "X" , "X" , "X" , "X" , "X" , "X" ]
	changeSanHoGuideList = [ "X" , "X" , "X" , "X" , "X" , "X" ]

	## 把 ['X', 'X', 'X', 'O', 'X', 'O']['O', 'X', 'X', 'X', 'X', 'O']取出O的交集['O', 'X', 'X', 'O', 'X', 'O']
	homeSanHoGuideList   = ['O' if a == 'O' or b == 'O' else 'X' for a, b in zip( homeSanHoGuideList, homeSanHoBuf)]   
	changeSanHoGuideList = ['O' if a == 'O' or b == 'O' else 'X' for a, b in zip( changeSanHoGuideList, changeSanHoBuf)]	

	if changeIdList[0] == "O"  and   changeIdList[2] == "O": ## 1,3爻發動時
		print("1//3")

		homeYao_A = dateZiBuf[0]
		homeYao_B = dateZiBuf[2]
		changeYao_A = changeZiBuf[0]
		changeYao_B = changeZiBuf[2]

		dnList = [ dateZiBuf[0],changeZiBuf[0],dateZiBuf[2],changeZiBuf[2] ]
		muteIdList = ['O', 'X', 'O', 'X', 'X', 'X'] 
		homeSanHoBuf,changeSanHoBuf = checkSameItem( 
			dateGanZiBuf = dnList , 
			orgHomeList = [value if guide == 'O' else '-' for value, guide in zip(dateZiBuf, muteIdList )]  , 
			orgChangeList = [value if guide == 'O' else '-' for value, guide in zip(changeZiBuf, muteIdList	)]
			) 
		## 把 ['X', 'X', 'X', 'O', 'X', 'O']['O', 'X', 'X', 'X', 'X', 'O']取出O的交集['O', 'X', 'X', 'O', 'X', 'O']
		homeSanHoGuideList   = ['O' if a == 'O' or b == 'O' else 'X' for a, b in zip( homeSanHoGuideList, homeSanHoBuf)]
		changeSanHoGuideList = ['O' if a == 'O' or b == 'O' else 'X' for a, b in zip( changeSanHoGuideList, changeSanHoBuf)]

	if changeIdList[3] == "O"  and   changeIdList[5] == "O": ## 1,3爻發動時
		print("4//6")

		homeYao_A = dateZiBuf[3]
		homeYao_B = dateZiBuf[5]
		changeYao_A = changeZiBuf[3]
		changeYao_B = changeZiBuf[5]

		dnList = [ dateZiBuf[3],changeZiBuf[3],dateZiBuf[5],changeZiBuf[5] ]
		muteIdList = ['X', 'X', 'X', 'O', 'X', 'O'] 
		homeSanHoBuf,changeSanHoBuf = checkSameItem( 
			dateGanZiBuf = dnList , 

							##["丙午", "丙戌", "丙寅", "丙卯", "丙亥", "丙未"] ['O', 'X', 'O', 'X', 'X', 'X'] to  ['丙午', '-', '丙寅', '-', '-', '-']
			orgHomeList = [value if guide == 'O' else '-' for value, guide in zip(dateZiBuf, muteIdList )]  , 
			orgChangeList = [value if guide == 'O' else '-' for value, guide in zip(changeZiBuf, muteIdList	)]
			) 
		## 把 ['X', 'X', 'X', 'O', 'X', 'O']['O', 'X', 'X', 'X', 'X', 'O']取出O的交集['O', 'X', 'X', 'O', 'X', 'O']
		homeSanHoGuideList   = ['O' if a == 'O' or b == 'O' else 'X' for a, b in zip( homeSanHoGuideList, homeSanHoBuf)]
		changeSanHoGuideList = ['O' if a == 'O' or b == 'O' else 'X' for a, b in zip( changeSanHoGuideList, changeSanHoBuf)]

	return homeSanHoGuideList , changeSanHoGuideList
# print("### ",checkThreeHo())


##################################################################################################################
## 判斷變爻與本爻的關係，
#  "="比和  
#  ">"本爻生變爻   
#  ">!"本爻剋變爻    
#  "<"變爻生本爻(回頭生)    
#  "!<"變爻剋本爻(回頭剋)

# 地支五行對應
deeZhi_type = {
	"子": "水", "丑": "土", "寅": "木", "卯": "木", "辰": "土", 
	"巳": "火", "午": "火", "未": "土", "申": "金", "酉": "金", 
	"戌": "土", "亥": "水"
}

# 五行生剋判斷
def getWuXingRelation(from_elem, to_elem):
	if from_elem == to_elem:
		return "="
	elif (from_elem, to_elem) in [("木", "火"), ("火", "土"), ("土", "金"), ("金", "水"), ("水", "木")]:
		return ">"     # from 生 to
	elif (from_elem, to_elem) in [("木", "土"), ("火", "金"), ("土", "水"), ("金", "木"), ("水", "火")]:
		return ">!"    # from 剋 to
	elif (to_elem, from_elem) in [("木", "火"), ("火", "土"), ("土", "金"), ("金", "水"), ("水", "木")]:
		return "<"     # to 生 from（change 生 home）
	elif (to_elem, from_elem) in [("木", "土"), ("火", "金"), ("土", "水"), ("金", "木"), ("水", "火")]:
		return "!<"    # to 剋 from（change 剋 home）
	else:
		return "0"     # 無關係

# 比較單一 home 與 change 的生剋關係
def getRelation(home_na, change_na):
	home_branch = home_na[1]
	change_branch = change_na[1]
	home_elem = deeZhi_type.get(home_branch)
	change_elem = deeZhi_type.get(change_branch)
	
	if not home_elem or not change_elem:
		return "?"

	return getWuXingRelation(home_elem, change_elem)

# 主功能函數
def getRelationFun(changeIdIndex, home_naGia, change_naGia):
	resultData = []
	for idx, flag in enumerate(changeIdIndex):
		if flag == "X":
			resultData.append("X")
		else:
			relation = getRelation(home_naGia[idx], change_naGia[idx])
			resultData.append(relation)

	print(resultData)
	return resultData



# 三合關係辨識函式
# monthGanZi      -------  甲申
# dayGanZi        -------  己未
# home_naGia      -------  ['乙未', '乙巳', '乙卯', '壬午', '壬申', '壬戌']
# change_naGia    -------  ['戊寅', '戊辰', '戊午', '辛未', '辛巳', '辛卯']
# changeIdIndex   -------  ['X', 'O', 'X', 'O', 'X', 'X']
# hide_naGia      -------  ['甲子', 'X', 'X', 'X', 'X', 'X']


# def threeHoTest(monthGanZi, dayGanZi, home_naGiaList, changeIdList, changeNaGiaList, hide_naGia):
#     """
#     三合判斷函數 - 三層級標記版
    
#     參數：
#         monthGanZi: 月干支，如 "甲申" 或 "申月"
#         dayGanZi: 日干支，如 "丙辰"
#         home_naGiaList: 本爻納甲，六爻內容
#         changeIdList: 發動標記 ['O', 'O', 'D', 'X', 'X', 'X']
#         changeNaGiaList: 動爻納甲
#         hide_naGia: 伏藏，如 ['己卯', 'X', '己亥', 'X', 'X', 'X']
    
#     回傳：
#         homeThreeHoId, changeThreeHoId, monty_day_ThreeHoId
        
#     標記規則（優先級順序）：
#         O標記：完整三合（≥3個地支） - 最高優先級
#         P標記：缺一三合（2個地支 + 靜爻中有缺失地支 + 無月支參與） - 中優先級  
#         H標記：缺一三合（2個地支 + 靜爻中無缺失地支 + 無月支參與） - 最低優先級
        
#     優先級規則：有O就不標P和H，有P就不標H，都沒有才標H
#     """
    
#     # 三合對照表，優先順序 木a → 火b → 金c → 水d
#     threeHo_dict = {
#         "木": ["亥", "卯", "未"],  
#         "火": ["寅", "午", "戌"],  
#         "金": ["巳", "酉", "丑"],  
#         "水": ["申", "子", "辰"]
#     }
    
#     # 屬性對照表
#     element_code = {
#         "木": "a",
#         "火": "b", 
#         "金": "c",
#         "水": "d"
#     }
    
#     # 取得地支
#     def get_zhi(ganzi_str):
#         if ganzi_str == 'X':
#             return 'X'
#         if "月" in ganzi_str:
#             return ganzi_str[0]  # "申月" -> "申"
#         return ganzi_str[-1]  # "甲申" -> "申"
    
#     # 取得月支和日支
#     month_zhi = get_zhi(monthGanZi)
#     day_zhi = get_zhi(dayGanZi)
    
#     # 收集本爻地支
#     home_zhis = [get_zhi(gz) for gz in home_naGiaList]
    
#     # 收集伏神地支
#     hide_zhis = [get_zhi(h) if h != 'X' else 'X' for h in hide_naGia]
    
#     # 初始化結果列表
#     homeThreeHoId = ['X'] * 6
#     changeThreeHoId = ['X'] * 6
#     monty_day_ThreeHoId = ['X', 'X']
    
#     # 記錄已有標記的局
#     has_O_elements = set()
#     has_P_elements = set()
    
#     # 按優先順序處理每個三合局，先處理O標記
#     for element in ["木", "火", "金", "水"]:
#         group = threeHo_dict[element]
#         code = element_code[element]
        
#         # 收集各來源的地支和位置，按優先順序
#         sources = {
#             'active_home': [],  # 動爻/暗動 - 優先級1
#             'change': [],       # 變爻 - 優先級2
#             'day': None,        # 日支 - 優先級3
#             'month': None       # 月支 - 優先級3
#         }
        
#         # 1. 收集動爻/暗動地支
#         for i, status in enumerate(changeIdList):
#             if status in ['O', 'D'] and home_zhis[i] in group:
#                 sources['active_home'].append((home_zhis[i], 'home', i))
        
#         # 2. 收集變爻地支 (只看O)
#         for i, status in enumerate(changeIdList):
#             if status == 'O':
#                 change_zhi = get_zhi(changeNaGiaList[i])
#                 if change_zhi in group:
#                     sources['change'].append((change_zhi, 'change', i))
        
#         # 3. 收集日月地支
#         if day_zhi in group:
#             sources['day'] = (day_zhi, 'day', 1)
#         if month_zhi in group:
#             sources['month'] = (month_zhi, 'month', 0)
        
#         # 收集所有地支，按優先順序去重
#         all_sources = []
#         used_zhis = set()
        
#         # 按優先順序添加地支
#         for zhi, source_type, pos in sources['active_home']:
#             if zhi not in used_zhis:
#                 all_sources.append((zhi, source_type, pos))
#                 used_zhis.add(zhi)
        
#         for zhi, source_type, pos in sources['change']:
#             if zhi not in used_zhis:
#                 all_sources.append((zhi, source_type, pos))
#                 used_zhis.add(zhi)
        
#         if sources['day'] and sources['day'][0] not in used_zhis:
#             all_sources.append(sources['day'])
#             used_zhis.add(sources['day'][0])
        
#         if sources['month'] and sources['month'][0] not in used_zhis:
#             all_sources.append(sources['month'])
#             used_zhis.add(sources['month'][0])
        
#         # 判斷是否構成三合（O標記）
#         if len(used_zhis) >= 3:
#             # 構成三合，標記O
#             has_O_elements.add(element)
#             mark = f'O{code}'
            
#             for zhi, source_type, pos in all_sources:
#                 if source_type == 'home':
#                     homeThreeHoId[pos] = mark
#                 elif source_type == 'change':
#                     changeThreeHoId[pos] = mark
#                 elif source_type == 'day':
#                     monty_day_ThreeHoId[1] = mark
#                 elif source_type == 'month':
#                     monty_day_ThreeHoId[0] = mark
    
#     # 如果沒有任何O標記，才考慮P標記
#     if not has_O_elements:
#         for element in ["木", "火", "金", "水"]:
#             group = threeHo_dict[element]
#             code = element_code[element]
            
#             # 收集各來源的地支和位置，按優先順序
#             sources = {
#                 'active_home': [],
#                 'change': [],
#                 'day': None,
#                 'month': None
#             }
            
#             # 收集動爻/暗動地支
#             for i, status in enumerate(changeIdList):
#                 if status in ['O', 'D'] and home_zhis[i] in group:
#                     sources['active_home'].append((home_zhis[i], 'home', i))
            
#             # 收集變爻地支
#             for i, status in enumerate(changeIdList):
#                 if status == 'O':
#                     change_zhi = get_zhi(changeNaGiaList[i])
#                     if change_zhi in group:
#                         sources['change'].append((change_zhi, 'change', i))
            
#             # 收集日月地支
#             if day_zhi in group:
#                 sources['day'] = (day_zhi, 'day', 1)
#             if month_zhi in group:
#                 sources['month'] = (month_zhi, 'month', 0)
            
#             # 收集所有地支，按優先順序去重
#             all_sources = []
#             used_zhis = set()
            
#             for zhi, source_type, pos in sources['active_home']:
#                 if zhi not in used_zhis:
#                     all_sources.append((zhi, source_type, pos))
#                     used_zhis.add(zhi)
            
#             for zhi, source_type, pos in sources['change']:
#                 if zhi not in used_zhis:
#                     all_sources.append((zhi, source_type, pos))
#                     used_zhis.add(zhi)
            
#             if sources['day'] and sources['day'][0] not in used_zhis:
#                 all_sources.append(sources['day'])
#                 used_zhis.add(sources['day'][0])
            
#             if sources['month'] and sources['month'][0] not in used_zhis:
#                 all_sources.append(sources['month'])
#                 used_zhis.add(sources['month'][0])
            
#             # 判斷是否構成缺一（P標記）
#             if len(used_zhis) == 2:
#                 # 檢查是否有月支參與
#                 has_month = any(source_type == 'month' for _, source_type, _ in all_sources)
                
#                 if not has_month:
#                     # 找出缺少的地支
#                     missing_zhi = None
#                     for zhi in group:
#                         if zhi not in used_zhis:
#                             missing_zhi = zhi
#                             break
                    
#                     # 檢查缺少的地支是否在靜爻中存在
#                     missing_in_static = False
#                     missing_static_pos = []
                    
#                     if missing_zhi:
#                         for i, status in enumerate(changeIdList):
#                             # 只檢查靜爻(X狀態)
#                             if status == 'X' and home_zhis[i] == missing_zhi:
#                                 missing_in_static = True
#                                 missing_static_pos.append(i)
                    
#                     # 如果缺少的地支在靜爻中存在，標記P
#                     if missing_in_static:
#                         has_P_elements.add(element)
#                         mark = f'P{code}'
                        
#                         # 標記原有的2個地支
#                         for zhi, source_type, pos in all_sources:
#                             if source_type == 'home':
#                                 homeThreeHoId[pos] = mark
#                             elif source_type == 'change':
#                                 changeThreeHoId[pos] = mark
#                             elif source_type == 'day':
#                                 monty_day_ThreeHoId[1] = mark
                        
#                         # 標記靜爻中的缺少地支
#                         for pos in missing_static_pos:
#                             homeThreeHoId[pos] = mark
    
#     # 如果沒有任何O和P標記，才考慮H標記
#     if not has_O_elements and not has_P_elements:
#         for element in ["木", "火", "金", "水"]:
#             group = threeHo_dict[element]
#             code = element_code[element]
            
#             # 收集各來源的地支和位置，按優先順序
#             sources = {
#                 'active_home': [],
#                 'change': [],
#                 'day': None,
#                 'month': None
#             }
            
#             # 收集動爻/暗動地支
#             for i, status in enumerate(changeIdList):
#                 if status in ['O', 'D'] and home_zhis[i] in group:
#                     sources['active_home'].append((home_zhis[i], 'home', i))
            
#             # 收集變爻地支
#             for i, status in enumerate(changeIdList):
#                 if status == 'O':
#                     change_zhi = get_zhi(changeNaGiaList[i])
#                     if change_zhi in group:
#                         sources['change'].append((change_zhi, 'change', i))
            
#             # 收集日月地支
#             if day_zhi in group:
#                 sources['day'] = (day_zhi, 'day', 1)
#             if month_zhi in group:
#                 sources['month'] = (month_zhi, 'month', 0)
            
#             # 收集所有地支，按優先順序去重
#             all_sources = []
#             used_zhis = set()
            
#             for zhi, source_type, pos in sources['active_home']:
#                 if zhi not in used_zhis:
#                     all_sources.append((zhi, source_type, pos))
#                     used_zhis.add(zhi)
            
#             for zhi, source_type, pos in sources['change']:
#                 if zhi not in used_zhis:
#                     all_sources.append((zhi, source_type, pos))
#                     used_zhis.add(zhi)
            
#             if sources['day'] and sources['day'][0] not in used_zhis:
#                 all_sources.append(sources['day'])
#                 used_zhis.add(sources['day'][0])
            
#             if sources['month'] and sources['month'][0] not in used_zhis:
#                 all_sources.append(sources['month'])
#                 used_zhis.add(sources['month'][0])
            
#             # 判斷是否構成缺一（H標記）
#             if len(used_zhis) == 2:
#                 # 檢查是否有月支參與
#                 has_month = any(source_type == 'month' for _, source_type, _ in all_sources)
                
#                 if not has_month:
#                     # H標記：2個地支但靜爻中沒有缺失地支
#                     mark = f'H{code}'
                    
#                     # 只標記原有的2個地支
#                     for zhi, source_type, pos in all_sources:
#                         if source_type == 'home':
#                             homeThreeHoId[pos] = mark
#                         elif source_type == 'change':
#                             changeThreeHoId[pos] = mark
#                         elif source_type == 'day':
#                             monty_day_ThreeHoId[1] = mark
    
#     return homeThreeHoId, changeThreeHoId, monty_day_ThreeHoId


# # 測試範例 - 您提供的新案例
# print("=== 測試新案例 ===")
# homeSanHo2, changeSanHo2, monthDay2 = threeHoTest(
#     monthGanZi="戊辰",
#     dayGanZi="甲辰",  # 假設日干支，您可以提供正確的
#     home_naGiaList=['庚子', '庚寅', '庚辰', '辛未', '辛巳', '辛卯'],
#     changeIdList=['X', 'X', 'O', 'X', 'D', 'O'],
#     changeNaGiaList=['己卯', '己丑', '己亥', '戊申', '戊戌', '戊子'],
#     hide_naGia=['X', 'X', '辛酉', 'X', 'X', 'X']
# )
# print("homeThreeHoId  =", homeSanHo2)
# print("changeThreeHoId =", changeSanHo2) 
# print("monty_day_ThreeHoId  =", monthDay2)

# print("\n=== 新案例分析 ===")
# print("月支: 辰, 日支: 辰")  
# print("發動爻: 第3爻(辰->亥), 第6爻(卯->子)")
# print("暗動爻: 第5爻(巳)")
# print("\n本爻地支: 子, 寅, 辰, 未, 巳, 卯")
# print("變爻地支: 卯, 丑, 亥, 申, 戌, 子")
# print("\n三合分析:")
# print("木局(亥卯未): 亥(變爻) + 卯(本爻/動爻) + 未(靜爻) = 3個 → 但未在靜爻，應標記P")
# print("水局(申子辰): 子(本爻/變爻) + 辰(本爻/月日) = 2個，缺申但申不在靜爻 → 不標記")

# # 原測試範例 - 睽之臨卦
# print("\n=== 測試睽之臨卦 ===")
# homeSanHo1, changeSanHo1, monthDay1 = threeHoTest(
#     monthGanZi="戊戌",
#     dayGanZi="戊寅", 
#     home_naGiaList=['丁巳', '丁卯', '丁丑', '己酉', '己未', '己卯'],
#     changeIdList=['X', 'X', 'X', 'O', 'X', 'O'],
#     changeNaGiaList=['丁巳', '丁卯', '丁丑', '癸丑', '癸亥', '癸酉'],
#     hide_naGia=['X', 'X', 'X', 'X', '丙子', 'X']
# )
# print("homeThreeHoId  =", homeSanHo1)
# print("changeThreeHoId =", changeSanHo1) 
# print("monty_day_ThreeHoId  =", monthDay1)





    # # 測試範例 - 睽之臨卦
    # print("=== 測試睽之臨卦 ===")
    # homeSanHo1, changeSanHo1, monthDay1 = threeHoTest(
    #     monthGanZi="戊戌",
    #     dayGanZi="戊寅", 
    #     home_naGiaList=['丁巳', '丁卯', '丁卯', '己酉', '己未', '己卯'],
    #     changeIdList=    ['X',  'X',   'D',    'O',   'X',    'O'],
    #     changeNaGiaList=['丁巳', '丁卯', '丁丑', '癸丑', '癸亥', '癸酉'],
    #     hide_naGia=['X', 'X', 'X', 'X', '丙子', 'X']
    # )
    # print("homeThreeHoId  =", homeSanHo1)
    # print("changeThreeHoId =", changeSanHo1) 
    # print("monty_day_ThreeHoId  =", monthDay1)




if __name__ == '__main__':
	# print(naGiaRanking( ['X', '丑', '亥', '未', 'X', '卯']	 ))
	# print(naGiaRanking(	 ))
	# orgGua,changeGua,_,_ = checkMainData( "0011X11" )
	# print( orgGua,changeGua,_,_)


	# ✅ 測試資料
	changeIdIndex = ['X', 'O', 'X', 'O', 'X', 'O']
	home_naGia =    ['戊寅', '戊辰', '戊午', '丁亥', '丁酉', '丁未']
	change_naGia =  ['戊寅', '戊子', '戊午', '辛未', '辛巳', '辛卯']

	# 執行
	getRelationFun(changeIdIndex, home_naGia, change_naGia)