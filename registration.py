import time

import main, function, gui, traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def vk(driver, login, password):
    try:
        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.NAME,'email')))

        element.click()
        element.send_keys(login)                                # Вводим логин

        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.NAME, 'pass')))
        element.clear()
        element.send_keys(password)                             # Вводим пароль

        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'install_allow')))
        element.click()                                         # Подтверждаем
        try:
            try:
                element_1 = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@class='box_error']")))
                if not element_1:
                    pass
                else:
                    driver.quit()
                    gui.Main_menu.warning_log()

                    return 1
            except:
                pass
            try:
                element_2 = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@class='oauth_form_header']")))
                if not element_2:
                    pass
                else:
                    driver.quit()
                    gui.Main_menu.warning_log()

                    return 1
            except:
                pass
        except:
            pass

        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='button button_default-border-radius button_default-disabled default-active basic-socials__button basic-socials__button_vk basic-socials__button_light']")))

        element.click()             # Повторное нажатие аккаунта и вход в игру
        function.log('login successful\n')
    except:
        function.log('login error \nRestarting the program\n\n')
        function.crash(traceback.format_exc())
        driver.quit()
        main.main()

def facebook(driver, login, password):
    try:
        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.NAME, 'email')))
        element.click()

        element.send_keys(login)

        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.NAME, 'pass')))
        element.clear()
        element.send_keys(password)

        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'loginbutton')))
        element.click()

        try:
            element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='fsl fwb fcb']")))
            if not element:
                pass
            else:
                driver.quit()
                gui.Main_menu.warning_log()
                return 1
        except:
            pass



        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='button button_default-border-radius button_default-disabled default-active basic-socials__button basic-socials__button_fb basic-socials__button_light']")))
        element.click()
        function.log('login successful\n')

    except:
        function.log('login error \nRestarting the program\n\n')
        driver.quit()
        main.main()

def without_reg(driver, login):
    try:
        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'auth-screen__content-body-light-auth-link')))
        element.click()
        time.sleep(3)
        element = main.driver.find_element_by_xpath(".//input[@class='quiz-input auth-screen__content-body-light-form-input']")
        element.click()
        element.send_keys(login)
        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, ".//div[@class='button default-active auth-screen__content-body-light-form-button']")))
        element.click()


        function.log('login successful\n')

    except:
        function.log('login error \nRestarting the program\n\n')
        function.crash(traceback.format_exc())
        driver.quit()
        main.main()