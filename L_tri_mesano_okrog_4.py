data = {
    'title': 'Tri leteca (gostimo na 2)',
    'song': [
        'x - - - - - - -',
        '- x - - - x - -',
        '- - x - x - x -',
        '- - - x - - - x'
    ],
    'bpm': 120,
    'timeSignature': '4/4'
}

from prog import BellMusicCreator

exportFile = __file__.replace('.py', '') + '.xml'
# BellMusicCreator().show(data)
BellMusicCreator().write(data, fp=exportFile)
