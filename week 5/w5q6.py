print("enter multi-line text(press Enter twice to finish):")

lines =[]
while True:
    line =input()
    if line=="":
        break
    lines.append(line)

print("\ntext after removing indentation:")

for line in lines:
    print(line.lstrip())

    
  
