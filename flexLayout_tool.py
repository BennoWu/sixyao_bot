# -*- coding: utf-8 -*-
from fourPillar_tool import PPPPP # 四柱得日期
from fourPillar_tool import getFourPillar # 四柱得日期
from fourPillar_tool import getGanziYear # 取得年干支list
from fourPillar_tool import ganZhi_Dict ## 六十甲子的字典
from fourPillar_tool import checkYear


from guaMatch import checkMainData as checkMainData

from sixYao_data import  * # baGuaAllDict 取得
from small_six_zan_work import sSixZmain ## 小六壬
import json



##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################


uiLayoutFront ="""
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
			"size": "md",
            "action": {
              "type": "postback",
              "label": "action",
              "data": "hello",
              "displayText": "__SHOW__"
            }
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
			  "text": "month_mode"
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
			  "text": "day_mode"
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
			  "text": "hour_mode"
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
				"type": "box",
				"layout": "horizontal",
				"contents": [
				  {
					"type": "box",
					"layout": "vertical",
					"contents": [
					  {
						"type": "text",
						"text": "__sunDate__",
						"size": "sm",
						"color": "#444445",
						"wrap": true,
						"weight": "regular",
						"margin": "none",
						"align": "start",
						"offsetTop": "2px",
						"flex": 0
					  }
					],
					"width": "150px"
				  },
				  {
					"type": "box",
					"layout": "vertical",
					"contents": [ 
					  {
						"type": "text",
						"text": "12:00",
						"size": "sm",
						"color": "#444445",
						"wrap": true,
						"weight": "regular",
						"offsetTop": "2px",
						"align": "end"
					  }
					],
					"width": "80px"
				  }
				]
			  },
			  {
				"type": "text",
				"text": "__darkDate__",
				"size": "sm",
				"color": "#444443",
				"wrap": true,
				"weight": "regular",
				"margin": "xs"
			  }
			],
			"margin": "none",
			"flex": 0,
			"height": "40px"
		  },
		  {
			"type": "box",
			"layout": "vertical",
			"contents": [],
			"width": "10px",
			"offsetStart": "7px",
			"offsetBottom": "8px"
		  }
		],
		"margin": "none"
	  },
	  {
		"type": "separator",
		"margin": "sm",
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
				"cornerRadius": "20px",
				"action": {
				  "type": "postback",
				  "label": "文字版",
				  "data": "__TXT__",
				  "displayText": "/(^o^)/ text version"
				}
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
			"margin": "xs"
		  }
		],
		"margin": "sm"
	  },









	  {
		"type": "box",
		"layout": "vertical",
		"contents": [],
		"margin": "sm",
		"cornerRadius": "10px",
		"action": {
				  "type": "message",
				  "label": "cmd",
				  "text": "__裝卦buf__"
				}
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
				"width": "15px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [
				  {
					"type": "text",
					"text": "__YO1__",
					"size": "xl",
					"weight": "bold",
					"align": "center",
					"color": "#657C96"
				  }
				],
				"width": "30px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [],
				"width": "5px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [
				  {
					"type": "text",
					"text": "__YO2__",
					"size": "xl",
					"weight": "bold",
					"align": "center",
					"color": "#657C96"
				  }
				],
				"width": "30px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [],
				"width": "5px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [
				  {
					"type": "text",
					"text": "__YO3__",
					"size": "xl",
					"weight": "bold",
					"align": "center",
					"color": "#657C96"
				  }
				],
				"width": "30px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [],
				"width": "5px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [
				  {
					"type": "text",
					"text": "__YO4__",
					"size": "xl",
					"weight": "bold",
					"align": "center",
					"color": "#657C96"
				  }
				],
				"width": "30px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [],
				"width": "5px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [
				  {
					"type": "text",
					"text": "__YO5__",
					"size": "xl",
					"weight": "bold",
					"align": "center",
					"color": "#657C96"
				  }
				],
				"width": "30px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [],
				"width": "5px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [
				  {
					"type": "text",
					"text": "__YO6__",
					"size": "xl",
					"weight": "bold",
					"align": "center",
					"color": "#657C96"
				  }
				],
				"width": "30px"
			  }
			],
			"backgroundColor": "#eeeeee",
			"cornerRadius": "10px"
		  }
		],
		"margin": "sm"
	  },
	  {
		"type": "separator",
		"margin": "md",
		"color": "#aaaaaa"
	  },"""




uiLayoutBack = """   
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
				"height": "sm"
			  }
			],
			"margin": "sm"
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

"""


uiLayoutBackExt = """   
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
					"height": "sm"
				  }
				],
				"width": "176px"
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
					"height": "sm",
					"style": "secondary"
				  }
				]
			  }
			],
			"margin": "sm"
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

"""












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
def uiInputData( dateData , date_ganZiList , finalGua , note = "test" , command = "", threePillar = False , notionAccount = False , printMode = False , dateSureMark = False ):
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
	display_notion_command = "☕ Uploading... // " + "n" + display_command
	display_notion_command = display_notion_command.replace( " // " , "\\n"  )

	display_notion_command = "☕ Uploading..... "


	commandExt = "&"+ command + "&"

 # Uploading,please wait……"
	# display_command = re.sub( " // " , "\\n" , display_command, count=2 )

	# if date_ganZi != "":
	# 	# command = "+%s // %s // %s // %s"% ( dateData , date_ganZi , (zeroSpace.join(finalGua)) , note )
	# 	command = "+%s // %s // %s // %s"% ( dateData , date_ganZi , finalGua , note )
	# else:
	# 	# command = "+%s // %s // %s"% ( dateData , (zeroSpace.join(finalGua)) , note )	
	# 	command = "+%s // %s // %s"% ( dateData , finalGua , note )		


	# print(command)
	finalGua = finalGua.replace("0","⚋").replace("1","⚊").replace("X","✕").replace("$","〇")


# uiLayoutFront
# uiLayoutBack
# uiLayoutBackExt




	uiLayout = uiLayoutFront

	# sun_yaoNumber = [ "初九","九二","九三","九四","九五","上九" ][::-1]
	# dark_yaoNumber = [ "初六","六二","六三","六四","六五","上六" ][::-1]	

	# sun_yaoNumber = [ "初爻","二爻","三爻","四爻","五爻","上爻" ][::-1]
	# dark_yaoNumber = [ "初爻","二爻","三爻","四爻","五爻","上爻" ][::-1]	



	# for i , row in enumerate( finalGua[::-1] ):  ##[::-1] 為反轉，因為finalGua是從下往上排的，UI是從上往下，所以要先反轉

	# 	## 如果爻為少陰少陽
	# 	if row == "⚋": 
	# 		uiLayout += uiLayoutMidA.replace( "__YO__" , row ).replace( "__INDEX__" , dark_yaoNumber[i] )

	# 	if row == "⚊" : 
	# 		uiLayout += uiLayoutMidA.replace( "__YO__" , row ).replace( "__INDEX__" , sun_yaoNumber[i] )			

	# 	## 如果為老陰老陽
	# 	if  row == "✕" :
	# 		uiLayout += uiLayoutMidB.replace( "__YO__" , row ).replace( "__INDEX__" , dark_yaoNumber[i] ).replace( '"offsetBottom": "sm"' , '"offsetBottom": "md"' )
	# 	if row == "〇":
	# 		uiLayout += uiLayoutMidB.replace( "__YO__" , row ).replace( "__INDEX__" , sun_yaoNumber[i] )

	# 	# if i != len( finalGua ) -1:
	# 	# 	uiLayout += ","
	# 	# 	uiLayout += ui_separator
	# 	uiLayout += ","	

	uiLayout =  (   uiLayout.replace( "__YO1__", finalGua[0] )
							.replace( "__YO2__", finalGua[1] )
							.replace( "__YO3__", finalGua[2] )
							.replace( "__YO4__", finalGua[3] )
							.replace( "__YO5__", finalGua[4] )
							.replace( "__YO6__", finalGua[5] )
				)

	if notionAccount == True:
		uiLayout += uiLayoutBackExt  ## 有notion上傳的版本
	else:
		uiLayout += uiLayoutBack		

	# note = note.replace("#",",")
	# command = command.replace("#",",")
	# display_command = display_command.replace("#",",")
