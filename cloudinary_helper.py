

# import requests

# api_key = 'ad00a6dab7b170765abacf52c3bbe6f2'
# image_path = r"D:\Dropbox\Python\linebot\六爻\sixYao_bot\papper_bg_01.jpg"

# with open(image_path, 'rb') as f:
#     image_data = f.read()

# res = requests.post("https://api.imgbb.com/1/upload", {
#     'key': api_key,
# }, files={
#     'image': image_data,
# })

# print(res.json()['data']['url'])  # 拿到圖片網址



from dotenv import load_dotenv
load_dotenv()  # 載入 .env 檔案




import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from datetime import datetime, timedelta, timezone

# # ✅ 請改成你的 Cloudinary 認證資訊
# cloudinary.config(
#     cloud_name = "ds9jcwwcw",   #'你的 cloud_name',
#     api_key=   "323614222724576", #'你的 api_key',
#     api_secret=  "caLU6rJpGJD7-00KhkyqjroBwxk" , #'你的 api_secret',
#     secure=True
# )

# print("cloud_name =", os.environ.get('CLOUDINARY_CLOUD_NAME'))
# print("api_key =", os.environ.get('CLOUDINARY_API_KEY'))
# print("api_secret =", os.environ.get('CLOUDINARY_API_SECRET'))



from PIL import Image
import io
# import cloudinary.uploader

cloudinary.config(
	cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
	api_key=os.environ.get('CLOUDINARY_API_KEY'),
	api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
	secure=True
)


import uuid


# def upload_image(image_input, folder="line_temp"):
#     """
#     上傳圖片到 Cloudinary，回傳直連 URL 與 public_id。
#     - 每次生成新的 public_id，避免覆蓋舊圖
#     - folder: Cloudinary 資料夾
#     - 支援檔案路徑或 PIL.Image 物件
#     """
#     # 生成唯一 public_id
#     unique_id = uuid.uuid4().hex
#     public_id = f"{folder}/{unique_id}"

#     # 處理上傳來源
#     if isinstance(image_input, Image.Image):
#         byte_io = io.BytesIO()
#         image_input.save(byte_io, format='JPEG')
#         byte_io.seek(0)
#         upload_source = byte_io
#     else:
#         upload_source = image_input

#     # 上傳
#     res = cloudinary.uploader.upload(
#         upload_source,
#         public_id=public_id,
#         resource_type='image',  # 確保是圖片
#         type='upload'            # 產生真正直連 URL
#     )

#     return {
#         "url": res["secure_url"],   # Notion 可直接外連
#         "public_id": res["public_id"],
#         "created_at": res["created_at"]
#     }
	
def upload_image(image_input, folder="line_temp"):
	"""
	上傳圖片到 Cloudinary，回傳直連 URL 與 public_id。
	- 每次生成新的 public_id，避免覆蓋舊圖
	- folder: Cloudinary 資料夾
	- 支援檔案路徑或 PIL.Image 物件
	"""
	# 生成唯一 public_id（不包含路徑）
	unique_id = uuid.uuid4().hex
	
	# 處理上傳來源
	if isinstance(image_input, Image.Image):
		byte_io = io.BytesIO()
		image_input.save(byte_io, format='JPEG')
		byte_io.seek(0)
		upload_source = byte_io
	else:
		upload_source = image_input
	
	# 上傳，使用 folder 參數
	res = cloudinary.uploader.upload(
		upload_source,
		folder=folder,           # ⭐ 明確指定資料夾
		public_id=unique_id,     # ⭐ 只放檔名
		resource_type='image',
		type='upload'
	)
	
	return {
		"url": res["secure_url"],
		"public_id": res["public_id"],
		"created_at": res["created_at"]
	}



	

def get_upload_time(public_id):
	"""取得圖片上傳時間（datetime 格式）"""
	res = cloudinary.api.resource(public_id)
	created_at = res["created_at"]
	return datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

def delete_image(public_id):
	"""刪除圖片"""
	res = cloudinary.uploader.destroy(public_id)
	return res["result"] == "ok"

# def delete_older_than(folder="line_temp", days=0):
#     """刪除某資料夾內 超過N天 的所有圖片"""
#     now = datetime.now(timezone.utc)
#     cutoff = now - timedelta(days=days)

#     res = cloudinary.api.resources(type="upload", prefix=folder + "/")
#     print(res)
#     deleted = []

#     for item in res["resources"]:
#         created_at = datetime.strptime(item["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
#         if created_at < cutoff:
#             public_id = item["public_id"]
#             delete_image(public_id)
#             deleted.append(public_id)

#     return deleted

def delete_older_than(folder="line_temp", days=0):
	"""刪除某資料夾內 超過N天 的所有圖片（分頁處理，避免一次刪不完）"""
	now = datetime.now(timezone.utc)
	cutoff = now - timedelta(days=days)

	deleted = []
	next_cursor = None
	total_deleted = 0

	while True:
		res = cloudinary.api.resources(
			type="upload",
			prefix=folder + "/",
			max_results=500,    # 一次最多 500 筆
			next_cursor=next_cursor
		)

		for item in res["resources"]:
			created_at = datetime.strptime(
				item["created_at"], "%Y-%m-%dT%H:%M:%SZ"
			).replace(tzinfo=timezone.utc)

			if created_at < cutoff:
				public_id = item["public_id"]
				delete_image(public_id)
				deleted.append(public_id)
				total_deleted += 1

				# 每刪 100 張印一次進度
				if total_deleted % 100 == 0:
					print(f"已刪除 {total_deleted} 張...")

		if "next_cursor" in res:
			next_cursor = res["next_cursor"]
		else:
			break

	print(f"✅ 完成，共刪除 {total_deleted} 張圖片")
	return deleted






