# -*- coding: utf-8 -*-
import argparse
import os


def parse_commandline():
    '''
    Parse inputs from command line.

    Returns
    -------
    args
        arguments to give to the functions
    '''
    description = '''
    ----------------------------------------------------
    ____  _____                                        
   |___ \|  __ \                                       
     __) | |  | |_ __ ___   __ _ _ __  _ __   ___ _ __ 
    |__ <| |  | | '_ ` _ \ / _` | '_ \| '_ \ / _ \ '__|
    ___) | |__| | | | | | | (_| | |_) | |_) |  __/ |   
   |____/|_____/|_| |_| |_|\__,_| .__/| .__/ \___|_|   
                                | |   | |              
                                |_|   |_|              
    ----------------------------------------------------
    '''

    epilog = '''
          -----------------------------------
         |  >>>Publication link<<<<<         |
         |  victoria.ruiz.serra@gmail.com    |
          -----------------------------------
        '''
    # innit parser
    parser = argparse.ArgumentParser(epilog=epilog,
                                     formatter_class=argparse.RawDescriptionHelpFormatter, description=description)
    # vcf file
    annovar_group = parser.add_mutually_exclusive_group(required=True)
    annovar_group.add_argument('-vf', '--varfile', nargs='+', metavar="<String>", dest="vf",
                               help='input directory containing single or \
                                    multiple annotated variants files is VCF or VEP format')
    annovar_group.add_argument("-maf", '--maf_file', nargs='+', metavar="<String>", dest="maf",
                               help="annotated variant file in MAF format.")
    annovar_group.add_argument("-varmap", action='store_true', dest="varmap",
                               help="use ClinVar db of annotated variants",
                               default="varmap")
    # force orverwrite files
    parser.add_argument('-f', "--force", dest="force", action='store_true',
                        help="force to owerwrite? (y/n)", default=False)
    # create default output directory
    parser.add_argument('-o', "--out", metavar="<String>", dest="out",
                        help="output directory")
    parser.set_defaults(out=".")
    # create default output directory
    parser.add_argument('-p', "--parallel", dest="parallel", action='store_true',
                        default=False,
                        help="Speed up running time. Depends on GNU Parallel. \
                        O. Tange(2011): GNU Parallel - The Command-Line Power Tool, \
                        login: The USENIX Magazine, February 2011: 42-47.")
    # store arguments into variable
    args = parser.parse_args()
    # clean up (recommended)
    del(parser)

    return args
