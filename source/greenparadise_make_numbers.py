import random
import json
invalids = [
    "1234-5689-3465-7657", # Bad start
    "62345-689-3465-7657", # Bad grouping
    "56785689346517657",   # Bad length
    "4234-3428-6666-7657", # Bad repetition
    "4234-3455-5562-7657", # Bad repetition across hyphen
    ]
def make_number():
    number=""
    if True:
        number+=random.choice("456")
        number+="".join(random.sample("0123456789",3))
    for j in range(3):
        number+=random.choice(["","-"])
        number+="".join(random.sample("0123456789",4))
    return(number)
total=100
faulty=random.sample(range(total),len(invalids))
numbers = []
for i in range(total):
    if i in faulty: numbers.append( {"card":invalids.pop(),"valid":False})
    else:           numbers.append( {"card":make_number() ,"valid":True })
fo=open("greenparadise.json","w")
json.dump(numbers,fo,indent=" ")
fo.close()
