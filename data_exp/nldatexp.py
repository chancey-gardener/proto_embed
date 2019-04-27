#/usr/bin/env python
# CMPS-143 NLP, asgn1
# A.Ian Bicket, SID: 1561327

import nltk, zipfile, argparse, sys


###############################################################################
## Utility Functions ##########################################################
###############################################################################
# This method takes the path to a zip archive.
# It first creates a ZipFile object.
# Using a list comprehension it creates a list where each element contains
# the raw text of the fable file.
# We iterate over each named file in the archive:
#     for fn in zip_archive.namelist()
# For each file that ends with '.txt' we open the file in read only
# mode:
#     zip_archive.open(fn, 'rU')
# Finally, we read the raw contents of the file:
#     zip_archive.open(fn, 'rU').read()

def unzip_corpus(input_file):
    zip_archive = zipfile.ZipFile(input_file)
    try:
        contents = [zip_archive.open(fn, 'rU').read().decode('utf-8')
                    for fn in zip_archive.namelist() if fn.endswith(".txt")]
    except ValueError as e:
        contents = [zip_archive.open(fn, 'r').read().decode('utf-8')
                    for fn in zip_archive.namelist() if fn.endswith(".txt")]
    return contents


###############################################################################


def process_corpus(corpus_name, pos_filename='-pos.txt',
                   freq_filename='-word-freq.txt',
                   posfreq_filename='-pos-word-freq.txt'):

    pos_filename = corpus_name + pos_filename
    freq_filename = corpus_name + freq_filename
    posfreq_filename = corpus_name + posfreq_filename
    input_file = corpus_name + ".zip"
    rawdat = unzip_corpus(input_file)
# 1.

    # Delimit sentences/tokenize, and declare nltk.Text object 1(b)/
    corpus_contents = [[nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(text)] for text in rawdat]
        #[nltk.word_tokenize(sent) for sent in [nltk.sent_tokenize(text) for text in rawdat]]
    corpus = nltk.Text([word for text in [nltk.word_tokenize(file) for file in rawdat] for word in text])
    #corpus = nltk.Text([token for sent in corpus_contents for token in sent])
    tagbank = []

# 2
    #  (a) and (b) apply POS tagger and write to file
    with open(pos_filename, 'w') as posfile:
        for text in corpus_contents:
            for sent in text:
                tags = nltk.pos_tag(sent)
                tagbank += tags
                line = ' '.join(['{}/{}'.format(w[0], w[1]) for w in tags])
                posfile.write(line + '\n')
            posfile.write('\n')


# 3
    words = [word[0] for word in tagbank]
    fdist = nltk.FreqDist([word.lower() for word in words])  # 3(c)
    # 3 (c)
    with open(freq_filename, 'w') as freqfile:
        freqfile.writelines(str(freq) + '\n' for freq in sorted(list(fdist.items()), key=lambda x: x[1], reverse=True))
    # 3(d)
    f_given_tag = nltk.ConditionalFreqDist([tag[::-1] for tag in tagbank])
    word_count = fdist.N()
    vocab_length = fdist.B()
    mc_pos = max(f_given_tag.items(), key=lambda x: x[1].N())
    most_common = fdist.most_common(1)[0]  # 3 (b)
    # change stdout to file and write with tabulate method
    pffile = open(posfreq_filename, 'w')
    stdout = sys.stdout
    sys.stdout = pffile
    f_given_tag.tabulate()
    sys.stdout.close()
    sys.stdout = stdout
    print('\nCorpus Name: {} \n\nTotal Word Count: {}\nVocabulary Size: {}\n'.format(corpus_name,
                                                                                   word_count,
                                                                                   vocab_length))  # 3 (a) ( 1(a))
    print('Most frequent word: {}; {} instances\n'.format(most_common[0],
                                                        most_common[1]))  # 3(b)
    print('Most frequent part of speech: {}, {} occurrences'.format(mc_pos[0], mc_pos[1].N()))



# 4 and 5
    for pos in ('NN', 'VBD', 'JJ', 'RB'):
        mc = f_given_tag[pos].most_common(1)[0]
        print("""
Most common {}: {} | {} instances
Words found in similar contexts:""".format(pos, mc[0], mc[1]))
        corpus.similar(mc[0])
    print('\nCollocations:')

    corpus.collocations()
    print('\n')



###############################################################################
## Program Entry Point ########################################################
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Assignment 1')
    parser.add_argument('--corpus', required=True, dest="corpus", metavar='NAME',
                        help='Which corpus to process {fables, blogs}')

    args = parser.parse_args()

    corpus_name = args.corpus

    if corpus_name == "fables" or "blogs":
        process_corpus(corpus_name)
    else:
        print("Unknown corpus name: {0}".format(corpus_name))

