from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import quickstart


with open('urls.txt', 'r') as file:
    urls = file.readlines()

firefox_profile_directory = 'C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/g47ns8ku.default-release-1708007965804'
firefox_options = webdriver.FirefoxOptions()
firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_directory)

url = "https://www.facebook.com/story.php?story_fbid=5143913235722860&id=251509411629958&mibextid=WC7FNe"


for url in urls:
    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.get(url)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"xqcrz7y x14yjl9h xudhj91 x18nykt9 xww2gxu x1lliihq x1w0mnb xr9ek0c x1n2onr6\"]")))
    sleep(4)
    spans = driver.find_elements(By.TAG_NAME, "span")
    print(len(spans))
    for span in spans:
        if "Most relevant" in span.text:
            driver.execute_script("arguments[0].scrollIntoView(false);", span)
            span.click()
            break
    sleep(2)
    spans = driver.find_elements(By.CSS_SELECTOR, "span[class=\"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xk50ysn xzsf02u x1yc453h\"]")
    print(len(spans))
    for span in spans:
        if "Newest" in span.text:
            span.click()
            break

    sleep(5)
    flag = 0
    initial_count = 0
    while(True):
        try:
            profiles = driver.find_elements(By.CSS_SELECTOR, "div[class=\"x1n2onr6 x1swvt13 x1iorvi4 x78zum5 x1q0g3np x1a2a7pz\"]")
            print(len(profiles))
            if initial_count != len(profiles):
                initial_count = len(profiles)
                flag = 0
            else:
                flag += 1
            
            if flag >=5:
                break

            view_more_comments_button = driver.find_elements(By.CSS_SELECTOR, "div[class=\"x78zum5 x13a6bvl\"]")[1].find_element(By.TAG_NAME, "span")
            driver.execute_script("arguments[0].scrollIntoView(true);", view_more_comments_button)
            view_more_comments_button.click()
            sleep(5)
        except:
            pass

    profile_links = []
    dates = []
    profiles = driver.find_elements(By.CSS_SELECTOR, "div[class=\"x1n2onr6 x1swvt13 x1iorvi4 x78zum5 x1q0g3np x1a2a7pz\"]")
    print(len(profiles))
    for profile in profiles:
        profile_links.append(profile.find_element(By.TAG_NAME, "a").get_attribute('href'))
        dates.append(profile.find_element(By.CSS_SELECTOR, "li[class=\"x1rg5ohu x1emribx x1i64zmx\"]").text)

    print(len(profile_links))

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
                    # country = driver.find_element(By.CSS_SELECTOR, "a[class=\"x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv x1fey0fg\"]").text
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
            print(f"Date that comment was made: {dates[index]}")
            print(f"Profile Link: {driver.current_url}")

            data = []
            data.append(name)
            data.append(city)
            data.append(country)
            data.append(job_title)
            data.append(phone_number)
            data.append(dates[index])
            data.append(driver.current_url)

            quickstart.main()
            last_index = quickstart.getColumnCount()
            print(last_index)
            RANGE_NAME = f'Sheet1!A{last_index + 2}:G'
            quickstart.insert_data(RANGE_NAME, data)
        except:
            pass

        index += 1

    driver.quit()
    sleep(10)


