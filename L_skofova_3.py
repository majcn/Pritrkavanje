data = {
    'title': 'Skofova na 3 zvonove (leteca)',
    'song': [
        'x - - - - - x - - - - - x - - - - - x - - - - -',
        '- - x - x - - - x x - x - x - x - x - x - - x -',
        '- x - x - x - x - - x - - - x - x - - - x x - x'
    ],
    'bpm': 120,
    'timeSignature': '3/4'
}

from prog import BellMusicCreator

exportFile = __file__.replace('.py', '') + '.xml'
# BellMusicCreator().show(data)
BellMusicCreator().write(data, fp=exportFile)
