import gzip
from Bio import SeqIO

list_lengths=[4000,5000000,4000,5000000,4000]
list_iterations=[50,1,10,1,10]

i=0

with gzip.open('FAL76452_pass_b7700786_985.fastq.gz', 'rt') as f:
    record_iterator=SeqIO.parse(f,"fastq")
    while i<5:
        n=list_iterations[i]
        m=list_lengths[i]
        j=0
        while j<n:
            file_name=str(list_lengths[i])+'_'+str(j)+'.fastq'
            k=0
            with open(file_name,"wt") as output:
                while k<m:
                    rec=next(record_iterator)
                    SeqIO.write([rec],output,"fastq")
                    k=k+1
            j=j+1

        i=i+1
            
