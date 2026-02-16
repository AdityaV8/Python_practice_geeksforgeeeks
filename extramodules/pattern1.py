import glob

myfiles = glob.glob("filehandling/*.txt")

for file in myfiles:
    with open(file,"r") as f:
        print(f.read())
