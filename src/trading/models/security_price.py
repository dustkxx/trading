from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime,
    DECIMAL,
    UniqueConstraint,
    Index,
)

Base = declarative_base()


## 1. 创建数据库引擎
postgres_engine = create_engine("postgresql://postgres:postgres@127.0.0.1/postgres")

# 绑定引擎
Session = sessionmaker(bind=postgres_engine)
# 创建数据库链接池，直接使用session即可为当前线程拿出一个链接对象conn
# 内部会采用threading.local进行隔离
session = scoped_session(Session)


## 2. 创建数据库会话
## 3. 创建数据库表
## 3. 创建数据表模型


def add_batch(prices, security):
    """
    批量插入数据
    """
    models = []
    for index, row in prices.iterrows():
        sp = SecurityPrice(
            security=security,
            date=index,
            open=float(row["open"]),
            close=float(row["close"]),
            low=float(row["low"]),
            high=float(row["high"]),
            volume=float(row["volume"]),
            money=float(row["money"]),
            factor=float(row["factor"]),
            high_limit=float(row["high_limit"]),
            low_limit=float(row["low_limit"]),
            avg=float(row["avg"]),
            pre_close=float(row["pre_close"]),
        )
        models.append(sp)
    session.add_all(models)
    session.commit()
    session.remove()


class SecurityPrice(Base):
    __tablename__ = "day_price"
    __table_args__ = (
        UniqueConstraint("security", "date", name="security_date_uc"),
        Index("security_date_idx", "security", "date"),
    )

    # 唯一键
    id = Column(Integer, primary_key=True)
    # 股票代码
    security = Column(String(20), nullable=False)
    # 日期
    date = Column(DateTime, nullable=False)
    # 开盘价
    open = Column(DECIMAL(10, 2), nullable=False)
    # 收盘价
    close = Column(DECIMAL(10, 2), nullable=False)
    # 最低价
    low = Column(DECIMAL(10, 2), nullable=False)
    # 最高价
    high = Column(DECIMAL(10, 2), nullable=False)
    # 成交量
    volume = Column(DECIMAL(19, 2), nullable=False)
    # 成交金额
    money = Column(DECIMAL(19, 2), nullable=False)
    # 复权因子
    factor = Column(DECIMAL(10, 2), nullable=False)
    # 涨停价
    high_limit = Column(DECIMAL(10, 2), nullable=False)
    # 跌停价
    low_limit = Column(DECIMAL(10, 2), nullable=False)
    # 平均价
    avg = Column(DECIMAL(10, 2), nullable=False)
    # 昨收价
    pre_close = Column(DECIMAL(10, 2), nullable=False)

    def __repr__(self):
        return (
            f"<DayPrice(security={self.security}, date={self.date}, open={self.open}, "
            f"close={self.close}, low={self.low}, high={self.high}, volume={self.volume}, "
            f"money={self.money}, factor={self.factor}, high_limit={self.high_limit}, "
            f"low_limit={self.low_limit}, avg={self.avg}, pre_close={self.pre_close})>"
        )
