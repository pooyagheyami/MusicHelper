#In the name of God
#!use/bin/env python
# -*- coding: utf-8 -*-

from music21 import *
from Database.PostGet import *


def xml2dbwrite(xmlfile, dbfile):
    score = converter.parse(xmlfile)
    nmeasur = len(score.measureOffsetMap())
    print(nmeasur,type(nmeasur))
    nparts = len(score.parts)
    txt = ''
    scr = {}
    msr = []
    nts = []
    for p in range(nparts):
        txt += 'Part %d\n\t'%p
        for m in range(int(nmeasur)):
            txt += '|'
            msr.append(score.parts[p].measure(m).pitches)
            elm = score.parts[p].measure(m).elements
            nnts = len(elm)
            #print(nnts)
            for n in range(nnts):
                if isinstance(elm[n],note.Note):
                    mdnt = elm[n].pitches[0].midi
                    #nt = score.parts[p].measure(m).pitches[n].midi
                    #nts.append(nt)
                    nts.append(mdnt)
                    txt += elm[n].nameWithOctave+':'+str(elm[n].duration.quarterLength)+','
            txt += ' '
        txt += '\n'    
        scr['part'+str(p)] = msr
    print(nts)    
    return txt,scr

    #get = Get(dbfile,'','')
    
    
