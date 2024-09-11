# splice modifer score (SMS) 

SMS is a model that takes genetic variant as input and outputs the predicted probability a variant impacts splicing. This implementation is trained on fine-mapped GTEx sQTL data.

The model is a logistic regression, and every GTEx variant is currently annotated with known molecular features that provide prediction value for the splicing prediction task.

Currently, SMS can be applied in the following ways:

GTEx SMS scores can be intersected with your GWAS variants of interest, providing interpretable feedback as to how variant impacts splicing (scores available here)
SMS full model and submodels can be retrained and tested in this code



## Step-by-Step Instructions
### 0. clone the github

### 1. import the environment using yaml file
```
conda env create SMS_environment.yaml 
```
then activate the environment
```
conda activate SMS_environment
```

### 2. Fetch sQTL variants data
```
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1QGM2GBtwzVA07bO_udLj5r3E8oSlMizf' -O sQTLs_for_model_fit.csv.gz
```


### 3. Run this notebook


```
jupyter notebook Run_GLM_for_github.ipynb

```

Any questions on implementation can be addressed to hnjacobs@mit.edu
