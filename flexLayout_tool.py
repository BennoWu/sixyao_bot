
from fourPillar_tool import PPPPP # 四柱得日期
from fourPillar_tool import getFourPillar # 四柱得日期

from guaMatch import checkMainData as checkMainData

from sixYao_data import  * # baGuaAllDict 取得
import json



##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################


uiLayoutFront ='''
{
  "type": "bubble",
  "size": "kilo",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "六爻排盤:",
            "weight": "bold",
            "color": "#6A8B91",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "節氣",
            "weight": "regular",
            "color": "#666666",
            "size": "lg",
            "align": "end",
            "action": {
              "type": "message",
              "label": "action",
              "text": "jechi_mode"
            },
            "gravity": "center"
          }
        ],
        "margin": "none"
      },
      {
        "type": "separator",
        "margin": "none",
        "color": "#cccccc"
      },
      

{
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "年",
            "size": "xxs",
            "gravity": "bottom",
            "flex": 0,
            "color": "#888888",
            "offsetBottom": "3px",
            "weight": "bold",
            "offsetEnd": "1px"
          },
          {
            "type": "text",
            "text": "年柱",
            "weight": "bold",
            "size": "xl",
            "margin": "none",
            "wrap": true,
            "flex": 0,
            "color": "#000001",
            "offsetEnd": "xs"
          },
          {
            "type": "text",
            "text": "|",
            "size": "xl",
            "margin": "none",
            "color": "#dddddd",
            "gravity": "top",
            "offsetTop": "-2px",
            "flex": 0,
            "offsetEnd": "xs"
          },
          {
            "type": "text",
            "text": "月",
            "size": "xxs",
            "gravity": "bottom",
            "flex": 0,
            "color": "#888888",
            "offsetBottom": "3px",
            "offsetEnd": "1px",
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "月柱",
            "weight": "bold",
            "size": "xl",
            "margin": "none",
            "wrap": true,
            "flex": 0,
            "action": {
              "type": "message",
              "label": "action",
              "text": "干支/月/6/2025-10-30"
            },
            "color": "#000002",
            "offsetEnd": "xs"
          },
          {
            "type": "text",
            "text": "|",
            "size": "xl",
            "margin": "none",
            "color": "#cccccc",
            "gravity": "top",
            "offsetTop": "-2px",
            "flex": 0,
            "offsetEnd": "xs"
          },
          {
            "type": "text",
            "text": "日",
            "size": "xxs",
            "gravity": "bottom",
            "flex": 0,
            "color": "#888888",
            "offsetBottom": "3px",
            "offsetEnd": "1px",
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "日柱",
            "weight": "bold",
            "size": "xl",
            "margin": "none",
            "wrap": true,
            "flex": 0,
            "action": {
              "type": "message",
              "label": "action",
              "text": "干支/日/6/2025-10-30"
            },
            "color": "#000002",
            "offsetEnd": "xs"
          },
          {
            "type": "text",
            "text": "|",
            "size": "xl",
            "margin": "none",
            "color": "#dddddd",
            "gravity": "top",
            "offsetTop": "-2px",
            "flex": 0,
            "offsetEnd": "xs"
          },
          {
            "type": "text",
            "text": "時",
            "size": "xxs",
            "gravity": "bottom",
            "flex": 0,
            "color": "#888888",
            "offsetBottom": "3px",
            "offsetEnd": "2px",
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "時柱",
            "weight": "bold",
            "size": "xl",
            "margin": "none",
            "wrap": true,
            "flex": 0,
            "action": {
              "type": "message",
              "label": "action",
              "text": "干支/時/6/2025-10-30-10-21"
            },
            "color": "#000003",
            "offsetEnd": "xs"
          }
        ],
        "spacing": "none",
        "margin": "xs",
        "cornerRadius": "7px",
        "justifyContent": "space-between"
      },



      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "國曆: __sunDate__",
                "size": "sm",
                "color": "#444443",
                "wrap": true,
                "weight": "regular",
                "margin": "none",
                "align": "start",
                "offsetTop": "2px"
              },
              {
                "type": "text",
                "text": "農曆: __darkDate__",
                "size": "sm",
                "color": "#444443",
                "wrap": true,
                "weight": "regular",
                "margin": "none"
              }
            ],
            "margin": "none",
            "flex": 0,
            "height": "40px"
          },


          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "|",
                "size": "3xl",
                "margin": "none",
                "color": "#dddddd",
                "align": "center"
              }
            ],
            "width": "10px",
            "offsetStart": "7px",
            "offsetBottom": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "12:00",
                "size": "3xl",
                "color": "#FCA32D",
                "weight": "regular"
              }
            ],
            "offsetStart": "7px",
            "offsetBottom": "sm"
          }
        ],
        "margin": "none"
      },





      {
        "type": "separator",
        "margin": "none",
        "color": "#aaaaaa"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "weight": "bold",
                    "color": "#ffffff",
                    "size": "xl",
                    "text": "占",
                    "contents": [],
                    "gravity": "center",
                    "align": "center",
                    "offsetTop": "-1px"
                  }
                ],
                "backgroundColor": "#91A4BC",
                "width": "30px",
                "height": "30px",
                "cornerRadius": "20px"
              },
              {
                "type": "text",
                "color": "#333333",
                "size": "lg",
                "wrap": true,
                "text": "__NOTE__",
                "margin": "sm",
                "contents": [],
                "gravity": "center"
              }
            ],
            "margin": "sm"
          }
        ],
        "spacing": "none",
        "margin": "sm"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "width": "251px",
                "margin": "none",
                "spacing": "none",
                "offsetStart": "sm"
              }
            ],
            "height": "5px"
          },'''






