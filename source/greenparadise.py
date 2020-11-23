import re,json
def isValid(number):
    match=re.match(r'[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$',number)
    if not match: return False
    else:
        digits=number.replace("-","")
        result=re.search(r'(\d)\1\1\1',digits)
        if result: return False
    return True
records=json.load(open("greenparadise.json"))
for record in records:
    valid=isValid(record["card"])
    if not valid:
        print("Invalid card:",record["card"])
    if valid != record["valid"]:
        print("Unmatched valid tag:",record["card"],valid,record["valid"])
