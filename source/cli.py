import argparse,textwrap
# Parser setup
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent("""\
    My little script
    ----------------
    This utility counts the number of lines in a text file.
    """)
)
parser.add_argument('src',help="Input File")
parser.add_argument('-v',help="Verbose",action='store_true')
args = vars(parser.parse_args())
# Use arguments...
if args["v"]:
    print(f"Processing {args['src']}...")
