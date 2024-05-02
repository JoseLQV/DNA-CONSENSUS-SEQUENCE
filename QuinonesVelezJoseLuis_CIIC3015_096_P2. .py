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
            # initialize maps in the first sequence
            if row == 0:
                countStruct.append({"A":0,"G":0,"C":0,"T":0})
            pos = countStruct[col]
            if char in pos:
                pos[char] += 1
        
    return countStruct
    

def find_consensus(countData):
    """Return the consensus sequence according to highest-occuring nucleotides"""
    consensusString = ""

#     countData = [
# {'A': 3, 'G': 1, 'C': 0, 'T': 0}, 
# {'A': 3, 'G': 0, 'C': 1, 'T': 0}, 
# {'A': 0, 'G': 0, 'C': 0, 'T': 4}, 
# {'A': 0, 'G': 1, 'C': 3, 'T': 0}, 
# {'A': 1, 'G': 0, 'C': 2, 'T': 1}, 
# {'A': 0, 'G': 4, 'C': 0, 'T': 0}, 
# {'A': 1, 'G': 0, 'C': 3, 'T': 0}, 
# {'A': 0, 'G': 1, 'C': 0, 'T': 3}, 
# {'A': 2, 'G': 0, 'C': 1, 'T': 1}, 
# {'A': 0, 'G': 4, 'C': 0, 'T': 0}]

    # Loop here to find highest-occuring nucleotide in each column
    for map in countData:
        maxValue = 0
        maxKey = ""
        # find highest-occuring nucleotide
        for key in map:
           if map[key] >= maxValue:
               maxKey = key
               maxValue = map[key]
        # and concatenate them into consensusString
        consensusString += maxKey
    
    return consensusString


def process_results(countData, outFilename):
    """Print consensus to screen and store results in output file."""
    consensus = find_consensus(countData)
    print("Consensus:",consensus)

    # Now open the output file, and write the consensus string.
    with open(outFilename,"w") as w_file:
        w_file.write(f"Consensus: {consensus}\n")
                    
    # Each row in the output file (except the first one) should
    # have the count data for a column, in order of columns.
        for pos,map in enumerate(countData):
            
            # initialize non increasing order string
            # Each row in the output file (except the first one) should
            # have the count data for a column, in order of columns.
            if pos+1 < 10 :
                orderedString = f"pos {pos+1}: "
            else:
                orderedString = f"pos {pos+1}:"
            
            # Then loop, to print nucleotide count in non-increasing order.
            listed = list(map.items())
            orderedlist = []
            i = 0
            #traverse tuples
            while len(listed) != 0:
                tuple = listed[0]
                max_tuple = tuple
                 #find highest-value
                for j in range(i+1,len(listed)):
                    next_tuple = listed[j]
                    if next_tuple[1] > tuple[1]:
                        max_tuple = next_tuple
                #add highest value tuple in result (ordered List)        
                listed.remove(max_tuple)
                orderedlist.append(max_tuple)
                orderedString += f"  {max_tuple[0]}:{max_tuple[1]}"
            print(orderedString)            
            

            w_file.write(orderedString+ "\n")



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
