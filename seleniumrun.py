from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def search(search_query):
    options = webdriver.ChromeOptions()
    options=Options()
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("https://www.gsmarena.com/")
    

    # Close the login popup if it appears
    try:
        close_button = driver.find_element(By.XPATH, '//button[contains(text(), "✕")]')
        close_button.click()
    except:
        pass

    # Enter the search query
    search_box = driver.find_element(By.XPATH, ".//input[@id='topsearch-text']")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.ENTER)
    search_box=driver.find_element(By.XPATH,"""//*[@id="review-body"]/div/ul/li[1]/a""").click()
    #search_box.submit()

    # Wait for the results to load and display the titles
    driver.implicitly_wait(5)  # You can increase this if your internet is slow

    img_element=driver.find_element(By.XPATH,"""//*[@id="body"]/div/div[1]/div/div[2]/div/a/img""")
    img_url=img_element.get_attribute('src')

    products = driver.find_elements(By.XPATH, """//*[@id="body"]/div/div[1]/div/div[1]/h1""")
    product_names=[b.text for b in products[:1]]
    for product in zip(product_names):
         product

    technologys = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[1]/tbody/tr[1]/td[2]/a""")
    technology_names=[b.text for b in technologys[:1]]
    for technology in zip(technology_names):
         technology

    announceds = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[2]/tbody/tr[1]/td[2]""")
    announced_names=[b.text for b in announceds[:1]]
    for announced in zip(announced_names):
         announced

    statuss = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[2]/tbody/tr[2]/td[2]""")
    status_names=[b.text for b in statuss[:1]]
    for status in zip(status_names):
         status
 
    dimensions = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[3]/tbody/tr[1]/td[2]""")
    dimension_names=[b.text for b in dimensions[:1]]
    for dimension in zip(dimension_names):
         dimension

    weights = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[3]/tbody/tr[2]/td[2]""")
    weight_count=[b.text for b in weights[:1]]
    for weight in zip(weight_count):
         weight

    sims = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[3]/tbody/tr[3]/td[2]""")
    sim_names=[b.text for b in sims[:1]]
    for sim in zip(sim_names):
         sim

    t_ypes = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[4]/tbody/tr[1]/td[2]""")
    t_ypes_names=[b.text for b in t_ypes[:1]]
    for t_ype in zip(t_ypes_names):
         t_ype

    sizes = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[4]/tbody/tr[2]/td[2]""")
    size_names=[b.text for b in sizes[:1]]
    for size in zip(size_names):
         size

    resolutions = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[4]/tbody/tr[3]/td[2]""")
    resolution_names=[b.text for b in resolutions[:1]]
    for resolution in zip(resolution_names):
         resolution

    oss = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[5]/tbody/tr[1]/td[2]""")
    os_names=[b.text for b in oss[:1]]
    for os in zip(os_names):
         os

    chipsets = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[5]/tbody/tr[2]/td[2]""")
    chipset_names=[b.text for b in chipsets[:1]]
    for chipset in zip(chipset_names):
         chipset

    cpus = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[5]/tbody/tr[3]/td[2]""")
    cpu_names=[b.text for b in cpus[:1]]
    for cpu in zip(cpu_names):
         cpu

    gpus = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[5]/tbody/tr[4]/td[2]""")
    gpu_names=[b.text for b in gpus[:1]]
    for gpu in zip(gpu_names):
         gpu

    cardslots = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[6]/tbody/tr[1]/td[2]""")
    cardslot_names=[b.text for b in cardslots[:1]]
    for cardslot in zip(cardslot_names):
         cardslot

    internals = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[6]/tbody/tr[2]/td[2]""")
    internal_names=[b.text for b in internals[:1]]
    for internal in zip(internal_names):
         internal

    singles = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[7]/tbody/tr[1]/td[2]""")
    single_names=[b.text for b in singles[:1]]
    for single in zip(single_names):
         single

    featuress = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[7]/tbody/tr[2]/td[2]""")
    features_names=[b.text for b in featuress[:1]]
    for features in zip(features_names):
         features

    videos = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[7]/tbody/tr[3]/td[2]""")
    video_names=[b.text for b in videos[:1]]
    for video in zip(video_names):
         video

    sin_gles = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[8]/tbody/tr[1]/td[2]""")
    sin_gle_names=[b.text for b in sin_gles[:1]]
    for sin_gle in zip(sin_gle_names):
         sin_gle

    feat_uress = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[8]/tbody/tr[2]/td[2]""")
    feat_ures_names=[b.text for b in feat_uress[:1]]
    for feat_ures in zip(feat_ures_names):
         feat_ures

    v_ideos = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[8]/tbody/tr[3]/td[2]""")
    v_ideo_names=[b.text for b in v_ideos[:1]]
    for v_ideo in zip(v_ideo_names):
         v_ideo

    loudspeakers = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[9]/tbody/tr[1]/td[2]""")
    loudspeaker_names=[b.text for b in loudspeakers[:1]]
    for loudspeaker in zip(loudspeaker_names):
         loudspeaker

    jacks = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[9]/tbody/tr[2]/td[2]""")
    jack_names=[b.text for b in jacks[:1]]
    for jack in zip(jack_names):
         jack

    wlans = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[1]/td[2]""")
    wlan_names=[b.text for b in wlans[:1]]
    for wlan in zip(wlan_names):
         wlan

    blutooths = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[2]/td[2]""")
    blutooth_names=[b.text for b in blutooths[:1]]
    for blutooth in zip(blutooth_names):
         blutooth

    positionings = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[2]/td[2]""")
    positioning_names=[b.text for b in positionings[:1]]
    for positioning in zip(positioning_names):
         positioning

    nfcs = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[4]/td[2]""")
    nfc_names=[b.text for b in nfcs[:1]]
    for nfc in zip(nfc_names):
         nfc

    radios = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[5]/td[2]""")
    radio_names=[b.text for b in radios[:1]]
    for radio in zip(radio_names):
         radio

    usbs = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[10]/tbody/tr[6]/td[2]""")
    usb_names=[b.text for b in usbs[:1]]
    for usb in zip(usb_names):
         usb

    sensorss = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[11]/tbody/tr/td[2]""")
    sensors_names=[b.text for b in sensorss[:1]]
    for sensors in zip(sensors_names):
         sensors

    ty_pes = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[12]/tbody/tr[1]/td[2]""")
    ty_pe_names=[b.text for b in ty_pes[:1]]
    for ty_pe in zip(ty_pe_names):
         ty_pe

    chargings = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[12]/tbody/tr[2]/td[2]""")
    charging_names=[b.text for b in chargings[:1]]
    for charging in zip(charging_names):
         charging

    colorss = driver.find_elements(By.XPATH, """//*[@id="specs-list"]/table[13]/tbody/tr[1]/td[2]""")
    colors_names=[b.text for b in colorss[:1]]
    for colors in zip(colors_names):
         colors



    driver.quit()

    return product[0],technology[0],announced[0],status[0],dimension[0],weight[0],sim[0],t_ype[0],size[0],resolution[0],os[0],chipset[0],cpu[0],gpu[0],cardslot[0],internal[0],single[0],features[0],video[0],sin_gle[0],feat_ures[0],v_ideo[0],loudspeaker[0],jack[0],wlan[0],blutooth[0],positioning[0],nfc[0],radio[0],usb[0],sensors[0],ty_pe[0],charging[0],colors[0],img_url


