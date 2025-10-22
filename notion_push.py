from notion_client import Client
# from notion_client.helpers import APIResponseError
import requests,os

def pushToNotion( imageUrl, titleText , apiToken , pageId  ):
    """
    建立新頁面：左欄放圖片，右欄放四個標題
    回傳：新頁面網址 or 錯誤訊息
    """
    try:
        notion = Client(auth=apiToken)

        # (3) 檢查圖片網址是否能存取
        try:
            r = requests.head(imageUrl, allow_redirects=True, timeout=5)
            if r.status_code != 200:
                return f"圖片網址不正確，HTTP 狀態碼: {r.status_code}"
        except Exception as e:
            return f"圖片檢查失敗: {str(e)}"



        # (4) 建立新頁面
        new_page = notion.pages.create(
            parent={"page_id": pageId},
            properties={
                "title": [
                    {
                        "type": "text",
                        "text": {"content": titleText}
                    }
                ]
            }, 


            children=[
                            {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {"type": "text", "text": {"content": "subtitle.."}}
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
                                            "image": {
                                                "type": "external",
                                                "external": {"url": imageUrl}
                                            }
                                        }
                                    ]
                                }
                            },
                            # 右欄：四個標題 + 空段落 + 分隔線
                            {
                                "object": "block",
                                "type": "column",
                                "column": {
                                    "children": [
                                        {
                                            "object": "block",
                                            "type": "heading_3",
                                            "heading_3": {
                                                "rich_text": [
                                                    {"type": "text", "text": {"content": "說明:"}}
                                                ]
                                            }
                                        },
                                        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": []}},
                                        {"object": "block", "type": "divider", "divider": {}},

                                        {
                                            "object": "block",
                                            "type": "heading_3",
                                            "heading_3": {
                                                "rich_text": [
                                                    {"type": "text", "text": {"content": "解卦:"}}
                                                ]
                                            }
                                        },
                                        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": []}},
                                        {"object": "block", "type": "divider", "divider": {}},

                                        {
                                            "object": "block",
                                            "type": "heading_3",
                                            "heading_3": {
                                                "rich_text": [
                                                    {"type": "text", "text": {"content": "反饋:"}}
                                                ]
                                            }
                                        },
                                        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": []}},
                                        {"object": "block", "type": "divider", "divider": {}},

                                        {
                                            "object": "block",
                                            "type": "heading_3",
                                            "heading_3": {
                                                "rich_text": [
                                                    {"type": "text", "text": {"content": "筆記:"}}
                                                ]
                                            }
                                        },
                                        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": []}},
                                        {"object": "block", "type": "divider", "divider": {}}
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
        )

        return new_page["url"]

    except Exception as e:
        return f"Error: {str(e)}"



if __name__ == '__main__':

    from dotenv import load_dotenv
    load_dotenv()  # 載入 .env 檔案


    notion_token = os.environ.get('NOTION_TOKEN')
    page_id      = os.environ.get('NOTION_PAGE_ID')


    img_url = "https://res.cloudinary.com/ds9jcwwcw/image/upload/v1760970853/line_temp/yvnimzx4hwedj2vsmhqx.jpg"
    titleName = "占占"
    url = pushToNotion( imageUrl = img_url , titleText = titleName , apiToken = notion_token , pageId = page_id )
    # pushToNotion( imageUrl, titleText , apiToken , pageId  )
    print( url )








# 呼叫上傳notion的程式
# sixYaoMain( data )

# imageUrl
# pushToNotion( imageUrl, titleText , apiToken , pageId  )
