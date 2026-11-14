with open('notes.txt', 'r') as file:
        lines = file.readlines()
print(lines)
print(len(lines))
print(lines[0].strip()) 




with open('human_genes.fasta', 'r') as file:
 lines = file.readlines()
 
 print(lines)
 print(len(lines)/2)
 



def fasta_to_dict(filename):
    sequences = {}
    name = None
    seq_parts = []

    with open(filename) as r:
        for line in r:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if name is not None:
                    sequences[name] = "".join(seq_parts)
                name = line[1:].split()[0]  # just the gene name, e.g. BRCA1
                seq_parts = []
            else:
                seq_parts.append(line)

        if name is not None:
            sequences[name] = "".join(seq_parts)

    return sequences


human_genes = fasta_to_dict("human_genes.fasta")

# Two columns: gene name, sequence
for name, seq in human_genes.items():
    print(f"{name}\t{seq}")


    seq_parts = []

    with open(filename) as r:
        for line in r:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if name is not None:
                    sequences[name] = "".join(seq_parts)
                name = line[1:].split()[0]
                seq_parts = []
            else:
                seq_parts.append(line)

        if name is not None:
            sequences[name] = "".join(seq_parts)

    return sequences


def gc_content(seq):
    seq = seq.upper()
    if len(seq) == 0:
        return 0.0
    gc = seq.count("G") + seq.count("C")
    return gc / len(seq) * 100


human_genes = fasta_to_dict("human_genes.fasta")

with open("gc_report.txt", "w") as out:
    for name, seq in human_genes.items():
        out.write(f"{name}\t{gc_content(seq):.1f}\n")
