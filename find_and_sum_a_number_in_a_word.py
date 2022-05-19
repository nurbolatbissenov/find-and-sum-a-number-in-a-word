str = []
list = []
string = 'BMW530'

for number in string:
    if number.isdigit():
        list.append(int(number))
    elif number.isalnum():
        str.append(number)

print('This is string:',''.join(str))
print('This is integer: ',list)
print('Sum:',sum(list))