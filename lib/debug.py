#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from department import Department
from employee import Employee

import random
from faker import Faker

fake = Faker()

def reset_database():
    Department.drop_table()
    Department.create_table()
    Employee.drop_table()
    Employee.create_table()

    payroll = Department.create("Payroll", "Building A, 5th Floor")
    hr = Department.create("Human Resources", "Building C, East Wing")

    job_titles = ['Manager', 'Accountant', 'Clerk', 'Assistant', 'Coordinator']

    for _ in range(5):
        name = fake.first_name()
        job_title = random.choice(job_titles)
        department_id = random.choice([payroll.id, hr.id])
        Employee.create(name, job_title, department_id)

reset_database()
import ipdb; ipdb.set_trace()
