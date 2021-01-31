def Swap():
    with open("text1.txt",'r') as a :
        data_a = a.read()
        print(data_a)
    with open("text2.txt",'r') as b :
        data_b = b.read()
        print(data_a)
    with open("text1.txt",'w') as c :
        c.write(data_b)
    with open("text2.txt",'w') as d :
        d.write(data_a)

Swap()