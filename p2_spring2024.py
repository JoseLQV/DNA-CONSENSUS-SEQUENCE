"""This program reads DNA sequences from an input file and finds the
consensus sequence.  An output file is also created to store the
counts per column, so as to validate the consensus.
Add the corresponding code to accomplish the requested tasks
"""



##### ADD YOUR NAME, Student ID, and Section number #######
# NAME: 
# STUDENT ID:
# SECTION:
###########################################################


def load_data(fileName):
    #Read DNA sequences from file and return them in a list.
    # Assume the file to be open exist
    dataList = list()
    # Use dataList to save the the all data from the file 
    # If file opens successfully, loop over the contents and store sequences in list.
    # Skip description lines (lines that start with ">").

    return dataList


def count_nucl_freq(dataList):
    """Count the occurrences of characters by column."""
    countStruct = list() # Indexed by columns (List of what?)

    # Loop over the sequences in dataList to count the nucleotides
    # We'll need a nested loop to process every character in every sequence.
    # Recommend: Use outer loop for columns (characters) and inner loop for
    # rows (sequences), since countStruct only cares about the characters (not the seqs).

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
