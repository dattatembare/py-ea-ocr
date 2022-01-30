# import csv
#
# field_names = ['No', 'Company', 'Car Model']
#
# cars = [
#     {'No': 1, 'Company': 'Ferrari', 'Car Model': '488 GTB'},
#     {'No': 2, 'Company': 'Porsche', 'Car Model': '918 Spyder'},
#     {'No': 3, 'Company': 'Bugatti', 'Car Model': 'La Voiture Noire'},
#     {'No': 4, 'Company': 'Rolls Royce', 'Car Model': 'Phantom'},
#     {'No': 5, 'Company': 'BMW', 'Car Model': 'BMW X7'},
# ]
#
# csv_file = open('voters.csv', 'w')
# writer = csv.DictWriter(csv_file, fieldnames=['header'])
# writer.writerow({'header': 'header text'})
# writer = csv.DictWriter(csv_file, fieldnames=field_names)
# writer.writeheader()
# writer.writerows(cars)
# writer = csv.DictWriter(csv_file, fieldnames=['footer'])
# writer.writerow({'footer': 'footer text'})
# csv_file.close()

# s = '[8] HNL1383009 |Name : Lipika Nag |Husband\'s |Name - Shambhu Nag |House Number: 807 |Age: 44 |Gender: FEMALE '
# print(s.replace("|Husband's |", "|Husband's "))
import json

_voter = """ 

Name : Ujwala “oe
Husband\'s Name « KeADarnka

House Num Abe .
Age : EMALE  

"""

_voter_details = [d.strip() for d in _voter.split('\n') if d.strip()]
print(_voter_details)
#
# file_pages = {1: "page 1 \\n next line address: 10/4", 2: "page 2 \\n next line"}
# print(file_pages)
# print(json.dumps(file_pages))
