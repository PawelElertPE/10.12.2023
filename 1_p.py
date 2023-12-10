import argparse

parser = argparse.ArgumentParser()

parser.add_argument('filename')
parser.add_argument(*name_or_flags: '-m', '--mode')


args = parser.parse_args()

print(f'Nazwa pliku to: {args.filename}')
print(f'Tryb to: {args.mode}')

with open(args.filename, 'r') as file1:
    content = file1.read()





