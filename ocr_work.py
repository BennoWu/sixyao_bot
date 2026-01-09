# -*- coding: utf-8 -*-

from PIL import Image
import re
from fourPillar_tool import getFourPillar # 四柱得日期

## 原本的OCR，可用但太吃系統

# import numpy as np
# from paddleocr import PaddleOCR

# # 初始化 OCR（中文+英文）
# ocr = PaddleOCR(use_angle_cls=True, lang="ch")

# def space_ocr_image_to_text(img):
#     """
#     輸入 PIL Image 或路徑字串，返回辨識到的文字（連成一行）
#     """
#     if isinstance(img, str):
#         results = ocr.ocr(img, cls=True)
#     else:
#         results = ocr.ocr(np.array(img), cls=True)
	
#     text_list = []
#     all_text = ""
#     for line in results[0]:
#         text = line[1][0]
#         text_list.append(text)
#         all_text += " " + text
#     return all_text



################################################################################
# OCR SPACE
################################################################################
import requests
from PIL import Image
from io import BytesIO

def space_ocr_image_to_text(input_data, timeout_sec=5):
	"""
	OCR.space OCR
	input_data: 檔案路徑(str) / PIL Image / bytes
	timeout_sec: 超時秒數
	"""
	url = 'https://api.ocr.space/parse/image'
	data_payload = {
		'apikey': 'K82723710988957',  # 你的 API Key
		'language': 'cht',
		'detectOrientation': False
	}

	# 將 input_data 統一轉成 bytes
	if isinstance(input_data, str):
		with open(input_data, 'rb') as f:
			img_bytes = f.read()
	elif isinstance(input_data, Image.Image):
		img_byte_arr = BytesIO()
		input_data.save(img_byte_arr, format='PNG')
		img_byte_arr.seek(0)
		img_bytes = img_byte_arr.getvalue()
	elif isinstance(input_data, bytes):
		img_bytes = input_data
	else:
		raise TypeError("input_data 必須是檔案路徑(str)、PIL Image 或 bytes")

	# Thread + 超時
	import threading
	result_holder = {}

	def call_ocr_space():
		try:
			response = requests.post(
				url,
				files={'file': ('image.png', img_bytes, 'image/png')},
				data=data_payload
			)
			result = response.json()
			if result.get('IsErroredOnProcessing', True):
				result_holder['text'] = None
			else:
				result_holder['text'] = result['ParsedResults'][0]['ParsedText']
		except Exception as e:
			result_holder['text'] = None
			result_holder['error'] = e

	thread = threading.Thread(target=call_ocr_space)
	thread.start()
	thread.join(timeout=timeout_sec)

	if thread.is_alive():
		return None
	return result_holder.get('text', None)


################################################################################
# VERYFI OCR
################################################################################




# Veryfi Key 設定
CLIENT_ID = "vrfCRJyK5KBmPRRSUGYUmonrpZUDn9SrcbfdwRB"
CLIENT_SECRET = "7TEsTdHNEyeUGuA4CDR3v2ocYAMafAif0tnKcywtKw2mWZmLE1I6GtEpAC2dMUzPw7tFZZzOL77o4XidfNCaaAKkvVeDlYDAWZ4zF2daMSoKPIhbrGIIILYMBBAnslrY"
USERNAME = "benno.wu"  # 通常是 email
API_KEY = "036e986501481a3cfb2d642c9d4dc0b0"


import io
import requests
import threading
from PIL import Image

# 全域 Session，保持長連接是唯一有效的加速手段
session = requests.Session()

def veryfi_ocr_image_to_text(input_image, timeout_sec=10):
    """
    極速版：不縮小、不轉灰階，僅透過記憶體直傳 API
    """

    # --- 自動相容邏輯 ---
    # 如果傳進來的是字串（路徑），幫忙 open 它
    if isinstance(input_image, str):
        input_image = Image.open(input_image)


    # if not isinstance(input_image, Image.Image):
    #     return None

    # 1. 直接將原圖轉為 BytesIO (保持原始解析度與顏色)
    # 使用 PNG 雖然較大，但在某些環境下編碼速度比 JPEG 快
    img_byte_arr = io.BytesIO()
    input_image.save(img_byte_arr, format='PNG')
    img_data = img_byte_arr.getvalue()

    headers = {
        "Client-Id": CLIENT_ID,
        "Authorization": f"apikey {USERNAME}:{API_KEY}",
        "Accept": "application/json"
    }

    result_holder = {"text": None, "error": None}

    def call_api():
        try:
            # 直接使用 multipart/form-data 傳送 Bytes
            files = {'file': ('crop.png', img_data, 'image/png')}
            # files = {'file': ('crop.webp', img_data, 'image/webp')}
            response = session.post(
                "https://api.veryfi.com/api/v8/partner/documents",
                headers=headers,
                files=files,
                timeout=timeout_sec
            )
            
            if response.status_code in [200, 201]:
                result_holder['text'] = response.json().get("ocr_text", "")
            else:
                result_holder['error'] = response.status_code
        except Exception as e:
            result_holder['error'] = str(e)

    # 這裡可以根據你的 Bot 框架決定是否保留 threading
    # 如果是單人使用的 Bot，直接執行 call_api() 甚至會更快
    call_api() 

    return result_holder['text']
# -------------------- 範例測試 --------------------
# if __name__ == "__main__":
#     img = Image.open("test.jpg")
#     sub_crop = img.crop((0, 0, 500, 500))  # 隨便 crop
#     text = veryfi_ocr_image_to_text(sub_crop, timeout_sec=10)
#     print("OCR 結果:", text)



# -------------------- 範例測試 --------------------
# if __name__ == "__main__":
#     img = Image.open("test.jpg")
#     sub_crop = img.crop((0, 0, 500, 500))  # 隨便 crop
#     text = veryfi_ocr_image_to_text(sub_crop, timeout_sec=10)
#     print("OCR 結果:", text)


# ################################################################################
# # 測試範例
# ################################################################################
# if __name__ == "__main__":
#     from PIL import Image

