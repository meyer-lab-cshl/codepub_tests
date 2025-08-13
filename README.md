# Unbiased and Error-Detecting Combinatorial Pooling Experiments with Balanced Constant-Weight Gray Codes for Consecutive Positives Detection

Supplementary repository to the paper: [arXive version](https://arxiv.org/abs/2502.08214).

Combinatorial pooling schemes have enabled the measurement of thousands of experiments in a small number of reactions. This efficiency is achieved by distributing the items to be measured across multiple reaction units called pools. However, current methods for the design of pooling schemes do not adequately address the need for balanced item distribution across pools, a property particularly important for biological applications. Here, we introduce balanced constant-weight Gray codes for detecting consecutive positives (DCP-CWGCs) for the efficient construction of combinatorial pooling schemes. Balanced DCP-CWGCs ensure uniform item distribution across pools, allow for the identification of consecutive positive items such as overlapping biological sequences, and enable error detection by keeping the number of tests on individual and consecutive positive items constant. For the efficient construction of balanced DCP-CWGCs, we have released an open-source python package codePub, with implementations of the two core algorithms: a branch-and-bound algorithm (BBA) and a recursive combination with BBA (rcBBA). Simulations using codePub show that our algorithms can construct long, balanced DCP-CWGCs that allow for error detection in tractable runtime.

### Figures

codepub_figures jupyter notebook contains the code to reproduce the figures. Some of the data shown on figures was obtained by separate scripts (.py file). Then this data is in "results" folder.

Scripts use codepub python package (version 2.3). It can be installed with pip:

```python
pip install codepub
```

or with conda:

```python
conda install -c vasilisa.kovaleva codepub
```

[documentation](https://codepub.readthedocs.io/en/latest/Introduction.html).

### Authors

Guanchen He<sup>*</sup>, Vasilisa A. Kovaleva<sup>*</sup>, Carl Barton, Paul G. Thomas, Mikhail V. Pogorelyy, Hannah V. Meyer<sup>#</sup>, and Qin Huang<sup>#</sup>

These authors contributed equally: *.
This work was supported by the National Natural Science Foundation of China under Grant 62071026 and 62331002. This work was also supported by the Simons Center for Quantitative Biology at Cold Spring Harbor Laboratory; US National Institutes of Health Grant S10OD028632-01. The funders had no role in the template design or decision to publish. (Corresponding authors #: Qin Huang, Hannah V. Meyer)
Guanchen He and Qin Huang are with the School of Electronic and Information Engineering, Beihang University, Beijing 100191, China.
Vasilisa A. Kovaleva and Hannah V. Meyer are with the Simons Center for Quantitative Biology, Cold Spring Harbor Laboratory, NY 11724, USA.
Carl Barton is with Birkbeck University of London, Malet Street, London, WC1E 7HX.
Mikhail V. Pogorelyy and Paul G. Thomas are with the Department of Host-Microbe Interaction, St. Jude Children’s Research Hospital, Memphis, TN 38105, USA.