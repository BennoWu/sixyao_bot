# -*- coding: utf-8 -*-

from PIL import Image, ImageEnhance, ImageFilter
import re
import requests
from io import BytesIO


# OCR SPACE
################################################################################
def ocr_image_to_text(input_data, preprocess=True):
	"""
	自動判斷輸入類型並進行 OCR
	input_data: 可以是檔案路徑(str) 或 PIL Image 物件
	preprocess: 是否進行圖像預處理
	"""
	url = 'https://api.ocr.space/parse/image'
	data_payload = {
		'apikey': 'K82723710988957',
		'language': 'cht',
		'detectOrientation': False,
	}
	
	# 判斷輸入類型並進行預處理
	if isinstance(input_data, str):
		img = Image.open(input_data)
		if preprocess:
			img = preprocess_image(img)
		
		img_byte_arr = BytesIO()
		img.save(img_byte_arr, format='PNG')
		img_byte_arr.seek(0)
		
		response = requests.post(
			url,
			files={'file': ('image.png', img_byte_arr, 'image/png')},
			data=data_payload
		)
	
	elif isinstance(input_data, Image.Image):
		if preprocess:
			input_data = preprocess_image(input_data)
		
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
	print("OCR 原始結果:", result['ParsedResults'][0]['ParsedText'])
	return result['ParsedResults'][0]['ParsedText']


def preprocess_image(img):
	"""
	圖像預處理：增強對比度、銳化、去噪
	"""
	# 轉換為 RGB
	if img.mode != 'RGB':
		img = img.convert('RGB')
	
	# 增強對比度
	enhancer = ImageEnhance.Contrast(img)
	img = enhancer.enhance(2.0)
	
	# 增強銳利度
	enhancer = ImageEnhance.Sharpness(img)
	img = enhancer.enhance(1.5)
	
	# 輕微去噪
	img = img.filter(ImageFilter.MedianFilter(size=3))
	
	return img


def extract_datetime(text: str):
	"""
	支援格式如：
	2025-09-29 01:48 或 2025-9-29 01:48
	返回 YYYY/MM/DD/HH/MM 字串
	"""
	# 改為允許日期後面直接接時間(沒有分隔符)
	m = re.search(r"(\d{4})\D*(\d{1,2})\D*(\d{1,2})\D*(\d{2}):?(\d{2})", text)
	if m:
		year = m.group(1)
		month = m.group(2).zfill(2)
		day = m.group(3).zfill(2)
		hour = m.group(4).zfill(2)
		minute = m.group(5).zfill(2)
		return f"{year}/{month}/{day}/{hour}/{minute}"
	return None


# 64 卦列表
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


def extract_hexagrams(text: str):
	"""
	提取本卦與變卦 - 改進版
	- 優先完整匹配卦名
	- 使用模糊匹配糾錯
	- 返回格式: "本卦之變卦卦"
	"""
	cleaned = text.replace("\n", " ").replace("【", "").replace("】", "").replace("\r", " ")
	
	# 八純卦轉換字典
	guaName_dict = {
		"天":"乾", "澤":"兌", "火":"離", "雷":"震",
		"風":"巽", "水":"坎", "山":"艮", "地":"坤"
	}
	
	ben_gua = None
	bian_gua = None
	
	# === 提取本卦 ===
	if "本卦" in cleaned:
		after_bengua = cleaned.split("本卦", 1)[1].strip()
		print(f"本卦後文字: {after_bengua}")
		
		# 先嘗試直接完整匹配
		for gua in guaList:
			if gua in after_bengua[:10]:  # 只檢查前10個字
				ben_gua = gua
				print(f"✓ 本卦完整匹配: {ben_gua}")
				break
		
		# 如果沒有完整匹配，使用模糊匹配
		if not ben_gua:
			raw_name = after_bengua.split()[0] if after_bengua.split() else after_bengua[:4]
			ben_gua = refindGuaName(raw_name)
			if ben_gua:
				print(f"✓ 本卦模糊匹配: {raw_name} → {ben_gua}")
	
	# === 提取變卦 ===
	if "變卦" in cleaned:
		after_biangua = cleaned.split("變卦", 1)[1].strip()
		print(f"變卦後文字: {after_biangua}")
		
		# 先嘗試直接完整匹配
		for gua in guaList:
			if gua in after_biangua[:10]:
				bian_gua = gua
				print(f"✓ 變卦完整匹配: {bian_gua}")
				break
		
		# 如果沒有完整匹配，使用模糊匹配
		if not bian_gua:
			raw_name = after_biangua.split()[0] if after_biangua.split() else after_biangua[:4]
			bian_gua = refindGuaName(raw_name)
			if bian_gua:
				print(f"✓ 變卦模糊匹配: {raw_name} → {bian_gua}")
	
	# === 組合結果 ===
	if ben_gua and bian_gua:
		# 提取本卦名（去掉「為」字）
		if "為" in ben_gua:
			homeGua = ben_gua.split("為")[-1]
		else:
			homeGua = ben_gua[2:]
		
		# 提取變卦名（判斷是否為八純卦）
		if "為" in bian_gua:
			# 八純卦：如「離為火」→ 取「火」再轉換成「離」
			changeGua_element = bian_gua.split("為")[-1]  # 取得「火」
			changeGua = guaName_dict.get(changeGua_element, changeGua_element)  # 轉換成「離」
		else:
			# 非八純卦：如「天火同人」→ 取後兩字「同人」
			changeGua = bian_gua[2:]
		
		result = f"{homeGua}之{changeGua}卦"
		print(f">>> 最終結果: {result}")
		return result
	
	print("⚠ 未能提取完整卦名")
	return None