## 少陰 少陽
uiLayoutMidA = '''
		  {
			"type": "box",
			"layout": "vertical",
			"contents": [
			  {
				"type": "box",
				"layout": "horizontal",
				"contents": [
				  {
					"type": "box",
					"layout": "vertical",
					"contents": [],
					"width": "42px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "__YO__",
						"size": "xxl",
						"align": "center",
						"offsetBottom": "7px",
						"weight": "regular",
						"gravity": "bottom"
					  }
					],
					"width": "30px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "－",
						"size": "md",
						"offsetTop": "-4px",
						"align": "center",
						"gravity": "center",
						"color": "#999999"
					  }
					],
					"width": "90px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "__INDEX__",
						"size": "lg",
						"weight": "regular",
						"color": "#333333",
						"gravity": "top"
					  }
					],
					"flex": 2
				  }
				],

                "margin": "xs",
                "height": "35px",
                "offsetTop": "5px"


			  }
			]
		  }
		  '''

ui_separator = '''
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [
				  {
					"type": "separator",
					"color": "#cccccc",
					"margin": "xs"
				  }
				],
				"margin": "none",
				"spacing": "none",
				"offsetStart": "sm"
			  }
			  '''


## 老陰 老陽
uiLayoutMidB = '''
		  {
			"type": "box",
			"layout": "vertical",
			"contents": [
			  {
				"type": "box",
				"layout": "horizontal",
				"contents": [
				  {
					"type": "box",
					"layout": "vertical",
					"contents": [],
					"width": "42px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "__YO__",
						"size": "xl",
						"align": "center",
						"weight": "bold",
						"offsetBottom": "7px",
						"gravity": "bottom"

					  }
					],
					"width": "30px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "－",
						"size": "md",
						"offsetTop": "-4px",
						"align": "center",
						"gravity": "center",
						"color": "#999999"
					  }
					],
					"width": "90px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "__INDEX__",
						"size": "lg",
						"weight": "regular",
						"color": "#333333",
						"gravity": "top"
					  }
					],
					"flex": 2
				  }
				],
                "margin": "xs",
                "height": "35px",
                "offsetTop": "5px"
			  }
			]
		  }
		  '''


uiLayoutBack = '''

		  {
			"type": "box",
			"layout": "vertical",
			"contents": [
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [],
				"height": "10px",
				"width": "251px",
				"margin": "none",
				"spacing": "none",
				"offsetStart": "sm"
			  }
			],
			"height": "10px"
		  }
		],

		"margin": "md",
		"cornerRadius": "10px",
		"backgroundColor": "#E5E5E5"
	  },





      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "width": "8px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "__ORGGUA__",
                    "align": "center",
                    "size": "md",

                    "weight": "bold"

                  }
                ]
              },














              {
                "type": "box",
                "layout": "vertical",
                "contents": [




                  {
                    "type": "text",
                    "text": "•",
                    "align": "center",
                    "size": "md",
                    "color": "#bbbbbb"
                  }



                ],
                "width": "20px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "__CHGGUA__",
                    "align": "center",

                    "size": "md",
                    "weight": "bold"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "width": "10px"
              }
            ],
            "offsetTop": "sm"
          }








        ],
        "margin": "md",
        "cornerRadius": "10px",
        "borderColor": "#999999",
        "borderWidth": "1px",
        "height": "30px"
      },





























      {
        "type": "box",
        "layout": "vertical",
        "margin": "xs",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "button",
                "style": "secondary",
                "action": {
                  "type": "postback",
                  "label": "裝卦",
                  "data": "__裝卦__",
                  "displayText": "__dis裝卦__"
                },
                "color": "#91A4BC",
                "margin": "none",
                "height": "md"
              }
            ],
            "margin": "xs"
          }
        ],

        "cornerRadius": "10px",
        "offsetTop": "3px"
      }
    ],
    "backgroundColor": "#fefefe"
  },
  "styles": {
    "footer": {
      "separator": true
    }
  }
}
'''



