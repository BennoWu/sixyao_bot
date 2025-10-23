# from notion_client import Client

# notion = Client(auth="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")

# # 測試讀取資料庫
# db = notion.pages.retrieve("26a739d0e36080d29148e0f263b77986")
# print(db)


from notion_client import Client
import os
from dotenv import load_dotenv

load_dotenv()



notion_token = os.environ.get('NOTION_TOKEN')
# print( notion_token )
database_id = "26a739d0-e360-80d2-9148-e0f263b77986"

print("=== 測試 1: 使用舊版 API (2022-06-28) ===")
try:
    notion_old = Client(auth=notion_token, notion_version="2022-06-28")
    db_old = notion_old.databases.retrieve(database_id=database_id)
    print(f"✅ 舊版 API 成功!")
    print(f"   資料庫: {db_old.get('title', [{}])[0].get('plain_text', 'N/A')}")
except Exception as e:
    print(f"❌ 舊版 API 失敗: {e}")

print("\n=== 測試 2: 使用新版 API (2025-09-03) ===")
try:
    notion_new = Client(auth=notion_token, notion_version="2025-09-03")
    db_new = notion_new.databases.retrieve(database_id=database_id)
    print(f"✅ 新版 API 成功!")
    print(f"   資料庫: {db_new.get('title', [{}])[0].get('plain_text', 'N/A')}")
    
    # 檢查是否有多個 data sources
    data_sources = db_new.get('data_sources', [])
    print(f"   Data Sources: {len(data_sources)} 個")
    for ds in data_sources:
        print(f"      - {ds['name']} (ID: {ds['id']})")
    
    if len(data_sources) > 1:
        print("\n⚠️  這個資料庫有多個 data sources!")
        print("   這就是為什麼舊程式碼會失敗的原因")
        
except Exception as e:
    print(f"❌ 新版 API 失敗: {e}")

print("\n=== 測試 3: 搜尋所有可存取的資料庫 ===")
try:
    notion = Client(auth=notion_token)
    results = notion.search(filter={"property": "object", "value": "database"})
    print(f"找到 {len(results['results'])} 個資料庫:")
    for db in results['results']:
        title = db.get('title', [{}])[0].get('plain_text', '(無標題)')
        print(f"   - {title} (ID: {db['id']})")
except Exception as e:
    print(f"❌ 搜尋失敗: {e}")



# ## 檢查NOTION帳號資料是否可執行
# from notion_client import Client
# def checkNotionAcc(token, pageId):
#     try:
#         notion = Client(auth=token)
#         notion.pages.retrieve(pageId)
#         return True
#     except Exception as e:
#         print(f"錯誤: {e}")
#         return False

# token_buf = "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"
# pageId_buf ="26a739d0e36080d29148e0f263b77986"
# checkNotionAcc( token_buf , pageId_buf )




# from notion_client import Client

# notion = Client(auth="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")

# page_id = "26a739d0e36080d29148e0f263b77986"
# page = notion.pages.retrieve(page_id)
# print(page)





# from notion_client import Client

# notion = Client(auth="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")

# # 這裡的 page_id 是父層頁面，也就是你要在哪個頁面下面放新頁
# parent_page_id = "26a739d0e36080d29148e0f263b77986"

# new_page = notion.pages.create(
#     parent={"page_id": parent_page_id},
#     properties={
#         "title": [
#             {"text": {"content": "我的新空白頁"}}
#         ]
#     }
# )

# print("新頁面建立成功！ID:", new_page["id"])
# print("網址: https://www.notion.so/" + new_page["id"].replace("-", ""))





# from notion_client import Client

# notion = Client(auth="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")

# # 父層頁面 ID
# parent_page_id = "26a739d0e36080d29148e0f263b77986"

# # 建立帶有空白兩欄的新頁面
# new_page = notion.pages.create(
#     parent={"page_id": parent_page_id},
#     properties={ "title": [{"text": {"content": "NEW1"}}]},


