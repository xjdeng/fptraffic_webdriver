import requests, time

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
    response.raise_for_status()
    analysis = response.json()
    return analysis['description']['captions'][0]['text']

def label(browser):
    imgs = browser.find_elements_by_class_name("img-polaroid")
    for i in range(len(imgs)):        
        imgurl = imgs[i].get_attribute("src")        
        texts = browser.find_elements_by_partial_link_text("here to add a description")
        b = texts[i]        
        b.click()
        wait()        
        input_area = browser.find_element_by_class_name("input-large")        
        input_area.click()
        wait()
        imgtxt = caption(imgurl)        
        input_area.send_keys(imgtxt)        
        checkbox = browser.find_element_by_css_selector(".icon-ok.icon-white")
        checkbox.click()
        wait()
        
def wait(seconds = 2):
    time.sleep(seconds)