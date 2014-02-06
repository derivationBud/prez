![logo](./img/python-logo-generic.svg) 
# Basics

By *David Roubinet* , Jan14

>>

What is Python ?

> - v2.0 released in 2000 by **Guido Van Rossum**
> - Quoting the Monty Python is a healthy habit  

Why ?

> Easy on the *developer*, not on the machine

Used ?

> Google, Youtube, Academics, Labs

For us ?

> - Analyze logs, generate plots, reports  
> - Glue or bridge existing apps, db, servers

>>
## Setup

Version
> **v2.7** recommended  
> *v3.3* nicer syntax but less libraries 

Install
> Linux & Mac : already there  
> Windows : get it @ [python-2.7.6.msi](http://www.python.org/ftp/python/2.7.6/python-2.7.6.msi)

Configure your text-editor / IDE

> **1 TAB &rarr; 4 spaces**

>>
##Hello World

Create a file **``helloWorld.py``**

```python
#!/usr/bin/env python
print "Hello World!"
```
Lauch on any os : 
> ```/<path>/<to>/python helloWorld.py```

Launch on Mac/Linux : 
> ```chmod +x ./helloWorld.py```  
> ```./helloWorld.py```
>>
## Interactive Shell

```</path/to/>python``` with *no arg* is a **console** ...

```
Python 2.7.4 (default, Sep 26 2013, 03:20:56) 
[GCC 4.7.3] on linux2
Type "help", "copyright", "credits" or "license" for more info.
>>> print 1+2
3
>>> exit()```

Handy calculator accepting _**big**_ numbers.

```
>>> 123**102
1480203295629928329479981685264795353307343870806030995772572
2520911504293200426656620631029510757221888460901007696324336
8523439832863460122438964502975350810638854406478502135611850
1231433129L```

>>
## Strings

Quoting  
> Many delimiters allowed:  `' '' ''' " "" """`  
> A delimiter encloses another: `'He said "Hello"'`  
> Triple quotes span over new lines:  
> ```python
message = """ This is a  very very very very  very very 
very very very very very very very very very long string.
                         Victor Hugo         """
```

Formatting : **string % (values)**

```
>>>"There are %d %s %s(s)"%(2,"red","banana")
'There are 2 red banana(s)'
```
```
>>>"%(boy)s runs fast. %(boy)s is %(age)d"%{"boy":"Al","age":12}
'Al runs fast. Al is 12'
```
>>
##String Cont'd
###Operations 

 |` ` | *Expression* | *Result*
 |--- | --- | --- 
 |concatenate| `'ABC'+'DEF'*2`| `'ABCDEFDEF'` 
 |1st, 2sd| `'ABCDEF'[0],'ABCDEF'[1]`| `('A','B')` 
 |last, before| `'ABCDEF'[-1],'ABCDEF'[-2]`| `('F','E')` 
 |2sd to 3rd| `'ABCDEF'[1:3]`|`'BC'` 
 |2sd to 2sd| `'ABCDEF'[1:2]`|`'B'` 
 |omit *first*| `'ABCDEF'[:2]`| `'AB'`
 |omit *last*| `'ABCDEF'[-2:]`| `'DE'` 
 |always full| `'ABCDEF'[:i]+'ABCDEF'[i:]`| `'ABCDEF'`   

    
*Trick:* Think of slicing[i:j**]** as slicing[i:j**[**
>>

##Lists

Square brackets 

```python
mylist = ['AB','cd',23,0x34,"EF"]
```

Trailing coma allowed 

```python
mylist2 = ['AB',
           0x34,
         # "EF", # Commenting out does'nt break syntax
          ]
```
Operations

| ` `          |Expression                | Result                 |
|--------------|--------------------------|------------------------|
| concatenate  |`['AB','CD']+['EF']*2`    |`['AB','CD','EF','EF']` |
| indexing     |`['AB','CD','EF'][0]`     |`'AB'`                  |
| slicing      |`['AB','CD','EF'][1:3]`   |`['CD','EF']`           |
| existence    |`'CD' in ['AB','CD','EF']`|`True`                  |

Quiz ? `[1,2,3,4,5][2:2]`
vv
##Answer:

* `[1,2,3,4,5][2:2]` = `[]` = empty list  
* Same goes for `mylist[i:j]` whenever  `i` &ge; `j`
>>
##Dictionaries

Curly Braces
```python
mydict = { 'price'  : 12, 
           'type'   : 'Table', 
           'options': ["red","blue"],
           'dim'    : {"W":90,"L":180,"H":72}, 
            }
```
Operations
 ` ` | Expression | Result |
 --- | --- | --- 
 keyword indexing |``{'A':12,'B':'C'}['A']``|``12``
 existence |``'C' in {'A':12,'B':'C'}``| ``False``
 modify entry |``d={'A':12,'B':'C'};d['A']=13``|``{'A':13,'B':'C'}``
 add entry |``d={'A':12,'B':'C'};d['Z']=0`` | ``{'A':12,'B':'C','Z':0}``
 remove entry |``d={'A':12,'B':'C'};del(d['B'])`` | ``{'A':12}``

Quiz ? ``mydict['options'][1][-2]``  
Quiz ? ``mydict['dim'][H]-mydict['price']``
vv
##Answer
Quiz ? ``mydict['options'][1][-2]``  
```python
mydict['options']        = ["red","blue"]
mydict['options'][1]     =        "blue"
mydict['options'][1][-2] =          "u"
```
Quiz ? ``mydict['dim'][H]-mydict['price']``

```python
mydict['dim']           = {"W":90,"L":180,"H":72} 
mydict['dim']["H"]      = 72
mydict['price']         = 12
                        -----
                        = 60
```
>>
##Introspection

Everything is an object 
```python
>>> dir('ABCDEF')
['__add__', '__class__', '__contains__', '__delattr__',
...
'lower', 'lstrip', 'partition', 'replace', 'rfind',
'strip', 'swapcase', 'title', 'translate', 'upper']
``` 
Methods
```python
>>> 'ABCDEF'.lower
<built-in method lower of str object at 0xb742b8e0>
>>> 'ABCDEF'.lower()
"abcdef"
```
Doc
```python
>>> help("ABCDEF".split)
split(...)
    S.split([sep [,maxsplit]]) -> list of strings
            
    Return a list of the words in the string S, using sep as ...
```
>>

##Usual methods

| ` `           | Expression              | Result |
| ------------- | ----------------------- | -------| 
| text trim     |``'A BC DEF\n'.strip()`` |``'A BC DEF'``
| text search   |``"ABCDEFABCDEF".find("EF")`` |``'4'``
| text replace  |``'ABCDEFABCDEF'.replace('A','aa')`` |``'aaBCDEFaaBCDEF'``
| text -> list  |``'A BC DEF'.split()`` |``['A','BC','DEF']``
| list -> text  |``'-'.join(['A','BC','DEF'])`` |``'A-BC-DEF'``
| list sort in place    |``l=[6,3,1,2]; l.sort()`` | ``[1,2,3,6]``
| list reverse in place |``l=[6,3,1,2]; l.reverse()`` | ``[2,1,3,6]``
| dict keys             |``{'A':12,'B':'4'}.keys()``|``['A','B']``
| dict values           |``{'A':12,'B':'4'}.values()``|``['12','4']``

>>

#Indentation
#Conditions
#Iterate
#File parsing
#Functions
#Modules
#Embedding doc
#Embedding test
#Standard libs
#os,sys,re
