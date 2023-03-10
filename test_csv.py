# COMP4111 Assignment 01 - CSVTable test 
# Author: Qianrui Zhao 		ID: qz2338 
# Any question please contact qz2338@columbia.edu 

# Functions to be tested in CSVTable 
# def __init__(self, table_name, table_file, key_columns) 
# def __str__(self) 
# def load(self) 
# def save(self) 
# def find_by_primary_key(self, values, fields) 
# def find_by_template(self, t, fields) 
# def insert(self, r) 
# def delete(self, t) 

from CSVTable import CSVTable 

######################################################
# test 01: init() with invalid parameters
# Expect: Error message
###################################################### 
print("test 01: init() with invalid file name\nExpect: Error message") 

try: 
	db_people = CSVTable("People", "test.file", ["playerID"]) 
except: 
	print("test 01 completed.")
	print("===================") 

######################################################
# test 02: init() with invalid primary keys
# Expect: Error message
###################################################### 
print("test02: init() with invalid primary keys\nExpect: Error message") 

try: 
	db_people = CSVTable("People", "people_test_CSV.csv", ["test"]) 
except: 
	print("test 02 completed.") 
	print("===================") 

######################################################
# test 03: init() with valid parameters 
# Expect: Successfully created the instance
###################################################### 
print("test 03: init() with valid parameters\nExpect: Successfully created the instance") 

db_people = CSVTable("People", "people_test_CSV.csv", ["playerID"]) 

print("test 03 completed.")
print("===================") 

######################################################
# test 04: load()  
# Expect: Successfully loaded the data 
###################################################### 
print("test 04: load()\nExpect: Successfully loaded the data") 

db_people.load() 

print("test 04 completed.")
print("===================") 

######################################################
# test 05: str() 
# Expected: Print whole table
###################################################### 
print("test 05: str()\nExpected: Print whole table") 

print(str(db_people))  

print("test 05 completed.")
print("===================") 

######################################################
# test 07: find_by_primary_key() with invalid fields 
# Expect: Error Message   
###################################################### 
print("test 07: find_by_primary_key() with invalid fields\nExpect: Error Message") 

primary_key = ["aardsda01"]
try: 
	db_people.find_by_primary_key(primary_key, ["name"]) 
except: 
	print("test 07 completed.")
	print("===================") 

######################################################
# test 08: find_by_primary_key() with valid input 
# Expect: Information of player whose ID is "aardsda01" 
###################################################### 
print("test 08: find_by_primary_key() with valid input\nExpect: Information of player whose ID is Expect: Information of player whose ID is 'aardsda01'")  

primary_key = ["aardsda01"]
db_people.find_by_primary_key(primary_key, ["nameFirst", "nameLast"])  

print("test 08 completed.")
print("===================") 

######################################################
# test 09: find_by_template() with invalid template 
# Expect: Error message 
###################################################### 
print("test 09: find_by_template() with invalid template\nExpect: Error message") 

template = {} 
template["test"] = 2 
try: 
	db_people.find_by_template(template, ["nameLast", "nameFirst"]) 
except: 
	print("test 09 completed.") 
	print("===================") 

######################################################
# test 10: find_by_template() with invalid fields 
# Expect: Error Message 
###################################################### 
print("test 10: find_by_template() with invalid fields\nExpect: Error Message") 

template = {} 
template["birthMonth"] = 8
try: 
	db_people.find_by_template(template, ["name"]) 
except: 
	print("test 10 completed.")
	print("===================") 

######################################################
# test 11: find_by_template() with valid input 
# Expect: Name of all players whose birth month == 8 
###################################################### 
print("test 11: find_by_template() with valid input\nExpect: Number of players whose birth month == 8 is 1862") 

template = {} 
template["birthMonth"] = 8 
res = db_people.find_by_template(template, ["nameLast", "nameFirst"])

print("Number of results: " + str(len(res))) 
print("test 11 completed.")
print("===================") 

######################################################
# test 12: insert() with invalid column 
# Expect: Error message 
###################################################### 
print("test 12: insert() with invalid column\nExpect: Error message") 

try: 
	db_people.insert({'playerID': 'testID001', 'birth': '8', 'nameFirst': 'TTTTT', 'nameLast': 'Aaron', 'birthDay': '5'})
except: 

	print("test 12 completed.")
	print("===================") 

######################################################
# test 13: insert() with valid data 
# Expect: New row inserted
###################################################### 
print("test 13: insert() with duplicate primary key\nExpect: Number of players whose birth month == 8 is now 1863") 

db_people.insert({'playerID': 'testID001', 'birthMonth': '8', 'nameFirst': 'TTTTT', 'nameLast': 'Aaron', 'birthDay': '5'})
res = db_people.find_by_template(template, ["nameLast", "nameFirst"]) 
print("Number of results: " + str(len(res))) 
print("test 13 completed.")
print("===================") 

######################################################
# test 14: insert() with duplicate primary key 
# Expect: Error message 
###################################################### 
print("test 14: insert() with duplicate primary key\nExpect: Error message") 

try: 
	db_people.insert({'playerID': 'testID001', 'birthMonth': '8', 'nameFirst': 'TTTTT', 'nameLast': 'Aaron', 'birthDay': '5'})
except: 
	print("test 14 completed.")
	print("===================") 

######################################################
# test 15: delete() with invalid template 
# Expect: Error message 
###################################################### 
print("test 15: delete() with invalid template\nExpect: Error message ") 

template = {} 
template["test"] = 1 
try: 
	db_people.delete(template) 
except:   
	print("test 15 completed.")
	print("===================") 

######################################################
# test 16: delete() with valid template 
# Expect: All players whose birth month == 8 are deleted 
###################################################### 
print("test 16: delete() with valid template\nExpect: Number of players whose birth month == 8 is now 0") 

template = {}
template["birthMonth"] = 8 
db_people.delete(template)  
res = db_people.find_by_template(template, ["nameLast", "nameFirst"])
print("Number of results: " + str(len(res))) 
print("test 16 completed.")
print("===================")



######################################################
# test 17: save() 
# Expect: In csv file, no players whose birth month == 8 
###################################################### 
print("test 17: save()\nExpect: After reload, Number of players whose birth month == 8 is now 0") 

db_people.save() 

db_people.load() 
res = db_people.find_by_template(template, ["nameLast", "nameFirst"])
print("Number of results: " + str(len(res))) 

print("test 17 completed.")
print("===================")


