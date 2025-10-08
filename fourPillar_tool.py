# -*- coding: utf-8 -*-

import  sxtwl
# https://blog.csdn.net/Lc_001/article/details/129195335
import datetime

from yearData import *


Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
ShX = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]
jqmc =["冬至","小寒","大寒","立春","雨水","驚蟄","春分","清明","穀雨","立夏","小滿","芒種",
	   "夏至","小暑","大暑","立秋","處暑","白露","秋分","寒露","霜降","立冬","小雪","大雪"]

WeekCn = ["(日)", "(一)", "(二)", "(三)", "(四)", "(五)", "(六)"]

ganZhi_Dict ={
	# 1984年 甲子
	1 : "甲子", 2 : "乙丑", 3 : "丙寅", 4 : "丁卯", 5 : "戊辰", 6 : "己巳", 7 : "庚午", 8 : "辛未", 9 : "壬申", 10 : "癸酉", 
	11 : "甲戌", 12 : "乙亥", 13 : "丙子", 14 : "丁丑", 15 : "戊寅", 16 : "己卯", 17 : "庚辰", 18 : "辛巳", 19 : "壬午", 20 : "癸未",
	21 : "甲申", 22 : "乙酉", 23 : "丙戌", 24 : "丁亥", 25 : "戊子", 26 : "己丑", 27 : "庚寅", 28 : "辛卯", 29 : "壬辰", 30 : "癸巳", 
	31 : "甲午", 32 : "乙未", 33 : "丙申", 34 : "丁酉", 35 : "戊戌", 36 : "己亥", 37 : "庚子", 38 : "辛丑", 39 : "壬寅", 40 : "癸卯", 
	41 : "甲辰", 42 : "乙巳", 43 : "丙午", 44 : "丁未", 45 : "戊申", 46 : "己酉", 47 : "庚戌", 48 : "辛亥", 49 : "壬子", 50 : "癸丑", 
	51 : "甲寅", 52 : "乙卯", 53 : "丙辰", 54 : "丁巳", 55 : "戊午", 56 : "己未", 57 : "庚申", 58 : "辛酉", 59 : "壬戌", 60 : "癸亥", 
}














# 輸入西元年份得到四柱及陰曆相關資訊
# detail = True ('2023/2/8/12/58', '癸卯-甲寅-丁酉-丙午', '陽曆: 2023年2月8日(三) 12:58', '陰曆: 2023年1月18日 | 立春>>雨水', '2023/1/18')
# detail = False  ['癸卯', '甲寅', '丁酉', '丙午']

def replaceYear( year ):
	yearBuf = str(year).replace("0","〇").replace("1","一").replace("2","二").replace("3","三").replace("4","四").replace("5","五").replace("6","六").replace("7","七").replace("8","八").replace("9","九")
	return yearBuf




