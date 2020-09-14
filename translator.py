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
                    data[0] = 'あ２'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.2543255962":
                    data[0] = 'い２'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.1910529223":
                    data[0] = 'う２'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.992104086":
                    data[0] = 'え２'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.3251480092":
                    data[0] = 'お２'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.2286178617":
                    data[0] = '笑顔'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.631788340":
                    data[0] = 'まばたき'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.226821586":
                    data[0] = '泣き'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.146247590":
                    data[0] = 'への字'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.456140828":
                    data[0] = '上ぎ見る'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.2813365169":
                    data[0] = '下を見て'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.3240688866":
                    data[0] = '左を見て'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.3105640497":
                    data[0] = '右を見て'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.2585484937":
                    data[0] = 'きみ'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.3464135367":
                    data[0] = '笑い'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.1400781561":
                    data[0] = 'ウィンク'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.2842757018":
                    data[0] = 'ウィンク右'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.1948989295":
                    data[0] = 'にこり'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.890025586":
                    data[0] = '困る'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.463008637":
                    data[0] = '困る２'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                elif expression == "blendShape.3360470953":
                    data[0] = 'にこり２'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
                else:
                    output.write(f'{data[0]},{data[1]},{data[2]}')