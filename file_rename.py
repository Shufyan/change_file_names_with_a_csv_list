# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 01:45:50 2020

@author: Shufyan
"""
# import required libraries
from csv import reader
import os

# Setting variables
csv_path = ""                  # Enter the folder path of CSV file containing the file path input & new file name.
csv_file_name = "sample.csv"   # Enter the file name of CSV file containing the file path input & new file name.

# A generic function to split the file path and filename
def path_and_filename(source_file_path):
    head_tail = os.path.split(source_file_path)
    source_path = head_tail[0]
    filename = head_tail[1]   
    return source_path, filename

print(u'os.getcwd() {}'.format(os.getcwd()))
# open file in read mode
with open(os.path.join(csv_path,csv_file_name), 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        if len(row) == 0:
            break
        # row variable is a list that represents a row in csv
        source_path, filename = path_and_filename(row[0])
        filename_updated = row[1]
        
        try:
            os.chdir(source_path)
            os.rename(filename,filename_updated)
        except Exception:
            continue

if __name__ == '__main__': 
    pass