def getFourPillar( fullDate = "" , detail = False ):
	# fullDate = "2020/12/30/03/00"

	fullDate = fullDate.replace( "-", "/")

	if fullDate == "":  ## 如果沒有輸入日期則取得現時
		fullDate = getNowTime()

	orgDate = fullDate.split("/")
	# print(">>>",orgDate)
	yNum = int(orgDate[0])
	mNum = int(orgDate[1])
	dNum = int(orgDate[2])
	hNum = int(orgDate[3])
	msNus = int(orgDate[4])
	# 從公歷年月日獲取一天的信息
	day = sxtwl.fromSolar( yNum ,  mNum , dNum ) 
	week = WeekCn[day.getWeek()]

	# lightDate = "陽曆: %d年%d月%d日%s %02d:%02d" % (day.getSolarYear(), day.getSolarMonth(), day.getSolarDay(),week , hNum ,msNus )
	lightDate = "%d/%02d/%02d/%02d:%02d" % (day.getSolarYear(), day.getSolarMonth(), day.getSolarDay() , hNum ,msNus )	
	timeShow = "%02d:%02d" % (hNum ,msNus) 




	# darkDate = "農曆:%d年%s%d月%d日" % (day.getLunarYear(), 
	#     '閏' if day.isLunarLeap() else '', day.getLunarMonth(), day.getLunarDay())
	darkDate = "陰曆: %d年%s%d月%d日" % (day.getLunarYear(), 
		'閏' if day.isLunarLeap() else '', day.getLunarMonth(), day.getLunarDay())



	datBuf = {
			1:"初一",2:"初二" ,3:"初三" ,4:"初四" ,5:"初五" ,6:"初六" ,7:"初七" ,8:"初八" ,9:"初九" ,10:"初十" ,11:"十一" ,12:"十二" ,13:"十三" ,14:"十四" ,15:"十五" ,16:"十六" ,17:"十七" ,18:"十八" ,19:"十九" ,20:"二十" ,21:"廿一" ,22:"廿二" ,23:"廿三" ,24:"廿四" ,25:"廿五" ,26:"廿六" ,27:"廿七" ,28:"廿八" ,29:"廿九" ,30:"三十" ,31:"三一" 
			}
	monthBuf = {
				1:"正月",2:"二月" ,3:"三月" ,4:"四月" ,5:"五月" ,6:"六月" ,7:"七月" ,8:"八月" ,9:"九月" ,10:"十月" ,11:"十一月" ,12:"十二月" 
				}

	# print( monthBuf[day.getLunarMonth()] + datBuf[day.getLunarDay()]) ## 轉換成中文數字

	fullDarkDate  = "%s%s%s" % ( 
		'閏' if day.isLunarLeap() else '', monthBuf[day.getLunarMonth()], datBuf[day.getLunarDay()])

	# fullDarkDate  = "%d/%s%d/%d" % (day.getLunarYear(), 
	# 	'閏' if day.isLunarLeap() else '', day.getLunarMonth(), day.getLunarDay())	



	yTG = day.getYearGZ()
	yGanZhi = Gan[yTG.tg] + Zhi[yTG.dz]
	# print("以立春為界的年干支", Gan[yTG.tg] + Zhi[yTG.dz]) 
	animalType = ShX[yTG.dz]
	# print("以立春為界的生肖:", ShX[yTG.dz])

	#月干支
	mTG = day.getMonthGZ()
	mGanZhi = Gan[mTG.tg] + Zhi[mTG.dz]
	# print("月干支", Gan[mTG.tg] + Zhi[mTG.dz]) 

	#日干支
	dTG  = day.getDayGZ()
	dGanZhi = Gan[dTG.tg] + Zhi[dTG.dz]
	# print( dGanZhi )


	if hNum == 23: ## 修正原本12點之前日干支都不會跳到隔日的問題
		tgIndex = Gan.index( Gan[dTG.tg] )
		dzIndex = Zhi.index( Zhi[dTG.dz])
		# print( Gan[ (tgIndex+1)%10 ] )
		# print( Zhi[ (dzIndex+1)%12 ] )
		nextTg = Gan[ (tgIndex+1)%10 ]
		nextDz = Zhi[ (dzIndex+1)%12 ]		
		dGanZhi = nextTg+nextDz
		# print(dGanZhi)



	# hour = 18
	sTG = day.getHourGZ( hNum  )
	hGanZhi = Gan[sTG.tg] + Zhi[sTG.dz]
	# print( hGanZhi )
	# print("%d時的干支"%(hour, ), Gan[sTG.tg] + Zhi[sTG.dz]) 

	fourPillar_Buf = [ yGanZhi, mGanZhi, dGanZhi , hGanZhi ] ## 四柱


	# checkOutLuck( Gan[mTG.tg] ,Zhi[mTG.dz] , Zhi[sTG.dz]) #判斷出行吉兇 日干 日支 時支


	if detail == True:
		day_buf = day

		jeChi_start = ""
		jeChi_end = ""
		jeChi_match = ">"

		while True:
			# 这里可以使用after或者before，不用担心速度，这里的计算在底层仅仅是+1这么简单
			if day.hasJieQi():
				# print( ">>>>> MATCH" , day_buf.hasJieQi())
				day_buf = day ## 如果這天正是節氣的當天，就從這天開始算
				jeChi_match = "!"
			else:
				day_buf = day_buf.before(1) ## 如果不是節氣當天，就往前算一天，如果還不是節氣日，就一路往前找

			# if day_buf.hasJieQi():

		# while True:
		# 	# 这里可以使用after或者before，不用担心速度，这里的计算在底层仅仅是+1这么简单
			# day_buf = day_buf.before(1)
			if day_buf.hasJieQi():
				# print('節氣：%s'% jqmc[day_buf.getJieQi()])
				jeChi_start = jqmc[day_buf.getJieQi()]
				while True:
					day_buf = day_buf.after(1)
					if day_buf.hasJieQi():
						# print('節氣：%s'% jqmc[day_buf.getJieQi()])
						jeChi_end = jqmc[day_buf.getJieQi()]
						break
				break

		jeChi = ( jeChi_start , jeChi_end )
		jeChi_show =  [ jeChi_start , jeChi_match , jeChi_end ]
	
		## 如果為True才會回傳一堆detail
		# return fullDate , '-'.join(fourPillar_Buf) , lightDate, "%s | %s"% ( darkDate , jeChi_show ) , fullDarkDate
		
		return lightDate ,fullDarkDate ,fourPillar_Buf , jeChi_show , week , timeShow 

	## 不為True則只傳回四柱
	return fourPillar_Buf




