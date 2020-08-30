# re.findall 的 api

"""

    re.finaall(pattern,string,flags=0)
        pattern --> 正则表达式
        string --> 匹配的字符串
        flags -- > 匹配模式

"""

import re

# falgs (re.DATALL re.S)
# rs = re.findall('a.c','a\nc')
# rs = re.findall('a.c','a\nc', flags=re.DOTALL)O


#  findall中分组的使用
"""
    当正则中出现()时就叫分组,此时正则只会匹配()里面的内容,()之外的正则内容的作用就是确定位置
    s = '430524200202162930'
    rs = re.findall('430524(\d{8})',s)
"""
# rs = re.findall('a.c','a\nc', flags=re.DOTALL)
# rs = re.findall('a(.+)c','a\nc', re.DOTALL)  


# print(rs)