uiLayoutBackExt = '''

		  {
			"type": "box",
			"layout": "vertical",
			"contents": [
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [],
				"height": "10px",
				"width": "251px",
				"margin": "none",
				"spacing": "none",
				"offsetStart": "sm"
			  }
			],
			"height": "10px"
		  }
		],

		"margin": "md",
		"cornerRadius": "10px",
		"backgroundColor": "#E5E5E5"
	  },




      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "width": "8px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "__ORGGUA__",
                    "align": "center",
                    "size": "md",

                    "weight": "bold"

                  }
                ]
              },














              {
                "type": "box",
                "layout": "vertical",
                "contents": [




                  {
                    "type": "text",
                    "text": "•",
                    "align": "center",
                    "size": "md",
                    "color": "#bbbbbb"
                  }



                ],
                "width": "20px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "__CHGGUA__",
                    "align": "center",

                    "size": "md",
                    "weight": "bold"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "width": "10px"
              }
            ],
            "offsetTop": "3px"
          }








        ],
        "margin": "md",
        "cornerRadius": "10px",
        "borderColor": "#bbbbbb",
        "borderWidth": "2px",
        "height": "30px"
      },


















      {
        "type": "box",
        "layout": "vertical",
        "margin": "xs",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "button",
                    "style": "secondary",
                    "action": {
                      "type": "postback",
                      "label": "裝卦",
                      "data": "__裝卦__",
                      "displayText": "__dis裝卦__"
                    },
                    "color": "#91A4BC",
                    "margin": "none",
                    "height": "md"
                  }
                ],
                "width": "172px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "width": "10px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "postback",
                      "label": "N",
                      "data": "__NOTION_CMD__",
                      "displayText": "__NOTION_DSP__"
                    },
                    "color": "#CEC6C0",
                    "margin": "none",
                    "height": "md",
                    "style": "secondary"
                  }
                ]
              }
            ],
            "margin": "xs"
          }
        ],
        "spacing": "sm",
        "offsetTop": "3px"
      }
    ],
    "backgroundColor": "#fefefe"
  },
  "styles": {
    "footer": {
      "separator": true
    }
  }
}
'''







































	          # }









			# 	"type": "button",
			# 	"action": {
			# 	  "type": "message",
			# 	  "label": "裝卦",
			# 	  "text": "__裝卦__"




# from guaMatch import checkMainData as ck







### 從號碼取得卦名
def getName(binary):
	for item in baGuaAllDict:
		if item['binary'] == binary:
			title = item['title']
			body = item['body']
			# 如果是純卦（八卦本體），加上 "為"
			if title in ['乾', '兌', '離', '震', '巽', '坎', '艮', '坤']:
				return f"{title}為{body}"
			else:
				if len( f"{title}{body}" ) == 4:
					return f"{title}{body}"
				else:
					return f"{title}{body}"
	return None  # 若找不到該 binary


# ## 簡體轉繁體
# def chineseChange( text = '中国的文化源远流长。123我是貓abc文化源,远流长干' ):
# 	from opencc import OpenCC
# 	# 模式	說明
# 	# 's2t'	簡體 → 繁體（一般用）
# 	# 't2s'	繁體 → 簡體
# 	# 's2tw'	簡體 → 台灣正體
# 	# 'tw2s'	台灣正體 → 簡體
# 	# 's2hk'	簡體 → 香港繁體
# 	# 'hk2s'	香港繁體 → 簡體
# 	# 'tw2sp'	台灣繁體 → 簡體（常用詞彙轉換）

# 	# 建立轉換器：從簡體轉繁體（s2t）或繁體轉簡體（t2s）
# 	cc = OpenCC('s2t')  # 簡轉繁
	
# 	converted = cc.convert(text)
# 	print(converted)  # 中國的文化源遠流長。

# chineseChange()

def clipData( fullDate ):
	return "/".join( fullDate.split("/")[:3] )


## 產生排盤 UI 
def uiInputData( dateData , date_ganZiList , finalGua , note = "test" , command = "", threePillar = False , notionAccount = False):
	# print( getFourPillar( fullDate = dateData , detail = True ))
	dateBuf = getFourPillar( fullDate = dateData , detail = True )
	# lightDate ,fullDarkDate ,fourPillar_Buf , jeChi_show , week , timeShow 
	print( ">>>",dateData )
	sun_date = '/'.join(dateBuf[0].split('/')[:3]) + dateBuf[4]
	print( sun_date )
	dark_date = dateBuf[1]
	print( dark_date )

	fourP = dateBuf[2]
	date_ganZi = ""

	if threePillar == True:
		fourP = dateBuf[2][:-1] + ["－－"]
		# print( fourP )
		## ['癸卯', '甲寅', '丁酉', '－－']


	elif  date_ganZiList:
		fourP = ['－－'] + date_ganZiList + ['－－']
		date_ganZi = ''.join(date_ganZiList) + '日'




	print( fourP )

	jeChi = jeChi_combime( dateBuf[3] ) 
	print( jeChi )
	currentTime = dateBuf[5] 
	print( currentTime )
	print( note)


	orgGua,changeGua,_,_ = checkMainData( finalGua )

	orgGuaName = getName(orgGua)
	chgGuaName = getName(changeGua)


	print( orgGua,changeGua)
	print( orgGuaName,chgGuaName)	

	# if set(orgGua).issubset({'0', '1'}):
	if ( "$" not in finalGua ) and  ( "X" not in finalGua ):
		chgGuaName = "－ － －"


	## 加入隱形空格
	# zeroSpace = '\u200b'
	# command = zeroSpace.join(command)
	import re

	display_command = command.replace( " // " , " - " , 1  )
	display_command = display_command.replace( " // " , "\\n"  )
	# display_command = re.sub( " // " , "\\n" , display_command, count=2 )

	# if date_ganZi != "":
	# 	# command = "+%s // %s // %s // %s"% ( dateData , date_ganZi , (zeroSpace.join(finalGua)) , note )
	# 	command = "+%s // %s // %s // %s"% ( dateData , date_ganZi , finalGua , note )
	# else:
	# 	# command = "+%s // %s // %s"% ( dateData , (zeroSpace.join(finalGua)) , note )	
	# 	command = "+%s // %s // %s"% ( dateData , finalGua , note )		


	# print(command)
	finalGua = finalGua.replace("0","⚋").replace("1","⚊").replace("X","✕").replace("$","〇")


	uiLayout = uiLayoutFront

	# sun_yaoNumber = [ "初九","九二","九三","九四","九五","上九" ][::-1]
	# dark_yaoNumber = [ "初六","六二","六三","六四","六五","上六" ][::-1]	

	sun_yaoNumber = [ "初爻","二爻","三爻","四爻","五爻","上爻" ][::-1]
	dark_yaoNumber = [ "初爻","二爻","三爻","四爻","五爻","上爻" ][::-1]	



	for i , row in enumerate( finalGua[::-1] ):  ##[::-1] 為反轉，因為finalGua是從下往上排的，UI是從上往下，所以要先反轉

		## 如果爻為少陰少陽
		if row == "⚋": 
			uiLayout += uiLayoutMidA.replace( "__YO__" , row ).replace( "__INDEX__" , dark_yaoNumber[i] )

		if row == "⚊" : 
			uiLayout += uiLayoutMidA.replace( "__YO__" , row ).replace( "__INDEX__" , sun_yaoNumber[i] )			

		## 如果為老陰老陽
		if  row == "✕" :
			uiLayout += uiLayoutMidB.replace( "__YO__" , row ).replace( "__INDEX__" , dark_yaoNumber[i] ).replace( '"offsetBottom": "sm"' , '"offsetBottom": "md"' )
		if row == "〇":
			uiLayout += uiLayoutMidB.replace( "__YO__" , row ).replace( "__INDEX__" , sun_yaoNumber[i] )

		# if i != len( finalGua ) -1:
		# 	uiLayout += ","
		# 	uiLayout += ui_separator
		uiLayout += ","	


	if notionAccount == True:
		uiLayout += uiLayoutBackExt  ## 有notion上傳的版本
	else:
		uiLayout += uiLayoutBack		

	# note = note.replace("#",",")
	# command = command.replace("#",",")
	# display_command = display_command.replace("#",",")


