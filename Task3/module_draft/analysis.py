# Author: Leonie Kreis, Gwydion Daskalakis
# Date: 18.03.21
# Package: DSS analysis package

import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt


class Analysis:
    """[analysis] parent class for the analysis with variance filter and plot function

    """
    def __init__(self, output_dir):
        """Initilizes the class

        Args:
            threshold (float): threshhold for the variance analysis
            output_dir (fstring): [name and location of output folder]
        """
        self.threshold = 1e-5
        self.output_dir = output_dir

    def remove_low_variance(self, df):
        """removes all columns with low variance

        Args:
            df ([pd.Dataframe]): the Dataframe that is to be analyzed
        """
        df = df.drop(df.columns[df.var() <= self.threshold], axis=1)

        return df

    def plot_and_save(self,
                      df,
                      x_axis,
                      y_axis,
                      title,
                      xlabel="",
                      ylabel="",
                      nr_of_subplots=1,
                      save_graph=True,
                      show_graph=True,
                      size=[15, 10],
                      crop_edge=0):
        """plots and saves the given data

        Args:
            df (pd.Dataframe): the Dataframe that is to be analyzed

            x_axis (string): the column name for the x-axis

            y_axis (string/list): the column name(s) for the y-axis

            title ([string]): [title of the plot and the filename]

            xlabel (str, optional): Custom label for the x-axis,
            if no label is given the column name will be used. Defaults to "".

            ylabel (str, optional): Custom label for the y-axis,
            if no label is given the column name will be used. Defaults to "".

            nr_of_subplots (int, optional): [nr of subplots]. Defaults to 1.

            save_graph (bool, optional): whether or not the graph should be saved as a pdf. Defaults to true.

            show_graph (bool, optional): whether or not the graph should be shown in a window. Defaults to true.

            size (list(int), optional): total size of the plot. Defaults to [15,10].

            crop_edge (int, optional): nr of cropped points at the edge of the graph. Defaults to 0.

        """

        if (type(y_axis) != list):
            y_axis_list = [y_axis]
        else:
            nr_of_subplots = len(y_axis)
            y_axis_list = y_axis

        # if(type(ylabel) != list):
        #     ylabel_list = [ylabel]
        # else:
        #     ylabel_list = ylabel

        # use column names as labels if no other label is given
        if (xlabel == ""):
            xlabel = x_axis
        if (ylabel == ""):
            ylabel = y_axis

        if (type(ylabel) != list):
            ylabel_list = [ylabel]
        else:
            ylabel_list = ylabel

        fig, axes = plt.subplots(nr_of_subplots,
                                 1,
                                 figsize=(size[0], size[1]),
                                 sharex=True,
                                 squeeze=False)

        for i in range(nr_of_subplots):
            if (crop_edge == 0) is True:
                axes[i, 0].plot(df[x_axis].values,
                                df[y_axis_list[i]].values,
                                label=ylabel_list[i])

            else:
                axes[i,
                     0].plot(df[x_axis].values[crop_edge:-crop_edge],
                             df[y_axis_list[i]].values[crop_edge:-crop_edge],
                             label=ylabel_list[i])
            axes[i, 0].set_ylabel(ylabel_list[i])
            axes[i, 0].legend()

        axes[-1, 0].set_xlabel(xlabel, fontsize=18)

        if save_graph:
            fig.savefig(self.output_dir + title + ".pdf")
        if show_graph:
            plt.show()


