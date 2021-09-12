#In the name of God
#!use/bin/env python
# -*- coding: utf-8 -*-

from music21 import *
from Database.PostGet import *

def Importfile(thisfile):
    score = converter.Converter().subconvertersList('input')
    c = converter.parse(thisfile)

    nmeasur = len(c.measureOffsetMap())
    nparts = len(c.parts)
    s_c_d = {}
    fdata = {}
    #print(nmeasur,nparts)
    for m in range(int(nmeasur)):
        for p in range(int(nparts)):
            #print(c.parts[p])
            #print(c.parts[p].measure(m))
            if c.parts[p].measure(m) != None:
                elm = c.parts[p].measure(m).elements
                fdata[(m,c.parts[p])]= elm
                if m == 0:
                    #print(c.parts[p].partName)
                    #print(elm)
                    apndlst = []
                    frstnts = []
                    for e in elm:
                        if isinstance(e,layout.PageLayout):
                            apndlst.append((e.pageNumber,e.rightMargin,e.leftMargin))
                        if isinstance(e,clef.TrebleClef):
                            apndlst.append((e.name,e.line,e.sign))
                        if isinstance(e,key.KeySignature):
                            apndlst.append((e,e.mode,e.sharps))
                        if isinstance(e,meter.TimeSignature):
                            apndlst.append((e.ratioString))
                #s_c_d[c.parts[p].partName]=[(elm[0].name,elm[0].line,elm[0].sign),
                #                            (elm[1],elm[1].mode,elm[1].sharps), #elm[1].tonic elm[1].pitchFromDegree(5) elm[1].pitches
                #                            (elm[2].ratioString)] #elm[2].displaySequence.partitionDisplay
                        if isinstance(e,note.Note):
                            frstnts.append(e)
                        #s_c_d[m] = [elm[i]  for i in range(3,len(elm))]
                    s_c_d[c.parts[p].partName]=apndlst
                    s_c_d[(m,p)] = frstnts
                else:
                    s_c_d[(m,p)] = [elm[i]  for i in range(len(elm))]
    #print(s_c_d)
    return s_c_d,fdata
                
                
        
        



'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
  '__weakref__', '_getStream', '_setStream', 'canBePickled', 'checkShowAbility', 'codecWrite', 'getExtensionForSubformats',
   'getTemporaryFile', 'launch', 'launchKey', 'parseData', 'parseFile', 'readBinary', 'registerFormats',
    'registerInputExtensions', 'registerOutputExtensions', 'registerOutputSubformatExtensions', 
    'registerShowFormats', 'show', 'stream', 'stringEncoding', 'write', 'writeDataStream']

    ['_DOC_ATTR', '_DOC_ORDER', '__annotations__', '__class__', '__deepcopy__', '__delattr__', '__dict__', '__dir__', '__doc__',
    '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
    '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__',
    '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_activeSite', '_activeSiteStoredOffset', '_cache',
    '_classListFullyQualifiedCacheDict', '_classSetCacheDict', '_classTupleCacheDict', '_deepcopySubclassable', '_derivation',
    '_duration', '_editorial', '_getActiveSite', '_getBarDuration', '_getBeatCount', '_getDenominator', '_getDuration', '_getMeasureOffset',
    '_getNumerator', '_getOffset', '_getPriority', '_getSeconds', '_getTimeSignatureForBeat', '_naiveOffset', '_overriddenBarDuration',
    '_priority', '_reprInternal', '_reprText', '_reprTextLine', '_setActiveSite', '_setBarDuration', '_setBeatCount', '_setDefaultAccentWeights',
    '_setDefaultBeamPartitions', '_setDefaultBeatPartitions', '_setDenominator', '_setDuration', '_setNumerator', '_setOffset', '_setPriority',
    '_setSeconds', '_style', '_styleClass', 'accentSequence', 'activeSite', 'averageBeatStrength', 'barDuration', 'beamSequence', 'beat',
    'beatCount', 'beatCountName', 'beatDivisionCount', 'beatDivisionCountName', 'beatDivisionDurations', 'beatDuration',
    'beatLengthToQuarterLengthRatio', 'beatSequence', 'beatStr', 'beatStrength', 'beatSubDivisionDurations', 'classSet', 'classSortOrder', 'classes',
    'classification', 'clearCache', 'containerHierarchy', 'contextSites', 'denominator', 'derivation', 'displaySequence', 'duration', 'editorial',
    'getAccent', 'getAccentWeight', 'getAllContextsByClass', 'getBeams', 'getBeat', 'getBeatDepth', 'getBeatDuration', 'getBeatOffsets',
    'getBeatProgress', 'getBeatProportion', 'getBeatProportionStr', 'getContextByClass', 'getMeasureOffsetOrMeterModulusOffset', 'getOffsetBySite',
    'getOffsetFromBeat', 'getOffsetInHierarchy', 'getSpannerSites', 'groups', 'hasEditorialInformation', 'hasStyleInformation', 'id', 'informSites',
    'isClassOrSubclass', 'isStream', 'load', 'loadRatio', 'measureNumber', 'mergeAttributes', 'next', 'numerator', 'offset', 'previous', 'priority',
    'purgeLocations', 'purgeOrphans', 'quarterLength', 'quarterLengthToBeatLengthRatio', 'ratioEqual', 'ratioString', 'resetValues', 'seconds',
    'setAccentWeight', 'setDisplay', 'setOffsetBySite', 'show', 'sites', 'sortTuple', 'splitAtDurations', 'splitAtQuarterLength',
    'splitByQuarterLengths', 'style', 'summedNumerator', 'symbol', 'symbolizeDenominator', 'write']
'''
