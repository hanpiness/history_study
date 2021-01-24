import requests
from lxml import etree


class Login(object):
    def __init__(self):
        self.headers = {
         'Referer':'https://github.com/',
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
         'Host':'github.com'
         }
        self.login_url = 'https://github.com/login'
        self.post_url = 'http://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

def token(self):
    response = self.session.post(self.login_url,headers=self.headers)
    selector = etree.HTML(response.text)
    token = selector.xpath('//div/input[2]/@value')[0]
    return token
def login()


