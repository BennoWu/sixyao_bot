
# http://www.ifuun.com/a2020060525094850/
# https://for621.pixnet.net/blog/post/269728244



# 大安

# 身未動時，屬木青龍．謀事一五七，貴人西南，沖犯東方，大人青面陰神，小孩婆祖六畜驚。

# 解曰：大安事事昌，求財在坤方，失物去不遠，宅舍保安康，

# 　　　行人身未動，病者主無妨，將軍回田野，仔細更推詳。


# 玥灃解﹕

# 卜到大安，屬吉卦，凡事都可以得到安康，但是此為靜卦，宜靜不宜動。

# 問運勢﹕目前運勢還不錯，有穩定成長的情況，但不宜躁進。

# 問財富﹕求財可，但是目前不宜擴張，只能夠守住舊業。

# 問感情﹕若為女子問則好，感情順遂。若為男子問則較差，感情雖穩，但是以無新鮮感，會出現點小問題。

# 問事業﹕目前工作穩定，可得上司賞識，但切勿鋒芒太露。

# 問身體﹕身體沒有大病，但須注意病由口入，或因過度操勞而得病。

# 問神鬼﹕大安為解災之神，鬼神之事問題不大，若是小孩為自身驚嚇所致，若是大人則為沖犯東方之煞神或犯土煞。

# 問行人﹕人平安，但目前不願與自身連絡。



