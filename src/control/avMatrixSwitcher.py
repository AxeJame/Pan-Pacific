# Python imports

# Extron Library imports

# Project imports

# Define UI Objects
from devices import devTLPList

# Define UI Objects
from library.devControl import devControl_class

# Define UI Object Events

# dev: Matrix switcher

# Input AV source
IDInputAVsource = {
    'Input1'   : 8501,
    'Input2'   : 8502,
    'Input3'   : 8503,
    'Input4'   : 8504,
    'Input5'   : 8505,
    'Input6'   : 8506
}

# Output video source
IDOutputViSource = {
    'ViOutput1'   : 8511,
    'ViOutput2'   : 8512,
    'ViOutput3'   : 8513,
    'ViOutput4'   : 8514,
    'ViOutput5'   : 8515,
    'ViOutput6'   : 8516,
    'ViOutput7'   : 8517,
    'ViOutput8'   : 8518
}

# Output Audio source
IDOutputAuSource = {
    'AuOutput1'   : 8518,
    'AuOutput2'   : 8519
}
# take button
IDbtnTake = 8500
# Select a Input to show current routing
for i in range(2):
    devControl_class.SelecteIOAVSource(i, devTLPList[i], IDInputAVsource, IDOutputAuSource, IDOutputViSource, mode = None)
    devControl_class.takeAction(i, devTLPList[i], IDbtnTake, IDInputAVsource, IDOutputAuSource, IDOutputViSource)
# Select outputs and press take button to switch
