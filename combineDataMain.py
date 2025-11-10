# -*- coding: utf-8 -*-
from pil_draw_work_v01 import *
from notion_push import ( pushToNotion as notionPush_pushUp )

from flexLayout_tool import *
from mainFun import *
from sixYao_data import  * # baGuaAllDict 取得
from fourPillar_tool import fourPillarToDateMain # 四柱得日期
# from fourPillar_tool import getYear # 四柱得日期
from fourPillar_tool import getNowTime # 現時日期時間取得

# from  supabase_io import check_user_exists , get_user_data
# from opencc import OpenCC
import os



from dotenv import load_dotenv
load_dotenv()  # 載入 .env 檔案





# 全形轉半形
def strQ2B(ustring):
	rstring = ""
	for uchar in ustring:
			inside_code = ord(uchar)
			if inside_code == 12288:             # 全形空格直接轉換pip install opencc-python-reimplemented
					inside_code = 32
			elif 65281 <= inside_code <= 65374:  # 全形字元（除空格）根據關係轉化
					inside_code -= 65248
			rstring += chr(inside_code)
	return rstring




## 產生文字排卦
## 產生文字排卦
def format_gua_text(data):
	"""
	將卦象字典格式化為文字輸出
	
	Args:
		data: 卦象資料字典
	
	Returns:
		str: 格式化後的卦象文字
	"""
	# 基本資訊
	note = data['note']
	user_define = data['user_define']
	
	# 六親簡稱映射
	family_abbr = {
		'父母': '父',
		'子孫': '孫',
		'兄弟': '兄',
		'妻財': '財',
		'官鬼': '官'
	}
	
	# 構建輸出文字
	lines = []
	lines.append(f"占: {note}")
	
	# 根據 user_define 決定日期和四柱格式
	if user_define:
		# 自訂模式：只顯示月柱和日柱
		month_zi = data['user_mouthZi']
		day_ganzi = data['user_dayGanZi']
		# 取月柱最後一個字（地支）+ "月"
		month_display = month_zi[-1] + "月"
		day_display = day_ganzi + "日"
		lines.append(f"{month_display} | {day_display}")
	else:
		# 正常模式：顯示日期和完整四柱
		date = data['fullDate']
		year = data['yearGanZi']
		month = data['monthGanZi']
		day = data['dayGanZi']
		hour = data['hourGanZi']
		lines.append(f"{date}")
		lines.append(f"{year} | {month} | {day} | {hour}")
	
	gua_name = data['mainGuaName']
	kong_wang = data['home_kongWang']
	lines.append(f"{gua_name}        空:{kong_wang}")
	lines.append("= = = = = = = = = = = = =")
	
	# 世應位置
	shi_yao = int(data['home_shiYao'])
	yin_yao = int(data['home_innYao'])
	
	# 六爻資料（從下往上：index 0-5 對應初爻-上爻）
	six_animals = data['home_sixAnimal']
	families = data['home_family']
	na_gias = data['home_naGia']
	input_gua = data['inputGua']
	
	# 變爻資料
	change_index = data['changeIdIndex']
	change_na_gias = data['change_naGia'] if data['change_naGia'] else []
	change_families = data['change_family'] if data['change_family'] else []
	
	# 伏神資料
	hide_families = data['hide_family']
	hide_na_gias = data['hide_naGia']
	
	# 六爻（從上往下：index 5-0）
	for i in range(5, -1, -1):
		yao_idx = i + 1  # 實際爻位（1-6）
		
		# 伏神（4個字寬）
		if hide_families[i] != 'X':
			hide_dizhi = hide_na_gias[i][1] if len(hide_na_gias[i]) > 1 else hide_na_gias[i]
			hide_family = family_abbr.get(hide_families[i], hide_families[i])
			fu_shen = f"{hide_dizhi}{hide_family}"
		else:
			fu_shen = "　　"
		
		# 六神
		animal = six_animals[i]
		
		# 六親簡稱
		family = family_abbr.get(families[i], families[i])
		
		# 世應標記
		if yao_idx == shi_yao:
			shi_ying = '世'
		elif yao_idx == yin_yao:
			shi_ying = '應'
		else:
			shi_ying = '　'
		
		# 地支（只取納甲的地支部分）
		dizhi = na_gias[i][1] if len(na_gias[i]) > 1 else na_gias[i]
		
		# 爻的符號（根據 inputGua）
		input_val = input_gua[i]
		
		if input_val == '1':
			yao_symbol = '⚊'  # 陽爻
		elif input_val == '0':
			yao_symbol = '⚋'  # 陰爻
		elif input_val == '@':
			yao_symbol = '〇'  # 老陽(動爻,陽變陰)
		elif input_val == 'X':
			yao_symbol = '✕'  # 老陰(動爻,陰變陽)
		else:
			yao_symbol = '⚊'  # 預設陽爻
		
		# 變爻（只在有變化時顯示）
		if input_val in ['@', 'X'] and change_na_gias:
			change_dizhi = change_na_gias[i][1] if len(change_na_gias[i]) > 1 else change_na_gias[i]
			change_family = family_abbr.get(change_families[i], change_families[i])
			bian_yao = f"{change_dizhi}{change_family}"
		else:
			bian_yao = ""
		
		# 組合完整行
		line = f" {fu_shen}   {animal}|{family}  {yao_symbol}  {shi_ying}  {dizhi}  {bian_yao} "
		lines.append(line)
	
	lines.append("= = = = = = = = = = = = =")
	
	# 神煞
	horse = data['horse_po']
	flower = data['flower_po']
	yang_knife = data['yangKnife_po']
	helpful = data['helpful_po']
	
	lines.append(f"馬:{horse}  桃:{flower}  刃:{yang_knife}  貴:{helpful}")
	
	print('\n'.join(lines))
	return '\n'.join(lines)

# ⚋
# ⚊
# ✕
# 〇




## 轉換成簡單符號模式 //
## ========================================================================================================================================
def riceGua( fullDataInput ):	
	# print( fullDataInput )

	guaSort = {  1:"乾", 2:"兌", 3:"離", 4:"震", 5:"巽", 6:"坎", 7:"艮", 0:"坤" }## 八卦排序
	guaGuaDict = { "乾":"111" ,"兌":"110" ,"離":"101" ,"震":"100" ,"巽":"011" ,"坎":"010" ,"艮":"001" ,"坤":"000" } # 由下往上排，所以順序要顛倒


	mode = ""
	riceText = ""

	bufList = fullDataInput.split("/")

	if len( bufList ) == 3: ## ['20-30-40'] 米卦
		# riceList = fullDataInput.split("//")[0] ##['20', '30', '40']
		mode = "riceMode"
		downGua   =  int( bufList[0] ) % 8       ## 由下往上排
		upGua     =  int( bufList[1] ) % 8       ## 由下往上排
		changeGua =  int( bufList[2] ) % 6       ## 由下往上排
		if changeGua == 0:
			changeGua = 6

		allGua = guaGuaDict.get( guaSort.get( downGua ) ) + guaGuaDict.get( guaSort.get( upGua ) )
		index = 1
		outGua = ""
		for gua in allGua:
			if index == changeGua:
				if gua == "1":
					outGua += "$"
				if gua == "0":
					outGua += "X"
			else:
				outGua += gua
			index += 1

		downGua = int(str(downGua).replace("0","8")) 
		upGua = int(str(upGua).replace("0","8")) 
		return( outGua,"%d.%d.%d "%(downGua,upGua,changeGua) ) 

	elif len( bufList ) == 6: ## ['1,0,11,0,00,1'] 六爻卦
		outGua = fullDataInput.replace( ",","" ).replace( "00","X" ).replace( "11","$" ).replace( "/","" )
		return( outGua,"" )




# orgData = "去學習是否順 // 火地晉 5 // 丙月，丙子日"
# print(allItem)

import re

FULL2HALF = str.maketrans({
	"，": ",",  # 全形逗號 → 半形逗號
	"。": ".",  # 全形句號 → 半形句號
	"？": "?",  # 全形問號 → 半形問號
	"！": "!",  # 全形驚嘆號 → 半形驚嘆號
	"；": ";",  # 全形分號 → 半形分號
	"：": ":",  # 全形冒號 → 半形冒號
	"、": ",",  # 頓號 → 半形逗號
	"．": ".",  # 全形句點 → 半形句點
})

