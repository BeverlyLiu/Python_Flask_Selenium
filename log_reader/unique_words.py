infile = 'err.log'
outfile = 'results.txt'

def extract_unique(infile, outfile):
    with open(infile, 'r') as f:
        data = f.read()
    words = data.split()
    unique_words = list(set(words))

    comma_delimited = ','.join(unique_words)

    with open(outfile, 'w') as f:
        f.write(comma_delimited)

extract_unique(infile, outfile)