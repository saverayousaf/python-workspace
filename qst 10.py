# Q10: Number classification function
def classify_numbers(number_list):
    counts = {'positive': 0, 'zero': 0, 'negative': 0}
    
    for num in number_list:
        if num > 0:
            print(f"{num} is positive")
            counts['positive'] += 1
        elif num == 0:
            print(f"{num} is zero")
            counts['zero'] += 1
        else:
            print(f"{num} is negative")
            counts['negative'] += 1
    
    return counts

numbers = [5, -2, 0, 12, -7, 0, 8]
result = classify_numbers(numbers)
print("Counts:", result)
