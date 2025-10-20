import os
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

print(SUPABASE_URL)
print(SUPABASE_KEY)
print(ENCRYPTION_KEY)

cipher = Fernet(ENCRYPTION_KEY.encode())

# Supabase REST API 的 headers
headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}


# === 三個主要功能 (用 REST API) ===

def save_user_token(user_id, notion_token):
    """儲存用戶的 Notion token"""
    # 加密
    encrypted = cipher.encrypt(notion_token.encode()).decode()
    
    # POST 到 Supabase
    url = f"{SUPABASE_URL}/rest/v1/user_tokens"
    data = {
        "user_id": user_id,
        "notion_token": encrypted
    }
    
    # upsert (有就更新,沒有就新增)
    response = requests.post(
        url, 
        json=data, 
        headers={**headers, "Prefer": "resolution=merge-duplicates"}
    )
    
    if response.status_code in [200, 201]:
        print(f"✅ 已儲存 {user_id} 的 token")
        return True
    else:
        print(f"❌ 錯誤: {response.text}")
        return False


def get_user_token(user_id):
    """取得用戶的 Notion token"""
    # GET 從 Supabase
    url = f"{SUPABASE_URL}/rest/v1/user_tokens"
    params = {"user_id": f"eq.{user_id}", "select": "notion_token"}
    
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200 and response.json():
        encrypted = response.json()[0]["notion_token"]
        # 解密
        token = cipher.decrypt(encrypted.encode()).decode()
        return token
    
    return None


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
    # 測試儲存
    save_user_token("line_user_456", "secret_notion_xyz")
    
    # 測試讀取
    token = get_user_token("line_user_456")
    print(f"讀到的 token: {token}")
    
    # 列出所有用戶
    users = list_all_users()
    print(f"所有用戶: {users}")
    
    # 測試刪除
    # delete_user_token("line_user_456")