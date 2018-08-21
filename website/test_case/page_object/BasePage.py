from time import sleep


class Page():
    '''页面基础'''
    def __init__(self, driver):
        '''初始化'''
        self.base_url = 'http://192.168.2.222:8808'
        self.driver = driver

    def _open(self, url):
        url_ = self.base_url + url
        print("Test page is:%s" % url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert self.driver.current_url == url_, 'Did not land on %s' % url_

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)
