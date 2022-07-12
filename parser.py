from cgitb import html
from re import sub
from decimal import Decimal
import requests
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.ikea.com/ru/ru/p/djungelskog-dyungelskog-myagkaya-igrushka-buryy-medved-80402833/"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.0.1842 Yowser/2.5 Safari/537.36"
}
page = requests.get(url = PRODUCT_URL,headers= headers)
# print(page.content)

soup = BeautifulSoup(html, "lxml")
product_title = soup.find(
    "h1",
    class_="pip-header-section"
).get_text()

print(product_title)
# product_price = soup.find("div", class_="pip-price").get_text()
# product_price = product_price.replace(",", ".")
# product_price_int = Decimal(sub(r"[^\d\-.]", "", product_price))
# #  print(price, type(price), price_int, type(price_int))

# from datetime import datetime
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class Price(Base):
#     __tablename__ = "price"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     datetime = Column(DateTime)
#     price = Column(String(64))
#     price_int = Column(Numeric(10, 2))

#     def __repr__(self):
#         return f"{self.name} | {self.price}"

# engine = create_engine("sqlite:///database.sqlite")
# Base.metadata.create_all(engine)

# session = Session(bind=engine)

# def add_price(title, price, price_int):
#     is_exist = session.query(Price).filter(
#         Price.name==title
#     ).order_by(Price.datetime.desc()).first()

#     if not is_exist:
#         session.add(
#             Price(
#                 name=title,
#                 datetime=datetime.now(),
#                 price=price,
#                 price_int=price_int
#             )
#         )
#         session.commit()
#     else:
#         if is_exist.price_int != price_int:
#             session.add(
#                 Price(
#                     name=title,
#                     datetime=datetime.now(),
#                     price=price,
#                     price_int=price_int
#                 )
#             )
#             session.commit()


# add_price(product_title, product_price, product_price_int)

# items = session.query(Price).all()
# for item in items:
#     print(item)
