import pymongo
import os
from pymongo import MongoClient


def remove_extras(filename):
    with open(f"plainTxtSpecials/{filename}") as f:
        file_string = f.read()
        file_string = file_string[file_string.find("A.", file_string.find("SOUP")):]
        file_string = file_string[:file_string.rfind("VEG", 0, file_string.rfind("MASH"))]
        return file_string

def cleanup_formatting(str):
    newStr = " ".join(str.split())
    return newStr

#client = MongoClient()
#print(client)

#db = client.blackolive
#specials = db.specials

directory_in_str = "/Users/victorochoa/Desktop/bo-specials/plainTxtSpecials/"
directory = os.fsencode(directory_in_str)

#listdir() returns a list version of the files in the directory
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    
    file_string = remove_extras(filename)

    if file_string.find("BREAKFAST") != -1:
            continue

    #Strings are falsy, so when empty and used as a boolean they evaluate to false
    #I parse the files backwards, simply because that's the way my brain worked up a solution in the background!
    while file_string:
        #Using the 9 at the end of each price as a marker
        start = file_string.rfind("9")
        description = file_string[start + 1:]
        description = cleanup_formatting(description)
        print(description)
        #push mongo
        
        #Using the $ symbol as a marker between the price and the name
        file_string = file_string[:start + 1]
        start = file_string.rfind("$")
        price = file_string[start + 1:]
        price = cleanup_formatting(price)
        print(price)
        #push

        #All that's left until the next description is the name with ... or . 
        # and the letter before it so strip and reduce!
        file_string = file_string[:start].strip("….")
        start = file_string.rfind(".")
        item_name = file_string[start + 1:]
        item_name = cleanup_formatting(item_name)
        print(item_name)
        #push
        
        specialItem = {
            "name" : f"{item_name}",
            "price" : f"{price}",
            "description": f"{description}",
            
        }

        file_string = file_string[:start - 1]
    


            


            

        



        
                

