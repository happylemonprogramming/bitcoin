# THINGS YOU NEED TO FILL OUT
# Name, Phone, Email for pick up, receipt and text confirmation for sandwich
first_name = 'Jack'
last_name = 'Lemon'
phone_number = "8005551234" # Used for sandwich and text
mail = "shadowysupercoder@hotmail.com"
# PaywithMoon login information (if same as above, set moon_email = mail)
moon_email = "shadowysupercoder@hotmail.com"
# Twilio authentication (optional, but needed for text notification)
account_sid = 'ENTER SID'
auth_token = 'ENTER TOKEN'

# In[1]:
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Find Brave browser path (works with any Chromium browser) and go incognito mode
driver_path = r"C:\Users\lemon\Documents\Programming\chromedriver.exe"
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--incognito")
options.binary_location = brave_path

# Open website
wd = webdriver.Chrome(executable_path=driver_path, options=options)
wd.implicitly_wait(100)
wd.maximize_window()
wd.get("https://www.jerseymikes.com/order/20301/")

# In[2]:
# Click "Guest" and enter name, phone and email then continue
wd.find_element_by_xpath('//*[@id="start-tabpanel"]/div/fieldset[3]/div/div/button[2]').click()
wd.find_element_by_xpath('//*[@id="guest_first_name"]').send_keys(first_name)
wd.find_element_by_xpath('//*[@id="guest_last_name"]').send_keys(last_name)
wd.find_element_by_xpath('//*[@id="guest_tel"]').send_keys(phone_number)
wd.find_element_by_xpath('//*[@id="guest_email"]').send_keys(mail)
wd.find_element_by_xpath('//*[@id="start-tabpanel"]/div/fieldset[3]/div/div/div/form/button').click()

# In[3]:
# Select items for sandwich and save
items = wd.find_element_by_xpath('//*[@id="order-app"]/div[3]/div[1]/div/button')
items.click()

cold = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div/fieldset/div[2]/button[2]')
cold.click()

number_7 = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div/fieldset/div[2]/div[5]/button/div[1]/img')
number_7.click()

rosemary = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div/fieldset/div[2]/div[4]/div[1]/ingredient-selector[1]/fieldset/div/div[3]/label/span')
rosemary.click()

customize_1 = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div/fieldset/div[2]/div[4]/div[2]/button')
customize_1.click()

no_onions = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div/fieldset/div[2]/div[4]/div[2]/ingredient-selector/fieldset/div/div[1]/label/span')
no_onions.click()

peppers = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div/fieldset/div[2]/div[4]/div[2]/ingredient-selector/fieldset/div/div[11]/label/span')
peppers.click()

save_1 = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div/fieldset/div[4]/button')
save_1.click()

# In[4]:
# Add another sandwich and save
add = wd.find_element_by_xpath('//*[@id="add-new-item"]')
add.click()

hot = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div[2]/fieldset/div[2]/button[3]')
hot.click()

kahuna = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div[2]/fieldset/div[2]/div[9]/button/div[1]/img')
kahuna.click()

wheat = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div[2]/fieldset/div[2]/div[4]/div[1]/ingredient-selector[1]/fieldset/div/div[2]/label/span')
wheat.click()

customize_2 = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div/fieldset/div[2]/div[4]/div[2]/button')
customize_2.click()

no_jalapeno = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div[2]/fieldset/div[2]/div[4]/div[2]/ingredient-selector/fieldset/div/div[1]/label/span')
no_jalapeno.click()

save_2 = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div/fieldset/div[4]/button')
save_2.click()

# In[5]:
# Add chips and save
chips = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div[3]/div[5]/button')
chips.click()

edit = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div[3]/fieldset/div[3]/button')
edit.click()

vinegar = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div[3]/fieldset/div[2]/div[3]/div[2]/ingredient-selector/fieldset/div/div[2]/label/input')
vinegar.click()

