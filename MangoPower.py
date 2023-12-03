FILENAME = 'bin.txt'

with open(FILENAME, 'r') as f:
    lines = f.readlines()
outputs = []

total_watts_consumed = 0


for line in lines:
    if line.startswith('Combined Power (CPU + GPU + ANE):'):
        parts = line.split(': ')
        if len(parts) != 2:
            print('WARN, found invalid line: ', line)
        else:
            res = parts[1].strip()
            if res.endswith('mW'):
                total_watts_consumed += int(res.split(' ')[0])
            outputs.append(parts[1])

for x in outputs: print(x)

print (f'Totally consumed {total_watts_consumed} mW')
