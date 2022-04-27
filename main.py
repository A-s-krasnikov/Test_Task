#
# # parser = ProgHub_parser(driver, "PY")
# # parser.parse()
#
# driver.get("https://zen.yandex.ru/")
# btn_sing_up = driver.find_element_by_class_name("auth-header-buttons-view__right-link")
# btn_sing_up.click()
#
# btn_sing_in = driver.find_element_by_class_name("registration-auth-link__link")
# btn_sing_in.click()

import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://mail.yandex.ru/?noretpath=1")
enter = driver.find_element(By.XPATH, '//*[@id="index-page-container"]/div/div[2]/div/div/div[4]/a[2]')
enter.click()
time.sleep(2)
# mail = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[2]/button')
# mail.click()
enter1 = driver.find_element(By.XPATH, '//*[@id="passp-field-login"]')
enter1.send_keys ("testkrasnikov@yandex.ru")
enter2 = driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]')
enter2.click()
time.sleep(1)
password = driver.find_element(By.ID, "passp-field-passwd")
password.send_keys("27Avg1986I")

time.sleep(1)

enter3 = driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]')
enter3.click()

time.sleep(30)
# driver.quit()
# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
# textarea = driver.find_element_by_css_selector(".textarea")

# Напишем текст ответа в найденное поле
# textarea.send_keys("get()")
# time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
# submit_button = driver.find_element_by_css_selector(".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
# submit_button.click()
# time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера

