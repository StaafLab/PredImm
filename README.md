# PredImm

## About

 **Pred**ict **I**mmune I**mm**ediatly

 

 ## Installation

To use PredImm you will first need to install conda, see https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

To run the code in this repository, the easiest is to clone it and then install the requirements

```
git clone https://github.com/StaafLab/PredImm
cd PredImm
conda env create -f environment/predimm.yml
```

## Using the predictor

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
the -i flag is used to give the (relative) path to the input file

## Specifying output files

If you run the notebook, you can specify your own output file within the notebook. 
When using the 




PredImm has been developed on Rocky Linux 8.8 and is not tested on other operating systems.
