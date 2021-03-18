import numpy as np 
import pandas as pd 
import seaborn as sn 
import matplotlib.pyplot as plt

class Analysis:
    """[summary]
    """
    def __init__(self,output_dir):
        """[summary]

        Args:
            output_dir ([string]): set the output dir for the analysis
        """
        self.threshold = 1e-5
        self.output_dir = output_dir

    def remove_low_variance(self, df):
        """removes all columns with low variance

        Args:
            df ([pd.Dataframe]): the Dataframe that is to be analyzed
        """
        df = df.drop(df.columns[df.var() <= self.threshold], axis=1)

    def plot_and_save(self, df, x_axis, y_axis, title, xlabel="", ylabel="", nr_of_subplots=1):
        """plots and saves the given data

        Args:
            df ([pd.Dataframe]): the Dataframe that is to be analyzed
            x_axis ([string]): [the column name for the x-axis]
            y_axis ([string/list]): [the column name(s) for the y-axis]
            title ([type]): [description]
            xlabel (str, optional): [description]. Defaults to "".
            ylabel (str, optional): [description]. Defaults to "".
            nr_of_subplots (int, optional): [description]. Defaults to 1.
        """

        if(type(y_axis) != list):
            y_axis_list = [y_axis]
        else:
            y_axis_list = y_axis


        if(type(ylabel) != list):
            ylabel_list = [ylabel]
        else:
            ylabel_list = ylabel


        fig, axes = plt.subplots(nr_of_subplots, 1, figsize=(15, 10), sharex=True)

        for i in range(nr_of_subplots):
            axes[i].plot(df[x_axis].values, df[y_axis_list[i]].values)
            axes[i].set_ylabel(ylabel_list[i])

        axes[-1].set_xlabel(xlabel, fontsize=18)
        fig.savefig(self.output_dir + title + ".pdf")
        plt.show()


class Numerical_Analysis(Analysis):

    def fft_with_freq_analysis(self, df, column_name, step_size):

        rfft = np.abs(np.fft.rfft(df[column_name].values))
        rfft_freq = np.sort(np.fft.fftfreq(rfft.size, step_size))
        return rfft, rfft_freq



