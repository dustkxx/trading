from calendar import c
import jqdatasdk as jq
from matplotlib.pylab import f
from sqlalchemy import true



# 价格数据字段
PRICE_FIELDS = [
    "open",
    "close",
    "low",
    "high",
    "volume",
    "money",
    "factor",
    "high_limit",
    "low_limit",
    "avg",
    "pre_close",
    "paused",
]


def get_price(security, fre, s_date, e_date):
    """
    获取股票数据
    参数：
        security: str, 股票代码
        frequency: str, 频率
        s_date: str, 开始日期
        e_date: str, 结束日期
    返回：
        DataFrame
    """

    price_list = jq.get_price(
        security, start_date=s_date, end_date=e_date, frequency=fre, fields=PRICE_FIELDS
    )
    return price_list


def get_minute_price(security, start_date, end_date):
    """
    获取分钟线数据
    参数：
        security: str, 股票代码
        start_date: str, 开始日期
        end_date: str, 结束日期
    返回：
        DataFrame
    """
    return get_price(security, "1m", start_date, end_date)


def get_day_price(security, start_date, end_date):
    """
    获取日线数据
    参数：
        security: str, 股票代码
        start_date: str, 开始日期
        end_date: str, 结束日期
    返回：
        DataFrame
    """
    return get_price(security, "1d", start_date, end_date)
