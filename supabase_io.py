import os
# from tqdm import tqdm  # pip install tqdm (進度條)
import requests
from cryptography.fernet import Fernet
from dotenv import load_dotenv
load_dotenv()  # 載入 .env 檔案
# === 設定 ===
# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")
# ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY")

# print(SUPABASE_URL)
# print(SUPABASE_KEY)
# print(ENCRYPTION_KEY)


# 初始化加密器
cipher = Fernet(ENCRYPTION_KEY.encode())

# Supabase REST API 的 headers
headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}





# https://supabase.com/dashboard/project/ppbvnymqxcbbmqwzwgrs/sql/
# https://supabase.com/dashboard/project/ppbvnymqxcbbmqwzwgrs/editor/17482?schema=public


# save_user_data() - 存資料
# get_user_data() - 讀資料
# update_page_id() - 只更新 page_id
# delete_user_token() - 刪除資料
# list_all_users() - 列出所有用戶







# === 主要功能 (用 REST API) ===

def save_user_data(user_id, notion_token, page_id):
    """儲存用戶的 Notion token 和 page_id"""
    # 加密 token (page_id 不加密,因為不是敏感資訊)
    encrypted_token = cipher.encrypt(notion_token.encode()).decode()
    
    # POST 到 Supabase
    url = f"{SUPABASE_URL}/rest/v1/user_tokens"
    data = {
        "user_id": user_id,
        "notion_token": encrypted_token,
        "page_id": page_id
    }
    
    # upsert (有就更新,沒有就新增)
    response = requests.post(
        url, 
        json=data, 
        headers={**headers, "Prefer": "resolution=merge-duplicates"}
    )
    
    if response.status_code in [200, 201]:
        print(f"✅ 已儲存 {user_id} 的資料")
        return True
    else:
        print(f"❌ 錯誤: {response.text}")
        return False


def get_user_data(user_id):
    """取得用戶的 Notion token 和 page_id"""
    # GET 從 Supabase
    url = f"{SUPABASE_URL}/rest/v1/user_tokens"
    params = {"user_id": f"eq.{user_id}", "select": "notion_token,page_id"}
    
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        
        # 解密 token
        notion_token = cipher.decrypt(data["notion_token"].encode()).decode()
        page_id = data["page_id"]
        
        return {
            "notion_token": notion_token,
            "page_id": page_id
        }
    
    return None


def update_page_id(user_id, page_id):
    """只更新 page_id (不動 token)"""
    url = f"{SUPABASE_URL}/rest/v1/user_tokens"
    params = {"user_id": f"eq.{user_id}"}
    data = {"page_id": page_id}
    
    response = requests.patch(url, params=params, json=data, headers=headers)
    
    if response.status_code == 204:
        print(f"✅ 已更新 {user_id} 的 page_id")
        return True
    return False


def delete_user_token(user_id):
    """刪除用戶的 token"""
    url = f"{SUPABASE_URL}/rest/v1/user_tokens"
    params = {"user_id": f"eq.{user_id}"}
    
    response = requests.delete(url, params=params, headers=headers)
    
    if response.status_code == 204:
        print(f"🗑️ 已刪除 {user_id} 的 token")
        return True
    return False


def list_all_users():
    """列出所有有 token 的用戶"""
    url = f"{SUPABASE_URL}/rest/v1/user_tokens"
    params = {"select": "user_id,created_at"}
    
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    return []


# === 測試 ===
if __name__ == "__main__":
    # 測試儲存 (同時存 token 和 page_id)
    save_user_data(
        user_id="line_user_456",
        notion_token="secret_notion_xyz",
        page_id="abc123-def456-ghi789"
    )
    
    # 測試讀取 (會回傳字典)
    data = get_user_data("line_user_456")
    if data:
        print(f"Token: {data['notion_token']}")
        print(f"Page ID: {data['page_id']}")
    
    # 測試只更新 page_id
    update_page_id("line_user_456", "new-page-id-xyz")
    
    # 列出所有用戶
    users = list_all_users()
    print(f"所有用戶: {users}")
    
    # 測試刪除
    # delete_user_token("line_user_456")