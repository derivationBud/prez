#!/usr/bin/env python
# Author: Derivation Bud
# Date: Jan14
# Converting sass to less sources

import glob
import re
sources = glob.glob("css/theme_orig/source/*.scss")+\
          glob.glob("css/theme_orig/template/*.scss")
for source in sources:
    destName = source.replace("_orig","")[:-5]+".less"
    dest = file(destName,"w")
    print "Creating:",dest.name
    varNames = []
    for line in file(source):
        # Convert Functions
        line = re.sub(r'@mixin +', r'.',line)

        # Convert Variables
        match = re.search(r'\$(\w*)',line)
        while match: 
            varName=match.groups()[0]
            if varName not in ["include"]:
                line = re.sub(r'\$'+varName, r'@'+varName,line,1)
            match = re.search(r'\$(\w*)',line)

        dest.write(line)
    dest.close()