class Statistical_Analysis(Analysis):
    """[Statistical Analysis] child class for statistical analysis, provides seabornplot, correlation matrix and euclidean distance

    Args:
        Analysis ([dataframe]): dataframe to be analyzed

    """
    def __init__(self, output_dir):
        Analysis.__init__(self, output_dir)

    def seaborn_plot(self, df):
        """[Seaborn plot] plots dataframe with seaborn

        Args:
            df ([dataframe]): dataframe which we want to plot

        Returns:
            seaborn plot.

        """
        df = df.drop(df.columns[df.var() <= self.threshold], axis=1)
        df.keys()
        g = sn.relplot(x="time",
                       y="value",
                       hue="variable",
                       kind="line",
                       data=pd.melt(df, ['time']))
        g.fig.autofmt_xdate()

    def correlation(self, df, writecsv=True):
        """[Correlation] provides correlation matrix of the dataframe

        Args:
            df ([dataframe]): dataframe which we want to compute the correlation from

        Returns:
            dataframe of sorted correlations (without the time column) and prints results in csv file (in output directory)
        """
        df = Analysis.remove_low_variance(self, df)
        corr_npop = df.corr()

        corr_npop_np = corr_npop.to_numpy()

        corr_npop_np = np.triu(corr_npop_np, k=1)
        corr_npop_df = pd.DataFrame(data=corr_npop_np, index=corr_npop.keys(), columns=corr_npop.keys())
        corr_npop_df = corr_npop_df.drop('time', axis=1)
        corr_npop_df = corr_npop_df.melt(ignore_index=False)
        corr_npop_df = corr_npop_df[corr_npop_df['value'] != 0]
        corr_npop_df = corr_npop_df.sort_values(
            by='value', key=abs, ascending=False)
        if writecsv:
            corr_npop_df.to_csv(self.output_dir + 'npop_out.csv')
        return corr_npop_df


    def eucl_distance(self, df):
        """[Euclidean Distance] computes euclidean distance of of the three components

        Args:
            df (dataframe): underlying dataframe from which we want to compute the distances

        Returns:
            numpy array consisting of the three distances in order of x,y,z.
            Further it saves the results in an txt file in the outputdirectory
        """
        # table_np = np.loadtxt(filenames_dict["table_dat"], skiprows=1)

        table_np = df.values
        table_np = np.nan_to_num(table_np)
        dist_2_3 = np.linalg.norm(table_np[:, 2] - table_np[:, 3])
        dist_4_5 = np.linalg.norm(table_np[:, 4] - table_np[:, 5])
        dist_6_7 = np.linalg.norm(table_np[:, 6] - table_np[:, 7])
        dist_all = [dist_2_3, dist_4_5, dist_6_7]
        dist_all
        plt.figure()
        plt.scatter([1, 2, 3], dist_all)
        plt.savefig(self.output_dir + 'table_plot.pdf')
        plt.show()
        np.savetxt(self.output_dir + 'table_out.txt', dist_all)
        return dist_all



class Numerical_Analysis(Analysis):
    def fft_with_freq_analysis(self,
                               df,
                               column_name,
                               step_size=0,
                               type="real"):
        """Calculates the fft and gives the frequencies in an pd.Dataframe.

        Args:
            df (pd.Dataframe): the Dataframe which includes the relevant data.

            column_name (string): the column name for the fft.

            step_size (float): stepsize for the freq analysis.
            Will use differenz beween first two steps if to inout is given, default =0.

            type (string): choice between "real" and "complex", this will determine the type of fft,
            default = "real".


        Returns:
            pd.Dataframe: The columns are freq and intensity
        """
        if step_size == 0:

            step_size = df.iloc[1, 0] - df.iloc[0, 0]

        if (type == "real"):
            rfft = np.abs(np.fft.rfft(df[column_name].values))

        if (type == "complex"):
            rfft = np.fft.fft(df[column_name].values)

        rfft_freq = np.sort(np.fft.fftfreq(rfft.size, step_size))
        return pd.DataFrame(list(zip(rfft_freq, rfft)),
                            columns=["freq", "intensitys"])

    def autocorrelation(self, df, time_label):
        """Calculates the autocorrolation function of a given complex dataframe that includes a time axis.

        Args:
            df (pd.Dataframe): The Dataframe which includes the relevant data.

            time_label (string): Label name of the time column.

        Returns:
            pd.Dataframe: The columns are: time, autocorr, autocorr_abs, autocorr_real, autocorr_imag,
            where "autocorr" is the complete complex number and the others are the respective part of it.
        """
        imag_array = df.drop(time_label, axis=1).values
        autocorr = np.zeros(len(imag_array), dtype=complex)
        for t in range(len(imag_array)):
            autocorr[t] = np.sum(imag_array[0, :] * imag_array[t, :])
        return pd.DataFrame(list(
            zip(df[time_label].values, autocorr, np.abs(autocorr),
                np.real(autocorr), np.imag(autocorr))),
                            columns=[
                                "time", "autocorr", "autocorr_abs",
                                "autocorr_real", "autocorr_imag"
                            ])
