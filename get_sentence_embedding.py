#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba
import re
import numpy as np
from gensim.models import Word2Vec
from scipy.spatial.distance import cosine

# 加载词向量模型
model = Word2Vec.load('wiki_and_news_word2vec_200.model')
word_dict = model.wv.vocab
word_count = model.corpus_count

def cut(str):
    return ' '.join(jieba.cut(str))

def token(string):
    return ' '.join(re.findall('[\w|\d]+',string))

def get_count(word,dim=200):
    """得到词频"""
    # vector = np.zeros(1)

    if word in word_dict:
        wf = word_dict[word].count
        wv = model.wv[word]
    else:
        wf = 1
        wv = np.zeros(dim)
    return wf / word_count,wv

# def sentence_embedding(sentence,cut):
#     # weight = alpah/(alpah + p)
#     # alpha is a parameter, 1e-3 ~ 1e-5
#     alpha = 1e-4
#
#     words = cut(sentence).split()
#
#     sentence_vec = np.zeros_like(model.wv[words])
#
#     words = [w for w in words if w in word_dict]
#
#     for w in words:
#         weight = alpha / (alpha + get_count(w))
#         sentence_vec += weight * model.wv[w]
#
#     sentence_vec /= len(words)

# 获取句子向量

def sentence_embedding(sentences,dim=200):
    # a = 1e-3
    alpha = 1e-4

    # words = cut(sentences).split()
    words = cut(token(sentence)).split()
    sum_vector = np.zeros(dim)
    for i,w in enumerate(words):
        wf,wv = get_count(w)
        sum_vector += alpha / (alpha + wf) * wv
    return sum_vector / (i+1)

sentence = '当然，关于MIUI 9的确切信息，我们还是等待官方消息。'
# print(token(sentence))
# print(cut(token(sentence)))
# print(cut(token(sentence)).split())
print(sentence_embedding(sentence))

def get_corrlations(text,cut_func):
    if isinstance(text,list):text= ' '.join(text)

    sub_sentences =