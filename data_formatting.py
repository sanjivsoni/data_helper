import pickle
import matplotlib.pyplot as plt
import math
import pandas as pd
import numpy as np

# Load Decoding Map
def load_obj(name ):
    '''
    It loads a python dictionary from saved .pkl file
    :param name: name of file
    :return: returns dict
    '''
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


# plots histogram from data
def plot_hist(df, bins, title, xlabel, ylabel, lower_limit, upper_limit):
    '''
    Takes data and labels and returns histogram
    :param df: series of numerical data
    :param bins: histogram bins (int)
    :param title: histogram title (string)
    :param xlabel: x axis label (string)
    :param ylabel: y axis label (string)
    :return: histogram plot
    '''
    df[(df > lower_limit) & (df < upper_limit)].hist(bins = bins)
    std = df.std().round(3)
    mean = df.mean().round(3)
    title = title + ' mean(' + str(std) + ') std(' + str(mean) + ')'
    max_ = df.max().round(3)
    min_ = df.min().round(3)
    xlabel = xlabel + ' max(' + str(max_) + ') min(' + str(min_) + ')'
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

# This method plots distribution of features of a dataframe
def plot_df_features(df, spec_plot, spec_xlabel, suptitle):
    '''
    It plots distribution of features in a single plot
    The title of each subplot has mean and std of data
    X labels are used from spec_xlabel
    suptitle : Super Title of the figure
    df: Dataframe of columns as features
    '''
    num_plots = len(spec_plot)

    fig = plt.figure(figsize = (15, 3 * num_plots))
    fig.subplots_adjust(hspace = 0.5, wspace = 0.4)
    fig.suptitle(suptitle, fontsize = 16)
    for i in range(0, num_plots):
        row = math.ceil(num_plots / 2.0)
        col = 2
        current = i + 1
        ax = fig.add_subplot(row, col, current)

        col = spec_plot[i]
        xlabel = spec_xlabel[col]

        df[col].hist(bins = 100)
        plt.xlabel(xlabel)

        std = str(df[col].std().round(3))
        mean = str(df[col].mean().round(3))
        title = col.replace('_', ' ').upper() + " mean = " + mean + ", STD = " + std
        plt.title(title)


def get_mean_std(series):
    '''
    Method of create_stats_table()
    :param series: Pandas Series
    :return: mean and std of series
    '''
    return series.mean(), series.std()


def format_value(value_a, value_b, kind):
    '''
    Method of create_stats_table()
    Formats value of each cell of stats table
    :param value_a: Mean or Count Value (int or float)
    :param value_b: Std or Percentage (float)
    :param kind: 'count' or 'mean'
    :return: Formatted Values as sting
    '''
    ret_str = ""
    if kind == "count":
        ret_str = str(round(value_a, 2)) + ' (' + str(round(value_b, 2)) + '%)'
    elif kind == "mean":
        ret_str = str(round(value_a, 2)) + ' (' + str(round(value_b, 2)) + ')'
    return ret_str

def format_table(df, value_heading):
    '''
    Creates a dataframe of bin and value
    value can be mean, std, count or any other value.
    :param df: Pandas Dataframe
    :param value_heading: Column Heading
    :return: Returns a dataframe with renamed column
    '''
    tab = pd.DataFrame(df).reset_index()
    tab.columns = ['Decile Bin', value_heading]
    return tab


def create_decile_plot(df, title, n_bins):
    '''
    Creates a decile plot by mean with std shown as the error bars
    :param df: Pandas Dataframe
    :param title: Title of Plot
    :return: Plots a figure in notebook
    '''
    df['decile_bin'] = pd.qcut(df['risk_score'].rank(method = 'first'), n_bins)
    x = range(1, n_bins + 1)
    y = df.groupby('decile_bin')['risk_score'].mean().values.round(4)
    e = df.groupby('decile_bin')['risk_score'].std().values.round(4)

    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.errorbar(x, y, color = 'red', yerr = e, alpha = 0.5,
                barsabove = True, ecolor = 'red', capsize = 10, fmt = 'o')
    ax.set_xticks(np.arange(1, n_bins + 1))
    ax.set_title(title)
    ax.grid(alpha = 0.5, linestyle=':')
    ax.yaxis.grid(True)
    plt.show()
