from cgitb import html
from re import sub
from decimal import Decimal
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

pr_url = "https://htmlacademy-schools.github.io/1902641-big-trip-1/13/"

headers = {
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'Referer': 'https://htmlacademy-schools.github.io/1902641-big-trip-1/13/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://htmlacademy-schools.github.io/1902641-big-trip-1/13/bundle.js', headers=headers)

driver = webdriver.Chrome(executable_path= "../chromedriver.exe")
driver.get(pr_url)
html = driver.page_source

soup = BeautifulSoup(html, "lxml")
title = soup.find("h3", class_="event__title")
print(title.get_text())

product_price = soup.find("p", class_="event__price").get_text()
product_price = product_price.replace(",", ".")
product_price_int = Decimal(sub(r"[^\d\-.]", "", product_price))
# print(price, type(price), price_int, type(price_int))
print(product_price)

driver.close()
driver.quit()

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