#     # 測試檔案路徑
#     text1 = space_ocr_image_to_text("test.jpg", timeout_sec=5)
#     print("OCR.space:", text1)

#     text2 = veryfi_ocr_image_to_text("test.jpg", timeout_sec=5)
#     print("Veryfi:", text2)

#     # 測試 PIL Image
#     img = Image.open("test.jpg")
#     text3 = space_ocr_image_to_text(img)
#     text4 = veryfi_ocr_image_to_text(img)
#     print("OCR.space (PIL):", text3)
#     print("Veryfi (PIL):", text4)

#     # 測試 bytes
#     with open("test.jpg", "rb") as f:
#         img_bytes = f.read()
#     text5 = space_ocr_image_to_text(img_bytes)
#     text6 = veryfi_ocr_image_to_text(img_bytes)
#     print("OCR.space (bytes):", text5)
#     print("Veryfi (bytes):", text6)















# import requests
# # from PIL import Image
# from io import BytesIO


# # OCR SPACE
# ################################################################################
# import requests
# # from PIL import Image
# from io import BytesIO
# import threading

# def space_ocr_image_to_text(input_data, timeout_sec=3):
# 	"""
# 	自動判斷輸入類型並進行 OCR.space
# 	input_data: 可以是檔案路徑(str) 或 PIL Image 物件
# 	timeout_sec: 超時秒數，防止卡住
# 	"""
# 	url = 'https://api.ocr.space/parse/image'
# 	data_payload = {
# 		'apikey': 'K82723710988957',  # 你的 API Key
# 		'language': 'cht',
# 		'detectOrientation': False,  # 強制橫排
# 	}

# 	# 將圖像轉成 bytes
# 	if isinstance(input_data, str):
# 		with open(input_data, 'rb') as f:
# 			img_bytes = f.read()
# 	elif isinstance(input_data, Image.Image):
# 		img_byte_arr = BytesIO()
# 		input_data.save(img_byte_arr, format='PNG')
# 		img_byte_arr.seek(0)
# 		img_bytes = img_byte_arr.getvalue()
# 	else:
# 		raise TypeError("input_data 必須是檔案路徑(str)或 PIL Image 物件")

# 	result_holder = {}

# 	def call_ocr_space():
# 		try:
# 			response = requests.post(
# 				url,
# 				files={'file': ('image.png', img_bytes, 'image/png')},
# 				data=data_payload
# 			)
# 			result = response.json()
# 			if result['IsErroredOnProcessing']:
# 				result_holder['text'] = None
# 			else:
# 				result_holder['text'] = result['ParsedResults'][0]['ParsedText']
# 		except Exception as e:
# 			result_holder['text'] = None
# 			result_holder['error'] = e

# 	thread = threading.Thread(target=call_ocr_space)
# 	thread.start()
# 	thread.join(timeout=timeout_sec)  # 超時跳出

# 	if thread.is_alive():
# 		return None  # 超時
# 	return result_holder.get('text', None)


# # 範例測試
# if __name__ == "__main__":
#     from PIL import Image
#     img = Image.open("test.jpg")
#     text = space_ocr_image_to_text(img, timeout_sec=5)
#     print(text)


# # OCR SPACE
# ################################################################################
# def space_ocr_image_to_text(input_data):
# 	"""
# 	自動判斷輸入類型並進行 OCR
# 	input_data: 可以是檔案路徑(str) 或 PIL Image 物件
# 	"""
# 	url = 'https://api.ocr.space/parse/image'
# 	data_payload = {
# 		'apikey': 'K82723710988957',
# 		'language': 'cht',
# 		'detectOrientation': False,  # 強制橫排
# 	}
# 	# 判斷輸入類型
# 	if isinstance(input_data, str):
# 		# 是字串 → 當作檔案路徑處理
# 		with open(input_data, 'rb') as f:
# 			response = requests.post(
# 				url,
# 				files={'file': f},
# 				data=data_payload
# 			)
	
# 	elif isinstance(input_data, Image.Image):
# 		# 是 PIL Image 物件
# 		img_byte_arr = BytesIO()
# 		input_data.save(img_byte_arr, format='PNG')
# 		img_byte_arr.seek(0)
		
# 		response = requests.post(
# 			url,
# 			files={'file': ('image.png', img_byte_arr, 'image/png')},
# 			data=data_payload
# 		)
	
# 	else:
# 		raise TypeError("input_data 必須是檔案路徑(str)或 PIL Image 物件")
	
# 	# 解析結果
# 	result = response.json()
# 	if result['IsErroredOnProcessing']:
# 		return None
# 	print(result['ParsedResults'][0] )
# 	return result['ParsedResults'][0]['ParsedText']


## 用陰曆反對陽曆
## 1 把國字日期改成數字
## 2 用sxtwl的程式轉成國曆 (他不吃中文只吃數字)
import sxtwl

# CN_NUM = {
# 	"〇": 0, "○": 0, "零": 0,
# 	"一": 1, "二": 2, "三": 3, "四": 4,
# 	"五": 5, "六": 6, "七": 7, "八": 8, "九": 9
# }
CN_NUM = {
	"〇": 0, "◯": 0, "○": 0, "零": 0,  # 🔥 加入 ○
	"一": 1, "二": 2, "三": 3, "四": 4,
	"五": 5, "六": 6, "七": 7, "八": 8, "九": 9
}

CN_DAY = {
	"初一": 1, "初二": 2, "初三": 3, "初四": 4, "初五": 5,
	"初六": 6, "初七": 7, "初八": 8, "初九": 9, "初十": 10,
	"十一": 11, "十二": 12, "十三": 13, "十四": 14, "十五": 15,
	"十六": 16, "十七": 17, "十八": 18, "十九": 19,
	"二十": 20, "廿一": 21, "廿二": 22, "廿三": 23, "廿四": 24,
	"廿五": 25, "廿六": 26, "廿七": 27, "廿八": 28, "廿九": 29,
	"三十": 30
}

