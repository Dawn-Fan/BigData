with open('fiel.txt','r+') as f:
    a = 2

    print(f.read())
    f.seek(0, 0)
    f.truncate(0)
    print(f.read())
    f.write(str(a))
    f.seek(0, 0)
    f.truncate(0)
    f.write(str(a))
    f.seek(0, 0)
    f.truncate(0)
    f.write(str(a))
    print(f.read())
    f.close()
    # f.write(str(a))
    #
    # f.write(str(a))
    #
    # f.write(str(a))
    #
    # f.write(str(a))
    # # print(a)
    # # a = int(a)
    # print(type(a))
