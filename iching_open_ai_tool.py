
# 建立 OpenAI client

import re,os
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()  # 載入 .env 檔案


openAiKey = os.environ.get('OPENAI_API_KEY')
client = OpenAI( api_key = openAiKey )





# client = OpenAI(api_key="你的_API_KEY")

# resp = client.chat.completions.create(
#     model="gpt-4.1-mini",
#     messages=[
#         {"role": "system", "content": "你是冷靜的工程助理"},
#         {"role": "user", "content": "用一句話解釋什麼是容積率"}
#     ]
# )

# print(resp.choices[0].message.content)



# PUNCT_TABLE 用來把全形標點轉半形
PUNCT_TABLE = str.maketrans({
    '，': ',', '。': '.', '：': ':', '；': ';', '！': '!', '？': '?',
    '（': '(', '）': ')', '【': '[', '】': ']', '『': '[', '』': ']'
})

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

def solve_iching(base_name, change_name=None, homeMeaning=None, changeMeaning=None):
    short_base = get_short_name(base_name)
    
    if change_name:
        short_change = get_short_name(change_name)
        prompt = f"""
請以中性、客觀的易經老師的視角描述卦象，扁平俐落，少用現代用詞，精簡約110字。
重點描述卦象的狀態與變化過程，不涉及心理、人物或主觀評價。
開頭必須明確說明「本卦」與「變卦」，例如「本卦{base_name}，變卦{change_name}」，之後只陳述事物的演變。
解說中不得使用「初現」「轉為」「呼應」「暗示」,修飾裝飾等主觀詞。
僅使用提供的卦名與意義，說明事物的進程與變化狀態。
禁止使用：
能量、分佈、系統、結構、特徵、建議、象徵、代表, 顯示,展現,流轉,修飾
科技冷硬詞：能量、分佈、系統、結構、特徵、動態、位移,裝飾,文飾
假掰修飾語：謙遜、誠懇、入理、象徵、暗示、建議、有利於、應如何。

卦名與象數：
本卦：{base_name}，意義：{homeMeaning}  
變卦：{change_name}，意義：{changeMeaning}  

請生成完整自然的解說文字：
"""

    else:
        prompt = f"""
請以誠懇、專業的易經老師身份解釋卦，文雅自然，略帶古文風，扁平俐落，精簡約110字。
重點描述卦象的狀態與變化過程，不涉及心理、人物或主觀評價。
開頭必須明確說明「本卦」與「變卦」，例如「本卦{base_name}，變卦{change_name}」，之後只陳述事物的演變。
解說中不得使用「初現」「轉為」「呼應」「暗示」等主觀詞。
僅使用提供的卦名與意義，說明事物的進程與變化狀態。
禁止使用：
能量、分佈、系統、結構、特徵、建議、象徵、代表, 顯示,展現,流轉
科技冷硬詞：能量、分佈、系統、結構、特徵、動態、位移,裝飾,文飾,修飾
假掰修飾語：謙遜、誠懇、入理、象徵、暗示、建議、有利於、應如何。


卦名與象數：
本卦：{base_name}，意義：{homeMeaning}  

請生成完整自然的解說文字：
"""


    try:
        resp = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "你是冷靜、專業的易經老師"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            # max_output_tokens=500
        )

        txt = resp.choices[0].message.content.strip()

        # 強制全形轉半形
        txt = txt.translate(PUNCT_TABLE)

        # # 用正則去掉最後出現的卦名
        # pattern = re.escape(short_base)
        # if change_name:
        #     pattern += r'之' + re.escape(short_change)
        # txt = re.sub(pattern + r'\s*$', '', txt)

        # if change_name:
        #     # 去掉最後出現的「巽之小畜卦」或類似卦名
        #     pattern = r'\s*' + re.escape(short_base) + r'之' + re.escape(short_change) + r'\s*$'
        # else:
        #     # 去掉最後出現的「巽卦」或類似卦名
        #     pattern = r'\s*' + re.escape(short_base) + r'\s*$'

        # txt = re.sub(pattern, '', txt)
        # print (short_base + "之" + short_change + "卦" )
        # txt = txt.replace( short_base + "之" + short_change + "卦" , "" )

        # # print ( txt )








        return txt.strip()
    except Exception as e:
        return f"分析時發生錯誤: {str(e)}"




if __name__ == '__main__':


    result = solve_iching(
        base_name="火澤睽",
        change_name="地水師",
        homeMeaning="修飾、文飾。山下有火,裝飾外表,但不宜過度虛飾。",
        changeMeaning="家庭、內政。風自火出,治家有道,內部穩定。"
    )

    print(result )