SEP_PATTERN = re.compile(r'[\s_\\;:；：．]+')

def _clean_subblock(s: str) -> str:
	"""清理單段落的小區塊文字"""
	s = s.translate(FULL2HALF).strip()
	
	# 🔥 新增：移除中文字之間的所有空白
	s = re.sub(r'([\u4e00-\u9fff])\s+([\u4e00-\u9fff])', r'\1\2', s)
	
	# ⭐ 把「中文 + 空白 + 逗號 + 空白 + 中文」的空白都收掉
	s = re.sub(r'([\u4e00-\u9fff])\s*,\s*([\u4e00-\u9fff])', r'\1,\2', s)
	
	# '-' 無空白 -> '/'
	s = re.sub(r'(?<!\s)-(?!\s)', '/', s)

	# '.' 無空白 -> '/'
	s = re.sub(r'(?<!\s)\.(?!\s)', '/', s)	
	
	# 逗號處理（重點）
	# 1. 數字/英文字母間的逗號 → '/'
	s = re.sub(r'(?<=[0-9A-Za-z]),(?=[0-9A-Za-z])', '/', s)
	# 2. 結尾逗號 → '/'
	s = re.sub(r',\s*$', '/', s)
	# 3. 中文後面接逗號，逗號後面不是中文 → '/'
	s = re.sub(r'(?<=[\u4e00-\u9fff]),(?![\u4e00-\u9fff])', '/', s)
	# 4. 逗號前面不是中文，後面是中文 → '/'
	s = re.sub(r'(?<![\u4e00-\u9fff]),(?=[\u4e00-\u9fff])', '/', s)
	
	# 其他雜項 -> '/'
	s = SEP_PATTERN.sub('/', s)
	
	# 尾巴句號刪除（只刪除句號，保留 ? !）
	s = re.sub(r'\.\s*$', '', s)
	
	# 合併多個 '/'
	s = re.sub(r'/+', '/', s)
	
	# 去掉段落首尾多餘 '/'
	s = s.strip('/ ')
	
	return s


# def unifiedData(orgData, strong_sep='//', sep_for_app=None):
# 	if not isinstance(orgData, str):
# 		return orgData
	
# 	# Step 1: 分段落（大區塊）
# 	STRONG_TOKEN = "STRONGSEPUNIQUE"
# 	# 保護原本的 //，換行，" - " 統一替代為 token
# 	s = orgData.replace(strong_sep, STRONG_TOKEN)
# 	s = re.sub(r'\s-\s', STRONG_TOKEN, s)
# 	s = re.sub(r'[\r\n]+', STRONG_TOKEN, s)
	
# 	# Step 2: 對每個段落清理
# 	segments = s.split(STRONG_TOKEN)
# 	cleaned_segments = [_clean_subblock(seg) for seg in segments if seg.strip()]
	
# 	# Step 3: 合併回單行，使用強分隔符
# 	result = strong_sep.join(cleaned_segments)
	
# 	# Step 4: 可選替換為 app 分隔符號
# 	if sep_for_app:
# 		result = result.replace(strong_sep, sep_for_app)
	
# 	return result
def unifiedData( orgData, strong_sep='//', sep_for_app=None ):
	
	## XXXX/XXXXX/XXXX 變成 XXXX//XXXXX//XXXX
	if not isinstance(orgData, str):
		return orgData
	
	# Step 1: 判斷是否包含「日期/卦象/數字符號」
	# 如果有這些特徵，換行 → //；否則換行 → ,
	has_special_pattern = bool(
		re.search(r'\d+[/\-]\d+', orgData) or  # 日期格式 2025/10/26
		re.search(r'[0-9X$@]{2,}', orgData) or  # 卦象符號 10$01X
		re.search(r'\d+,\d+,\d+', orgData)      # 米卦格式 27,71,42
	)
	
	# Step 2: 分段落（大區塊）
	STRONG_TOKEN = "STRONGSEPUNIQUE"
	
	# 保護原本的 //
	s = orgData.replace(strong_sep, STRONG_TOKEN)
	s = re.sub(r'\s-\s', STRONG_TOKEN, s)
	
	# 🔥 關鍵：根據內容類型決定換行的處理方式
	if has_special_pattern:
		# 有特殊符號 → 換行變成 //
		s = re.sub(r'[\r\n]+', STRONG_TOKEN, s)
	else:
		# 純中文 → 換行變成 ,
		s = re.sub(r'[\r\n]+', ',', s)
	
	# Step 3: 對每個段落清理
	segments = s.split(STRONG_TOKEN)
	cleaned_segments = [_clean_subblock(seg) for seg in segments if seg.strip()]
	
	# Step 4: 合併回單行
	result = strong_sep.join(cleaned_segments)
	
	# Step 5: 可選替換為 app 分隔符號
	if sep_for_app:
		result = result.replace(strong_sep, sep_for_app)
	
	# print(result)
	return result
# print(unifiedData("店家維修，能否順利修好電腦保住資料 - 0-1-00-11-0-1"))




## 確認內容為天干地支
def testTgdz( testData ):
	testData  =  testData.replace("月","").replace("日","").replace("/","" )
	tgdz = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸","子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
	for td in testData:
		if td not in tgdz:
			return False
	return True

## 確認內容快速模式 例如10X1$0
def checkInData( testData ):
	testData = testData.replace("/","")

	print( "----->>>-----",testData )
	# textDate  =  testData.replace("月","").replace("日","").replace("/","" )
	tgdz = ["0","1","X","$","@","6","7","8","9"]

	for td in testData:
		if td not in tgdz:
			return False
	return True


import re
from datetime import datetime, timezone, timedelta

Gan = "甲乙丙丁戊己庚辛壬癸"
Zhi = "子丑寅卯辰巳午未申酉戌亥"

def is_ganzhi(s):
	return len(s) == 2 and s[0] in Gan and s[1] in Zhi

ganZhi_Dict = {
	i + 1: gz for i, gz in enumerate([
		"甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉",
		"甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未",
		"甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰", "癸巳",
		"甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑", "壬寅", "癸卯",
		"甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑",
		"甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥"
	])
}

def checkYear(zhi, skip=0):
	dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
	localtimeReal = dt1.astimezone(timezone(timedelta(hours=8)))
	year_real = localtimeReal.year

	matched_years = [y for y in range(1984, 2100) if ganZhi_Dict[(y - 1983) % 60 or 60].endswith(zhi)]
	matched_years.sort(key=lambda y: abs(y - year_real))
	filtered = sorted([y for y in matched_years if y <= year_real], reverse=True)
	target_year = filtered[skip] if skip < len(filtered) else filtered[-1]
	return ganZhi_Dict[(target_year - 1983) % 60 or 60]

def reverse_gan_zhi(zhi_target, kong_wang_input):
	kong_wang_dict = {
		"戌亥": range(1, 11),
		"申酉": range(11, 21),
		"午未": range(21, 31),
		"辰巳": range(31, 41),
		"寅卯": range(41, 51),
		"子丑": range(51, 61),
	}
	ganZhi_List = [v for _, v in sorted(ganZhi_Dict.items())]
	kong_set = set(kong_wang_input)

	for key, rng in kong_wang_dict.items():
		if kong_set.issubset(set(key)):
			for i in rng:
				if ganZhi_List[i - 1][1] == zhi_target:
					return ganZhi_List[i - 1]
	return None

