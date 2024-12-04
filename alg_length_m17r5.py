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

m = 17
r = 5

bba_check = dict()
bba_check_n = dict()

available = math.comb(m, r)
for perc in tqdm.tqdm(range(40, 100), leave=False):
    n = available*perc//100
    if available > n and n > 0:
        start = time.time()
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(400)
        try:
            b, S = cdp.bba(m, r, n)
        except TimeoutException:
            S = []
        finally:
            signal.alarm(0)
        end = time.time()
        if S is not None:
            bba_check_n[n] = len(S)
        else:
            bba_check_n[n] = 0
        bba_check[n] = end-start

bba_check = pd.DataFrame.from_dict(bba_check, orient = 'index', columns = ['time (s)'])
bba_check_n = pd.DataFrame.from_dict(bba_check_n, orient = 'index', columns = ['real length'])

bba_result = bba_check.merge(bba_check_n, left_index = True, right_index = True)
bba_result.index.names = ['n']
bba_result.to_csv('results/BBA_length_m17r5.tsv', sep = "\t", index = None)

rcbba_check = dict()
rcbba_check_n = dict()

available = math.comb(m, r)
for perc in tqdm.tqdm(range(40, 100), leave=False):
    n = available*perc//100
    if available > n and n > 0:
        start = time.time()
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(400)
        try:
            b, S = cdp.rcbba(m, r, n)
        except TimeoutException:
            S = []
        finally:
            signal.alarm(0)
        end = time.time()
        if S is not None:
            rcbba_check_n[n] = len(S)
        else:
            rcbba_check_n[n] = 0
        rcbba_check[n] = end-start

rcbba_check = pd.DataFrame.from_dict(rcbba_check, orient = 'index', columns = ['time (s)'])
rcbba_check_n = pd.DataFrame.from_dict(rcbba_check_n, orient = 'index', columns = ['real length'])

rcbba_result = rcbba_check.merge(rcbba_check_n, left_index = True, right_index = True)
rcbba_result.index.names = ['n']
rcbba_result.to_csv('results/rcBBA_length_m17r5.tsv', sep = "\t", index = None)