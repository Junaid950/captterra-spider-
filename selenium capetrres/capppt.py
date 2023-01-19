from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
def cat1():

    names = []
    links = []
    driver.get('https://www.capterra.com/categories')
    containers = driver.find_elements_by_xpath('//div[@class="browse  base-margin-bottom  base-padding-top"]//li/a')
    for container in containers:
        name = container.text
        link = container.get_attribute('href')
        names.append(name)
        links.append(link)
        print(name, link)

    return names[:1], links[:1]


def cat2():
    names, links = cat1()
    prod_links = []
    cat_names = []
    #driver.get('https://www.capterra.com/360-degree-feedback-software/')
    for name, link in zip(names, links):
        driver.get(link)
    while True:
        try:
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Show More")]')))
                driver.find_element_by_xpath('//div[contains(text(), "Show More")]').click()
        except:
            break
        containers = driver.find_elements_by_xpath('//div[@class="ProductCard__Root-sc-1aqkmbf-0 eiRAVe"]')

        for container in containers:
            name = container.find_element_by_xpath('.//h2').text
            cat_names.append(name)
            print(name)
        links =driver.find_elements_by_xpath('//div[@class="ProductCard__Root-sc-1aqkmbf-0 eiRAVe"]//a[@class="Link__StyledStandardLink-e9c1rj-0 eZMnyW"]')
        for link in links:
            prod =link.get_attribute('href')
            prod_links.append(prod)
            print(prod)



    return cat_names[:1], prod_links[:1]
def prod():
    cat_names, links = cat2()

    for link, cat_name in zip(links, cat_names):
        driver.get(link)
        print(link, cat_name)

    #d = driver.find_element_by_xpath('//div[@class="ReviewInfoSubheading__StarRatingCustom-eohjgy-1 jLfxXh StarRating__Root-sc-1tc8ja2-0 kFwEQb"]')

    try:
        about = driver.find_element_by_xpath('//div[@class="Section__Body-w4hkcm-1 jhCJZs"]').text
    except:
        about =" "
    print(about)
    try:
        best_for = driver.find_element_by_xpath('//div[@class="Section__Body-w4hkcm-1 jhCJZs"]//em').text
    except:
        best_for =" "
    print(best_for)
    try:
        ratings = driver.find_element_by_xpath('//div[@class="StarRating__Rating-sc-1tc8ja2-1 eLNbDF"]').text
    except:
        ratings =" "
    print(ratings)
    try:
        reviews = driver.find_element_by_xpath('//div[@class="StarRating__Count-sc-1tc8ja2-2 kZpsxs"]').text
    except:
        reviews =" "
    print(reviews)
    try:
        contact_details = driver.find_element_by_xpath('//div[@class="ProductSummary__CompanyDetailsLeft-mcm4i7-3 hBKuhE"]//p').text
    except:
        contact_details =" "
    print(contact_details)
    try:
        website_link =driver.find_element_by_xpath('//div[@class="ProductSummary__CompanyDetailsLeft-mcm4i7-3 hBKuhE"]//following-sibling::p').text
    except:
        website_link =" "
    print(website_link)
    try:
        Year_founded = driver.find_element_by_xpath( '//div[@class="ProductSummary__CompanyDetailsRight-mcm4i7-4 gpdJOr"]//p').text
    except:
        Year_founded=" "
    print(Year_founded)
    try:
        located=driver.find_element_by_xpath('//div[@class="ProductSummary__CompanyDetailsRight-mcm4i7-4 gpdJOr"]//following-sibling::p').text
    except:
        located=" "
    print(located)
    try:
        Pricing_overview= driver.find_element_by_xpath('//div[@class="PricingDetailsSection__Root-vqro3q-0 gwXvkQ"]//span').text
    except:
        Pricing_overview =" "
    print(Pricing_overview)
    try:
        over_all_rating =driver.find_elements_by_xpath('.//div[@class="RatingSection__RatingContainer-ttxeb9-0 bYTAgX"]//div[@class="StarRating__Rating-sc-9jwzgg-1 cAGyvf"]')[0].text
    except:
         over_all_rating =" "
    print(over_all_rating)
    try:
        Ease_of_Use=  driver.find_elements_by_xpath('.//div[@class="RatingSection__RatingContainer-ttxeb9-0 bYTAgX"]//div[@class="StarRating__Rating-sc-9jwzgg-1 cAGyvf"]')[1].text
    except:
     Ease_of_Use =" "
    print(Ease_of_Use)
    try:
        Customer_Service = driver.find_elements_by_xpath(
            './/div[@class="RatingSection__RatingContainer-ttxeb9-0 bYTAgX"]//div[@class="StarRating__Rating-sc-9jwzgg-1 cAGyvf"]')[
            2].text

    except:
        Customer_Service=" "
    print(Customer_Service)
    return

prod()
driver.close()