## 由干支取得西元年
def getYear ( pillarYear ):  
	yearBuf = None
	for yGZ in  ganZhi_Dict.keys():  # ganZhi_Dict為六十甲子與年的對照表
		if ganZhi_Dict[yGZ] == pillarYear:
			# print ( "year:" , yGZ + 1983 )
			yearBuf = yGZ + 1983 ## 1983為甲子元年
			# 找出年干支所在的西元年
			return yearBuf
# print(getYear ( "甲子" ))


# ## 由西元年取得年干支
# def getYearGZ ( year ):

# 	for each in ganZhi_Dict.keys():
# 		# print(each,year)
# 		checkYear = ( year -1983 )%60
# 		if checkYear == 0:
# 			checkYear = 60
					
# 		if each == checkYear:
# 			return ganZhi_Dict[each]




## 輸入干支或輸入西元年，取得該年資訊，如兩引數都有輸入，則以干支優先
## yearGZ     干支
## basicYear  西元年


# 	## 輸入干支或輸入西元年
# def checkYear(dateDataIn=""):
#     import calendar, datetime
#     from datetime import datetime, timezone, timedelta

#     ZhiList = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
#     GanList = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
#     ShX = ["鼠","牛","虎","兔","龍","蛇","馬","羊","猴","雞","狗","豬"]

#     dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
#     localtimeReal = dt1.astimezone(timezone(timedelta(hours=8)))  # 東八區
#     year__real = localtimeReal.year

#     dateDataIn = dateDataIn.strip().replace("年", "")  # 移除「年」字與空白
#     print("輸入：", dateDataIn)

#     # 預設
#     basicYear = None
#     yearGZ = None

#     # ✅ 輸入為單一地支（午、辰等），只取最接近的過去年
#     if dateDataIn in ZhiList:
#         matchingYears = [(key + 1983, val) for key, val in ganZhi_Dict.items() if val[1] == dateDataIn]
#         matchingYears = [item for item in matchingYears if item[0] <= year__real]
#         if not matchingYears:
#             return None
#         basicYear, yearGZ = max(matchingYears, key=lambda x: x[0])

#     # ✅ 輸入為完整干支（甲午）
#     elif len(dateDataIn) == 2 and dateDataIn[0] in GanList and dateDataIn[1] in ZhiList:
#         yearGZ = dateDataIn
#         basicYear = next((key + 1983 for key, val in ganZhi_Dict.items() if val == yearGZ), None)

#     # ✅ 輸入為數字（西元年或民國年）
#     elif dateDataIn.isdigit():
#         basicYear = int(dateDataIn)
#         if basicYear < 999:
#             basicYear += 1911  # 民國轉西元
#         yearGZ = ganZhi_Dict.get((basicYear - 1983) % 60 or 60)

#     else:
#         return None  # 格式錯誤或無法辨識

#     if basicYear is None:
#         return None

#     animalType = ShX[ZhiList.index(yearGZ[-1])]
#     yearList = [basicYear, yearGZ, animalType]

#     # 🧠 加入相關循環年份（允許未來年份）
#     relatedYears = [basicYear - 120, basicYear - 60, basicYear, basicYear + 60, basicYear + 120]
#     relatedYears = [y for y in relatedYears if y <= year__real] if dateDataIn in ZhiList else relatedYears
#     yearList.extend(relatedYears)

#     yearList.extend(getDictData(yearGZ))  # 加入該年五行與命理描述
#     return yearList



	# print( yearList)
	## [1954, '甲午', '馬', 1894, 1954, 2014]

	# yearList.extend( getDictData( yearGZ )) # 加入最後兩項 更多該年資訊
	# # [1954, '甲午', '馬', 1894, 1954, 2014, '金', '五行屬沙中金，雲中之馬。為人和氣，喜好春風，交朋結友，利官近貴，遇凶不為凶，可逢凶化吉，骨肉少靠，女人口快能言，多出風頭。']
	# return yearList

# print(checkYear( "卯"))

# 乙巳年卯月戊戌日
# 巳年寅月申日(戌亥空)

# 比對四柱是否相同
# list1 = ['庚子', '甲申', '乙未', '丁丑']
# list2 = ['庚子', '甲申', '巳未', '乙丑'] 
# list1 為標準版本  list2 為輸入版
# def compare_ganzhiList(  list1, list2, item = 1 ):
# 	## item為對從後數來幾個元素作用

#     if len(list1) != len(list2) or item > len(list1):
#         return False
	
#     split_index = len(list1) - item
	
