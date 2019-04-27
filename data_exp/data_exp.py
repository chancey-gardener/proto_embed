#!/usr/bin/python3

import nltk, sys, argparse as ap

ROUND_TO=5

def readfile(path):
    with open(path) as dfile:
        text = dfile.read()
    return text

def normalize(w):
    return w.lower().strip()

def wordmat(text):
    return [[normalize(word) for word in nltk.word_tokenize(sent)] for
            sent in nltk.sent_tokenize(text)]

def freqdist(wm, normed=False):
    out = {}
    # TODO: refactor this to be more concise
    # maybe the best way is to user Counter object and update
    if isinstance(wm[0], list):
        for sent in wm:
            for word in sent:
                if word not in out:
                    out[word] = 1
                else:
                    out[word] += 1
    elif isinstance(wm[0], str):
        for word in wm:
            if word in out:
                out[word] += 1
            else:
                out[word] = 1
    else:
        raise TypeError("Unrecognized wordmat format: {}<{}>".format(type(wm), type(wm[0])))
    # generally, we don't want to set normed from freqdist since 
    # the normalized values are easily recoverable from raw frequencies, and 
    # this function will, in most cases, return output intended to be combined
    # with other frequency distributions, and may require a normalizing constant
    # that isn't recoverable from this namespace.
    if normed:
        vsize = len(out)
        out = {word:f/vsize for word in out}
    return out

def cfreqdist(wm, n, reverse=False, normed=False, sent_partition=True):
    '''gives a conditional frequency distribution from a wordmap
        sent_partition: if set to false, we'll consider ngrams across sentences.
        RETURN TYPE: DICT<STRING, DICT<STRING:
    '''
    #out = {}
    # set subroutines w/args
    rrange = lambda w: range(w) if not reverse else reversed(range(w))
    ngram = lambda seq, i: tuple(seq[i:i+n])

    # TODO: refactor the following block to make it more concise
    if not sent_partition:
        # TODO: support optional filtering of punctuation given this setting.
        flat = [word for word in sent for sent in wm]
        tokset = set(flat)
        dat = [ngram(flat, i) for i in rrange(len(flat)-n)]
    else:
        tokset = set(word for sent in wm for word in sent)
        dat = [[ngram(sent,i) for i in rrange(len(sent)-n)] 
                      for sent in wm]


    # now get the frequencies
    out = {w:{} for w in tokset}
    for seq in dat:
        tok, cond = seq[0], seq[1:]
        if cond in out[tok]:
            out[tok][cond] += 1
        else:
            out[tok][cond] = 1
    if normed:
        out = {t:{seq:out[t][seq]/len(out[t]) 
                for seq in out[t]} 
                    for t in out}

    return out
        


def tok_seq_analyze( **kwargs):
    '''Returns a frequency distribution for sequences of size n
    for each integer n given as a positional argument.
    Keyword arguments:
        REQUIRED: filepath - filepath to NL text file
        OPTIONAL: reverse_condition: optional bool; see help message for command line flag --condition_on_subsequents
        
    '''
    print(dir())
    print("\n\n")
    print(kwargs.keys())
    print("\n\n")
    fpath = kwargs["fpath"]

    if len(seqs) == 0:
        args = [1]
    if "sent_partition" in kwargs:
        sp = kwargs["sent_partition"]
    else:
        sp = True
    if "reverse_condition" in kwargs:
        reverse_conditioning = kwargs["reverse_condition"]
    else:
        reverse_conditioning = False

    text = readfile(fpath)
    # generate conditional frequency distribution(s)
    out = {}    
    for wsize in sorted(seqs):
        if wsize == 1:
            fd = freqdist(wordmat(text))
        else:
            fd = cfreqdist(wordmat(text), n=wsize, reverse=reverse_conditioning, sent_partition=sp)
        out[wsize] = fd
    return out

def pprintfreqdists(fds, fname):
    whole_log = "Frequency analysis for {}\n".format(fname)

    for f in fds:
        whole_log += _printfreqdist(fds[f], f)+"\n\n"
        
    return whole_log

def _printfreqdist(fd, w):
    ttype = "{} word sequences".format(w) if w > 1 else "single words"
    header = "\tFrequency Analysis for {}\n\n".format(ttype)
    strlog = header
    print(header)
    vocab_size = len(fd)
    if w == 1:
        for tok in fd:
            prob = round(fd[tok], ROUND_TO)
            line = "\t\t{}: {}".format(tok, pct_f)
            strlog += "\n" + line
    else:
        for tok in fd:
            wtitle = "\n\t\tConditional Frequency of: {}".format(fd[tok])
        for cseq in sorted(fd[tok].items(), key=lambda p: p[1]):
            seq, n_occurrences = ' '.join(cw for cw in cseq[0]), cseq[1]
            cnprob = n_occurrences/vocab_size
            #TODO: update headers here to reflect whether we're getting subsequent conditions
            # or precedent conditions.
            line = "\t\t\tProbability of {} given {}: {} | {} total occurrences in file".format(tok, seq, cnprob, n_occurrences)
            print(line)
            strlog += "\n" + line
    return strlog




if __name__ == "__main__":
    # handle command line arguments
    aprsr = ap.ArgumentParser(description="freqer; a first glancer at the statistical structure of a natural language text file")
    aprsr.add_argument("-files", required=True, metavar="F", type=str, nargs='+',
            help="Relative path to a natural language text file for first pass frequency analysis")
    aprsr.add_argument("--sequences",dest="sequences", metavar="S", type=int,
                        nargs='+',default=[1, 2],
                        help="n, where n tells freqer to return a frequency analysis of n-grams, feed in as many as you want.")
    aprsr.add_argument("--conditional_sequences", metavar="C", type=int, nargs='+',default=[2], help="each integer set here will tell freqer to analyze p(s[k]|s[k[0:k-1]) (default)  OR p(s[0]|s[1:]) if --condition_on_subsequents is set for each sequence s of length k", dest="conditional_sequences")
    aprsr.add_argument("--condition_on_subsequents",  action="store_const", const=True, default=False, help="If set, conditional sequences will be analyzed in reverse order, so P(s[0] | s[1:]) instead of p(s[k]|s[:k-1]), which is the default procedure. Obviously, this flag does nothing if --conditional_sequences is set to nothing. If you do this, frequer will throw a warning, but will continue with any valid procedures it has been passed via cmd line args.")
    aprsr.add_argument("--tojson", type=str, dest="tojson")
    aprsr.add_argument("--totxt", type=str, dest="totxt")
    args = aprsr.parse_args()
    # do stuff
    def main(**kwargs):
        print(kwargs.keys())
        # TODO: clean up argument passing
        files = kwargs['files']
        condition_on_subsequents=kwargs['condition_on_subsequents']
        sequences=kwargs['sequences']
        for f in files:
            # get data from each file
            odat = tok_seq_analyze(fpath=f, 
                    reverse_conditioning=condition_on_subsequents,
                    seqs=sequences)

                                

    # and here. we. go.
    seqs = args.sequences
    kwmap = {k[0]:k[1] for k in args._get_kwargs()}
    print(kwmap.keys())
    main(**kwmap)




