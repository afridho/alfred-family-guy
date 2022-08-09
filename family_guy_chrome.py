#!/usr/bin/python
# encoding: utf-8
#
# Copyright (c) 2022 Ridho Zega
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
from __future__ import print_function, absolute_import
import json
import sys
import random
import string
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf-8')

filename = 'data.json'
listObj = []

def log(s, *args):
    """Simple STDERR logger."""
    if args:
        s = s % args
    print(s, file=sys.stderr)
    
# def empty_data():
#     empty = [{'title': 'empty',
#             'subtitle': 'empty'}]
#     return empty

def time_now():
    now = datetime.now()

    # dd/mm/YY H:M:S
    timeNow = now.strftime("%-d %B, %Y %H:%M:%S")
    return timeNow

def movies(search=None):
    data_out = data_object()
    projects = sorted(data_out, key=lambda x: x['finished'], reverse=False)
    result = []
    for project in projects:
        if search is not None and project['name'].lower().find(search.lower()) == -1:
            continue
        result.append({
            'title': '{} ☑️'.format(project['name'])if project['finished'] == True else '{}'.format(project['name']),
            'subtitle': '{}{}'.format(('Last watched: ' + project['last_watched'][:-3] + '   |   ' if project['last_watched'] and project['finished'] == False else ''),('Watch Now🍿' if project['finished'] == False else '{}'.format('Mod keys for option'))),
            'arg': '{}_{}'.format(project['id'],project['url']),
            'valid' : False if project['finished'] == True else True,
            'icon': {
                'path': 'icon.png'
            },
            'mods': {
                'alt': {
                    'valid': True,
                    'arg': project['id'],
                    'subtitle': '🚫Delete this season'
                },
                'ctrl': {
                    'valid': True,
                    # add argument project finished to Dialog Conditional
                    'arg': '{}:{}'.format(project['id'],project['finished']),
                    'subtitle' : '{}'.format('🍿Mark Unwatched' if project['finished'] == True else '☑️Mark Watched'),
                },
                'cmd': {
                    'valid': True,
                    'arg': 'Season ',
                    'subtitle': '➕Add season',
                },
            }
        })
        
    return result
def data_object():
    f = open(filename)
    posts = json.load(f)
    return posts

"""Run Script Filter."""
def main():
    SEARCH = sys.argv[1] if len(sys.argv) >= 2 else None
    posts  = movies(search=SEARCH)
    data = json.dumps({ "items": posts }, indent=4)
    print(data)
    
"""Start Add Data Function"""
def randomId():
    random_id = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(15)])
    return random_id
def addData(seasonName=None, Url=None):
    with open(filename) as fp:
        listObj = json.load(fp)
        listObj.append({
            "id": randomId(),
            "name": seasonName,
            "url": Url,
            "last_watched": "",
            "finished" : False,
        })
    with open(filename, 'w') as json_file:
        json.dump(listObj, json_file, 
                            indent=4,  
                            separators=(',',': '))
    print('Data saved.')

def getData(queryName=None, queryNumber=None, queryUrl=None):
    result = []
    result = [{ 'title': 'Save Data',
        'subtitle': 'Format data is right✅',
        'arg': '{} {}\n{}'.format(queryName, queryNumber, queryUrl),
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
                    'title': 'Season Name (space) Url Hotstar',
                    'subtitle': 'ex: Season 20 https://www.hotstar.com/id/tv/family-guy/1260024995/seasons/season-20/ss-8438',
                    'valid' : False,
                    'icon': {
                        'path': 'icon.png'
                    }
    }]
    data = json.dumps({ "items": data_default }, indent=2)
    print(data)
    
def formatError():
    data_default = [{
                    'title': 'Format Data is wrong🚫',
                    'valid' : False,
                    'icon': {
                        'path': 'icon.png'
                    }
    }]
    data = json.dumps({ "items": data_default }, indent=2)
    print(data)

def mainAddData():
    """Run Script Filter."""
    if len(sys.argv) >= 2:
        Query = sys.argv[1] 
        querySplit = Query.split()
        if(len(querySplit) > 1 and len(querySplit) != 2 and len(querySplit) < 4):
            posts  = getData(querySplit[0], querySplit[1], querySplit[2])
            data = json.dumps({ "items": posts }, indent=2)
            print(data)
        elif (len(querySplit) == 2):
            return default()
        elif (len(querySplit) >=3):
            return formatError()
        else:
            return default()
    else:
        return default()   
"""End Add Data Function"""

"""Start Delete Data Function"""
def deleteData(dataId=None):
    with open(filename, 'r') as f:
        my_list = json.load(f)
        for idx, obj in enumerate(my_list):
            if obj['id'] == dataId:
                my_list.pop(idx)
    with open(filename, 'w') as f:
        f.write(json.dumps(my_list, indent=4))
"""End Delete Data Function"""

"""Begin Mark Watched Data"""
def markWatchedData(dataId=None):
    with open(filename, 'r') as f:
        my_list = json.load(f)
        for idx, obj in enumerate(my_list):
            if obj['id'] == dataId:
                obj['finished'] = False if obj['finished'] == True else obj['finished'] == False
    with open(filename, 'w') as f:
        f.write(json.dumps(my_list, indent=4))
"""End Mark Watched Data"""

"""Begin write last watched time"""
# Last time data click
def writeLastWatchedTime(dataId=None):
    with open(filename, 'r') as f:
        my_list = json.load(f)
        for idx, obj in enumerate(my_list):
            if obj['id'] == dataId:
                obj['last_watched'] = time_now()
    with open(filename, 'w') as f:
        f.write(json.dumps(my_list, indent=4))
"""End write last watched time"""

if __name__ == '__main__':
    # default load filter
    main() 
    
