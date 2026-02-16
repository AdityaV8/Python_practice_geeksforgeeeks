def get_average():
    with open("filehandling/file4.txt") as file:
        data = file.readlines()[1:]
    values = [float(i.strip()) for i in data]  
    avg = sum(values) / len(values)
    return avg

print(get_average())