## Log in to Static Web Page using Scrapy

Scrapy is a free and open-source Python web crawling framework that allows developers to scrape and extract data from websites in a structured and efficient way. It provides a set of powerful tools for extracting the data, cleaning it, and storing it in a structured format such as JSON or CSV.

Many websites require users to log in before allowing them to access certain pages or data. This makes it challenging for web scrapers to obtain the information they need. 

This project provides an easy-to-use solution that demonstrates the login process to [openlibrary.org]('https://openlibrary.org/account/login') page using a username and password.


### Installation

To run this project, you need to have Python 3.x and python-dotenv installed on your system. You can install the required Python packages by running the following command:

<code>
pip install -r requirements.txt
</code>

### Usage

To run the spider, make sure you are in the directory containing the `scrapy.cfg` file and run the following command:
<code>
scrapy crawl login
</code>

### Contributing

If you find a bug or have a suggestion for improvement, please create an issue on the GitHub repository or submit a pull request. Contributions are always welcome!
