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

_voter = """ 

Name : Ujwala “oe
Husband\'s Name « KeADarnka

House Num Abe .
Age : EMALE  

"""

_voter_details = [d.strip() for d in _voter.split('\n') if d.strip()]
print(_voter_details)

_list = [{'Name : Ramesh Gaonkar': "Father's Name : Manohar Gaonkar | House Number : - | Age: 31 Gender: MALE"},
         {'Name : Chetan Parab': "Mother's Name : Laxmi Parab | House Number: 598/14 | Age: 33 Gender: MALE"},
         {'Name: Pragati Parab': "Husband's Name: Harichandra Parab | House Number: 598/2 | Age: 31 Gender: FEMALE"},
         {'Name : Gurudas Parab': "Father's Name : Surya Parab | House Number : 890 | Age: 63 Gender: MALE"},
         {'Name: Rajashri Parab': "Husband's Name: Gurudas Parab | House Number: 890 . | Age: 51 Gender: FEMALE"},
         {'Name: Gaurav Parab': "Father's Name: Gurudas Parab | House Number : 890 | Age: 30 Gender: MALE"},
         {'Name: Sneha Parab': "Father's Name : Gurudas Parab | House Number : 890 | Age: 28 Gender: FEMALE"},
         {'Name: Sanni Mandrekar': "Father's Name : Shankar Mandrekar | House Number: 894 | Age: 31 Gender: MALE"},
         {'Name: Resha Palekar Gauns': "Father's Name : Damodar Palekar | Gauns ; | House Number: 894 | Age: 43 Gender: FEMALE"},
         {'Name: Shrimati Parab': "Husband's Name: Gopal Parab | House Number: 894 | Age: 79 Gender: FEMALE"},
         {'Name: Nilu Parab': "Father's Name : Gopal Parab | House Number: 894 | Age: 48 Gender: FEMALE"},
         {'Name: Vithal Parab': "Father's Name : Krhna Parab | House Number: 895 | Age: 87 Gender: MALE"},
         {'Name : Gamati Parab': "Husband's Name: Vithal Parab | House Number: 895 | Age: 77 Gender: FEMALE"},
         {'Name : Rajendra Parab': "Father's Name : Krhna Parab | House Number : 895 | Age: 60 Gender: MALE"},
         {'Name: Ramita Parab': "Husband's Name: Rajendra Parab | House Number: 695 | Age: 48 Gender: FEMALE"},
         {'Name: Rashmi Parab': "Father's Name : Rajendra Parab | House Number: 895 | Age: 23 Gender: FEMALE"},
         {'Name : Aditi Parab': "Father's Name : Rajendra Parab | House Number: 895 | Age: 21 Gender: FEMALE"},
         {'Name: Santosh Parab': "Father's Name : Dattulo Parab | House Number: 896 | Age: 57 Gender: MALE"},
         {'Name : Supriya Parab': "Husband's Name: Santosh Parab | House Number : 896 | Age: 52 Gender: FEMALE"},
         {'Name : Mohan Parab': "Father's Name : Dattulo Parab | House Number: 896 | Age: 52 Gender: MALE"},
         {'Name : Mayuri Parab': "Husband's Name: Mohan Parab | House Number: 896 | Age: 47 Gender: FEMALE"},
         {'Name : Sanam Parab': "Father's Name : Santosh Parab | House Number : 896 | Age: 27 Gender: MALE"},
         {'Name: Shumesh Parab': "Father's Name : Santosh Parab | House Number: 896 | Age: 24 Gender: MALE"},
         {'Name: Prakash Parab': "Father's Name: Ganesh Parab | House Number: 897 | Age: 52 Gender: MALE"},
         {'Name : Pratima Parab': "Husband's Name: Prakash Parab | House Number : 897 | Age: 46 Gender: FEMALE"},
         {'Name : Neeta Parab': "Father's Name : Prakash Parab | House Number: 897 | Age: 29 Gender: FEMALE"},
         {'Name: Ganesh Parab': "Father's Name : Prakash Parab | House Number: 897 | Age: 27 Gender: MALE"},
         {'Name: Shanti Parab': "Husband's Name: Shantaram Parab | House Number : 917(1) | Age: 59 Gender: FEMALE"},
         {'Name : Shantaram Parab': "Father's Name : Shankar Parab | House Number: 917/14 | Age: 69 Gender: MALE"},
         {'Name: Saiksha Parab': "Father's Name : Shantaram Parab | House Number: 917/14 | Age: 19 Gender: FEMALE"}]