ZHI_HOUR = {
	"子": 23, "丑": 1, "寅": 3, "卯": 5,
	"辰": 7, "巳": 9, "午": 11, "未": 13,
	"申": 15, "酉": 17, "戌": 19, "亥": 21
}

def parse_lunar_text(text):
	"""
	解析農曆文本
	返回: (年, 月, 日, 時) 或 None
	"""
	# 🔥 檢查是否有「閏」字,有的話直接跳過
	if '閏' in text:
		print("⚠️ 偵測到閏月,目前不支援,跳過此筆資料")
		return None
	
	# 用正則抓取「年份 + 月日 + 時辰」
	match = re.search(
		r'[一二三四五六七八九十○◯〇零]{4}年[正一二三四五六七八九十]+月[初十廿卅三]{1,3}[一二三四五六七八九十]日?[子丑寅卯辰巳午未申酉戌亥]時',
		text
	)
	if not match:
		return None
	
	date_text = match.group()
	print("OCR取得陰曆: " + date_text)
	
	try:
		# 年
		y_txt = re.search(r"(.*)年", date_text).group(1)
		year = int("".join(str(CN_NUM[c]) for c in y_txt))
		
		# 月
		m_txt = re.search(r"年(.*?)月", date_text).group(1)
		month = CN_DAY.get(m_txt, 10 if m_txt == "十" else None)
		
		# 日
		d_txt = re.search(r"月(.*?)([子丑寅卯辰巳午未申酉戌亥])", date_text).group(1)
		day = CN_DAY[d_txt]
		
		# 時
		zhi = re.search(r"([子丑寅卯辰巳午未申酉戌亥])時", date_text).group(1)
		hour = ZHI_HOUR[zhi]
		
		return year, month, day, hour
		
	except Exception as e:
		print(f"解析農曆文本失敗: {e}")
		return None


def lunar_to_solar(text):
	"""
	農曆轉陽曆
	"""
	result = parse_lunar_text(text)
	# print( result ) #(2025, 10, 24, 21) 正確會取得這種格式
	if not result:
		return None
	
	lunar_y, lunar_m, lunar_d, hour = result
	
	try:
		# 生成農曆對應的陽曆日 (False = 不是閏月)
		solar_day = sxtwl.Day_fromLunar(lunar_y, lunar_m, lunar_d, False)
		
		# 🔥 用方法取得年月日
		year = solar_day.getSolarYear()
		month = solar_day.getSolarMonth()
		day = solar_day.getSolarDay()
		
		rtmDate = f"{year}/{month}/{day}/{hour}/00"
		return rtmDate
		
	except Exception as e:
		print(f"農曆轉陽曆失敗: {e}")
		return None


import re

# 農曆日、月對照表
datBuf = {
	1:"初一",2:"初二" ,3:"初三" ,4:"初四" ,5:"初五" ,6:"初六" ,7:"初七" ,8:"初八" ,9:"初九" ,10:"初十" ,
	11:"十一" ,12:"十二" ,13:"十三" ,14:"十四" ,15:"十五" ,16:"十六" ,17:"十七" ,18:"十八" ,19:"十九" ,20:"二十" ,
	21:"廿一" ,22:"廿二" ,23:"廿三" ,24:"廿四" ,25:"廿五" ,26:"廿六" ,27:"廿七" ,28:"廿八" ,29:"廿九" ,30:"三十" 
}
monthBuf = {
	1:"正月",2:"二月" ,3:"三月" ,4:"四月" ,5:"五月" ,6:"六月" ,7:"七月" ,8:"八月" ,9:"九月" ,10:"十月" ,11:"十一月" ,12:"十二月"
}

def getDarkDateOcr(ocr_txt, date_tuple):
	"""
	OCR 文本 + tuple 比對，農曆月日 & 日柱地支是否一致
	date_tuple = ('2025/12/24/11:27', '十一月初五', ['乙巳','戊子','丁卯','丙午'], ['冬至','>','小寒'], '(三)', '11:27')
	"""
	# ========================
	# 0️⃣ OCR 文本清理
	# ========================
	text = ocr_txt.replace("ㄧ", "1").replace("○", "0").replace("◯", "0").replace("〇", "0")
	text = re.sub(r"\s+", "", text)
	
	print(f"清理後文本: {text}")
	
	# ========================
	# 1️⃣ 從 OCR 文本抓農曆月日
	# ========================
	m_md = re.search(
		r"([正一二三四五六七八九十冬臘腊]+)月([初十廿卅一二三四五六七八九]+)", 
		text
	)
	month_ocr = m_md.group(1) if m_md else None
	day_ocr = m_md.group(2) if m_md else None
	
	print(f"OCR 月份: {month_ocr}, 日期: {day_ocr}")
	
	# ========================
	# 2️⃣ 從 OCR 文本抓地支
	# ========================
	m_zhi = re.search(r"(子|丑|寅|卯|辰|巳|午|未|申|酉|戌|亥)", text)
	zhi_ocr = m_zhi.group(1) if m_zhi else None
	
	print(f"OCR 地支: {zhi_ocr}")
	
	# ========================
	# 3️⃣ 從 tuple 拿資料
	# ========================
	lunar_md = date_tuple[1]          # '十一月初五'
	day_zhi = date_tuple[2][3]        # '丙午'
	
	# 抓 tuple 日柱地支
	m_day_zhi = re.search(r"(子|丑|寅|卯|辰|巳|午|未|申|酉|戌|亥)$", day_zhi)
	day_zhi_only = m_day_zhi.group(1) if m_day_zhi else None
	
	print(f"Tuple 農曆: {lunar_md}, 日柱地支: {day_zhi_only}")
	
	# ========================
	# 4️⃣ 農曆月日比對
	# ========================
	# tuple 月日拆開
	m_match = re.match(r"(.+)月(.+)", lunar_md)
	tuple_month, tuple_day = m_match.groups() if m_match else (None, None)
	
	# 🔥 月份轉數字（處理冬月、臘月）
	def month_to_num(m_text):
		if not m_text:
			return None
		
		# 統一加上「月」字
		if "月" not in m_text and "冬" not in m_text and "臘" not in m_text and "腊" not in m_text:
			m_text = m_text + "月"
		
		# 特殊月份處理
		if "冬" in m_text:
			return 11
		if "臘" in m_text or "腊" in m_text:
			return 12
		
		# 一般月份
		for k, v in monthBuf.items():
			if isinstance(k, int) and v == m_text:
				return k
		
		return None










	
	month_num = month_to_num(month_ocr)
	tuple_month_num = month_to_num(tuple_month)
	print(f"月份數字 - OCR: {month_num}, Tuple: {tuple_month_num}")
	print( tuple_month )
	
	# 日期轉數字
	day_num = None
	for k, v in datBuf.items():
		if v == day_ocr:
			day_num = k
			break
	
	tuple_day_num = None
	for k, v in datBuf.items():
		if v == tuple_day:
			tuple_day_num = k
			break
	
	print(f"日期數字 - OCR: {day_num}, Tuple: {tuple_day_num}")
	
	# ========================
	# 5️⃣ 判斷是否一致
	# ========================
	print(">>>農曆:::",tuple_month_num,tuple_day_num )
	lunar_match = (month_num == tuple_month_num) and (day_num == tuple_day_num)
	zhi_match = (zhi_ocr == day_zhi_only)
	
	print(f"農曆匹配: {lunar_match}, 地支匹配: {zhi_match}")
	
	return lunar_match and zhi_match
