from selenium import webdriver


def browser():
    '''firefox无头模式设置'''
    # options = webdriver.FirefoxOptions()
    # options.add_argument('-headless')
    # driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    # driver = webdriver.Ie()

    # driver.get("http://www.baidu.com")

    return driver


if __name__ == '__main__':
    browser()