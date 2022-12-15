def count_batteries_by_usage(cycles):
  for i in cycles:
    if i<310:
      low_count=low_count+1
    if i<=929 and i>=310:
      medium_count=medium_count+1
    if i>=930:
      high_count=high_count+1
  return {
    "lowCount": low_count,
    "mediumCount": medium_count,
    "highCount": high_count
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
