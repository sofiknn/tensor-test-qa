import pytest
from pages.main_page import MainPage
from pages.contacts_page import ContactsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_contacts_offices(browser):
    main = MainPage(browser)
    main.open()
    main.open_contacts_offices()

    contacts = ContactsPage(browser)

    # Step 2 - Проверка Москвы
    assert contacts.get_region() == 'г. Москва', "Неверный регион"
    assert contacts.partners_contain('Москва'), "Нет партнеров в Москве"

    # Step 3 - Смена региона
    contacts.change_region_to_kamchatka()
    browser.switch_to.window(browser.window_handles[-1])

    wait = WebDriverWait(browser, 10)
    wait.until(lambda driver: contacts.get_region() == 'Камчатский край')

    # Step 4 - Проверка Камчатки
    assert contacts.get_region() == 'Камчатский край', "Регион не сменился на Камчатский край"
    assert contacts.partners_contain('Петропавловск-Камчатский'), "Нет партнёров в Камчатском крае"
