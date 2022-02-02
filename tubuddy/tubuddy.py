#!/usr/bin/env python3
import mytudelft as mytud
import queue 
import schedule 

import click
import json

course_schedule='schedule_cse'
course_list = ['CSE2315', 'CSE2120', 'CSE2530'] 
schedule = Schedule() 

def login():

    try:
        credentials = open('rsc/login.cred', 'r').readline()[:-1].split(':')
        mytud.login(credentials[0], credentials[1])

    except BaseException as e:
        print(f'Credentials invalid: {e}')

        while(True):
            try: 
                username = click.prompt('username (netid)', type=str)
                password = click.prompt('password', type=str, hide_input=True)

                if mytud.login(username, password): 
                    
                    break

            except BaseException as e:
                print(f'Incorrect credentials: {e}')
    
    print(f'Logged in!')

def enroll(): 
    for course in course_list:
        try: 
            mytud.register_for_course(course)
        except BaseException as e:
            print(f'{course} failed: {e}')

def check():
    """
    Print enqueuings and enrol for the next two weeks
    """
    
    # check currently enqueued
    # From List<QueueItem> remove past QueueItems
    # Print QueueItems for today, given that we have their queue status

    # Print recently registered tests

    # Enrolling
    # Enroll for as many QueueItems as possible
    # Fetch queue status for next two weeks' items

def test_registrations():
    """ 
    Get current test registrations
    """

def course_registrations():
    """
    Get current course registrations
    """
    
    # Print following programme {prg} with the {var} variant,
    # Taking additional courses: {c for c in courses}

def queue_registrations():
    """
    Get current registrations for queue
    """

login()
enroll()
