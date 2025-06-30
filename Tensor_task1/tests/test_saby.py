from pages.main_page import MainPage
from pages.contacts_page import ContactsPage
from pages.tensor_page import TensorPage

def test_saby_tensor_flow(browser):
    url = "https://saby.ru/"
    main = MainPage(browser)
    contacts = ContactsPage(browser)
    tensor = TensorPage(browser)

    main.open(url)
    main.go_to_offices()
    contacts.click_tensor_logo()

    browser.switch_to.window(browser.window_handles[-1])
    tensor.verify_slogan_visible()
    tensor.click_more()

    all_equal, sizes = tensor.all_cards_same_size()
    for i, (w, h) in enumerate(sizes, 1):
        print(f"    Карточка {i}: width={w}, height={h}")
    assert all_equal, "Не все карточки одинакового размера"