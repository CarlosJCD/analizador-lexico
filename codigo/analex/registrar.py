from analex import variables

def identificador(token):
    if len(variables.IDS) == 0:
        variables.IDS.append([token, 'id01'])
    else:
        flag = True
        for row in variables.IDS:
            if row[0] == token:
                flag = False
                break

        if flag:
            num_id = f"{(len(variables.IDS) + 1)}"
            if len(num_id) == 1:
                variables.IDS.append([token, f"id0{num_id}"])
            else:
                variables.IDS.append([token, f"id{num_id}"])


def string(token: str):
    num_id = f"{(len(variables.TXT) + 1)}"
    if len(num_id) == 1:
        variables.TXT.append([token, f"txt0{num_id}"])
    else:
        variables.TXT.append([token, f"txt{num_id}"])


def num(token: str):
    if token[0:2] == "0x":
        variables.VAL.append([token, int(token, base=16)])
    else:
        variables.VAL.append([token, int(token)])

