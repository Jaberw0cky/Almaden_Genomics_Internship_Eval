from  Bio import SeqIO

# Function to find all occurrences of a subsequence in a sequence
def find_subsequence(seq, subseq):
    count = 0
    positions = []
    start = 0
    while True:
        position = seq.find(subseq, start)
        if position == -1:
            break
        count += 1
        positions.append(position)
        start = position + 1
    return count, positions

# Read the subsequence from sequences.txt
with open('sequences.txt', 'r') as seq_file:
    subsequence = seq_file.read().strip()

# Initialize counters
hit_count = 0
hit_positions = {}

# Open the output files
with open('hit_entries.fastq', 'w') as hit_entries_file, open('hits.txt', 'w') as hits_file:
    # Iterate through the FASTQ file
    for record in SeqIO.parse('SRR11772358_1M_filtered_1.fastq', 'fastq'):
        # Find occurrences of the subsequence in the read
        count, positions = find_subsequence(str(record.seq), subsequence)

        # If at least one occurrence is found, write to hit_entries.fastq
        if count > 0:
            hit_count += 1
            hit_entries_file.write(record.format('fastq'))

        # Record the count and positions in hits.txt
        hits_file.write(f'{record.id}\t{count}\t{positions}\n')

# Print summary
print(f'Total matching entries: {hit_count}')