# 干支/日/2025.5.11/10/申
	reDataLayout =   (  uiLayout.replace("節氣", jeChi )
								.replace("__sunDate__", sun_date )
								.replace("__darkDate__", dark_date )
								.replace("年柱", fourP[0] )
								.replace("月柱", fourP[1] )
								.replace("日柱", fourP[2] )
								.replace("時柱", fourP[3] )
								.replace("__NOTE__", note )
								.replace("12:00", currentTime )
								.replace("__裝卦__", command )
								.replace("__dis裝卦__", display_command )								
								.replace("__ORGGUA__" , orgGuaName)
								.replace("__CHGGUA__" , chgGuaName)
						)

	if date_ganZiList: ## 自定月日
		reDataLayout = reDataLayout.replace( "month_mode","- - -" ).replace( "day_mode" , "- - -" ).replace( "hour_mode" , "- - -" ).replace ( "jechi_mode" , "- - -")
		reDataLayout = reDataLayout.replace("#000001", "#cccccc" ).replace("#000003", "#cccccc" ).replace("#444443", "#999999" ).replace("#FCA32D", "#dddddd" ).replace(currentTime ,"00:00" )
	
	elif threePillar:
		reDataLayout = reDataLayout.replace("#000003", "#cccccc" ).replace("#FCA32D", "#dddddd" ).replace(currentTime ,"00:00" )
		reDataLayout = reDataLayout.replace( "month_mode" , "干支/月/" + "6/" + clipData(dateData).replace("/","-")  ).replace( "day_mode" , "干支/日/" + "6/" + clipData(dateData).replace("/","-")  ).replace( "hour_mode" , "- - -" ) .replace( "jechi_mode" , "干支/節氣/" + "6/" + clipData(dateData).replace("/","-") )
	else:
		reDataLayout = reDataLayout.replace( "month_mode" , "干支/月/" + "6/" + clipData(dateData).replace("/","-")  ).replace( "day_mode" , "干支/日/" + "6/" + clipData(dateData).replace("/","-")  ).replace( "hour_mode" , "干支/時/" + "6/" + dateData.replace("/","-")  ).replace( "jechi_mode" , "干支/節氣/" + "6/" + clipData(dateData).replace("/","-") )

	if note == "no title":
		reDataLayout = reDataLayout.replace( "#9BB0CE" , "#FF6470" )



# pushToNotion( apiToken , pageId , imageUrl , titleText )
	reDataLayout = reDataLayout.replace("__NOTION_DSP__", "☕ Uploading,please wait……" ).replace("__NOTION_CMD__", "n" + command )

# ⏳⚡
	# print( reDataLayout )

	# 文字轉換成字典
	reDataLayout_dict = json.loads(reDataLayout)
	return( reDataLayout_dict )


