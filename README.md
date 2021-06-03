# bo-specials
## What is this?

At the restaurant I work at, like many other restaurants we have rotating specials. One of my responsibilities is retrieving the daily specials from one of the cooks
and then creating a formatted page of specials to be printed and displayed on our menus. However, this job is very tedious and repetitive:
1. Search for item by name through the macOS finder
2. Check the description, check the price
3. Copy and paste into current specials page
4. Correct formatting
5. Repeat until all specials have been found

It was asking to be done by a computer already!

## What are all these files?
### plainTxtSpecials and Specials
The specials folder contains about 100 or so pages worth of specials ranging back to last year. The plainTxtSpecials folder contains all of these specials pages
converted to .txt files to facilitate parsing and inserting into the database.

### SpecialsConverter.py
This script converted all the .docx files into .txt files using pypandoc.

### DatabaseCreator.py
With the help of MongoDB and pymongo, I parsed through the .txt files to extract the name, description, and price of each special item and insert it into the 
database I had set up locally.

### SpecialsCreator.py
With the help of the docxtpl library, this is the main driver which accepts input for filling out the templates for the specials pages. The important part here is that
the user just types the name of the special, and the description and price are filled in using information stored in the database. This is much more efficient than
manually searching through files on the computer.

###Templates.docx
The two templates are those used by the SpecialsCreator.py. One is for lunch specials and the other for dinner specials, the only real differences are that one says 
"Lunch Specials" at the top and the other says "Dinner Specials", along with which vegetables we have available.

##Now what?
Well, as it stands right now the program runs through the terminal, and only works if the inserted name matches the stored name exactly.

I am looking to go beyond this and implement a more user friendly program:
- GUI with more options such as updating stored specials
- Suggestions for specials whose names are close to that entered
- Click and choose by type of item (seafood, sautee, pasta)

Other features I'd like/have to implement:
- Pushing updates to our WordPress website with a single click
- Random generation of a specials page
- Inserting new specials
