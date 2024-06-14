**splice modifer score (SMS)** readme

SMS is a model that takes genetic variant as input and outputs the predicted probability a variant impacts splicing. This implementation is trained on fine-mapped GTEx sQTL data.

The model is a logistic regression, and every GTEx variant is currently annotated with known molecular features that provide prediction value for the splicing prediction task. 

SMS can be applied in the following ways:
- GTEx SMS scores can be intersected with your GWAS variants of interest, providing interpretable feedback as to how variant impacts splicing (scores available here) 
- SMS can be applied on a new set of variants, provided they are annotated with all features (ie, all gnomAD variants)
    - However, scoring genetic variants with unpaired transcriptomic data has not been implemented or tested and is not fully recommended at this time
- SMS could also be retrained using other s-QTL data besides GTEx (though this functionality is not fully implemented)

Any questions on implementation can be addressed to hnjacobs@mit.edu


