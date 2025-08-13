import pandas as pd
import numpy as np
import codepub as cdp
from itertools import combinations
import math

import tqdm
import time
import signal

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()

## parameters
n_down = 10
n_up = 15
iters_down = 2
iters_up = 13
time_max = 400

rca_new_time = dict()
rca_new_results = dict()
for n_pools in range(n_down, n_up):
    el_time = dict()
    el_result = dict()
    for iters in range(iters_down, iters_up):
        el_time[iters] = []
        el_result[iters] = []
        available = np.min([math.comb(n_pools, iters), math.comb(n_pools, iters+1)])
        for len_lst in tqdm.tqdm(range(60, 100), leave=False):
            l = available*len_lst//100
            if l > 3:
                start = time.time()
                signal.signal(signal.SIGALRM, timeout_handler)
                signal.alarm(time_max)
                try:
                    b, S = cdp.rcbba(n_pools, iters, l)
                except TimeoutException:
                    S = []
                finally:
                    signal.alarm(0)
                end = time.time()
                if S is not None:
                    el_result[iters].append(len(S))
                else:
                    el_result[iters].append(0)
                el_time[iters].append(end-start)
    rca_new_time[n_pools] = el_time
    rca_new_results[n_pools] = el_result
    print(n_pools)

rca_results = pd.DataFrame(columns = ['m', 'r', 'n', 'real_n', 'max_n', 'Time (s)'])
for keyb in list(rca_new_time.keys()):

    results19 = pd.DataFrame(columns = ['m', 'r', 'n', 'real_n', 'max_n', 'Time (s)'])
    for key in list(rca_new_time[keyb].keys()):
        results19_inter = pd.DataFrame()
        times = rca_new_time[keyb][key]
        peptides = []
        real_peptides = rca_new_results[keyb][key]
        maxi = []
        available = np.min([math.comb(keyb, key), math.comb(keyb, key+1)])
        for len_lst in range(60, 100):
            l = available*len_lst//100
            if l > 3:
                peptides.append(l)
                maxi.append(available)
        results19_inter['n'] = peptides
        results19_inter['real_n'] = real_peptides
        results19_inter['max_n'] = maxi
        results19_inter['Time (s)'] = times
        results19_inter['m'] = [keyb]*len(times)
        results19_inter['r'] = [key]*len(times)
        if results19.empty:
            results19 = results19_inter
        else:
            results19 = pd.concat([results19, results19_inter])
    if rca_results.empty:
        rca_results = results19
    else:
        rca_results = pd.concat([rca_results, results19])

rca_results.to_csv('results/rcbba_lim_failures.tsv', sep = "\t", index = None)