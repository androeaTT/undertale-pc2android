

def file2string(filename, text=None):
    with open(filename, 'r') as file:
        lines = file.readlines()

    single_line_content = '\r\n'.join([line.strip() for line in lines])
    
    return single_line_content


def ini2string(input_file):
    result = ""
    
    # Чтение файла построчно
    with open(input_file, 'r') as file:
        file_contents = file.readlines()

    for line in file_contents:
        new_line = line.rstrip('\n')

        if not new_line.startswith("["):
            r = new_line.split("=")
            if len(r) > 1 and '"' in r[1]:
                p = r[1].split('"')
                new_line = r[0] + '=\"' + p[1] + '\"'

        new_line += "\r\n"

        result += new_line

    result = result.replace("\\r\\n[", "\\r[")

    return result


def main():
    files = {"default" : "", "file9" : file2string("file9"), "config.ini" : "", "undertale.ini" : ini2string("undertale.ini"), "file0" : file2string("file0"),}
    finalfiles = str(files)
    with open('undertale.sav', 'w') as file:
        file.write(str(finalfiles))

    

main()
