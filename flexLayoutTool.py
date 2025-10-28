



## ====== 起頭 ======
up_LayoutFelx = """
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "_type",
            "weight": "bold",
            "color": "#1DB446",
            "size": "lg",
            "margin": "none"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "巳火",
                "weight": "bold",
                "size": "3xl",
                "wrap": true,
                "margin": "none",
                "offsetTop": "none",
                "offsetBottom": "none",
                "action": {
                  "type": "message",
                  "label": "action",
                  "text": "hello"
                },
                "offsetStart": "0px"
              },
              {
                "type": "text",
                "text": "陰火",
                "weight": "bold",
                "color": "#FF7777",
                "size": "lg",
                "margin": "none",
                "wrap": true,
                "gravity": "bottom",
                "offsetBottom": "5px",
                "offsetEnd": "6px",
                "align": "end",
                "flex": 1
              }
            ]
          },
          {
            "type": "text",
            "text": "__SUB__",
            "weight": "bold",
            "size": "md",
            "margin": "xs",
            "wrap": true,
            "offsetTop": "none",
            "offsetBottom": "none",
            "action": {
              "type": "message",
              "label": "action",
              "text": "hello"
            },
            "color": "#888888"
          }
        ]
      },
      """



## ====== 內容(可螱塊) ======
item_LayoutFelx = """

      {
        "type": "separator",
        "margin": "md",
        "color": "#848484"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "____title",
            "size": "lg",
            "color": "#555555",
            "wrap": true,
            "weight": "bold",
            "margin": "lg"
          },
          {
            "type": "text",
            "text": "____text",
            "size": "md",
            "color": "#000000",
            "wrap": true,
            "margin": "xs"
          }
        ]
      },
      """



## ====== 結尾 ======
down_LayoutFelx = """
      {
        "type": "separator",
        "margin": "md",
        "color": "#ffffff"
      }
    ]
  },
  "styles": {
    "footer": {
      "separator": true
    }
  }
}"""



