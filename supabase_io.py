import os
import requests
from dotenv import load_dotenv

load_dotenv()  # 載入 .env 檔案

# === 設定 ===
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Supabase REST API headers
headers = {
	"apikey": SUPABASE_KEY,
	"Authorization": f"Bearer {SUPABASE_KEY}",
	"Content-Type": "application/json"
}

# =====================================================
# 核心功能（不加密版本）
# =====================================================

def save_user_data(user_id, notion_token, page_id):
	"""儲存用戶的 Notion token 和 page_id（不加密）"""
	url = f"{SUPABASE_URL}/rest/v1/user_tokens"

	data = {
		"user_id": user_id,
		"notion_token": notion_token,  # 直接存
		"page_id": page_id
	}

	response = requests.post(
		url,
		json=data,
		headers={**headers, "Prefer": "resolution=merge-duplicates"}
	)

	if response.status_code in (200, 201):
		print(f"✅ 已儲存 {user_id} 的資料")
		return True

	print(f"❌ 錯誤: {response.text}")
	return False


def get_user_data(user_id):
	"""取得用戶的 Notion token 和 page_id（不解密）"""
	url = f"{SUPABASE_URL}/rest/v1/user_tokens"
	params = {
		"user_id": f"eq.{user_id}",
		"select": "notion_token,page_id"
	}

	response = requests.get(url, params=params, headers=headers)

	if response.status_code == 200 and response.json():
		data = response.json()[0]
		return {
			"notion_token": data["notion_token"],
			"page_id": data["page_id"]
		}

	return None


def delete_user_token(user_id):
	"""刪除用戶資料"""
	url = f"{SUPABASE_URL}/rest/v1/user_tokens"
	params = {"user_id": f"eq.{user_id}"}

	response = requests.delete(url, params=params, headers=headers)

	if response.status_code == 204:
		print(f"🗑️ 已刪除 {user_id} 的 token")
		return True

	return False


def check_user_exists(user_id):
	"""確認 user_id 是否存在"""
	url = f"{SUPABASE_URL}/rest/v1/user_tokens"

	headers_count = {
		"apikey": SUPABASE_KEY,
		"Authorization": f"Bearer {SUPABASE_KEY}",
		"Prefer": "count=exact"
	}

	params = {
		"select": "user_id",
		"user_id": f"eq.{user_id}"
	}

	response = requests.get(url, params=params, headers=headers_count)

	if response.status_code == 200:
		content_range = response.headers.get("content-range", "")
		if "/" in content_range:
			return int(content_range.split("/")[-1]) > 0

	return False


def supabase_health_check():
	"""保持 Supabase 活躍（輕量）"""
	try:
		url = f"{SUPABASE_URL}/rest/v1/user_tokens?limit=1"
		response = requests.get(url, headers=headers, timeout=5)

		if response.status_code == 200:
			return "ok", 200
		return "error", response.status_code

	except Exception:
		return "error", 500


# =====================================================
# 本地測試
# =====================================================
if __name__ == "__main__":
	print(supabase_health_check())
