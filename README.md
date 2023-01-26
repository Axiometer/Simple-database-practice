# Design for CSVTable class: 
1). Primary key values are maintained by iterative dictionaries to provide O(1) primary key access. 

e.g. primary key = {"playerID", "Height", "Weight"} 

data structure for saving primary key value {"playerID" : '007', "Height" : '160'", "Weight" : '100'} is 

{'007' : {'160' : '100': {index}}} 

the index is an automatic increasing number and is sured to be non-repeated. 

Pons: O(1) time complexity for seaching by primary key. I think this design is important. Primary key search operator is called in high frequency since we need not only in find_by _primary_key(), but also every time before insert a new entryto check if there is a duplicate primary key.  
Cons: Extra memory cost for maintaining this structure. 

2). All data are maintained in a dictionary where the key is the index. The index is also include in the value as a column. 

e.g. {index_000: {"index": index_1000, "playerID": '007', "Height" : '160', "Weight" : '100'}} 

When searching by template, it has to match every entry in the dictionary. The time complexity is O(n). 

# Correctness rules (Applied to both CSVTable and RDBTable implementation)

1). Inserting a duplicate primary key is forbidden. 
The principle is also work during data loading phrase. 

2). Primary key must be valid. 

3). All key specified in template and target fields must be valid. 

4). In find_by_template() function, if the input template is empty then seach all by default. 

```
forked from:
https://github.com/lt616/Simple-database-practice-Python-MySQL
```