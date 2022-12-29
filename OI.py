
#Lab assigment_fileIO

def getFile():
    input_file_opened = False
    while not input_file_opened:
        try:
            file_name = input('Enter input file name (with extension): ')
            input_file = open(file_name, 'r')
            input_file_opened = True
        except IOError:
            print ('Input file not found - please reenter')
            
    return (file_name, input_file)


file_name, input_file = getFile()
output_file = open('output.txt','w')
line = input_file.readline()
while line != '':
    output_file.write(line.replace(" ",""))
    print(line.replace(" ",""), end='')
    line = input_file.readline()


input_file.close()
output_file.close()