def refindGuaName(inputName):
	"""
	模糊比對卦名 - 改進版
	優先順序：
	1. 完整包含匹配
	2. 前綴匹配
	3. 字數相同且錯字在容許範圍內
	"""
	if not inputName:
		return None
	
	inputName = inputName.strip()
	best_match = None
	min_distance = float('inf')
	
	# === Case 1: 完整包含匹配（優先度最高）===
	for gua in guaList:
		if inputName in gua or gua in inputName:
			return gua
	
	# === Case 2: 前綴匹配 ===
	if len(inputName) >= 2:
		for gua in guaList:
			if gua.startswith(inputName[:2]):
				# 如果輸入較短，直接返回
				if len(inputName) < len(gua):
					return gua
	
	# === Case 3: 同長度字串的容錯匹配 ===
	for gua in guaList:
		if len(gua) != len(inputName):
			continue
		
		distance = sum(1 for a, b in zip(gua, inputName) if a != b)
		
		# 三字卦容許 1 字錯，四字卦容許 2 字錯
		if len(gua) == 3 and distance <= 1:
			if distance < min_distance:
				best_match = gua
				min_distance = distance
		elif len(gua) == 4 and distance <= 2:
			if distance < min_distance:
				best_match = gua
				min_distance = distance
	
	if best_match:
		print(f"  模糊匹配: {inputName} → {best_match} (錯字數: {min_distance})")
	
	return best_match


def cropTool(img: Image.Image, 
			 w_ratio=0.5, h_ratio=0.25, 
			 quadrant=1, mode="datetime", h_split=1):
	"""
	裁切圖片指定區域，並回傳 OCR 結果 - 改進版
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
		combined_text = ""
		found_result = None

		for i in range(h_split):
			split_top = i * (crop_h // h_split)
			split_bottom = split_top + (crop_h // h_split) if i < h_split - 1 else crop_h
			sub_crop = full_crop.crop((0, split_top, crop_w, split_bottom))

			text = ocr_image_to_text(sub_crop, preprocess=True)
			if not text:
				continue
			
			combined_text += " " + text

			if mode == "hexagrams":
				parsed = extract_hexagrams(text)
				if parsed:
					print(f"✓ [{i+1}/{h_split}] 提前成功辨識：{parsed}")
					found_result = parsed
					break

		if found_result:
			return found_result

		text = combined_text.strip()
		print(f">>>> 最終合併文字: {text}")

	else:
		text = ocr_image_to_text(full_crop, preprocess=True)
		if text:
			print(f">>>> OCR 結果: {text}")

	# --- 模式回傳 ---
	if not text:
		return None
	
	if mode == "datetime":
		return extract_datetime(text)
	elif mode == "hexagrams":
		return extract_hexagrams(text)
	else:
		return text


def getPicData(image_input):
	"""
	支援四種輸入並進行 OCR 辨識 - 改進版
	"""
	import io
	
	# 解析輸入類型
	if isinstance(image_input, Image.Image):
		print(">> PIL Image")
		img = image_input
	elif isinstance(image_input, bytes):
		print(">> bytes")
		img = Image.open(io.BytesIO(image_input))
	elif hasattr(image_input, "read"):
		print(">> BytesIO/file-like")
		img = Image.open(image_input)
	elif isinstance(image_input, str):
		print(">> local path")
		img = Image.open(image_input)
	else:
		raise TypeError("image_input 必須是 PIL.Image, str 路徑, bytes 或 BytesIO 類型")
	
	# ===== 裁切 OCR =====
	print("\n=== 開始辨識日期時間 ===")
	dt = cropTool(img, w_ratio=0.5, h_ratio=0.25, quadrant=2, mode="datetime", h_split=1)
	
	print("\n=== 開始辨識卦名 ===")
	# 先嘗試單次辨識
	hx = cropTool(img, w_ratio=0.5, h_ratio=0.25, quadrant=3, mode="hexagrams", h_split=1)
	
	# 如果失敗，嘗試分段辨識
	if not hx:
		print("⚠ 單次辨識失敗，嘗試分段辨識...")
		hx = cropTool(img, w_ratio=0.5, h_ratio=0.3, quadrant=3, mode="hexagrams", h_split=3)
	
	print(f"\n=== 辨識結果 ===")
	print(f"日期時間: {dt}")
	print(f"卦名: {hx}")
	
	if dt and hx:
		result = f"{dt}//{hx}//Untitled"
		print(f"\n>>> 最終命令: {result}")
		return result
	else:
		print("⚠ 辨識失敗")
		return False


# # ===== 測試 =====
# if __name__ == '__main__':
# 	# 測試模糊匹配
# 	print("=== 測試模糊匹配 ===")
# 	print(refindGuaName("天火同人"))  # 應該返回 天火同人
# 	print(refindGuaName("天火"))      # 應該返回 天火同人
# 	print(refindGuaName("天山頓"))    # 應該返回 天山遯
# 	print(refindGuaName("離為火"))    # 應該返回 離為火
	
# 	print("\n=== 測試圖片辨識 ===")
	# getPicData("your_image_path.jpg")
# ===== 範例 =====
if __name__ == '__main__':
	# local 路徑
	getPicData("D:\\Dropbox\\Python\\linebot\\六爻\\work\\ocr_test_source\\占軍官正規班訓練是否合格.jpg")

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
