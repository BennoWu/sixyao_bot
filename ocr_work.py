# -*- coding: utf-8 -*-

from PIL import Image
import re


## 原本的OCR，可用但太吃系統

# import numpy as np
# from paddleocr import PaddleOCR

# # 初始化 OCR（中文+英文）
# ocr = PaddleOCR(use_angle_cls=True, lang="ch")

# def ocr_image_to_text(img):
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



import requests
# from PIL import Image
from io import BytesIO


# OCR SPACE
################################################################################
def ocr_image_to_text(input_data):
	"""
	自動判斷輸入類型並進行 OCR
	input_data: 可以是檔案路徑(str) 或 PIL Image 物件
	"""
	url = 'https://api.ocr.space/parse/image'
	data_payload = {
		'apikey': 'K82723710988957',
		'language': 'cht',
		'detectOrientation': False,  # 強制橫排
	}
	# 判斷輸入類型
	if isinstance(input_data, str):
		# 是字串 → 當作檔案路徑處理
		with open(input_data, 'rb') as f:
			response = requests.post(
				url,
				files={'file': f},
				data=data_payload
			)
	
	elif isinstance(input_data, Image.Image):
		# 是 PIL Image 物件
		img_byte_arr = BytesIO()
		input_data.save(img_byte_arr, format='PNG')
		img_byte_arr.seek(0)
		
		response = requests.post(
			url,
			files={'file': ('image.png', img_byte_arr, 'image/png')},
			data=data_payload
		)
	
	else:
		raise TypeError("input_data 必須是檔案路徑(str)或 PIL Image 物件")
	
	# 解析結果
	result = response.json()
	if result['IsErroredOnProcessing']:
		return None
	print(result['ParsedResults'][0] )
	return result['ParsedResults'][0]['ParsedText']


# # API_NINJAS
# ################################################################################

# import requests
# from io import BytesIO

# def ocr_ninjas_api(input_img):
#     url = "https://api.api-ninjas.com/v1/imagetotext"
#     api_key = "K/5emWH/7hJ5sXD5/ujH+w==Ci9HgvDablZxLZhQ"  # 換成你的 API Key

#     # 確保是 RGB
#     if input_img.mode != "RGB":
#         input_img = input_img.convert("RGB")

#     # 存成 JPEG 並壓縮，避免超過 200 KB
#     buffer = BytesIO()
#     input_img.save(buffer, format="JPEG", quality=80)
#     image_data = buffer.getvalue()

#     headers = {
#         "X-Api-Key": api_key,
#         "Content-Type": "application/octet-stream"
#     }

#     response = requests.post(url, headers=headers, data=image_data)

#     if response.status_code == 200:
#         result = response.json()
#         text = result.get("text", "")
#         print("辨識結果:", text)
#     else:
#         print("錯誤:", response.status_code, response.text)
#         text = ""

#     return text










def extract_datetime(text: str):
	"""
	支援格式如：
	2025-09-29 01:48 或 2025-9-29 01:48
	返回 YYYY/MM/DD/HH/MM 字串
	2025一10一0100:15
	2025一10800:40
	"""
	text = text.replace(" ", "")
	# 改為允許日期後面直接接時間(沒有分隔符)
	m = re.search(r"(\d{4})\D*(\d{1,2})\D*(\d{1,2})(\d{2}):?(\d{2})", text)
	if m:
		year = m[1]
		month = m[2].zfill(2)
		day = m[3].zfill(2)
		hour = m[4].zfill(2)
		minute = m[5].zfill(2)
		return f"{year}/{month}/{day}/{hour}/{minute}"
	return None




