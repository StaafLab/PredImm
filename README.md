# PredImm

## About

 Predict 
 **Imm**une **Imm**ediatly

 ## Installation

To use PredImm you will first need to install conda, see https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

To run the code in this repository, the easiest is to clone it and then install the requirements

```
git clone https://github.com/StaafLab/PredImm
cd PredImm
conda env create -f environment/predimm.yml
```

## Getting started

PredImm comes with TCGA TNBC samples as an exmaple data set. To run this example, activate the conda environment and run the notebook or the script.

To run the notebook
```
conda activate predimm
jupyter notebook
```
and open im_pred.ipynb

or start your code interpretered and choose predimm as kernel. 

To run the script

```
conda activate predimm
./im_pred.py -i data/tcga_fpkm.csv
```

