# print = lambda *args, **kwargs: None

def print_threeho_table(zhis_list):

	threeHo_dict = {
		"木": ["亥", "卯", "未"],
		"火": ["寅", "午", "戌"],
		"金": ["巳", "酉", "丑"],
		"水": ["申", "子", "辰"]
	}

	element_code = {
		"木": "a",
		"火": "b",
		"金": "c",
		"水": "d"
	}

	for elem, group in threeHo_dict.items():
		prefix = element_code[elem]
		line = []
		for i, z in enumerate(group):
			if z in zhis_list:
				# print( z , prefix)
				line.append(f"{z}-O{prefix}{i}")                
			# else:
			#     line.append("-")
		print(" 。".join(line))

def combineListFun(newDataList, orgDataList):
	# print()
	# print("newDataList - ", newDataList)
	# print("orgDataList - ", orgDataList)
	# print()

	length = min(len(newDataList), len(orgDataList))

	# 先找出 orgDataList 中 O 開頭元素的代號(例如 Oa2 → a2)
	o_codes = set()
	for item in orgDataList:
		if isinstance(item, str) and item.startswith("O") and len(item) > 1:
			o_codes.add(item[1:])  # 把 a2 存起來

	# print("O codes:", o_codes)

	# 先把 newDataList 中與 O code 衝突的 P 項目清掉
	cleaned_new = []
	for item in newDataList:
		if isinstance(item, str) and item.startswith("P"):
			code = item[1:]
			if code in o_codes:   # 與 O 衝突 → 不要
				cleaned_new.append('-')
				continue
		cleaned_new.append(item)

	# 合併邏輯(原本的)
	combined = []
	for i in range(length):
		if orgDataList[i] != '-':
			combined.append(orgDataList[i])
		else:
			combined.append(cleaned_new[i])

	return combined


# def combineListFun( newDataList , orgDataList ):
# 	print()
# 	print( "newDataList - " , newDataList )
# 	print( "orgDataList - " , orgDataList )
# 	print()
# 	# if newDataList is None:
# 	#     newDataList = ['-', '-', '-', '-', '-', 'Oa1']
# 	# if orgDataList is None:
# 	#     orgDataList = ['-', 'Oc3', '-', 'Ob1', '-', '-']
# 	# print(">>>",newDataList)
# 	# 確保兩個列表長度相同,取最短長度
# 	length = min(len(newDataList), len(orgDataList))
	
# 	combined = []
# 	for i in range(length):
# 		if orgDataList[i] != '-':
# 			combined.append(orgDataList[i])
# 		else:
# 			combined.append(newDataList[i])
# 	# print ( ">" , combined )
# 	return combined


# ## print的關閉功能
# def print( *n ):
# 	pass


def get_missing_zhis( bufs , mode ):
	"""
	找出三合組中,哪些地支還沒被標記到,比如亥卯未缺卯,回傳卯,亥卯未缺亥卯,回傳亥卯
	
	:param bufs: list of list,例如 [homeBuf, changeBuf, month_day_Buf]
	:param mode: 三合組,例如 ["亥", "卯", "未"]
	:return: list,剩下沒被標記的地支
	"""
	modeBuf = mode.copy()
	# 把所有 buf 平攤處理
	for buf_list in bufs:
		for buf in buf_list:
			if buf != "-":
				# print( buf[-1] )
				idx = int(buf[-1])   # "Oa0" → 0
				if mode[idx] in modeBuf:
					modeBuf.remove(mode[idx])

	return modeBuf


# 取得地支
def get_zhi(ganzi_str):
	if ganzi_str == 'X':
		return 'X'
	if "月" in ganzi_str:
		return ganzi_str[0]  # "申月" -> "申"
	return ganzi_str[-1]     # "甲申" -> "申"




## 重新檢查是否有重複的數字
def refinding(  orgItemList , indexList ):
	newList = ['-'] * 6
	# homeBuf   -  ['-', 'Pc2', '-', 'Pc1', '-', 'Oc0']
	for indexItem in indexList:
		if indexItem == "-":
			continue

		indexBuf = indexItem[-1]
		# for each in homeAllBuf:
		for i, each in enumerate( orgItemList):
			# print( each , str(indexItem))
			if each[-1] == indexBuf:
				# print("get!")
				newList[i] = "-"
			else:
				newList[i] = each
	return newList






