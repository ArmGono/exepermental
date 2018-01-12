#!/usr/bin/env python
# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

_firstName = 'Varduhi'
_lastName =  'Meneshyan'
_contentText = 'lorem lorem lorem parabum'

browser = webdriver.Firefox()
browser.get('http://auto.armrus.net/')
assert 'Test for automation' in browser.title

nameElem = browser.find_element_by_name('firstname')
lastElem = browser.find_element_by_name('lastname')
textElem = browser.find_element_by_name('content')

nameElem.send_keys(_firstName)
lastElem.send_keys(_lastName)
textElem.send_keys(_contentText)
