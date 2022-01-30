a = input().split()
stu_id,grade = a
list_id = [stu_id]
list_grade = [grade]
while True:
    a = input().split()
    if a == ["q"]:
        break
    else:
        stu_id, grade = a
        list_id.append(stu_id)
        list_grade.append(grade)
edit = input().split()
grades = ["F","D","D+","C","C+","B","B+","A"]
for i in range(len(edit)):
    index_id = list_id.index(edit[i])      #หาตำแหน่งของตัวที่ต้องการแก้
    grade_edit = grades[grades.index(list_grade[index_id])+1]   #แก้ตัวที่ต้องการแก้
    list_grade[index_id] = grade_edit
for i in range(len(list_grade)):
    print(list_id[i],list_grade[i])