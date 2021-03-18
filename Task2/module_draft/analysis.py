import numpy as np 
import pandas as pd 
import seaborn as sn 
import matplotlib.pyplot as plt

class analysis:
    """[analysis] parent class for the analysis with variance filter and plot function
    """
    def __init__(self,output_dir):
        self.threshold = 1e-5
        self.output_dir = output_dir

    def remove_low_variance(self, df):
        df = df.drop(df.columns[df.var() <= self.threshold], axis=1)

    def plot_and_save(self, df, x_axis, y_axis, title, xlabel="", ylabel="", nr_of_subplots=1):
        

        if(type(y_axis) != list):
            y_axis_list = [y_axis]
        else:
            y_axis_list = y_axis


        if(type(ylabel) != list):
            ylabel_list = [ylabel]
        else:
            ylabel_list = ylabel


        fig, axes = plt.subplots(nr_of_subplots, 1, figsize=(15, 10), sharex = True)

        for i in range(nr_of_subplots):
            axes[i].plot(df[x_axis].values, df[y_axis_list[i]].values)
            axes[i].set_ylabel(ylabel_list[i])

        axes[-1].set_xlabel(xlabel, fontsize = 18)
        fig.savefig(self.output_dir + title + ".pdf")
        plt.show()


