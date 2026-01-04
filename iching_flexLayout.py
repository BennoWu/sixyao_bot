
from iching_open_ai_tool import *


## 易經卦

ichingGuaLayoutHome = """
{
  "type": "bubble",
  "body": {
	"type": "box",
	"layout": "vertical",
	"contents": [
	  {
		"type": "text",
		"text": "易經解卦",
		"weight": "bold",
		"color": "#57988F",
		"size": "sm"
	  },
	  {
		"type": "text",
		"text": "__GUAMATCH__",
		"weight": "bold",
		"size": "xl",
		"margin": "xs"
	  },
	  {
		"type": "text",
		"text": "__MAINSUB__",
		"size": "xs",
		"color": "#365E8E",
		"wrap": true,
		"weight": "bold",
		"margin": "xs"

	  },
	  {
		"type": "separator",
		"margin": "xs"
	  },
	  {
		"type": "box",
		"layout": "vertical",
		"margin": "sm",
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
					"text": "__AI_TXT__",
					"size": "md",
					"color": "#555555",
					"flex": 0,
					"wrap": true
				  }
				],
				"width": "260px",
				"paddingAll": "xs"
			  }
			]
		  }
		]
	  },
	  {
		"type": "separator",
		"margin": "md"
	  },
	  {
		"type": "separator",
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
				"type": "text",
				"text": "本卦",
				"size": "sm",
				"color": "#111111",
				"wrap": true
			  }
			],
			"margin": "md",
			"height": "16px"
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
					"text": "__HOMEGUA__",
					"size": "lg",
					"color": "#555555",
					"weight": "bold"
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
					"text": "__HOMEGUA_SUB__",
					"size": "sm",
					"color": "#111111",
					"align": "end",
					"gravity": "bottom"
				  }
				],
				"offsetBottom": "0px"
			  }
			]
		  },


		  {
			"type": "separator"
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
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "__HOMETXT__",
						"size": "md",
						"color": "#555555",
						"flex": 0,
						"wrap": true
					  }
					],
					"width": "260px",
					"spacing": "none",
					"paddingAll": "xs"
				  }
				],
				"spacing": "md"
			  }
			]
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
						"text": "More..",
						"size": "md",
						"color": "#999999",
						"wrap": true,
						"weight": "bold",
						"align": "end",
						"action": {
						  "type": "message",
						  "label": "action",
						  "text": "__HOMEMORE__"
						}
					  }
					],
					"width": "260px",
					"spacing": "none",
					"paddingAll": "xs"
				  }
				],
				"spacing": "md"
			  }
			]
		  }
		]
	  }"""






ichingGuaLayoutChange = """
	  ,
	  {
		"type": "box",
		"layout": "vertical",
		"contents": [
		  {
			"type": "separator",
			"margin": "md"
		  },
		  {
			"type": "separator",
			"margin": "xs"
		  },
		  {
			"type": "box",
			"layout": "vertical",
			"contents": [
			  {
				"type": "text",
				"text": "變卦",
				"size": "sm",
				"color": "#111111",
				"wrap": true
			  }
			],
			"margin": "md",
			"height": "16px"
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
					"text": "__CHGGUA__",
					"size": "lg",
					"color": "#555555",
					"weight": "bold"
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
					"text": "__CHGGUA_SUB__",
					"size": "sm",
					"color": "#111111",
					"align": "end",
					"gravity": "bottom"
				  }
				],
				"offsetBottom": "0px"
			  }
			]
		  },



		  {
			"type": "separator"
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
					"layout": "horizontal",
					"contents": [
					  {
						"type": "text",
						"text": "__CHGTXT__",
						"size": "md",
						"color": "#555555",
						"flex": 0,
						"wrap": true
					  }
					],
					"width": "260px",
					"spacing": "none",
					"paddingAll": "xs"
				  }
				],
				"spacing": "md"
			  }
			]
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
						"text": "More...",
						"size": "md",
						"color": "#999999",
						"wrap": true,
						"weight": "bold",
						"align": "end",
						"action": {
						  "type": "message",
						  "label": "action",
						  "text": "__CHGMORE__"
						}
					  }


					],
					"width": "260px",
					"spacing": "none",
					"paddingAll": "xs"
				  }
				],
				"spacing": "md"
			  }
			]
		  }
		]
	  }

  """