#     for i in range(len(list1)):
#         a, b = list1[i], list2[i]
#         if i < split_index:
#             if a != b:
#                 return False  # 前段必須完全相同
#         else:
#             if a == b:
#                 continue
#             elif a[-1] != b[-1]:
#                 return False  # 後段只比對地支
#     return True
def normalize_ganzhi(gz, GanList, ZhiList):
	"""把輸入拆成 (干, 支)，允許只有地支，或附帶 '月' '時'"""
	gz = gz.replace("月", "").replace("時", "")
	gan = None
	zhi = None
	for g in GanList:
		if g in gz:
			gan = g
			break
	for z in ZhiList:
		if z in gz:
			zhi = z
			break
	return (gan, zhi)


def compare_ganzhiList(list1, list2, item=3 ):
	GanList = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
	ZhiList = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]

	if len(list1) != len(list2) or item > len(list1):
		return False

	split_index = len(list1) - item

	for i in range(len(list1)):
		a_gan, a_zhi = normalize_ganzhi(list1[i], GanList, ZhiList)
		b_gan, b_zhi = normalize_ganzhi(list2[i], GanList, ZhiList)

		if i < split_index:
			# 前段必須完整匹配
			if a_gan != b_gan or a_zhi != b_zhi:
				return False
		else:
			# 後段可以寬鬆比對
			if b_gan is None:  # list2 沒寫天干，只比地支
				if a_zhi != b_zhi:
					return False
			else:  # list2 有寫天干，必須完全一致
				if a_gan != b_gan or a_zhi != b_zhi:
					return False
	return True




## 由四柱取得西元年月日時
## >inputDate 2022/01/01/01/00

# def fourPillarToDateMain( inputDate ="庚子,甲申,乙未,丁丑"  ):
def fourPillarToDateMain( inputDate = '乙巳/卯/戊戌'  ):

	# print( inputDate , type(inputDate) )
	inputDate = inputDate.replace("  "," ").replace("  "," ").replace(",","/").replace(" ","/").replace(".","/").replace("/","/").replace("-","/")

	inputDateList = inputDate.split("/")
	# print( inputDateList )
	# print ( getYear( inputDateList[0] ) )
	currentYear = getYear( inputDateList[0] ) ## 由干支取得西元年
	inputDate = "%02d/%02d/%02d/%02d/%02d"% (  currentYear-1 , 1 , 1 , 1 , 0 )
	print( ">inputDate" , inputDate )
	out = inputDate

	for eachHour in range( 4380*3 ):  # 兩小時一檔跑三年份
		yValue =0
		mValue =0
		dValue =0
		hValue =0

		# print( out ) ##2020/08/20/01/00
		# print(inputDateList) ###['庚子', '甲申', '乙未', '丁丑']

		# print( getFourPillar(out)[:-1] )

		# if "卯" in  getFourPillar(out)out[1]:
		# 	print ( getFourPillar(out))

		# print ( getFourPillar(out))

		# 三柱
		if len( inputDateList ) == 3: ## 如果只有年月日柱，缺時柱 ##['庚子', '甲申', '乙未']
			if ( getFourPillar( out )[0] == inputDateList[0]) and ( getFourPillar( out )[1][-1] == inputDateList[1][-1] ) and ( getFourPillar( out )[2] == inputDateList[2] ):

			# if getFourPillar( out )[:-1] == inputDateList:   ## 比對得到的四柱，去掉時柱之後，是否和輸入的三柱相同
				out = ( dt + datetime.timedelta( hours = 15 )).strftime("%Y/%m/%d/%H/%M")
				return out +"<" 	## 三柱的標示

		# print( getFourPillar( out ) ,  inputDateList )
		if ( compare_ganzhiList( getFourPillar( out ) ,  inputDateList  )):
		# 	print("TRUE  ==========")

		# if  getFourPillar( out ) == inputDateList:##['庚子', '甲申', '乙未', '丁丑']

			return out

			break

		dt = datetime.datetime.strptime( out , "%Y/%m/%d/%H/%M")
		out = ( dt + datetime.timedelta( hours = 2 )).strftime("%Y/%m/%d/%H/%M")

		# out = ( dt + datetime.timedelta( minutes = 10 )).strftime("%Y-%m-%d-%H-%M")



## 取得東八區現時，西元年/月/日/時/分  2024/10/20/14/29
def getNowTime( utc_hour = 8 ):
	import datetime
	from datetime import datetime,timezone,timedelta
	dt1 = datetime.now(timezone.utc)
	localtimeReal = dt1.astimezone(timezone(timedelta( hours = utc_hour ))) # 轉換時區 -> 東八區 ( 大陸，台灣，東8區，日本，東9區)

	year__real =  localtimeReal.year
	month__real = localtimeReal.month
	day__real = localtimeReal.day
	hour__real = localtimeReal.hour
	mins__real = localtimeReal.minute
	# print(  "%s/%s/%s/%s/%s"% (year__real,month__real,day__real,hour__real,mins__real) )
	return  "%s/%s/%s/%s/%s"% (year__real,month__real,day__real,hour__real,mins__real)

 # "2023/2/8/12/58"
