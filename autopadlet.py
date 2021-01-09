#Librairies
#selenium
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#other
import os
import time
import pyautogui
#custom
import whatsappweb
import padlet
import csvReader

#Page links
whatsapplink = "https://web.whatsapp.com/"
#padletlink = "https://padlet.com/thilochalas/bz3zhbzqmuzhd1qm"
padletlink = "https://padlet.com/julietierno/ksuy76z8oopbxk7e"

#Discussion name
#discussionname = '"Mainaccount"'
discussionname = '"Maths expertes Tle"'
#discussionname = '"Existance Muy Caliente"'

#Whatsapp message reading
messages = []
lastmessages = []
newmessagefound = False

commands = []
lastcommands = []
newcommandsfound = False

#div names
internetstatusdiv = "div." + "pcVTC" 
imgmsgdiv = "div." + "j9c-4" 
imgpicdiv = "div." + "_1mTER" 
actionbuttonsdiv = "div." + "_1RLgD" 
msginputdiv = "div." + "_2HE1Z" 
msginputfield = "div." + "_1awRl" 
normmsgdiv = "div." + "_2tbXF" 
msgtimespan = "span." + "_2JNr-"

#Padlet categories
#categories = ["First column", "second column", "third", "fourth"]
#catcodes = ["C1", "C2", "C3", "C4"]
#catids = ["section-41504012", "section-41504018", "section-41504020", "section-41504022"]

categories = ["DS,DM,Interros", "Progression Prevue", "Chapitre 1 Cours", "Chapitre 2 Cours", "Chapitre 3 Cours", "Chapitre 4 Cours", "Chapitre 5 Cours", "Chapitre 6 Cours", "Chapitre 7 Cours", "Chapitre 1 Exercices", "Chapitre 2 Exercices", "Chapitre 3 Exercices", "Chapitre 4 Exercices", "Chapitre 5 Exercices", "Chapitre 6 Exercices", "Chapitre 7 Exercices"]
catcodes = ["DSDM", "PP", "C1C", "C2C", "C3C", "C4C", "C5C", "C6C", "C7C", 'C1EX', 'C2EX', 'C3EX', 'C4EX', 'C5EX', 'C6EX', 'C7EX']
catids = ["section-40996450", "section-41017892", "section-40996545", "section-4096706", "section-40996607", "section-40996788", "section-40997070", "section-40996932", "section-40997157", "section-40996563", "section-40996739", "section-40996630", "section-40996816", "section-40997097", "section-40996954", "section-40997172"]

#other
killtaskrequested = False
recoveredcrashes = 0


def initialisation(whatsapplink, discussionname, padletlink, commands, lastcommands):
    #Opening upload log
    uploadlog = csvReader.importCSV("uploadedimages.csv")

    #fetching chrome profile
    os.system("rm -r /home/pi/Desktop/Projet_Transfert_Auto_Padlet/chromedata/Default")
    os.system("cp -r /home/pi/.config/chromium/Default /home/pi/Desktop/Projet_Transfert_Auto_Padlet/chromedata")

    #setting chrome options
    coptions = webdriver.ChromeOptions()
    coptions.add_argument("--user-data-dir=/home/pi/Desktop/Projet_Transfert_Auto_Padlet/chromedata")
    #Opening whatsapp and navigating to discussion
    whatsappdriver = selenium.webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", options=coptions)
    whatsappdriver.get(whatsapplink)
    time.sleep(5)
    wait = WebDriverWait(whatsappdriver, 600)
    whatsappweb.opendiscussion(discussionname, wait)
    #Opening padlet
    padletdriver = selenium.webdriver.Chrome(os.path.expanduser("/usr/lib/chromium-browser/chromedriver"))
    padletdriver.get(padletlink)
    commands, newcommandsfound, lastcommands = whatsappweb.findnewmessagesforcommands(whatsappdriver, commands, lastcommands, normmsgdiv)
    return uploadlog,whatsappdriver,padletdriver,commands,newcommandsfound,lastcommands

uploadlog,whatsappdriver,padletdriver,commands,newcommandsfound,lastcommands = initialisation(whatsapplink, discussionname, padletlink, commands, lastcommands)

