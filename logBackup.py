import pygsheets
import csv
import os


def logDataFun( userID , userName, logTime = "", inputData = "", command = "" , file_path="__log__.csv"):
	# 檢查檔案是否存在，以及是否需要加標題列
	file_exists = os.path.isfile(file_path)
	write_header = not file_exists or os.path.getsize(file_path) == 0

	# 取得下一筆流水號
	def get_next_record_number():
		if not file_exists:
			return 1
		with open(file_path, "r", encoding="utf-8") as f:
			lines = f.readlines()
			if len(lines) <= 1:
				return 1
			last_line = lines[-1]
			try:
				return int(last_line.split(",")[0]) + 1
			except:
				return 1

	record_num = get_next_record_number()

	# 準備要寫入的資料

	row_data = {
		"record_num": record_num,
		"id": userID,
		"name": userName,
		"time": logTime,
		"user_input": inputData,
		"command":command
	}

	# 寫入檔案
	with open(file_path, "a", newline='', encoding="utf-8") as f:
		writer = csv.DictWriter(f, fieldnames=["record_num", "id", "name", "time", "user_input","command"])
		if write_header:
			writer.writeheader()
		writer.writerow(row_data)

	print(f"✅ 已寫入第 {record_num} 筆資料：{row_data}")
	# uploadCsvToGoogleSheet(csv_path="__log__.csv")




import csv
import pygsheets


def resource_path(relative_path):
	import os,sys
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")

	return os.path.join( base_path, relative_path )



# googleJson = resource_path(r"googleSheetKey/sixyao-data-8f0c712298cd.json")




def uploadCsvToGoogleSheet(csv_path="__log__.csv"):
	import os
	import csv
	import pygsheets
	
	# 從環境變數讀取金鑰
	credentials_json = os.environ.get('GOOGLE_CREDENTIALS')
	
	if credentials_json:
		# Render 上使用環境變數
		gc = pygsheets.authorize(service_account_env_var='GOOGLE_CREDENTIALS')
	else:
		# 本地開發用檔案
		gc = pygsheets.authorize(service_file='googleSheetKey/sixyao-data-8f0c712298cd.json')
	
	# 開啟 Google Sheet
	globalSheet = gc.open_by_url(
		'https://docs.google.com/spreadsheets/d/1Zlj55gQ5N75lWJYAyZ5Es6WTM_LS6SeFumZWlpLo6-0/edit?usp=sharing'
	)
	
	# 開啟 log 工作表
	sheetName = "log"
	wks = globalSheet.worksheet_by_title(sheetName)
	
	# 取得目前已有的資料列數
	existing_rows = len(wks.get_all_records())  # 不包含表頭
	start_row = existing_rows + 2  # 表頭佔一行
	
	# 讀取 CSV 所有資料（略過表頭）
	with open(csv_path, newline='', encoding="utf-8") as f:
		reader = csv.reader(f)
		rows = list(reader)
	print(rows)
	if len(rows) <= 1:
		print("⚠️ 沒有要上傳的資料。")
		return "⚠️ 沒有要上傳的資料。"
	
	data_to_upload = rows[1:]  # 排除第一列表頭
	
	# 清洗資料：確保所有內容都以文字格式上傳
	cleaned_data = []
	for row in data_to_upload:
		cleaned_row = []
		for cell in row:
			# 處理 None 或空值
			if cell is None or cell == 'None' or cell == 'null' or cell == '':
				cleaned_row.append('')
			else:
				# 將所有內容轉換為字串，確保以文字格式儲存
				cell_str = str(cell)
				# 如果是純數字或以 + 開頭，加上單引號前綴強制為文字
				if cell_str.isdigit() or cell_str.startswith("+"):
					cleaned_row.append("'" + cell_str)
				else:
					cleaned_row.append(cell_str)
		cleaned_data.append(cleaned_row)
	
	total = len(cleaned_data)
	
	# 寫入到 Google Sheet（parse=False 確保不自動解析格式）
	wks.update_values(f'A{start_row}', cleaned_data, parse=False)
	print(f"✅ 已成功上傳 {total} 筆 log 到 Google Sheet（從第 {start_row} 行開始）。")
	
	# 清空原始 CSV 檔案，只保留表頭
	with open(csv_path, "w", newline='', encoding="utf-8") as f:
		writer = csv.writer(f)
		writer.writerow(rows[0])  # 寫回原本表頭
	
	print("🧹 已清空本地 __log__.csv，只保留表頭。")
	
	return f"🆗 上傳 {total} 筆 log 到 Google Sheet(從第 {start_row} 行開始)"


