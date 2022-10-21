from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service = Service(executable_path="../chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://www.pbclibrary.org/raton/mousercise.htm")

# title = driver.title
# PAGE 1
submit_button = driver.find_element(by=By.XPATH, value="/html/body/table[2]/tbody/tr[2]/td/form/input")
submit_button.click()

# PAGE2
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/p/a')
submit_button.click()

# PAGE3
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/p/a')
submit_button.click()

# PAGE4
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td/a')
submit_button.click()

# PAGE5
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[1]/a')
submit_button.click()

# PAGE6
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td/a')
submit_button.click()

# PAGE7
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/p/a')
submit_button.click()

# PAGE8
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/p/a')
submit_button.click()

# PAGE9
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/p/a')
submit_button.click()

# PAGE10
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td/a[2]')
submit_button.click()

# PAGE11
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td/a[2]')
submit_button.click()

# PAGE12
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td/a[2]')
submit_button.click()

# PAGE13
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td/a[2]')
submit_button.click()

# PAGE14
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td[2]/a[2]')
submit_button.click()

# PAGE15
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[4]/a')
submit_button.click()

# PAGE16
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/a')
submit_button.click()

# PAGE17
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr/td/form/input')
submit_button.click()

# PAGE18
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td/form/input')
submit_button.click()

# PAGE19
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td/form/button')
submit_button.click()

# PAGE20
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td/form/input')
submit_button.click()

# PAGE21
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[3]/a/img')
submit_button.click()

# PAGE22
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[3]/td[2]/a/img')
submit_button.click()

# PAGE23
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[1]/img')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[2]/img')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[3]/img')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[4]/img')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[5]/img')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[6]/img')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[7]/img')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[8]/img')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[9]/img')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[10]/img')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td[11]/img')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[4]/td/a/img')
submit_button.click()

# PAGE24
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[2]/td[1]/form/input')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[2]/td[3]/form/input')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[3]/td[1]/form/input')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[3]/td[3]/img')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[4]/td[1]/img')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[4]/td[3]/img')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[5]/td[1]/img')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[5]/td[3]/a/img')
submit_button.click()

# PAGE25
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[2]/td[1]/img')
ActionChains(driver).double_click(submit_button).perform()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[2]/td[2]/img')
ActionChains(driver).double_click(submit_button).perform()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[2]/td[3]/img')
ActionChains(driver).double_click(submit_button).perform()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[2]/td[4]/img')
ActionChains(driver).double_click(submit_button).perform()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[3]/td[1]/img')
ActionChains(driver).double_click(submit_button).perform()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[3]/td[2]/img')
ActionChains(driver).double_click(submit_button).perform()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[3]/td[3]/img')
ActionChains(driver).double_click(submit_button).perform()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[3]/td[4]/img')
ActionChains(driver).double_click(submit_button).perform()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr[4]/td/a/img')
submit_button.click()

# PAGE26
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='//*[@id="red-slider"]/div[2]/div')
submit_button2 = driver.find_element(by=By.XPATH, value='//*[@id="canvas"]/table/tbody/tr[3]/td/a')
ActionChains(driver).drag_and_drop(submit_button, submit_button2).perform()
submit_button = driver.find_element(by=By.XPATH, value='//*[@id="canvas"]/table/tbody/tr[3]/td/a')
ActionChains(driver).double_click(submit_button).perform()

# PAGE27
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/p[1]/a')
submit_button.click()

# PAGE28
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/p[1]/a')
submit_button.click()

# PAGE29
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/p[2]/a')
submit_button.click()

# PAGE30
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/p/a')
submit_button.click()

# PAGE31
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/table/tbody/tr/td[2]/p/a')
submit_button.click()

# PAGE32
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td/a')
submit_button.click()
alert = WebDriverWait(driver, timeout=3).until(expected_conditions.alert_is_present())
alert.accept()

# PAGE33
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr/td[2]/span/a')
submit_button.click()

# PAGE34
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[1]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[2]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[3]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[4]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[5]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[6]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[7]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[8]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[9]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/p/a/img')
submit_button.click()

# PAGE35
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/input[1]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/input[5]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/input[7]')
submit_button.click()

# PAGE36
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[1]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[2]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[3]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[4]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[5]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[6]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[7]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[8]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[9]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/p/a/img')
submit_button.click()

# PAGE37
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/input[2]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/input[5]')
submit_button.click()

# PAGE38
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/select')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/select/option[6]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/p/a/img')
submit_button.click()

# PAGE39
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/select')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/select/option[3]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/input')
submit_button.click()

# PAGE40
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/select/option[6]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/p/a/img')
submit_button.click()

# PAGE41
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/select/option[6]')
submit_button.click()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/table/tbody/tr[2]/td/form/input')
submit_button.click()

# PAGE41
# title = driver.current_url
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[1]')
ActionChains(driver).send_keys_to_element(submit_button, "David").perform()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[2]')
ActionChains(driver).send_keys_to_element(submit_button, "Lucero").perform()
submit_button = driver.find_element(by=By.XPATH, value='/html/body/form/input[3]')
submit_button.click()
