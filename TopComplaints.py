# break complaints into different complaint types, and
# output one complaint type per line, followed by the number of complaints of
# that type.
# Output the items ordered by the greatest to lowest number of complaints.
#
# e.g. output:
# Street Condition with 450 complaints
# Highway Sign - Damaged with 421 complaints
# Sidewalk condition with 405 complaints
# Bridge condition with 388 complaints


import csv
import os
import sys

# Problem solution.
def solution(filename, k):
  complaintTypeCount = {}
  # Columns:
  # Unique Key,Created Date,Closed Date,Agency,Agency Name,Complaint Type,...
  with open(filename) as f:
    csvReader = csv.reader(f)
    headers = next(csvReader)

    for row in csvReader:
      complaintType = row[5]
      count = complaintTypeCount.setdefault(complaintType, 0)
      complaintTypeCount[complaintType] = count + 1

  # Computes list of complaint types sorted by number of complaints.
  sortedByCount =\
  sorted(complaintTypeCount.iteritems(), key=lambda x: (-x[1], x[0]), reverse=False)

  kTop = sortedByCount[:k]
  for item in kTop:
    print '%s with %d complaints' % (item[0], item[1])


if __name__ == '__main__':
  # Runs with provided filename.
  solution(sys.argv[1], int(sys.argv[2]))
