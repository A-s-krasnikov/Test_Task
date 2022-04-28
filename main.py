
import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(2)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://passport.yandex.ru/auth/add?from=mail&origin=hostroot_homer_auth_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F%3Fnoretpath%3D1&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1")
time.sleep(1)
# Ищем поля ввода адреса почты
username = driver.find_element(By.XPATH, '//*[@id="passp-field-login"]')
# Вводим почту
username.send_keys("testkrasnikov@yandex.ru")
# Ищем кнопку Войти
button = driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]')
# Кликаем на войти
button.click()
# Ждем 1 секунду
time.sleep(1)
# Ищем поле для ввода пароля
password = driver.find_element(By.ID, "passp-field-passwd")
# Вводим пароль
password.send_keys("27Avg1986I")
# Ждем 1 секунду
time.sleep(1)
# Ищем кнопку Войти
enter3 = driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]')
# Жмем на кнопку войти
enter3.click()
# Ждем 5 секунд чтобы все загрузилось
time.sleep(5)
# Ищем кнопку написать
toWrite = driver.find_element(By.XPATH, '//a[@class=\'Button2 Button2_type_link Button2_view_action Button2_size_m Layout-m__compose--3KGCi qa-LeftColumn-ComposeButton ComposeButton-m__root--3ijKP\']')
# Жмем на кнопку написать
toWrite.click()
# Ждем 1 секунду чтобы появилось окно
time.sleep(1)
# Ищем поле для ввода почты кому
message = driver.find_element(By.XPATH, '//div[@class=\'composeYabbles\']')
# Вводим почту
message.send_keys('a.s.krasnikov@yandex.ru')
time.sleep(1)
# Ищем поле ввода сообщения
text = driver.find_element(By.XPATH, '//*[@id="cke_1_contents"]/div')
# Жмем на поле ввода сообщения
text.click()
# Вводим сообщение
text.send_keys('Отправляем тестовое сообщение')
time.sleep(1)
# Ищем поле с типом файл-инпут
file = driver.find_element(By.XPATH, '//input[@class="WithUpload-FileInput qa-Compose-FileInput"]')
# Добавляем файл с локального компьютера
file.send_keys('/Users/aleksandrkrasnikov/Downloads/Test.txt')
# Ждем 5 секунд чтобы файл успешно загрузился, можно увеличить для больших файлов
time.sleep(5)
# Ищем кнопку отправить
buttonSend = driver.find_element(By.XPATH, '//button[@class="Button2 Button2_pin_circle-circle Button2_view_default Button2_size_l"]')
# Жмем кнопку отправить
buttonSend.click()
# Ждем 15 секунд
time.sleep(15)
# Закрываем браузер
driver.quit()
