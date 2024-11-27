from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--log-level=3")
    try:
        driver = webdriver.Chrome()
    except:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    finally:
        return driver

def main():
    driver = get_driver()

    driver.get('https://github.com/login?return_to=%2Fsponsors%2FPrem-ium%2Fsponsorships%3Ftier_id%3D308205')
    driver.execute_script("alert('Automation is only available for Gold Sponsors under the \"sponsor\" repository. The purpose of this script is to identify Python as the language of the repo/project.\\n Interested users are encouraged to become Gold Sponsors to access this feature.');")

    print("\nAutomation is only available for Gold Sponsors under the 'sponsor' repository.")
    print("The purpose of this script is to identify Python as the language of the repo/project.")
    print("Interested users are encouraged to become Gold Sponsors to access this feature.")
    sleep(1000)

if __name__ == '__main__':
    main()
