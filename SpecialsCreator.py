from time import time
import pymongo
from pymongo import MongoClient
from docxtpl import DocxTemplate
from datetime import date

#Create template object
def select_template_and_collection():
    while True:
        global time_of_day
        time_of_day = input("Are you working on lunch or dinner specials?\nType L or D: ")
        if "L" == time_of_day.upper():
            collection = db.lunchSpecials
            template = DocxTemplate("LunchSpecialsTemplate.docx")
            time_of_day = "LUNCH"
            break
        elif "D" == time_of_day.upper():
            collection = db.dinnerSpecials
            template = DocxTemplate("DinnerSpecialsTemplate.docx")
            time_of_day = "DINNER"
            break
        else:
            print("Invalid input.")
    return template, collection
    

def get_num_of_specials():
    num_of_specials = input("Please enter the number of specials for today: ")

    while not(num_of_specials.isdigit()):
        num_of_specials = input("Please enter a number: ")

    num_of_specials = int(num_of_specials)
        
    while num_of_specials > 6:
        print("I can only handle up to 6 specials at the moment.")
        num_of_specials = int(input("Try again: "))

    return num_of_specials


#Get info for context to be used in template
def get_context():
    context = {}

    appetizer = input("What is the appetizer today? ")
    context["appetizer"] = appetizer

    app_price = input("How much is it? ")
    context["app_price"] = app_price

    soup1 = input("First soup? ")
    context["soup_one"] = soup1

    soup2 = input("Second soup? ")
    context["soup_two"] = soup2

    dessert1 = input("First dessert? ")
    context["dessert_one"] = dessert1

    dessert2 = input("Second dessert? ")
    context["dessert_two"] = dessert2

    i = 1
    while i <= num_of_specials:
        special = input(f"Enter special number {i}: ").upper()

        special = collection.find_one({"name": special})
        context[f"s{i}"] = special["name"]
        context[f"s{i}_price"] = special["price"]
        context[f"s{i}_description"] = special["description"]

        i += 1

    veg_otd = input("Vegetable of the day? ")
    context["veg"] = veg_otd

    return context

#MongoDB database
client = MongoClient()
db = client.blackolive

template, collection = select_template_and_collection()

num_of_specials = get_num_of_specials()

context = get_context()

template.render(context)
filestr = time_of_day + str(date.today().strftime("%b-%d-%Y"))
filestr = filestr + ".docx"
template.save(filestr)

#TODO#
#Create user friendly GUI

#Automate updates to the WordPress and website?
#Random generation of specials