##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################















		
startLayout = """{

	"type": "bubble",
	"body": {
	"type": "box",
	"layout": "vertical",
	"contents": [
		{
				"type": "box",
				"layout": "horizontal",
				"contents": [
					{
						"type": "box",
						"layout": "horizontal",
						"contents": [
							{
								"type": "text",
								"text": "歲次干支",
								"weight": "bold",
								"color": "#1DB446",
								"size": "lg",
								"flex": 2
							}
						],
						"width": "80px"
					},
					{
						"type": "filler"
					},
					{
						"type": "box",
						"layout": "horizontal",
						"contents": [
							{
								"type": "text",
								"text": "index",
								"weight": "regular",
								"color": "#bbbbb0",
								"size": "sm",
								"gravity": "bottom",
								"flex": 3,
								"align": "end"
							},
							{
								"type": "text",
								"text": "__INDEX__",
								"weight": "bold",
								"color": "#bbbbb0",
								"size": "md",
								"flex": 3,
								"gravity": "bottom",
								"margin": "xs"
							}
						],
						"width": "80px"
					},
					{
						"type": "filler"
					},
					{
						"type": "box",
						"layout": "horizontal",
						"contents": [
							{
								"type": "text",
								"text": "by",
								"weight": "regular",
								"color": "#999999",
								"size": "sm",
								"flex": 3,
								"align": "end",
								"gravity": "bottom"
							},
							{
								"type": "text",
								"text": "日",
								"weight": "bold",
								"color": "#777777",
								"size": "lg",
								"gravity": "bottom",
								"align": "end",
								"margin": "xs",
								"flex": 0
							}
						],
						"width": "100px"
					}
				]
			},

		{
		"type": "separator",
		"margin": "none"
		},"""


date_separator = """
							{
								"type": "separator",
								"margin": "sm" 
							},"""


hourModeLayout = """
								{
									"type": "box",
									"layout": "horizontal",
									"contents": [
										{
											"type": "text",
											"text": "年柱",
											"weight": "regular",
											"size": "lg",
											"margin": "none",
											"wrap": true,
											"flex": 0,
											"gravity": "bottom",
											"color": "#888888"
										},
										{
											"type": "text",
											"text": "|",
											"size": "lg",
											"margin": "xs",
											"color": "#cccccc",
											"flex": 0,
											"gravity": "center",
											"weight": "regular"
										},

										{
											"type": "text",
											"text": "月柱",
											"weight": "regular",
											"size": "lg",
											"margin": "xs",
											"wrap": true,
											"flex": 0,
											"color": "#888888",
											"gravity": "bottom"
											




										},
										{
											"type": "text",
											"text": "|",
											"size": "lg",
											"margin": "xs",
											"color": "#cccccc",
											"flex": 0,
											"gravity": "center",
											"weight": "regular"
										},
										{
											"type": "text",
											"text": "日柱",
											"weight": "regular",
											"size": "lg",
											"margin": "xs",
											"wrap": true,
											"flex": 0,
											"color": "#888888",
											"gravity": "bottom"
										},
										{
											"type": "text",
											"text": "|",
											"size": "lg",
											"margin": "xs",
											"color": "#cccccc",
											"flex": 0,
											"gravity": "center",
											"weight": "regular"
										},
										{
											"type": "text",
											"text": "時柱",
											"weight": "bold",
											"size": "lg",
											"margin": "xs",
											"wrap": true,
											"flex": 0,
											"color": "#2E4E7C"
										}
									],
									"margin": "xs"
								},

								{
								"type": "box",
								"layout": "horizontal",

						        "contents": [
						                  {
								            "type": "box",
								            "layout": "vertical",
								            "contents": [],
								            "flex": 0,
								            "width": "20px"
								          },
								          {
								            "type": "text",
								            "text": "__JECHI__",
								            "size": "sm",
								            "color": "#ff5252",
								            "wrap": true,
								            "weight": "bold",
								            "margin": "none",
								            "gravity": "bottom",
								            "offsetTop": "-1px",
								            "align": "end",
								            "flex": 1,
								            "offsetStart": "-5px"
								          },



								          {
								            "type": "text",
								            "text": "__TIME__",
								            "size": "md",
								            "color": "#34495e",
								            "wrap": true,
								            "weight": "regular",
								            "margin": "none",
								            "align": "end",
								            "gravity": "bottom",
								            "flex": 2
								          }
						            ],

						            "flex": 3,
						            "offsetStart": "1px"
						          },"""





dayModeLayout = """{
										"type": "box",
										"layout": "horizontal",
										"contents": [
											{
												"type": "text",
												"text": "年柱",
												"weight": "regular",
												"size": "lg",
												"margin": "none",
												"wrap": true,
												"flex": 0,
												"gravity": "bottom",
												"color": "#888888"
											},
											{
												"type": "text",
												"text": "|",
												"size": "lg",
												"margin": "xs",
												"color": "#cccccc",
												"flex": 0,
												"gravity": "center",
												"weight": "regular"
											},
											{
												"type": "text",
												"text": "月柱",
												"weight": "regular",
												"size": "lg",
												"margin": "xs",
												"wrap": true,
												"flex": 0,
												"color": "#2E4E7C",
												"gravity": "bottom"
											},
											{
												"type": "text",
												"text": "|",
												"size": "lg",
												"margin": "xs",
												"color": "#cccccc",
												"flex": 0,
												"gravity": "center",
												"weight": "regular"
											},
											{
												"type": "text",
												"text": "日柱",
												"weight": "bold",
												"size": "lg",
												"margin": "xs",
												"wrap": true,
												"flex": 0,
												"color": "#2e4e7c",
												"gravity": "bottom",
												"action": {
												  "type": "message",
												  "label": "action",
												  "text": "_時_"
												}
											},

														  {
															"type": "box",
															"layout": "horizontal",
								


												            "contents": [
												              {
												                "type": "text",
												                "text": "__JECHI__",
												                "size": "sm",
												                "color": "#ff5252",
												                "wrap": true,
												                "weight": "bold",
												                "margin": "none",
												                "align": "end",
												                "gravity": "bottom",
												                "offsetTop": "-1px"
												              }

												            ],
												            "flex": 3,
												            "maxWidth": "28px",
												            "offsetStart": "0px",
												            "margin": "sm"
												          },


												          {
												            "type": "text",
												            "text": "__TIME__",
												            "size": "md",
												            "color": "#34495e",
												            "weight": "regular",
												            "margin": "none",
												            "align": "end",
												            "gravity": "bottom",
												            "flex": 10,
												            "wrap": true
												          }
												        ],



										"offsetEnd": "1px",
										"margin": "sm"
									},"""





