from selenium import webdriver 
driver = webdriver.Firefox(executable_path='C:\\Users\\compu\\Desktop\\vs code\\geckodriver-v0.27.0-win64\\geckodriver.exe')
driver.get('https://www.youtube.com/')

searchbox = driver.find_elements_by_id('search-input')
searchbox.send_keys("pls beg")
searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbutton.click()