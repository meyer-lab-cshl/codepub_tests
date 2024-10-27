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
n_down = 5
n_up = 15
iters_down = 3
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
        available = math.comb(n_pools, iters)
        for len_lst in tqdm.tqdm(range(60, 100), leave=False):
            l = available*len_lst//100
            if available > l and l > 0:
                start = time.time()
                signal.signal(signal.SIGALRM, timeout_handler)
                signal.alarm(time_max)
                try:
                    b, S = cdp.rcau(n_pools, iters, l)
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


rca_results = pd.DataFrame(columns = ['N_pools', 'Iters', '# of peptides', 'Max', 'Time (s)'])
for keyb in list(rca_new_time.keys()):

    results19 = pd.DataFrame(columns = ['N_pools', 'Iters', '# of peptides', 'Max', 'Time (s)'])
    for key in list(rca_new_time[keyb].keys()):
        results19_inter = pd.DataFrame()
        times = rca_new_time[keyb][key]
        peptides = []
        max = []
        available = math.comb(keyb, key)
        for len_lst in range(60, 100):
            l = available*len_lst//100
            if available > l and l>0:
                peptides.append(l)
                max.append(available)
        results19_inter['# of peptides'] = peptides
        results19_inter['Max'] = max
        results19_inter['Time (s)'] = times
        results19_inter['N_pools'] = [keyb]*len(times)
        results19_inter['Iters'] = [key]*len(times)
        results19 = pd.concat([results19, results19_inter])
    rca_results = pd.concat([rca_results, results19])

rca_results.to_csv('RCAU_lim_failures.tsv', sep = "\t", index = None)