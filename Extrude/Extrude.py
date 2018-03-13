
def readfile(imput):
    file = open(imput, "r")
    vertex = []
    face = []
    for line in file:
        li = line.split(' ')
        if li[0] == "v":
            mylist = []
            for i in range(1, 4):
                mylist.append(float(li[i]))
            vertex.append(mylist)
        elif li[0] == "f":
            mylist = []
            for i in range(1, 4):
                mylist.append(int(li[i]))
            face.append(mylist)

    return vertex,face

if __name__ == "__main__":
    imput="textito.obj"
    lista1,lista2=readfile(imput)
    print lista1
    print lista2