def get_short_name(name):
	"""
	根據易經命名慣例提取簡稱：
	- 八純卦 (如：乾為天) -> 取第 1 個字 (乾)
	- 64 卦其餘卦 (如：雷山小過) -> 取後 2 個字 (小過)
	"""
	if len(name) == 3 and name[1] == '為':
		return name[0]
	elif len(name) >= 4:
		return name[-2:]
	elif len(name) >= 3:
		return name[-1]		
	return name


### 防止寫錯字用的
def fixGuaWording( guaName ):
	fixList = {	"西日":"酉日","西月":"酉日","始":"姤","恒":"恆","遁":"遯","暌":"睽","癸":"睽","責":"賁","憤":"賁","濛":"蒙","盟":"蒙","萌":"蒙","換":"渙","喚":"渙" ,"移":"頤","ㄅ":"剝" ,"須":"需","遇":"豫","進":"晉","減":"蹇","垢":"姤","后":"姤","夠":"姤","脆":"萃","卒":"萃","丰":"豐","換":"渙","喚":"渙","中浮":"中孚","中俘":"中孚","中浮":"中孚","同仁":"同人","大友":"大有","噴":"賁","奔":"賁","波":"剝","忘":"妄","進":"晉","佳人":"家人","頂":"鼎","丰":"豐" ,"屢":"履"  }


	nameBuf = ""
	for item in guaName:  # item 是每個字
		if item in fixList.keys():  # 這裡要用 item,不是 guaName!
			nameBuf += fixList[item]
		else:
			nameBuf += item
	
	return nameBuf





import os
import json
import requests

# 記憶體層快取（多個 URL 可共用）
_JSON_CACHE = {}


def load_json_with_cache(url, force_reload= False):
	if not force_reload and url in _JSON_CACHE:
		return _JSON_CACHE[url]

	local_file = url.split("/")[-1]

	if not force_reload and os.path.exists(local_file):
		with open(local_file, "r", encoding="utf-8") as f:
			data = json.load(f)
			_JSON_CACHE[url] = data
			return data

	# ⬇️ 真的要更新時才下載
	import requests
	resp = requests.get(url)
	resp.raise_for_status()
	data = resp.json()

	with open(local_file, "w", encoding="utf-8") as f:
		json.dump(data, f, ensure_ascii=False, indent=2)

	_JSON_CACHE[url] = data
	return data




## gua64.json
def get_gua_text(gua_name):
	gua_name = fixGuaWording(gua_name)
	# print ( gua_name )
	GUA64_URL = r"https://res.cloudinary.com/ds9jcwwcw/raw/upload/v1767273900/__icon/gua64.json"
	gua_dict = load_json_with_cache(GUA64_URL ,force_reload= False)

	gua = gua_dict.get(gua_name)
	if not gua:
		return {
			"judgment": "找不到此卦",
			"desc": "",
			"meaning" : gua.get( "meaning" , "")
		}

	return {
		"judgment": gua.get("judgment", ""),
		"desc": gua.get("desc", ""),
		"meaning" : gua.get( "meaning" , "")
	}


## guaMatchDict.json
def get_gua_match_text(gua, yao):
	gua = fixGuaWording( gua )
	yao = fixGuaWording( yao )
	# print(gua, yao)
	GUA_MATCH_URL = r"https://res.cloudinary.com/ds9jcwwcw/raw/upload/v1767351820/__icon/guaMatchDict.json"
	guaMatchDict = load_json_with_cache(GUA_MATCH_URL)
	return guaMatchDict.get(gua, {}).get(yao, "找不到卦辭")

