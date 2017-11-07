def read_music_not(file, mode):
    count = 0
    has_title = True
    file = open(file, mode)
    result = open("res.txt", "w")
    for line in file:
        x = line[2:-1]
        y = " ... "
        if line[:2] == "X:":
            result.write(x + y)
            count += 1
            has_title = False
        elif (line[:2]  == "T:" and not has_title):
            result.write(x +y)
            has_title = True
        elif (line[:2] == "M:"):
            result.write(x + y)
        elif (line[:2] == "K:"):
            result.write(x)
            result.write("\n")

    file.close()
    result.close()

read_music_not("hnr1.txt", "r")