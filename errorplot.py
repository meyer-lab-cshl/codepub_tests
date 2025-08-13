import codepub as cdp
import copepodTCR as cpp
import pandas as pd
import numpy as np

import seaborn as sn
from matplotlib import pyplot as plt

import tqdm

pep_length = 15
shift = 3
n_pools = 18
iters = 6

shift_errors = pd.DataFrame(columns = ['Peptide', 'Address', 'Epitope', 'Act Pools',
                                        '# of pools', '# of epitopes', '# of peptides', 'Remained', '# of lost',
                                           'Right peptide', 'Right epitope', 'Shift', 'Len'])
shift_errors.to_csv('results/error_plot_M18_R6.tsv', sep = "\t", index = None)

length = shift*1000+500
lst_all = []
sequence = cpp.random_amino_acid_sequence(length)
for i in range(0, len(sequence), shift):
    ps = sequence[i:i+pep_length]
    if len(ps) == pep_length:
        lst_all.append(ps)
            
for x in [15, 12, 9, 6, 3]:
    for i in tqdm.tqdm([100, 500, 1000], leave = True):
        lst = lst_all[:i]
        b, lines = cdp.rcbba(m=n_pools, r=iters, n=i)
        pools, peptide_address = cpp.pooling(lst=lst, addresses=lines, n_pools=n_pools)
        check_results = cpp.run_experiment(lst=lst, peptide_address=peptide_address, ep_length=x,
                              pools=pools, iters=iters, n_pools=n_pools, regime='with dropouts')
        check_results['Len'] = i
        check_results['Shift'] = x
        shift_errors = pd.read_csv('results/error_plot_M18_R6.tsv', sep = "\t")
        if shift_errors.empty:
        	shift_errors = check_results
        else:
			shift_errors = pd.concat([shift_errors, check_results])
        shift_errors.to_csv('results/error_plot_M18_R6.tsv', sep = "\t", index = None)

    print(x)