
n Dictionaries
'''
Dictionary

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.'''


employee={
            'name':"sangeetha",
                "age":12,
                    "phone":9087654321
                       
                    }
print(employee)

# how to access the particular key

print(employee['name'])

# changeable duplicate



employee={
            'name':"sangeetha",
                "age":12,
                    "phone":9087654321,
                       "age":90
                       }
print(employee["age"])

#length of dictionar

print(len(employee))
#====================================

# dictionary in other data type
employee1 = {
          "it": "aws",
            "course": "aws",
              "year": 2024,
                "colors": ["red", "white", "blue"]
                }

print(employee1)


# addming items
thisdict = {
          "brand": "Ford",
            "model": "Mustang",
              "year": 1964
              }
thisdict["color"] = "red"
print(thisdict)
