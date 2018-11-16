
def read_config():
    fl = open("Config")
    ls_fl = [x for x in fl]

    info_dict = {}
    blank_dict = {}

    switch = 0
    for line in ls_fl:

        if line[0] == "*":
            break

        if line[0] == "=":
            switch = 1
            continue

        if line[0] == "/" or not line.__contains__(":"):
            continue

        tmp = line.split(" :: ")

        if switch == 0:
            info_dict[tmp[0]] = tmp[1][:-1]
        if switch == 1:
            blank_dict[tmp[0]] = tmp[1][:-1]

    return blank_dict, info_dict


print(read_config())