gua_dict = {
	"大安" : { #"安靜,不動,平安"
		"show_type" : "解卦",
		"subTitle" :"身不動 | 失物行人,靜止不動,平安",
		# 身未動時．屬木青龍．謀事一五七（屬四肢）．
		# 貴人西南．沖犯東方．大人青面陰神．小孩婆祖六畜驚．

		"index" : "木",
		"luckType" : "大吉",
		"godType" : "青龍",
		"謀事" : "一五七",
		"斷辭" : "大安事事昌 求財在坤方 失物去不遠 宅舍保安康 行人身未動 病者主無妨 將軍回田野 仔細與推詳",
# 人平安，但目前不願與自身連絡。


		"尋物" : {
				"大安加大安" : "大安加大安 失物在家裡",
				"留連加大安" : "留連加大安 物在家中藏",
				"速喜加大安" : "速喜加大安 失物不丟失",
				"赤口加大安" : "赤口加大安 失物東北找",
				"小吉加大安" : "小吉加大安 失物自己出",
				"空亡加大安" : "空亡加大安 失物反覆間"
				},
		"日加時斷" : {
			"大安加大安" : None ,
			"留連加大安" : "留連加大安,辦事兩分張,婚姻有喜事,先苦後來甜",
			"速喜加大安" : "速喜加大安,事事都平安,姻姻成全了,占病都相安",
			"赤口加大安" : "赤口加大安,辦事險和難,失物東北找,婚姻指定難",
			"小吉加大安" : "小吉加大安,事事兩周全,婚姻當日定,失物自己損",
			"空亡加大安" : "空亡加大安,事事不周全,婚姻從和好,失物反覆間"
		}
	},

	"留連" : { #"遲滯,膠著,曖昧,不樂觀,不順利"
		"show_type" : "解卦",
		"subTitle" :"卒未歸 | 時機未到,凡事暫緩,失物未遠",
		# 卒未歸時．屬水元武．謀事二八十（屬腎胃）．
		# 貴人南方．沖犯北方．大人烏面夫人．小孩遊路亡魂．



		"index" : "水",
		"luckType" : "小凶",
		"godType" : "玄武",
		"謀事" : "二八十",
		"斷辭" : "留連事難成 求謀日未明 官事只宜緩 去者未回程 失物南方見 急討方稱心 更須防口舌 人口只平平",
# 人平安，但目前仍流連忘返。


		"尋物" : {
				"大安加留連" : "大安加留連 失物西北去",
				"留連加留連" : "留連加留連 失物落在南",
				"速喜加留連" : "速喜加留連 失物無信息",
				"赤口加留連" : "赤口加留連 失物不回還",
				"小吉加留連" : "小吉加留連 失物上西南",
				"空亡加留連" : "空亡加留連 失物永不還"
				},
		"日加時斷" : {
			"留連加留連" : None ,
			"大安加留連" : "大安加留連,辦事不周全,失物西北去,婚姻晚幾天",
			"速喜加留連" : "速喜加留連,婚姻不可言,失物無信息,病人有仙緣",
			"赤口加留連" : "赤口加留連,辦事有困難,行人在外走,失物不回還",
			"小吉加留連" : "小吉加留連,事事有反還,婚姻有人破,失物上西南",
			"空亡加留連" : "空亡加留連,辦事處處難,婚姻重新定,失物永不還"
		}
	},

	"速喜" : { #"歡樂,喜慶,快速"
		"show_type" : "解卦",
		"subTitle" :"人便至 | 時機已到,刻不容緩,速辦成功",

		# 人便至時．屬火未雀．謀事三六九（屬心腦）．
		# 貴人西南．沖犯南方．大心火箭將軍．小孩婆祖動物驚．



		"index" : "火",
		"luckType" : "中吉",
		"godType" : "朱雀",
		"謀事" : "三六九",
		"斷辭" : "速喜喜來臨 求財向南行 失物申午未 逢人路上尋 官事有福德 病者無禍侵 田宅六蓄吉 行人有信音",
# 人已經快到了。


		"尋物" : {
				"大安加速喜" : "大安加速喜 失物當日見",
				"留連加速喜" : "留連加速喜 失物三天裡",
				"速喜加速喜" : "速喜加速喜 失物落正南",
				"赤口加速喜" : "赤口加速喜 失物有著落",
				"小吉加速喜" : "小吉加速喜 失物在院裡",
				"空亡加速喜" : "空亡加速喜 失物在家裡"
				},
		"日加時斷" : {
			"速喜加速喜" : None ,
			"大安加速喜" : "大安加速喜,事事自己起,失物當日見,婚姻自己提",
			"留連加速喜" : "留連加速喜,事事由自己,婚姻有成意,失物三天裡",
			"赤口加速喜" : "赤口加速喜,婚姻在自己,失物有著落,辦事官事起",
			"小吉加速喜" : "小吉加速喜,事事從頭起,婚姻能成就,失物在院裡",
			"空亡加速喜" : "空亡加速喜,事事怨自己,婚姻有一定,失物在家裡"
		}
	},

	"赤口" : { #"磕碰,口舌,衝突"
		"show_type" : "解卦",
		"subTitle" :"官事凶 | 口舌是非,主事不利,辦事宜緩",

		# 官事凶時．屬金白虎．謀事四七十（屬肺胃）．
		# 貴人東方．沖犯西方．大人金神七煞．小孩迷魂童子．


		"index" : "金",
		"luckType" : "中凶",
		"godType" : "白虎",
		"謀事" : "四七十",
		"斷辭" : "赤口主口舌 官非切要防 失物速速討 行人有驚慌 六畜多作怪 病者出西方 更須防詛咒 誠恐染瘟肓",
# 所問之人目前有困難或者有事情糾纏。


		"尋物" : {
				"大安加赤口" : "大安加赤口 失物不用找",
				"留連加赤口" : "留連加赤口 失物準丟失",
				"速喜加赤口" : "速喜加赤口 失物往正北",
				"赤口加赤口" : "赤口加赤口 失物正西找",
				"小吉加赤口" : "小吉加赤口 失物丟了手",
				"空亡加赤口" : "空亡加赤口 失物往遠走"
				},
		"日加時斷" : {
			"赤口加赤口" : None,
			"大安加赤口" : "大安加赤口,辦事不順手,失物不用找,婚姻兩分手",
			"留連加赤口" : "留連加赤口,病者死人口,失物準丟失,婚姻兩分手",
			"速喜加赤口" : "速喜加赤口,自己往外走,失物往正北,婚姻得勤走",
			"小吉加赤口" : "小吉加赤口,辦事往外走,婚姻有難處,失物丟了手",
			"空亡加赤口" : "空亡加赤口,辦事官非有,婚姻難定准,失物往遠走"
		}
	},

	"小吉" : {
		"show_type" : "解卦",
		"subTitle" :"人來喜 | 喜事到來,辦事吉利,成功在望",

		# 人來喜時．屬水六合．謀事一五七（屬肝腸）．
		# 貴人西南．沖犯東方．大人無主家神．小孩婆祖六畜驚．


		"index" : "水",
		"luckType" : "小吉",
		"godType" : "六合",
		"謀事" : "一五七",
		"斷辭" : "小吉最吉昌 路上好商量 陰人來報喜 失物在坤方 行人即便至 交關甚是強 凡事街合和 病者叩穹蒼",
		"尋物" : {
				"大安加小吉" : "大安加小吉 失物不出門",
				"留連加小吉" : "留連加小吉 失物東南去",
				"速喜加小吉" : "速喜加小吉 失物在家裡",
				"赤口加小吉" : "赤口加小吉 失物無信息",
				"小吉加小吉" : "小吉加小吉 失物在西南",
				"空亡加小吉" : "空亡加小吉 失物回家裡"
				},
		"日加時斷" : {
			"小吉加小吉" : None,
			"大安加小吉" : "大安加小吉,事事從己及,失物不出門,婚姻成就地",
			"留連加小吉" : "留連加小吉,事事不用提,失物東南去,病者出人齊",
			"速喜加小吉" : "速喜加小吉,婚姻有人提,病人當天好,時物在家裡",
			"赤口加小吉" : "赤口加小吉,辦事自己提,婚姻不能成,失物無信息",
			"空亡加小吉" : "空亡加小吉,事事有猜疑,婚姻有喜事,失物回家裡"
		}
	},

	"空亡" : {
		"show_type" : "解卦",
		"subTitle" :"信音稀 | 查無音信,難有結果,辦事無成",

		# 音信稀時．屬土勾陳．主事三六九（屬脾腦）．
		# 貴人北方．沖犯厝地．大人土壓夫人．小孩土瘟神煞．


		"index" : "土",
		"luckType" : "大凶",
		"godType" : "勾陳",
		"謀事" : "三六九",
		"斷辭" : "空亡事不祥 陰人少乖張 求財無利益 行人有災殃 失物尋不見 官事有刑傷 病人逢暗鬼 解禳保平安",
# 人在途中遇到困難或災厄而難到。
		"尋物" : {
				"大安加空亡" : "大安加空亡 失物無蹤影",
				"留連加空亡" : "留連加空亡 失物不見面",
				"速喜加空亡" : "速喜加空亡 失物不久見",
				"赤口加空亡" : "赤口加空亡 失物不用找",
				"小吉加空亡" : "小吉加空亡 失物正東找",
				"空亡加空亡" : "空亡加空亡 失物尋不見"
				},
		"日加時斷" : {
			"空亡加空亡" : None,		
			"大安加空亡" : "大安加空亡,病人要上床,失物無蹤影,事事不順情",
			"留連加空亡" : "留連加空亡,病人準死亡,失物不見面,婚姻兩分張",
			"速喜加空亡" : "速喜加空亡,婚姻有分張,病者積極治,失物不久見",
			"赤口加空亡" : "赤口加空亡,無病也上床,失物不用找,婚姻不能成",
			"小吉加空亡" : "小吉加空亡,病人不妥當,失物正東找,婚姻再想想"
		}
	}
}

