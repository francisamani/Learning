# Francis Amani
# Pythion 2.0

""" Dictionaries """

# First Trial

print ''
student_details = { 'id':"16671/1313", 'name': "John Doe"
    }

print student_details ['id']

# Second trial

print ''
student_details ['course'] = 'computer science'
print student_details

# Third trial

name = (raw.input('Kindly provide us with your name?\n'))
school_id = (raw_input('Provide us with your school ID?\n'))
entry_year = (raw.input('What year did you join?\n'))
gender = (raw.input('Are you male or female?\n'))
course = (raw.input('What course are you pursuing?\n'))
age = (raw.input('How old are you?\n'))

student details = {'name':name, 'school_id':school_id, 'entry_year':entry_year, 'gender'}

str(student_details)
print(student_details)

print(len(student_details))
print(student_details.keys())
print(student_details.values())

# For loops

for age in range(1,20):
    print age

# Looping a score list
list = [1,5,15]
for x in list:
    print list
