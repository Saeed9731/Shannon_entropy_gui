# Shannon entropy for pi digits
import timeit
import numpy as np

def pi_entropy000620(tex, word_length):
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
   # print(pii)
   pii = list(filter(None, pii)) # pii = list(filter(len, pii))
   n = len(pii)
   # Shannon entropy for pi digits by probability of term frequency 
   import collections
   vf = collections.Counter(pii) # extract vocabulary & frequencies
   p = [ x/n for x in list(vf.values()) ] # probability of terms
   e1 = -sum( p*np.log(p) ) # entropy by probability of term 
   data = [["w", "e2"]]
   with open('pi-entropy(gui2_2_2).txt', 'w') as fout:
            for w in vf:
               d = np.diff( list( np.where(np.array(pii) == w)[0] ) )
               p = [ x/n for x in d ] # probability of term
               e2 = -sum( p*np.log(p) ) # entropy by probability of term distance
               w_e2 = [w, "%f" % e2]
               data.append(w_e2)
               fout.write( "%s \t %f \n" % (w, e2) )
   tf = timeit.default_timer()
   return data, e1, tf-ti