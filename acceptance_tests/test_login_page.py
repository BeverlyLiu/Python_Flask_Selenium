from selenium import webdriver

def test_login_function():
    with webdriver.Chrome() as driver:
        # webdriver load url
        try:
            driver.get('http://127.0.0.1:5000/')
            login_element = driver.find_element_by_xpath('//*[@id="navbarToggle"]/div[2]/a[1]')
                # element.click
            login_element.click()
                # fill out email field
            email = driver.find_element_by_id('email')
            email.click()
            email.send_keys('bevliu@gmail.com')


                # fill out password field
            password = driver.find_element_by_id("password")
            password.click()
            password.send_keys('password')

                # click on login button
            login_botton_element = driver.find_element_by_xpath('//*[@id="submit"]')
            login_botton_element.click()

                # check page is at home url
            print('Current Url: {}'.format(driver.current_url))
            # home_url = driver.current_url
            return True
        except:
            return False

home_page = test_login_function()
print('\nHome Page: {}'.format(home_page))