# AUTOGENERATED! DO NOT EDIT! File to edit: 00_plots.ipynb (unless otherwise specified).

__all__ = ['get_cmap', 'PrC_curve', 'plot_ROC_based_on_annotation', 'plot_percent_annot_aganist_pip_bins', 'ecdf',
           'upset_plot', 'example']

# Cell
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns

# Cell
def get_cmap(n, name='Set3'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)


# Cell
def PrC_curve(df, list_of_annotations):

    sns.set_style("white")
    figure(figsize=(8, 6), dpi=80)
#use annotation and probablities
    cmap=get_cmap(len(list_of_annotations)+1)

    from sklearn.metrics import precision_recall_curve
    for i, given_annotation in enumerate(list_of_annotations):

        y_true = list(df[given_annotation])
        y_scores = list(df.pip>0.95)
        precision, recall, thresholds = precision_recall_curve(y_true, y_scores)
        print(precision)
        print(recall)

        plt.plot(recall, precision,  c=cmap(i), label = given_annotation)

    plt.title('PrC curve for annotations in sQTLs in skipped exons')
    plt.legend(loc = 'lower right')

    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('Percision')
    plt.xlabel('Recall')
    plt.show()
#this function plots the percent of each categorical annotation aganist a given set of PIP bins in a given df.

def plot_ROC_based_on_annotation(df, list_of_annotations):

    sns.set_style("white")
    figure(figsize=(8, 6), dpi=80)
#use annotation and probablities
    cmap=get_cmap(len(list_of_annotations)+1)

    for i, given_annotation in enumerate(list_of_annotations):

        y_true = list(df[given_annotation] )
# predicted probabilities generated by sklearn classifier
        y_probas = list(df.pip )
        fpr, tpr, threshold = metrics.roc_curve(y_true, y_probas)
#calc ROC
        roc_auc = metrics.auc(fpr, tpr)

# method I: plt

        plt.plot(fpr, tpr,  c=cmap(i), label = 'AUC = %0.2f' % roc_auc + ' ' + given_annotation)

    plt.title('ROC curve for annotations in sQTLs in skipped exons')
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()



# Cell
def plot_percent_annot_aganist_pip_bins(df, pip_bin_type, annotation):
# top bar -> sum all values(smoker=No and smoker=Yes) to find y position of the bars
    plt.figure(figsize=(7, 7))

    sns.set(font_scale=3)

# set plot style: grey grid in the background:
    sns.set(style="darkgrid")

    sum_df=df.groupby(pip_bin_type)[annotation].sum()
    size_df=df.groupby(pip_bin_type)[annotation].size()


    fraction_of_annot= sum_df.to_frame()/size_df.to_frame()*100

    sns.barplot(data=fraction_of_annot, x=fraction_of_annot.index, y=annotation, palette='Blues')


    plt.ylabel('% of variants in ' + annotation)



# Cell
def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y


# Cell
from upsetplot import generate_counts

example = generate_counts()

def upset_plot(df, annots, pip_cutoff):
    import upsetplot
    from upsetplot import plot
    from matplotlib import pyplot

    df=df[df.pip>pip_cutoff]

    ax=plt.figure(figsize=(7, 7))



    subset=df.groupby(annots).size()


    ax=plot(subset)

    pyplot.show()