# https://vocus.cc/article/63a6db7dfd897800013450e8
# 用id數字取得項目的內容
def getGridData( dayItem , hourItem ):
	for each in gua_dict.keys():
		if  each == hourItem:
			return gua_dict[each]["日加時斷"][dayItem + "加" + hourItem]






def sLouZan_fun():
	import  sxtwl
	import calendar,datetime
	from datetime import datetime,timezone,timedelta
	# 天干
	Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
	# 地支
	Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
	# 星期
	WeekCn = ["(日)", "(一)", "(二)", "(三)", "(四)", "(五)", "(六)"]
	dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
	localtimeReal = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區

	nowYear  = localtimeReal.year  		# 取得年
	nowMonth = localtimeReal.month 		# 取得月
	nowDay   = localtimeReal.day   		# 取得日
	nowHour  = localtimeReal.hour  		# 取得小時
	nowMins  = localtimeReal.minute		# 取得分鐘

	# 從公歷年月日獲取一天的信息
	day = sxtwl.fromSolar( nowYear ,  nowMonth , nowDay ) 
	week = WeekCn[day.getWeek()]

	lightDate = "陽曆: %d年%d月%d日%s %02d:%02d" % (day.getSolarYear(), day.getSolarMonth(), day.getSolarDay(),week ,nowHour , nowMins  )
	# 陽曆: 2023年6月27日(二) 09:19

	darkDate = "陰曆: %d年%s%d月%d日" % (day.getLunarYear(), 
	    '閏' if day.isLunarLeap() else '', day.getLunarMonth(), day.getLunarDay())

	sTG = day.getHourGZ(nowHour)
	# print("%d時的干支"%(nowHour, ), Gan[sTG.tg] + Zhi[sTG.dz]) 

	#年干支
	yTG = day.getYearGZ()
	# print("年干支", Gan[yTG.tg] + Zhi[yTG.dz]) 

	#月干支
	mTG = day.getMonthGZ()
	# print("月干支", Gan[mTG.tg] + Zhi[mTG.dz]) 

	#日干支
	dTG  = day.getDayGZ()
	# print("日干支", Gan[dTG.tg] + Zhi[dTG.dz])

	sTG = day.getHourGZ( nowHour )
	# print("%d時的干支"%(hour, ), Gan[sTG.tg] + Zhi[sTG.dz]) 

	yGanZhi = Gan[yTG.tg] + Zhi[yTG.dz]                           # 年干支
	mGanZhi = Gan[mTG.tg] + Zhi[mTG.dz]                           # 月干支
	dGanZhi = Gan[dTG.tg] + Zhi[dTG.dz]                           # 日干支
	sGanZhi = Gan[sTG.tg] + Zhi[sTG.dz]     
	pillarList = [yGanZhi , mGanZhi,  dGanZhi,  sGanZhi ]   

	print( lightDate )
	print( darkDate )
	print( "%s|%s|%s|%s" % ( yGanZhi , mGanZhi,  dGanZhi,  sGanZhi ) )

	monthBuf  = day.getLunarMonth() # 月
	dayBuf    = day.getLunarDay() # 日
	hourBuf   = Zhi.index( Zhi[sTG.dz] )+1  # 第幾個時辰


	print( "%s,%s,%s "%( monthBuf , dayBuf , hourBuf))
	print( getGodData( monthBuf , dayBuf , hourBuf , date = True ))



