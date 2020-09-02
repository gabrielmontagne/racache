from argparse import ArgumentParser
from collections import OrderedDict
from csv import DictReader
from io import StringIO
from os.path import abspath, isfile
from shlex import split
from subprocess import check_output

alphaToPrestonBlair = {
    'A': 'MBP',
    'B': 'etc',
    'C': 'E',
    'D': 'AI',
    'E': 'O',
    'F': 'U',
    'G': 'FV',
    'H': 'L',
    'X': 'rest'
}

def main():
    parser = ArgumentParser(prog='Racache')
    parser.add_argument('input')
    parser.add_argument('-o', default=None)
    parser.add_argument('-fps', default=10, type=float)
    args = parser.parse_args()
    full_path = abspath(args.input)
    assert isfile(full_path), 'Input file cannot be found'
    out = check_output(split(f'rhubarb {full_path}')).decode('utf8')
    fields = DictReader(StringIO(out), dialect='excel-tab', fieldnames=('time', 'viseme'))
    frames = OrderedDict([(round(float(f['time']) * args.fps), alphaToPrestonBlair.get(f['viseme'])) for f in fields])
    output = args.o or f'{args.input}.dat'
    with open(output, 'w') as o:
        o.write('OkaLoka\n')
        for f in frames:
            o.write(f'{f} {frames.get(f)}\n')

if __name__ == '__main__':
    main()
