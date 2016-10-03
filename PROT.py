

from Bio.Seq import Seq
import Bio.Alphabet

f = open("rosalind_prot (2).txt", 'r')
seq = Seq(f.read().replace('\n', ''), Bio.Alphabet.IUPAC.unambiguous_rna)
f.close

protein = seq.translate(to_stop=True)

o = open("0088_PROT2.txt", 'w')
o.write(str(protein))
o.close()
