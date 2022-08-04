#!/usr/bin/python
# encoding: utf-8
#
# Copyright (c) 2018 Dean Jackson <deanishe@deanishe.net>
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2018-12-23
#


from __future__ import print_function, absolute_import

import json
import sys
from collections import OrderedDict
reload(sys)
sys.setdefaultencoding('utf-8')

filename = 'file2.json'
listObj = []


def log(s, *args):
    """Simple STDERR logger."""
    if args:
        s = s % args
    print(s, file=sys.stderr)
    
def addData(Name=None, Url=None):
    with open(filename) as fp:
        listObj = json.load(fp)
        
        # Verify existing list
        print(listObj)

        print(type(listObj))
    
        listObj.append({
            "id": "Person_3",
            "name": "hehe",
            "url": "33@gmail.com",
            "finished" : False,
        })
    
    
    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, 
                            indent=4,  
                            separators=(',',': '))
    
    print('Successfully appended to the JSON file')
    
    # querySplit = query.split

def getData(queryName=None, queryUrl=None):
   
    
    result = []
    result = [{ 'title': queryName,
        'subtitle': queryUrl,
        'arg': queryUrl,
        'valid' : True,
        'icon': {
            'path': 'icon.png'
        }}]

    return result
 
def data_object():
    f = open(filename)
    posts = json.load(f)
    return posts

def default():
    data_default = [{
                    'title': 'Season Name[space]Url Hotstar',
                    'subtitle': 'ex: Season 20 https://www.hotstar.com/id/tv/family-guy/1260024995/seasons/season-20/ss-8438',
                    'arg': 'hehe',
                    'valid' : True,
                    'icon': {
                        'path': 'icon.png'
                    }
    }]
    data = json.dumps({ "items": data_default }, indent=2)
    print(data)

def mainData():
    """Run Script Filter."""
    if len(sys.argv) >= 2:
        Query = sys.argv[1] 
        querySplit = Query.split()
        if(len(querySplit) > 1 and len(querySplit) != 2):
            posts  = getData(querySplit[0], querySplit[2])
            data = json.dumps({ "items": posts }, indent=2)
            print(data)
        elif (len(querySplit) == 2):
            return default()
        else:
            return default()
    else:
        return default()
        


if __name__ == '__main__':
    main()

