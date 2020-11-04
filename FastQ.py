import gzip

fastq = gzip.open("FAL76452_pass_b7700786_985.fastq.gz","rt")
lines = fastq.readlines()

n=100
file = open("100.txt","w")
i=0
for line in lines:
    i=i+1
    if (i+2) % 4 == 0:
        file.write(line[0:n]+"\n")
        


fastq.close()
file.close()  
