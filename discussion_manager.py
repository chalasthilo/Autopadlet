import csvReader

discussions = [{"discussionname": 'Mainaccount',
                "padletlink": "https://padlet.com/thilochalas/bz3zhbzqmuzhd1qm",
                "categories": ["First column", "second column", "third", "fourth", "NONE"],
                "catcodes": ["C1", "C2", "C3", "C4", "VOID"],
                "catids": ["section-41504012", "section-41504018", "section-41504020", "section-41504022", "section-52239313"],
                "messages": [],
                "lastmessages": [],
                "newmessagefound": False,
                "commands": [],
                "lastcommands": [],
                "newcommandsfound": False},
                
                {"discussionname": 'Multipadlet?',
                "padletlink": "https://padlet.com/thilochalas/multipadlet",
                "categories": ["Column ONE", "Column TWO", "Column THREE", "Column Four", "NONE"],
                "catcodes": ["C1", "C2", "C3", "C4", "VOID"],
                "catids": ["section-51673453", "section-51673465", "section-51673480", "section-51673489", "section-52239330"],
                "messages": [],
                "lastmessages": [],
                "newmessagefound": False,
                "commands": [],
                "lastcommands": [],
                "newcommandsfound": False},

                ]
###################################################################################################
discussions_a_ajouter = [{"discussionname": 'Mainaccount',
                "padletlink": "https://padlet.com/thilochalas/bz3zhbzqmuzhd1qm",
                "categories": ["First column", "second column", "third", "fourth", "NONE"],
                "catcodes": ["C1", "C2", "C3", "C4", "VOID"],
                "catids": ["section-41504012", "section-41504018", "section-41504020", "section-41504022", "section-52239313"],
                "messages": [],
                "lastmessages": [],
                "newmessagefound": False,
                "commands": [],
                "lastcommands": [],
                "newcommandsfound": False}
                ]
###################################################################################################
def sauvegarder_discussions(discussions):
    csvReader.exportJSON("discussionswithpadlets.json", discussions)
def ajouter_discussions(discussions_a_ajouter):
    discussions = csvReader.importJSON("discussionswithpadlets.json")
    discussions += discussions_a_ajouter
    sauvegarder_discussions(discussions)

    
###################################################################################################
#mettre les fonctions ici