# 2024-10-20 14:27:04.115877+08:00







def checkMsgFun( msg , utc = 8 ):
	# print( ">>" , msg )
	import calendar,datetime
	from datetime import datetime,timezone,timedelta
	dt1 = datetime.utcnow().replace( tzinfo = timezone.utc )
	localtimeReal = dt1.astimezone(timezone(timedelta( hours = utc ))) # 轉換時區 -> 東八區 ( 大陸，台灣，東8區，日本，東9區)

	year__real =  localtimeReal.year
	month__real = localtimeReal.month
	day__real = localtimeReal.day
	hour__real = localtimeReal.hour
	mins__real = localtimeReal.minute

	year_Buf = None
	month_Buf =None
	day_Buf = None
	hour_Buf = None
	mins_Buf =None

 


	# 林小姐|now


	msg = msg.replace("  "," ").replace("  "," ").replace(",","/").replace(" ","/").replace(".","/").replace("/","/").replace("時盤","時").replace("刻盤","刻")
	# print( "in:" + msg )



	if msg == "":
		year_Buf  = year__real
		month_Buf = month__real
		day_Buf   = day__real
		hour_Buf  = hour__real
		mins_Buf  = mins__real

	# 3,59
	if ( len( msg.split("/")) == 2 ):
		if ((  msg.split("/")[0].isdigit() == True ) and (  msg.split("/")[1].isdigit() == True ))  and ((  0 <= int(msg.split("/")[0]) <= 23 ) and ( 0 <= int(msg.split("/")[1]) <= 60)):
			# mainData = pageMainClass( panType , year = year__real , month = month__real ,day = day__real , hour = int(  msg.split("/")[0] )  , mins = int(  msg.split("/")[1] ) )
			# panType   = "時盤"
			year_Buf  = year__real
			month_Buf = month__real
			day_Buf   = day__real
			hour_Buf  = int(  msg.split("/")[0] )
			mins_Buf  = int(  msg.split("/")[1] )

		else:
			# print( "%s-%d年%d月%d日%d:%d ??" % (panType , year__real , month__real ,day__real , int(  msg.split("/")[0] )  ,int(  msg.split("/")[1] )) )
			return ( "Error" , "%d年%d月%d日%02d:%02d ??" % ( year__real , month__real ,day__real , int(  msg.split("/")[0] )  ,int(  msg.split("/")[1] )) )
	# 5,14,3,59
	if ( len( msg.split("/")) == 4 ):
		if ((  msg.split("/")[0].isdigit() == True ) and (  msg.split("/")[1].isdigit() == True ) and (  msg.split("/")[2].isdigit() == True ) and (  msg.split("/")[3].isdigit() == True ) ) and ( 1 <= int(msg.split("/")[0]) <= 12 ) and ( 1 <= int(msg.split("/")[1]) <= calendar.monthrange(   year__real  ,  int(msg.split("/")[0])  )[1] )  and (  0 <= int(msg.split("/")[2]) <= 23) and ( 0 <= int(msg.split("/")[3]) <= 60 ) :
			# mainData = pageMainClass( panType , year = year__real , month = int(  msg.split("/")[0] )  , day = int(  msg.split("/")[1] ) , hour = int(  msg.split("/")[2] )  , mins = int(  msg.split("/")[3] ) )
			year_Buf  = year__real
			month_Buf = int(  msg.split("/")[0] )
			day_Buf   = int(  msg.split("/")[1] )
			hour_Buf  = int(  msg.split("/")[2] )
			mins_Buf  = int(  msg.split("/")[3] )
		else:
			# print( "%s-%d年%d月%d日%d:%d ??" % ( panType , year__real ,  int(  msg.split("/")[0] )  ,  int(  msg.split("/")[1] )   ,  int(  msg.split("/")[2] )  , int(  msg.split("/")[3] ))   )
			return ( "Error" , "%d年%d月%d日%02d:%02d ??" % ( year__real ,  int(  msg.split("/")[0] )  ,  int(  msg.split("/")[1] )   ,  int(  msg.split("/")[2] )  , int(  msg.split("/")[3] ))   )

	# 2023,5,14,3,59
	if ( len( msg.split("/")) == 5 ):
		if int(  msg.split("/")[0] ) < 999:
			addYear = 1911
		else:
			addYear = 0

		if ((  msg.split("/")[0].isdigit() == True ) and (  msg.split("/")[1].isdigit() == True ) and (  msg.split("/")[2].isdigit() == True ) and (  msg.split("/")[3].isdigit() == True )  and (  msg.split("/")[4].isdigit() == True )  and ( 1 <= int(msg.split("/")[1]) <= 12 ) and ( 1 <= int(msg.split("/")[2]) <= calendar.monthrange(   int(msg.split("/")[0])+addYear  ,  int(msg.split("/")[1])  )[1] )  and (  0 <= int(msg.split("/")[3]) <= 23) and ( 0 <= int(msg.split("/")[4]) <= 60 )):
			# 民國
			if int(  msg.split("/")[0] ) < 999:
				# mainData = pageMainClass( panType , year = int(  msg.split("/")[0] )+1911 , month = int(  msg.split("/")[1] )  , day = int(  msg.split("/")[2] ) , hour = int(  msg.split("/")[3] )  , mins = int(  msg.split("/")[4] ) )
				year_Buf  = int(  msg.split("/")[0] )+1911
				month_Buf = int(  msg.split("/")[1] )
				day_Buf   = int(  msg.split("/")[2] )
				hour_Buf  = int(  msg.split("/")[3] )
				mins_Buf  = int(  msg.split("/")[4] )				
				# print("5A")
			# 西元
			else:
				# mainData = pageMainClass( panType , year = int(  msg.split("/")[0] ) , month = int(  msg.split("/")[1] )  , day = int(  msg.split("/")[2] ) , hour = int(  msg.split("/")[3] )  , mins = int(  msg.split("/")[4] ) )
				year_Buf  = int(  msg.split("/")[0] )
				month_Buf = int(  msg.split("/")[1] )
				day_Buf   = int(  msg.split("/")[2] )
				hour_Buf  = int(  msg.split("/")[3] )
				mins_Buf  = int(  msg.split("/")[4] )
				# print("5B")
		else:
			return ( "Error" , "%d年%d月%d日%02d:%02d ??" % (  int(  msg.split("/")[0]) , int(  msg.split("/")[1]) ,int(   msg.split("/")[2]) , int(  msg.split("/")[3]) , int(  msg.split("/")[4]) ) )

	print( year_Buf,month_Buf,day_Buf,hour_Buf,mins_Buf  ) 
	# print( )
	return  "%d/%02d/%02d/%02d/%02d"%( year_Buf,month_Buf,day_Buf,hour_Buf,mins_Buf  ) 






















