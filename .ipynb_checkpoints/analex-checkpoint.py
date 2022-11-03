
if __name__ == "__main__":
    filename = "prueba.mio"
    TXT = []
    IDS = []
    VAL = []

    token_list = list()
    with open(filename) as fp:
        for line in fp:
            token_list.extend(line.split(" "))
    print("\n".join(token_list))
