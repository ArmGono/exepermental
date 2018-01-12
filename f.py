#!/usr/bin/env python
# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle

FILENAME = "pass.dat"
with open(FILENAME, "rb") as file:
  _name = pickle.load(file)
  _pass = pickle.load(file)

browser = webdriver.Firefox()
browser.get('https://passport.yandex.ru/passport?mode=auth&from=mail&retpath=https%3A%2F%2Fmail.yandex.ru&origin=hostroot_ru_nol_mobile_enter')
assert u'Авторизация' in browser.title

loginElem = browser.find_element_by_name('login')
passElem = browser.find_element_by_name('passwd')
loginElem.send_keys(_name)
passElem.send_keys(_pass + Keys.RETURN)
