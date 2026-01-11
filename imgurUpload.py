# -*- coding: utf-8 -*-
"""
Imgur 上傳工具 - 簡單函數版
支援: 檔案路徑、PIL Image、BytesIO、bytes
"""

import requests
import datetime
from io import BytesIO
from pathlib import Path
from PIL import Image


def upload_to_imgur(image_input, title=None, description=None, use_album=True):
    """
    上傳圖片到 Imgur - 支援所有格式
    
    Args:
        image_input: 支援以下格式:
            - str/Path: 檔案路徑
            - PIL.Image: PIL Image 物件
            - BytesIO: 二進位流
            - bytes: 純二進位資料
        title: 圖片標題 (可選)
        description: 圖片描述 (可選,預設為上傳時間)
        use_album: 是否上傳到相簿 (預設 True)
    
    Returns:
        dict: 成功時回傳 {
            'success': True,
            'url': str,  # 圖片連結
            'id': str,   # 圖片 ID
            'delete_hash': str  # 刪除用的 hash
        }
        失敗時回傳 {
            'success': False,
            'error': str
        }
    """
    # Imgur 帳號設定
    ACCESS_TOKEN = '44428b7d1cc740be9b475a0cb866a99e3fe44045'
    ALBUM_ID = 'FhfzevH'
    
    # 1️⃣ 轉換所有格式為 BytesIO
    try:
        # PIL Image 物件
        if isinstance(image_input, Image.Image):
            img_byte_arr = BytesIO()
            
            # 處理 RGBA → RGB (JPEG 不支援透明)
            if image_input.mode == 'RGBA':
                rgb_image = Image.new('RGB', image_input.size, (255, 255, 255))
                rgb_image.paste(image_input, mask=image_input.split()[3])
                rgb_image.save(img_byte_arr, format='JPEG', quality=90, optimize=True)
            else:
                image_input.save(img_byte_arr, format='JPEG', quality=90, optimize=True)
            
            img_byte_arr.seek(0)
        
        # BytesIO 物件
        elif isinstance(image_input, BytesIO):
            image_input.seek(0)
            img_byte_arr = image_input
        
        # bytes 資料
        elif isinstance(image_input, bytes):
            img_byte_arr = BytesIO(image_input)
        
        # 檔案路徑
        elif isinstance(image_input, (str, Path)):
            file_path = Path(image_input)
            
            if not file_path.exists():
                return {
                    'success': False,
                    'error': f'檔案不存在: {image_input}'
                }
            
            with open(file_path, 'rb') as f:
                img_byte_arr = BytesIO(f.read())
        
        else:
            return {
                'success': False,
                'error': f'不支援的格式: {type(image_input)}'
            }
    
    except Exception as e:
        return {
            'success': False,
            'error': f'格式轉換失敗: {str(e)}'
        }
    
    # 2️⃣ 準備上傳參數
    url = "https://api.imgur.com/3/upload"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    files = {
        'image': img_byte_arr
    }
    data = {}
    
    # 設定標題和描述
    if title:
        data['title'] = title
    if description:
        data['description'] = description
    else:
        data['description'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 設定相簿
    if use_album:
        data['album'] = ALBUM_ID
    
    # 3️⃣ 上傳
    try:
        response = requests.post(url, headers=headers, files=files, data=data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()['data']
            print(f"✅ 圖片上傳成功: {result['link']}")
            
            return {
                'success': True,
                'url': result['link'],
                'id': result['id'],
                'delete_hash': result.get('deletehash'),
                'width': result.get('width'),
                'height': result.get('height'),
                'size': result.get('size')
            }
        else:
            error_msg = f"上傳失敗: {response.status_code} - {response.text}"
            print(f"❌ {error_msg}")
            return {
                'success': False,
                'error': error_msg
            }
    
    except Exception as e:
        error_msg = f"上傳發生錯誤: {str(e)}"
        print(f"❌ {error_msg}")
        return {
            'success': False,
            'error': error_msg
        }


# ===== 使用範例 =====

if __name__ == '__main__':
    
    # ✅ 方式 1: 上傳檔案路徑
    result = upload_to_imgur(
        r"D:\Dropbox\Python\linebot\六爻\sixyao_bot_render\paper_1800.jpg",
        title="測試圖片"
    )
    print(result)
    
    # ✅ 方式 2: 上傳 PIL Image
    img = Image.new("RGB", (500, 700), "#FF5733")
    result = upload_to_imgur(img, title="純色圖片")
    if result['success']:
        print(f"URL: {result['url']}")
    
    # ✅ 方式 3: 上傳 BytesIO
    byte_io = BytesIO()
    img.save(byte_io, format='PNG')
    byte_io.seek(0)
    result = upload_to_imgur(byte_io)
    print(result['url'] if result['success'] else result['error'])
    
    # ✅ 方式 4: 上傳 bytes
    with open("test.jpg", "rb") as f:
        image_bytes = f.read()
    result = upload_to_imgur(image_bytes)