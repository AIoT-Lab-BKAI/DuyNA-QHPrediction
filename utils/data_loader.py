#  nhan vao input la mot file
# xu ly ssa
# tra ve dang du lieu mong muon 

import numpy as np
import pandas as pd
from utils.ssa import SSA
from utils.reprocess_daily import extract_data, ed_extract_data, roll_data

def get_input_data(input_file, default_n,sigma_lst):
    dat = pd.read_csv(input_file, header=0, index_col=0)
    Q = dat['Q'].to_list()
    H = dat['H'].to_list()

    lst_H_ssa = SSA(H, default_n)
    lst_Q_ssa = SSA(Q, default_n)

    H_ssa = lst_H_ssa.reconstruct(sigma_lst)
    Q_ssa = lst_Q_ssa.reconstruct(sigma_lst)

    # dat['Q_ssa'] = Q_ssa
    # dat['H_ssa'] = H_ssa

    dat['Q'] = Q_ssa
    dat['H'] = H_ssa
    # print(dat.head())
    result = dat[[ 'Q', 'H']]
    return result

if __name__=="__main__":
    res = get_input_data('../data/SonTay.csv', 20,[1,2,3])
    res.to_csv('../data/modified_data.csv')
    print(res.head())