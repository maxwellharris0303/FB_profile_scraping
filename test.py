from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import quickstart


firefox_profile_directory = 'C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/g47ns8ku.default-release-1708007965804'
firefox_options = webdriver.FirefoxOptions()
firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_directory)

url = "https://www.facebook.com/story.php?story_fbid=pfbid0nURTgrjuWAN4PEToAw9YX2KYHyfzcHPNFPv7fa2yFvpcr2BGz4BhEiWTaiuoznH5l&id=251509411629958&eav=Afal-XUBjZyzxkiChB6V3K9g__eaEkGF-90-UP5GWWyY_O7WwTdQA8Uf-nw_Om33Ax4&m_entstream_source=timeline&anchor_composer=false&paipv=0&_rdr"

driver = webdriver.Firefox(options=firefox_options)
driver.maximize_window()

profile_links = ['https://www.facebook.com/terrylim.tweet?comment_id=Y29tbWVudDo1Mzk1NDI2MTU3MjM4MjMyXzEzMzE2OTgwMTA4MzY0MDM%3D']


index = 0
for _ in range(len(profile_links)):
    try:
        driver.get(profile_links[index])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x1qjc9v5 xozqiw3 x1q0g3np x1l90r2v x1ve1bff\"]")))

        name = driver.find_element(By.CSS_SELECTOR, "div[class=\"x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x1qjc9v5 xozqiw3 x1q0g3np x1l90r2v x1ve1bff\"]").find_element(By.TAG_NAME, "h1").text
        
        city = ""
        country = ""
        job_title = ""
        phone_number = ""

        spans = driver.find_elements(By.CSS_SELECTOR, "span[class=\"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h\"]")
        for span in spans:
            if "Lives in" in span.text:
                a_tag = span.find_element(By.TAG_NAME, "a")
                city = a_tag.text
                driver.execute_script("arguments[0].scrollIntoView(false);", a_tag)
                actions = ActionChains(driver)
                actions.move_to_element(a_tag).perform()
                sleep(2)
                country = driver.find_element(By.CSS_SELECTOR, "span[style=\"-moz-box-orient: vertical; -webkit-line-clamp: 5; display: -webkit-box;\"]").text
                break

        try:
            img = driver.find_elements(By.CSS_SELECTOR, "img[src=\"https://static.xx.fbcdn.net/rsrc.php/v3/yp/r/Q9Qu4uLgzdm.png\"]")[-1:]
            print(img)
            two_levels_up_element = img[0].find_element(By.XPATH, "../..")
            job_title = two_levels_up_element.find_element(By.TAG_NAME, "span").text
        except:
            pass

        try:
            img = driver.find_element(By.CSS_SELECTOR, "img[src=\"https://static.xx.fbcdn.net/rsrc.php/v3/yu/r/lnfZfe30sq0.png\"]")
            two_levels_up_element = img.find_element(By.XPATH, "../..")
            phone_number = two_levels_up_element.find_element(By.TAG_NAME, "span").text
        except:
            pass
        

        print(f"Name: {name}")
        print(f"City: {city}")
        # country = country.split(", ")[-1]
        print(f"Country: {country}")
        print(f"Job title: {job_title}")
        print(f"Phone number: {phone_number}")
        print(f"Profile Link: {driver.current_url}")


    except:
        pass

    index += 1


