# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:35:47 2024

@author: dkkie
"""

import csv

def ReadData(): # dictionary, tuple
    with open('movies.txt', mode='r') as file:
        reader = csv.DictReader(file)
        
        rdata = {}
        
        for row in reader:
           rdata[row['name']] = tuple([row['rating'], row['Duration'], row['Year'], row['Genre'], row['Gross_income']])
           
    return rdata

def SaveData(new_data):
    with open('movies.txt', mode='w', newline='') as file:
        fields = ['name', 'rating', 'Duration', 'Year', 'Genre', 'Gross_income']
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for row in new_data.keys():
            writer.writerow({fields[0]:row, fields[1]:new_data[row][0], fields[2]:new_data[row][1], fields[3]:new_data[row][2], fields[4]:new_data[row][3], fields[5]:new_data[row][4]})
            


