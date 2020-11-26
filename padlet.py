#Librairies
import selenium
from selenium.webdriver.common.keys import Keys
import time
import os
import csvReader
import pyautogui

def setimagecategories(messagetexts, padletsends, categories, catcodes, catids):
    categorized = []
    for i in padletsends:
        codefound = False
        for code in range(len(catcodes)):
            if catcodes[code] in messagetexts[i]:
                categorized.append({'category_name': categories[code], 'category_id': catids[code], 'message_id': i})
                codefound = True
        if codefound == False :
            categorized.append({'category_name': "Codenotfound error", 'category_id': "ERR", 'message_id': i})
    return categorized

def setmessagedata(messages, categorized, messagetexts, messagetimes, catcodes):
    messagesdata = []
    for message in categorized:
        if message["category_id"] != "ERR":
            text = messagetexts[message["message_id"]]
            text = text.replace("!padlet ", "")
            for code in range(len(catcodes)):
                if catcodes[code] in text:
                    text = text.replace(catcodes[code], "")
            text = text.split(";",1)
            if len(text) != 2:
                if len(text) == 1:
                    text.append("")
                else:
                    text = ["Sans Titre", ""]
        else:
            text = ["Erreur", "Erreur: ce code de categorie padlet n'existe pas"]
        messagesdata.append({"category_name": message["category_name"], "category_id": message["category_id"], "message": messages[message["message_id"]], "Title": text[0], "Description": text[1], "Time": messagetimes[message["message_id"]]})
    return messagesdata

def postonpadlet(messagedata, padletdriver):
    downloads = os.listdir("/home/pi/Downloads/")
    for name in downloads:
        if "WhatsApp" in name:
            filename = name
            break
    print(messagedata["category_id"])
    column = padletdriver.find_element_by_id(messagedata["category_id"])
    addpostdiv = column.find_element_by_class_name("add-post")
    addpostbutton = addpostdiv.find_element_by_class_name("flat-button")
    addpostbutton.click()
    postdiv = column.find_element_by_xpath("//div[@id='wish-new']")
    postdiv = postdiv.find_element_by_css_selector("div.real-wish")
    textsection = postdiv.find_element_by_css_selector("section.words")
    titlesection = textsection.find_element_by_css_selector("textarea.multiline-input")
    titlesection.send_keys(messagedata["Title"])
    titlesection.send_keys(Keys.RETURN)
    descriptionsection = textsection.find_element_by_css_selector("trix-editor")
    descriptionsection.send_keys(messagedata["Description"])
    #set description
    uploadbutton = postdiv.find_element_by_xpath("//button[@title='Upload']")
    uploadbutton.click()
    uploadpanel = padletdriver.find_element_by_css_selector("div.side-panel-with-curtain")
    uploadpanel = uploadpanel.find_element_by_css_selector("div.file-browser-input-body")
    pickfilebtn = uploadpanel.find_element_by_css_selector("div.raised-button")
    pickfilebtn.click()
    time.sleep(5)
    pyautogui.write("/home/pi/Downloads/" + filename)
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(10)
    tempstring = ""
    for char in filename:
        if char != " ":
            tempstring += char
        else:
            tempstring += ("\\" + " ")
    filename = tempstring
    os.system("cd /home/pi/Downloads/")
    os.system("rm -r /home/pi/Downloads/WhatsApp*")
    #padletdriver.click()

def checkuploads(message, uploadedimages):
    messagetocheck = message["category_name"] + message["Title"] + message["Description"]
    for upload in uploadedimages:
        if upload["uploaddata"] == messagetocheck:
            return False
    return True

def updateuploadlog(uploadlog):
    csvReader.exportCSV(uploadlog,"uploadedimages.csv")