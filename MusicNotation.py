def read_music_not(file, mode):
    count = 0
    count_x = 0
    file = open(file, mode)
    res = open("res.txt", "w")
    data = file.read().split()
    for line in data:
        x = line[2:]
        y = " ... "
        if line[:2] == "X:":
            res.write(x + y)
            count += 1
            count_x = 1
        elif (line[:2]  == "T:" and count_x == 1):
            res.write(x +y)
            count_x = 0
        elif (line[:2] == "M:"):
            res.write(x + y)
        elif (line[:2] == "K:"):
            res.write(x)
            res.write("\n")

    file.close()
    res.close()

read_music_not("hnr1.txt", "r")