def parse_ganzhi_from_text(text):
	# 1. 提取空亡信息
	# kong_match = re.search(r'(?:空亡|空)?(?:\(|-|--|：|:)\s*([戌申午辰寅子亥酉未巳卯丑]{2})\)?', text)
	# kong_match = re.search( r'(?:空亡|空)?(?:\(|<{1,2}|:)\s*([戌申午辰寅子亥酉未巳卯丑]{2})(?:空)?\)?', text )    
	kong_match = re.search( r'(?:空亡|空)?(?:\(|<{1,2}|:|/)\s*([戌申午辰寅子亥酉未巳卯丑]{2})(?:空)?\)?', text )        
	# "卯年丑月酉日<午未"
	# "卯年丑月酉日:午未"
	# "卯年丑月酉日<<午未"
	# "卯年丑月酉日(午未"
	kong_raw = kong_match.group(1) if kong_match else None
	
	# 2. 檢查年份跳躍（如2巳年）
	skip_match = re.search(r'(\d)([子丑寅卯辰巳午未申酉戌亥])年', text)
	year_skip = int(skip_match.group(1)) - 1 if skip_match else 0
	
	# 3. 移除空亡部分，避免干擾
	clean_text = re.sub(r'(?:空亡|空)?(?:\(|-|--|：|:)\s*[戌申午辰寅子亥酉未巳卯丑]{2}\)?', '', text)
	
	# 4. 按順序提取所有干支組合和地支
	# 找到所有干支和地支的位置
	ganzhi_positions = []
	
	# 完整干支 (天干+地支)
	for match in re.finditer(r'[甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥]', clean_text):
		ganzhi_positions.append((match.start(), match.group(), 'complete'))
	
	# 單獨地支 (確保不是完整干支的一部分)
	for match in re.finditer(r'[子丑寅卯辰巳午未申酉戌亥]', clean_text):
		# 檢查這個地支是否已經被包含在完整干支中
		is_part_of_complete = False
		for pos, _, type_ in ganzhi_positions:
			if type_ == 'complete' and pos <= match.start() < pos + 2:
				is_part_of_complete = True
				break
		
		if not is_part_of_complete:
			ganzhi_positions.append((match.start(), match.group(), 'single'))
	
	# 按位置排序
	ganzhi_positions.sort(key=lambda x: x[0])
	
	# 提取按順序排列的干支/地支
	ordered_elements = [item[1] for item in ganzhi_positions]
	
	# 5. 按年月日順序分配
	year_raw = None
	month_raw = None
	day_raw = None
	
	# 年柱 (第一個)
	if len(ordered_elements) >= 1:
		first = ordered_elements[0]
		if is_ganzhi(first):
			year_raw = first
		elif first in Zhi:
			year_raw = checkYear(first, year_skip)
	
	# 月柱 (第二個)
	if len(ordered_elements) >= 2:
		second = ordered_elements[1]
		month_raw = second
	
	# 日柱 (第三個)
	if len(ordered_elements) >= 3:
		third = ordered_elements[2]
		if is_ganzhi(third):
			day_raw = third
		elif third in Zhi:
			# 只有地支，嘗試用空亡補天干
			if kong_raw:
				day_raw = reverse_gan_zhi(third, kong_raw) or third
			else:
				day_raw = third
		else:
			day_raw = third
	
	# 6. 組裝結果
	result_parts = []
	if year_raw:
		result_parts.append(year_raw)
	if month_raw:
		result_parts.append(month_raw)
	if day_raw:
		result_parts.append(day_raw)
	
	print()
	print(text + " <輸入")
	return "/".join(result_parts)


# print(parse_ganzhi_from_text("乙巳年卯月戊戌日"))
# print(parse_ganzhi_from_text("乙巳年卯月戊戌日"))         # → 乙巳/卯/戊戌
# print(parse_ganzhi_from_text("巳年寅月申日(戌亥空)"))     # → 乙巳/寅/壬申
# print(parse_ganzhi_from_text("乙巳年寅月申日-戌亥"))      # → 乙巳/寅/壬申
# print(parse_ganzhi_from_text("乙巳年寅月申日--戌亥"))     # → 乙巳/寅/壬申
# print(parse_ganzhi_from_text("乙巳年戊寅月申日-戌亥"))    # → 乙巳/戊寅/壬申
# print(parse_ganzhi_from_text("巳年寅月申日(戌亥)"))       # → 乙巳/寅/壬申
# print(parse_ganzhi_from_text("巳年寅月申日(戌亥"))        # → 乙巳/寅/壬申
# print(parse_ganzhi_from_text("巳年寅月申日--戌亥"))       # → 乙巳/寅/壬申

# print(reverse_gan_zhi("申", "戌亥"))
# reverse_gan_zhi("巳", "寅")    # → "乙巳"
# reverse_gan_zhi("巳", "卯")    # → "乙巳"
# reverse_gan_zhi("巳", "寅卯")  # → "乙巳"
# reverse_gan_zhi("巳", "卯寅")  # → "乙巳"
# reverse_gan_zhi("午", "辰")    # → "丙午"
# reverse_gan_zhi("亥", "戌")    # → "乙亥"





### 防止寫錯字用的
def fixGuaWording( guaName ):
	fixList = {	"西日":"酉日","西月":"酉日","始":"姤","恒":"恆","遁":"遯","暌":"睽","癸":"睽","責":"賁","憤":"賁","濛":"蒙","盟":"蒙","萌":"蒙","換":"渙","喚":"渙" ,"移":"頤","ㄅ":"剝" ,"須":"需","遇":"豫","進":"晉","減":"蹇","垢":"姤","后":"姤","夠":"姤","脆":"萃","卒":"萃","丰":"豐","換":"渙","喚":"渙","俘":"中孚","浮":"中孚","中俘":"中孚","中浮":"中孚","同":"同人","有":"大有","噴":"賁","奔":"賁","波":"剝","妄":"無妄","進":"晉","夷":"明夷","佳人":"家人","頂":"鼎","丰":"豐","既":"既濟","未":"未濟" ,"屢":"履"  }


	nameBuf = ""
	for item in guaName:
		if guaName in fixList.keys():
			nameBuf +=  fixList[guaName]
		else:
			nameBuf += item
	return nameBuf



## 簡體轉繁體
def chineseChange( text = '中国的文化源远流长。123我是貓abc文化源,远流长' ):
	from opencc import OpenCC
	# 模式	說明
	# 's2t'	簡體 → 繁體（一般用）
	# 't2s'	繁體 → 簡體
	# 's2tw'	簡體 → 台灣正體
	# 'tw2s'	台灣正體 → 簡體
	# 's2hk'	簡體 → 香港繁體
	# 'hk2s'	香港繁體 → 簡體
	# 'tw2sp'	台灣繁體 → 簡體（常用詞彙轉換）

	# 建立轉換器：從簡體轉繁體（s2t）或繁體轉簡體（t2s）
	cc = OpenCC('s2t')  # 簡轉繁
	
	converted = cc.convert(text)
	print(converted)  # 中國的文化源遠流長。
	return converted

# chineseChange()



