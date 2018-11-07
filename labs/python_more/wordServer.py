#!/usr/bin/env python 
# Author: David Roubinet
# python-more lab's solution

import SimpleXMLRPCServer
import urllib
import re

class wordGen:
    def __init__(self):    
    	url = "http://www.gutenberg.org/files/44955/44955-h/44955-h.htm"
    	txt = urllib.urlopen(url).read()
        words = re.findall(r'\b[a-zA-Z]{8}\b',txt,re.M)
        words = [word.lower() for word in words ]
        words = set(words)
    	#self.words = ["banana","yogurt","pizza"]
    	self.words = words
    	print "Ready with %d words in stock"%(len(words))
    def next(self): 
    	if not self.words: self.__init__()
    	return self.words.pop() 

if __name__ == "__main__":
    server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8080))
    server.register_instance(wordGen())
    server.serve_forever()