# Web scraping - beleške

**WARNING**
Avoid putting your *passwords* in *source code* whenever possible. 
It’s easy to accidentally leak your passwords to others when they are left unencrypted on your hard drive. 
If possible, have your program prompt users to enter their passwords from the keyboard using the 
*pyinputplus.inputPassword()* function described in Chapter 8.

    pyinputplus.inputPassword()

## Set the Environment Variable

For Zsh (.zshrc):

    echo 'export MY_PASSWORD="your_password_here"' >> ~/.zshrc
    source ~/.zshrc

    echo 'export LINKEDIN_EMAIL="milcanovicn@gmail.com"' >> ~/.zshrc
    source ~/.zshrc

For Bash (.bash_profile):

    echo 'export MY_PASSWORD="your_password_here"' >> ~/.bash_profile
    source ~/.bash_profile

*Those commands are meant to be executed in the terminal.*

Password Linkedin:

    echo 'export MY_PASSWORD="_____________"' >> ~/.zshrc
    source ~/.zshrc

    password = os.getenv('LINKEDIN_PASSWORD')

**Sigurnost**: Razmisli o korišćenju *keychain* ili *password manager* za čuvanje osetljivih informacija.


**Idealni klijent** (musko ili zensko): 1. Raspolaze velikom kolicinom novca 2. Kreativna osoba / ima viziju / otvorenog je uma 3. Digitalna, IT industrija, moda (ne samo visoka moda, vec i sportska odeca itd.), marketing 4. Na istaknutoj je poziciji / odlucuje o pitanjima dizajna 5. Treba mu vizuelni identitet brenda / graficki dizajn 6. Nas covek (ili zena) ili covek iz razvijene zapadne zemlje 7. Neko ko zeli da plati za dobro obavljen posao...


## Postavi Razuman Interval Između Zahteva

Dodaj nasumične pauze između zahteva kako bi simulirao ljudsko ponašanje. Na primer:

    import random
    import time
# Nasumična pauza između 2 i 5 sekundi
    time.sleep(random.uniform(2, 5))


## Postavi User-Agent

Postavi User-Agent kako bi izgledao kao različiti pretraživači:
python
Copy code
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

    options = Options()
    ptions.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
    driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=options)


## Primer Koda za Pretraživanje Više Stranica

**python**
*Copy code*

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    import random
    import pandas as pd

Postavi WebDriver

    driver = webdriver.Chrome()
    driver.get('https://www.linkedin.com/login')

Prijavi se (korišćenje prethodnih koraka)

Nasumična pauza između 2 i 5 sekundi

    def random_sleep():
    time.sleep(random.uniform(2, 5))

    data = []
    for page in range(1, 11):  # Na primer, 10 stranica
    search_url = f'https://www.linkedin.com/search/results/people/?keywords=graphic%20design&page={page}'
    driver.get(search_url)
    
    random_sleep()      Pauza

    people = driver.find_elements(By.CSS_SELECTOR, 'li.reusable-search__result-container')
    for person in people:
    name = person.find_element(By.CSS_SELECTOR, 'span.actor-name').text
    position = person.find_element(By.CSS_SELECTOR, 'p.subline-level-1').text
    location = person.find_element(By.CSS_SELECTOR, 'p.subline-level-2').text
    data.append({'Name': name, 'Position': position, 'Location': location})
    
    random_sleep()      Pauza

    df = pd.DataFrame(data)
    df.to_csv('linkedin_data.csv', index=False)

    driver.quit()

_____________________________________

    from dataclasses import dataclass
    from time import sleep
    from selenium.webdriver import Chrome
    from . import constants as c

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC


    @dataclass
    class Contact:
    name: str = None
    occupation: str = None
    url: str = None


    @dataclass
    class Institution:
    institution_name: str = None
    linkedin_url: str = None
    website: str = None
    industry: str = None
    type: str = None
    headquarters: str = None
    company_size: int = None
    founded: int = None


    @dataclass
    class Experience(Institution):
    from_date: str = None
    to_date: str = None
    description: str = None
    position_title: str = None
    duration: str = None
    location: str = None


    @dataclass
    class Education(Institution):
    from_date: str = None
    to_date: str = None
    description: str = None
    degree: str = None


    @dataclass
    class Interest(Institution):
    title = None


    @dataclass
    class Accomplishment(Institution):
    category = None
    title = None


    @dataclass
    class Scraper:
    driver: Chrome = None
    WAIT_FOR_ELEMENT_TIMEOUT = 5
    TOP_CARD = "pv-top-card"

    @staticmethod
    def wait(duration):
        sleep(int(duration))

    def focus(self):
        self.driver.execute_script('alert("Focus window")')
        self.driver.switch_to.alert.accept()

    def mouse_click(self, elem):
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(elem).perform()

    def wait_for_element_to_load(self, by=By.CLASS_NAME, name="pv-top-card", base=None):
        base = base or self.driver
        return WebDriverWait(base, self.WAIT_FOR_ELEMENT_TIMEOUT).until(
            EC.presence_of_element_located(
                (
                    by,
                    name
                )
            )
        )

    def wait_for_all_elements_to_load(self, by=By.CLASS_NAME, name="pv-top-card", base=None):
        base = base or self.driver
        return WebDriverWait(base, self.WAIT_FOR_ELEMENT_TIMEOUT).until(
            EC.presence_of_all_elements_located(
                (
                    by,
                    name
                )
            )
        )


    def is_signed_in(self):
        try:
            WebDriverWait(self.driver, self.WAIT_FOR_ELEMENT_TIMEOUT).until(
                EC.presence_of_element_located(
                    (
                        By.CLASS_NAME,
                        c.VERIFY_LOGIN_ID,
                    )
                )
            )

            self.driver.find_element(By.CLASS_NAME, c.VERIFY_LOGIN_ID)
            return True
        except Exception as e:
            pass
        return False

    def scroll_to_half(self):
        self.driver.execute_script(
            "window.scrollTo(0, Math.ceil(document.body.scrollHeight/2));"
        )

    def scroll_to_bottom(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

    def scroll_class_name_element_to_page_percent(self, class_name:str, page_percent:float):
        self.driver.execute_script(
            f'elem = document.getElementsByClassName("{class_name}")[0]; elem.scrollTo(0, elem.scrollHeight*{str(page_percent)});'
        )

    def __find_element_by_class_name__(self, class_name):
        try:
            self.driver.find_element(By.CLASS_NAME, class_name)
            return True
        except:
            pass
        return False

    def __find_element_by_xpath__(self, tag_name):
        try:
            self.driver.find_element(By.XPATH,tag_name)
            return True
        except:
            pass
        return False

    def __find_enabled_element_by_xpath__(self, tag_name):
        try:
            elem = self.driver.find_element(By.XPATH,tag_name)
            return elem.is_enabled()
        except:
            pass
        return False

    @classmethod
    def __find_first_available_element__(cls, *args):
        for elem in args:
            if elem:
                return elem[0]