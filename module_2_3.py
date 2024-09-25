my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count=0
while count < len(my_list):
    numbers = my_list[count]
    count=count + 1
    if numbers == 0:
       continue
    elif numbers < 0:
       break
    elif count == len(my_list):
        print (numbers)
        print ("Конец списка")
    else:
        print (numbers)












