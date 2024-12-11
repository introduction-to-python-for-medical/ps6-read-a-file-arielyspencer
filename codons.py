def create_codon_dict(file_path):
    f = open(file_path)
    rows = f.readlines()
    f.close()
    mydic = {}
    for row in rows:
      c = row.strip().split('\t')
      mydic[c[0]] = c[2]
    return mydic