# def getDarkDateOcr(ocr_txt, date_tuple):
# 	"""
# 	OCR 文本 + tuple 比對，農曆月日 & 日柱地支是否一致
# 	date_tuple = ('2025/11/08/10:30', '九月十九', ['乙巳','丁亥','辛巳','癸巳'], ['立冬','>','小雪'], '(六)', '10:30')
# 	"""

# 	# ========================
# 	# 0️⃣ OCR 文本清理
# 	# ========================
# 	text = ocr_txt.replace("ㄗ", "1").replace("○","0")
# 	text = re.sub(r"\s+", "", text)  # 移除空格換行

# 	# ========================
# 	# 1️⃣ 從 OCR 文本抓農曆月日
# 	# ========================
# 	m_md = re.search(r"([正一二三四五六七八九十]+)月([初一二三四五六七八九十廿三]+)", text)
# 	month_ocr = m_md.group(1) if m_md else None
# 	day_ocr = m_md.group(2) if m_md else None

# 	# ========================
# 	# 2️⃣ 從 OCR 文本抓地支
# 	# ========================
# 	m_zhi = re.search(r"(子|丑|寅|卯|辰|巳|午|未|申|酉|戌|亥)", text)
# 	zhi_ocr = m_zhi.group(1) if m_zhi else None

# 	# ========================
# 	# 3️⃣ 從 tuple 拿資料
# 	# ========================
# 	lunar_md = date_tuple[1]          # tuple 的農曆月日 e.g., '九月十九'
# 	day_zhi = date_tuple[2][3]       # tuple 的日柱 e.g., '癸巳'

# 	# 抓 tuple 日柱地支
# 	m_day_zhi = re.search(r"(子|丑|寅|卯|辰|巳|午|未|申|酉|戌|亥)$", day_zhi)
# 	day_zhi_only = m_day_zhi.group(1) if m_day_zhi else None

# 	# ========================
# 	# 4️⃣ 農曆月日比對
# 	# ========================
# 	# tuple 月日拆開
# 	m_match = re.match(r"(.+)月(.+)", lunar_md)
# 	tuple_month, tuple_day = m_match.groups() if m_match else (None, None)

# 	# OCR 農曆月日轉數字
# 	month_num = None
# 	for k,v in monthBuf.items():
# 		if v == month_ocr:
# 			month_num = k
# 			break
# 	day_num = None
# 	for k,v in datBuf.items():
# 		if v == day_ocr:
# 			day_num = k
# 			break

# 	# tuple 月日轉數字
# 	tuple_month_num = None
# 	for k,v in monthBuf.items():
# 		if v == tuple_month:
# 			tuple_month_num = k
# 			break
# 	tuple_day_num = None
# 	for k,v in datBuf.items():
# 		if v == tuple_day:
# 			tuple_day_num = k
# 			break

# 	# ========================
# 	# 5️⃣ 判斷是否一致
# 	# ========================
# 	lunar_match = (month_num == tuple_month_num) and (day_num == tuple_day_num)
# 	zhi_match = (zhi_ocr == day_zhi_only)

# 	return lunar_match and zhi_match
# # fourPillarToDateMain( inputDate = '乙巳/卯/戊戌'  )




def extract_datetime(text: str):
	"""
	解析模糊日期時間 → YYYY/MM/DD/HH/MM
	支援:
	2025-11一0518.58
	2025一10一0100:15
	2025一10800:40
	2025-09-29 01:48
	2025/9/29 0148
	2025一1ㄗ0810:30  <- ㄗ自動轉1
	"""
	# 先把 ㄗ 轉成 1
	text = text.replace("ㄗ", "1")
	m = re.search(
		r"(\d{4})\D*(\d{1,2})\D*(\d{1,2})\D*(\d{2})\D*(\d{2})",
		text
	)
	if m:
		year, month, day, hour, minute = m.groups()
		rtmDate =  f"{year}/{month.zfill(2)}/{day.zfill(2)}/{hour.zfill(2)}/{minute.zfill(2)}"

		print(getFourPillar( fullDate = rtmDate , detail = True ))
		date_tuple = getFourPillar( fullDate = rtmDate , detail = True )

		if getDarkDateOcr( text , date_tuple ):
			return rtmDate
		elif ( res := lunar_to_solar(text)):
			print ( "重新取得陰曆轉公曆",res)
			return res
		else:
			return rtmDate + "#"
	return None







