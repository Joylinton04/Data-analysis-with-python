# import pandas as pd
# import re

# df = pd.read_csv('FINE GRAINED SENTIMENTS.csv')
# top_section = df.head(10)
# tail_section = df.tail()

# df.map(lambda x: re.sub(r"[^a-zA-Z0-9\s.]", "", str))
# print(top_section)

list_ = ['foo', 'card', 'bar', 'aaaa', 'abab']

sorted_list = list_.sort(key=lambda x: len(set(list(x))))

# print(list_)

word = "lintonmm"

print(set(list(word)))