# def uploadCsvToGoogleSheet(csv_path="__log__.csv"):
#     import os
#     import csv
#     import pygsheets
	
#     # 從環境變數讀取金鑰
#     credentials_json = os.environ.get('GOOGLE_CREDENTIALS')
	
#     if credentials_json:
#         # Render 上使用環境變數
#         gc = pygsheets.authorize(service_account_env_var='GOOGLE_CREDENTIALS')
#     else:
#         # 本地開發用檔案
#         gc = pygsheets.authorize(service_file='googleSheetKey/sixyao-data-8f0c712298cd.json')
	
#     # 開啟 Google Sheet
#     globalSheet = gc.open_by_url(
#         'https://docs.google.com/spreadsheets/d/1Zlj55gQ5N75lWJYAyZ5Es6WTM_LS6SeFumZWlpLo6-0/edit?usp=sharing'
#     )
	
#     # 開啟 log 工作表
#     sheetName = "log"
#     wks = globalSheet.worksheet_by_title(sheetName)
	
#     # 取得目前已有的資料列數
#     existing_rows = len(wks.get_all_records())  # 不包含表頭
#     start_row = existing_rows + 2  # 表頭佔一行
	
#     # 讀取 CSV 所有資料（略過表頭）
#     with open(csv_path, newline='', encoding="utf-8") as f:
#         reader = csv.reader(f)
#         rows = list(reader)
#     print(rows)
#     if len(rows) <= 1:
#         print("⚠️ 沒有要上傳的資料。")
#         return "⚠️ 沒有要上傳的資料。"
	
#     data_to_upload = rows[1:]  # 排除第一列表頭
	
#     # 清洗資料：避免 + 開頭被當成公式，以及處理 None/null
#     cleaned_data = []
#     for row in data_to_upload:
#         cleaned_row = []
#         for cell in row:
#             # 🔥 處理 None 或空值
#             if cell is None or cell == 'None' or cell == 'null' or cell == '':
#                 cleaned_row.append('')
#             # 處理 + 開頭的字串
#             elif isinstance(cell, str) and cell.startswith("+"):
#                 cleaned_row.append("'" + cell)
#             else:
#                 cleaned_row.append(cell)
#         cleaned_data.append(cleaned_row)
	
#     total = len(cleaned_data)
	
#     # 寫入到 Google Sheet（從下一行開始）
#     wks.update_values(f'A{start_row}', cleaned_data)
#     print(f"✅ 已成功上傳 {total} 筆 log 到 Google Sheet（從第 {start_row} 行開始）。")
	
#     # 清空原始 CSV 檔案，只保留表頭
#     with open(csv_path, "w", newline='', encoding="utf-8") as f:
#         writer = csv.writer(f)
#         writer.writerow(rows[0])  # 寫回原本表頭
	
#     print("🧹 已清空本地 __log__.csv，只保留表頭。")
	
#     return f"🆗 上傳 {total} 筆 log 到 Google Sheet(從第 {start_row} 行開始)"

	
if __name__ == '__main__':
	# logDataFun("userID", "userName", "logTime", "inputData" )
	# for i,a in enumerate(range(500)):
	# 	logDataFun( f"id{i:03}", "userName", "2025/6/15/12/11", "inputDatainputDatainputDatainputData" )

	uploadCsvToGoogleSheet("__log__.csv")











