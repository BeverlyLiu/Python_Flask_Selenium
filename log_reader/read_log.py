file_name = 'err.log'

def ReadFileContents(file_name):
    with open('err.log', 'r') as infile:
        with open('results.txt', 'w') as outfile:
            num_line = 0
            outfile.write('\nError found:\n')
            for line in infile:
                if "ERR" in line:
                    # print(line)
                    outfile.write(line)
                    num_line += 1
            outfile.write('\nThe number of errors: ')
            outfile.write(str(num_line))

ReadFileContents(file_name)