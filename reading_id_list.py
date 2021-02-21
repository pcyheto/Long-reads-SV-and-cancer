import gzip
from Bio import SeqIO

with gzip.open("IDs","rb") as f:
    mylist=(f.readlines())

appended=[]

for l in mylist:
    appended.append(l.strip().decode())

with gzip.open("reads", "rt") as g, open("output.fastq","wt") as output:
    for records in SeqIO.parse(g, "fastq"):
        if records.id in appended:
            SeqIO.write([records],output,"fastq")



