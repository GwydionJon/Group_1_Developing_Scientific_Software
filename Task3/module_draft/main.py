# Author: Tobias Kaczun, Leonie Kreis, Gwydion Daskalakis
# Date: 19.03.21
# Package: DSS Analysis Package

import sys
import numpy as np

import reader
from user_input import user_input
import analysis


def main():
    """Main function for commandline call
    """
    # end user version for user_input
    args = user_input(sys.argv[1:])

    # add your own args = user_input() for testing and debugging so that you
    # don't have to call the script with full command line input

    # args = user_input(['Input/Task1/', '-o',
    #                    'Output/Task2/'])

    # read files
    reader_obj = reader.FileReader(args.path)
    input_df = reader_obj.read()

    # perform statistical analysis
    stat_ana = analysis.Statistical_Analysis(args.output)
    stat_ana.correlation(input_df['npop.t'])
    stat_ana.eucl_distance(input_df['table.dat'])

    # perfomr numerical analysis
    num_ana = analysis.Numerical_Analysis(args.output)

    # return new df with the desired columns
    df_efield_relevant = num_ana.remove_low_variance(input_df['efield.t'])

    # fft with freq of the df
    df_efield_fft = num_ana.fft_with_freq_analysis(df_efield_relevant, "y")

    # disabled plot to not have it get on my nerves
    num_ana.plot_and_save(df_efield_fft, "freq", "intensitys",
                          "efield_fft_analysis", xlabel="Freq",
                          show_graph=False)

    df_autocorr = num_ana.autocorrelation(input_df["nstate_i.t"], "time")
    num_ana.plot_and_save(df_autocorr, "time", ["autocorr_abs",
                                                "autocorr_real",
                                                "autocorr_imag"],
                          "nstate_autocorr_analysis", xlabel="time",
                          show_graph=False)

    df_autocorr_fft = num_ana.fft_with_freq_analysis(
        df_autocorr, "autocorr", type="complex")

    # adding abs**2 to the dataframe
    df_autocorr_fft["intensitys_squared"] = np.abs(
        df_autocorr_fft["intensitys"].values)**2
    num_ana.plot_and_save(df_autocorr_fft, "freq", ["intensitys",
                                                    "intensitys_squared"],
                          "nstate_autocorr_fft_analysis", xlabel="Freq",
                          show_graph=True, crop_edge=3)


if __name__ == "__main__":
    main()