# 📄
# 干支/日/2025.5.11/10/申
	reDataLayout =   (  uiLayout.replace("__sunDate__",  "國曆: " + sun_date )
								.replace("__darkDate__", "農曆: " + dark_date + " • " + jeChi )
								.replace("年柱", fourP[0] )
								.replace("月柱", fourP[1] )
								.replace("日柱", fourP[2] )
								.replace("時柱", fourP[3] )
								.replace("__NOTE__", note )
								.replace("__TXT__", "t" + display_command )	

								.replace("__裝卦buf__", commandExt )															
								.replace("12:00", currentTime )
								.replace("__裝卦__", command )
								.replace("__dis裝卦__", display_command )								
								.replace("__ORGGUA__" , orgGuaName)
								.replace("__CHGGUA__" , chgGuaName)
								.replace("__SHOW__", command[1:] )

						)
	# print("dateMark - " , dateSureMark )
	if dateSureMark == True:
		reDataLayout = reDataLayout.replace( "#444445" , "#F15B5E")

	if date_ganZiList: ## 自定月日
		reDataLayout = reDataLayout.replace( "month_mode","- - -" ).replace( "day_mode" , "- - -" ).replace( "hour_mode" , "- - -" ).replace ( "jechi_mode" , "- - -")
		reDataLayout = reDataLayout.replace("#000001", "#cccccc" ).replace("#000003", "#cccccc" ).replace("#444443", "#999999" ).replace("#FCA32D", "#dddddd" ).replace(currentTime ,"00:00" )
	
	elif threePillar:
		reDataLayout = reDataLayout.replace("#000003", "#cccccc" ).replace("#FCA32D", "#dddddd" ).replace(currentTime ,"00:00" )
		reDataLayout = reDataLayout.replace( "month_mode" , "干支/月/" + "6/" + clipData(dateData).replace("/","-")  ).replace( "day_mode" , "干支/日/" + "6/" + clipData(dateData).replace("/","-")  ).replace( "hour_mode" , "- - -" ) .replace( "jechi_mode" , "干支/節氣/" + "6/" + clipData(dateData).replace("/","-") )
	else:
		reDataLayout = reDataLayout.replace( "month_mode" , "干支/月/" + "6/" + clipData(dateData).replace("/","-")  ).replace( "day_mode" , "干支/日/" + "6/" + clipData(dateData).replace("/","-")  ).replace( "hour_mode" , "干支/時/" + "6/" + dateData.replace("/","-")  ).replace( "jechi_mode" , "干支/節氣/" + "6/" + clipData(dateData).replace("/","-") )

	if note == "Untitled":
		reDataLayout = reDataLayout.replace( "#9BB0CE" , "#FF6470" )



# pushToNotion( apiToken , pageId , imageUrl , titleText )
	reDataLayout = reDataLayout.replace("__NOTION_DSP__",  display_notion_command ).replace("__NOTION_CMD__", "n" + command )
	# print( "Notion:")
	# print ( display_notion_command.replace("☕...\\n" , ""))

# ⏳⚡
	if printMode == True:
		print( reDataLayout )

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
								},
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "More..",
									"size": "lg",
									"align": "end",
									"weight": "bold",
									"action": {
									  "type": "message",
									  "label": "action",
									  "text": "__MORE__"
									}
								  }
								],
								"margin": "md"
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
def ganZiList_fun( currentTime = "" , dayMode = "d" , index = "" , runtime = 10 , printMode = False):
	# dayMode	= dayMode.lower().replace( "jc","節氣").replace("jechi","節氣") 






# "2023/5/17/12/00"
# "2023/5/17"  --> "2023/5/17/00/00"
	if runtime > 20:
		runtime = 20
	print( currentTime )
	kongWangList = [  "甲子","甲戌","甲申","甲午","甲辰","甲寅"  ]

	hourMuuList = [ "乙未","丙戌","辛丑","壬辰" ]

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


	zhong_qi = [
		"雨水",
		"春分",
		"穀雨",
		"小滿",
		"夏至",
		"大暑",
		"處暑",
		"秋分",
		"霜降",
		"小雪",
		"冬至",
		"大寒"
	]

	step_day = [
		"立春",
		"立夏",
		"立秋",
		"立冬",
		"春分",
		"夏至",
		"秋分",
		"冬至"
		]





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
			# ['乙巳-辛巳-甲戌', '2025/05/05', '(一)', '立夏']

			buf_dayModeLayout = dayModeLayout.replace("年柱", row[0].split("-")[0] ).replace("月柱", row[0].split("-")[1] ).replace("日柱", row[0].split("-")[2] ).replace("__TIME__", lightDate ).replace("__JECHI__", row[3] if row[3] != '' else '　')
			
			## 出空之日變色			
			if (row[0].split("-")[2] in kongWangList) and (dayMode.lower() == "d"):
				buf_dayModeLayout = buf_dayModeLayout.replace ( "#2e4e7c" , "#3aa078" )
			
			if dayMode == "jc":
				# print(row[3])

				if row[3] in zhong_qi:
					buf_dayModeLayout = buf_dayModeLayout.replace("ff5252", "777777") ## 中氣顏色
				else:
					buf_dayModeLayout = buf_dayModeLayout.replace("ff5252", "333333")	

			# if dayMode == "d":
			# 	if row[3] in step_day:
			# 		buf_dayModeLayout = buf_dayModeLayout.replace("ff5252", "79A1CF") ## 節令顏色


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
			if  row[0].split("-")[3] in hourMuuList:
				buf_hourModeLayout = buf_hourModeLayout.replace( "#2E4E7C" , "#998675")
			
			finalLayout += buf_hourModeLayout	
			if i != len( dateDataList ) -1:
				finalLayout += date_separator

	if dayMode == "h":
		showDayMode = "時"
	elif dayMode == "d":
		showDayMode = "日"
	elif dayMode == "m":
		showDayMode = "月"	
	elif dayMode == "jc":
		showDayMode = "節氣"
	else:
		pass


	print(row[1].replace("/" , "/")) 
	moreCmdDate = PPPPP ( currentTime = row[1] , dayMode = dayMode  , runtime = 2 )[-1][1].replace("/","-").replace(":","-")

	if ( dayMode.lower() == "d" ) or ( dayMode.lower() == "h" ) :
		print( "## ",moreCmdDate )
		more_command = "干支/" + showDayMode + "/" + moreCmdDate			

	else:
		print("## ", row[1] )
		more_command = "干支/" + showDayMode + "/" + row[1].replace("/","-").replace(":","-")


	finalLayout += endLayout.replace( "__MORE__" , more_command )
	if index:
		finalLayout = finalLayout.replace( "__INDEX__" , index )

	if printMode == True:
		print ( finalLayout )

	# 文字轉換成字典
	finalLayout_dict = json.loads(finalLayout)
	return finalLayout_dict








start_yearListFlex = """

{
  "type": "bubble",
  "body": {
	"type": "box",
	"layout": "vertical",
	"contents": [

"""



