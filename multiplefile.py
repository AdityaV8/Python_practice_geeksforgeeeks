contents = ["Aditya is a boy","Aditya is a play boy","Aditya is learning python"]
filenames = ["file1.txt","file2.txt","file3.txt"]

for content,filename in zip(contents,filenames):
    file = open(f"filehandling/{filename}","w")
    file.write(content)