def threeHoTest(
				monthGanZi, 
				dayGanZi, 
				home_naGia, 
				changeIdIndex, 
				change_naGia, 
				hide_naGia
				):



	# 取得月支和日支
	month_zhi = get_zhi(monthGanZi)
	day_zhi   = get_zhi(dayGanZi)

	# 收集本卦 / 變卦 / 伏神 地支
	home_zhis   = [get_zhi(gz) for gz in home_naGia ]
	if change_naGia != None:
		change_zhis = [get_zhi(gz) for gz in change_naGia ] ## ['己卯', '己丑', '己亥', '戊申', '戊戌', '戊子'] to ['卯', '丑', '亥', '申', '戌', '子']
	else:
		change_zhis = ['-'] * 6
	hide_zhis   = [get_zhi(h) if h != 'X' else 'X' for h in hide_naGia]


	# 三合對照表,優先順序 木a → 火b → 金c → 水d
	threeHo_dict = {
		"木": ["亥", "卯", "未"],  
		"火": ["寅", "午", "戌"],  
		"金": ["巳", "酉", "丑"],  
		"水": ["申", "子", "辰"]
	}

	# 屬性對照表
	element_code = {
		"木": "a",
		"火": "b", 
		"金": "c",
		"水": "d"
	}

	# 初始化結果
	homeThreeHoId       = ['-'] * 6
	changeThreeHoId     = ['-'] * 6
	month_day_ThreeHoId = ['-', '-']


	clear_homeId      = ['-'] * 6
	clear_changeId   = ['-'] * 6
	clear_month_dayId = ['-', '-']

	
	O_mode_total = 0 ## 三合全有的數量
	P_mode_total = 0 ## 缺一待補的數量

	# === 用來快速標註三合 ===
	def mark_threeho( zhi, group, prefix ):
		if zhi in group:
			idx = str(group.index(zhi))
			return f"{prefix}{idx}"
		return "-"


	for type in threeHo_dict:
		# === 先處理本卦 ===
		# typeMode = threeHo_dict["木"]   # 這裡先只跑木局
		typeMode = threeHo_dict[ type ]
		typeCode = element_code[ type ]
		# 初始化
		homeBuf   = ['-'] * 6
		homeAllBuf   = ['-'] * 6 ## 所有的爻,包括靜爻       
		changeBuf = ['-'] * 6

		prefix = "O" + typeCode   # 之後可以改 Ob, Oc, Od
		prefix_P = "P" + typeCode   # 之後可以改 Ob, Oc, Od

		# ============================================================
		# 【修改1】處理 D 位置：只有在 O 位置沒有相同地支時才標記
		# ============================================================
		# 先收集所有 O 位置的地支
		o_position_zhis = set()
		for i, ind in enumerate(changeIdIndex):
			if ind == "O":
				o_position_zhis.add(home_zhis[i])
		
		# 處理 homeBuf
		for i, z in enumerate(home_zhis):
			## 動爻
			if changeIdIndex[i] == "O":
				code = mark_threeho(z, typeMode, prefix)
				if code != "-":
					homeBuf[i] = code
			
			## 暗動：只有當 O 位置沒有相同地支時才標記
			elif changeIdIndex[i] == "D":
				if z not in o_position_zhis:  # O位置沒有這個地支才標記
					code = mark_threeho(z, typeMode, prefix)
					if code != "-":
						homeBuf[i] = code
			
			## 靜爻
			else:
				code = mark_threeho(z, typeMode, prefix_P)  ## 針對靜爻用 P 模式
				if code != "-":
					homeAllBuf[i] = code
		# ============================================================

		# 處理 changeBuf
		for i, z in enumerate(change_zhis):
			if changeIdIndex[i] == "O":
				code = mark_threeho(z, typeMode, prefix)
				if code != "-":
					changeBuf[i] = code


		# === 對照 homeBuf / changeBuf 決定最終標記 ===
		for i in range(6):
			if changeBuf[i] == "-":
				continue
			# 如果變卦同樣出現在本卦標記 → 不用重複標
			if changeBuf[i] in homeBuf:
				changeBuf[i] = "-"
				continue
			# 如果變卦同組出現多次,要依據本卦有沒有相同支判斷
			if changeBuf.count(changeBuf[i]) > 1:
				# print(changeBuf.count(changeBuf[i]) , changeBuf[i])
				if home_zhis[i] not in typeMode:     # 本卦有對應的話就可以留
					# print( i , home_zhis[i] )
					# print( changeBuf[i] ,' -- ', changeBuf[i]  )
					changeBuf[i] = "-"


		# === 日月補缺判斷 ===
		# 先找目前已標記的地支
		typeModeBuf = typeMode.copy()
		num = 0

		for i, ind in enumerate(changeIdIndex):
			if ind == "X":
				continue

			if home_zhis[i] in typeModeBuf:
				num += 1
				# print("home", home_zhis[i])
				typeModeBuf.remove(home_zhis[i])

			if change_zhis[i] in typeModeBuf:
				num += 1
				# print("change", change_zhis[i])
				typeModeBuf.remove(change_zhis[i])

		typeModeBuf = get_missing_zhis([homeBuf, changeBuf], typeMode)
		print("六爻未標記的地支:      ", typeModeBuf)

		# 補月日
		month_day_Buf = ["X", "X"]

		# --- 準備一份暫存,先嘗試補
		temp_missing = typeModeBuf.copy()
		tempBuf = ['-', '-']         # [月, 日] 暫存
		
		# ============================================================
		# 【修改2】月日補缺：跳過三合中間的地支（索引1）
		# ============================================================
		# 注意:這裡「先試日」後試月→ 日優先
		print( temp_missing )
		if len(temp_missing) == 2:
			# 先用「日」補
			if day_zhi in temp_missing:
				day_idx = typeMode.index(day_zhi)
				if day_idx != 1:  # 不是中間的地支才補
					tempBuf[1] = f"{prefix}{day_idx}"
					temp_missing.remove(day_zhi)
			# 再用「月」補
			if month_zhi in temp_missing:
				month_idx = typeMode.index(month_zhi)
				if month_idx != 1:  # 不是中間的地支才補
					tempBuf[0] = f"{prefix}{month_idx}"
					temp_missing.remove(month_zhi)

		elif len(temp_missing) == 1:
			need = temp_missing[0]
			need_idx = typeMode.index(need)
			
			# 先看「日」
			if day_zhi == need and need_idx != 1:  # 不是中間才補 日月如果為帝旺位則跳過
				tempBuf[1] = f"{prefix}{need_idx}"
				temp_missing.clear()
			# 再看「月」
			elif month_zhi == need and need_idx != 1:  # 不是中間才補
				tempBuf[0] = f"{prefix}{need_idx}"
				temp_missing.clear()
		# ============================================================

		# 收尾:若月日同支而兩邊都被暫時填了 → 只留「日」
		if month_zhi == day_zhi and tempBuf[0] != '-' and tempBuf[1] != '-':
			tempBuf[0] = '-'

		# 寫回你的變數
		month_day_Buf = tempBuf


		if len(get_missing_zhis([homeBuf, changeBuf, month_day_Buf], typeMode )) == 0:
			O_mode_total += 1
			print( "O type +1:" , type )

		## 缺一待用
		homeAllBuf = refinding( homeAllBuf , month_day_Buf )
		if  len(get_missing_zhis([homeBuf, changeBuf, month_day_Buf], typeMode )) == 1 and len(get_missing_zhis( [homeAllBuf ,homeBuf, changeBuf, month_day_Buf], typeMode )) == 0:


			homeBuf = combineListFun( newDataList = homeAllBuf , orgDataList = homeBuf )
			P_mode_total += 1 ## 缺一待補的數量
			clear_homeIdBuf      = ['X' if x != '-' else '-' for x in homeBuf]
			# ['Oa2', '-', 'Pa1', '-', '-', '-'] -> ['X', '-', 'X', '-', '-', '-']
			clear_changeIdBuf    = ['X' if x != '-' else '-' for x in changeBuf]
			clear_month_dayIdBuf = ['X' if x != '-' else '-' for x in month_day_Buf]
			# print(">>>", homeBuf,clear_homeIdBuf)

			# clear_homeIdBuf = []
			# for x in homeBuf:
			#     if x != '-':
			#         clear_homeIdBuf.append('X')
			#     else:
			#         clear_homeIdBuf.append('-')


			# print( clear_homeId,clear_changeId,clear_month_dayId)
			print ( "for get index:")
			clear_homeId = combineListFun( newDataList = clear_homeIdBuf , orgDataList = clear_homeId )
			clear_changeId = combineListFun( newDataList = clear_changeIdBuf , orgDataList = clear_changeId )
			clear_month_dayId = combineListFun( newDataList = clear_month_dayIdBuf , orgDataList = clear_month_dayId )
			print()



		checkLose = get_missing_zhis([homeBuf, changeBuf, month_day_Buf], typeMode )
		print("六爻+日月未被標記的地支:", checkLose)

		print()
		print( "type - " , type )
		print( "homeBuf   - ",homeBuf )
		print( "changeBuf - ",changeBuf )
		print( "month_day_Buf - ",month_day_Buf )
		print( "after combine:")
		# --- 只有當三合湊齊時才正式標
		if not checkLose:   # temp_missing 空代表三個都找到
			month_day_Buf = tempBuf
		else:
			month_day_Buf = ["-", "-"]   # 不完整 → 直接放棄
			homeBuf   = ['-'] * 6
			changeBuf = ['-'] * 6



		# === 最後指定本卦 ===
		# homeThreeHoId = homeBuf
		# changeThreeHoId = changeBuf
		# month_day_ThreeHoId = month_day_Buf

		# print(homeBuf,homeThreeHoId)
		# print(changeBuf,changeThreeHoId)
		# print(month_day_Buf,month_day_ThreeHoId)
		homeThreeHoId = combineListFun( newDataList = homeBuf , orgDataList = homeThreeHoId )
		changeThreeHoId = combineListFun( newDataList = changeBuf , orgDataList = changeThreeHoId )
		month_day_ThreeHoId = combineListFun( newDataList = month_day_Buf , orgDataList = month_day_ThreeHoId ) 
		print("------------------------------------------------------- end of",type)
	if O_mode_total > 2:
		month_day_ThreeHoId = ["-", "-"]   # 不完整 → 直接放棄
		homeThreeHoId   = ['-'] * 6
		changeThreeHoId = ['-'] * 6

	if O_mode_total > 0:
		print( O_mode_total )
		print ( "clear P mode")
		homeThreeHoId = [ '-' if clear_homeId[i] == 'X' else homeThreeHoId[i] for i in range(len(homeThreeHoId)) ]
		changeThreeHoId = [ '-' if clear_changeId[i] == 'X' else changeThreeHoId[i] for i in range(len(changeThreeHoId)) ]
		month_day_ThreeHoId = [ '-' if clear_month_dayId[i] == 'X' else month_day_ThreeHoId[i] for i in range(len(month_day_ThreeHoId)) ]

	if P_mode_total > 1:
		print( P_mode_total )
		print ( "clear P mode")
		homeThreeHoId = [ '-' if clear_homeId[i] == 'X' else homeThreeHoId[i] for i in range(len(homeThreeHoId)) ]
		changeThreeHoId = [ '-' if clear_changeId[i] == 'X' else changeThreeHoId[i] for i in range(len(changeThreeHoId)) ]
		month_day_ThreeHoId = [ '-' if clear_month_dayId[i] == 'X' else month_day_ThreeHoId[i] for i in range(len(month_day_ThreeHoId)) ]

	# print( clear_homeId )
	# print( clear_changeId )
	# print( clear_month_dayId )
	# print ( P_mode_total )
	# print_threeho_table(typeMode)
	print("\n================================================================" )    
	print("index         ", changeIdIndex)
	print("home_zhis     ", home_zhis)
	print("change_zhis   ", change_zhis)
	print("月日          ", [month_zhi,day_zhi] )
	print("")
	print("homeThreeHoId ", homeThreeHoId)
	print("changeThreeHoId", changeThreeHoId)
	print("month_day_ThreeHoId:", month_day_ThreeHoId)
	# print("\n\n\n")

		# return homeThreeHoId, changeThreeHoId, month_day_ThreeHoId

	return homeThreeHoId, changeThreeHoId, month_day_ThreeHoId




