
def happy_numbers(number_range):

    lower_limit = number_range[0]
    upper_limit = number_range[1]
    happy_list = []

    for num in range(lower_limit, upper_limit+1):
        cycle = 0
        num_rotate = num

        while cycle <= 100:
            digit_square_sum = 0
            for index in range(0,len(str(num_rotate))):
                digit_square_sum += int(str(num_rotate)[index])**2
            num_rotate = digit_square_sum
            if num_rotate == 1:
                happy_list.append(num)
                break
            else:
                cycle += 1

    print("Happy numbers in your selected range are: ")

    for element in happy_list:
        print(element)

test_range = (0,30)
happy_numbers(test_range)
