def readFiles():
    data = []
    with open('tornado.txt', 'r') as file:
        for i in file:
            data.append((i.rstrip()).split(","))
        file.close()
        print("F3 tornado in Alabama since 2000: ")
        print("Year", "%-30s"%"County", "%5s"%"Fat.", "%5s"%"Inj.")
        for i in data:
            if i[2] == "F3" and int(i[0]) >= 2000:
                print(i[0], "%-30s"%i[1], "%5s"%i[3], "%5s"%i[4])
    
    
readFiles()