def extract_hexagrams(text: str):
	"""
	提取本卦與變卦，最小變動實現規則：
	- 本卦名稱與變卦名稱：
		1. 先判斷最後一個字是否存在於字典 key 中，有的話直接取字典對應值
		2. 三個字取最後一個字，四個字取最後兩個字
	- 返回格式: "本卦之變卦卦"
	- 若未找到「本卦」「變卦」關鍵字，則從文本中依序找64卦名稱
	"""
	# 移除干擾字符
	cleaned = text.replace("\n", " ").replace("【", "").replace("】", "")
	guaName_dict = { "天":"乾","澤":"兌","火":"離","雷":"震","風":"巽","水":"坎","山":"艮","地":"坤" }
	
	def process_gua(name):
		if not name:
			return None
		# 先判斷最後一個字是否存在字典 key
		last_char = name[-1]
		if last_char in guaName_dict:
			return guaName_dict[last_char]
		# 沒匹配再依字數取字
		if len(name) == 3:
			return name[-1]
		elif len(name) == 4:
			return name[-2:]
		else:
			return name
	
	# 找本卦
	ben_gua = None
	if "本卦" in cleaned:
		after_bengua = cleaned.split("本卦", 1)[1].strip()
		ben_gua_full = refindGuaName(after_bengua.split()[0])
		ben_gua = process_gua(ben_gua_full)
	
	# 找變卦
	bian_gua = None
	if "變卦" in cleaned:
		after_biangua = cleaned.split("變卦", 1)[1].strip()
		bian_gua_full = refindGuaName(after_biangua.split()[0])
		bian_gua = process_gua(bian_gua_full)
	
	# 🔥 新邏輯：如果本卦或變卦缺失，從全文按順序找64卦
	if not ben_gua or not bian_gua:
		found_guas = []
		
		# 遍歷整個文本，按出現順序找卦名
		for i, char in enumerate(text):
			# 檢查從當前位置開始是否匹配任何卦名
			for gua in guaList:
				if text[i:i+len(gua)] == gua:
					# 避免重複添加
					if gua not in found_guas:
						found_guas.append(gua)
					# 找到兩個就停止
					if len(found_guas) == 2:
						break
			if len(found_guas) == 2:
				break
		
		# 第一個是本卦，第二個是變卦
		if len(found_guas) >= 1 and not ben_gua:
			ben_gua = process_gua(found_guas[0])
		if len(found_guas) >= 2 and not bian_gua:
			bian_gua = process_gua(found_guas[1])
	
	print(ben_gua, bian_gua)
	
	if ben_gua and bian_gua:
		return f"{ben_gua}之{bian_gua}卦"
	return None


# def extract_hexagrams(text: str):
# 	"""
# 	提取本卦與變卦，最小變動實現規則：
# 	- 本卦名稱與變卦名稱：
# 		1. 先判斷最後一個字是否存在於字典 key 中，有的話直接取字典對應值
# 		2. 三個字取最後一個字，四個字取最後兩個字
# 	- 返回格式: "本卦之變卦卦"
# 	- 若未找到「本卦」「變卦」關鍵字，則從文本中依序找64卦名稱
# 	"""
# 	# 移除干擾字符
# 	cleaned = text.replace("\n", " ").replace("【", "").replace("】", "")
# 	guaName_dict = { "天":"乾","澤":"兌","火":"離","雷":"震","風":"巽","水":"坎","山":"艮","地":"坤" }
	
# 	def process_gua(name):
# 		if not name:
# 			return None
# 		# 先判斷最後一個字是否存在字典 key
# 		last_char = name[-1]
# 		if last_char in guaName_dict:
# 			return guaName_dict[last_char]
# 		# 沒匹配再依字數取字
# 		if len(name) == 3:
# 			return name[-1]
# 		elif len(name) == 4:
# 			return name[-2:]
# 		else:
# 			return name
	
# 	# 找本卦
# 	ben_gua = None
# 	if "本卦" in cleaned:
# 		after_bengua = cleaned.split("本卦", 1)[1].strip()
# 		ben_gua_full = refindGuaName(after_bengua.split()[0])
# 		ben_gua = process_gua(ben_gua_full)
	
# 	# 找變卦
# 	bian_gua = None
# 	if "變卦" in cleaned:
# 		after_biangua = cleaned.split("變卦", 1)[1].strip()
# 		bian_gua_full = refindGuaName(after_biangua.split()[0])
# 		bian_gua = process_gua(bian_gua_full)
	
# 	# 如果沒有找到本卦或變卦，則從文本中依序查找64卦
# 	if not ben_gua or not bian_gua:
# 		found_guas = []
# 		for gua in guaList:
# 			if gua in text:
# 				found_guas.append(gua)
# 				if len(found_guas) == 2:
# 					break
		
# 		# 第一個是本卦，第二個是變卦
# 		if len(found_guas) >= 1 and not ben_gua:
# 			ben_gua = process_gua(found_guas[0])
# 		if len(found_guas) >= 2 and not bian_gua:
# 			bian_gua = process_gua(found_guas[1])
# 	print( ben_gua , bian_gua)


# 	if ben_gua and bian_gua:
# 		return f"{ben_gua}之{bian_gua}卦"
# 	return None


# def extract_hexagrams(text: str):
#     """
#     提取本卦與變卦，最小變動實現規則：
#     - 本卦名稱與變卦名稱：
#         1. 先判斷最後一個字是否存在於字典 key 中，有的話直接取字典對應值
#         2. 三個字取最後一個字，四個字取最後兩個字
#     - 返回格式: "本卦之變卦卦"
#     """
#     # 移除干擾字符
#     cleaned = text.replace("\n", " ").replace("【", "").replace("】", "")
#     guaName_dict = { "天":"乾","澤":"兌","火":"離","雷":"震","風":"巽","水":"坎","山":"艮","地":"坤" }

#     def process_gua(name):
#         if not name:
#             return None
#         # 先判斷最後一個字是否存在字典 key
#         last_char = name[-1]
#         if last_char in guaName_dict:
#             return guaName_dict[last_char]
#         # 沒匹配再依字數取字
#         if len(name) == 3:
#             return name[-1]
#         elif len(name) == 4:
#             return name[-2:]
#         else:
#             return name

