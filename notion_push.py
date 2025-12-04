from notion_client import Client
from notion_client.errors import APIResponseError
import requests, os

def pushToNotion( imageUrl , titleText , apiToken , pageId ):
    """
    在指定頁面下建立子頁面，並置換左欄圖片為同一路徑（刷新用）
    """
    try:
        notion = Client(auth=apiToken)

        # 檢查圖片是否可存取
        try:
            r = requests.head(imageUrl, allow_redirects=True, timeout=5)
            if r.status_code != 200:
                return f"圖床上傳失敗，HTTP 狀態碼: {r.status_code}"
        except Exception as e:
            return f"圖片檢查失敗: {str(e)}"

        # 建立子頁面
        try:
            new_page = notion.pages.create(
                parent={"type": "page_id", "page_id": pageId},
                properties={"title": [{"type": "text", "text": {"content": titleText}}]},
                children=[
                    {
                      "object": "block",
                      "type": "heading_3",
                      "heading_3": {
                        "rich_text": [
                          {
                            "type": "text",
                            "text": { "content": "subtitle.." }
                          }
                        ]
                      }
                    },

                    {
                        "object": "block",
                        "type": "column_list",
                        "column_list": {
                            "children": [
                                # 左欄：圖片
                                {
                                    "object": "block",
                                    "type": "column",
                                    "column": {
                                        "children": [
                                            {
                                                "object": "block",
                                                "type": "image",
                                                "image": {"type": "external", "external": {"url": imageUrl}}
                                            }
                                        ]
                                    }
                                },
                                # 右欄：四個標題
                                {
                                    "object": "block",
                                    "type": "column",
                                    "column": {
                                        "children": [
                                            {"object": "block", "type": "heading_3", "heading_3": {"rich_text":[{"type":"text","text":{"content":"說明:"}}]}},
                                            {"object": "block", "type": "paragraph", "paragraph": {"rich_text":[]}},
                                            {"object": "block", "type": "divider", "divider":{}},
                                            {"object": "block", "type": "heading_3", "heading_3": {"rich_text":[{"type":"text","text":{"content":"解卦:"}}]}},
                                            {"object": "block", "type": "paragraph", "paragraph": {"rich_text":[]}},
                                            {"object": "block", "type": "divider", "divider":{}},
                                            {"object": "block", "type": "heading_3", "heading_3": {"rich_text":[{"type":"text","text":{"content":"反饋:"}}]}},
                                            {"object": "block", "type": "paragraph", "paragraph": {"rich_text":[]}},
                                            {"object": "block", "type": "divider", "divider":{}},
                                            {"object": "block", "type": "heading_3", "heading_3": {"rich_text":[{"type":"text","text":{"content":"筆記:"}}]}},
                                            {"object": "block", "type": "paragraph", "paragraph": {"rich_text":[]}},
                                            {"object": "block", "type": "divider", "divider":{}}
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            )
        except APIResponseError as e:
            # 處理 Notion API 錯誤
            if e.code == "unauthorized":
                return "Notion 上傳失敗: API Token 不正確或已過期"
            elif e.code == "object_not_found":
                return "Notion 上傳失敗: Page ID 不存在或無權限存取"
            elif e.code == "validation_error":
                return f"Notion 上傳失敗: 資料格式錯誤 - {str(e)}"
            elif e.code == "rate_limited":
                return "Notion 上傳失敗: 請求過於頻繁，請稍後再試"
            else:
                return f"Notion 上傳失敗: {e.code} - {str(e)}"

        # ------------------- 置換左欄圖片 -------------------
        column_list_id = None
        results = notion.blocks.children.list(new_page["id"])["results"]
        for block in results:
            if block["type"] == "column_list":
                column_list_id = block["id"]
                break

        if column_list_id:
            # 取得 column_list 下的 column
            columns = notion.blocks.children.list(column_list_id)["results"]
            if columns and columns[0]["type"] == "column":
                left_column_id = columns[0]["id"]
                # 取得左欄裡的子圖塊
                left_children = notion.blocks.children.list(left_column_id)["results"]
                for c in left_children:
                    if c["type"] == "image":
                        image_block_id = c["id"]
                        # 用相同路徑刷新圖片
                        try:
                            notion.blocks.update(
                                block_id=image_block_id,
                                image={"external": {"url": imageUrl}}
                            )
                        except APIResponseError as e:
                            # 圖片更新失敗不影響整體結果，只記錄警告
                            print(f"警告: 圖片刷新失敗 - {str(e)}")
                        break

        return new_page["url"]

    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"未預期的錯誤: {str(e)}"

if __name__ == '__main__':
    
    from dotenv import load_dotenv
    load_dotenv()  # 載入 .env 檔案


    notion_token = os.environ.get('NOTION_TOKEN')
    page_id      = os.environ.get('NOTION_PAGE_ID')

    img_url = "https://res.cloudinary.com/ds9jcwwcw/image/upload/v1761221999/line_temp/5d146b4556304ebe9d174a2866c0583b.jpg"
    titleName = "占天氣氣氣"
    url = pushToNotion( imageUrl = img_url , titleText = titleName , apiToken = notion_token , pageId = page_id )
    # pushToNotion( imageUrl, titleText , apiToken , pageId  )
    print( ">>>" , url )

