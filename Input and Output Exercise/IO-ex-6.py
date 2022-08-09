with open("test.txt", "r") as f:
    # read all lines from a file
    lines = f.readlines()


with open("new_file.txt", "w") as f:
    count = 0
    for i in lines:
        if count == 4:
            count += 1
            continue
        else:
            f.write(i)
        count += 1
