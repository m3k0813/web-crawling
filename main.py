# import requests
# from bs4 import BeautifulSoup
# import pandas
# import selenium
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/M/PycharmProjects/chromedriver.exe')
driver.implicitly_wait(2)
driver.get('https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fmail.daum.net%2F')
driver.implicitly_wait(3)

my_id="아이디"
my_pwd="비밀번호"

driver.find_element_by_name('id').send_keys(my_id)
driver.find_element_by_name('pw').send_keys(my_pwd)

driver.find_element_by_xpath('//*[@id="loginBtn"]').click()

# 메일 제목 추출
titles=driver.find_elements_by_css_selector('strong.tit_subject')
for title in titles:
    print(title.text)