def PPPPP ( currentTime = "" , dayMode = "" , index = "" , runtime = 24 ): # runtime為跑出幾條

	# currentTime = "2023/5/17/12/00" ## 格式完整
	# currentTime ="2023/5/17/"     --> "2023/5/17/00/00" #補上後面的 00/00
	# currentTime ="2023/5/17/15"  --> "2023/5/17/15/00" #補上後面的 00/00
	# format_time = lambda s: "/".join((s.split("/") + ["00", "00"])[:5])
	# print( "CTT")
	# print(currentTime)

	currentTime = (currentTime.replace("  "," ")
		.replace("  "," ")
		.replace(",","/")
		.replace(" ","/")
		.replace(".","/")
		.replace("-","/")        # ✅ 加上這一行
		# .replace("時盤","時")
		# .replace("刻盤","刻"))
		)
	if currentTime:
		format_time = lambda s: "/".join((s.strip("/").split("/") + ["00", "00"])[:5])
		currentTime = format_time(currentTime)  # 把結果存回去
	dayMode = dayMode.lower()
	import datetime
	timeList = []
	# print( currentTime )
	nowTime = checkMsgFun( currentTime ) ## 不輸入則取現時，輸入方式同起盤
	# ('時盤', '2023/05/13/02/26')
	# print( nowTime )

	inDate = nowTime ##'2023/05/13/02/26'

	inDateHour = int(inDate.split("/")[-2])
	inDateMin  = int(inDate.split("/")[-1]	)
# timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[,
# hours[, weeks]]]]]]])

	dt = datetime.datetime.strptime( inDate , "%Y/%m/%d/%H/%M")
	out = ( dt + datetime.timedelta( minutes = int(inDateMin)*-1 )).strftime("%Y/%m/%d/%H/%M")  # 2023/05/01/03/37 -> 2023/05/01/03/00

	inDate = out


	if inDateHour%2 == 0:
		dt = datetime.datetime.strptime( inDate , "%Y/%m/%d/%H/%M")
		out = ( dt + datetime.timedelta( hours= -5 )).strftime("%Y/%m/%d/%H/%M") # 本為減一，但會從下一時辰開始算，對照不易，所以改為減三(早一時辰)
		inDate = out
	else:
		dt = datetime.datetime.strptime( inDate , "%Y/%m/%d/%H/%M")
		out = ( dt + datetime.timedelta( hours= -4 )).strftime("%Y/%m/%d/%H/%M")
		inDate = out

	if (dayMode == "d") or (dayMode == "jc"): ## 日 或 節氣
		dt = datetime.datetime.strptime( inDate , "%Y/%m/%d/%H/%M")		# 把起點提前一天
		out = ( dt + datetime.timedelta( days=-1 )).strftime("%Y/%m/%d/%H/%M")
		inDate = out	

	if dayMode == "m":
		dt = datetime.datetime.strptime( inDate , "%Y/%m/%d/%H/%M")		# 把起點提前一天 // 只輸出年月柱  '癸卯-癸亥'
		out = ( dt + datetime.timedelta( days=-30 )).strftime("%Y/%m/%d/%H/%M") 
		inDate = out	



