import os, glob
import chardet

extension = input("File extension to change encode (ex: .txt): ")
newEncoding = input("Encoding to change (ex: utf8): ")

for file in glob.glob(f'*{extension}'):
    try:
        data = open(file, 'rb').read()
        encoding = chardet.detect(data)['encoding']

        with open(file, encoding=encoding) as fileToRead:
            data = fileToRead.read()
        with open(file, 'w', encoding=newEncoding) as fileToChange:
            fileToChange.write(data)
        print('Arquivo convertido com sucesso!')

    except:
        raise Exception('Não foi possível converter estes arquivos!')