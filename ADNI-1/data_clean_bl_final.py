
# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# %matplotlib inline

from pprint import pprint
from itertools import product
from collections import OrderedDict
from itertools import product

from __future__ import print_function # For Python 2 / 3 compatability
import json
from copy import copy

import warnings
from sklearn import preprocessing
# %autosave 300
warnings.filterwarnings("ignore")

# load ADNIMERGE.csv, the main dataset (we will add our own variables to it).
ADNI_merge = pd.read_csv('ADNIMERGE2.csv')

''' ADNI1 data within ADNIMERGE.csv '''
# select only the rows that correspond to ADN2
ADNI1 = ADNI_merge[ADNI_merge['COLPROT']=='ADNI1']
print(ADNI1.shape)

import numpy as np
ADNI1 = ADNI1.replace('Unknown', np.nan)
ADNI1 = ADNI1.replace(-1, np.nan)
ADNI1 = ADNI1.replace(-4, np.nan)

ADNI1_bl = ADNI1.copy()
ADNI1_bl = ADNI1_bl[ADNI1_bl['VISCODE'] == 'bl']

ADNI1_bl.columns

list(ADNI1_bl.columns.values.tolist())

ADNI1_bl.shape

ADNI1_bl= ADNI1_bl.drop(labels = [ 'SITE', 'ORIGPROT', 'EXAMDATE',
         'AV45', 'ABETA', 'TAU', 'PTAU', 'CDRSB', 'ADAS11', 'ADAS13', 'ADASQ4', 'PIB',
       'MMSE', 'RAVLT_immediate', 'RAVLT_learning', 'RAVLT_forgetting',
       'RAVLT_perc_forgetting', 'LDELTOTAL', 'DIGITSCOR', 'TRABSCOR', 'FAQ', 'MOCA', 'EcogPtMem', 'EcogPtLang',
       'EcogPtVisspat', 'EcogPtPlan', 'EcogPtOrgan', 'EcogPtDivatt',
       'EcogPtTotal', 'EcogSPMem', 'EcogSPLang', 'EcogSPVisspat', 'EcogSPPlan',
       'EcogSPOrgan', 'EcogSPDivatt', 'EcogSPTotal', 'FLDSTRENG', 'FSVERSION', 'IMAGEUID',
       'Ventricles', 'Hippocampus', 'WholeBrain', 'Entorhinal', 'Fusiform',
       'MidTemp', 'ICV', 'DX',  'mPACCdigit',
 'mPACCtrailsB', 'EXAMDATE_bl',   'Years_bl', 'Month_bl', 'Month', 'M',
       'update_stamp', 'FSVERSION_bl', 'FLDSTRENG_bl'],axis=1)

ADNI1_bl.columns

print((ADNI1_bl.isnull().sum()/len(ADNI1_bl['DX_bl'])).sort_values(ascending=False))

#Drop 50% or more missing
ADNI1_bl= ADNI1_bl.drop(['AV45_bl', 'EcogSPLang_bl', 'MOCA_bl', 'EcogPtMem_bl', 'EcogSPLang_bl', 'EcogSPVisspat_bl',
                        'EcogSPPlan_bl', 'EcogPtOrgan_bl', 'EcogSPDivatt_bl', 'EcogPtTotal_bl', 'EcogPtMem_bl',
                        'EcogSPVisspat_bl', 'EcogSPPlan_bl', 'EcogPtOrgan_bl', 'EcogSPDivatt_bl', 'EcogPtTotal_bl',
                        'PIB_bl', 'ABETA_bl', 'TAU_bl', 'PTAU_bl' , 'EcogPtOrgan_bl', 'EcogPtMem_bl',
                        'EcogSPDivatt_bl', 'EcogSPPlan_bl', 'EcogSPVisspat_bl', 'EcogSPLang_bl', 'EcogPtTotal_bl',
                        'FDG_bl', 'FDG'], axis=1)

print((ADNI1_bl.isnull().sum()/len(ADNI1_bl['DX_bl'])).sort_values(ascending=False))

ADNI1_bl= ADNI1_bl.drop(['EcogSPOrgan_bl', 'EcogSPTotal_bl', 'EcogPtLang_bl',
                        'EcogPtVisspat_bl', 'EcogPtPlan_bl', 'EcogPtDivatt_bl', 'EcogSPMem_bl'], axis=1)

encode = preprocessing.LabelEncoder()
ADNI1_bl.loc[:, 'DX_bl'] = encode.fit_transform(ADNI1_bl['DX_bl'])

ADNI1_bl.head()

ADNI1_bl.shape

list(ADNI1_bl.columns.values.tolist())

categorical_predictors = ['PTRACCAT', 'PTMARRY','APOE4', 'PTGENDER']

''' Remove all categorical data with nan (only ~0.5-1%) '''
categorical_predictors_drop = ['PTETHCAT']

'''' Hot-One Encoding of Categorical Predictors '''
ADNI1_bl_categorical_nodrop = pd.get_dummies(ADNI1_bl[categorical_predictors] , columns=categorical_predictors, prefix = categorical_predictors , drop_first=False)
ADNI1_bl_categorical_drop = pd.get_dummies(ADNI1_bl[categorical_predictors_drop] , columns=categorical_predictors_drop, prefix = categorical_predictors_drop , drop_first=False)
ADNI1_bl= pd.get_dummies(ADNI1_bl, columns=categorical_predictors, prefix = categorical_predictors , drop_first=False)
ADNI1_bl= pd.get_dummies(ADNI1_bl, columns=categorical_predictors_drop, prefix = categorical_predictors_drop , drop_first=True)
print(ADNI1_bl.shape)

ADNI1_bl.shape

ADNI1_bl.isnull().sum()

ADNI1_bl_remove = ADNI1_bl.copy()
print('Shape before deleting missing', ADNI1_bl_remove.shape)
ADNI1_bl_remove.dropna(axis=0, inplace=True)
print('Shape after deleting missing', ADNI1_bl_remove.shape)
print('Data contains NaN?', ADNI1_bl_remove.isnull().any().any())

ADNI1_bl_remove.isnull().sum()

ADNI1_bl_remove.head()

ADNI1_bl_remove.shape

ADNI1_bl_remove.columns

ADNI1_bl_remove.to_csv(path_or_buf='ADNI1_bl_remove_all_missing.csv', index=False)