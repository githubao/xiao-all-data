#!/usr/bin/env python
# encoding: utf-8

"""
@description: 合并两个有序列表

@author: baoqiang
@time: 2020/6/29 10:00 下午
"""


def combine_ab(s1, s2):
    if len(s1) == 0:
        return s2
    if len(s2) == 0:
        return s1

    res = list()
    i, j = 0, 0
    l1, l2 = len(s1), len(s2)

    # same as eof
    s1.append(1000)
    s2.append(1000)

    while i < l1 or j < l2:
        if s1[i] < s2[j]:
            res.append(s1[i])
            i += 1
            continue
        elif s1[i] > s2[j]:
            res.append(s2[j])
            j += 1
            continue
        else:
            # 不添加相同的元素
            i += 1
            continue

    return res


def combine_ab_2(a, b, res):
    if len(a) == 0:
        res.extend(b)
        return res
    if len(b) == 0:
        res.extend(a)
        return res

    if a[0] < b[0]:
        res.append(a[0])
        return combine_ab_2(a[1:], b, res)
    else:
        res.append(b[0])
        return combine_ab_2(a, b[1:], res)


def run():
    a = [1, 2, 3]
    b = [2, 4, 5, 6, 7]
    # c = combine_ab(a, b)
    # a = [1]
    # b = [2]
    c = combine_ab_2(a, b, [])
    print(c)


if __name__ == '__main__':
    run()
