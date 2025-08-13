# Unbiased and Error-Detecting Combinatorial Pooling Experiments with Balanced Constant-Weight Gray Codes for Consecutive Positives Detection

Supplementary repository to the paper: [arXive version](https://arxiv.org/abs/2502.08214).

Combinatorial pooling schemes have enabled the measurement of thousands of experiments in a small number of reactions. This efficiency is achieved by distributing the items to be measured across multiple reaction units called pools. However, current methods for the design of pooling schemes do not adequately address the need for balanced item distribution across pools, a property particularly important for biological applications. Here, we introduce balanced constant-weight Gray codes for detecting consecutive positives (DCP-CWGCs) for the efficient construction of combinatorial pooling schemes. Balanced DCP-CWGCs ensure uniform item distribution across pools, allow for the identification of consecutive positive items such as overlapping biological sequences, and enable error detection by keeping the number of tests on individual and consecutive positive items constant. For the efficient construction of balanced DCP-CWGCs, we have released an open-source python package codePub, with implementations of the two core algorithms: a branch-and-bound algorithm (BBA) and a recursive combination with BBA (rcBBA). Simulations using codePub show that our algorithms can construct long, balanced DCP-CWGCs that allow for error detection in tractable runtime.

### Figures

codepub_figures.ipynb contains the code for all figures in the manuscript. Some of the data shown on figures was obtained by separate scripts (.py files). Then this data is in "results" folder.

All scripts use codepub python package (version 2.3). It can be installed with pip:

```python
pip install codepub
```

or with conda:

```python
conda install -c vasilisa.kovaleva codepub
```

Codepub documentation: [readthedocs](https://codepub.readthedocs.io/en/latest/Introduction.html).


### Authors

Guanchen He, Vasilisa A. Kovaleva, Carl Barton, Paul G. Thomas, Mikhail V. Pogorelyy, Hannah V. Meyer, and Qin Huang