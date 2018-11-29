# coding: utf-8

# Copyright (c) 2012, Machinalis S.R.L.
# This file is part of quepy and is distributed under the Modified BSD License.
# You should have received a copy of license in the LICENSE file.
#
# Authors: Rafael Carrascosa <rcarrascosa@machinalis.com>
#          Gonzalo Garcia Berrotaran <ggarcia@machinalis.com>

"""
Modified to be able to use it in Spanish
Needed library: pattern
"""

from quepy.tagger import Word

# Replace Spanish module to modify language
from pattern.text.es import parsetree
def run_nltktagger(string, nltk_data_path=None):
    parsed = parsetree(string, lemmata=True)
    words = []
    for sentence in parsed:
        for w in list(sentence):
            word = Word(w.string,pos=w.type,lemma=w.lemma)
            words.append(word)

    return words
