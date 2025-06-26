marks=[]
with open(r"C:\Users\MTBD\Documents\marks.csv","r") as file:
  for lb in file:
    marks.append(int(lb.strip()))
marks.sort()
for index,mark in enumerate(marks):
 if mark>=90:
  grade="A+"
 elif mark>=80:
  grade="A"
 else:
  grade="fail"
 print(f"index {index} : mark {mark} Grade={grade}")

Highest = max(marks)
if Highest>=90:
  top="A+"
elif Highest>=80:
 top="A"
else:
 top="fail"
print(f"hvalue={Highest} and Grade={top}") 