# 	children=[
#         {
#             "object": "block",
#             "type": "column_list",
#             "column_list": {
#                 "children": [
#                     # 左欄 - 空白
#                     {
#                         "object": "block",
#                         "type": "column",
#                         "column": {
#                             "children": [
# 						        {
# 						            "object": "block",
# 						            "type": "image",
# 						            "image": {
# 						                "type": "external",
# 						                "external": {
# 						                    "url": "https://res.cloudinary.com/ds9jcwwcw/image/upload/v1757613934/line_temp/agjvmffk8b5bkejxgnxc.jpg"
# 						                }
# 						            }
# 						        }
#                             ]
#                         }
#                     },
#                     # 右欄 - 四個標題區塊
#                     {
#                         "object": "block",
#                         "type": "column", 
#                         "column": {
#                             "children": [
#                                 # 占問標題
#                                 {
#                                     "object": "block",
#                                     "type": "heading_3",
#                                     "heading_3": {
#                                         "rich_text": [
#                                             {
#                                                 "type": "text",
#                                                 "text": {"content": "占問:"}
#                                             }
#                                         ]
#                                     }
#                                 },
#                                 # 占問內容
#                                 {
#                                     "object": "block",
#                                     "type": "paragraph",
#                                     "paragraph": {
#                                         "rich_text": [
#                                             {
#                                                 "type": "text",
#                                                 "text": {"content": ""}
#                                             }
#                                         ]
#                                     }
#                                 },
#                                 # 橫隔線
#                                 {
#                                     "object": "block",
#                                     "type": "divider",
#                                     "divider": {}
#                                 },
#                                 # 解卦標題
#                                 {
#                                     "object": "block",
#                                     "type": "heading_3",
#                                     "heading_3": {
#                                         "rich_text": [
#                                             {
#                                                 "type": "text",
#                                                 "text": {"content": "解卦:"}
#                                             }
#                                         ]
#                                     }
#                                 },
#                                 # 解卦內容
#                                 {
#                                     "object": "block",
#                                     "type": "paragraph",
#                                     "paragraph": {
#                                         "rich_text": [
#                                             {
#                                                 "type": "text",
#                                                 "text": {"content": ""}
#                                             }
#                                         ]
#                                     }
#                                 },
#                                 # 橫隔線
#                                 {
#                                     "object": "block",
#                                     "type": "divider",
#                                     "divider": {}
#                                 },
#                                 # 反饋標題
#                                 {
#                                     "object": "block",
#                                     "type": "heading_3",
#                                     "heading_3": {
#                                         "rich_text": [
#                                             {
#                                                 "type": "text",
#                                                 "text": {"content": "反饋:"}
#                                             }
#                                         ]
#                                     }
#                                 },
#                                 # 反饋內容
#                                 {
#                                     "object": "block",
#                                     "type": "paragraph",
#                                     "paragraph": {
#                                         "rich_text": [
#                                             {
#                                                 "type": "text",
#                                                 "text": {"content": ""}
#                                             }
#                                         ]
#                                     }
#                                 },
#                                 # 橫隔線
#                                 {
#                                     "object": "block",
#                                     "type": "divider",
#                                     "divider": {}
#                                 },
#                                 # 筆記標題
#                                 {
#                                     "object": "block",
#                                     "type": "heading_3",
#                                     "heading_3": {
#                                         "rich_text": [
#                                             {
#                                                 "type": "text",
#                                                 "text": {"content": "筆記:"}
#                                             }
#                                         ]
#                                     }
#                                 },
#                                 # 筆記內容
#                                 {
#                                     "object": "block",
#                                     "type": "paragraph",
#                                     "paragraph": {
#                                         "rich_text": [
#                                             {
#                                                 "type": "text",
#                                                 "text": {"content": ""}
#                                             }
#                                         ]
#                                     }
#                                 }
#                             ]
#                         }
#                     }        
#                 ]
#             }
#         }
#     ]
# )

# print(f"新頁面建立成功！")
# print(f"頁面 ID: {new_page['id']}")
# print(f"頁面網址: {new_page['url']}")




# from notion_client import Client

# notion = Client(auth="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")
# parent_page_id = "26a739d0e36080d29148e0f263b77986"

# # parent_page_id = "xxxxxxxxxxxxxxxxxxxxxxxx"  # 主頁的 page_id

# # 建立一個新資料庫
# database = notion.databases.create(
#     parent={"type": "page_id", "page_id": parent_page_id},
#     title=[{"type": "text", "text": {"content": "子專案總覽"}}],
#     properties={
#         "Name": {"title": {}},  # 必須要有 title property
#         "Tag": {"multi_select": {"options": []}}
#     }
# )

# database_id = database["id"]

# # 在資料庫下新增幾個頁面
# notion.pages.create(
#     parent={"database_id": database_id},
#     properties={
#         "Name": {"title": [{"text": {"content": "子專案 A"}}]},
#         "Tag": {"multi_select": [{"name": "設計"}]}
#     }
# )

# notion.pages.create(
#     parent={"database_id": database_id},
#     properties={
#         "Name": {"title": [{"text": {"content": "子專案 B"}}]},
#         "Tag": {"multi_select": [{"name": "開發"}]}
#     }
# )
























