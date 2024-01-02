marks = []
name = input('name: ')
marks.append(name)

point1 = float(input('point1: '))
marks.append(point1)

point2 = float(input('point2: '))
marks.append(point2)

point3 = float(input('point3: '))
marks.append(point3)

point4 = float(input('point4: '))
marks.append(point4)

average = (marks[1] + marks[2] + marks[3] + marks[4]) / 4
print("Average:", average)
