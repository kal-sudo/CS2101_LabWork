grades={'A':90,'B':80,'C':70,'D':60,'F':0}
marks=[]
num_grades=int(input("Enter the number of subjects:"))
for i in range (num_grades):
    element=int(input(f"Enter marks of subject {i+1}:"))
    marks.append(element)

for i, mark in enumerate(marks):
    if mark >= grades['A']:
        print(f"Grade of subject {i+1}: A")
    elif mark >= grades['B']:
        print(f"Grade of subject {i+1}: B")
    elif mark >= grades['C']:
        print(f"Grade of subject {i+1}: C")
    elif mark >= grades['D']:
        print(f"Grade of subject {i+1}: D")
    else:
        print(f"Grade of subject {i+1}: F")