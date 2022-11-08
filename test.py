import argparse
parser = argparse.ArgumentParser(description='SVDA')
parser.add_argument('--adamix', action="store_true", default=False)

args = parser.parse_args()

print(args.adamix)