item_yearListFlex = """
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
				"text": "____gz_a",
				"color": "#333334",
				"weight": "bold",
				"size": "sm",
				"align": "center",
				"offsetTop": "sm"
			  },
			  {
				"type": "text",
				"text": "____year_a",
				"weight": "regular",
				"size": "sm",
				"color": "#1E3850",
				"align": "center",
				"margin": "none"
			  }
			],
			"backgroundColor": "____bgColor_a",
			"offsetBottom": "none",
				"action": {
				  "type": "message",
				  "label": "action",
				  "text": "____year_a"
				}
		  },
		  {
			"type": "box",
			"layout": "vertical",
			"contents": [
			  {
				"type": "text",
				"text": "____gz_b",
				"color": "#333334",
				"weight": "bold",
				"size": "sm",
				"align": "center",
				"offsetTop": "sm"
			  },
			  {
				"type": "text",
				"text": "____year_b",
				"weight": "regular",
				"size": "sm",
				"color": "#1E3850",
				"align": "center",
				"margin": "none"
			  }
			],
			"backgroundColor": "____bgColor_b",
			"offsetBottom": "none",
				"action": {
				  "type": "message",
				  "label": "action",
				  "text": "____year_b"
				}
		  },
		  {
			"type": "box",
			"layout": "vertical",
			"contents": [
			  {
				"type": "text",
				"text": "____gz_c",
				"color": "#333334",
				"weight": "bold",
				"size": "sm",
				"align": "center",
				"offsetTop": "sm"
			  },
			  {
				"type": "text",
				"text": "____year_c",
				"weight": "regular",
				"size": "sm",
				"color": "#1E3850",
				"align": "center",
				"margin": "none"
			  }
			],
			"backgroundColor": "____bgColor_c",
			"offsetBottom": "none",
				"action": {
				  "type": "message",
				  "label": "action",
				  "text": "____year_c"
				}
		  },
		  {
			"type": "box",
			"layout": "vertical",
			"contents": [
			  {
				"type": "text",
				"text": "____gz_d",
				"color": "#333334",
				"weight": "bold",
				"size": "sm",
				"align": "center",
				"offsetTop": "sm"
			  },
			  {
				"type": "text",
				"text": "____year_d",
				"weight": "regular",
				"size": "sm",
				"color": "#1E3850",
				"align": "center",
				"margin": "none"
			  }
			],
			"backgroundColor": "____bgColor_d",
			"offsetBottom": "none",
				"action": {
				  "type": "message",
				  "label": "action",
				  "text": "____year_d"
				}
		  },
		  {
			"type": "box",
			"layout": "vertical",
			"contents": [
			  {
				"type": "text",
				"text": "____gz_e",
				"color": "#333334",
				"weight": "bold",
				"size": "sm",
				"align": "center",
				"offsetTop": "sm"
			  },
			  {
				"type": "text",
				"text": "____year_e",
				"weight": "regular",
				"size": "sm",
				"color": "#1E3850",
				"align": "center",
				"margin": "none"
			  }
			],
			"backgroundColor": "____bgColor_e",
			"offsetBottom": "none",
				"action": {
				  "type": "message",
				  "label": "action",
				  "text": "____year_e"
				}
		  }
		],
		"margin": "xs",
		"spacing": "lg"
	  }
"""

year_sep = """
	  ,{
		"type": "separator",
		"color": "#888888"
	  }

"""


end_yearListFlex = """

	]
  },
  "styles": {
	"footer": {
	  "separator": true
	}
  }
}

"""




# yearFlexLayout = start_yearListFlex
# yearFlexLayout += item_yearListFlex
# yearFlexLayout += year_sep
# yearFlexLayout += ","
# yearFlexLayout += item_yearListFlex
# yearFlexLayout += end_yearListFlex