#     # 找本卦
#     ben_gua = None
#     if "本卦" in cleaned:
#         after_bengua = cleaned.split("本卦", 1)[1].strip()
#         ben_gua_full = refindGuaName(after_bengua.split()[0])
#         ben_gua = process_gua(ben_gua_full)

#     # 找變卦
#     bian_gua = None
#     if "變卦" in cleaned:
#         after_biangua = cleaned.split("變卦", 1)[1].strip()
#         bian_gua_full = refindGuaName(after_biangua.split()[0])
#         bian_gua = process_gua(bian_gua_full)

#     if ben_gua and bian_gua:
#         return f"{ben_gua}之{bian_gua}卦"

#     return None






# import difflib

# 模糊比對卦名
# 保留字的順序 → “天山X” 只能匹配“天山遯”，不能匹配“山天遯”。
# 三字卦 → 允許一個字錯
# 四字卦 → 允許一到兩個字錯
# OCR 錯字校正 → 返回最接近的正確卦名
guaList = [
	"乾為天","天風姤","天山遯","天地否","風地觀","山地剝","火地晉","火天大有",
	"坎為水","水澤節","水雷屯","水火既濟","澤火革","雷火豐","地火明夷","地水師",
	"艮為山","山火賁","山天大畜","山澤損","火澤睽","天澤履","風澤中孚","風山漸",
	"震為雷","雷地豫","雷水解","雷風恆","地風升","水風井","澤風大過","澤雷隨",
	"巽為風","風天小畜","風火家人","風雷益","天雷無妄","火雷噬嗑","山雷頤","山風蠱",
	"離為火","火山旅","火風鼎","火水未濟","山水蒙","風水渙","天水訟","天火同人",
	"坤為地","地雷復","地澤臨","地天泰","雷天大壯","澤天夬","水天需","水地比",
	"兌為澤","澤水困","澤地萃","澤山咸","水山蹇","地山謙","雷山小過","雷澤歸妹"
]
def refindGuaName(inputName):
	best_match = None
	min_distance = None

	# 🔹 Case1: 完全匹配，直接返回
	for gua in guaList:
		if gua == inputName:
			return gua

	# 🔹 Case2: 前兩字或後兩字能對上，直接挑候選
	for gua in guaList:
		if inputName in gua:
			return gua
		if len(inputName) >= 2 and gua.startswith(inputName[:2]):
			if len(inputName) < len(gua):
				return gua

	# 🔹 Case3: 原本距離比對（錯一字/兩字）
	for gua in guaList:
		if len(gua) != len(inputName):
			continue
		distance = sum(1 for a, b in zip(gua, inputName) if a != b)
		if len(gua) == 3 and distance <= 1:
			if min_distance is None or distance < min_distance:
				best_match = gua
				min_distance = distance
		elif len(gua) == 4 and distance <= 2:
			if min_distance is None or distance < min_distance:
				best_match = gua
				min_distance = distance

	return best_match




# # 範例
# print(refindGuaName("天火同人"))  # -> 天山遯
# print(refindGuaName("允為天"))  # -> 乾為天





# def cropTool(img: Image.Image, 
# 			 w_ratio=0.5, h_ratio=0.25, 
# 			 quadrant=1, mode="datetime"):
# 	"""
# 	裁切圖片指定區域，並回傳 OCR 結果
# 	img: PIL Image
# 	w_ratio, h_ratio: 裁切區域相對於整張圖的寬高比例
# 	quadrant: 1=右上, 2=左上, 3=左下, 4=右下
# 	mode: "datetime" / "hexagrams" / "raw"
# 	"""
# 	w, h = img.size
# 	# print( img.size )
# 	crop_w, crop_h = int(w * w_ratio), int(h * h_ratio)

# 	if quadrant == 1:      # 右上
# 		left, top = w - crop_w, 0
# 	elif quadrant == 2:    # 左上
# 		left, top = 0, 0
# 	elif quadrant == 3:    # 左下
# 		left, top = 0, h - crop_h
# 	elif quadrant == 4:    # 右下
# 		left, top = w - crop_w, h - crop_h
# 	else:
# 		raise ValueError("quadrant must be 1,2,3,4")

# 	right, bottom = left + crop_w, top + crop_h
# 	crop_img = img.crop((left, top, right, bottom))
# 	# crop_img = crop_img.rotate(90, expand=True)
# 	# crop_img.show()
# 	# OCR
# 	text = space_ocr_image_to_text(crop_img)
# 	# text = ocr_ninjas_api(crop_img)	
# 	print( ">>>> ",text )

# 	if mode == "datetime":
# 		return extract_datetime(text)
# 	elif mode == "hexagrams":
# 		return extract_hexagrams(text)
# 	else:
# 		return text  # debug: 回傳原始 OCR 文字
# from PIL import Image



# ## 賽跑模式

# import threading
# import queue
# import time
# import io
# from PIL import Image

# def racing_ocr_test(sub_crop):
#     # 確保輸入是 PIL 物件 (相容路徑測試)
#     if isinstance(sub_crop, str):
#         sub_crop = Image.open(sub_crop)

#     results = queue.Queue()
#     start_time = time.time()

#     # --- 定義 Space 任務 ---
#     def run_space():
#         t0 = time.time()
#         try:
#             # 呼叫你的 Space 函數
#             res = space_ocr_image_to_text(sub_crop)
#             elapsed = time.time() - t0
#             if res:
#                 print(f"【Space】完成! 耗時: {elapsed:.2f}秒, 內容: {res[:20]}...")
#                 results.put(("Space", res, elapsed))
#             else:
#                 print(f"【Space】錯誤: 回傳為空, 耗時: {elapsed:.2f}秒")
#         except Exception as e:
#             elapsed = time.time() - t0
#             print(f"【Space】拋出異常: {e}, 耗時: {elapsed:.2f}秒")

