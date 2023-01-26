from CSVTable import CSVTable 

db_people = CSVTable("People", "students.csv", ["ID"])

#вывод всей таблицы
db_people.load() 
print(db_people)

# поиск по шаблону и вывод нужных
template = {}
template["class"] = "1a"
res = db_people.find_by_template(template, ["ID", "name"])
print(res)