#导入模块
import re

# 字符匹配
# rs = re.findall('abc','adqwehwqueyqwehqehabc')

# . 匹配 --> ‘.’号不能匹配换行符，其他都可以匹配
# rs = re.findall('a.c','aec')

# / --> 转义符，去掉特殊含义
# rs = re.findall('a/.c','abc')

# [] --> 逐个匹配
# rs = re.findall('a[bd]c','abcdsadadadc')

# ^ --> 反转
# rs = re.findall('a[^bd]c','aacabcaccadc')

# \d --> 匹配数字[0-9]   \D --> 匹配非数字
# rs = re.findall('\d','0098jj')
# rs = re.findall('\D','0098jj')

# \s --> 匹配空白字符 \S --> 匹配非空白字符
# rs = re.findall('\s','12 43 kk &&& ^^')
# rs = re.findall('\S','12 43 kk &&& ^^')

# \w --> 匹配单词字符 \W --> 匹配非单词字符(匹配特殊字符) 单词字符[A-Za-z0-9_中文]
# rs = re.findall('\w', 'hellow^^')
# rs = re.findall("\W", 'hellow^^')


# 数量词 --> *(0或者无限) +(1或者无限) ?(0或者1) {m}(匹配m次)
# rs = re.findall('a*','aaddaaaddaaaadd')
# rs = re.findall('a+', 'aaddaaaddaaaadd')
# rs = re.findall('a?','aaddaaaddaaaadd')
# rs = re.findall('a{4}','aaddaaaddaaaadd')
# rs = re.findall('\w*','aaddaaaddaaaadd')



s = 'ss4430524200002162930ss112341763708746273'
rs = re.findall(r'[43,11]\d{16}', s)
print(rs)