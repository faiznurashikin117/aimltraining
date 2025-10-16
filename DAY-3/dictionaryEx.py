print("Dictionary Example")

our_dictionary=[
    {'id':'1','name':'ravi','age':'35'},
    {'id':'2','name':'amit','age':'30'},
    {'id':'3','name':'vijay','age':'35'},
    {'id':'4','name':'nitin','age':'12'}
    ]

#key=id,name,age
#value=the data(1,ravi,amit,35,etc)

for k in our_dictionary:
    print(k['id']+'->'+k['name']+'->'+k['age'])