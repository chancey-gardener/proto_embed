#!/usr/bin/python3

#############DIMENSIONALITY REDUCTION FUNCTIONS:

def scratchTSNE(dist):
    exper = lambda vec: np.e** ((0-np.linalg.norm(xiv-vec)**2)/tsig)
    outmat = []
    for k in dist:
        dvec = dist[k]
        diffscore = exper(dvec)
        denexp += diffscore
           # print(diffscore)
        count += 1
        prop = round((count/span)*100, 2)
        if prop%1 == 0:
            print('{}% complete'.format(prop))
            print('{}/{}'.format(numexp,denexp))

def pj_given_i(xiv, xjv, dist, sig_squared_i=1/np.sqrt(2)):
        '''where xi and xj are word keys pointing to vector values in dist.
            NOTE: sig_squred_i is set to constant for now, fix when
            a better strategy can be decided on'''
        tsig = sig_squared_i * 2
            ####################
            # NOTE: Ok, so the main
            # problem here is that 
            # tsig (the variance of 
            # the p value being conditioned
            # on (pretty much any vector
            # from this set)) is turning
            # out to be so close to 0
            # that dividing by it produces
            # a massive number, taking 
            # its negative and exp-ing it
            # produces a value too close to 0
            # for python to handle (is there a double type?
            ##############################################
            # get numerator of expression for p(j|i)
        
        numexp = exper(xjv)
        print("numexp: {}".format(numexp))
        print("tsig: {}".format(tsig))
        # well now? we're gonna compute a motherfuckin denominator
        denexp = 0
     # TODO: the values computed in this for loop have got to be stored
    #   warp = pool(4)
    #   noti = (dist[k] for k in dist if dist[k] != xi)
        print('Computing covariance matrix...')
        #denexp = sum(warp.map(exper, noti))
        denexp = 0
        count = 0 # just to show us how
        span = len(dist)
        
        pji = numexp/denexp
        return pji


dimred = {
    
        'TSNE': TSNE
}

