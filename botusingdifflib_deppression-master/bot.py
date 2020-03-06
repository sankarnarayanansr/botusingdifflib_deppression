import pandas as pd
from difflib import get_close_matches
from difflib import SequenceMatcher
from heapq import nlargest as _nlargest



def get_close_matches_indexes(word, n=3, cutoff=0.6):
    
    data=pd.read_csv('scrap.csv')
    pattern=list(data['title'])
    possibilities=list(data['title'])
    if not n >  0:
        raise ValueError("n must be > 0: %r" % (n,))
    if not 0.0 <= cutoff <= 1.0:
        raise ValueError("cutoff must be in [0.0, 1.0]: %r" % (cutoff,))
    result = []
    s = SequenceMatcher()
    s.set_seq2(word)
    for idx, x in enumerate(possibilities):
        s.set_seq1(x)
        if s.real_quick_ratio() >= cutoff and \
           s.quick_ratio() >= cutoff and \
           s.ratio() >= cutoff:
            result.append((s.ratio(), idx))

    result = _nlargest(n, result)

    b=[x for score, x in result]
    print(data.loc[b]['response'])
    d=data.loc[b]['response']
    # for i in d:
    #     print(i)
    return data.loc[b[0]]['response']

# c=get_close_matches_indexes(inp, pattern)
# print()
