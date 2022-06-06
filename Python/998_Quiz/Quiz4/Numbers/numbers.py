mynumbers = [6,9,32,28,15,22,3,18]
minimum = mynumbers[0]
for i in mynumbers:
    if i < minimum:
        minimum=i
print(minimum)

maximum = mynumbers[0]
for i in mynumbers:
    if i > maximum:
        maximum=i
print(maximum)

average=0
count=0
for i in mynumbers:
    average=average+i
    count=count+1
average=average/count
print(average)