# https://res.cloudinary.com/ds9jcwwcw/raw/upload/v1766911910/__icon/gua64.json
# https://res.cloudinary.com/ds9jcwwcw/raw/upload/v1767271041/__icon/guaMatchDict.json

# result = get_gua_text("乾為天")

# print(result["judgment"])
# print(result["desc"])







# def warm_up_cache(urls):
#     for url in urls:
#         try:
#             load_json_with_cache(url)
#             print(f"🔥 cache warmed: {url}")
#         except Exception as e:
#             print(f"⚠️ cache warm failed: {url} → {e}")



# URLS_TO_WARM = [
#      r"https://res.cloudinary.com/ds9jcwwcw/raw/upload/v1767273900/__icon/gua64.json",
#      r"https://res.cloudinary.com/ds9jcwwcw/raw/upload/v1767351820/__icon/guaMatchDict.json"
# ]
# ## 放在app = Flask(__name__)下
# warm_up_cache(URLS_TO_WARM)





def find_full_gua_name(short_name):
	"""根據簡稱找到完整卦名"""
	bufList = ["坤為地","山地剝","水地比","風地觀","雷地豫","火地晉","澤地萃","天地否",
			   "地山謙","艮為山","水山蹇","風山漸","雷山小過","火山旅","澤山咸","天山遯",
			   "地水師","山水蒙","坎為水","風水渙","雷水解","火水未濟","澤水困","天水訟",
			   "地風升","山風蠱","水風井","巽為風","雷風恆","火風鼎","澤風大過","天風姤",
			   "地雷復","山雷頤","水雷屯","風雷益","震為雷","火雷噬嗑","澤雷隨","天雷無妄",
			   "地火明夷","山火賁","水火既濟","風火家人","雷火豐","離為火","澤火革","天火同人",
			   "地澤臨","山澤損","水澤節","風澤中孚","雷澤歸妹","火澤睽","兌為澤","天澤履",
			   "地天泰","山天大畜","水天需","風天小畜","雷天大壯","火天大有","澤天夬","乾為天"]
	
	for gua in bufList:
		if short_name in gua:
			return gua
	
	return None



	