# in_date = '2023-3-31-22-50'
	fp_buf = getFourPillar( inDate ,  True  )
	# print( fp_buf )
 #                         # ('時盤', '2022/12/22/17/13')
	# for each in range( runtime ):
	add = 0
	while True:
		dt = datetime.datetime.strptime( inDate , "%Y/%m/%d/%H/%M")

		if dayMode == "h": ## 四柱全部出現模式，每個進程為一時辰(hours=2)  '2025/04/09/15:00'
			out = ( dt + datetime.timedelta( hours=2 )).strftime("%Y/%m/%d/%H/%M")

		if (dayMode == "d") or (dayMode == "jc"):  ## 年，月，日柱模式，每個進程為一天( days=1 )  '2025/04/09/15:00'
			out = ( dt + datetime.timedelta( days=1 )).strftime("%Y/%m/%d/%H/%M")



		# if dayMode == "jc":  ## 節氣模式，每個進程約15天，但因天數不固定，則用日來跑，跑到有節氣當日出現才加一( days=1 )  '2025/04/09/15:00'
		# 	out = ( dt + datetime.timedelta( days=1 )).strftime("%Y/%m/%d/%H/%M")



		if dayMode == "m":  ## 年，月柱模式，每個進程跳一個月柱 ( 約30天 )  ['乙巳-辛巳', '2025/05/05']
			out = ( dt + datetime.timedelta( days= 1 )).strftime("%Y/%m/%d/%H/%M")
			nowMonth = getFourPillar( out ,  True  )[2][1] ## 取得月柱
			for foo in range( 1,50):
				out = ( dt + datetime.timedelta( days= foo )).strftime("%Y/%m/%d/%H/%M")
				if nowMonth != getFourPillar( out ,  True  )[2][1] :
					# print (  nowMonth , getFourPillar( out ,  True  )[2][1] , getFourPillar( out ,  True  )[2]  )
					break




		inDate = out
		# print( inDate)
		fp_buf = getFourPillar( inDate ,  True  )
	 #                         # ('時盤', '2022/12/22/17/13')
		# print( fp_buf )	 
		# ('2026/3/26/23:00', '二月初八', ['丙午', '辛卯', '庚子', '丙子'], ['春分', '>', '清明'], '(四)', '23:00')

		lightDate  = fp_buf[0] ## 陽曆日期時間 '2026/3/27/23:00'
		fourPillar = fp_buf[2] ## 農曆日期 '二月初九'

		jeChi_buf =  fp_buf[3][0] if fp_buf[3][1] == '!' else ''	## 節氣
			
		week       = fp_buf[4] ## '(四)'


		if (dayMode == "d") or (dayMode == "jc"):
			fourPillar = fourPillar[:-1]
			lightDate  = lightDate[:-6]

		elif dayMode == "m":
			fourPillar = fourPillar[:-1]
			lightDate  = lightDate[:-6]

		# elif dayMode == "jc":
		# 	if jeChi_buf:
		# 		fourPillar = fourPillar[:-1]
		# 		lightDate  = lightDate[:-6]
		# 		eachList = [ '-'.join(fourPillar)  , lightDate  , jeChi_buf ]
		# 	else:
		# 		continue

		eachList = [ '-'.join(fourPillar)  , lightDate , week  , jeChi_buf ]
		# print( eachList) 
		# ['乙巳-辛巳-庚寅', '2025/05/21', '小滿'] 年月日柱，陽曆，陰曆, 節氣

		if len(timeList) > runtime:
			break

		if index != "":
			if index in " ".join(eachList):
				# print( " ".join(eachList))
				timeList.append( eachList )

		elif dayMode == "jc":
			# print( eachList )
			if jeChi_buf:
				timeList.append( eachList )
		else:
			timeList.append( eachList )

			# if (index == "節氣") or (index.lower() == "jc") or (index.lower() == "jechi"):

	# ['乙巳-甲申-戊申', '2025/08/07', '立秋']
	return timeList









