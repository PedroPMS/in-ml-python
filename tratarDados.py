def tratarDados():
    with open('./dermatology.names', 'r+') as file:
        header = file.readline()

    with open('./dermatology.data', 'r+') as f:
        firstLine = f.readline()
        if (firstLine[0].isnumeric()):
            content = f.read()
            f.seek(0, 0)
            f.write(header.rstrip('\r\n') + '\n' + content)
