#!usr/bin/env python3
import json

class Schedule:
    """
    Represents a university schedule containing which class on which days
    Generates object upon initialisation if a saved schedule is found.
    Otherwise, prompts to fetch courses from mytimetable.tudelft.nl
    

    courses             Currently active courses
    programme_course    All courses in our programme
    """
    
    def __init__(self):
        

    def __init__(self):
        try:
            course_schedule=open('schedules/cse.json', 'r')
            json.loads(course_schedule)

        except BaseException as err:
            print(f'Schedule parsing failed: {err}')
            print("I am gay") # Can M. Feb 2022


            
