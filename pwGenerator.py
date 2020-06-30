import random
import string
from selenium import webdriver
from selenium.webdriver import ActionChains
import os
import time
from selenium.webdriver.common.keys import Keys

generatedPassword = ''
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
passwordLength = None
passwordNumbers = None
letters = string.ascii_letters
numbers = string.digits

#Ensure that the entries to the below questions are the correct input. Integers rather than strings or floats.

while type(passwordLength) is not int:
    passwordLength = input("How many letters would you like in your password? ")
    try:
        passwordLength = int(passwordLength)
        #print("Input is an integer number.") verbose print to ensure integer detection was working
        #print("Input number is: ", passwordLength) verbose print to ensure storage of number was correct
    except ValueError:
        print("This is not a number. Please enter a valid number")
while type(passwordNumbers) is not int:
    passwordNumbers = input("How many numbers would you like in your password? ")
    try:
        passwordNumbers = int(passwordNumbers)
        #print("Input is an integer number.") verbose print to ensure integer detection was working
        #print("Input number is: ", passwordNumbers) verbose print to ensure integer detection was working
    except ValueError:
        print("This is not a number. Please enter a valid number")
#randomly generate the amount of letters and numbers needed     
rand_letters = random.choices(letters,k=passwordLength)
rand_numbers = random.choices(numbers,k=passwordNumbers)
"""print(rand_letters) same verbose prints here
print(rand_numbers)"""


#As string.ascii_letters and digits returns an array the below is needed to remove all punctuation listed at the top of the code.
no_punct_char = ""
for char in rand_letters:
    if char not in punctuations:
        no_punct_char = no_punct_char + char
"""print(no_punct_char)"""

no_punct_num = ""
for char in rand_numbers:
    if char not in punctuations:
        no_punct_num = no_punct_num + char
"""print(no_punct_num)"""

#Output the final generated password.

print("Your new generated password is " + no_punct_char + no_punct_num)

driver = webdriver.Chrome()
driver.get("https://securemessage.zenzero.co.uk")

search_input_box = driver.find_element_by_name("content")
search_input_box.send_keys(no_punct_char + no_punct_num)

Expiry = driver.find_element_by_id("expiry-days-range")
print(Expiry)
move = ActionChains(driver)
move.click_and_hold(Expiry).move_by_offset(-230,0).release().perform()

ViewLimit = driver.find_element_by_id("view-limit-range")
print(ViewLimit)
move.click_and_hold(ViewLimit).move_by_offset(-230,0).release().perform()

Submit = driver.find_element_by_xpath('//button[normalize-space()="Submit & Generate Link"]').click()
print(Submit)
time.sleep(2)

