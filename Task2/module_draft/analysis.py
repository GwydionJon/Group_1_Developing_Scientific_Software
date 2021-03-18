import numpy as np 
import pandas as pd 
import seaborn as sn 
import matplotlib.pyplot as plt

class Analysis:
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


class Statistical_Analysis(Analysis):
    """[summary]

    Args:
        Analysis ([type]): [description]
    """
    def __init__(self, output_dir):
        Analysis.__init__(self, output_dir)

    def seaborn_plot(self, df):
        df=df.drop(df.columns[df.var()<=self.threshold],axis=1)
        df.keys()
        g = sn.relplot(x="time", y="value", hue="variable", kind="line", data=pd.melt(df, ['time']))
        g.fig.autofmt_xdate()



    def correlation(self,df): 
        corr_npop = df.corr()   
        corr_npop_np = corr_npop.to_numpy()
        corr_npop_np = np.triu(corr_npop_np, k=1)
        corr_npop_df = pd.DataFrame(data=corr_npop_np, index= ['time', 'MO3', 'MO4', 'MO6', 'MO11', 'MO12', 'MO14'], columns= ['time', 'MO3', 'MO4', 'MO6', 'MO11', 'MO12', 'MO14'])
        corr_npop_df = corr_npop_df.drop('time', axis=1)
        corr_npop_df = corr_npop_df.melt(ignore_index=False)
        corr_npop_df = corr_npop_df[corr_npop_df['value']!=0]
        corr_npop_df = corr_npop_df.sort_values(by='value', key=abs, ascending=False)
        corr_npop_df
        corr_npop_df.to_csv(self.output_dir+'npop_out.csv')


    def eucl_distance(self, df):
        #table_np = np.loadtxt(filenames_dict["table_dat"], skiprows=1)
        table_np = df.values
        table_np = np.nan_to_num(table_np)
        dist_2_3 = np.linalg.norm(table_np[:,2]-table_np[:,3])
        dist_4_5 = np.linalg.norm(table_np[:,4]-table_np[:,5])
        dist_6_7 = np.linalg.norm(table_np[:,6]-table_np[:,7])
        dist_all = [dist_2_3, dist_4_5, dist_6_7]
        dist_all
        plt.figure()
        plt.scatter([1, 2, 3], dist_all )
        plt.savefig(self.output_dir+'table_plot.pdf')
        plt.show()
        np.savetxt(self.output_dir+'table_out.txt', dist_all)