# 報三個數字
def getGodData( oneNumBuf =0 , twoNumBuf =0 , threeNumBuf =0 , date = False ):
	if date == True:
		print( ">>>>%s,%s,%s "%( oneNumBuf , twoNumBuf , threeNumBuf))
	else:

		if oneNumBuf != 0:
			print(oneNumBuf)
		if twoNumBuf != 0:
			print(twoNumBuf)
		if threeNumBuf != 0:
			print(threeNumBuf)

	stepName = [ "大安","留連","速喜","赤口","小吉","空亡" ]

	if oneNumBuf  == 0:
		oneNum = oneNumBuf % 6
	else:
		oneNum = oneNumBuf % 6-1
	print( oneNum, stepName [  oneNum ]  )

	if twoNumBuf  == 0:
		twoNum = twoNumBuf % 6
	else:
		twoNum = twoNumBuf % 6-1
	print( twoNum , stepName [  oneNum + twoNum ]  )

	if threeNumBuf  == 0:
		threeNum = threeNumBuf % 6
	else:
		threeNum = threeNumBuf % 6-1
	# print( threeNum ,oneNum + twoNum+ threeNum )	
	print( threeNum , stepName [ ( oneNum + twoNum+ threeNum )%6]  )



	monthItem = stepName [  oneNum ]                      # 月 
	dayItem   = stepName [  oneNum + twoNum ]             # 日
	hourItem  = stepName [  ( oneNum + twoNum+ threeNum )%6 ]   # 時

	print( monthItem,dayItem ,hourItem )
	totalDateTime  = "%s月/%s日/%s時"% (oneNumBuf,twoNumBuf ,threeNumBuf)  # 小吉月/大安日/留連時



	print( luckType,godBeast,number,subTitle,find_lost,mainData)
	return luckType,godBeast,number,subTitle,find_lost,mainData