## 輸入64卦卦名取得符號模式，例如: 雷澤(無變爻時只有爻的名字)  雷澤歸妹,1,3  or 雷澤,1,3  or  歸妹,1,3  
def checkAllGua( guaName , checkMode = False ):
	guaNameList = guaName.split("/")
	print( "Guaname - " , guaName , guaNameList )

	changeList = []

	gua = ""
	gua_binary = ""



	# print ( "*********", ("".join(str(c) for c in list(set(list(guaName.replace("/","" )[:6])))) )in[ "0","1","01","10" ] )


	## 如果全都是數字 例101010-2
	if ( len(guaNameList) > 1 ) and ( guaName.replace("/","" ).isdigit() == True ) and ( "".join(str(c) for c in list(set(list(guaName.replace("/","" )[:6])))) ) in [ "0","1","01","10" ] :
		changeList = guaNameList[1:]
		gua_binary = guaNameList[0]

		# print( "ON- 數字模式加動爻 例101010-2")
		if checkMode == True:
			return True

	else:
		if len( guaNameList) == 1: ## 101010  雷澤歸妹  雷澤  歸妹

			for foo in guaName: 
				if foo.isdigit() == True:
					# print( "ON- 數字模式沒有動爻 例101010")
					changeList.append( foo )
				else:
					## 不是數字的話  雷澤歸妹  雷澤  歸妹

					gua += foo
		else:
			gua =  guaNameList.pop(0)  ## 雷澤歸妹,1,3 的"雷澤歸妹"被取出
			changeList = guaNameList ## "1,3" 變爻掉到這裏，變卦卦爻(改個名免得混亂)

		gua = chineseChange(gua).removesuffix("卦")
		# gua = gua.removesuffix("卦")		
		print( "gua: ",  gua)

		for e in baGuaAllDict:


			# print("=========",gua)
			# # print(  gua.split("之")[0]  == e['outGua']+e['inGua'] ) 
			# print(  gua.split("之")[0] , e['title'] ) 


			# print( set( gua ).issubset(set("天雷火澤風水山地")) )



			# print( e['title']+e['body']  )
			if ( gua == e['title']+e['body'] ) or ( gua == e['title']+ "為" + e['body'] ): ## 雷澤歸妹 or 乾為天
				print( "A:",e['binary']  )
				gua_binary = e['binary'] 

				if checkMode == True:
					return True

			elif gua == e['title']:           ## 雷澤
				gua_binary = e['binary'] 
				# print("AAA")

				if checkMode == True:
					print( "B",e['title'],e['binary']  )
					return True

			elif gua == e['body']:           ## 歸妹
				print( "C",e['binary']  )
				gua_binary = e['binary'] 

				if checkMode == True:
					return True


			# 地風升之地水師
			## 賁之明夷卦
			# elif ( len(gua.split("之")) == 2) and ( ( fixGuaWording( gua.split("之")[0] ) == e['body'] ) or (  gua.split("之")[0]  == e['title']) )  and ( ( fixGuaWording( gua.split("之")[1] ) in [gua["body"] for gua in baGuaAllDict]  ) or ( set( gua ).issubset(set("天雷火澤風水山地")) ) == True  ): ## 咸之解
			elif (	len( gua.split("之") ) == 2								# XX 之 XX
					and (
						fixGuaWording(gua.split("之")[0]) == e["body"] 	   ## '睽'    body
						or gua.split("之")[0] == e["title"]                ## '火澤'  title
						or ( gua.split("之")[0] == e['title']+e['body'] ) 
						or ( gua.split("之")[0] == e['title']+ "為" + e['body'] )
					)
					and (
						fixGuaWording(gua.split("之")[1]) in [g["body"] for g in baGuaAllDict]            ## '鼎'
						or fixGuaWording(gua.split("之")[1]) in [g["title"] for g in baGuaAllDict]   ## 復之艮的艮
						or set(gua.split("之")[1]).issubset("天雷火澤風水山地")  
												   ##'火風'
						or ( gua.split("之")[1] in [g["title"] + ("為" if len(g["title"]) == 1 else "") + g["body"] for g in baGuaAllDict] )

					)
				):
				# print( ">>>>>>>")
				# print( ">>>>>>>")
				# print( ">>>>>>>")				
				binaryA = e['binary'] 

				changeGuaBody = fixGuaWording( gua.split("之")[1] ) ## 變卦   解
				print( changeGuaBody )
				if checkMode == True:
					return True

				for bee in baGuaAllDict:
					print ( bee['title'] , bee['body'] )
					## 地水   水   地水師    震為雷
					if ( changeGuaBody == bee['title'] ) or ( changeGuaBody == bee['body'] ) or ( changeGuaBody == bee['title'] + bee['body'] ) or ( changeGuaBody == bee['title'] +"為"+ bee['body'] ) :
					# if changeGuaBody == bee['body']: ## 找到變卦
						binaryB = bee['binary']
						# print("INNNN--body: " ,changeGuaBody  , binaryA, binaryB )

						gua_binary = binaryA
						changeList = [str(i + 1) for i in range(len(binaryA)) if binaryA[i] != binaryB[i]]  ## ['2', '3', '5']
						break
					# elif changeGuaBody == bee['title']: ## 找到變卦
					# 	binaryB = bee['binary']
					# 	# print("INNNN--title: " ,changeGuaBody  , binaryA, binaryB )

					# 	gua_binary = binaryA
					# 	changeList = [str(i + 1) for i in range(len(binaryA)) if binaryA[i] != binaryB[i]]  ## ['2', '3', '5']						

		if checkMode == True:
			return False		

	# print( ">",changeList)
	# print( ">",gua_binary)


	add = 1
	result = ""
	for binBuf in gua_binary:
		if str( add ) in changeList:
			if binBuf == "1":
				result += "$"
			elif binBuf == "0":
				result += "X"
		else:
			result += binBuf
		add += 1

	# print ("final-",result)
	return result



def is_valid_date(date_list):
	try:
		year, month, day = map(int, date_list)
	except:
		return False

	# 每個月的天數，二月固定 29 天
	month_days = {
		1: 31, 2: 29, 3: 31, 4: 30,
		5: 31, 6: 30, 7: 31, 8: 31,
		9: 30, 10: 31, 11: 30, 12: 31
	}

	# 月份檢查
	if month not in month_days:
		return False

	# 日期檢查
	if 1 <= day <= month_days[month]:
		return True
	else:
		return False



# ## 檢查NOTION帳號資料是否可執行
# from notion_client import Client
# def checkNotionAcc(token, pageId):
#     try:
#         notion = Client(auth=token)
#         notion.pages.retrieve(pageId)
#         return True
#     except Exception as e:
#         print(f"錯誤: {e}")
#         return False


import re
from datetime import datetime

def looks_like_year(text):
	# 支援 - / , . 空白 混用
	pattern = r'(\d{2,4})[\/\-,.\s](\d{1,2})[\/\-,.\s](\d{1,2})'
	
	match = re.search(pattern, text)
	if not match:
		return False  # 找不到三組數字
	
	year, month, day = match.groups()
	
	# 年份格式統一
	year = int(year)
	# 如果只有 2 位數的年份，自行決定如何處理，例如 25 -> 2025
	if year < 100:
		year += 2000  # 可自行調整

	month = int(month)
	day = int(day)

	# 檢查是否合法日期
	try:
		datetime(year, month, day)
		return True
	except ValueError:
		return False























# ===========================================================================================================================================================
# ===========================================================================================================================================================
# ===========================================================================================================================================================
# ===========================================================================================================================================================

 ##   ##    ##      ####    ##   ##  
 ### ###   ####      ##     ###  ##   
 #######  ##  ##     ##     #### ##   
 #######  ##  ##     ##     ## ####  
 ## # ##  ######     ##     ##  ###   
 ##   ##  ##  ##     ##     ##   ##   
 ##   ##  ##  ##    ####    ##   ##   

# ===========================================================================================================================================================
# ===========================================================================================================================================================
# ===========================================================================================================================================================
# ===========================================================================================================================================================





from logBackup import ( logDataFun as logBK_logDataFun,    uploadCsvToGoogleSheet as logBK_uploadCsv  )
from sixYaoJsonDataClass import *



