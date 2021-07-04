# 셀레니움(Selenium)이란?
셀레니움이란 웹사이트를 테스트하기 위한 포터블 프레임워크이다.
</br>
</br>
## 셀레니움을 통해 크롬에서 웹 크롤링을 해보기
<pre>
<code>
from selenium import webdriver
</code>
</pre>
- 셀레니움 Import

<pre>
<code>
driver = webdriver.Chrome('./chromedriver.exe')  
</code>
</pre>
- 크롬 드라이버를 다운받은 후 크롬 드라이버가 저장된 위치를 입력한다.  

<pre>
<code>
driver.implicitly_wait(3)
</code>
</pre>
- 지정한 시간만큼 대기할 수 있도록 암묵적 대기를 설정

<pre>
<code>
driver.get(' ')
</code>
</pre>
- 입력된 링크에 해당하는 웹 주소를 브라우저에 띄운다.

<pre>
<code>
driver.find_element_by_id(' ')
</code>
</pre>
- 조건에 맞는 요소 하나만 반환한다. id 속성으로 접근

<pre>
<code>
driver.find_elements_by_css_selector(' ')
</code>
</pre>
- 조건에 맞는 요소들을 반환한다. css 셀렉터로 접근

<pre>
<code>
driver.find_element_by_name(' ').send_keys()
</code>
</pre>
- 선택한 요소의 키보드 입력을 명령으로 주어 텍스트 입력을 수행한다.

<pre>
<code>
driver.find_element_by_xpath(' ').click()
</code>
</pre>
- 선택한 요소를 클릭한다.



