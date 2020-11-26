#Librairies
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

def opendiscussion(nameofdiscussion, wait):
    target = nameofdiscussion
    x_arg = " //span[contains(@title, " + target + ")]"
    target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
    target.click()

def findnewmessages(whatsappdriver,messages, lastmessages, messagediv):
    lastmessages += messages
    messages = whatsappdriver.find_elements_by_css_selector(messagediv)
    if not messages in lastmessages:
        templist = []
        for message in messages:
            if not message in lastmessages:
                templist.append(message)
        messages = templist
        return messages, True, lastmessages
    else:
        return messages, False, lastmessages

def readmessagetext(message):
    messagetexts = []
    for i in message:
        try:
            messagetext = i.find_element_by_css_selector("span.copyable-text")
            messagetext = messagetext.find_element_by_css_selector("span")
            messagetexts.append(messagetext.text)
        except:
            messagetext = "No Desc"
            messagetexts.append(messagetext)
    return messagetexts

def findmessagetime(message):
    messagetimes = []
    for i in message:
        timeofmessage = i.find_element_by_css_selector("span._2JNr-")
        messagetimes.append(timeofmessage.text)
    return messagetimes

def findpadletsends(messages):
    indexes = []
    for i in range(len(messages)):
        endstr = 10
        if len(messages[i]) < endstr:
            endstr = len(messages[i])
        if "!padlet" in messages[i][0:endstr]:
            indexes.append(i)
    return indexes

def downloadimage(message, whatsappdriver, imgbtndiv, actbtndiv):
    imagebutton = message.find_element_by_css_selector(imgbtndiv)
    imagebutton.click()
    actionbuttons = whatsappdriver.find_element_by_css_selector(actbtndiv)
    downloadbutton = actionbuttons.find_element_by_xpath("//div[@title='Télécharger']")
    downloadbutton.click()
    closebutton = actionbuttons.find_element_by_xpath("//div[@title='Fermer']")
    closebutton.click()
    time.sleep(2)

def sendmessage(text, whatsappdriver, msginputdiv, msginput):
    text_box = whatsappdriver.find_elements_by_css_selector(msginputdiv)[1]
    text_box = text_box.find_element_by_css_selector(msginput)
    text_box.send_keys(text)
    text_box.send_keys(Keys.RETURN)

def findnewmessagesforcommands(whatsappdriver,messages, lastmessages, msgdiv):
    lastmessages += messages
    messages = whatsappdriver.find_elements_by_css_selector(msgdiv)
    if not messages in lastmessages:
        templist = []
        for message in messages:
            if not message in lastmessages:
                templist.append(message)
        messages = templist
        return messages, True, lastmessages
    else:
        return messages, False, lastmessages

def executecommands(commandtexts, commandindexes):
    answers = []
    for i in commandindexes:
        if "instructions" in commandtexts[i] or "help" in commandtexts[i] or "aide" in commandtexts[i]:
            reply = "Autopadlet: Bonjour, bienvenue dans le guide d'utilisation d'autopadlet. Ce systeme permet de transferer automatiquement les photos postées sur ce groupe whatsapp sur le padlet. Liste des commandes possibles: [!padlet syntaxe: instructions pour qu'une image soit transferée automatiquement], [!padlet liste catégories: liste des catégories du padlet], [!padlet lien padlet: renvoie le lien pour aller sur le padlet]"
        elif "syntaxe" in commandtexts[i] or "transfert" in commandtexts[i]:
            reply = "Afin qu'une photo soit transférée, suivez les instructions qui suivent: 1. Choisissez la photo a mettre sur whatsapp 2. Dans la description de la photo, écrivez en respectant la syntaxe: !padlet {Code correspondant a la catégorie dans le padlet (envoyer la commande \"!padlet liste catégories' pour avoir la liste des catégories)} {Titre a donner a l'image} ; {description a donner a l'image}\" (remplacer le texte dans les {} par ce qu'il faut et ne recopiez pas les {}) Exemple: !padlet C1EX Exemple;Voici un exemple de la syntaxe"
        elif "liste catégories" in commandtexts[i]:
            #reply = "Autopadlet: Bonjour, voici la liste des catégories dans le padlet: [DS, DM et interros: code = DSDM],[Progression Prévue: code = PP],[Chapitre {nombre du chapitre} cours: code = C{nombre du chapitre}C (ex: cours chapitre 1: code = C1C)],[[Chapitre {nombre du chapitre} exercices: code = C{nombre du chapitre}EX (ex: exercices chapitre 1: code = C1EX)]"
            reply = "Autopadlet: Bonjour, voici la liste des catégories dans le padlet: C1, C2, C3, C4"
        elif "lien padlet" in commandtexts[i]:
            #reply = "Autopadlet: Bonjour, voici le lien vers le padlet: https://padlet.com/julietierno/ksuy76z8oopbxk7e"
            reply = "Autopadlet: Bonjour, voici le lien vers le padlet: https://padlet.com/thilochalas/bz3zhbzqmuzhd1qm"
        elif "kill_autopadlet" in commandtexts[i]:
            reply = "(!padlet kill) Autopadlet: Killing the autopadlet process"
        elif "statut" in commandtexts[i]:
            reply = "Autopadlet est en ligne: " + time.strftime("%X %x")
        else:
            reply = "Erreur Autopadlet: Cette commande n'existe pas"
        answers.append(reply)
    return answers
