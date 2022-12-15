x = 10 #globalna

def poruka():
    print("Hello")
    print(x)
    a = 15 #lokalna promenljiva
    
def proba():
    global y
    y = 15
    print(x)

poruka()
proba()
print(y)