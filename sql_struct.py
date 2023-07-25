# coding=utf-8
from __future__ import unicode_literals, absolute_import
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker

engine=create_engine("mysql+pymysql://root:yhl2016#@10.7.60.109:3306/atl_aps2", echo=True)
# <-元类
ModelBase = declarative_base()

# build one class for each table
class Buffer(ModelBase):
    __tablename__ = "config_baseline_buffer_info"

    id = Column(String(length=128), primary_key=True)
    facotry_name = Column(DateTime)
    product_process = Column(String(length=30))
    product_name = Column(String(length=128))
    work_shop = Column(String(length=128))
    pack = Column(String(length=128))
    buffer_day = Column(Integer)


sql_session = sessionmaker(bind=engine)()
tmp = sql_session.query(Buffer).filter(Buffer.id == '00105d52c59fc2e21997e984ea311f45')
for i in tmp:
    print(i.id, i.work_shop, i.product_name)
sql_session.close()
