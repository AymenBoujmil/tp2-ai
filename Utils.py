def successors(liste):
    children = list()
    for el in liste:
        if type(el) == int:
            if el != 1 and el != 2:
                temp = list(liste)
                temp.remove(el)
                children=children+devise(el,temp)
        else:
            for e in el:
                if e != 1 and e != 2:
                    temp = list(el)
                    temp.remove(e)
                    children = children + devise(e, temp)
    return children


def devise(el,temp):
    devisers = list()
    for i in range(1, int(el/2)+1):
        if i != el-i:
            child= list([i,el-i])
            devisers.append(temp+child)
    return devisers

def terminal(state):
    for el in state:
        if el != 1 and el != 2:
            return False
    return True

def gameOver(liste):
    for state in liste:
        if(type(state) == int):
            return terminal(liste)
            break
        if terminal(state):
            return True
    return False