def ichingGuaUI(guaName, printMode=False):
	# 移除開頭的 #
	guaName = guaName.lstrip("#").strip()
	guaName = fixGuaWording( guaName )
	# 處理不同格式
	if "/" in guaName:
		# 格式: "風山漸/天山遁"
		homeGua, changeGua = guaName.split("/")
		mainTitle = get_short_name(homeGua) + "之" + get_short_name(changeGua) + "卦"
		mainSubTitle = get_gua_match_text(get_short_name(homeGua), get_short_name(changeGua))
		print( homeGua, changeGua )
		change_result = get_gua_text(changeGua)
		changeGuaSub = change_result["judgment"]
		changeGuaTxt = change_result["desc"]
		changeMeaning = change_result["meaning"]
		
	elif "之" in guaName:
		# 格式: "漸之遁" 或 "漸之遁卦"
		guaName = guaName.replace("卦", "")  # 移除「卦」字
		parts = guaName.split("之")
		
		if len(parts) == 2:
			short_home = parts[0].strip()
			short_change = parts[1].strip()
			
			# 從簡稱找到完整卦名
			homeGua = find_full_gua_name(short_home)
			changeGua = find_full_gua_name(short_change)
			
			# print( homeGua ,changeGua)
			if homeGua and changeGua:
				mainTitle = short_home + "之" + short_change + "卦"
				mainSubTitle = get_gua_match_text(short_home, short_change)
				change_result = get_gua_text(changeGua)
				changeGuaSub = change_result["judgment"]
				changeGuaTxt = change_result["desc"]
				changeMeaning = change_result["meaning"]
			else:
				# 找不到卦名,返回錯誤或預設值
				return {"error": f"找不到卦名: {guaName}"}
		else:
			return {"error": f"格式錯誤: {guaName}"}
			
	else:
		# 格式: 單一卦名 "雷澤歸妹"
		homeGua = guaName
		changeGua = "-"
		mainTitle = homeGua + "卦"
		mainSubTitle = get_gua_match_text(get_short_name(homeGua), get_short_name(homeGua))
		change_result = "-"
		changeGuaSub = "-"
		changeGuaTxt = "-"
		changeMeaning = "-"
	
	# 取得本卦資訊
	home_result = get_gua_text(homeGua)
	homeGuaSub = home_result["judgment"]
	homeGuaTxt = home_result["desc"]
	homeMeaning = home_result["meaning"]
	
	# 返回結果 (根據你原本的程式邏輯)
	# ...








	print ( "mainTitle - " , mainTitle ) 
	print ( "mainSubTitle - " , mainSubTitle ) 

	print ( "homeGua - " , homeGua ) 
	print ( "changeGua - " , changeGua ) 

	print ( "homeGuaSub - ", homeGuaSub )
	print ( "homeGuaTxt - ", homeGuaTxt )
	print ( "changeGuaSub - ", changeGuaSub )
	print ( "changeGuaTxt - ", changeGuaTxt )


	print ( "homeMeaning - ", homeMeaning )
	print ( "changeMeaning - ", changeMeaning )



	ai_guaTxt = solve_iching( homeGua, changeGua , homeMeaning , changeMeaning )
	print ( "ai_guaTxt - ", ai_guaTxt )

	# ai_guaTxt = "小過之鼎卦, 當前處於小有過錯的階段, 意謂著雖有小過失但非重大阻礙, 猶如雷聲在山頂迴盪, 宜居安思危、謹守小節, 避免過度冒險; 隨後轉入鼎卦, 象徵事物穩定、賢才匯聚, 猶如木上生火, 烹飪成物, 預示著新局面即將確立, 應當審慎權衡進退, 穩步前行, 轉機就在這些變化之中."

	# mainTitle ## 標題
	# mainSubTitle  ## 副標題
	# homeGua ## 本卦
	# homeGuaSub ## 本卦副標

	# homeGuaTxt ## 本卦內文

	# changeGua ## 變卦
	# changeGuaSub ## 變卦副標
	# changeGuaTxt ## 變卦	內文

	# ai_guaTxt ## ai產生內容



	ichingGua_layoutFlex = ichingGuaLayoutHome
	if changeGua != "-":
		ichingGua_layoutFlex += ichingGuaLayoutChange
	ichingGua_layoutFlex += """
	]
  }
}"""

	# print( mainTitle)

	ichingGua_layoutFlex = (   ichingGua_layoutFlex .replace( "__GUAMATCH__" , mainTitle )
													.replace( "__MAINSUB__" , mainSubTitle )
													.replace( "__AI_TXT__" , ai_guaTxt )
													.replace( "__HOMEGUA__" , homeGua )
													.replace( "__HOMEGUA_SUB__" , homeGuaSub )
													.replace( "__HOMETXT__" , homeGuaTxt )
													.replace( "__CHGGUA__" , changeGua )
													.replace( "__CHGGUA_SUB__" , changeGuaSub )
													.replace( "__CHGTXT__" , changeGuaTxt )

													.replace("__HOMEMORE__" , "["+ homeGua + "]")  ## 本卦
													.replace("__CHGMORE__" , "["+ changeGua + "]")	 ## 變卦													
							)


	if printMode == True:
		print( ichingGua_layoutFlex )


	# 文字轉換成字典
	finalLayout_dict = json.loads(ichingGua_layoutFlex)
	return finalLayout_dict









if __name__ == '__main__':
	ichingGuaUI( "#雷澤歸妹/地火明夷" , printMode = True )

