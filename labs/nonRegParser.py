#!/usr/bin/env python 
# Author: David Roubinet
# python-basics lab's solution

inputData = """\
Suite,     Test,   Status
v2,        mini,   Pass
v2,        mini2,  Pass
Legacy,    basic,  Pass
v2,        mini3,  Pass
Local,     test2,  Pass
v2,        full,   Pass
Local,     test1,  Pass
Legacy,    extra,  Fail
Local,     test3,  Fail
Blind,     ztest,  Fail
Local,     test4,  Pass""".split("\n")

db    = {}
fails = []
for line in inputData[1:]: # <- Skipping header row
    suite,test,status = line.replace(" ","").split(",")
    if suite not in db: db[suite]={"totalCount":0,"passCount":0}
    db[suite]["totalCount"] += 1
    if status=="Pass": db[suite]["passCount"] += 1
    else             : fails.append("%s -> %s"%(suite,test))

for fail in fails: print "FAIL:",fail

for suite in db:
    print "STAT:",suite,100*db[suite]["passCount"]/db[suite]["totalCount"]