def sixYaoMain ( fullDataInput , userSetting = None , showPic = False ):
	print( "========================= MAIN =========================")
	fullDataInput = fullDataInput.replace( '\u200b' , '' )
	# fullDataInput = fullDataInput if '//' in fullDataInput else fullDataInput.replace('/', '//') if '/' in fullDataInput else fullDataInput
	# if "//" not in fullDataInput:
	# 	fullDataInput = fullDataInput.replace( '/' , '//' )



	fullDataInput = fullDataInput.replace( " - " , '//' ).replace( "\n" , '//' )
	fullDataInput = fullDataInput.strip() ## 清除頭尾空格

	# fullDataInput = fullDataInput.replace("，","#")
	fullDataInput = unifiedData(fullDataInput)
	print( fullDataInput)

	notionAccount = False
	# ui_mode = ""
	notionMode = False
	textUIMode = False


	## 開頭為"n"則為上傳notion模式，差異在上傳圖床的檔案夾是會保存的
	if fullDataInput[:1] == "n":
		print( ">> 上傳Notion模式")
		notionMode = True
		fullDataInput = fullDataInput[1:]
		print ( "Notion mode ON")		


	print( "##### userSetting dict:",userSetting )
	if userSetting == None:
		print( "產生一組假的")
		linebot_Id =  "U21eaaf32db85b983a842d9a9da81d8f1"    
		user_name =   "Benno"
		user_utc_hour =   8        
		user_tipsMode =   "ON"  
		user_notion =    False 
		# 建立 jsonData
		jsonData = jsonDataClass(
			linebotId=linebot_Id,
			linebotUserName=user_name,
			userImage="http://displayName.jpg",
			command=fullDataInput
		)


	else:
		linebot_Id =      userSetting [ "linebotId" ]
		user_name =       userSetting [ "linebotUserName" ]
		user_utc_hour =   userSetting [ "utc" ]     
		user_tipsMode =   userSetting [ "tipsMode" ]
		user_notion =     userSetting [ "notionToken_pageId" ]

		# linebot_Id    = userSetting.get("linebotId", "預設值")
		# user_name     = userSetting.get("linebotUserName", "Benno")
		# user_utc_hour = userSetting.get("utc", 8)
		# user_tipsMode = userSetting.get("tipsMode", "ON")
		# user_notion   = userSetting.get("notionToken_pageId", None)



	token_buf = ""
	pageId_buf = ""



	build_mode = False

	if fullDataInput[:1] == "+":
		print( ">> 出圖模式")
		build_mode = True
		fullDataInput = fullDataInput[1:]


	## 開頭為"t"則為文字裝卦版本	
	if fullDataInput[:1] == "t":
		print( ">> 文字卦模式")
		textUIMode = True
		fullDataInput = fullDataInput[2:]
		print ( "Text mode ON")	

	# jsonData.showData()

	finalGua = "------"
	checkItem = [ "-" , "-" , "-"  ]
	# [0]卦，[1]時間，[2]內文
	fullDataInputOrg = fullDataInput

	fullDataInput = unifiedData(fullDataInput)
	# fullDataInput =fullDataInput.replace( '\u200b' , "")
	guaSort = {  1:"乾", 2:"兌", 3:"離", 4:"震", 5:"巽", 6:"坎", 7:"艮", 0:"坤" }## 八卦排序

	guaGuaDict = { "乾":"111" ,"兌":"110" ,"離":"101" ,"震":"100" ,"巽":"011" ,"坎":"010" ,"艮":"001" ,"坤":"000" } # 由下往上排，所以順序要顛倒

	dateData = ""    ## 日期  2024-12-5-10-31
	dateMonth = ""   ## 月干支
	dateDay = ""     ## 日干支
	noteText = ""    ## 說明文字
	preNote = ""     ## 文字前的三個數字( 米卦用 )

	print( ">> fullDateInput:  " + fullDataInput )

	# for i, fruit in enumerate(fruits):

	for i,buf in enumerate(fullDataInput.split("//")):
		buf_org = buf
		# 判斷是否為「三柱八字」，也就是剛好含有 3 組干支（1組=1天干+1地支，共6字）
		# 範例:
		#   "甲辰年丙寅月辛丑日" → ✅ True （三柱）
		#   "巳月乙未日" → ❌ False （只有一組）
		#   "甲辰年丙寅月" → ❌ False（兩組）
# 嘗試直接抽出所有合法干支組合（如：甲辰/丙寅/辛丑）


		# 卦
		#######################################################################################
		parts = buf.split("/")
		clean_digits = buf.replace("/", "")

		# 27-71-42 ## 米卦模式，數字分上卦下卦變卦三段，拿變卦來做判斷，數字大於6
		# 條件 A：三段數字，最後一段 > 6
		cond_three_part_valid = (
			len(parts) == 3
			and all(part.isdigit() for part in parts)
			and int(parts[-1]) > 6
		)


		#  0-1-00-11-0-1
		# 條件 B：六段，每段只能是 "0", "1", "00", "11"
		valid_values = {"0", "1", "00", "11"}
		cond_six_part_valid = (
			len(parts) == 6
			and all(part in valid_values for part in parts)
		)
		

		# print("-----------", buf + "/12/00" )
		# print( len((buf + "/12/00").split("/")))



		cleaned = re.sub(r'[年月日時\s\.,:/：()\[\]（）\-—《》〈〉…、，]', '', buf)

		# 統一判斷條件
		if ( cond_three_part_valid or cond_six_part_valid ) and is_valid_date(parts) == False:
			print( ">> 進入米卦和0,00模式")
			finalGua,preNote = riceGua( buf ) 
			## ['20-30-40'] 米卦          --> 101X0$ , 27.71.42
			## ['1,0,11,0,00,1'] 六爻卦   --> 101X0$ , None
			checkItem[0] = "卦"

		## 卦 $0011X0
		elif checkInData( buf_org ) == True:
			print(">>進入直上模式")
			if len( buf_org ) == 6:
				finalGua = buf_org.replace("/","").replace("@","$").replace("6","X").replace("7","1").replace("8","0").replace("9","$")
				checkItem[0] = "卦"
			else:
				print( "卦有問題")

		elif checkAllGua( buf , checkMode = True ) == True:  ## 雷澤歸妹.3    101001.2.3  豐之離
			print(">> 進入卦名模式")
			finalGua = checkAllGua( buf )		
			checkItem[0] = "卦"




		# 時間
		#######################################################################################

		## 取得自行輸入日期(四柱or三柱) ##"庚子,甲申,乙未,丁丑"
		## 四柱 ，年月日三柱也行，時柱會訂在中午十二點
		elif (  2 < len( buf.split("/") ) < 5 ) and ( testTgdz( buf ) ): 
			print( parts )
			print(buf)
			dateData_buf = fourPillarToDateMain(  buf.replace( "/", "/") )
			print( dateData_buf )
			if dateData_buf == None:
				print( "不正確四柱:", buf)
				dateData = "error四柱"
			else:
				dateData = dateData_buf
				checkItem[1] = "日"

		## 取得自行輸入日期 ## 2024-12-5-10-31    2025-08-17 22:36
		# elif (buf.endswith("<") or buf.isdigit() or "/" in buf)  and    (len(buf.rstrip("<").split("/")) == 5)  and    (buf.rstrip("<").replace("/", "").isdigit()) or (  len((re.sub(r"[- :]", "/", buf)).split("/")) == 5  and    buf.rstrip("<").replace("/", "").isdigit())  :
		elif  looks_like_year(buf) == True:
			if (
				(
					(buf.endswith("<") or buf.isdigit() or "/" in buf) and (len(buf.rstrip("<").split("/")) == 5) and (buf.rstrip("<").replace("/", "").isdigit())
				)
				or
				(
					(len((re.sub(r"[- :]", "/", buf)).split("/")) == 5) and (buf.rstrip("<").replace("/", "").isdigit())
				)
				or
				(
					len(  (buf + "/12/00").split("/")  ) == 5 ## 缺少時柱
				)
			):
				print( ">>進入日期模式", buf )
				if len( buf.split("/") ) == 3:
					dateData = buf + "/12/00<"
				else:
					dateData = buf

				checkItem[1] = "日"
			else:
				print( "日期輸入有誤")
				dateData = "------"


		## 自訂干支
		elif testTgdz( buf_org ) == True:  ## 乙月-丙子日
			print( ">> 自訂干支模式")
			# print(buf.split( "/" ))
			if buf_org[-1:] != "日":
				buf_org += "日"


			if len(buf_org.split( "/" )) == 2:
				# print("aa")
				# dateData =  buf.split( "/" )[0]  + "/" + buf.split( "/" )[1]
				dateMonth = buf_org.split( "/" )[0] 
				dateDay = buf_org.split( "/" )[1]

			elif len( buf_org.split( "/" ) ) == 1:  ## 乙月丙子日 (黏在一起)
				print(">>>>>>>>", buf_org )
				monthId = buf_org.index("月")       ## 確認"月"的位置
				# dateData = buf[ :buf.index("月")+1] + "/" + buf[ buf.index("月")+1: ] 
				dateMonth = buf_org[ :buf_org.index("月")+1]
				dateDay   = buf_org[ buf_org.index("月")+1: ]
			checkItem[1] = "日"


		# 巳年卯月戊戌日    乙巳,卯月,申-戌亥 
		elif all(c in '012345678甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥' for c in cleaned)  and ( len(buf.rstrip("<").split("/")) != 5 )  and is_valid_date(parts) == False:
			buf_tmp = "/".join(
				re.findall(r'[甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥]', buf)
			)

			# 如果抽到的是三柱完整干支，就直接使用
			if all(re.fullmatch(r'[甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥]', p) for p in buf_tmp.split('/')) \
				and len(re.sub(r'[^甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥]', '', buf_tmp)) >= 6:
				
				buf = buf_tmp
				print(">>三柱完整干支:", buf)

			# 否則使用智能補全（parse_ganzhi_from_text）來還原
			else:
				print ( ">>>>>>org BUF:" , buf )
				buf = parse_ganzhi_from_text(buf)
				print("BUFF (parsed):", buf)

			checkItem[1] = "日"
			dateData = fourPillarToDateMain(  buf.replace( "/", "/") )
			print( dateData )





		## 文字說明
		else:
			noteText = fullDataInputOrg.split("//")[i]
			
			checkItem[2] = "占"

		## 如果這裏日期還是空的，表示沒有要自行設定，所以從系統取得
		if dateData == "":
			dateData =  getNowTime( user_utc_hour )
			checkItem[1] = "日"
			print( "日期現時" )

		if noteText == "":
			noteText = "Untitled"
			checkItem[2] = "占"
		print( "- - - - - - - - - - - - - - - - - - - - - - - - - -")
	# dateData = dateData.replace("/" , " ")

	date_ganZi = ""
	date_ganZiList = []
	if  dateMonth and dateDay:
		date_ganZi =  dateMonth+dateDay + " // " 
		date_ganZiList = [dateMonth,dateDay[:2]]
	# if user_uiStyle == "UA":
	# 	command =  "++%s // %s%s // %s"% ( dateData , date_ganZi , finalGua , preNote + noteText ) 
	# elif user_uiStyle == "UB":
	# 	command =  "+%s // %s%s // %s"% ( dateData , date_ganZi , finalGua , preNote + noteText ) 
	# else:
	# 	command =  "++%s // %s%s // %s"% ( dateData , date_ganZi , finalGua , preNote + noteText ) 

	command =  "+%s // %s%s // %s"% ( dateData , date_ganZi , finalGua , preNote + noteText ) 

	print( checkItem )
	print( "    日期- ",  dateData)
	print( "    月干- " , dateMonth )
	print( "  日干支- " , dateDay )
	print( "finalGua - ",  finalGua )
	print( "    文字- ",  preNote + noteText )  ## [3|7|4]  +  占今年幾時換工作較好
	print("\n")
	print ( command )


	if checkItem != ['卦', '日', '占']:
		print ("error")
		return "error"




	# "2025,4,27,12,28//010$1X//問題問題問題"
	# "2025,4,27,12,28//卯月丁巳日//010$1X//問題問題問題"
 # (','.join(finalGua))  "\u200b".join(num)
	# zeroSpace = '\u200b'

	# currentCommand = "+%s%s//%s//%s"% ( dateData , date_ganZi , (zeroSpace.join(finalGua)) , preNote + noteText )
	print( "\n")



	showBuf = showPic ## 上傳時記得OFF掉

	if notionMode:
		showBuf = False

	# command_mode = True	
	#  XXX//XXXX//XXXXX		UI模式

	# command_mode = False
	# +XXX//XXXX//XXXXX    	產生圖檔模式

	print ( "linebot_Id --" , linebot_Id )
	print ( "user_name --" , user_name )
	print ( "user_utc_hour --" , user_utc_hour )
	print ( "user_tipsMode --" , user_tipsMode )
	print ( "user_notion --" , user_notion )

	# textUI = format_gua_text(
	# 				mainFunction( 
	# 					inputData = finalGua ,
	# 					noteText = preNote + noteText  , 
	# 					user_mouthZi = dateMonth , 
	# 					user_dayGanZi = dateDay , 
	# 					userDefineDate = dateData )
	# 				)



	if build_mode == True:
		print ( "\n\n\n==== 圖片裝卦模式 ====\n\n\n")
		## 產生圖片，回傳連結
		image_url = drawUi_v1(  
			mainFunction( 
				inputData = finalGua ,
				noteText = preNote + noteText  , 
				user_mouthZi = dateMonth , 
				user_dayGanZi = dateDay , 
				userDefineDate = dateData ), 

			# fontStyle = user_fontStyle, 
			tipsMode = user_tipsMode, 
			# uiStyle = user_uiStyle , 

			show = showBuf , 
			savePic = False,
			notion = notionMode )


		# return image_url
		# print( image_url )
		if notionMode == True:
			import supabase_io
			# data = get_user_data( linebot_Id ) ## << 這裏出錯  NameError: name 'get_user_data' is not defined
			data = supabase_io.get_user_data( linebot_Id )
			token_buf = data['notion_token']
			pageId_buf = data['page_id']

			notionUrl = notionPush_pushUp(  image_url , preNote + noteText  , token_buf , pageId_buf )
			print( "NOTION URL:" , notionUrl )
			return notionUrl
		else:
			return image_url

	## 產生UI模式
	elif textUIMode == True:
		print( "\n\n\n==== TEXT UI模式 ====\n\n\n")
		textUI = format_gua_text(
						mainFunction( 
							inputData = finalGua ,
							noteText = preNote + noteText  , 
							user_mouthZi = dateMonth , 
							user_dayGanZi = dateDay , 
							userDefineDate = dateData )
						)
		return textUI

	## 產生UI模式
	elif fullDataInput[:1] != "+":
		print( "\n\n\n==== UI 模式 ====\n\n\n")
	# else: 
		# dateData =  getNowTime( user_utc_hour )
		## 產生裝卦UI時，記錄到log中
		logBK_logDataFun( linebot_Id , user_name , dateData , fullDataInput , command )
		# save_json_data(  linebot_Id, "temp", command , json_path='__sixYoSet__.json')
		threePil_mode = False
		if  "<" in dateData:  ## 如果只有三柱
			dateData = dateData[:-1]
			threePil_mode = True



		ui_cmd_dict = uiInputData(  dateData , 
									date_ganZiList , 
									finalGua = finalGua , 
									note = preNote + noteText , 
									command = command  ,
									threePillar = threePil_mode , 
									notionAccount = user_notion,
									printMode = showPic  )
		# print( ui_cmd_dict )
		return ui_cmd_dict