# ichingGuaUI( "#巽為風/風天小畜" , printMode = True )
# {
#   "type": "bubble",
#   "body": {
#     "type": "box",
#     "layout": "vertical",
#     "contents": [
#       {
#         "type": "text",
#         "text": "易經解卦",
#         "weight": "bold",
#         "color": "#57988F",
#         "size": "sm"
#       },
#       {
#         "type": "text",
#         "text": "__GUAMATCH__",
#         "weight": "bold",
#         "size": "xl",
#         "margin": "xs"
#       },
#       {
#         "type": "text",
#         "text": "__MAINSUB__",
#         "size": "xs",
#         "color": "#365E8E",
#         "wrap": true,
#         "weight": "bold"
#       },
#       {
#         "type": "separator",
#         "margin": "sm"
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "margin": "sm",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "__AI_TXT__",
#                     "size": "md",
#                     "color": "#555555",
#                     "flex": 0,
#                     "wrap": true
#                   }
#                 ],
#                 "width": "260px",
#                 "paddingAll": "xs"
#               }
#             ]
#           }
#         ]
#       },
#       {
#         "type": "separator",
#         "margin": "md"
#       },
#       {
#         "type": "separator",
#         "margin": "xs"
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "本卦",
#                 "size": "sm",
#                 "color": "#111111",
#                 "wrap": true
#               }
#             ],
#             "margin": "md",
#             "height": "16px"
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "__HOMEGUA__",
#                     "size": "lg",
#                     "color": "#555555",
#                     "weight": "bold"
#                   }
#                 ],
#                 "width": "90px"
#               },
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "__HOMEGUA_SUB__",
#                     "size": "sm",
#                     "color": "#111111",
#                     "align": "end",
#                     "gravity": "bottom"
#                   }
#                 ]
#               }
#             ]
#           },
#           {
#             "type": "separator"
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "margin": "xs",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "__HOMETXT__",
#                         "size": "md",
#                         "color": "#555555",
#                         "flex": 0,
#                         "wrap": true
#                       }
#                     ],
#                     "width": "260px",
#                     "spacing": "none",
#                     "paddingAll": "xs"
#                   }
#                 ],
#                 "spacing": "md"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "More..",
#                         "size": "md",
#                         "color": "#999999",
#                         "wrap": true,
#                         "weight": "bold",
#                         "align": "end"
#                       }
#                     ],
#                     "width": "260px",
#                     "spacing": "none",
#                     "paddingAll": "xs"
#                   }
#                 ],
#                 "spacing": "md"
#               }
#             ]
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#           {
#             "type": "separator"
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "變卦",
#                 "size": "sm",
#                 "color": "#111111",
#                 "wrap": true
#               }
#             ],
#             "margin": "md",
#             "height": "16px"
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "__CHGGUA__",
#                     "size": "lg",
#                     "color": "#555555",
#                     "weight": "bold"
#                   }
#                 ],
#                 "width": "90px"
#               },
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "text",
#                     "text": "__CHGGUA_SUB__",
#                     "size": "sm",
#                     "color": "#111111",
#                     "align": "end",
#                     "gravity": "bottom"
#                   }
#                 ]
#               }
#             ]
#           },
#           {
#             "type": "separator"
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "margin": "xs",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "__CHGTXT__",
#                         "size": "md",
#                         "color": "#555555",
#                         "flex": 0,
#                         "wrap": true
#                       }
#                     ],
#                     "width": "260px",
#                     "spacing": "none",
#                     "paddingAll": "xs"
#                   }
#                 ],
#                 "spacing": "md"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "contents": [
#               {
#                 "type": "box",
#                 "layout": "horizontal",
#                 "contents": [
#                   {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                       {
#                         "type": "text",
#                         "text": "More...",
#                         "size": "md",
#                         "color": "#999999",
#                         "wrap": true,
#                         "weight": "bold",
#                         "align": "end"
#                       }
#                     ],
#                     "width": "260px",
#                     "spacing": "none",
#                     "paddingAll": "xs"
#                   }
#                 ],
#                 "spacing": "md"
#               }
#             ]
#           }
#         ]
#       }
#     ]
#   },
#   "styles": {
#     "footer": {
#       "separator": true
#     }
#   }
# }