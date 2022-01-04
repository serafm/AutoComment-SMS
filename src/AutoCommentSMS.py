from time import sleep
from selenium import webdriver
from keyboard import press


driver = webdriver.Chrome('chromedriver')
driver.minimize_window()
driver.get("https://www.instagram.com")
print("Opened Instagram \n")

sleep(4)
driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
sleep(3)

username = driver.find_element_by_name('username')
username.send_keys('testinstacomment') # <- INSERT YOUR INSTAGRAM USERNAME HERE
password = driver.find_element_by_name('password')
password.send_keys('k3phmjtw') # <- INSERT YOUR INSTAGRAM PASSWORD HERE
sleep(1)

print("Logging in... \n")
login = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()
sleep(5)
print("Logged in \n")

print("Going to the post... \n")
driver.get('https://www.instagram.com/p/CTC0acnjeeH/')  # <- URL OF THE POST HERE

sleep(2)
print("Post found \n")
comments = "COMMENT HERE"  # <- THE COMMENT HERE

def setComment():
    print("Commenting... \n")
    comment = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
    comment.click()
    sleep(1)
    comment = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
    comment.click()
    sleep(1)
    comment.send_keys(comments)
    sleep(1)
    sendComment = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button[2]')
    sendComment.click()
    print("Comment Successful! \n")
    sleep(3)
    sendSMS()

def sendSMS():
    print("Sending SMS... may take a while \n")
    driver.get("https://globfone.com/send-text/")
    sleep(0.5)
    textbox = driver.find_element_by_xpath('/html/body/div[1]/div/section[1]/div/div/div[2]/div/div/div/div[2]/form/input')
    textbox.click()
    textbox.send_keys("UPDATE")
    nextbutton = driver.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/div[2]/div/div/div/div[2]/a")
    nextbutton.click()
    sleep(4)
    country = driver.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]")
    country.click()
    country.send_keys("Greece") # <- COUNTRY NAME HERE (For example: "Greece")
    press('enter')
    sleep(1)
    pnum = driver.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[2]/input")
    pnum.click()
    pnum.send_keys("6947011810") # <- PHONE NUMBER HERE
    sleep(0.5)
    nextbutton = driver.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]")
    nextbutton.click()
    sleep(2)
    input_text = driver.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[3]/div/textarea")
    input_text.click()
    sleep(1)
    input_text.send_keys("Hello World") # <- SMS TEXT HERE
    sleep(1)
    nextbutton = driver.find_element_by_xpath("/html/body/div[1]/div/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]")
    nextbutton.click()
    sleep(20)
    print("SMS Sent!")

setComment()