# 測試
# result = combineListFun()
# print(result)  # ['-', 'Oc3', '-', 'Ob1', '-', 'Oa1']






if __name__ == '__main__':
	threeHoTest(
				 # monthGanZi = "戊午",
				 # dayGanZi = "癸亥",
				 # changeIdIndex = ['X', 'O', 'O', 'X', 'O', 'O'],
				 # home_naGia = ['庚子', '庚寅', '庚辰', '辛未', '辛巳', '辛卯'],
				 # hide_naGia = ['X', 'X', '辛酉', 'X', 'X', 'X'],
				 # change_naGia = ['己卯', '己丑', '己亥', '戊申', '戊戌', '戊子']


				monthGanZi = "丁卯",
				dayGanZi = "丙申",
				changeIdIndex = ['O', 'X', 'X', 'X', 'O', 'X'],
				home_naGia = ['乙未', '乙巳', '乙卯', '丁亥', '丁酉', '丁未'],
				hide_naGia = ['X', 'X', 'X', 'X', 'X', 'X'],
				change_naGia = ['庚子', '庚寅', '庚辰', '庚午', '庚申', '庚戌']




				# monthGanZi = "己卯",
				# dayGanZi = "戊戌",
				# changeIdIndex = ['X', 'X', 'X', 'X', 'O', 'O'],
				# home_naGia = ['辛丑', '辛亥', '辛酉', '丁亥', '丁酉', '丁未'],
				# hide_naGia = ['X', '庚寅', 'X', '庚午', 'X', 'X'],
				# change_naGia = ['辛丑', '辛亥', '辛酉', '己酉', '己未', '己巳']
				# monthGanZi = "卯月",
				# dayGanZi = "丁巳",
				# changeIdIndex = ['O', 'X', 'O', 'O', 'X', 'O'],
				# home_naGia = ['己卯', '己丑', '己亥', '己酉', '己未', '己巳'],
				# hide_naGia = ['X', 'X', 'X', 'X', 'X', 'X'],
				# change_naGia = ['乙未', '乙巳', '乙卯', '癸丑', '癸亥', '癸酉']
				)
	# a =  combineListFun(  ['-', 'Oc1', '-', '-', '-', '-'] ,   ['-', '-', '-', '-', '-', 'Oc2'] ) 
	# print(a)

# sixYaoMain( "巳年卯月戊戌日//大過之鼎卦")


