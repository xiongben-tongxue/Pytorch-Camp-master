# -*- coding:utf-8 -*-
"""
@file name  : lesson-02.py
@author     : TingsongYu https://github.com/TingsongYu
@date       : 2018-08-26
@brief      : 张量的创建
"""
import torch
import numpy as np
torch.manual_seed(1)

# ===============================  example 1 ===============================
# 通过torch.tensor创建张量
#
flag = True
#flag = False
if flag:
    arr = np.ones((3, 3))
    print("ndarray的数据类型：", arr.dtype)

    t = torch.tensor(arr, device='cuda')
    # t = torch.tensor(arr)

    print(t)
