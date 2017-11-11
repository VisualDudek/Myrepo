""" Use k-means to locate voting clusters in the U.S. Congres.

"""
import csv
import glob
from collections import defaultdict
from pprint import pprint
from typing import NamedTuple, DefaultDict, List, Dict
from kmeans import k_mean, assign_data


# It will be easy to create Senator object
from typing import Tuple

Senator = NamedTuple('Senator', [('name', str), ('party', str), ('state', str)])
VoteValue = int
VoteHistory = Tuple[VoteValue, ...]

# Load votes which were arranged by topic and accumulate votes by senator
vote_value: Dict[str, VoteValue] = {'Yea': 1, 'Nay': -1, 'Not Voting': 0}       # type: Dict[str, VoteValue]
accumulated_record = defaultdict(list)                    # type: DefaultDict[Senator, List[VoteValue]]
for filename in glob.glob('congress_data/*.csv'):
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        vote_topic = next(reader)
        headers = next(reader)
        for person, state, district, vote, name, party in reader:       # OLD: for row in reader:
            senator = Senator(name, party, state)
            accumulated_record[senator].append(vote_value[vote])

# lists are used in accumulation phase next you want dictionary KEY
# Transform the record into a plain dict that maps to tuple of votes
record = {senator: tuple(votes) for senator, votes in accumulated_record.items()}  # type: Dict[Senator, VoteHistory]
#                     ^== cast or type conversion


# Use k-means to locate the cluster centroids from pattern of votes, assign each senator to the nearest cluster
centroids = k_mean(record.values(), k=3, iterations=100)
clustered_votes = assign_data(centroids, record.values())

for centroid in centroids:
    for x in centroid:
        print(f'{x:.2f}', end=' ')
    print()

pprint(clustered_votes)

""" Przykłady dostępu do namedtupla
print('------------')
print(senator)
print(senator.name)
print(senator.party)
print(senator[0])
print(senator[1])
"""

