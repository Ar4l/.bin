#!/usr/bin/env python3
import mytudelft as mytud

import click

course_schedule='schedule_cse'
course_list = ['CSE2315', 'CSE2120', 'CSE2530'] 

def login():

    try:
        credentials = open('login.cred', 'r').readline()[:-1].split(':')
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
    # username = click.prompt('Please enter username', type=str, default=credentials[0])
    # password = click.prompt('Please enter password', type=str, default=credentials[1], hide_input=True)
    # mytud.login(username, password)

def enroll(): 
    for course in course_list:
        try: 
            mytud.register_for_course(course)
        except BaseException as e:
            print(f'{course} failed: {e}')

login()
enroll()