def extract_hexagrams(text: str):
	"""
	提取本卦與變卦。
	- 用空格作為分隔
	- 忽略 OCR 可能的換行、方括號
	- 返回格式: "本卦,變卦"
	"""
	# 移除干擾字符
	cleaned = text.replace("\n", " ").replace("【", "").replace("】", "")
	guaName_dict = { "天":"乾","澤":"兌","火":"離","雷":"震","風":"巽","水":"坎","山":"艮","地":"坤", }
	
	# 找本卦
	if "本卦" in cleaned:
		after_bengua = cleaned.split("本卦", 1)[1].strip()
		print( after_bengua )
		ben_gua = refindGuaName(after_bengua.split()[0])   # 取空格前第一段文字
	else:
		ben_gua = None

	# 找變卦
	if "變卦" in cleaned:
		after_biangua = cleaned.split("變卦", 1)[1].strip()
		print( after_biangua )       
		bian_gua = refindGuaName(after_biangua.split()[0] )
	else:
		bian_gua = None




	# print(ben_gua,bian_gua)
	if ben_gua and bian_gua:

		homeGua , changeGua = ben_gua[2:] , bian_gua[2:]
		if homeGua in guaName_dict:
			homeGua = guaName_dict[homeGua]

		if changeGua in guaName_dict:
			changeGua = guaName_dict[changeGua]    
		
		return f"{homeGua}之{changeGua}卦"  

	return None




import difflib

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

	# 🔹 Case1: 如果前兩字或後兩字能對上，就先直接挑候選
	for gua in guaList:
		# 允許 inputName 在 gua 裡面任何位置匹配
		if gua.find(inputName) != -1:
			return gua

		# 原先前兩字匹配邏輯
		if len(inputName) >= 2 and gua.startswith(inputName[:2]):
			if len(inputName) < len(gua):
				return gua

		# 距離比對
		if len(gua) == len(inputName):
			distance = sum(1 for a, b in zip(gua, inputName) if a != b)
			if len(gua) == 3 and distance <= 1:
				return gua
			elif len(gua) == 4 and distance <= 2:
				return gua

	# 🔹 Case2: 原本的距離比對（錯一字/兩字）
	for gua in guaList:
		if len(gua) != len(inputName):
			continue  # 只比對同長度
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
# print(refindGuaName("天山頓"))  # -> 天山遯
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
# 	text = ocr_image_to_text(crop_img)
# 	# text = ocr_ninjas_api(crop_img)	
# 	print( ">>>> ",text )

# 	if mode == "datetime":
# 		return extract_datetime(text)
# 	elif mode == "hexagrams":
# 		return extract_hexagrams(text)
# 	else:
# 		return text  # debug: 回傳原始 OCR 文字
from PIL import Image
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

	# --- 分段 OCR ---
	if h_split > 1:
		split_h = crop_h // h_split
		combined_text = ""
		found_result = None

		for i in range(h_split):
			split_top = i * split_h
			split_bottom = split_top + split_h if i < h_split - 1 else crop_h
			sub_crop = full_crop.crop((0, split_top, crop_w, split_bottom))

			text = ocr_image_to_text(sub_crop)
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
		text = ocr_image_to_text(full_crop)
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

def getPicData(image_input):
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
	dt = cropTool(img, w_ratio=0.5, h_ratio=0.25, quadrant=2, mode="datetime", h_split=1)

	hx = cropTool(img, w_ratio=0.5, h_ratio=0.25, quadrant=3, mode="hexagrams", h_split=1)
	if not hx:
		print ( "try again")
		hx = cropTool(img, w_ratio=0.5, h_ratio=0.25, quadrant=3, mode="hexagrams", h_split=3)		
	# hx = cropTool(img, w_ratio=0.5, h_ratio=0.25, quadrant=3, mode="hexagrams", h_split=3)
	# hx = cropTool(img, w_ratio=0.6, h_ratio=0.25, h_split = 3 , quadrant=3, mode="hexagrams")   ## 卦名

	print("Datetime:", dt)
	print("Hexagrams:", hx)
	
	if dt and hx:

		## 產生命令的本番
		# ============================================
		print(f"{dt}//{hx}//untitled")
		return f"{dt}//{hx}//untitled"      
		# return dt, hx
		# ============================================


# ===== 範例 =====
if __name__ == '__main__':
	# local 路徑
	getPicData("D:\\Dropbox\\Python\\linebot\\六爻\\work\\ocr_test_source\\ooo.jpg")

	# # PIL.Image
	# img_obj = Image.open("D:\\Dropbox\\Python\\linebot\\六爻\\work\\ocr_test_source\\S__117137475.jpg")
	# getPicData(img_obj)

	# # BytesIO (例如 LineBot content.raw)
	# # 假設 content 是 line_bot_api.get_message_content(message_id)
	# # getPicData(io.BytesIO(content.raw.read()))


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