monthModeLayout = """{
										"type": "box",
										"layout": "horizontal",
										"contents": [
											{
												"type": "text",
												"text": "年柱",
												"weight": "regular",
												"size": "lg",
												"margin": "none",
												"wrap": true,
												"flex": 0,
												"gravity": "bottom",
												"color": "#888888"
											},
											{
												"type": "text",
												"text": "|",
												"size": "lg",
												"margin": "xs",
												"color": "#cccccc",
												"flex": 0,
												"gravity": "center",
												"weight": "regular"
											},
											{
												"type": "text",
												"text": "月柱",
												"weight": "bold",
												"size": "lg",
												"margin": "xs",
												"wrap": true,
												"flex": 0,
												"color": "#2E4E7C",
												"gravity": "bottom"


											},
											{
												"type": "text",
												"text": "|",
												"size": "lg",
												"margin": "xs",
												"color": "#cccccc",
												"flex": 0,
												"gravity": "center",
												"weight": "regular"
											},
											{
												"type": "text",
												"text": "日柱",
												"weight": "regular",
												"size": "lg",
												"margin": "xs",
												"wrap": true,
												"flex": 0,
												"color": "#2e4e7c",
												"gravity": "bottom",	

												"action": {
												  "type": "message",
												  "label": "action",
												  "text": "_日_"
												}
											},

														  {
															"type": "box",
															"layout": "horizontal",

												            "contents": [
												              {
												                "type": "text",
												                "text": "__JECHI__",
												                "size": "sm",
												                "color": "#ff5252",
												                "wrap": true,
												                "weight": "bold",
												                "margin": "none",
												                "align": "end",
												                "gravity": "bottom",
												                "offsetTop": "-1px"
												              }

												            ],
												            "flex": 3,
												            "maxWidth": "28px",
												            "offsetStart": "0px",
												            "margin": "sm"
												          },
												          {
												            "type": "text",
												            "text": "__TIME__",
												            "size": "md",
												            "color": "#34495e",
												            "weight": "regular",
												            "margin": "none",
												            "align": "end",
												            "gravity": "bottom",
												            "flex": 10,
												            "wrap": true
												          }
												        ],











										"offsetEnd": "1px",
										"margin": "sm"
									},"""






endLayout = """{
									"type": "separator",
									"margin": "none",
									"color": "#ffffff"
								}
							]
						},
						"styles": {
							"body": {
								"backgroundColor": "#FFFFFF"
							},
							"footer": {
								"separator": true
							}
						}
					}"""


def jeChi_combime(data): 
	# ['立夏', '>', '小滿']   # 立夏→小滿
	# ['立夏', '!', '小滿']   # [立夏]→小滿
	a, symbol, b = data
	if symbol == '>':
		return f"{a}→{b}"
	elif symbol == '!':
		return f"[{a}]→{b}"
	else:
		return f"{a} {symbol} {b}"


## 產生四柱列表的UI(月，日 ，時，節氣)
def ganZiList_fun( currentTime = "" , dayMode = "d" , index = "" , runtime = 10 ):
	# dayMode	= dayMode.lower().replace( "jc","節氣").replace("jechi","節氣") 
