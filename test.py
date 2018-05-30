#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Zhang Shuai'

import pickle,os
a = [[1,1,1,1],[2,2],[3,3,3]]
def pad_sequences(sequences, pad_mark=0):
    """

    :param sequences:
    :param pad_mark:
    :return:
    """
    max_len = max(map(lambda x : len(x), sequences))
    print(max_len)
    seq_list, seq_len_list = [], []
    for seq in sequences:
        seq = list(seq)
        seq_ = seq[:max_len] + [pad_mark] * max(max_len - len(seq), 0)
        seq_list.append(seq_)
        seq_len_list.append(min(len(seq), max_len))
    return seq_list, seq_len_list
pad_sequences(a)
print(a[2]+[0,0])