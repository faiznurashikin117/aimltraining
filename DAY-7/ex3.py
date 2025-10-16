import datetime
import inspect
dtclasses = inspect.getmembers(datetime,inspect.isclass)

print("All classes in datetime module")
for n,func in dtclasses:
    print(n,end="\t")

print("\n---Today---\n'")
print(datetime.date.today())

print("---Current Date Time---")
print(datetime.datetime.now())

print("---Current Time---")
print(datetime.datetime.now().time())
print(datetime.datetime.now().time())

print("---Current Time in AM/PM---")
cttime=datetime.datetime.now().time()
formatedtime=datetime.datetime.now().strftime("%I %M %S %p")
#"%I =hour %M =minute %S =string %p =AM/PM")
print("Current time",cttime)
print("Formated time",formatedtime)


# functions=inspect.getmembers(datetime.datetime,inspect.isbuiltin)

# print("All function in datetime module")
# for n,func in functions:
#     print(n,end="\t")



