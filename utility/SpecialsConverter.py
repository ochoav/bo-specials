#Script to convert all docx files to txt files for easier parsing and extraction
#of info for database
import pypandoc
import os

#String to be used for pathlike filename for the directory
#Can't use ~ because bash is what expands ~, python doesn't know that ~ stands for
# /Users/victorochoa
directory_in_str = "/Users/victorochoa/Desktop/bo-specials/specials/"
directory = os.fsencode(directory_in_str)

#Using pypandoc module for easy conversion
i = 1
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    #If this isn't a dinner special, name the corresponding txt file with LUNCH
    if filename.find("DINNER") == -1:
        output = pypandoc.convert_file(f'specials/{filename}', 'plain', outputfile=f"../plainTxtSpecials/LUNCH{i}.txt")
        assert output == ""
    else:
        output = pypandoc.convert_file(f'specials/{filename}', 'plain', outputfile=f"../plainTxtSpecials/DINNER{i}.txt")
        assert output == ""
    i+=1