# def getYear ( pillarYear ):
# 	yearBuf = None
# 	for yGZ in  ganZhi_Dict.keys():
# 		if ganZhi_Dict[yGZ] == pillarYear:
# 			# print ( "year:" , yGZ + 1983 )
# 			yearBuf = yGZ + 1983
# 			# 找出年干支所在的西元年
# 			return yearBuf


def getYearGZ ( year ):

	for each in ganZhi_Dict.keys():
		# print(each,year)
		checkYear = ( year -1983 )%60
		if checkYear == 0:
			checkYear = 60
					
		if each == checkYear:
			return ganZhi_Dict[each]



# 從干支或年份取得該年資料
# checkYear( 1971 )
# [1971, '辛亥', '豬', 1911, 1971, 2031]
# checkYear( 戊戌 )
# [2018, '戊戌', '狗', 1958, 2018, 2078]
# def checkYear ( yearGZ = "" , basicYear = ""):
def checkYear ( yearData = "" ):
	import calendar,datetime
	from datetime import datetime,timezone,timedelta
	ZhiList = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
	GanList = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
	dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
	localtimeReal = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
	year__real =  localtimeReal.year #取得現在的年

	## 年干支
	yearGZ = "" 
	## 年份 
	basicYear = ""

	if yearData.isdigit():  
		# 如果全是數字，判斷為西元年份
		basicYear = int(yearData)
		print("西元年:", basicYear)

	elif any(g in yearData for g in GanList) and any(z in yearData for z in ZhiList):
		# 如果同時包含天干和地支，判斷為干支
		yearGZ = yearData
		print("干支:", yearGZ)

	else:
		print("❌ 格式不正確:", yearData)


	if yearGZ != "":
		basicYear = getYear( yearGZ )
	else:
		# print(basicYear)
		basicYear = int(basicYear)
		if basicYear < 999:
			basicYear += 1911 # 民國轉西元
		# basicYear = year 

		yearGZ = getYearGZ( basicYear )
	if basicYear == None:
		return None

	animalType = ShX [ Zhi.index( yearGZ[-1] )]
	# print(basicYear)
	# print( animalType )
	yearList = [ basicYear , yearGZ ]
	yearList.append(animalType)
	# if getYear( yearGZ ) >= year__real:
	if (abs(getYear( yearGZ ) - year__real) < 40) or (getYear( yearGZ ) > year__real):
		yearList.append(basicYear-60 )
		yearList.append(basicYear )
		yearList.append(basicYear+60 )

	elif getYear( yearGZ ) < year__real:
		print( basicYear , basicYear+60 ,basicYear+120)	
		yearList.append(basicYear)
		yearList.append(basicYear+60 )
		yearList.append(basicYear+120 )

	return yearList



if __name__ == '__main__':

	# getList = PPPPP ( dayMode = "節氣" , index = "" ,runtime = 10 )
	# for i in getList:
	# 	print(i)	


	# print( getNowTime() )


	# print( checkYear (   "1971"))
	# print()
	# print( checkYear (  "戊戌" ))
	# print()
	# print(getFourPillar( fullDate = "2020/12/30/03/00" , detail = False ))
	# print()
	# print(fourPillarToDateMain( inputDate ="乙巳,辰月,庚戌,申"))

	PPPPP ( currentTime = "2025-09-15" )
	# fourPillarToDateMain( inputDate ="庚子,甲申,乙未,丁丑"  )
	# getNowTime()

	# # print( getFourPillar( fullDate = "2023/2/8/12/58" , detail = True ))
	# print( getFourPillar(  detail = True ))
	# # ('2025/04/11/16:57', '三月十四', ['乙巳', '庚辰', '庚戌', '甲申'], ['清明', '>', '穀雨'], '(五)', '16:57')
	# print( getFourPillar(  detail = False ))
	# # ['乙巳', '庚辰', '庚戌', '甲申']


	# print( checkYear( "乙丑"))

	# print(checkYear ( "1985"))
	# [1985, '乙丑', '牛', 1985, 2045, 2105, '金', '五行屬海中金，海內之牛。乙丑年出生的人，非常得慷慨大方，喜愛春風，見事則多學少成，幼災父母，九流中人，夫妻無刑，兒女不孤，六親少靠，乃是賢良、純和之命。']
	



	# 由四柱取得西元年月日時
	# >inputDate 2022/01/01/01/00
	# print( fourPillarToDateMain( inputDate ="乙巳,庚辰,庚戌,甲申"))
	# print( fourPillarToDateMain())
	# 2020/08/20/01/00
		# ['乙巳', '庚辰', '庚戌', '甲申']
		# 2025/04/11/15/00

