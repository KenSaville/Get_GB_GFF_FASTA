"""
Get Genbank file, convert to GFF format, fasta
"""

import subprocess
from pathlib import Path

from latch import small_task, workflow
from latch.types import LatchFile

@small_task
def get_gb_file(ACC: str)  -> LatchFile:

    # A reference to our output.
    gb_file = Path(ACC + ".gb").resolve()

    cmd = ["bio", "fetch", ACC]
    
    with open (ACC + ".gb", "w") as f:
        subprocess.run(cmd, stdout=f)

    return LatchFile(str(gb_file), "latch:///" + ACC + ".gb")

@small_task
def gb_to_gff(ACC:str, gb_file:LatchFile) -> LatchFile:

    gff_file = Path(ACC + ".gff").resolve()
    
    gff_cmd = ["bio", "gff", gb_file]

    with open(gff_file, "w") as f:
        subprocess.run(gff_cmd, stdout=f)

    return LatchFile(str(gff_file), "latch:///" + ACC + ".gff")

@small_task   
def gb_to_fasta(ACC:str, gb_file:LatchFile) -> LatchFile:
    fasta_file = Path(ACC + ".fasta").resolve()
    
    fasta_cmd = ["bio", "fasta", gb_file]
    
    with open(fasta_file, "w") as f:
        subprocess.run(fasta_cmd, stdout=f)
        
    return LatchFile(str(fasta_file), "latch:///" + ACC + ".fasta")
        
       
@workflow
def file_converter(ACC:str) -> (LatchFile, LatchFile, LatchFile):
    """input a genbank accession number, return gb file, gff file, fasta file.  Which can then be used to load into IGV for visualization

    Get_GB_GFF_FASTA
    ----

    
    Get_GB_GFF_FASTA takes a genbank accession number and returns the genbank file, a GFF file, and a Fasta file.  
    The GFF and Fasta can be downloaded and loaded into IGV for visualization.

    * The code used to fetch the various files types is modified from the Biostar Hanbook (by Istvan Albert).
    * In particular the "bio" suite of tools developed for that habdbook.

    __metadata__:
        display_name: genbank to GFF be converted 
        author:
            name:  Ken Saville
            email: ksaville@albion.edu
            github:
        repository:
        license:
            id: MIT

    Args:

        ACC:
          Accession number to file to be converted (test = NC_045512)

          __metadata__:
            display_name: ACC

    """
    gb_file = get_gb_file(ACC=ACC)
    return get_gb_file(ACC=ACC), gb_to_gff(ACC=ACC, gb_file=gb_file), gb_to_fasta(ACC=ACC, gb_file=gb_file)

