from sys import argv

frame_count = int(0)

with open(argv[1], 'r', encoding='Shift-JIS') as input:
    with open(f'{argv[1][:-4]}_fixed.csv', 'w', encoding='Shift-JIS') as output:
        get_len = input.readlines()
        frame_count = int(len(get_len))
        
with open(argv[1], 'r', encoding='Shift-JIS') as input:
    with open(f'{argv[1][:-4]}_fixed.csv', 'w', encoding='Shift-JIS') as output:
        output.write('Vocaloid Motion Data 0002,0\n')
        output.write(f'{argv[1][:-4]}\n')
        output.write('0\n')
        output.write(f'{frame_count}\n')
        for line in input:
            d = line.split(',')
            n = d[0]
            f = d[1]
            v = d[2]
            if v == '-0.001\n':
                v = '1\n'
                output.write(f'{n},{f},{v}')
            elif v != '-0.001\n':
                output.write(line)
            
        output.write('0\n')
        