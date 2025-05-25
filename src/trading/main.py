from base_data import get_day_price, get_minute_price
from models import security_price
import jqdatasdk as jq


if __name__ == "__main__":
    security = "000001.XSHE";
    # 获取日线数据
    dailys = get_day_price(security, "2025-02-15", "2025-02-21")
    print(dailys)

    # 批量插入
    security_price.add_batch(dailys,security)