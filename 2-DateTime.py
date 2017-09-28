import  datetime

current_date = datetime.date.today()

# print(current_date.strftime('%d %b, %Y'))
# #user_input = input('Inform your birthday')
# #birthday = datetime.datetime.strptime(user_input, '%d/%m/%Y')
# #print(birthday)
# print(current_date.year)
# print(current_date.month)
# print(current_date.day)
#
# date_day = 27
# date_month = 2
# date_year = 1982
#
# date_form = str(date_day) + '/' + str(date_month) + '/' + str(date_year)
# print(date_form)
# date_stored = datetime.datetime.strptime(date_form, '%d/%m/%Y').date()
# print(date_stored)
#
# result = current_date - date_stored
# print(result)

user_input = input('Inform the dead line: ')
deadline = datetime.datetime.strptime(user_input, '%d/%m/%Y').date()
due_days = (deadline - current_date).days
print('You have ' + str(due_days//7) + ' week(s) and ' + str(due_days%7) + ' days')