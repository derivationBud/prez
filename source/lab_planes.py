import json,csv,argparse

def crunch(people):
    report={ "stats":{}, "children":[] }
    for victim in people:
        if victim["Country"] not in report["stats"]:
            report["stats"][victim["Country"]]=0
        report["stats"][victim["Country"]]+=1
        if int(victim["Age"])<18:
            report["children"].append(victim["Name"])
    return report

def main(args):
    # Collect Data
    people=[]
    for filename in args["listing"]:
        if args["v"]:
            print(f"Processing {filename}...")
        if ".json" in filename:
            people += json.load(open(filename))
        elif ".csv" in filename:
            for row in csv.reader(open(filename)):
                people.append({"Country":row[0],"Age":row[1],"Name":row[2]})
    # Data Analysis
    report=crunch(people)
    # Display report
    print("Victims per country:")
    for country,count in report["stats"].items():
        print(f"{country:40} {count:3} {'*'*count}")
    print("Victims under 18:")
    for child in report["children"]:
        print(child)

def test():
    report = crunch( [
        {"Country" : "Nintendo", "Age" : 35, "Name" : "Mario"},
        {"Country" : "Nintendo", "Age" : 30, "Name" : "Luigi"},
        {"Country" : "Nintendo", "Age" : 18, "Name" : "Peach"},
        {"Country" : "Nintendo", "Age" : 17, "Name" : "Zelda"},
        {"Country" : "Hogwarts", "Age" :  7, "Name" : "Harry"},
        {"Country" : "Hogwarts", "Age" :  7, "Name" : "Ron"  },
        ])
    assert len(report["children"])==3
    assert report["stats"]["Nintendo"]==4
    assert report["stats"]["Hogwarts"]==2
    assert "Ron"       in report["children"]
    assert "Harry"     in report["children"]
    assert "Zelda"     in report["children"]
    assert "Mario" not in report["children"]
    print("PASS")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description=("Missing people analysis"))
    parser.add_argument('listing',nargs='*',
        help="Missing people input File (*.json|csv).")
    parser.add_argument('-v',action='store_true', help="Verbose")
    parser.add_argument('-t',action='store_true', help="Run Selftest")
    args = vars(parser.parse_args())

    if args["t"]: test()
    else:         main(args)
