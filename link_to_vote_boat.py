#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PURPOSE: For linking together the vote-boat-site to django-vote-boat

This creates symbolic links to the templates and static files found in 
django-vote-boat/vote_boat/ 

AUTHOR: dylangregersen
DATE: Sat Aug 16 12:06:55 2014
"""
# ########################################################################### #

# import modules 

from __future__ import print_function, division
import os 
import sys 
import re 
import time

# ########################################################################### #

# get directory from user
while True:
    path = raw_input("give the directory to the django-vote-boat [../django-vote-boat]: \n") or "../django-vote-boat"    
    if os.path.isdir(path):
        if os.path.isdir(os.path.join(path,"vote_boat")):
            path = os.path.abspath(path)
            break
        else:
            print("not the correct directory")
    else:
        print("not a valid directory")
     
   
# create symbolic links in appropriate places
print("\ncreating links -->")
pwd = os.path.dirname(__file__)
for value in "templates static".split():
    # source from the vote_boat app
    src = os.path.join(path,"vote_boat",value,"vote_boat")
    # dest to the vote_boat_site
    dest = os.path.join(pwd,"vote_boat_site",value,"vote_boat")
    # run linking command
    cmd = "ln -s {} {}".format(src,dest)
    print(cmd)
    os.system(cmd)




    
