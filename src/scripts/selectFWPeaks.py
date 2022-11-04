# File Name: selectFWPeaks.py
# Created By: ZW
# Created On: 2022-11-02
# Purpose: postprocessing script for ATAC-Seq data that selects the most 
#    representative set of non-overlapping, fixed-width peaks by peak score

# Module imports
# ----------------------------------------------------------------------------
from argparse import ArgumentParser
from bedtools.


# Main Execution Block
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    # setup commandline parser 
    descr  = """
     Postprocessing script for ATAC-Seq data that selects the most 
     representative set of non-overlapping, fixed-width peaks by peak score
    """
    parser = ArgumentParser(description=descr)
    parser.add_argument("output_bed", metavar="OUTPUT", type=str,
            help="output file destination (BED6) for selected peaks")
    parser.add_argument("input_peaks", metavar="IN_PEAKS", type=str, nargs='+', 
            help="input peaks files to select (.bed or .narrowPeak)")  
    args = parser.parse_args()
    
    # sort narrow peaks input files
    # ------------------------------------------------------------------------
    sorted_inputs = []
    for input in args.input_peaks:
        sorted_inputs.append(pybed.BedTool(input).sort())