if __name__ == '__main__':
	# sixYaoMain( "2021/04/18/19/00//1​1​0​X​1​1//男占女未來是否有機會共事")
	# sixYaoMain( "俘之履//男占女未來是否有機會共事//辛丑，壬辰，丙申，戊戌")
	# sixYaoMain( "2025,4,27,12,28//卯月丁巳日//010$1X//問題問題問題" )
	# sixYaoMain( "復之艮//吃飽了沒")
	# sixYaoMain( "27 71 42//吃飽了沒")
	# sixYaoMain( "地风升之地水师//卯月乙未日//一人占賣貨")	
	# sixYaoMain( "100101//占今年幾時換工作今時換工作較好" )
	# sixYaoMain( "傑利老家的田今年能賣掉嗎//天山之雷天" )
	# sixYaoMain( "占今年幾時換工作較好//01X$01//申月癸卯" )  ## 二合
	# sixYaoMain( "0,1,X,$,0,1//吃飯沒" )
	# sixYaoMain( "乙巳，庚辰，乙卯，甲申//山雷之山地//六月七能見他嗎" )
	# sixYaoMain( "癸卯,乙卯,庚午,丙戌//火水之解//今年財運" )
	# sixYaoMain( "是否要投資台績電//0,1,11,0,0,1//丁月乙亥日" )
	# sixYaoMain( "+某某集團的發展//地風,3,1//丁月乙亥日") 
	sixYaoMain( "兩村相爭//火天.1,3,4,6//卯月丁巳日") ## 三合

	# sixYaoMain( "乙巳年寅月申日-戌亥//大过之鼎卦")	
	# sixYaoMain( "+巳年卯月戊戌日//大过之鼎卦")	## 三合太多
	# sixYaoMain( "吃不吃辣//100010.2")	
	# sixYaoMain( "+嬰兒健康吉凶//山風 .,2.3//己卯月甲午日",showPic = True )  ## 三合 跳格
	# sixYaoMain( "去學習是否順利 // 火地晉卦5 // 丙月，丙子日")
	# sixYaoMain( "去學習是否順利//100X10//己亥 辛未 壬申")
