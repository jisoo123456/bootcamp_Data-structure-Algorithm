def sort(array):
    for i in array: #0: i = [sera, 88]
        for j in range(1, len(array)): # 1 2 3 4 5
            if array[j][1] < array[j-1][1]:
                array[j], array[j-1] = array[j-1], array[j]

    return array


student_array = [['sera', 88], ['alice', 99], ['tom', 71], ['tony', 78], ['judy', 67], ['bella', 92]]

print(student_array)
sort(student_array)
print(student_array)

for i in range(len(student_array)//2):
    print(f'[{student_array[i][0]}, {student_array[len(student_array)-1-i][0]}]')