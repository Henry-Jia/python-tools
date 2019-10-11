from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains

# from selenium import webElement

driver=webdriver.Firefox()

rollno="2017UGCS026"

driver.get("https://nilekrator.pythonanywhere.com/rank")

# webDriver driver = new FirefoxDriver();
inpt = driver.find_element_by_xpath("//input[@name='roll']")
inpt.send_keys(rollno)
driver.find_element_by_xpath("/html/body/div[2]/div/div/form/div[2]/button").click()
time.sleep(5)
students= driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[4]/table/tbody/tr[1]/td[2]/span")
cgpa= driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[4]/table/tbody/tr[1]/td[3]")

num=len(students)
for i in range(num):
	print(students[i].text+" : : "+cgpa[i].text)

driver.close();
