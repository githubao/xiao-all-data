#!/usr/bin/env python
# encoding: utf-8

"""
@description: pca 降维

@author: baoqiang
@time: 2020/7/1 12:50 下午
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA


def run():
    pca1()
    pca2()


def pca1():
    # load data
    iris = load_iris()
    data = iris.data

    # norm
    mean_val = np.mean(data, axis=0)
    meaned_data = data - mean_val

    # log
    print('feature mean: ', np.mean(meaned_data, axis=0))
    print('mean samples: ',meaned_data[:5, :])

    # cov, rowvar=False, column as feature
    cov_mat = np.cov(meaned_data, rowvar=False)
    print('cov shape: ', cov_mat.shape)
    print('cov mat: ', cov_mat)

    # eig
    eig_vals, eig_vecs = np.linalg.eig(np.mat(cov_mat))
    print("eig_vals: ", eig_vals)
    print("eig_vecs: ", eig_vecs)

    # desc order
    sorted_idx = np.argsort(-eig_vals)
    top2_idx = sorted_idx[:2]
    top2_vec = eig_vecs[:, top2_idx]
    print('top2 vec: ', top2_vec)

    # pca
    pca_data = meaned_data * top2_vec
    print('pca samples: ', pca_data[:5, :])

    # restore
    recon_data = (pca_data * top2_vec.T) + meaned_data
    print("rocon samples: ", recon_data[:5, :])


def pca2():
    # load data
    iris = load_iris()
    data = iris.data

    pca = PCA(n_components=2)
    print('pca: ', pca)
    feature2 = pca.fit_transform(data)

    print('accurate ratio: ', pca.explained_variance_ratio_)
    print('feature samples: ', feature2[:5, :])


if __name__ == '__main__':
    run()
