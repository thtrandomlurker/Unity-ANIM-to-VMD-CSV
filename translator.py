from sys import argv

with open(argv[1], 'r', encoding='UTF-8') as input:
    with open(argv[2], 'w', encoding='Shift-JIS') as output:
        for line in input:
            data = line.split(',')
            if len(data) == 3: #which it always is
                expression = data[0]
                if expression == "blendShape.1147791917":
                    data[0] = 'あ'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.1253204511":
                    data[0] = 'い'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.1588805200":
                    data[0] = 'う'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.1124347444":
                    data[0] = 'え'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.2748434218":
                    data[0] = 'お'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.1598983058":
                    data[0] = 'あ'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.2543255962":
                    data[0] = 'い'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.1910529223":
                    data[0] = 'う'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.992104086":
                    data[0] = 'え'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.3251480092":
                    data[0] = 'お'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.2286178617":
                    data[0] = '笑い'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.631788340":
                    data[0] = 'まばたき'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.226821586":
                    data[0] = '泣き'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.BS_eye.1400781561":
                    data[0] = 'ウィンク左'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.2842757018":
                    data[0] = 'ウィンク右'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                else:
                    output.write(f'{data[0]},{data[1]},{data[2]}')