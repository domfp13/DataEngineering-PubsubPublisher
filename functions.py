#!/usr/bin/env python3
# Created by Enrique Plata

from os import environ

def decoratorGetRegistry(funtion):
    def wrapper():
        listOfRegistries = {'TOPIC': 'Appusma206_apps', 'PROJECT_ID':'microstrategyit'}
        return listOfRegistries
    return wrapper
@decoratorGetRegistry
def getRegistry():
    '''
    If the is commented it will take the values from /tmp/
    '''
    listOfRegistries = {'TOPIC': environ.get('TOPIC'), 'PROJECT_ID': environ.get('PROJECT_ID')}    
    return listOfRegistries