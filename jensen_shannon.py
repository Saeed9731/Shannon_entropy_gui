# Jensen-Shannon divergence for pi digits
import timeit
import numpy as np

def jensen_shanon_DV(tex, word_length):
    ti = timeit.default_timer()
    f = open(tex, "r")
    pii = f.read()
    f.close()
    # remove whitespaces and newlines, convert string list to integer list
    pii = list(map(str,"".join(pii.split())))
    nt = len(pii)
    wl = word_length # word length
    for i in range(nt):
        pii[i : i+wl] = [''.join(pii[i : i+wl])]
    pii = list(filter(None, pii)) # pii = list(filter(len, pii))
    n = len(pii)
    import random
    spii = random.sample(pii, n)
    import collections
    vf = collections.Counter(pii) # extract vocabulary & frequencies
    data = [["w", "jsd"]]
    with open('pi-js(gui2_2_2).txt', 'w') as fout:
        for w in vf:
            d = np.diff( np.array( np.where(np.array(pii) == w)[0] ) )
            p = d/n # probability of term in original set
            sd = np.diff( np.array( np.where(np.array(spii) == w)[0] ) )
            q = sd/n # probability of term in shuffled set
            m = (p+q)/2
            kld_pm = sum( p*np.log(p/m) )
            kld_qm = sum( q*np.log(q/m) )
            jsd = (kld_pm+kld_qm)/2 # jsd
            w_jsd = [w, "%f" %jsd]
            data.append(w_jsd)
            fout.write( "%s \t %f \n" % (w, jsd) )
    tf = timeit.default_timer()
    return data, tf-ti