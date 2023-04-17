import scrapy
from scrapy import FormRequest

from LoginStatic.settings import EMAIL, PASSWORD, ALIAS

class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["openlibrary.org"]
    start_urls = ["https://openlibrary.org/account/login"]

    def parse(self, response):
        yield FormRequest.from_response(
            response,
            formid = 'register',
            formdata = {
                'username': EMAIL,
                'password': PASSWORD,
                'redirect': f'https://openlibrary.org/people/{ALIAS}',
                'debug_token': '',
                'login': 'Log In'
            },
            callback = self.process_data
        )

    def process_data(self, response):
        
        if response.xpath("//img[@class='account__icon']").get():
            print("Logged In...")