# import cloudinary
# import cloudinary.uploader
# import cloudinary.api

# # 1️⃣ 設定 Cloudinary
# cloudinary.config(
#     cloud_name = "你的cloud_name",
#     api_key = "你的api_key",
#     api_secret = "你的api_secret"
# )















if __name__ == '__main__':
	
# https://console.cloudinary.com/app/c-23207f9a45824cd129542519c8eb28/assets/media_library/folders/cbba2d5838093ff9d98caf59474a6c2f1a?view_mode=mosaic
# https://console.cloudinary.com/app/c-23207f9a45824cd129542519c8eb28/assets/media_library/search?q=&view_mode=mosaic
	# from cloudinary_helper import upload_image, delete_older_than

	# 上傳圖片
	# res = upload_image( r"D:\Dropbox\Python\linebot\六爻\584488494031437884.jpg")
	# print("連結：", res["url"])
	# print("public_id：", res["public_id"])
	# print("上傳時間：", res["created_at"])


	# # # upload_image( r"D:\Dropbox\Python\linebot\六爻\work\834185e004190e75a5bfdb32019e51fb.jpg", folder="__image_hosting")

	# # # # 刪除超過 15 天的圖
	# deleted = delete_older_than( days = 15 )
	# print("已刪除：", deleted)






	filePathList = [r"D:\Dropbox\Python\linebot\六爻\sLiuZen\sLiuZen-icon-38.png",
					r"D:\Dropbox\Python\linebot\六爻\sLiuZen\sLiuZen-icon-39.png",
					r"D:\Dropbox\Python\linebot\六爻\sLiuZen\sLiuZen-icon-40.png",
					r"D:\Dropbox\Python\linebot\六爻\sLiuZen\sLiuZen-icon-41.png",
					r"D:\Dropbox\Python\linebot\六爻\sLiuZen\sLiuZen-icon-42.png",
					r"D:\Dropbox\Python\linebot\六爻\sLiuZen\sLiuZen-icon-43.png",
					]

	#### delete_older_than(folder="__icon", days=0)
	
	nameList = [ "大安","留連","速喜","赤口","小吉","空亡" ]
	print( "url_dict = {")
	for i, each in enumerate(filePathList):
		res = upload_image( each , folder="__icon")
		# print( i , res["url"])
		print (f'"{nameList[i]}" : "{res["url"]}",')
	print( "}")
# delete_image("line_temp/m45zouwd2vvb6fejpb9g")


	filePathList = [r"D:\Dropbox\Python\linebot\六爻\sLiuZen\yo-61.png",  ## $
					r"D:\Dropbox\Python\linebot\六爻\sLiuZen\yo-62.png",  ## X
					r"D:\Dropbox\Python\linebot\六爻\sLiuZen\yo-63.png",  ## 1
					r"D:\Dropbox\Python\linebot\六爻\sLiuZen\yo-64.png",  ## 0
					]

	### delete_older_than(folder="__icon", days=0)
	
	nameList = [ "OO","XX","O","X" ]
	print( "url_dict = {")
	for i, each in enumerate(filePathList):
		res = upload_image( each , folder="__icon")
		# print( i , res["url"])
		print (f'"{nameList[i]}" : "{res["url"]}",')
	print( "}")
# delete_image("line_temp/m45zouwd2vvb6fejpb9g")



	# # 2️⃣ 上傳 JSON
	# res = cloudinary.uploader.upload(
	#     r"D:\Dropbox\Python\linebot\六爻\work\baGuaData\gua64.json",  # Windows
	#     # r"D:\Dropbox\Python\linebot\六爻\work\baGuaData\guaMatchDict.json",  # Windows	    
	#     resource_type="raw",
	#     folder="__icon",
	#     public_id="gua64"
	# )


	# # 3️⃣ 取得可公開 URL
	# print("✅ 上傳完成，檔案 URL：")
	# print(res['secure_url'])

	# res = cloudinary.uploader.upload(
	#     # r"D:\Dropbox\Python\linebot\六爻\work\baGuaData\gua64.json",  # Windows
	#     r"D:\Dropbox\Python\linebot\六爻\work\baGuaData\guaMatchDict.json",  # Windows	    
	#     resource_type="raw",
	#     folder="__icon",
	#     public_id="guaMatchDict"
	# )


	# # 3️⃣ 取得可公開 URL
	# print("✅ 上傳完成，檔案 URL：")
	# print(res['secure_url'])






# https://res.cloudinary.com/ds9jcwwcw/raw/upload/v1766859111/__icon/guaMatchDict.json
# https://res.cloudinary.com/ds9jcwwcw/raw/upload/v1766859141/__icon/gua64.json