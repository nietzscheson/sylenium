import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_structry():

    options = Options()
    
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get("https://example.com")
    assert "Example Domain" in driver.title
    driver.quit()