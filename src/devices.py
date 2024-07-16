"""
This is the place to define each of the devices in the system.
* Extron control devices (e.g. all extronlib.device objects)
* Non-control devices and services (e.g. device modules)
* User defined devices (e.g. all extronlib.interface objects or custom python coded devices)

Note: This is for definition only.  Connection and logic defined in system.py (see below).
"""

# Python imports

# Extron Library imports
from extronlib.device import ProcessorDevice, UIDevice
# Project imports

# Define devices

## define Processor & Touch panel

devIPCP = ProcessorDevice('ProcessorAlias')     # IPCP test
# devIPCP = ProcessorDevice('ProcessorAlias')       # IPCP main

devTLP = UIDevice('PanelAliasWeb')
devIpad1 = UIDevice('PanelAlias_01')
devIpad2 = UIDevice('PanelAlias_02')

devTLPList = [devTLP, devIpad1, devIpad2]
