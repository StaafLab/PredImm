#!/usr/bin/env python

"""
Title: im_pred.py
Author: S.J. Roostee
Description:
	This script outputs IM predictions based on input fpkm data.
TODO:
    - check that genes are not entrez IDs
    - check if data need transposing
"""

import sys
import os
import argparse

import joblib
import pandas as pd
import numpy as np

import argparse

#########################   argparse    ##################################

usage = "This script outputs IM predictions based on input fpkm data."

parser = argparse.ArgumentParser(description=usage)

parser.add_argument(
	"-v", "--version",
	action = "version",
	version = "%(prog)s 1.0"
	)

parser.add_argument(
	"-i",
	dest = "input",
	metavar = "INPUT",
	required = True,
	help = "input file with fpkm data, expected format is samples as column names and gene names as rows."
	)

parser.add_argument(
	"-o",
	dest = "output",
	metavar = "OUTPUT",
	default = "results/impred.txt", 
	help = "predictions"
	)

args = parser.parse_args()

fpkm_file = args.input

pred_file = args.output

fpkm = pd.read_csv(fpkm_file, sep = ',', header = 0, index_col = 0)

fpkm = np.transpose(fpkm)

genes = pd.read_csv("results/genes_ordered.csv")
gene_list = genes['gene'].tolist()

##here we make sure the columns are in the right order
fpkm = fpkm[fpkm.columns.intersection(gene_list)]

genes.set_index("gene", inplace = True)
fpkm = fpkm[genes.index]

# ##########################    predictions     ##############################

rf_loaded = joblib.load("model/rf_fpkm_intersectionmodel.joblib")

fpkm_pred = rf_loaded.predict(fpkm)
fpkm_proba = rf_loaded.predict_proba(fpkm)
fpkm["IMpred"] = fpkm_pred
fpkm["proba_0"] = fpkm_proba[:, [0]]
fpkm["proba_1"] = fpkm_proba[:, [1]]

pred = fpkm[["IMpred", "proba_0", "proba_1"]]

# #########################   save output     #############################

pred.to_csv(pred_file)
