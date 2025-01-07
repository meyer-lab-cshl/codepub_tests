import pandas as pd
import numpy as np
import codepub as cdp
import tqdm
import time

## RCA+BBA running time

### parameters
length_down = 50
length_up = 3000
step = 100

## fixed iters
iters = 4
n_down = 20
n_up = 25

rca_results_time_fixI4 = pd.DataFrame(columns = ['m', 'n', 'Time (s)'])

for n in range(n_down, n_up):
    results_time = dict()
    for i in tqdm.tqdm(range(length_down, length_up, step)):
        start_time = time.time()
        b, lines = cdp.rcbba(m=n, r=iters, n=i)
        end_time = time.time()
        elapsed_time = end_time - start_time
        results_time[i] = elapsed_time
    results_time = pd.DataFrame.from_dict(results_time, orient = 'index')
    results_time = results_time.reset_index()
    results_time.columns = ['n', 'Time (s)']
    results_time['m'] = n
    rca_results_time_fixI4  = pd.concat([rca_results_time_fixI4, results_time])

rca_results_time_fixI4.to_csv('rca_running_time_fixI4.tsv',
                               sep = "\t", index = None)

### fixed n_pools

iters_down = 4
iters_up = 7
n_pools = 20

rca_results_time_fixN20 = pd.DataFrame(columns = ['r', 'n', 'Time (s)'])

for iters in range(iters_down, iters_up):
    results_time = dict()
    for i in tqdm.tqdm(range(length_down, length_up, step)):
        start_time = time.time()
        b, lines = cdp.rcbba(m=n_pools, r=iters, n=i)
        end_time = time.time()
        elapsed_time = end_time - start_time
        results_time[i] = elapsed_time
    results_time = pd.DataFrame.from_dict(results_time, orient = 'index')
    results_time = results_time.reset_index()
    results_time.columns = ['n', 'Time (s)']
    results_time['r'] = iters
    rca_results_time_fixN20  = pd.concat([rca_results_time_fixN20, results_time])

rca_results_time_fixN20.to_csv('rca_running_time_fixN20.tsv',
                               sep = "\t", index = None)