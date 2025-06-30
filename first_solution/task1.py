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

# Step 2, 3
try:
    tensor_logo = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img')))
    tensor_logo.click()
    print('✅ Шаг №2, 3')
except:
    print('❌ Шаг №2, 3')

# Step 4
browser.switch_to.window(browser.window_handles[-1])

try:
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Сила в людях')]")))
    print('✅ Шаг №4')
except:
    print('❌ Шаг №4')

# Step 5
try:
    more = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')))
    more.click()
    print('✅ Шаг №5')
except:
    print('❌ Шаг №5')

# Step 6
print('   Шаг №6')
try:
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "tensor_ru-About__block3-image-wrapper")))

    cards = browser.find_elements(By.CLASS_NAME, "tensor_ru-About__block3-image-wrapper")

    if not cards:
        print("    ❌ Карточки с изображениями не найдены")
    else:
        width0 = cards[0].size['width']
        height0 = cards[0].size['height']
        all_equal = True

        for idx, card in enumerate(cards):
            w = card.size['width']
            h = card.size['height']
            print(f"    Карточка {idx+1}: width={w}, height={h}")
            if w != width0 or h != height0:
                all_equal = False

        if all_equal:
            print("    ✅ Все карточки имеют одинаковые размеры")
        else:
            print("    ❌ Некоторые карточки имеют разные размеры")
except Exception as e:
    print("    ❌ Ошибка при проверке карточек:", e)

browser.quit()
