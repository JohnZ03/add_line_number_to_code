file_name = input("Input file name: ")
file_to_convert = open(file_name, 'r')
line_count = 1
output = open("output.txt", 'w')

lines = file_to_convert.read().splitlines()

for line in lines:
    output.write(str(line_count) + ":  " + line+'\n')
    line_count += 1

output.close()
file_to_convert.close()