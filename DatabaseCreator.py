import pymongo
import os
from pymongo import MongoClient

#client = MongoClient()
#print(client)

#db = client.blackolive
#specials = db.specials

directory_in_str = "/Users/victorochoa/Desktop/bo-specials/plainTxtSpecials/"
directory = os.fsencode(directory_in_str)

starts_list = ["A.", "B.", "C.", "D.", "E.", "F.", "G.", "H."]
#listdir() returns a list version of the files in the directory
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    #Opens file with resources, auto closes
    with open(f"plainTxtSpecials/{filename}") as f:

        file_string = f.read()
        if file_string.find("BREAKFAST") != -1:
            continue

        start_index = file_string.find("A.")
        file_string = file_string[start_index:]

        while not(file_string.startswith("VEG")):
            name_index = file_string.find(".")
            file_string = file_string[name_index+1:]
            end_index = file_string.find(".")
            specialitem_name = file_string[:end_index]
            specialitem_name = specialitem_name.strip("…")
            #join the specialitem_name list split into its words with single spaces
            specialitem_name = " ".join(specialitem_name.split())
            #push to mongo

            price_index = file_string.find("$")
            file_string = file_string[price_index+1:]
            end_index = file_string.find('\n')
            specialitem_price = file_string[:end_index]
            #push to mongo

            description_index = end_index + 1
            file_string = file_string[description_index:]
            end_index = file_string.find(".")
            specialitem_description = file_string[:end_index-1]
            specialitem_description = " ".join(specialitem_description.split())
            
            file_string = file_string[end_index:]
            
            

        



        
                

