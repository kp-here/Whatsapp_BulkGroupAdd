from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# grp_name = input("\nEnter Group Name :\n")
grp_name="testing 0006"

#importing contact names
l=[]
with open("a.csv") as file:
    for a in file.readlines():
        l.append(a.rstrip('\n'))
file.close()

N=[]

#loading web driver
driver = webdriver.Chrome(executable_path=r'T:\Whatsapp Automation\chromedriver.exe')
wait = WebDriverWait(driver, 5)
driver.maximize_window()
driver.get('https://web.whatsapp.com/')


#selenium functions to select and click elements
def findbyxpath(x):
    a= wait.until(EC.presence_of_element_located((By.XPATH, x)))
    a.click()
    return a

def findbyxpath_noclick(x):
    return wait.until(EC.presence_of_element_located((By.XPATH, x)))

#click search box
group_title = findbyxpath("//div[@class='_13NKt copyable-text selectable-text']")

#type in group name and select it
group_title.send_keys(grp_name + Keys.ENTER) 


#clicked on group name header
head_title= findbyxpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[1]/div[1]/span[1]")


#click on add participant
add_part=findbyxpath("//div[contains(text(),'Add participant')]")


#select participants one by one
for i in l:
    #pass string & keys to search box
    
    box=findbyxpath_noclick("//div[@class='nBIOd tm2tP copyable-area']//div//div[@class='_13NKt copyable-text selectable-text']")
    box.send_keys(i)

    #wait till exact contact name appears in the list
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='emoji-texttt _ccCW FqYAR i0jNr'][contains(text(),'{}')]".format(i))))
    except:
        #if the given contact name is not found in the contact list
        #crossout the given name and skip to next name
        # cross=findbyxpath("//div[@class='_3yWey XKmj6 _3N4HJ']//span//span")
        back=findbyxpath("//div[@class='_3yWey XKmj6 _3N4HJ']//button[@class='_28-cz']")

        #click on the box
        box2=findbyxpath("//div[@class='nBIOd tm2tP copyable-area']//div//div[@class='_13NKt copyable-text selectable-text']")

        N.append(i)
        continue

    box.send_keys(Keys.ENTER)

#confirm the selected participants [green tick]
finalize=findbyxpath("//div[@class='_165_h _2HL9j']") 


#confirm - 'add participant'
confirm = findbyxpath("//div[@class='tvf2evcx m0h2a7mj lb5m6g5c j7l1k36l ktfrpxia nu7pwgvd gjuq5ydh'][contains(text(),'Add participant')]") 


#invite to group - for participants who cannot be added
invite=findbyxpath("//div[@class='tvf2evcx m0h2a7mj lb5m6g5c j7l1k36l ktfrpxia nu7pwgvd gjuq5ydh'][contains(text(),'Invite to group')]") 

#'send invite'
invite=findbyxpath("//div[@class='_165_h _2HL9j']") 

print("Contacts not added :")
for i in N:
    print(i)

time.sleep(5)
driver.quit()

