data = {
    'title': 'Radetski na 3 zvonove',
    'song': [
        '- - - - - - - - - - - - x - x -     - - - - - - - - - - - - x - x -     - - - - - - - - - - - - x - x -     - - - - x - x - - - - - x - x -     - - x - - - x - - - x - - - x - - - x - - - x - - - x - - - x - - - - - - - - - x - x - x - - -',
        '- x - - - x - - - x - - - x - -     - x - - - x - - - x - - - x - -     - x - - - x - - - x - - - x - -     - x - - - x - - - x - - - x - -     - - - - x - - - - - - - x - - - - - - - x - - - - - - - x - - - - - - - x - x - - x - x - - - -',
        'x - x - x - x - x - x - - - - -     x - x - x - x - x - x - - - - -     x - x - x - x - x - x - - - - -     x - x - - - - - x - x - - - - -     x - - - - - - - x - - - - - - - x - - - - - - - x - - - - - - - x - x - - - - - - - - - - - - -'
    ],
    'bpm': 180,
    'timeSignature': '4/4'
}

from prog import BellMusicCreator

exportFile = __file__.replace('.py', '') + '.xml'
# BellMusicCreator().show(data)
BellMusicCreator().write(data, fp=exportFile)