#     # --- 定義 Veryfi 任務 ---
#     def run_veryfi():
#         t0 = time.time()
#         try:
#             # 呼叫你的 Veryfi 函數
#             res = veryfi_ocr_image_to_text(sub_crop)
#             elapsed = time.time() - t0
#             if res:
#                 print(f"【Veryfi】完成! 耗時: {elapsed:.2f}秒, 內容: {res[:20]}...")
#                 results.put(("Veryfi", res, elapsed))
#             else:
#                 print(f"【Veryfi】錯誤: 回傳為空, 耗時: {elapsed:.2f}秒")
#         except Exception as e:
#             elapsed = time.time() - t0
#             print(f"【Veryfi】拋出異常: {e}, 耗時: {elapsed:.2f}秒")

#     # 啟動雙線程
#     t1 = threading.Thread(target=run_space)
#     t2 = threading.Thread(target=run_veryfi)
#     t1.start()
#     t2.start()

#     # 這裡我們等待「第一個」成功的結果
#     try:
#         # 設定總超時時間為 10 秒
#         winner_name, winner_text, winner_time = results.get(timeout=10)
#         total_wait = time.time() - start_time
#         print(f"\n🏆 最終贏家: {winner_name} (體感總等候: {total_wait:.2f}秒)")
#         return winner_text
#     except queue.Empty:
#         print("\n❌ 兩者皆在限時內失敗或超時")
#         return None

# --- 使用方式 ---
# result = racing_ocr_test(sub_crop)


def get_final_ocr_result(sub_crop):
    """
    判斷裁判：先跑 OCR.space (1)，不行再跑 Veryfi (2)
    """
    print("--- 開始執行 OCR 流程 ---")
    
    # 1. 優先嘗試 OCR.space (設定較短的 3 秒超時，不行就趕快換人)
    text = space_ocr_image_to_text(sub_crop, timeout_sec=3)
    
    # 2. 判斷是否有回傳結果 (排除 None 或空字串)
    if text and text.strip():
        print(">>> [成功] 由 OCR.space 回傳結果")
        return text
    
    # 3. 如果 (1) 失敗或沒字，執行 Veryfi (2)
    print(">>> [切換] OCR.space 無結果，啟動 Veryfi...")
    text = veryfi_ocr_image_to_text(sub_crop)
    
    if text and text.strip():
        print(">>> [成功] 由 Veryfi 回傳結果")
        return text
    
    print(">>> [失敗] 兩家 OCR 皆未辨識出文字")
    return None



















from PIL import Image, ImageEnhance
def cropTool(img: Image.Image, 
			 w_ratio=0.5, h_ratio=0.25, 
			 quadrant=1, mode="datetime", h_split=1):
	"""
	裁切圖片指定區域，並回傳 OCR 結果
	img: PIL Image
	w_ratio, h_ratio: 裁切區域相對於整張圖的寬高比例
	quadrant: 1=右上, 2=左上, 3=左下, 4=右下
	mode: "datetime" / "hexagrams" / "raw"
	h_split: 將裁切區沿高度分成幾份，預設 1 = 不分
	"""
	w, h = img.size
	crop_w, crop_h = int(w * w_ratio), int(h * h_ratio)

	if quadrant == 1:      # 右上
		left, top = w - crop_w, 0
	elif quadrant == 2:    # 左上
		left, top = 0, 0
	elif quadrant == 3:    # 左下
		left, top = 0, h - crop_h
	elif quadrant == 4:    # 右下
		left, top = w - crop_w, h - crop_h
	else:
		raise ValueError("quadrant must be 1,2,3,4")

	right, bottom = left + crop_w, top + crop_h
	full_crop = img.crop((left, top, right, bottom))

	# # 1. 轉灰階 (1-channel)
	# full_crop = full_crop.convert('L')

	# # 2. 縮小 (記得強制轉 int)
	# orig_w, orig_h = full_crop.size
	# # 使用 // 運算子直接取得整數
	# full_crop = full_crop.resize((int(orig_w * 0.4), int(orig_h * 0.4)), Image.Resampling.LANCZOS)
	full_crop.show()
	# --- 分段 OCR ---
	if h_split > 1:
		split_h = crop_h // h_split
		combined_text = ""
		found_result = None

		for i in range(h_split):
			split_top = i * split_h
			split_bottom = split_top + split_h if i < h_split - 1 else crop_h
			sub_crop = full_crop.crop((0, split_top, crop_w, split_bottom))

			# text = space_ocr_image_to_text(sub_crop)
			# text = veryfi_ocr_image_to_text(sub_crop)	
			text = get_final_ocr_result(sub_crop)
			print(text)		
			combined_text += " " + text

			if mode == "hexagrams":
				parsed = extract_hexagrams(text)
				if parsed:  # ✅ 找到卦名就中斷
					print(f">>>> [{i+1}/{h_split}] 提前成功辨識：{parsed}")
					found_result = parsed
					break

		# 如果中途找到結果，直接回傳
		if found_result:
			return found_result

		# 沒有提前找到，就回傳全部合併結果
		text = combined_text.strip()
		print(">>>> 最終合併:", text)

	else:
		text = get_final_ocr_result(full_crop)
		# text = space_ocr_image_to_text(full_crop)
		# text = veryfi_ocr_image_to_text(full_crop)		
		print(">>>> ", text)

	# --- 模式回傳 ---
	if mode == "datetime":
		return extract_datetime(text)
	elif mode == "hexagrams":
		return extract_hexagrams(text)
	else:
		return text  # debug: 回傳原始 OCR 文字







from PIL import Image
import io
import time