def getDateTime_fun():
	import  sxtwl
	import calendar,datetime
	from datetime import datetime,timezone,timedelta


	from datetime import datetime,timezone,timedelta
	# dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)  # 舊版修改
	dt1 = datetime.now(timezone.utc)
	localtimeReal = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區 ( 大陸，台灣，東8區，日本，東9區)


	# 天干
	Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
	# 地支
	Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
	# 星期
	WeekCn = ["(日)", "(一)", "(二)", "(三)", "(四)", "(五)", "(六)"]


	nowYear  = localtimeReal.year  		# 取得年
	nowMonth = localtimeReal.month 		# 取得月
	nowDay   = localtimeReal.day   		# 取得日
	nowHour  = localtimeReal.hour  		# 取得小時
	nowMins  = localtimeReal.minute		# 取得分鐘

	# 從公歷年月日獲取一天的信息
	day = sxtwl.fromSolar( nowYear ,  nowMonth , nowDay ) 
	week = WeekCn[day.getWeek()]

	lightDate = "陽曆:%d年%d月%d日%s" % (day.getSolarYear(), day.getSolarMonth(), day.getSolarDay(),week  )
	# 陽曆: 2023年6月27日(二) 09:19
	timeNow = "%02d:%02d" % ( nowHour , nowMins )

	darkDate = "陰曆:%d年%s%d月%d日" % (day.getLunarYear(), 
	    '閏' if day.isLunarLeap() else '', day.getLunarMonth(), day.getLunarDay())

	sTG = day.getHourGZ(nowHour)
	# print("%d時的干支"%(nowHour, ), Gan[sTG.tg] + Zhi[sTG.dz]) 

	#年干支
	yTG = day.getYearGZ()
	# print("年干支", Gan[yTG.tg] + Zhi[yTG.dz]) 

	#月干支
	mTG = day.getMonthGZ()
	# print("月干支", Gan[mTG.tg] + Zhi[mTG.dz]) 

	#日干支
	dTG  = day.getDayGZ()
	# print("日干支", Gan[dTG.tg] + Zhi[dTG.dz])

	sTG = day.getHourGZ( nowHour )
	# print("%d時的干支"%(hour, ), Gan[sTG.tg] + Zhi[sTG.dz]) 

	yGanZhi = Gan[yTG.tg] + Zhi[yTG.dz]                           # 年干支
	mGanZhi = Gan[mTG.tg] + Zhi[mTG.dz]                           # 月干支
	dGanZhi = Gan[dTG.tg] + Zhi[dTG.dz]                           # 日干支
	sGanZhi = Gan[sTG.tg] + Zhi[sTG.dz]     
	pillarList = [yGanZhi , mGanZhi,  dGanZhi,  sGanZhi ]   

	print( lightDate )
	print( darkDate )
	print( "%s|%s|%s|%s" % ( yGanZhi , mGanZhi,  dGanZhi,  sGanZhi ) )
	main_gnaZhi =  "%s|%s|%s|%s" % ( yGanZhi , mGanZhi,  dGanZhi,  sGanZhi )


	monthBuf  = day.getLunarMonth() # 月
	dayBuf    = day.getLunarDay() # 日
	hourBuf   = Zhi.index( Zhi[sTG.dz] )+1  # 第幾個時辰


	fullDate = "%d/%02d/%02d %02d:%02d"%( nowYear,nowMonth,nowDay,nowHour,nowMins  ) 

	# print( "%s,%s,%s "%( monthBuf , dayBuf , hourBuf))
	return ( lightDate, darkDate,timeNow, main_gnaZhi ,fullDate ,monthBuf,dayBuf,hourBuf )




