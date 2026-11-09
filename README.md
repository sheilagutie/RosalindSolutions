# RosalindSolutions
def gc_content(sequence):
  gc_count = sequence.count("G") + sequence.count("C")
  gc_percentage = (gc_count / len(sequence)) * 100
  return gc_percentage

gc_content(sequence1)
