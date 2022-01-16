from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# открыть окно на весь экран
chrome_options.add_argument('start-maximized')

# starts a new chrome session
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.implicitly_wait(10) # seconds
# driver = webdriver.Chrome(r'G:\000---Python\gb python\env\chromedriver_win32\chromedriver.exe') # Add path if required
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# Закрыть одну вкладку
driver.close()
# Закрыть весь браузер
# driver.close()

element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")