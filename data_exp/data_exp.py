#!/usr/bin/python3

import nltk, sys, re, json, argparse as ap

ROUND_TO=5
PUNCT = {",", ".", "\\", ":", ";", "'", '"', "(", ")", "?", "!"}
RE_NWORD = r'\W'
PUNCT_FILTER  = lambda s: False if re.fullmatch(RE_NWORD, s) else True

def readfile(path):
    with open(path) as dfile:
        text = dfile.read()
    return text

def normalize(w):
    return w.lower().strip()

def wordmat(text, ignore_punct=True):
    if ignore_punct:
        out = [[normalize(word) for word in nltk.word_tokenize(sent) if PUNCT_FILTER(word)] for
            sent in nltk.sent_tokenize(text)]
    else:
        out = [[normalize(word) for word in nltk.word_tokenize(sent)]
                for sent in nltk.sent_tokenize(sent)]
    return out
                

def fdupdate(news, base):
    for k in news:
        if k in base:
            base[k] += news[k]
        else:
            base[k] = news[k]
    return base

def cfupdate(news, base):
    for k in news:
        if k not in base:
            base[k] = {}
        for s in news[k]:
            # TODO: can we do this recursively; it'd be prrtier..
            if s in base[k]:
                base[k][s] += news[k][s]
            else:
                base[k][s] = news[k][s]
    return base


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
        # now make le dat flat
        dat = [ng for sent in dat for ng in sent]


    # now get the frequencies
    out = {w:{} for w in tokset}
    for seq in dat:
        tok, cond = seq[0], seq[1:]
        #print(tok)
        #print(cond)
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
    title =  "Frequency analysis for {}\n".format(fname)
    print(title)
    whole_log = title
    for f in fds:
        flog = _printfreqdist(fds[f], f)+"\n\n"
        whole_log += flog
    return whole_log

def cfkeystostring(struct):
    ns = {}
    for ik in struct:
        if ik != 1:
            for k in struct:
                ns[k] = {}
                for sk in struct[k]:
                    str_sk = str(sk)
                    ns[k][str_sk] = struct[k][sk]
        else:
            ns[ik] = struct[ik]
    return ns

def _printfreqdist(fd, w):
    ttype = "{} word sequences".format(w) if w > 1 else "single words"
    header = "\tFrequency Analysis for {}\n\n".format(ttype)
    strlog = header
    print(header)
    vocab_size = len(fd)
    if w == 1:
        print(fd)
        for tok in fd:
            prob = round(fd[tok], ROUND_TO)
            line = "\t\t{}: {}".format(tok, prob)
            # print from here so you can specify what to print to stdout
            if fd[tok] > 1:
                print(line)
            strlog += "\n" + line
    else:
        for tok in fd:
            wtitle = "\n\t\tConditional Frequency of: {}".format(fd[tok])
            fditer = sorted(fd[tok].items(), key=lambda p: p[1])
            #print(fditer)
            for cseq in fditer:
                seq, n_occurrences = ' '.join(cw for cw in cseq[0]), cseq[1]
                cnprob = n_occurrences/vocab_size
            #TODO: update headers here to reflect whether we're getting subsequent conditions
            # or precedent conditions.
                line = "\t\t\tp( {} |  {} ): {} ::: {} instances in file".format(tok, seq, cnprob, n_occurrences)
                if n_occurrences > 2:
                    print(line)
                strlog += "\n" + line
    return strlog




if __name__ == "__main__":
    # handle command line arguments
    aprsr = ap.ArgumentParser(description="freqer; a first glancer at the statistical structure of a natural language text file")
    aprsr.add_argument( metavar="F", type=str, nargs='+',
            help="Relative path to a natural language text file for first pass frequency analysis", dest="files")
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
        # TODO: clean up argument passing
        files = kwargs['files']
        condition_on_subsequents=kwargs['condition_on_subsequents']
        sequences=kwargs['sequences']
        all_dat = {}
        for f in files:
            # get data from each file
            print("Computing word frequencies for {}".format(f))
            odat = tok_seq_analyze(fpath=f, 
               reverse_conditioning=condition_on_subsequents,
               seqs=sequences)
            #log = pprintfreqdists(odat, f)
            # iterate over seq lengths (keys of odat)
            for ws in odat:
                if ws not in all_dat.keys():
                    all_dat[ws] = odat[ws]
                else:
                    # TODO: update this when sequences is fully
                    # decoupled from conditional sequences
                    if ws == 1:
                        fdupdate(odat[ws], all_dat[ws])
                    else:
                        cfupdate(odat[ws], all_dat[ws])
        jsout = kwargs['tojson']
        log = pprintfreqdists(all_dat, "ALL FILES")
        if jsout is not None:
            if not jsout.endswith(".json"):
                jsout += ".json"
            with open(jsout, "w") as jfile:
                # CONVERT TUPLE KEYS TO STRING
                print(all_dat)
                jstring = json.dumps(cfkeystostring(all_dat))
                jfile.write(jstring)
            print("frequency data written to {}".format(jsout))
             



                                

    # and here. we. go.
    seqs = args.sequences
    kwmap = {k[0]:k[1] for k in args._get_kwargs()}
    #print(kwmap.keys())
    main(**kwmap)