# 110$0$
	# sixYaoMain( "占盧女甲辰年流年//甲辰年辰月癸亥日//10X01$" ) # 三合缺一，靜爻有
	# sixYaoMain( "占一男終身財福//乙巳年辰月辰日-寅卯//00$01X" )
	# sixYaoMain( "占家宅人口平安否//卯月癸亥日//111X1X" )
	# sixYaoMain( "+占開店//寅月辛酉日//X0100$" ,showPic = True)
	# sixYaoMain( "卯月乙未日//一人占賣貨?////家人之小畜卦")
	# sixYaoMain( "+酉月丙寅日//占何日雨?//升之師卦",showPic = True )
	# sixYaoMain( "卯月戊辰日//占父官事?//萃之同人卦")
	# sixYaoMain( "+巳月丁亥日//一人占僕何日回?//夬之屢卦",showPic = True)
	# sixYaoMain( "申月戊辰日//占具題?//中孚之損卦")
	# sixYaoMain( "卯年丑月酉日-午未//柯男占甲辰年流年//1X1110")
	# sixYaoMain( "傑利如果漲房租租客是否會續租//898887")  # 二合
	# sixYaoMain( "申月戊辰日//妻占夫近病?//同人之離卦" )	
	# sixYaoMain( "傑利婚姻終身卦//010$X1//2025/08/20/15/25" )	
	# sixYaoMain( "丑月戊辰日//占防恭劾?//井之中孚卦" )	# 三合 四格
	# sixYaoMain( "+寅月戊午日//占地造葬可否?//頤之無妄卦" )	
	# sixYaoMain( "辰年辰月丁未日//赫女占回北部工作吉凶?//10XX1$" )	 # 三合 四格

	# sixYaoMain( "+占陳女(妹妹)終身婚姻?//乙巳年申月己酉日//001$00" )	 
	# sixYaoMain( "乙巳年申月己酉日//占陳女(姐姐)終身婚姻?//0X00X1" )	 


	# sixYaoMain( "卯年戌月丁卯日//謝男占回家工作吉凶?//00 0 11 1 00 0" )	 # 三合 四格

	# sixYaoMain( "+00$100" )	

	# sixYaoMain( "+2025/9/4/11/35 // 00010$ // 小單近況" )	
	# sixYaoMain( "+2025/9/8/15/10 // 000$00 // 常秉賢近況吉凶0815" )
	# sixYaoMain( "+2025/9/11/15/43 // 101010 // 常秉賢近況吉凶0911" )


	# sixYaoMain( "2025/8/25/0/47 // 10XX1$ // 赫女占回北部工作吉凶?" )	 ## 三合 四格
	# sixYaoMain( "+2024/04/13/12/00<//10XX1$//赫女占回北部工作吉凶?")  ## 三合 四格

 

	# sixYaoMain( "+申月戊午日//一人占自久病問過得今年否?//遁之姤卦" )
	# sixYaoMain( "2024,11,17,21,04//姜舒蕾(許奇峰老婆)何時懷孕?//地天泰之震為雷" ) ## 三合
	# sixYaoMain( "+2025/05/08/09/40//1X01$0//在某公司的發展" )
	# sixYaoMain("2025/05/08/09/40 // 在某公司的發展 //  隨之歸妹")
	# sixYaoMain( "巳年甲申月乙丑日//占姜小姐胎產吉凶(政閩)//巽為風" )
	# sixYaoMain( "2025-08-24 13:17//占姜小姐胎產吉凶(陳春霖)//澤水困" )
	# sixYaoMain( "2025-08-24 00:46//占姜小姐胎產吉凶(盈樺)//山地之晉" )
	# sixYaoMain( "占姜小姐胎產吉凶(JTin)// 乙巳年甲申月乙丑日 // 33.51.69")
	# sixYaoMain( "占姜女子孫吉凶(尾翼)// 甲申月乙丑日//需之夬" )
	# sixYaoMain( "乙巳年卯月辛巳日//占賴男乙巳年業務吉凶//11010X" )
	# sixYaoMain( "" )
	# sixYaoMain( "巳年卯月戊戌日//大过之鼎卦")  ## 多個三合

	# sixYaoMain( "理事長病危?//丙戌，戊戌，戊寅，戊午//110101, 4,6" )           ## 三合 四格
	# sixYaoMain( "黃連老師狗狗生病//2025/07/09/22/58//011100.3" ) ## 暗動  沖脫
	# sixYaoMain( "+一女占前男友是否有機會復合//旅之小過卦//甲申月戊申日" ,showPic = True)
	# sixYaoMain( "某男占陳女有法助本人事業否?//明夷之泰卦//庚子年甲申月丙申日" )	## 雙沖
	# sixYaoMain( "占今年房價貴賤//旅之小過卦//癸卯年辛酉月庚午日丁亥時" )	
	# sixYaoMain( "蔡男占租一地方做教室吉凶//兌為澤//癸卯 丁巳 己卯 庚午" ) ## 日沖月沖
	# sixYaoMain( "010011,1,4,5//乙巳-戊寅-壬申//龔子修占今年能否上南京師大?")

	# sixYaoMain( "2寅年巳月寅日-申酉//華一希占高考考運//天火 1 3 5" )
	# sixYaoMain( "0X@0X1" ) 
	# sixYaoMain( "2025,10,30//澤之節" ) 
	# sixYaoMain( "Q媽的鑽石項鍊在那裏?//1X@001" ) 
	# sixYaoMain( "++乙巳年卯月己丑日//自占4/6馬祖新村擺攤收入吉凶?//1X0$$0") ## 三合
	# sixYaoMain( "乙巳卯月戌-辰巳//X10101//自占今日在台中舊酒廠業績?" ) ## 三缺一


