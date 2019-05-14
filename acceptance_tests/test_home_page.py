from selenium import webdriver

def test_home_left_side():
    with webdriver.Chrome() as driver:
        # webdriver load (url)
        try:
            driver.get('http://127.0.0.1:5000/')
        # element = home element
            home_element = driver.find_element_by_xpath('//*[@id="navbarToggle"]/div[1]/a[1]')
        # element.click
            home_element.click()
        # left_element = left element
            left_element = driver.find_element_by_xpath('/html/body/main/div/div[1]')
        # return left_element exists
            return True
        except:
            return False

def test_home_right_side():
    with webdriver.Chrome() as driver:
    # load homepage
        try:
            driver.get('http://127.0.0.1:5000/')
            home_element = driver.find_element_by_xpath('//*[@id="navbarToggle"]/div[1]/a[1]')
    # click home
            home_element.click()
            right_element = driver.find_element_by_xpath('/html/body/main/div/div[2]/div')
    # return right side exists
            return True
        except:
            return False

def test_all():
    # test home left side exists
    left_exists = test_home_left_side()
    # test home right side exists
    right_exists = test_home_right_side()
    # return results
    return "\tLeft exists: {}\n\tRight exists: {}".format(left_exists, right_exists)

print('Home Page: \n{}'.format(test_all()))