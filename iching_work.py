

import google.generativeai as genai
import json,re
import os

# 1. 設定你的 API KEY
genai.configure(api_key="AIzaSyCtkeSJz0guaPjN0kJwGub2_DDOmBdK9NY")


# 2. 標點符號對照表與邏輯設定
FULL_SHAPE = "，。！責？：；（）「」『』"
HALF_SHAPE = ",.!??:;()\"\"''"
PUNCT_TABLE = str.maketrans(FULL_SHAPE, HALF_SHAPE)

# def load_iching_db():
# 	try:
# 		with open('iching_data.json', 'r', encoding='utf-8') as f:
# 			return json.load(f)
# 	except FileNotFoundError:
# 		print("錯誤：找不到 iching_data.json 檔案！")
# 		return {}

def get_short_name(name):
	"""
	根據易經命名慣例提取簡稱：
	- 八純卦 (如：乾為天) -> 取第 1 個字 (乾)
	- 64 卦其餘卦 (如：雷山小過) -> 取後 2 個字 (小過)
	"""
	if len(name) == 3 and name[1] == '為':
		return name[0]
	elif len(name) >= 4:
		return name[-2:]
	elif len(name) >= 3:
		return name[-1]		
	return name

def solve_iching(base_name, change_name = None , homeMeaning = None, changeMeaning = None ):
	# db = load_iching_db()
	
	# 抓取資料
	# base_info = db.get(base_name)



	short_base = get_short_name(base_name)

	if change_name:
		# change_info = db.get(change_name)
		short_change = get_short_name(change_name)
		print( base_name , change_name)
		# if not base_info or not change_info: return "找不到卦名"
		print( short_base , short_change )
		# 動卦 Prompt：精簡範本，靠左對齊
		prompt = f"""你是誠懇的易經老師。模仿範本語氣, 150字內, 全半形標點, 禁止分段。
開頭必須是「{short_base}之{short_change}卦, 」.
【範本】: {short_base}之{short_change}卦,當前處於{short_base}階段,意謂著雖有小過非大礙,猶如雷在山下,宜居安思危、謹守小節。隨後的{short_change},則是火在水上,象徵新篇章將啟。當知所進退,穩步前行,轉機就在變化中。
【內容】: {short_base}({  homeMeaning  })轉至{short_change}({  changeMeaning  })。"""
# base_info.get('meaning')
	else:
		# if not base_info: return "找不到卦名"
		# 靜卦 Prompt：靠左對齊
		prompt = f"""你是誠懇的易經老師。解析「靜卦」, 120字內, 全半形標點。
開頭必須是「{short_base}卦, 」.
【範本】: {short_base}卦,局勢穩定,猶如{  homeMeaning  },核心在於守恆與深耕。不求劇烈變動,應專注內在修煉。建議保持定力,靜待時機成熟,穩中求進才是上策。
【內容】: {base_name} 的意義是: {  homeMeaning  }。"""

	# 建議使用 1.5-flash, 額度較穩且不影響這種文字解析品質
	model = genai.GenerativeModel("models/gemini-2.5-flash-lite")
	# model = genai.GenerativeModel("gemini-1.5-flash-latest")	
	try:
		response = model.generate_content(prompt)
		txt = response.text.strip()

		# 1. 暴力去油：確保從卦名開始
		txt = re.sub(r"^[^" + short_base + "]*", "", txt)
		
		# 2. 強制全形轉半形
		final = txt.translate(PUNCT_TABLE)
		
		# 3. 增加視覺呼吸感：逗號與句號後加一格空格 (Line 閱讀較輕鬆)
		# final = final.replace(",", ", ").replace(".", ". ")
		
		return final.strip()

	except Exception as e:
		return f"分析時發生錯誤: {str(e)}"

# 5. 執行測試
if __name__ == "__main__":
	# 測試八純卦與四字卦的組合
	result = solve_iching("水火既濟", "澤火革")
	print(f"--- 測試結果 ---\n{result}")



