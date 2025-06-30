from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 0
link = 'https://saby.ru/'
browser = webdriver.Chrome()
browser.get(link)
wait = WebDriverWait(browser, 15)

# Step 1
try:
    contacts = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="wasaby-content"]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[1]')))
    contacts.click()
    offices = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="wasaby-content"]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]/span')))
    offices.click()
    print('✅ Шаг №1')
except:
    print('❌ Шаг №1')


# Step 2
try:
    print('   Шаг №2')
    region_title = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')))
    if region_title.text == 'г. Москва':
        print("   ✅ Регион определён как Москва")

    partners = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]')))
    if (partners.text != '') and ('Москва' in partners.text):
        print("   ✅ Есть список партнеров")
except:
    print('   ❌ Ошибка при обработке региона/партнеров')

# Step 3
try:
    region_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')))
    region_link.click()

    new_region = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')))
    new_region.click()
    print('✅ Шаг №3')
except:
    print('❌ Шаг №3')

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Step 4
browser.switch_to.window(browser.window_handles[-1])

try:
    print('   Шаг №4')

    region_xpath = '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span'
    WebDriverWait(browser, 10).until(
        lambda driver: driver.find_element(By.XPATH, region_xpath).text.strip() == 'Камчатский край'
    )
    region_title = browser.find_element(By.XPATH, region_xpath)

    if region_title.text.strip() == 'Камчатский край':
        print("   ✅ Регион определён как Камчатский край")

    partners_xpath = '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]'
    partners = wait.until(EC.visibility_of_element_located((By.XPATH, partners_xpath)))
    partners_text = partners.text

    if 'Петропавловск-Камчатский' in partners_text:
        print("   ✅ Есть список партнёров, относящийся к Камчатскому краю")
except Exception as e:
    print('   ❌ Ошибка при обработке региона/партнёров:', e)

browser.quit()