# "2023/5/17/12/00"
# "2023/5/17"  --> "2023/5/17/00/00"

	print( currentTime )
	kongWangList = [  "甲子","甲戌","甲申","甲午","甲辰","甲寅"  ]

	dayMode	= dayMode.replace( "jechi","jc" ).replace( "節氣","jc" ).replace( "月","m" ).replace( "日","d" ).replace( "時","h" )
	dateDataList = PPPPP ( currentTime = currentTime , dayMode = dayMode , index = index , runtime = runtime )
	for i in dateDataList:
		print(i)  

	if dayMode.lower() == "m":
		startLayout_buf = startLayout.replace("日","月")
	elif dayMode.lower() == "h":
		startLayout_buf = startLayout.replace("日","時")		

	elif dayMode == "jc": ## 如果為節氣，則以"日"模式進行
		startLayout_buf = startLayout.replace("日","節氣")	
		# startLayout_buf = startLayout
	else:
		startLayout_buf = startLayout

	if index == "":
		indexColor = "#ffffff"
		finalLayout = startLayout_buf.replace( "#bbbbb0" , indexColor )
	else:
		indexColor = "#777777"
		finalLayout = startLayout_buf.replace( "#bbbbb0" , indexColor )

	# dayModeLayout
	# finalLayout = startLayout_buf
	finalLayout += date_separator

	# ['乙巳-庚辰-乙巳', '2025/04/06'] "2025·04·07"

	for i , row in enumerate(dateDataList):
		## 月
		if ( dayMode.lower() == "m" ) or ( dayMode.lower() == "月" ):
			# print( dayMode.lower())
			# print( row[0].split("-")[0] , row[0].split("-")[1] , row[0].split("-")[2]  , row[0].split("-")[3] )
			# ['乙巳-乙酉-丙申', '2025/09/23', '(二)', '秋分']
			lightDate = "'" + row[1][2:]  +row[2]
			buf_dayModeLayout = monthModeLayout.replace("年柱", row[0].split("-")[0] ).replace("月柱", row[0].split("-")[1] ).replace("日柱", row[0].split("-")[2] ).replace("__TIME__", lightDate ).replace("__JECHI__", row[3] if row[3] != '' else '　')
			buf_dayModeLayout = buf_dayModeLayout.replace("ff5252", "888888")
			## 出空之日變色
			# if row[0].split("-")[2] in kongWangList:
			# 	buf_dayModeLayout = buf_dayModeLayout.replace ( "#2e4e7c" , "#3aa078" )

			currentTimeBuf = row[1].replace( "/" , ",")  ## "干支/日/2023-05-06/15"
			day_command =  f"干支/日/{8}/{currentTimeBuf}" ##"干支/日/%s/%s"% ( "2023-05-06" , "15" )

			buf_dayModeLayout = buf_dayModeLayout.replace( "_日_", day_command )			
			# buf_dayModeLayout = monthModeLayout.replace("年柱", row[0].split("-")[0] ).replace("月柱", row[0].split("-")[1] ).replace("日柱", row[0].split("-")[2] ) .replace("__TIME__", row[1] ).replace("#2e4e7c", "#cccccc" )
			
			finalLayout += buf_dayModeLayout ## 每日項目
			if i != len( dateDataList ) -1:
				finalLayout += date_separator

		## 日
		if (dayMode.lower() == "d") or (dayMode == "jc"):
			# print( row[0].split("-")[0] , row[0].split("-")[1] , row[0].split("-")[2]  , row[0].split("-")[3] )
			# ['乙巳-乙酉-丙申', '2025/09/23', '秋分', '(二)']
			lightDate = "'" + row[1][2:]  +row[2]


			buf_dayModeLayout = dayModeLayout.replace("年柱", row[0].split("-")[0] ).replace("月柱", row[0].split("-")[1] ).replace("日柱", row[0].split("-")[2] ).replace("__TIME__", lightDate ).replace("__JECHI__", row[3] if row[3] != '' else '　')
			
			## 出空之日變色			
			if (row[0].split("-")[2] in kongWangList) and (dayMode.lower() == "d"):
				buf_dayModeLayout = buf_dayModeLayout.replace ( "#2e4e7c" , "#3aa078" )
			
			if dayMode == "jc":
				buf_dayModeLayout = buf_dayModeLayout.replace("ff5252", "888888")

			currentTimeBuf = row[1].replace( "/" , ",")  ## "干支/日/2023-05-06/15"
			hour_command =  f"干支/時/{8}/{currentTimeBuf}" ##"干支/日/%s/%s"% ( "2023-05-06" , "15" )

			buf_dayModeLayout = buf_dayModeLayout.replace( "_時_", hour_command )

			finalLayout += buf_dayModeLayout ## 每日項目
			if i != len( dateDataList ) -1:
				finalLayout += date_separator

		## 時
		if dayMode.lower() == "h":		
			# 時
			buf_hourModeLayout = hourModeLayout.replace("年柱", row[0].split("-")[0] ).replace("月柱", row[0].split("-")[1] ).replace("日柱", row[0].split("-")[2] ).replace("時柱", row[0].split("-")[3] ).replace("__TIME__", row[1]+row[2] ).replace("__JECHI__", row[3] if row[3] != '' else '　')
			finalLayout += buf_hourModeLayout	
			if i != len( dateDataList ) -1:
				finalLayout += date_separator
	finalLayout +=endLayout
	print ( finalLayout )

	# 文字轉換成字典
	finalLayout_dict = json.loads(finalLayout)
	return finalLayout_dict



if __name__ == '__main__':
	# ganZiList_fun( currentTime = "" , dayMode = "jc" , index = "" , runtime = 10 )
	# ganZiList_fun( currentTime = "" , dayMode = "d" , index = "" , runtime = 10 )
	ganZiList_fun( currentTime = "2025/05/08" , dayMode = "h" , index = "" , runtime = 5 )	

# "干支/時/10/2025-08-31-15-48"
	# "d" -- day
	# "m" -- month
	# "h" -- hour
	# "節氣"

	# 干支/日/2025.5.11/10/申
# ['乙巳-乙酉-己卯', '2025/09/07', '白露']



# # 年干支
# {