save_3 = wd.find_element_by_xpath('//*[@id="items-tabpanel"]/div/div[1]/div/div[3]/fieldset/div[4]/button')
save_3.click()

# In[6]:
# Checkout and review order
checkout = wd.find_element_by_xpath('//*[@id="order-app"]/div[3]/div[1]/div/button')
checkout.click()

# TODO: add pickup date, time, tip, promo code and notes, if needed
review = wd.find_element_by_xpath('//*[@id="order-app"]/div[3]/div[1]/div/button')
review.click()

# In[7]:
# Save total as text to input into PaywithMoon card
time.sleep(5)
cost = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="payment-tabpanel"]/div/div[1]/div[2]/table/tfoot/tr[3]/td[1]/span'))).text
total = cost.replace('$','')

# In[8]:
# Log in to PaywithMoon
# Open a new window in browswer
wd.execute_script("window.open('');")
  
# Switch to the new window and open new URL
wd.switch_to.window(wd.window_handles[1])
wd.get('https://paywithmoon.com/')

# Log in
WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="basic-navbar-nav"]/div/a[5]'))).click()
WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]'))).send_keys(moon_email)
password = input("Enter PaywithMoon Password\n") # don't store passwords in code
WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))).send_keys(password)
WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/form/button'))).click()

# In[9]
# Create payment at PaywithMoon
# Create card
WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div[1]/div/button/div[2]'))).click()
# Send Total
WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/input'))).send_keys(total)

# In[10]:
# Hit Continue
WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/button'))).click()

# In[11]:
# Confirm Card Creation
WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/button'))).click()

# TODO: at this point you should be prompted with a lightning invoice. Pay invoice to generate card.

# In[12]:
# Store Card Values
# Name and zip shouldn't matter for PaywithMoon
name = 'Satoshi Nakamoto'
zip_code = '10005'
card_number = WebDriverWait(wd, 180).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cardInfoModal"]/div/div/div[2]/div[1]/div[1]/div[2]/div/span'))).text
security = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cardInfoModal"]/div/div/div[2]/div[1]/div[1]/div[4]/div/span'))).text
exp = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cardInfoModal"]/div/div/div[2]/div[1]/div[1]/div[3]/div/span'))).text

# In[9]:
# Enter card information on sandwich site
# Switch back to sandwiches
wd.switch_to.window(wd.window_handles[0])
# Add security code
WebDriverWait(wd, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cvv_code"]'))).send_keys(security)
# Add postal code
WebDriverWait(wd, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="billing_postcode"]'))).send_keys(zip_code)
# Add name
WebDriverWait(wd, 2).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="first-data-payment-field-name"]')))
WebDriverWait(wd, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="name"]'))).send_keys(name)

# In[10]:
# Add card expiry
wd.switch_to.default_content()
WebDriverWait(wd, 2).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'/html/body/main/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/form/div[5]/span/iframe')))
WebDriverWait(wd, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/input'))).send_keys(exp)

# In[10]:
# Add card number
wd.switch_to.default_content()
WebDriverWait(wd, 2).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'/html/body/main/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/form/div[3]/span/iframe')))
WebDriverWait(wd, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/input[1]'))).send_keys(card_number)

# In[11]:
# Confirm card use
wd.switch_to.default_content()
use_card = wd.find_element_by_xpath('//*[@id="tokenize-card-button"]')
use_card.click()

# In[10]:
# Submit order
# WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="payment-tabpanel"]/div/div[1]/button'))).click()

# In[11]:
# Send "Ready By" text message to self 
ready_by = wd.find_element_by_xpath('//*[@id="complete-tabpanel"]/div/div[2]/div[2]/div[1]/strong[1]')
from twilio.rest import Client 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGaf6176f2db8e12d7e89a9e926b83ce3b', 
                              body=ready_by.text,      
                              to='+1'+ phone_number
                          ) 
 
print(message.sid)