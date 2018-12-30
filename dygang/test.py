txt = """◎片　　名　在天堂等我<br>
◎年　　代　2018<br>
◎产　　地　中国大陆<br>
◎类　　别　<a href="http://www.dygang.net/e/search/result/?searchid=176518" target="_blank" title="爱情片">爱情</a> / 灾难<br>
◎语　　言　汉语普通话<br>
◎字　　幕　中字<br>
◎上映日期　2018-11-30(中国大陆)<br>
◎片　　长　129分钟<br>
◎导　　演　王军<br>
◎编　　剧　王军 / 王劲松 Jingsong Wang<br>
◎主　　演　李滨 Bin Li<br>
　　　　　　于非非<br>
　　　　　　毛孩 Hai Mao<br>
　　　　　　李梦男 Mengnan Li<br>
　　　　　　肥龙 Helong Wang<br>
　　　　　　苇青 Qing Wei<br>
　　　　　　彭玉 Yu Peng<br>
　　　　　　马德华 Dehua Ma<br>
　　　　　　李勤勤 Qinqin Li<br>
　　　　　　刘伟 Wei Liu<br>
　　　　　　张洪杰 Hongjie Zhang<br>
　　　　　　苗苗 Miao Miao<br>
　　　　　　娜仁花 Renhua Na<br>
　　　　　　赵倩 Qian Zhao<br>
　　　　　　穆建荣 Jianrong Mu<br>
　　　　　　柏辰<br>
　　　　　　罗赞袭</p>"""

import re

m = re.search(r'片　　名 (.*?)<br>',txt)
if m:
    print(m.group(1))