def tokenization(filename) -> list:
    token_list = []
    try:
        with open(filename) as fp:
            for line in fp:
                if line[0] != "#":
                    token_list.append(line.split(" "))
        fp.close()

        for linea in token_list:
            if linea[-1] == "\n":
                linea.pop()
            elif linea[-1][-1:] == "\n":
                linea[-1] = linea[-1][:-1]

    except FileNotFoundError as e:
        print(f"Error: No es posible encontrar el archivo {filename}")
    finally:
        return token_list

