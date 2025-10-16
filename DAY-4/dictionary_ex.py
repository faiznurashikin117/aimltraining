# employee={"id":1,
#           "name":"Sam",
#           "salary":55000.50
#           }

# print("Employees Details as follows:")
# for key,value in employee.items():
#     print(key,"->",value)
# #Adding key in dictionary
# employee["city0"]="Muscat"
# print("\nDictionary after adding City\n")

# for key,value in employee.items():
#     print(key,"->",value)

#Delete key value pairs
# del employee["salary"]
# print("\nEmployee Details after deleting salary\n")
# for key,value in employee.items():
#     print(key,"->",value)


employee={"id":1,
          "name":"Sam",
          "salary":55000.50
          }
print("All Keys from employee")
for k in employee.keys():
    print(k,end="\t")

print("\nAll Values from employee")
for v in employee.values():
    print(v,end="\t")

print("\nKey:Value")
for k,v in employee.items():
    print(k,":",v)

print("\nDictionary as follows")
print(employee)