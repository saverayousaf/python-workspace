# Q9: Number classification
numbers = [5, 12, 7, 18, 9, 24, 3, 16, 11]
div3 = 0
even_not_div3 = 0
odd_not_div3 = 0

for num in numbers:
    if num % 3 == 0:
        print(f"{num} is divisible by 3")
        div3 += 1
    elif num % 2 == 0:
        print(f"{num} is even but not divisible by 3")
        even_not_div3 += 1
    else:
        print(f"{num} is odd and not divisible by 3")
        odd_not_div3 += 1


