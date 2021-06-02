from time import time
import pymongo
from pymongo import MongoClient
from docxtpl import DocxTemplate

client = MongoClient()
db = client.blackolive
doc = DocxTemplate("SpecialsTemplate.docx")

while True:
    timeOfDay = input("Are you working on lunch or dinner specials?\n Type L or D: ")
    if "L" == timeOfDay.upper():
        collection = db.lunchSpecials
        break
    elif "D" == timeOfDay.upper():
        collection = db.dinnerSpecials
        break
    else:
        print("Invalid input.")


numOfSpecials = input("Please enter the number of specials for today: ")
numOfSpecials = int(numOfSpecials)

i = 1
while i <= numOfSpecials:
    special = input(f"Enter special number {i}: ").upper()

    special = collection.find_one({"name": special})
    print(special)

    i += 1

#TODO#
#Find the corresponding specials in the database - MongoDB

#Use MS Word template to populate
#Create user friendly GUI

#Automate updates to the WordPress and website?
#Random generation of specials
