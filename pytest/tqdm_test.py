# -*- ecoding: utf-8 -*-
# @ModuleName: tqdm_test
# @Function: 
# @Author: Yufan-tyf
# @Time: 2022/4/1 20:02
from tqdm import tqdm
import numpy as np
if __name__ == '__main__':
    test_list = np.arange(10, 20, 1)
    for data in tqdm(test_list, desc='Processing'):
        print(data)
    # print(test_list)