## 列出前後二十年的干支
def yearListFlexLayout( year , printMode = False ):
	"""
	依據 getGanziYear(year) 的結果,每輪取 5 筆產生 yearFlexLayout 字串。
	如果最後不足 5 筆就跳出(不處理最後不足的一批)。
	需要外部變數: start_yearListFlex, item_yearListFlex, ganZhi_Dict, getGanziYear()
	"""
	year = int( year )
	allYearList = getGanziYear( year = year, before = 27, after = 23 )

	idx = (year - 1984) % 60 + 1
	gan_zhi = ganZhi_Dict[idx]  # 完整干支,如 "甲子"
	zhi = gan_zhi[1]  # 地支(第二個字),如 "子"

	yearFlexLayout = start_yearListFlex

	# 計算最後一輪完整五筆的起始 index
	last_start_index = (len(allYearList) // 5 - 1) * 5

	for i in range(0, len(allYearList), 5):
		if i + 5 > len(allYearList):
			break  # 不足五筆就跳過

		# 🔥 關鍵: allYearList 的每個元素是 (干支, 年份) 的 tuple
		gz_a, year_a = allYearList[i]      # gz_a 是干支字串,如 "辛未"
		gz_b, year_b = allYearList[i + 1]
		gz_c, year_c = allYearList[i + 2]
		gz_d, year_d = allYearList[i + 3]
		gz_e, year_e = allYearList[i + 4]

		orgColor = "#ffffff"
		currentYearColor = "#9ae2c5"
		homeColor = "#ff979c"

		# 🔥 修正顏色判斷邏輯
		def get_color(gz_str, year_num):
			"""
			gz_str: 干支字串,如 "乙巳"
			year_num: 年份數字,如 2025
			"""
			# 1. 完全相同(天干地支 + 年份) → homeColor
			# print( year_num , year )
			# print( gz_str , gan_zhi )			
			# if gz_str == gan_zhi and year_num == year:
			if gz_str == gan_zhi and year_num == year:				
				# print("HOME")
				return homeColor
			# 2. 只有地支相同 → currentYearColor
			elif gz_str[1] == zhi:  # gz_str[1] 是地支
				return currentYearColor
			# 3. 其他 → orgColor
			else:
				return orgColor

		bgColor_a = get_color(gz_a, year_a)
		bgColor_b = get_color(gz_b, year_b)
		bgColor_c = get_color(gz_c, year_c)
		bgColor_d = get_color(gz_d, year_d)
		bgColor_e = get_color(gz_e, year_e)

		yearFlexLayout += (
			item_yearListFlex
				.replace("____gz_a", gz_a)
				.replace("____year_a", str(year_a))
				.replace("____gz_b", gz_b)
				.replace("____year_b", str(year_b))
				.replace("____gz_c", gz_c)
				.replace("____year_c", str(year_c))
				.replace("____gz_d", gz_d)
				.replace("____year_d", str(year_d))
				.replace("____gz_e", gz_e)
				.replace("____year_e", str(year_e))
				.replace("____bgColor_a", bgColor_a)
				.replace("____bgColor_b", bgColor_b)
				.replace("____bgColor_c", bgColor_c)
				.replace("____bgColor_d", bgColor_d)
				.replace("____bgColor_e", bgColor_e)
		)

		# 如果不是最後一輪就加分隔符
		if i != last_start_index:
			yearFlexLayout += year_sep
			yearFlexLayout += ","

	yearFlexLayout += end_yearListFlex

	if printMode == True:
		print( yearFlexLayout )

	finalLayout_dict = json.loads(yearFlexLayout)
	return finalLayout_dict








# 年干支查詢
## 從checkYear()得到年的資料，干支，生肖，前12年後12年，產生flex msg的UI
def getFlexMessage_GZ ( dataList , printMode = False ):
	# [1983, '癸亥', '豬', 1923, 1983, 2043]
	print( dataList )
	GZ = dataList[1]
	animalType = dataList[2]
	yearShow = "%s,%s,%s | %s"%( str(dataList[3]),str(dataList[4]),str(dataList[5]),animalType )
	currentYear = dataList[0]


	fm_command = """
	{
	  "type": "bubble",
	  "body": {
		"type": "box",
		"layout": "vertical",
		"contents": [
		  {
			"type": "text",
			"text": "年干支",
			"weight": "bold",
			"color": "#6A8B91",
			"size": "lg"
		  },




		{
		"type": "box",
		"layout": "horizontal",
		"contents": [
		  {
			"type": "text",
			"text": "____GZ",
			"weight": "bold",
			"size": "xxl",
			"margin": "none",
			"flex": 5
		  },
		  {
			"type": "box",
			"layout": "vertical",
			"contents": [
			  {
				"type": "text",
				"text": "____yearA",
				"size": "lg",
				"color": "#888888",
				"wrap": true,
				"weight": "bold",
				"margin": "sm",
				"flex": 2,
				"gravity": "bottom",
				"align": "end"
			  }
			],
			"flex": 0
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
				"type": "text",
				"text": "____yearB",
				"size": "lg",
				"color": "#2769C0",
				"wrap": true,
				"weight": "bold",
				"margin": "sm",
				"flex": 2,
				"gravity": "bottom",
				"align": "end"
			  }
			],
			"flex": 0
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
				"type": "text",
				"text": "____yearC",
				"size": "lg",
				"color": "#888888",
				"wrap": true,
				"weight": "bold",
				"margin": "sm",
				"flex": 2,
				"gravity": "bottom",
				"align": "end"
			  }
			],



				"flex": 0
			  }
			]
		  },
		  {
			"type": "separator",
			"margin": "md"
		  },






		  {
			"type": "box",
			"layout": "horizontal",
			"margin": "md",
			"contents": [
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [
				  {
					"type": "text",
					"text": "◀",
					"size": "lg",
					"color": "#000000",
					"flex": 0,
					"action": {
					  "type": "message",
					  "label": "action",
					  "text": "____pre"
					},
					"weight": "bold"
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
					"text": "◁",
					"size": "lg",
					"color": "#000000",
					"weight": "bold",
					"action": {
					  "type": "message",
					  "label": "action",
					  "text": "____preOne"
					},
					"align": "end"
				  }
				],
				"width": "30px"
			  },
			  {
				"type": "box",
				"layout": "horizontal",
				"contents": [
				  {
					"type": "box",
					"layout": "vertical",
					"contents": [],
					"width": "35px",
					"flex": 0
				  },
				  {
					"type": "box",
					"layout": "baseline",
					"contents": [
					  {
						"type": "text",
						"text": "LIST",
						"align": "center",
						"size": "lg",
						"weight": "bold",
						"color": "#174779",
						"action": {
						  "type": "message",
						  "label": "action",
						  "text": "____yearlist"
						}
					  }
					],
					"width": "84px",
					"flex": 2,
					"cornerRadius": "15px",
					"borderWidth": "2px",
					"borderColor": "#cccccc"
				  },
				  {
					"type": "box",
					"layout": "vertical",
					"contents": [],
					"width": "35px",
					"flex": 0
				  }
				]
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [
				  {
					"type": "text",
					"text": "▷",
					"size": "lg",
					"color": "#000000",
					"flex": 0,
					"action": {
					  "type": "message",
					  "label": "action",
					  "text": "____postOne"
					},
					"weight": "bold"
				  }
				],
				"width": "30px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [
				  {
					"type": "text",
					"text": "▶",
					"size": "lg",
					"color": "#000000",
					"weight": "bold",
					"action": {
					  "type": "message",
					  "label": "action",
					  "text": "____post"
					},
					"align": "end"
				  }
				],
				"width": "20px"
			  }
			],
			"offsetTop": "xs"
		  }
		]
	  },








	  "styles": {
		"footer": {
		  "separator": true
		}
	  }
	}"""


	# [1983, '癸亥', '豬', 1923, 1983, 2043]
	# print( dataList )
	GZ = dataList[1]
	animalType = dataList[2]
	yearShow = "%s,%s,%s | %s"%( str(dataList[3]),str(dataList[4]),str(dataList[5]),animalType )
	yearA = str(dataList[3])
	yearB = str(dataList[4])
	yearC = "%s | %s"% ( str(dataList[5]),animalType )
	currentYear = dataList[0]

	final_flexLayout =  ( fm_command .replace( "____GZ", GZ )
									.replace( "____yearA", yearA )
									.replace( "____yearB", yearB )
									.replace( "____yearC", yearC )

									.replace( "____preOne" , str( currentYear - 1 ) ) 
									.replace( "____postOne" , str( currentYear + 1 ) )
									.replace( "____pre" , str( currentYear - 12 ) ) 
									.replace( "____post" , str( currentYear + 12 ))
									.replace( "____yearlist" , "--"+ str( currentYear ))
						)
	if printMode == True:
		print( final_flexLayout )

	finalLayout_dict = json.loads( final_flexLayout )
	return finalLayout_dict





drawUiLayoutFront ='''
{
  "type": "bubble",
  "size": "mega",
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
			"layout": "vertical",
			"contents": [
			  {
				"type": "text",
				"text": "__占__",
				"weight": "regular",
				"size": "xl",
				"wrap": true,
				"action": {
				  "type": "postback",
				  "label": "action",
				  "data": "__NOTE__",
				  "displayText": "__NOTE_DSP__"
				}
			  }
			],
			"width": "200px"
		  },
		  {
			"type": "text",
			"text": "reload",
			"weight": "bold",
			"size": "lg",
			"align": "end",
			"gravity": "bottom",
			"action": {
			  "type": "message",
			  "label": "action",
			  "text": "__占__"
			},
			"color": "#8CC63F"
		  }
		]
	  },
	  {
		"type": "separator",
		"color": "#888888",
		"margin": "none"
	  },

'''








eachRawDrawFlex ='''
	  {
		"type": "box",
		"layout": "horizontal",
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
					"type": "text",
					"text": "__NUM1__",
					"size": "sm",
					"weight": "bold",
					"margin": "none",
					"align": "center",
					"color": "#ffffff",
					"gravity": "top"
				  }
				],
				"width": "18px",
				"height": "19px",
				"backgroundColor": "#606b7c",
				"offsetTop": "xs",
				"action": {
				  "type": "postback",
				  "label": "action",
				  "data": "__SIX1__"
				  
				}
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [],
				"width": "4px",
				"height": "50px"
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
						"type": "text",
						"text": "__UP1__",
						"size": "md",
						"align": "end",
						"weight": "regular",
						"color": "#1E3850"
					  }
					],
					"height": "19px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "__MID1__",
						"size": "md",
						"align": "end",
						"weight": "regular",
						"color": "#1E3850"
					  }
					],
					"height": "19px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "__DN1__",
						"size": "md",
						"align": "end",
						"weight": "regular",
						"color": "#1E3850"
					  }
					],
					"height": "19px"
				  }
				]
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [],
				"width": "5px",
				"backgroundColor": "#eeeeea"
			  }
			],
			"width": "62px",
			"height": "60px",

			"action": {
			  "type": "message",
			  "label": "action",
			  "text": "__DRAW1__"
			},
			"backgroundColor": "#eeeeea"
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
					"text": "__NUM2__",
					"size": "sm",
					"weight": "bold",
					"margin": "none",
					"align": "center",
					"color": "#ffffff",
					"gravity": "top"
				  }
				],
				"width": "18px",
				"height": "19px",
				"backgroundColor": "#606b7c",
				"offsetTop": "xs",
				"action": {
				  "type": "postback",
				  "label": "action",
				  "data": "__SIX2__"
				  
				}
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [],
				"width": "4px",
				"height": "50px"
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
						"type": "text",
						"text": "__UP2__",
						"size": "md",
						"align": "end",
						"weight": "regular",
						"color": "#1E3850"
					  }
					],
					"height": "19px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "__MID2__",
						"size": "md",
						"align": "end",
						"weight": "regular",
						"color": "#1E3850"
					  }
					],
					"height": "19px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "__DN2__",
						"size": "md",
						"align": "end",
						"weight": "regular",
						"color": "#1E3850"
					  }
					],
					"height": "19px"
				  }
				]
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [],
				"width": "5px",
				"backgroundColor": "#eeeeeb"
			  }
			],
			"width": "62px",
			"height": "60px",
			"action": {
			  "type": "message",
			  "label": "action",
			  "text": "__DRAW2__"
			},
			"backgroundColor": "#eeeeeb"
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
					"text": "__NUM3__",
					"size": "sm",
					"weight": "bold",
					"margin": "none",
					"align": "center",
					"color": "#ffffff",
					"gravity": "top"
				  }
				],
				"width": "18px",
				"height": "19px",
				"backgroundColor": "#606b7c",
				"offsetTop": "xs",
				"action": {
				  "type": "postback",
				  "label": "action",
				  "data": "__SIX3__"
				  
				}
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [],
				"width": "4px",
				"height": "50px"
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
						"type": "text",
						"text": "__UP3__",
						"size": "md",
						"align": "end",
						"weight": "regular",
						"color": "#1E3850"
					  }
					],
					"height": "19px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "__MID3__",
						"size": "md",
						"align": "end",
						"weight": "regular",
						"color": "#1E3850"
					  }
					],
					"height": "19px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "__DN3__",
						"size": "md",
						"align": "end",
						"weight": "regular",
						"color": "#1E3850"
					  }
					],
					"height": "19px"
				  }
				]
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [],
				"width": "5px",
				"backgroundColor": "#eeeeec"
			  }
			],
			"width": "62px",
			"height": "60px",
			"action": {
			  "type": "message",
			  "label": "action",
			  "text": "__DRAW3__"
			},
			"backgroundColor": "#eeeeec"
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
					"text": "__NUM4__",
					"size": "sm",
					"weight": "bold",
					"margin": "none",
					"align": "center",
					"color": "#ffffff",
					"gravity": "top"
				  }
				],
				"width": "18px",
				"height": "19px",
				"backgroundColor": "#606b7c",
				"offsetTop": "xs",
				"action": {
				  "type": "postback",
				  "label": "action",
				  "data": "__SIX4__"
				  
				}
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [],
				"width": "4px",
				"height": "50px"
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
						"type": "text",
						"text": "__UP4__",
						"size": "md",
						"align": "end",
						"weight": "regular",
						"color": "#1E3850"
					  }
					],
					"height": "19px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "__MID4__",
						"size": "md",
						"align": "end",
						"weight": "regular",
						"color": "#1E3850"
					  }
					],
					"height": "19px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "__DN4__",
						"size": "md",
						"align": "end",
						"weight": "regular",
						"color": "#1E3850"
					  }
					],
					"height": "19px"
				  }
				]
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [],
				"width": "5px",
				"backgroundColor": "#eeeeed"
			  }
			],
			"width": "62px",
			"height": "60px",
			"action": {
			  "type": "message",
			  "label": "action",
			  "text": "__DRAW4__"
			},
			"backgroundColor": "#eeeeed"
		  }







		],
		"margin": "sm",
		"spacing": "4px"

	  }'''

sep ='''
	  {
		"type": "separator",
		"color": "#888888",
		"margin": "sm"
	  }'''


drawUiLayoutBack ='''
	]
  },
  "size": "mega",
  "styles": {
	"footer": {
	  "separator": true
	}
  }
}'''


# import random

# def getRandomNum( ):
# 	result = []
# 	for _ in range(3):

# 		r = random.random()  # 0~1
# 		if r < 0.7:
# 			# 70% 機率落在 100 ~ 300
# 			num =  random.randint(10, 100)
# 		elif r > 0.8:
# 			# 15% 機率落在 100 ~ 300
# 			num =  random.randint(100, 200)
# 		else:
# 			# 15% 機率落在 700 ~ 1000
# 			num =  random.randint(300, 900)
# 		result.append(str(num))
# 	# print ( result )
# 	return result
import secrets

def getRandomNum():
	result = []
	for _ in range(3):

		r = secrets.randbelow(10_000_000) / 10_000_000  # 0~1 高亂度浮點

		if r < 0.7:
			# 70% 機率：10 ~ 100
			minv, maxv = 30, 150
			num = secrets.randbelow(maxv - minv + 1) + minv

		elif r > 0.8:
			# 20% 機率：100 ~ 200
			minv, maxv = 100, 300
			num = secrets.randbelow(maxv - minv + 1) + minv

		else:
			# 10% 機率：300 ~ 900
			minv, maxv = 300, 600
			num = secrets.randbelow(maxv - minv + 1) + minv

		result.append(str(num))

	return result


pool = ["#eeeeee" ,"#CCD4D6" ,"#ededed" ,"#E7E6E5" ,"#dddddd","#E7E6E1","#EBE1D8","#C4BFBB","#EBECE7","#eeeeee" ,"#CCD4D6" ,"#ededed" ,"#E7E6E5" ,"#dddddd","#E7E6E1","#EBE1D8","#B8B4C1","#EBECE7", "#B4BFB9","#9bad7d"]
queue = []

## 產生16格抽籤模式UI
def getDrawRiceGua( note = "" , printMode = False ):
	import random
	draw_FinalLayout = ""
	draw_FinalLayout = drawUiLayoutFront.replace( "__占__" , note ).replace( "__NOTE__", "s+" + note )
	# draw_FinalLayout = draw_FinalLayout.replace( "__NOTE_DSP__", "\udbc0\udc9c" )



	def get_one():
		global queue
		if not queue:
			queue = pool[:]          # 複製
			random.shuffle(queue)    # 打亂順序
		return queue.pop()           # 每拿一個就少一個



	for i in range(4):
		randList1 = getRandomNum()
		randList2 = getRandomNum()
		randList3 = getRandomNum()
		randList4 = getRandomNum()

		color1 = get_one()
		color2 = get_one()
		color3 = get_one()
		color4 = get_one()
		print(color1,color2,color3,color4)

		











		eachRawDrawFlex_Buf = eachRawDrawFlex.replace( "__UP1__" , randList1[0] ).replace( "__MID1__" , randList1[1] ).replace( "__DN1__" , randList1[2] ).replace( "__NUM1__", str(i*4+1)).replace( "__DRAW1__" , ",".join(randList1) + " // " + note ).replace( "#eeeeea" , color1).replace( "__SIX1__" , "s+" + ",".join(randList1)+ " // " + note ).replace( "__SIX_DSP1__" , "\udbc0\udc9c" )
		eachRawDrawFlex_Buf = eachRawDrawFlex_Buf.replace( "__UP2__" , randList2[0] ).replace( "__MID2__" , randList2[1] ).replace( "__DN2__" , randList2[2] ).replace( "__NUM2__", str(i*4+2)).replace( "__DRAW2__" , ",".join(randList2) + " // " + note ).replace( "#eeeeeb" , color2).replace( "__SIX2__" , "s+" + ",".join(randList2)+ " // " + note ).replace( "__SIX_DSP2__" , "\udbc0\udc9c" ) 
		eachRawDrawFlex_Buf = eachRawDrawFlex_Buf.replace( "__UP3__" , randList3[0] ).replace( "__MID3__" , randList3[1] ).replace( "__DN3__" , randList3[2] ).replace( "__NUM3__", str(i*4+3)).replace( "__DRAW3__" , ",".join(randList3) + " // " + note ).replace( "#eeeeec" , color3).replace( "__SIX3__" , "s+" + ",".join(randList3)+ " // " + note ).replace( "__SIX_DSP3__" , "\udbc0\udc9c" ) 
		eachRawDrawFlex_Buf = eachRawDrawFlex_Buf.replace( "__UP4__" , randList4[0] ).replace( "__MID4__" , randList4[1] ).replace( "__DN4__" , randList4[2] ).replace( "__NUM4__", str(i*4+4)).replace( "__DRAW4__" , ",".join(randList4) + " // " + note ).replace( "#eeeeed" , color4).replace( "__SIX4__" , "s+" + ",".join(randList4)+ " // " + note ).replace( "__SIX_DSP4__" , "\udbc0\udc9c" ) 
		
		if i != 3:
			draw_FinalLayout += eachRawDrawFlex_Buf
			draw_FinalLayout += ","		
			draw_FinalLayout += sep
			draw_FinalLayout += ","
		else:
			draw_FinalLayout += eachRawDrawFlex_Buf
			draw_FinalLayout += drawUiLayoutBack
		
	# print(draw_FinalLayout)
	if printMode == True:
		print( draw_FinalLayout )

	draw_FinalLayout_dict = json.loads( draw_FinalLayout )
	return draw_FinalLayout_dict



how_to_use = """
{
  "type": "bubble",
  "size": "giga",
  "body": {
	"type": "box",
	"layout": "vertical",
	"contents": [
	  {
		"type": "text",
		"text": "裝卦初號機 V1.0",
		"weight": "regular",
		"color": "#295F87",
		"size": "md"
	  },
	  {
		"type": "text",
		"text": "使用說明",
		"weight": "bold",
		"size": "xl",
		"margin": "none",
		"offsetStart": "-1px"
	  },
	  {
		"type": "text",
		"text": "礙於LINE的使用介面沒有表單模式，只能用文字指令替代",
		"size": "sm",
		"wrap": true,
		"margin": "sm"
	  },
	  {
		"type": "separator",
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
				"layout": "horizontal",
				"contents": [
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "1,搖卦",
						"size": "md",
						"weight": "bold",
						"align": "start"
					  }
					],
					"width": "50px"
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
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "2,輸入指令",
						"size": "md",
						"weight": "bold",
						"align": "start"
					  }
					],
					"width": "80px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "輸入符號請參考以下原則",
						"size": "sm",
						"gravity": "bottom",
						"color": "#333333"
					  }
					],
					"margin": "sm"
				  }
				],
				"margin": "md"
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
						"contents": [
						  {
							"type": "box",
							"layout": "horizontal",
							"contents": [
							  {
								"type": "box",
								"layout": "vertical",
								"contents": [],
								"width": "7px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "老陽",
									"size": "md",
									"weight": "regular",
									"align": "start"
								  }
								],
								"width": "80px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "〇",
									"size": "md",
									"weight": "bold",
									"align": "start"
								  }
								],
								"width": "83px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "$",
									"size": "md",
									"weight": "bold",
									"align": "start"
								  }
								],
								"width": "85px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "9",
									"size": "md",
									"weight": "bold",
									"align": "start"
								  }
								],
								"width": "70px"
							  }
							],
							"margin": "md",
							"backgroundColor": "#eeeeee",
							"width": "320px"
						  },
						  {
							"type": "box",
							"layout": "horizontal",
							"contents": [
							  {
								"type": "box",
								"layout": "vertical",
								"contents": [],
								"width": "7px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "少陰",
									"size": "md",
									"weight": "regular",
									"align": "start"
								  }
								],
								"width": "80px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "⚋",
									"size": "md",
									"weight": "bold",
									"align": "start"
								  }
								],
								"width": "83px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "0",
									"size": "md",
									"weight": "bold",
									"align": "start"
								  }
								],
								"width": "85px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "8",
									"size": "md",
									"weight": "bold",
									"align": "start"
								  }
								],
								"width": "70px"
							  }
							],
							"margin": "md",
							"backgroundColor": "#eeeeee",
							"width": "320px"
						  },
						  {
							"type": "box",
							"layout": "horizontal",
							"contents": [
							  {
								"type": "box",
								"layout": "vertical",
								"contents": [],
								"width": "7px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "少陽",
									"size": "md",
									"weight": "regular",
									"align": "start"
								  }
								],
								"width": "78px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": " ⚊",
									"size": "md",
									"weight": "bold",
									"align": "start"
								  }
								],
								"width": "85px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "1",
									"size": "md",
									"weight": "bold",
									"align": "start"
								  }
								],
								"width": "85px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "7",
									"size": "md",
									"weight": "bold",
									"align": "start"
								  }
								],
								"width": "70px"
							  }
							],
							"margin": "md",
							"backgroundColor": "#eeeeee",
							"width": "320px"
						  },
						  {
							"type": "box",
							"layout": "horizontal",
							"contents": [
							  {
								"type": "box",
								"layout": "vertical",
								"contents": [],
								"width": "7px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "老陰",
									"size": "md",
									"weight": "regular",
									"align": "start"
								  }
								],
								"width": "80px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "✕",
									"size": "md",
									"weight": "bold",
									"align": "start"
								  }
								],
								"width": "84px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "X",
									"size": "md",
									"weight": "bold",
									"align": "start"
								  }
								],
								"width": "85px"
							  },
							  {
								"type": "box",
								"layout": "horizontal",
								"contents": [
								  {
									"type": "text",
									"text": "6",
									"size": "md",
									"weight": "bold",
									"align": "start"
								  }
								],
								"width": "70px"
							  }
							],
							"margin": "md",
							"backgroundColor": "#eeeeee",
							"width": "320px"
						  }
						]
					  }
					]
				  }
				]
			  }
			],
			"margin": "xs"
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
						"text": "其他使用範例:",
						"size": "md",
						"weight": "bold",
						"align": "start"
					  }
					],
					"width": "110px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "問題 // 卦",
						"size": "sm",
						"gravity": "bottom",
						"color": "#333333"
					  }
					],
					"margin": "sm"
				  }
				],
				"margin": "lg"
			  },
			  {
				"type": "box",
				"layout": "horizontal",
				"contents": [
				  {
					"type": "text",
					"text": "基本模式:",
					"size": "sm",
					"gravity": "bottom",
					"color": "#295F87",
					"weight": "bold"
				  }
				],
				"margin": "xs"
			  },
			  {
				"type": "separator"
			  },
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
						"text": "陳男占財運吉凶",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "115px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "15px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "X0X1$0",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "115px"
				  }
				],
				"margin": "xs"
			  },
			  {
				"type": "separator",
				"margin": "xs"
			  },
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
						"text": "陳男占財運吉凶",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "115px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "16px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "686798",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "115px"
				  }
				],
				"margin": "xs"
			  },
			  {
				"type": "separator",
				"margin": "xs"
			  },
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
						"text": "陳男占財運吉凶",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "115px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "15px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "000110,1,3,5",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "115px"
				  }
				],
				"margin": "xs"
			  },
			  {
				"type": "box",
				"layout": "horizontal",
				"contents": [
				  {
					"type": "text",
					"text": "64卦卦名模式:",
					"size": "sm",
					"gravity": "bottom",
					"color": "#295F87",
					"weight": "bold"
				  }
				],
				"margin": "lg"
			  },
			  {
				"type": "separator",
				"margin": "xs"
			  },
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
						"text": "陳男占財運吉凶",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "115px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "15px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "萃之豐卦",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "115px"
				  }
				],
				"margin": "xs"
			  },
			  {
				"type": "separator",
				"margin": "xs"
			  },
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
						"text": "陳男占財運吉凶",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "115px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "15px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "澤地之雷火",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "115px"
				  }
				],
				"margin": "xs"
			  },
			  {
				"type": "separator",
				"margin": "xs"
			  },
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
						"text": "陳男占財運吉凶",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "115px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "15px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "雷天大壯",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "115px"
				  }
				],
				"margin": "xs"
			  },
			  {
				"type": "box",
				"layout": "horizontal",
				"contents": [
				  {
					"type": "text",
					"text": "米卦模式:",
					"size": "sm",
					"gravity": "bottom",
					"color": "#295F87",
					"weight": "bold"
				  }
				],
				"margin": "lg"
			  },
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
						"text": "陳男占財運吉凶",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "115px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "15px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "27,85,123",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "115px"
				  }
				],
				"margin": "none"
			  }
			],
			"margin": "md"
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
						"text": "自訂時間:",
						"size": "md",
						"weight": "bold",
						"align": "start"
					  }
					],
					"width": "80px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "問題 // 卦 // 時間",
						"size": "sm",
						"gravity": "bottom",
						"color": "#333333"
					  }
					],
					"margin": "sm"
				  }
				],
				"margin": "lg"
			  },
			  {
				"type": "separator",
				"margin": "xs"
			  },
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
						"text": "占明日天氣",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "82px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "14px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "X0X1$0",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "60px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "14px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "2025-11-5-9-30",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "200px"
				  }
				],
				"margin": "xs"
			  },
			  {
				"type": "separator"
			  },
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
						"text": "占明日天氣",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "82px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "14px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "X0X1$0",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "60px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "14px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "2025-11-5",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "200px"
				  }
				],
				"margin": "xs"
			  },
			  {
				"type": "separator",
				"margin": "xs"
			  },
			  {
				"type": "box",
				"layout": "horizontal",
				"contents": [
				  {
					"type": "text",
					"text": "四柱模式:",
					"size": "sm",
					"gravity": "bottom",
					"color": "#295F87",
					"weight": "regular"
				  }
				],
				"margin": "lg"
			  },
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
						"text": "占今年財運",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "82px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "14px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "X0X1$0",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "57px",
					"margin": "xs"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "14px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "乙巳,丙戌,戊寅,癸丑",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "160px"
				  }
				],
				"margin": "xs"
			  },
			  {
				"type": "separator",
				"margin": "xs"
			  },
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
						"text": "占今年財運",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "82px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "14px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "X0X1$0",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "57px",
					"margin": "xs"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "14px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "乙巳,丙戌,戊寅",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "160px"
				  }
				],
				"margin": "xs"
			  },
			  {
				"type": "separator",
				"margin": "xs"
			  },
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
						"text": "占天氣",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "48px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "14px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "X0X1$0",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "57px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "14px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "乙巳年戌月戊寅日",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "130px"
				  }
				],
				"margin": "xs"
			  },
			  {
				"type": "separator",
				"margin": "xs"
			  },
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
						"text": "占天氣",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "48px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "14px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "X0X1$0",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "57px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "//",
						"size": "md",
						"gravity": "bottom",
						"color": "#888888",
						"weight": "bold"
					  }
					],
					"margin": "sm",
					"width": "14px"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "戌月戊寅日",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"width": "130px"
				  }
				],
				"margin": "xs"
			  }
			]
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
					"layout": "horizontal",
					"contents": [
					  {
						"type": "box",
						"layout": "horizontal",
						"contents": [
						  {
							"type": "text",
							"text": "其他:",
							"size": "md",
							"weight": "bold",
							"align": "start"
						  }
						],
						"width": "40px"
					  },
					  {
						"type": "box",
						"layout": "horizontal",
						"contents": [
						  {
							"type": "text",
							"text": "(待補)",
							"size": "md",
							"weight": "bold",
							"align": "start",
							"color": "#999999"
						  }
						],
						"width": "100px"
					  }
					],
					"margin": "none"
				  },
				  {
					"type": "separator",
					"margin": "xxl"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "建議或勘誤..",
						"size": "md",
						"weight": "regular",
						"align": "start"
					  }
					],
					"margin": "md"
				  },
				  {
					"type": "box",
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "benno.wu@gmail.com",
						"size": "md",
						"weight": "regular",
						"align": "start",
						"action": {
						  "type": "postback",
						  "label": "action",
						  "data": "sendMe",
						  "displayText": "benno.wu@gmail.com"
						}
					  }
					]
				  }
				],
				"margin": "none"
			  }
			],
			"margin": "lg"
		  }
		]
	  }
	]
  },
  "styles": {
	"footer": {
	  "separator": true
	}
  }
}"""

def howToUse( printMode = False ):
	how_json = how_to_use

		
	# print(how_json)
	if printMode == True:
		print( how_json )

	how_dict = json.loads( how_json )
	return how_dict



## 小六壬
# small_six_zan_test
# (['速喜', '留連', '赤口'], '官事凶 | 口舌是非,主事不利,辦事宜緩', '赤口主口舌 官非切要防 失物速速討 行人有驚慌 六畜多作怪 病者出西方 更須防詛咒 誠恐染瘟肓')

sSixZanUiLayout = """
{
  "type": "bubble",
  "size": "deca",
  "body": {
	"type": "box",
	"layout": "vertical",
	"contents": [
	  {
		"type": "box",
		"layout": "vertical",
		"contents": [
		  {
			"type": "image",
			"url": "__URL__",
			"size": "full",
			"aspectRatio": "10:5.5"
		  }
		],
		"height": "104px"
	  },
	  {
		"type": "text",
		"text": "__SUB__",
		"size": "sm",
		"weight": "bold",
		"color": "#888888",
		"margin": "sm",
		"offsetBottom": "xs"
	  },
	  {
		"type": "separator",
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
				"type": "text",
				"text": "__占__",
				"weight": "regular",
				"size": "lg",
				"wrap": true
			  }
			],
			"margin": "sm"
		  }
		]
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
				"type": "text",
				"text": "__NUMBER__",
				"size": "md",
				"weight": "regular",
				"color": "#6D839B"
			  }
			],
			"height": "20px",
			"margin": "none"
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
					"text": "__STEP1__",
					"size": "lg",
					"weight": "bold",
					"margin": "sm",
					"flex": 0,
					"color": "#666666"
				  }
				],
				"width": "40px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [
				  {
					"type": "text",
					"text": "-",
					"size": "lg",
					"weight": "bold",
					"margin": "sm",
					"flex": 0,
					"color": "#888888"
				  }
				],
				"width": "9px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [
				  {
					"type": "text",
					"text": "__STEP2__",
					"size": "lg",
					"weight": "bold",
					"margin": "sm",
					"flex": 0,
					"color": "#666666"
				  }
				],
				"width": "40px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [
				  {
					"type": "text",
					"text": "-",
					"size": "lg",
					"weight": "bold",
					"margin": "sm",
					"flex": 0,
					"color": "#888888"
				  }
				],
				"width": "9px"
			  },
			  {
				"type": "box",
				"layout": "vertical",
				"contents": [
				  {
					"type": "text",
					"text": "__STEP3__",
					"size": "lg",
					"weight": "bold",
					"margin": "sm",
					"flex": 0,
					"color": "#444444",
					"action": {
					  "type": "message",
					  "label": "action",
					  "text": "Hi~"
					}
				  }
				],
				"width": "40px"
			  }
			],
			"offsetBottom": "md",
			"margin": "xs"
		  }
		],
		"offsetBottom": "sm"
	  }
	],
	"height": "220px",
	"backgroundColor": "#eeeeee"
  },
  "styles": {
	"footer": {
	  "separator": true
	}
  }
}
"""

url_dict = {
"大安" : "https://res.cloudinary.com/ds9jcwwcw/image/upload/v1765216454/__icon/9f1845a5ec6b478c9cc9b81bdcb9653e.png",
"留連" : "https://res.cloudinary.com/ds9jcwwcw/image/upload/v1765216455/__icon/e76ceed944c24a3ca2278a8eaa7c6454.png",
"速喜" : "https://res.cloudinary.com/ds9jcwwcw/image/upload/v1765216455/__icon/690b743b0c1b4d738ac086d568c1b26a.png",
"赤口" : "https://res.cloudinary.com/ds9jcwwcw/image/upload/v1765216456/__icon/4f897c1d223b4d5a84df2d6cd7f54baf.png",
"小吉" : "https://res.cloudinary.com/ds9jcwwcw/image/upload/v1765216457/__icon/05f41ac5befb4086b3b67f4666a7b499.png",
"空亡" : "https://res.cloudinary.com/ds9jcwwcw/image/upload/v1765216457/__icon/54037963d532475da28a01e464297a48.png",
}

def sSixZnUi( impNumList = [] , title = "- - -", printMode = False ):

	luckBufAll = sSixZmain( impNumList[0], impNumList[1], impNumList[2]  )

	subTitle = luckBufAll[1].split("|")[1].replace( " " , "" ).replace(","," , ")
	luckBuf = luckBufAll[0]

	print( luckBufAll )
	# (['赤口', '速喜', '小吉'], '人來喜 | 喜事到來,辦事吉利,成功在望', '小吉最吉昌 路上好商量 陰人來報喜 失物在坤方 行人即便至 交關甚是強 凡事街合和 病者叩穹蒼', '2025/12/07/16/04')
	fullDate = luckBufAll[-1]
	url = url_dict[luckBuf[-1]]

	numText = ""
	if fullDate == "":
		numText = ' | '.join(str(x) for x in impNumList) ## [3,2,1]  -> 3-2-1  ,, [3,2]  -> 3-2
	else:
		numText = fullDate

	titleA = luckBuf[0] if len(luckBuf) > 0 else None
	titleB = luckBuf[1] if len(luckBuf) > 1 else None
	titleC = luckBuf[2] if len(luckBuf) > 2 else None

	numA = impNumList[0] if len(impNumList) > 0 else None
	numB = impNumList[1] if len(impNumList) > 1 else None
	numC = impNumList[2] if len(impNumList) > 2 else None

	sZnLayout = sSixZanUiLayout

	sZnLayout = ( sZnLayout .replace( "__NUMBER__", numText )
							.replace( "__STEP1__", titleA )
							.replace( "__STEP2__", titleB )
							.replace( "__STEP3__", titleC )
							.replace( "__占__", title )
							.replace( "__SUB__", subTitle )							
							.replace( "__URL__", url )						

				)
		
	# print(sZnLayout)
	if printMode == True:
		print( sZnLayout )

	sZnLayoutJson = json.loads( sZnLayout )
	return sZnLayoutJson






if __name__ == '__main__':
	ganZiList_fun( currentTime = "" , dayMode = "h" , index = "" , runtime = 10 , printMode = False )
	ganZiList_fun( currentTime = "2025/12/15/19:00" , dayMode = "h" , index = "" , runtime = 10 , printMode = False )
	# ganZiList_fun( currentTime = "" , dayMode = "jc" , index = "" , runtime = 10 , printMode = False )
	# ganZiList_fun( currentTime = "2026/05/05" , dayMode = "jc" , index = "" , runtime = 10 , printMode = False )		
	# ganZiList_fun( currentTime = "" , dayMode = "d" , index = "" , runtime = 20 , printMode = True )
	# ganZiList_fun( currentTime = "2025/12/11/18/56" , dayMode = "h" , index = "" , runtime = 8 , printMode = True )
	# ganZiList_fun( currentTime = "2025/05/08" , dayMode = "jc" , index = "" , runtime = 20 ) 



# 干支/日/10/2025-08-31-15-48
# 干支/日/10
# 干支/日/2025-08-31-15-48
# 干支/日/10/戌
# 干支/日/2025-08-31-15-48/戌


# # "干支/時/10/2025-08-31-15-48"
# 	# "d" -- day
# 	# "m" -- month
# 	# "h" -- hour
# 	# "節氣"

# 	# 干支/日/2025.5.11/10/申
# # ['乙巳-乙酉-己卯', '2025/09/07', '白露']

	# getDrawRiceGua("占明天天氣" , printMode = True )

	# sSixZnUi( [208,69,42] , "XX展的文件",  printMode = True)

	# yearListFlexLayout( "2025",True ) 

	# getFlexMessage_GZ ( checkYear ( yearData = "2025" ) )

	# howToUse( printMode = True )

# getDrawRiceGua( note = "" , printMode = False )


# {
#   "type": "bubble",
#   "size": "hecto",
#   "body": {
#     "type": "box",
#     "layout": "vertical",
#     "contents": [
#       {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#           {
#             "type": "image",
#             "url": "https://res.cloudinary.com/ds9jcwwcw/image/upload/v1765014022/sLiuZen-icon-38_krdu4l.png",
#             "size": "full",
#             "aspectRatio": "10:5.6"
#           }
#         ],
#         "height": "120px"
#       },
#       {
#         "type": "separator",
#         "margin": "sm"
#       },
#       {
#         "type": "box",
#         "layout": "horizontal",
#         "contents": [
#           {
#             "type": "text",
#             "text": "3,15,9",
#             "size": "xl",
#             "flex": 1
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "速喜",
#                     "size": "lg",
#                     "weight": "bold",
#                     "margin": "sm",
#                     "flex": 0,
#                     "color": "#666666"
#                   }
#                 ],
#                 "width": "40px"
#               },
#               {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "-",
#                     "size": "lg",
#                     "weight": "bold",
#                     "margin": "sm",
#                     "flex": 0,
#                     "color": "#888888"
#                   }
#                 ],
#                 "width": "8px"
#               },
#               {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "小吉",
#                     "size": "lg",
#                     "weight": "bold",
#                     "margin": "sm",
#                     "flex": 0,
#                     "color": "#666666"
#                   }
#                 ],
#                 "width": "40px"
#               },
#               {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "-",
#                     "size": "lg",
#                     "weight": "bold",
#                     "margin": "sm",
#                     "flex": 0,
#                     "color": "#888888"
#                   }
#                 ],
#                 "width": "8px"
#               },
#               {
#                 "type": "box",
#                 "layout": "vertical",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "大安",
#                     "size": "lg",
#                     "weight": "bold",
#                     "margin": "sm",
#                     "flex": 0,
#                     "color": "#666666"
#                   }
#                 ],
#                 "width": "40px"
#               }
#             ],
#             "margin": "none",
#             "flex": 2
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "身不動|失物行人,靜止不動,平安",
#                 "size": "sm",
#                 "weight": "regular",
#                 "margin": "sm",
#                 "flex": 0,
#                 "color": "#666666",
#                 "wrap": true
#               }
#             ]
#           }
#         ],
#         "margin": "none"
#       }
#     ]
#   },
#   "styles": {
#     "footer": {
#       "separator": true
#     }
#   }
# }

# https://res.cloudinary.com/ds9jcwwcw/image/upload/v1765014022/sLiuZen-icon-38_krdu4l.png