import requests
import io
import uuid
from pathlib import Path
from PIL import Image

def upload_imageBB(image_input , expiration = None):

	api_key = "b62a6870d803b93a06bee15741b6ac15"
	"""
	上傳圖片到 ImgBB,回傳圖片資訊。
	
	Args:
		image_input: 支援三種輸入格式
			- str/Path: 圖片檔案路徑
			- PIL.Image: PIL Image 物件
			- bytes/BytesIO: 二進位圖片資料
		api_key: ImgBB API Key
		expiration: 圖片保存時間(秒),None 表示永久保存
	
	Returns:
		dict: {
			"url": 圖片直連網址,
			"delete_url": 刪除連結,
			"display_url": 顯示頁面網址,
			"thumb_url": 縮圖網址,
			"image_id": ImgBB 圖片 ID,
			"created_at": 上傳時間戳
		}
		失敗時回傳 None

	60秒      = 60
	5分鐘     = 300
	30分鐘    = 1800
	1小時     = 3600
	6小時     = 21600
	12小時    = 43200
	1天       = 86400
	7天       = 604800
	30天      = 2592000
	180天(最大) = 15552000	
	"""
	# 生成唯一檔名
	unique_filename = f"{uuid.uuid4().hex}.jpg"
	
	# 處理上傳來源
	upload_source = None
	
	if isinstance(image_input, Image.Image):
		# PIL Image 物件
		byte_io = io.BytesIO()
		image_input.save(byte_io, format='JPEG')
		byte_io.seek(0)
		upload_source = byte_io
		
	elif isinstance(image_input, (str, Path)):
		# 檔案路徑
		if not Path(image_input).exists():
			print(f"錯誤: 檔案不存在 - {image_input}")
			return None
		upload_source = open(image_input, "rb")
		
	elif isinstance(image_input, bytes):
		# bytes 資料
		upload_source = io.BytesIO(image_input)
		
	elif isinstance(image_input, io.BytesIO):
		# BytesIO 物件
		image_input.seek(0)
		upload_source = image_input
		
	else:
		print(f"錯誤: 不支援的圖片格式 - {type(image_input)}")
		return None
	
	# 建構 API URL
	url = f"https://api.imgbb.com/1/upload?key={api_key}"
	
	# 準備參數
	data = {}
	if expiration:
		data['expiration'] = expiration  # 秒數
	
	try:
		# 上傳圖片
		response = requests.post(
			url,
			files={"image": (unique_filename, upload_source, "image/jpeg")},
			data=data,
			timeout=30
		)
		
		# 關閉檔案(如果是從路徑開啟的)
		if isinstance(image_input, (str, Path)):
			upload_source.close()
		
		if response.status_code == 200:
			result = response.json()
			data = result["data"]
			
			return {
				"url": data["url"],
				"delete_url": data["delete_url"],
				"display_url": data["display_url"],
				"thumb_url": data.get("thumb", {}).get("url"),
				"image_id": data["id"],
				"created_at": data.get("time")  # Unix timestamp
			}
		else:
			print(f"上傳失敗 (狀態碼 {response.status_code}): {response.text}")
			return None
			
	except requests.exceptions.Timeout:
		print("錯誤: 請求超時")
		return None
	except Exception as e:
		print(f"發生錯誤: {str(e)}")
		return None
	finally:
		# 確保資源被釋放
		if isinstance(upload_source, io.BytesIO) and upload_source != image_input:
			upload_source.close()


# ===== 使用範例 =====
if __name__ == "__main__":
	API_KEY = "b62a6870d803b93a06bee15741b6ac15"
	
	# # 方式 1: 使用檔案路徑
	# result = upload_imageBB(
	# 	r"D:\Dropbox\Python\linebot\六爻\work\ocr_test_source\xxxxxxx.jpg",
	# 	api_key=API_KEY
	# )
	
	# # 方式 2: 使用 PIL Image
	# from PIL import Image
	# img = Image.open(r"D:\Dropbox\Python\linebot\六爻\work\ocr_test_source\xxxxxxx.jpg")
	# result = upload_imageBB(img, api_key=API_KEY ,expiration=60)
	
	# # 方式 3: 使用 BytesIO
	# with open(r"D:\Dropbox\Python\linebot\六爻\work\ocr_test_source\xxxxxxx.jpg", "rb") as f:
	# 	byte_data = io.BytesIO(f.read())
	# result = upload_imageBB(byte_data, api_key=API_KEY)
	
	# 方式 4: 設定過期時間(60秒後過期)
	result = upload_imageBB(
		r"D:\Dropbox\Python\linebot\六爻\work\ocr_test_source\xxxxxxx.jpg",
		api_key=API_KEY,
		expiration=60
	)
	
	if result:
		print(f"✅ 上傳成功!")
		print(f"📷 圖片網址: {result['url']}")
		print(f"🗑️  刪除連結: {result['delete_url']}")
		print(f"🆔 圖片 ID: {result['image_id']}")
	else:
		print("❌ 上傳失敗")
















