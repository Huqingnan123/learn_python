# 正则表达式的用法
import re
test = '    HUqingnan@@,,,   123'
if re.match(r'\s+\w{3,10}.....\s+\d{2,4}\d$', test):
    print('ok')
else:
    print('failed')


print(re.split(r'\s+', test))


print(re.split(r'[\s\,]+', test))


