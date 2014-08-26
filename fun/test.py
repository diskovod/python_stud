
def total(initial=5, *numbers, extra_numbers):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    
    print(count)

total(10, 1, 2, 3, extra_number=50)
