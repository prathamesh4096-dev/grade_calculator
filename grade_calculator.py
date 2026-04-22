# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:38:47 2026

@author: Prathamesh
"""
name = str(input("Enter student name: "))
marks = int(input("Enter marks (0-100): "))

while not (0 <= marks <= 100):                                  #Input Validation logic
    print("❌ Out of range. Try again.")
    marks = int(input("Enter marks between 0 and 100: "))
    
if marks >= 90:                                                 # A Grade condition
    grade = 'A'
    message = 'Very Good! Keep it up!👍'
elif marks >= 80:                                               # B grade condition
    grade = 'B'
    message = 'Well Done!'
elif marks >= 70:                                               # C grade condition
    grade = 'C'
    message = 'Average performance.'
elif marks >= 60:                                               # D Grade condition
    grade = 'D'
    message = 'You can do better.'
else:                                                           # F grade condition
    grade = 'F'
    message = 'You failed. Try again.'

print(f'\nResult for {name}: ')                                 # Formatted output
print(f'Marks: {marks}')
print(f'Grade: {grade}')
print(f'Comments: {message}')