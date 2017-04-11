from music21 import clef, key, stream, metadata, meter, tempo, note, bar, instrument

class BellMusicCreator:

    __bells = [
        (clef.BassClef(),   key.KeySignature(5), 'A#3'),
        (clef.BassClef(),   key.KeySignature(5), 'C#4'),
        (clef.TrebleClef(), key.KeySignature(5), 'E4' ),
        (clef.TrebleClef(), key.KeySignature(5), 'F#4'),
    ]

    def __getInstrument(self):
        i = instrument.Instrument()
        i.instrumentName = ""
        i.instrumentAbbreviation = ""
        i.midiProgram = 14

        return i # instrument.ChurchBells()

    def __getNote(self, n, t):
        return {
            'x': note.Note(n, type='eighth'),
            '-': note.Rest(n, type='eighth')
        }.get(t, None)

    def __generate(self, data):
        output = stream.Score([metadata.Metadata(title=data['title'], composer='')])
        for i in range(len(data['song'])):
            clef, keySignature, noteType = self.__bells[i]
            songPart = data['song'][i]
            timeSignature = data['timeSignature']
            bpm = data['bpm']

            streamPart = stream.Part([clef, keySignature, meter.TimeSignature(timeSignature), tempo.MetronomeMark(number=bpm)])

            streamPart.append(filter(None, map(lambda x: self.__getNote(noteType, x), songPart)))
            streamPart.makeMeasures(inPlace=True, finalBarline=bar.Repeat(direction='end', times=5))
            streamPart.measure(1).leftBarline = bar.Repeat(direction='start')


            streamPart.insert(0, self.__getInstrument())

            output.insert(0, streamPart)

        return output

    def show(self, data):
        self.__generate(data).show()

    def write(self, data, fp=None):
        self.__generate(data).write(fp=fp)