print("Enter loop")
while True :
    try:
        #print("/////////////////////////////////////////////Detecting new messages/////////////////////////////////////////////")
        messages, newmessagefound, lastmessages = whatsappweb.findnewmessages(whatsappdriver, messages, lastmessages, imgmsgdiv)
        if newmessagefound and messages != []:
            print("New message(s) found") 
            newmessagefound = False
            messagetexts = whatsappweb.readmessagetext(messages)
            messagetimes = whatsappweb.findmessagetime(messages, msgtimespan)
            padletsends = whatsappweb.findpadletsends(messagetexts)
            categorized = padlet.setimagecategories(messagetexts, padletsends, categories, catcodes, catids)
            messages_with_data = padlet.setmessagedata(messages, categorized, messagetexts, messagetimes, catcodes)
            print(messages_with_data)
            for message in messages_with_data:
                if message["category_id"] != "ERR":
                    if padlet.checkuploads(message, uploadlog):
                        uploadlog.append({"uploaddata": (message["category_name"] + message["Title"] + message["Description"] + message["Time"])})
                        padlet.updateuploadlog(uploadlog)
                        whatsappweb.downloadimage(message["message"], whatsappdriver, imgpicdiv, actionbuttonsdiv)
                        padlet.postonpadlet(message, padletdriver)
                        whatsappweb.sendmessage(('''L'image"''' + message["Title"] + '" est sur le padlet'), whatsappdriver, msginputdiv, msginputfield)
                else:
                    whatsappweb.sendmessage(("Erreur dans le code de catégorie padlet"), whatsappdriver, msginputdiv, msginputfield)      
        #print("/////////////////////////////////////////////Detecting new commands/////////////////////////////////////////////")
        commands, newcommandsfound, lastcommands = whatsappweb.findnewmessagesforcommands(whatsappdriver, commands, lastcommands, normmsgdiv)
        if newcommandsfound and commands != []:
            print("New commands found")
            newcommandsfound = False
            commandtexts = whatsappweb.readmessagetext(commands)
            commandstoexecute = whatsappweb.findpadletsends(commandtexts)
            responses = whatsappweb.executecommands(commandtexts, commandstoexecute)
            commandtexts, commandstoexecute = [],[]
            for text in responses:
                whatsappweb.sendmessage(text, whatsappdriver, msginputdiv, msginputfield)
                if text == "Autopadlet: Killing the autopadlet process":
                    killtaskrequested = True
                    time.sleep(5)
                    print("AUTOPADLET PROCESS TERMINATED")
                    whatsappdriver.quit()
                    padletdriver.quit()
                    quit()
                    exit()
                    break
        try:
            internetloss = whatsappdriver.find_element_by_css_selector(internetstatusdiv)
            internetloss = internetloss.text
            if internetloss != "L'ordinateur n'est pas connecté":
                raise Exception("Not lost")
            print("INTERNET: CONNEXION LOST")
            while "pas connecté" in internetloss:
                print("INTERNET: WAITING FOR RESPONSE")
                time.sleep(1)
                try:
                    internetloss = whatsappdriver.find_element_by_css_selector(internetstatusdiv)
                    internetloss = internetloss.text
                except:
                    internetloss = " "
            time.sleep(10)
            commands, newcommandsfound, lastcommands = whatsappweb.findnewmessagesforcommands(whatsappdriver, commands, lastcommands, normmsgdiv)
        except:
            #print("Internet connexion is stable")
            pass
        time.sleep(5)
    except:
        if killtaskrequested:
            quit()
        print("AUTOPADLET: FATAL ERROR OCCURED")
        print("AUTOPADLET: RESTARTING")
        for i in range(5):
            pyautogui.press("esc")
        whatsappdriver.quit()
        padletdriver.quit()
        uploadlog,whatsappdriver,padletdriver,commands,newcommandsfound,lastcommands = initialisation(whatsapplink, discussionname, padletlink, commands, lastcommands)
        recoveredcrashes += 1
        print("AUTOPADLET: RECOVERED CRASHES = "+str(recoveredcrashes))