# 群組討論
	# sixYaoMain( "辰年午月癸卯日//廖女占去XX案場工作吉凶//111$10" ) #第三問
	# sixYaoMain( "+2025/08/22/09/10 // 1001$0 // 占黃連老師台中經營課是否會開" )
	# sixYaoMain( "2025/08/31/12/28 // X011$0 // 舅舅為了生小孩想換女朋友")
	# sixYaoMain( "2025-08-17 22:36 // 隨之困 // 占繳罰款去申訴有機會撤銷否?")
	# sixYaoMain( "+2025/08/27/18/36 // 10111$ // 提供群友AB免費服務項目(已有)但部分服務另收費/有搞頭嗎" )


	# sixYaoMain( "2025/08//測測//111111" )

	# sixYaoMain( "set nt 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,26a739d0e36080d29148e0f263b77986" )
	# sixYaoMain( "set nt 123adf" )
	# sixYaoMain( "+乙巳年辰月辰日-寅卯//00$01X//占一男終身財福",showPic = True ) ## 三合 日
	# sixYaoMain( "傑利的房貸吉凶//01$X10//2025,8,14,15,10" )

	# sixYaoMain( "+2025/08/31/15:48//傑利的房貸吉凶0831//110000",showPic = True) ## 九月七日 酉月卯日
	# sixYaoMain( "+2025/9/2/12/37 // 101X0X // 傑利的房貸吉凶0902" ) ## 九月七日 酉月卯日
	# sixYaoMain( "2025/9/2/14/11 // X1$110 // 傑利漲房租有沒有望" )
	# sixYaoMain( "+2025/9/17/2/4 // 1$0$00 // 傑利與同學見面錢財吉凶",showPic = True)
	# sixYaoMain( "+乙巳年乙酉月丁亥日//男占小孩突發疾病吉凶//011100" ,showPic = True )
	# sixYaoMain("+2025/10/02/20/41//01$10X//測試測試測試",showPic = True )


	# sixYaoMain( "+2025/8/31/17/1 // 01X0XX // 陳佩吟流年感情吉凶0831") ## 丑月
	# sixYaoMain( "++2025/9/10/14/28 // 01$$11 // 陳佩吟流年感情吉凶0910") ## 丑月
	# sixYaoMain("++2025/9/11/16/1 // 10$X0X // 陳佩吟流年感情吉凶0911" )
	# sixYaoMain("+2025/9/14/14/32 // 0101$0 // 與陳佩吟的感情發展吉凶" ) ## 酉兄強勢，辰父合應
	# sixYaoMain("++2025/9/29/13/35 // 1100X1 // 與陳佩吟的感情發展吉凶0929" )
	# sixYaoMain( "與陳佩吟的感情發展吉凶1008//" )

	# sixYaoMain("++2025/9/29/13/46 // 10$000 // 陳佩吟的感情吉凶" )
	# sixYaoMain("+2025/9/29/13/56 // 10$$0X // XXX")
	# sixYaoMain( "++2025/10/1/14/18 // XXX010 // 占與陳佩吟的感情吉凶" )
	# sixYaoMain( "++2025/10/3/17/48 // 10X$00 // 占我有沒有辦法得到這個小奴" ) 
	# sixYaoMain( "++2025/10/7/20/18 // 0X011X // 是否能得到小奴" )
	# sixYaoMain( "++2025/10/8/20/9 // 0XX01$ // 是否能得到電話中的小奴")

	# sixYaoMain("+乙巳,乙酉,辛丑,甲午//火雷之天雷//妹妹否應接受現在手上的工作offer",showPic = True )
	# sixYaoMain("+2025/9/18/15/19 // 10110$ // 自占是否能接到越南的大筆訂單？",showPic = True ) # 缺一待用
	# sixYaoMain( "+2025/10/1/0/15 // 01X10$ // 自占工作-留在原公司" ,showPic = True)
	# sixYaoMain( "++2025/10/1/0/15 // 101100 // 自占工作-去C公司" )
	# sixYaoMain( "++2025/10/1/0/15 // 001$0$ //  自占工作-去D公司" )
	# sixYaoMain( "+2025-10-01 00:15//旅之震//no title" )
	# sixYaoMain( "set nt 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,2807e0d9df298007bf76e212cc0459f5" )



	# sixYaoMain("n++占十月工作吉凶(測試)//10$000//2025-10-01 00:15" )
	# sixYaoMain("n++男占女愛不愛他(測試)//10$000//2025-10-01 00:15" )
	# sixYaoMain("n++二手賓士能不能買(測試)//10$000//2025-10-01 00:15" )	
	# sixYaoMain( "++2025-10-02-20-41//恆之解卦//回原公司" )
	# sixYaoMain( "++2025-10-02-20-41//賁之明夷卦//待在新公司" )


	# sixYaoMain( "++2025/10/5/12/57 // 1111XX // 1. 正念問卷導引介入路線" )
	# sixYaoMain( "++2025/10/5/12/57 // $1101$ // 2. 經筋機器學習路線" )
	# sixYaoMain( "++2025/10/5/16/44 // 010X$X // 伍懷芝占兩個科目同時進行吉凶" )


	# sixYaoMain( "+2025/8/30/16/50 // 01X000 // 問陳老闆的工作幾時開工" )


	# sixYaoMain("+乙巳 乙酉 乙酉 辛巳//女問是否會和某男在一起//困之坎")



	# ['乙巳-乙酉-壬午', '2025/09/10', ''] 兄弟寅木 子孫午火 出伏


	# sixYaoMain( "傑利是否可貸到330萬?//1$01X0" )
	# sixYaoMain( "2025/8/16/19/41//0​X​$​1​0​1//瑞豐近況0816" )
	# sixYaoMain( "+2025/8/16/19/41 //瑞豐近況0816//0X$101" ,showPic = True)
	# sixYaoMain( "n++2025/8/30/18/17 // 011$X1 // 瑞豐近況0830" ,showPic = True)
	# ['乙巳-丁亥-庚辰', '2025/11/07', '立冬'] 亥月鬆一點
	# sixYaoMain( "++2025/9/21/13/5 // 001X1$ // 盧卡斯最近工作吉凶" )
	# sixYaoMain( "++2025/9/21/13/26 // 0010XX // 瑞豐工作吉凶0921" )
	# sixYaoMain( "++2025/9/23/19/23 // 1X0001 // 盧卡斯工作吉凶0923" )
	# sixYaoMain( "++2025/9/24/13/4 // 11X$01 // 占阿聰在美國工作吉凶" )
	# sixYaoMain( "++2025/9/24/13/4 // 000000 // 占阿聰身體吉凶" )
	# sixYaoMain( "++2025/9/24/13/17 // $01110 // 占阿聰感情吉凶" )

	# sixYaoMain( "甲戌/戊戌/戊寅//X10101//自占今日在台中舊酒廠業績?" )	
	# sixYaoMain( "" )
	# sixYaoMain( "阿西最近的財運//1X0$00")
# 巳年寅月申日(戌亥空) 待修正

	# sixYaoMain( "一年輕人 出車禍目前昏迷不醒，代占是否有機會救的回來//乙巳 癸未 癸巳 丙辰//夬 3 4 5 6 ")
# 	txt = """
	# sixYaoMain( "2025/8/26/22/23//001X1$//傑利老家的地幾時賣掉?0826" )
	# sixYaoMain( "傑利老家的地幾時賣掉?0828//X110$0" )
	# sixYaoMain( "n++占繳罰款去申訴有機會撤銷罰單否？//2025-08-17 22:36//隨之困" ) ## 待修

	# sixYaoMain( "2025/8/29/15/56 // 01$101 // 占高潔妮財運吉凶" )
	# ['乙巳-甲申-甲戌', '2025/09/02', ''] 出空
	# ['乙巳-甲申-乙亥', '2025/09/03', ''] 亥填實
	# ['乙巳-甲申-丙子', '2025/09/04', ''] 子日
	# ['乙巳-乙酉-壬午', '2025/09/10', ''] 午日



# 天何言哉，叩之即應，富貴窮通，命運使然。遇事難斷，卜而決疑，惟神惟靈，實明我心。卦神在上，弟子誠心祈求靈卦， 弟子某某某要問某某事，請賜萬象六爻，斷驗如神，以決憂疑。謝卦神賜卦
# """
	# sixYaoMain( "+可否得到銀行offer//2025/06/05/21/22//11X0$X")
	# sixYaoMain( "瑞豐近況2//@@11@0//2025 ,07 14 18 35") ## 化退
	# sixYaoMain( "+蔡男占銀行貸款可否通過//癸卯,丁巳,乙亥,己酉//豐之離卦")

	# sixYaoMain("+甲辰年丙寅月辛丑日甲午//占下廣告對命理事業收入效益?//小畜之巽卦")	
	# sixYaoMain( "乾之同人//馬關條約" )

	# sixYaoMain( "+網上範例:打印機壞掉是否修的好//2020/3/25/13/36//困之解")

	# sixYaoMain( "0,1,00,11,0,1//2024 12 5 10 31//占今年幾時換工作較好" )
	# sixYaoMain( "+0,1,00,11,0,1//亥月,丙子日//占今年幾時換工作較好" ) ## 三合缺一待用
	# sixYaoMain( "27,55,22//乙月,丙子日//占今年幾時換工作較好" )
	# sixYaoMain( "+0,1,00,11,0,1//辛亥月乙卯日//占今年幾時換工作較好" )
	# print( unifiedData("""2025/10/22/18/15 - $00001
# 高雄場課程""", strong_sep='//', sep_for_app= "||") )
# 	sixYaoMain( """2025/10/22/18/15 - $00001
# 高雄場課程""" ) ## 三合局

	# sixYaoMain( "占今年幾時換工作較好//0,1,00,11,0,1" )
	# sixYaoMain( "2025/10/21/14/45 // X$1000 // 瑞豐最近的財運吉凶1021",showPic = True  )
	# sixYaoMain( "占今年幾時換工作較好好好好好好//27,71,42" )


	# sixYaoMain( "0,1,00,11,0,11" )
	# sixYaoMain( "+852,2492,253//乙月,丙子日//占今年幾時換工作較好" )

	# sixYaoMain( "101010.2.4//占看看今年幾時換工作較好" )
	# sixYaoMain( "0,1,00,11,0,1//占看看今年幾時換工作較好" )
	# sixYaoMain( "1,0,1,1,11,1//明天是否有工作" )

	# sixYaoMain( "001010.5//老人死//巳月乙卯日" )
	# sixYaoMain( "010110.2//老人死2//巳月丙辰日" )	

	# sixYaoMain( "大過之小過//測試//巳月丙辰日" )	
	# sixYaoMain( "艮之大過//占看看今年幾時換工作較好" )
	# sixYaoMain( "110011.2.5//占看看今年幾時換工作較好" )
	# sixYaoMain( "地水 3 4//測病//癸亥月乙酉日" )	

	# sixYaoMain( "漸之遁 //一二三四五六七八九十一二三四五六七八//2017.2.27.2.45" )
	# sixYaoMain( "姤之姤 //母病//己亥，丁卯，辛酉，壬辰" )
	# sixYaoMain( "2015/2/4/8/00 //山風之地風 //修橋" )


	# sixYaoMain( "大壯之大過//病//癸卯，丙辰，乙未" )
	# sixYaoMain( "X001$$//瑞豐近況" )
	# sixYaoMain( "訟之升//瑞豐近況" )
	# sixYaoMain( "+2025/8/29/16/50 // 1X000$ // 瑞豐近況0829",showPic = True )