# 報三個數字
def sSixZmain( oneNumBuf =0 , twoNumBuf =0 , threeNumBuf =0  ):
	print( ">>>>%s,%s,%s "%( oneNumBuf , twoNumBuf , threeNumBuf))
	fullDateBuf = ""
	## 如果沒有自行輸入時
	if (oneNumBuf ==0) and (twoNumBuf == 0 ) and (threeNumBuf == 0):
		getTimeBuf = getDateTime_fun()
		print( getTimeBuf )
		fullDateBuf = getTimeBuf[-4]
		oneNumBuf = getTimeBuf[-3]
		twoNumBuf =getTimeBuf[-2]
		threeNumBuf = getTimeBuf[-1]
		print( ">>>>%s,%s,%s "%( oneNumBuf , twoNumBuf , threeNumBuf ))



	stepName = [ "大安","留連","速喜","赤口","小吉","空亡" ]

	finalNumberList = []

	if oneNumBuf  == 0:
		oneNum = oneNumBuf % 6  # 手動給值
	else:
		oneNum = oneNumBuf % 6-1 # 時辰給值
		hourItem = stepName [  oneNum ] 
	# print( oneNum, stepName [  oneNum ]  )
	finalNumberList.append( stepName [  oneNum ]  )


	if twoNumBuf  == 0:
		twoNum = twoNumBuf % 6  # 手動給值
	else:
		twoNum = twoNumBuf % 6-1 # 時辰給值
		dayItem = stepName [  (oneNum + twoNum)%6] 
		hourItem = stepName [  (oneNum + twoNum)%6 ] 
		# print( twoNum , stepName [  (oneNum + twoNum)%6 ]  )
		finalNumberList.append( stepName [  (oneNum + twoNum)%6 ]  )
	if threeNumBuf  == 0:
		threeNum = threeNumBuf % 6  # 手動給值
	else:
		threeNum = threeNumBuf % 6-1 # 時辰給值
	# print( threeNum ,oneNum + twoNum+ threeNum )	
		hourItem = stepName [ ( oneNum + twoNum+ threeNum )%6]
		# print( threeNum , stepName [ ( oneNum + twoNum+ threeNum )%6]  )
		finalNumberList.append( stepName [  ( oneNum + twoNum+ threeNum )%6 ]  )


	mainData = gua_dict[hourItem]["斷辭"] # 主要結果
	number =  gua_dict[hourItem]["謀事"] 	 # 三六九
	find_lost =  gua_dict[hourItem]["尋物"][ dayItem + "加"+ hourItem] 	 # 三六九


	# print (finalNumberList)
	# print( "大標: " ,gua_dict[hourItem]["subTitle"])
	# print ( "卦詞: " , mainData )

	return ( finalNumberList, gua_dict[hourItem]["subTitle"] , mainData  ,fullDateBuf )
	# print ( "================================================================" )
	# print (  hourItem )
	# print( "大標: " ,gua_dict[hourItem]["subTitle"])
	# print( "五行: " ,gua_dict[hourItem]["index" ])
	# print( "運勢: " ,gua_dict[hourItem]["luckType" ])
	# print( "六神: " ,gua_dict[hourItem]["godType" ])
	# print ( "數字: ", number )
	# print ( "卦詞: " , mainData )
	# print ( "尋物: " , find_lost)


if __name__ == '__main__':
	# sLouZan_fun()
	# getGodData( 8,25 )
	# print( getDateTime_fun() )
	print(sSixZmain(   ))

