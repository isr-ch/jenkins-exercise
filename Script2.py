def longes_word():
    size = 0

    with open("C:/Users/israe/PycharmProjects/pythonProject/venv/file.txt","r") as f:
        data = f.readlines()
        for line in data:
            words = line.split()
            for word in words:
               if(len(word)) > size:
                 size = len(word)

    
    return size

longes_word()
