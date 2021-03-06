import requests, time
from selenium.common.exceptions import ElementNotInteractableException, StaleElementReferenceException

def caption(image_url):
    with open('subscription_key.key','r') as f:
        subscription_key = f.read()
    vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"

    vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
    
    vision_analyze_url = vision_base_url + "describe"
       
    headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
    params   = {'visualFeatures': 'Categories,Description,Color'}
    data     = {'url': image_url}
    response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
    goahead = False
    while goahead == False:
        try:
            response.raise_for_status()
            goahead = True
        except requests.exceptions.HTTPError:
            wait()
            
    analysis = response.json()
    return analysis['description']['captions'][0]['text']

def label(browser, start = 0):
    imgs = browser.find_elements_by_class_name("img-polaroid")
    texts = browser.find_elements_by_partial_link_text("here to add a description")
    for i in range(start, len(imgs)):        
        imgurl = imgs[i].get_attribute("src")        
        b = texts[i]        
        b.click()
        wait()        
        input_area = browser.find_element_by_class_name("input-large")
        goahead = False
        while goahead == False:
            try:
                input_area.click()
                wait()
                imgtxt = caption(imgurl)        
                input_area.send_keys(imgtxt)        
                checkbox = browser.find_element_by_css_selector(".icon-ok.icon-white")
                checkbox.click()
                wait()
                goahead = True
            except ElementNotInteractableException:
                wait()
            except StaleElementReferenceException:
                goahead = True #skip if can't be found

        
def wait(seconds = 2):
    time.sleep(seconds)