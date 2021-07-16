# 다음 메일 가져오기
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/M/PycharmProjects/chromedriver.exe')
driver.implicitly_wait(2)
driver.get('https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fmail.daum.net%2F')
driver.implicitly_wait(3)

my_id=""
my_pwd=""

driver.find_element_by_name('id').send_keys(my_id)
driver.find_element_by_name('pw').send_keys(my_pwd)

driver.find_element_by_xpath('//*[@id="loginBtn"]').click()

# 메일 제목 추출
titles=driver.find_elements_by_css_selector('strong.tit_subject')
# 메일 날짜 추출
dates=driver.find_elements_by_class_name('txt_date')
for title in titles:
    print(title.text)

for date in dates:
    print(date.text)

driver.quit()

# 네이버 메일 가져오기 캡차 우회하기 위해 pyperclip 사용
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import pyperclip
#
#
# driver = webdriver.Chrome('C:/Users/M/PycharmProjects/chromedriver.exe')
# driver.get('https://nid.naver.com/nidlogin.login?url=http%3A%2F%2Fmail.naver.com%2F')
# time.sleep(2)
#
# # 아이디 입력폼
# tag_id = driver.find_element_by_name('id')
# # 패스워드 입력폼
# tag_pw = driver.find_element_by_name('pw')
#
# my_id = ''
# my_pwd = ''
#
# tag_id.click()
# pyperclip.copy(my_id)
# tag_id.send_keys(Keys.CONTROL, 'v')  # 복사 후 붙혀넣기
# time.sleep(1)
#
# tag_pw.click()
# pyperclip.copy(my_pwd)
# tag_pw.send_keys(Keys.CONTROL, 'v')
# time.sleep(1)
#
# # 로그인 버튼 클릭
# driver.find_element_by_id('log.login').click()
# time.sleep(1)
#
# # 네이버 기기 등록
# driver.find_element_by_id('new.save').click()
# time.sleep(3)
#
# # 메일 제목 추출
# titles = driver.find_elements_by_css_selector("strong.mail_title")
# for title in titles:
#     print(title.text)
#
# driver.quit()
