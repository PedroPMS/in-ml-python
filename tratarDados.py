def tratarDados():
    with open('./dermatology.names', 'r+') as cabecalho:
        header = cabecalho.readline()
    cabecalho.close()

    with open('./dermatology.data', 'r+') as dados:
        contents = dados.read()
        retirandoInterrogacao = contents.replace('?', '0')
    dados.close()

    with open("./dermatology.data", "w") as dados:
        dados.write(retirandoInterrogacao)
    dados.close()

    with open('./dermatology.data', 'r+') as dados:
        firstLine = dados.readline()
        if (firstLine[0].isnumeric()):
            content = dados.read()
            dados.seek(0, 0)
            dados.write(header.rstrip('\r\n') + '\n' + content)
    dados.close()
