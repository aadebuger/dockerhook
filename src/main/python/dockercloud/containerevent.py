'''
Created on Jan 2, 2015

@author: aadebuger
'''
from docker import Client
import json
def processEvent(cli,eventstr):
    event = json.loads(eventstr)
    print 'id=',event['id']
    print 'status=',event['status']
    info = cli.inspect_container(event['id'])
    print 'info=',info
    print 'name=',info['Name']
    print 'HostConfig=',info['HostConfig']
    print 'PortBindings=',info['HostConfig']['PortBindings']
    processPort(info['HostConfig']['PortBindings'])

def filterPort(portvalue):
    k =portvalue.find("/")
    if k ==-1:
        return portvalue
    else:
        return portvalue[0:k]
def processPortitem(item,portdict):
        print 'item=',item,portdict[item]
        print 'host port=',filterPort(item)
def processPort(portdict):
        print 'portdict.iterkeys',portdict.iterkeys()
        map(  lambda x: processPortitem (x,portdict) ,portdict.iterkeys());

def events():
    cli = Client(base_url='tcp://172.17.42.1:4243')
    eventiter = cli.events()
    
    while 1:
            event = eventiter.next()
            print 'event',event
            processEvent(cli,event)
        
if __name__ == '__main__':
    events();