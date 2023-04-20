import pytest
from selenium import webdriver as selenium_webdriver
from selenium.webdriver.common.by import By
import time


def test_show_my_pets(selenium_driver):
    ''' Тест на проверку списка питомцев:
      1. Проверяем, что оказались на странице питомцев пользователя.
      2. Проверяем, что присутствуют все питомцы.  '''

    driver = selenium_driver

    # Нажимаем на кнопку входа в пункт меню Мои питомцы
    driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/my_pets']").click()
    time.sleep(3)
    # Проверяем, что оказались на странице питомцев пользователя
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    # 1. Проверяем, что присутствуют все питомцы, для этого:
    # находим кол-во питомцев по статистике пользователя и проверяем, что их число
    # соответствует кол-ву питомцев в таблице
    pets_number = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    # pets_count = 100
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    assert int(pets_number) == len(pets_count)
    # 2. Проверяем, что с фото больше или равно чем без фото
    photo = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr/th/img')
    count_photo = 0
    count_not_photo = 0
    for i in range(len(photo)):
        if photo[i].get_attribute('src') != '':
            count_photo = count_photo + 1
            print(i, end=";")
        else:
            count_not_photo = count_not_photo + 1
    assert int(count_photo) >= len(pets_count)/2

