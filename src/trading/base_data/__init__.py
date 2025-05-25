from .pricedata import get_minute_price
from .pricedata import get_day_price
import jqdatasdk as jq
import os


# 从环境变量中获取账号密码
key = os.getenv("JQ_ACCOUNT")
password = os.getenv("JQ_PASSWORD")

# 账号密码认证
jq.auth(key, password)

# 打印当日可调用数据量
count = jq.get_query_count()
print("当日可调用数据量: ", count)
