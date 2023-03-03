def calculator():
    sum = 0
    inp = input('Enter two or more numbers with spaces in between: ')
    numbers = inp.split()

    if len(numbers) > 1:
        for n in numbers:
            #list_of_numbers.append(float(n))
            sum += float(n)
        print('Answer:',sum)
    else:
        print('Error: Not enough numbers')

calculator()