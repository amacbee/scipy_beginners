# !/usr/local/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
print pd.read_table('../data/batters.txt', sep='\t', index_col=0)


