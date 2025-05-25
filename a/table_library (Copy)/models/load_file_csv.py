import csv
import os

from flask import request
from table_library.models.create_session import sessions
from table_library.models.student import Student

def load_csv_file():
    file = request.files['csv_fils']
    file.save(os.path.join(file.filename))
    with open(file.filename,'r')as filename:
        name_file = ['first_name','last_name','phone','email']
        read_file = csv.DictReader(f=filename,fieldnames=name_file,delimiter=";")
        dict_list = []

        for string in read_file:
            print(string)
            dict_list.append(string)


        sessions.bulk_insert_mappings(Student,dict_list)
        sessions.commit()
load_csv_file()