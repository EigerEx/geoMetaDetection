import os

directory = "data\\labels\\"
checklist = []

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print(filename)
        with open(f, "r") as rf:
            num = rf.read(1)
            checklist.append(num)
            print(num)

with open("data\\checknum.txt","w") as f:
    for entry in checklist:
        f.write(entry +  ",")

print("Finished")
