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
            threshold ([float]): [threshhold for the variance analysis]
            output_dir ([string]): [name and location of output folder]
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
            df ([pd.Dataframe]): [the Dataframe that is to be analyzed] 
            x_axis ([string]): [the column name for the x-axis]\ 
            y_axis ([string/list]): [the column name(s) for the y-axis]
            title ([string]): [title of the plot and the filename]
            xlabel (str, optional): [label for the x-axis]. Defaults to "".
            ylabel (str, optional): [label for the y-axis]. Defaults to "".
            nr_of_subplots (int, optional): [nr of subplots]. Defaults to 1.

            list_ref (integer list): A list with the indices of the reference vectors.
            list_comp (integer list): A list with the indices of the vectors to\
            compare to.
            data (numpy array): The data object.
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
        """[calculates the fft and gives the frequencies in an pd.Dataframe]

        Args:
            df ([pd.Dataframe]): [the Dataframe which includes the relevant data]
            column_name ([string]): [the column name for the fft]
            step_size ([float]): [stepsize for the freq analysis]

        Returns:
            [pd.Dataframe]: [with freq and intensity]
        """
        
        rfft = np.abs(np.fft.rfft(df[column_name].values))
        rfft_freq = np.sort(np.fft.fftfreq(rfft.size, step_size))
        return pd.DataFrame([rfft_freq, rfft],columns=["freq", "intensitys" ])

    def autocorrelation(self, df, time_label):
        """[calculates the autocorrolation function]

        Args:
            df ([pd.Dataframe]): [the Dataframe which includes the relevant data]
            time_label ([type]): [label name of the time column]

        Returns:
            [pd.Dataframe]: [time, autocorr]
        """
        imag_array = df.drop(time_label, axis=1).values
        autocorr = np.zeros(len(imag_array), dtype=complex)
        for t in range(len(imag_array)):
            autocorr[t] = np.sum(imag_array[0, :] * imag_array[t, :])
        return pd.DataFrame([df[time_label], autocorr], columns=["time", "autocorr"])