def getPicData(image_input , showPic = False ):


	start = time.time()





	"""
	支援四種輸入:
	1. Local 路徑（字串）
	2. PIL.Image 物件
	3. BytesIO 或類檔案物件
	4. bytes (原始二進位資料)
	"""
	# PIL.Image 物件直接用
	if isinstance(image_input, Image.Image):
		print(">>PIL Image")
		img = image_input
	
	# bytes 型別 (LINE Bot 的 content.content)
	elif isinstance(image_input, bytes):
		print(">>bytes")
		img = Image.open(io.BytesIO(image_input))
	
	# BytesIO 或類檔案物件
	elif hasattr(image_input, "read"):
		print(">>BytesIO/file-like")
		img = Image.open(image_input)  # BytesIO 不用再包一層!
	
	# 字串當檔案路徑
	elif isinstance(image_input, str):
		print(">>local path")
		img = Image.open(image_input)
	
	else:
		raise TypeError("image_input 必須是 PIL.Image, str 路徑, bytes 或 BytesIO 類型")
	
	# ===== 裁切 OCR =====
	# dt = cropTool(img, w_ratio=0.5, h_ratio=0.25, quadrant=2, mode="datetime")     ## 日期
	# hx = cropTool(img, w_ratio=0.6, h_ratio=0.25, quadrant=3, mode="hexagrams")   ## 卦名
	dt = cropTool(img, w_ratio=0.45, h_ratio=0.25, quadrant=2, mode="datetime", h_split=1)

	hx = cropTool(img, w_ratio=0.4, h_ratio=0.25, quadrant=3, mode="hexagrams", h_split=1)
	if not hx:
		print ( "try again")
		hx = cropTool(img, w_ratio=0.5, h_ratio=0.25, quadrant=3, mode="hexagrams", h_split=3)	
	# hx = cropTool(img, w_ratio=0.5, h_ratio=0.25, quadrant=3, mode="hexagrams", h_split=3)
	# hx = cropTool(img, w_ratio=0.6, h_ratio=0.25, h_split = 3 , quadrant=3, mode="hexagrams")   ## 卦名

	print("Datetime:", dt)
	print("Hexagrams:", hx)
	end = time.time()

	print(f"執行時間: {end - start:.3f} 秒")
	if dt and hx:

		## 產生命令的本番
		# ============================================
		print(f"{dt}//{hx}//Untitled")
		return f"{dt}//{hx}//Untitled"      
		# return dt, hx
		# ============================================
	elif dt:
		return f"{dt}//   //"  		
	else:
		return False

# # ===== 範例 =====
if __name__ == '__main__':
	# local 路徑
	getPicData("D:\\Dropbox\\Python\\linebot\\六爻\\work\\ocr_test_source\\xxxxxxx.jpg")
	# print(veryfi_ocr_image_to_text("D:\\Dropbox\\Python\\linebot\\六爻\\work\\ocr_test_source\\xox.jpg"))
	# # PIL.Image
	# img_obj = Image.open("D:\\Dropbox\\Python\\linebot\\六爻\\work\\ocr_test_source\\S__117137475.jpg")
	# getPicData(img_obj)

	# # BytesIO (例如 LineBot content.raw)
	# # 假設 content 是 line_bot_api.get_message_content(message_id)
	# # getPicData(io.BytesIO(content.raw.read()))




	# text = '卦象\r\n易爻\r\n卦\r\n2025一12322:05\r\n二○二五年十月廿四亥時\r\n大雪(7日5時4分)\r\n'
	# print(lunar_to_solar(text))








# 2025一10一0220:41
# 2025一10一0100:15


# @handler.add(MessageEvent, message=ImageMessage)
# def handle_image_message(event):
#     user_id = event.source.user_id  ##利用reply取得id存至user_id中
#     # 取得 LINE 傳來的圖片 stream
#     message_id = event.message.id
#     jsonData = jsonDataClass( linebotId = user_id ) ## class建立


#     content = line_bot_api.get_message_content(message_id)
#     ui_command = getPicData (content.raw)
#     flexMsgJson = sixYaoMain( ui_command ) # 取得起盤介面的json

#     jsonData.uiJsonSetting( f"set temp {message_id},{ui_command}" )



#     # Flex message的容器，把寫好的json放入就可以變成介面，之前的寫法太土，這次改好看一點
#     line_bot_api.reply_message(
#         event.reply_token,
#         FlexSendMessage(
#             alt_text='< 裝卦UI >',
#             contents= flexMsgJson   # 直接放轉好的 dict
#         )
#     )




# changeNote = "aaa"
# jsonData = jsonDataClass( linebotId = user_id ) ## class建立
# msg_id_command = jsonData.temp ## 取得temp的暫存message_id和ui command

# msgId     = msg_id_command.split(",")[0]
# uiCommand = msg_id_command.split(",")[1]
# newCommand = uiCommand.replace( "no title" , changeNote)


# flexMsgJson = sixYaoMain( ui_command ) # 取得起盤介面的json


# jsonData.uiJsonSetting("set temp none") ## 取完之後刪除

# # Step1: 刪掉舊的
# line_bot_api.delete_message(msg_id)  

# # Step2: 發送新 UI
# line_bot_api.push_message(
#     user_id,
#     FlexSendMessage(
#         alt_text="更新後的卦象UI",
#         contents=new_flex_json
#     )
# )



# lineBotId = "two"
# lineBotName = "啦啦啦"
# userImage = "www.xyz.com/aa/5465465.png"




# guaList = ["乾為天","天風姤","天山遯","天地否","風地觀","山地剝","火地晉","火天大有","坎為水","水澤節","水雷屯","水火既濟","澤火革","雷火豐","地火明夷","地水師","艮為山","山火賁","山天大畜","山澤損","火澤睽","天澤履","風澤中孚","風山漸","震為雷","雷地豫","雷水解","雷風恆","地風升","水風井","澤風大過","澤雷隨","巽為風","風天小畜","風火家人","風雷益","天雷無妄","火雷噬嗑","山雷頤","山風蠱","離為火","火山旅","火風鼎","火水未濟","山水蒙","風水渙","天水訟","天火同人","坤為地","地雷復","地澤臨","地天泰","雷天大壯","澤天夬","水天需","水地比","兌為澤","澤水困","澤地萃","澤山咸","水山蹇","地山謙","雷山小過","雷澤歸妹" ]
# guaList = ["乾為天","天風姤","天山遯","天地否","風地觀","山地剝","火地晉"..........]
# def refindGuaName( inputName = "天山頓" ):
#     ...............
#     return "天山遯"