#       "type": "bubble",
#       "body": {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#           {
#             "type": "text",
#             "text": "年干支",
#             "weight": "bold",
#             "color": "#1DB446",
#             "size": "lg"
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "_GZ",
#                 "weight": "bold",
#                 "size": "xxl",
#                 "margin": "none",
#                 "flex": 5
#               },
#               {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "_yearShow",
#                     "size": "lg",
#                     "color": "#888888",
#                     "wrap": true,
#                     "weight": "bold",
#                     "margin": "sm",
#                     "flex": 2,
#                     "gravity": "bottom",
#                     "align": "end"
#                   }
#                 ],
#                 "flex": 0
#               }
#             ]
#           },
#           {
#             "type": "separator",
#             "margin": "md"
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "margin": "sm",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "◁",
#                 "size": "md",
#                 "color": "#000000",
#                 "flex": 0,
#                 "action": {
#                   "type": "message",
#                   "label": "action",
#                   "text": "_pre"
#                 },
#                 "weight": "bold"
#               },
#               {
#                 "type": "text",
#                 "text": "▷",
#                 "size": "md",
#                 "color": "#000000",
#                 "weight": "bold",
#                 "action": {
#                   "type": "message",
#                   "label": "action",
#                   "text": "_next"
#                 },
#                 "align": "end"
#               }
#             ]
#           }
#         ]
#       },
#       "styles": {
#         "footer": {
#           "separator": true
#         }
#       }
#     }


















# upLayoutFelx = """{  
    
#       "type": "bubble",
#       "body": {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "_type",
#                 "weight": "bold",
#                 "color": "#1DB446",
#                 "size": "lg",
#                 "margin": "none"
#               },
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "__TITLE__",
#                     "weight": "bold",
#                     "size": "3xl",
#                     "wrap": true,
#                     "margin": "none",
#                     "offsetTop": "none",
#                     "offsetBottom": "none",
#                     "action": {
#                       "type": "message",
#                       "label": "action",
#                       "text": "hello"
#                     },
#                     "offsetStart": "0px"
#                   },


#                   {
#                     "type": "text",
#                     "text": "__ETC__",
#                     "weight": "bold",
#                     "color": "#FF7777",
#                     "size": "lg",
#                     "margin": "none",
#                     "wrap": true,
#                     "gravity": "bottom",
#                     "offsetBottom": "5px",
#                     "offsetEnd": "6px",
#                     "align": "end",
#                     "flex": 1
#                   }               

#                 ]
#               },
#               {
#                 "type": "text",
#                 "text": "__SUB__",
#                 "weight": "bold",
#                 "size": "md",
#                 "margin": "xs",
#                 "wrap": true,
#                 "offsetTop": "none",
#                 "offsetBottom": "none",
#                 "action": {
#                   "type": "message",
#                   "label": "action",
#                   "text": "hello"
#                 },
#                 "color": "#888888"
#               }
#             ]
#           },





# 		  {
#             "type": "separator",
#             "margin": "md",
#             "color": "#848484"
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [

#               {
#                 "type": "text",
#                 "text": "____title",
#                 "size": "lg",
#                 "color": "#555555",
#                 "wrap": true,
#                 "weight": "bold",
#                 "margin": "lg"
#               },
#               {
#                 "type": "text",
#                 "text": "____text",
#                 "size": "md",
#                 "color": "#000000",
#                 "wrap": true,
#                 "margin": "xs"
#               }
#             ]
#           },

















#           {
#             "type": "separator",
#             "margin": "md",
#             "color": "#ffffff"
#           }
#         ]
#       },
#       "styles": {
#         "footer": {
#           "separator": true
#         }
#       }
#     }
# """


    # ## 兩塊色塊資訊
    # useShin_flexMsg_color = """
    #             ,
    #               {
    #                 "type": "box",
    #                 "layout": "horizontal",
    #                 "contents": [],
    #                 "backgroundColor": "_colorA",
    #                 "position": "absolute",
    #                 "height": "37px",
    #                 "width": "37px",
    #                 "offsetStart": "172px",
    #                 "offsetTop": "5px",
    #                 "cornerRadius": "5px",
    #                 "borderWidth": "2px",
    #                 "borderColor": "#999999"
    #               },
    #               {
    #                 "type": "box",
    #                 "layout": "horizontal",
    #                 "contents": [],
    #                 "backgroundColor": "_colorB",
    #                 "position": "absolute",
    #                 "height": "37px",
    #                 "width": "37px",
    #                 "offsetStart": "216px",
    #                 "offsetTop": "5px",
    #                 "cornerRadius": "5px",
    #                 "borderColor": "#999999",
    #                 "borderWidth": "2px"
    #               }"""

    # ## 右邊補充文字
    # etc_flex_layout = """
    #             ,
    #               {
    #                 "type": "text",
    #                 "text": "_subEtc",
    #                 "weight": "bold",
    #                 "color": "#FF7777",
    #                 "size": "lg",
    #                 "margin": "none",
    #                 "wrap": true,
    #                 "gravity": "bottom",
    #                 "offsetBottom": "5px",
    #                 "offsetEnd": "6px",
    #                 "align": "end",
    #                 "flex": 1
    #               }"""

    # ## 內容(可多塊)
    # useShin_flexMsg_insert = """
    #       {
    #         "type": "separator",
    #         "margin": "md",
    #         "color": "#848484"
    #       },
    #       {
    #         "type": "box",
    #         "layout": "vertical",
    #         "contents": [

    #           {
    #             "type": "text",
    #             "text": "____title",
    #             "size": "lg",
    #             "color": "#555555",
    #             "wrap": true,
    #             "weight": "bold",
    #             "margin": "lg"
    #           },
    #           {
    #             "type": "text",
    #             "text": "____text",
    #             "size": "md",
    #             "color": "#000000",
    #             "wrap": true,
    #             "margin": "xs"
    #           }
    #         ]
    #       }"""