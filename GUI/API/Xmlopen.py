#In the name of God
#!use/bin/env python
# -*- coding: utf-8 -*-

from music21 import *
from Database.PostGet import *


def xml2dbwrite(xmlfile, dbfile):
    score = converter.parse(xmlfile)
    nmeasur = len(score.measureOffsetMap())
    #print(nmeasur,type(nmeasur))
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
    #print(nts)
    return txt,scr

    #get = Get(dbfile,'','')
    
    
def xml2dbf2(xmlfile, dbfile):
    MyData = Post(u'Main.db',u'ScoreInfo',u'',u'')
    score = converter.parse(xmlfile)
    nmeasur = len(score.measureOffsetMap())
    nparts = len(score.parts)
    imsur = {}
    ipart = {}
    ints  = []
    prnot = 0
    nxnot = 0
    disSp = 0
    disAt = 0
    disTn = 0
    disBs = 0
    for m in range(int(nmeasur)):
        for p in range(nparts):
            if m == 0:
                elm = score.parts[p].measure(0).elements

                MyData.Tabel = u'ScoreInfo'
                MyData.Field = u'id, Celf, KeySig, TimeSig, NPartSys, NMasurSys'
                iData = [score.id,elm[0].name,elm[1].name,str(elm[2].numerator)+'/'+str(elm[2].denominator),p,int(nmeasur)]
                print(iData)
                MyData.Data = iData
                MyData.Addrecord()
                for n in range(3,len(elm)):
                    if isinstance(elm[n], note.Note):
                        MyData.Tabel = u'MScore'
                        MyData.Field = u'id, NoteName, Npart, Nmesur, Nnote, Ndur'
                        nData = [score.id, elm[n].nameWithOctave, p, m, elm[n].pitches[0].midi, elm[n].duration.quarterLength ]
                        MyData.Data = nData
                        MyData.Addrecord()

            else:
                ptchs  = score.parts[p].measure(m).pitches
                elm = score.parts[p].measure(m).elements
                nnts = len(elm)
                for n in range(nnts):
                    if isinstance(elm[n], note.Note):
                        mdnt = elm[n].pitches[0].midi
                        thsdu = elm[n].duration.quarterLength
                        MyData.Tabel = u'MScore'
                        MyData.Field = u'id, NoteName, Npart, Nmesur, Nnote, Ndur'
                        nData = [score.id, elm[n].nameWithOctave, p, m, elm[n].pitches[0].midi,
                                 elm[n].duration.quarterLength]
                        MyData.Data = nData
                        MyData.Addrecord()





