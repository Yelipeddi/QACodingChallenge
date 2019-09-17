# To Test static HTML Page using pytest
 
import requests
class TestStaticHTMLPage:

    def test_google_website(self):
	url = "https://www.google.com/"
	webPage = requests.get(url)
	# If the status code is 200, the google website is up
	assert int(webPage.status_code) == 200 
