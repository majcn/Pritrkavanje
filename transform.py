title         = 'Skofova'
bpm           = '120'
timeSignature = '3/4'
input         = '122 123 133 132'

result = [''] * max(map(int, input.replace(' ', '')))
for i in input:
    for ir in range(len(result)):
        if i == ' ':
            result[ir] += '    '
        else:
            result[ir] += 'x ' if int(i) == (ir + 1) else '- '


template =  '''data = {
    'title': '%TITLE%',
    'song': [
        %SONG%
    ],
    'bpm': '%BPM%',
    'timeSignature': '%TIME_SIGNATURE%'
}

from prog import BellMusicCreator

exportFile = __file__.replace('.py', '') + '.xml'
# BellMusicCreator().show(data)
BellMusicCreator().write(data, fp=exportFile)'''

print template.replace('%TITLE%', title).replace('%BPM%', bpm).replace('%TIME_SIGNATURE%', timeSignature).replace('%SONG%', '\'' + '\',\n        \''.join(result) + '\'')
