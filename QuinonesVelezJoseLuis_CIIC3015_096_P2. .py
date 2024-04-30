"""This program reads DNA sequences from an input file and finds the
consensus sequence.  An output file is also created to store the
counts per column, so as to validate the consensus.
Add the corresponding code to accomplish the requested tasks
"""



##### ADD YOUR NAME, Student ID, and Section number #######
# NAME: Jose Luis Quinones Velez
# STUDENT ID: 843-18-5449
# SECTION: CIIC 3015-096
###########################################################


def load_data(fileName):
    # Assume the file to be open exist
    dataList = list()
    
    #Read DNA sequences from file and return them in a list.
    with open(fileName, "r") as file:
        for line in file:
            # Skip description lines (lines that start with ">").
            if line.strip()[0] != ">":
                # If file opens successfully, loop over the contents and store sequences in list.
                
                # Use dataList to save the the all data from the file 
                dataList.append(line.strip())
            
    return dataList


def count_nucl_freq(dataList):
    """Count the occurrences of characters by column."""
    countStruct = list({}) # Indexed by columns (List of what?) 
    
    # Recommend: Use outer loop for columns (characters) and inner loop for
    # rows (sequences), since countStruct only cares about the characters (not the seqs).
    
    # # datalist = GATCAGCTAG
    #              AATCCGATCG
    #              AATGCGCTAG
    #              ACTCTGCGTG

    
    # Loop over the sequences in dataList to count the nucleotides
    for row,seq in enumerate(dataList):
        for col,char in enumerate(seq):
            if row == 0:
                countStruct.append({"A":0,"G":0,"C":0,"T":0})
            pos = countStruct[col]
            if char in pos:
                pos[char] += 1
        
    return countStruct
    

def find_consensus(countData):
    """Return the consensus sequence according to highest-occuring nucleotides"""
    consensusString = ""

    # Loop here to find highest-occuring nucleotide in each column
    # and concatenate them into consensusString
    return consensusString


def process_results(countData, outFilename):
    """Print consensus to screen and store results in output file."""
    consensus = find_consensus(countData)
    print(consensus)

    # Now open the output file, and write the consensus string.
    # Then loop, to print nucleotide count in non-increasing order.
    # Each row in the output file (except the first one) should
    # have the count data for a column, in order of columns.


def main():

    # File name "constants". Assume the names of the files don change.
    INPUTFILE  = "DNAInput.txt" #  or "DNAInput.fasta"
    OUTPUTFILE = "DNAOutput.txt"

    seqList = load_data(INPUTFILE)

    countData = count_nucl_freq(seqList)

    process_results(countData, OUTPUTFILE)

# The code below makes Python start from the main function
# whenever our program is invoked as a "standalone program"
# (as opposed to being imported as a module).
if __name__ == "__main__":
    main()
