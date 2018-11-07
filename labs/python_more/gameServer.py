#!/usr/bin/env python 
# Author: David Roubinet
# python-more lab's solution

import SimpleXMLRPCServer
import xmlrpclib

class hangMan:
    def __init__(self):    
        self.wordServer  = xmlrpclib.Server('http://localhost:8080')
        self.secret = self.wordServer.next()
    def new(self): 
        self.secret = self.wordServer.next()
        return True
    def guess(self,propal): 
        if   len(propal)==1: 
            return [idx for idx,char in enumerate(self.secret) if char==propal]
        elif len(propal)==8: 
            return propal==self.secret
        else               : 
            return -1

if __name__ == "__main__":
    server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8081))
    server.register_instance(hangMan())
    server.serve_forever()