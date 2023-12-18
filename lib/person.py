#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="", job=""):
        self.name = name
        self.job = job
        name_check = (isinstance(name, str) and not (len(name) < 1 or len(name) > 25))
        job_check = job in APPROVED_JOBS
        if name == False:
            print("Name must be string between 1 and 25 characters.")
        elif (len(job) >0) and (not job_check):
            print('Job must be in list of approved jobs.')
        elif (not name_check):
            print("Name must be string between 1 and 25 characters.")
        elif (not job_check) and (self.name==""):
            print('Job must be in list of approved jobs.')
        else:
            name_cased = " ".join([s.capitalize() for s in name.split(" ")])
            self.name = name_cased
            pass
