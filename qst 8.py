# Q8: Tuple marks operations
marks = (75, 80, 65, 90, 85)


print("First mark:", marks[0])
print("Last mark:", marks[-1])


m1, m2, m3, m4, m5 = marks
print("Unpacked marks:", m1, m2, m3, m4, m5)


new_marks = tuple(mark + 5 for mark in marks)
print("Original marks:", marks)
print("New marks (+5):", new_marks)
