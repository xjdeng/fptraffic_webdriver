import EasyWebdriver
browser = EasyWebdriver.Chrome()

imgs = browser.find_elements_by_class_name("img-polaroid")
a = imgs[0]
imgurl = a.get_attribute("src")

edits = browser.find_elements_by_class_name("icon-edit")

texts = browser.find_elements_by_partial_link_text("here to add a description")

b = texts[0]

b.click()

input_area = browser.find_element_by_class_name("input-large")

input_area.click()

input_area.send_keys("testing")

checkbox = browser.find_element_by_css_selector(".icon-ok.icon-white")

checkbox.click()