import re

# r原串能消除转义符带来的影响

# 未用r原串之前 --> 当我们想查询'a\\nc'时
# rs = re.findall('a\\\\nc','a\\nc')

# 使用r原串
rs = re.findall(r'a\\nc','a\\nc')


# r原串可以解决写正则时,不符合PEP8规范的问题
rs = re.findall('\d','123')
rs = re.findall(r'\d','123')