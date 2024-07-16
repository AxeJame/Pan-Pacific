# Extron Library imports
from extronlib.system import MESet, Wait
from extronlib.ui import Button, Label
from extronlib import event
# Project imports
from modules.helper.ModuleSupport import eventEx
from extronlib.device import ProcessorDevice, UIDevice
import variables as var


# from ui.tlpStart import IDStartPageDict

class devControl_class:
    #=Ref======================================================

    #=================================================================
    def SelecteIOAVSource(ID: int, TLP: UIDevice, IDInputAVsource: dict, IDOutputAuSource: dict, IDOutputViSource: dict , mode :str):
        UIhost = TLP
        btnInputAVsourceGroup=[]
        btnInputAVsourceGroupDict={}
        for i in IDInputAVsource:
            btnTempo = Button(UIhost, IDInputAVsource.get(i))
            btnInputAVsourceGroup.append(btnTempo)
            btnInputAVsourceGroupDict[btnTempo]=i

        # TLP: Select Output AV Source
        btnInputAVsourceGroup= MESet(btnInputAVsourceGroup)
        @eventEx(btnInputAVsourceGroup.Objects, 'Pressed')
        def btnInputAVsourceGroupPressed(button: Button, state: str):
            # print(button.Name, state)
            btnInputAVsourceGroup.SetCurrent(button)
            var.InputCurrentSelected = btnInputAVsourceGroupDict.get(button)
            print('TLP {}: Current input:{}'.format(ID, var.InputCurrentSelected))  # show TLP : Input Current Selected
            devControl_class.SelecteOutputAuSource(ID, TLP, IDOutputAuSource, mode = 'viewCurrent')
            devControl_class.SelecteOutputViSource(ID, TLP, IDOutputViSource, mode = 'viewCurrent')

        # Reset button when press Take button
        if mode == 'reset':
            btnInputAVsourceGroup.SetCurrent(None)
            print('Reset Input source .......')
            devControl_class.SelecteOutputAuSource(ID, TLP, IDOutputAuSource, mode = 'reset')
            devControl_class.SelecteOutputViSource(ID, TLP, IDOutputViSource, mode = 'reset')
            print('Reset AV source: done')


           

    #=================================================================

    def SelecteOutputAuSource(ID: int, TLP: UIDevice, IDOutputAuSource: dict, mode: str):
        # Selecte Output Au Source mode: mode = None : normal; mode = reset : reset to state(0); mode = viewCurrent : ViewViCurrentStream
        UIhost = TLP
        btnOnputAusourceGroup=[]
        btnOnputAusourceGroupDict={}
        btnOnputAuCurrentGroupDict={}
        for i in IDOutputAuSource:
            btnTempo = Button(UIhost, IDOutputAuSource.get(i))
            btnOnputAusourceGroup.append(btnTempo)
            btnOnputAusourceGroupDict[btnTempo]=i
            btnOnputAuCurrentGroupDict[i] = btnTempo
        @eventEx(btnOnputAusourceGroup, 'Pressed')
        def btnOnputAusourceGroupPressed(button: Button, state: str):
            # print(button.Name, button.State)
            if button.State == 0:
                button.SetState(1)
                # Output selected
                var.OutputAuSelected[btnOnputAusourceGroupDict.get(button)] = 'selected'
                print('{}: selected'.format(btnOnputAusourceGroupDict.get(button)))
            else:
                button.SetState(0)
                # Output deselected
                var.OutputAuSelected[btnOnputAusourceGroupDict.get(button)] = 'deselected'
                print('{}: selected'.format(btnOnputAusourceGroupDict.get(button)))
       
        # ==Function Reset =========================================
        def resetAubtn(btn: Button):
                btn.SetState(0)
        def resetAu():
            # reset Output Au Selected button  
            for i in range(len(btnOnputAusourceGroup)):
                resetAubtn(btnOnputAusourceGroup[i])
            # reset Output Au Selected variable   
            for i in btnOnputAusourceGroupDict:
                var.OutputAuSelected[btnOnputAusourceGroupDict[i]] = 'deselected'
            print('Clear output Audio button')
        # ==Function Reset close =========================================
        if mode == 'reset':
            resetAu()
        #  mode = viewCurrent 
        if (mode == 'viewCurrent'):
            resetAu()
            print('Mode viewCurrent:')
            for i in IDOutputAuSource:                
                if (i in var.ViewAuCurrentStream[var.InputCurrentSelected]):
                    btnOnputAuCurrentGroupDict[i].SetState(1)
                    var.OutputAuSelected[i] = 'selected'
                    # ----->Troubleshooting code :
                    # print('Input current: {} - Output current : {}'.format(var.InputCurrentSelected, i))
                    # print(i,': selected')
            print('ViewAuCurrentStream[{}]:{}'.format(var.InputCurrentSelected,var.ViewAuCurrentStream[var.InputCurrentSelected]))
            print('==================================================')


    #=================================================================

    def SelecteOutputViSource(ID: int, TLP: UIDevice, IDOutputViSource: dict, mode: str):
        # Selecte Output Vi Source mode: mode = None : normal; mode = reset : reset to state(0); mode = viewCurrent : ViewViCurrentStream
        UIhost = TLP
        btnOnputVisourceGroup=[]
        btnOnputVisourceGroupDict={}
        btnOnputViCurrentGroupDict={}
        for i in IDOutputViSource:
            btnTempo = Button(UIhost, IDOutputViSource.get(i))
            btnOnputVisourceGroup.append(btnTempo)
            btnOnputVisourceGroupDict[btnTempo]=i
            btnOnputViCurrentGroupDict[i] = btnTempo
        @eventEx(btnOnputVisourceGroup, 'Pressed')
        def btnOnputVisourceGroupPressed(button: Button, state: str):
            # print(button.Name, state)
            if button.State == 0:
                button.SetState(1)
                # Output selected
                var.OutputViSelected[btnOnputVisourceGroupDict.get(button)] = 'selected'
                print('{}: selected'.format(btnOnputVisourceGroupDict.get(button)))
            else:
                button.SetState(0)
                # Output deselected
                var.OutputViSelected[btnOnputVisourceGroupDict.get(button)] = 'deselected'
                print('{}: deselected'.format(btnOnputVisourceGroupDict.get(button)))
       
        # ==Function Reset =========================================
        def resetVibtn(btn: Button):
                btn.SetState(0)
        def resetVi():
            # reset Output Vi Selected button  
            for i in range(len(btnOnputVisourceGroup)):
                resetVibtn(btnOnputVisourceGroup[i])
            # reset Output Vi Selected variable   
            for i in btnOnputVisourceGroupDict:
                var.OutputViSelected[btnOnputVisourceGroupDict[i]] = 'deselected'
            print('Clear output Video button')
        # ==Function Reset close =========================================

        if mode == 'reset':
            resetVi()
        #  mode = viewCurrent 
        if (mode == 'viewCurrent'):
            resetVi()
            print('Mode viewCurrent:')
            for i in IDOutputViSource:                
                if (i in var.ViewViCurrentStream[var.InputCurrentSelected]):
                    btnOnputViCurrentGroupDict[i].SetState(1)
                    var.OutputViSelected[i] = 'selected'
                    # ----->Troubleshooting code :
                    # print('Input current: {} - Output current : {}'.format(var.InputCurrentSelected, i))
                    # print(i,': selected')
            print('ViewViCurrentStream[{}]:{}'.format(var.InputCurrentSelected,var.ViewViCurrentStream[var.InputCurrentSelected]))
            print('==================================================')
        
    #=================================================================
    def takeAction(ID: int, TLP: UIDevice, IDbtnTake: int, IDInputAVsource: dict, IDOutputAuSource: dict, IDOutputViSource: dict):
        UIhost = TLP
        btnTake = Button(UIhost, IDbtnTake)
        @eventEx(btnTake, 'Pressed')
        def btnTakePressed(button: Button, state: str):
            print(button.Name, state)
            
            #Routing Audio
            if var.InputCurrentSelected not in var.ViewAuCurrentStream:
                var.ViewAuCurrentStream[var.InputCurrentSelected] = []
            for i in var.OutputAuSelected:
                # ----->Troubleshooting code :
                # print('{}:{}'.format(i,var.OutputViSelected.get(i)))
                if var.OutputAuSelected.get(i) == 'selected':
                    for j in var.ViewAuCurrentStream:
                        if (j != var.InputCurrentSelected) and (i in var.ViewAuCurrentStream[j]):
                            print('CurrentStream[ {} ] : remove : {}'.format(j, i))
                            var.ViewAuCurrentStream[j].remove(i)
                    if i not in var.ViewAuCurrentStream[var.InputCurrentSelected]:
                        var.ViewAuCurrentStream[var.InputCurrentSelected].append(i)
                        print('CurrentStream[ {} ] : append : {}'.format(var.InputCurrentSelected, i))
                if var.OutputAuSelected.get(i) == 'deselected':
                    if i in var.ViewAuCurrentStream[var.InputCurrentSelected]:
                        var.ViewAuCurrentStream[var.InputCurrentSelected].remove(i)
                        print('CurrentStream[ {} ] : remove : {}'.format(var.InputCurrentSelected, i))
                        # ----->Troubleshooting code :
                        # print('CurrentStream {} : deselected : {}'.format(var.InputCurrentSelected, i))
            print('ViewAuCurrentStream[{}]:{}'.format(var.InputCurrentSelected,var.ViewAuCurrentStream[var.InputCurrentSelected]))
            #Routing Video
            if var.InputCurrentSelected not in var.ViewViCurrentStream:
                var.ViewViCurrentStream[var.InputCurrentSelected] = []
            for i in var.OutputViSelected:
                # ----->Troubleshooting code :
                # print('{}:{}'.format(i,var.OutputViSelected.get(i)))
                if var.OutputViSelected.get(i) == 'selected':
                    for j in var.ViewViCurrentStream:
                        if (j != var.InputCurrentSelected) and (i in var.ViewViCurrentStream[j]):
                            print('CurrentStream[ {} ] : remove : {}'.format(j, i))
                            var.ViewViCurrentStream[j].remove(i)
                    if i not in var.ViewViCurrentStream[var.InputCurrentSelected]:
                        var.ViewViCurrentStream[var.InputCurrentSelected].append(i)
                        print('CurrentStream[ {} ] : append : {}'.format(var.InputCurrentSelected, i))
                if var.OutputViSelected.get(i) == 'deselected':
                    if i in var.ViewViCurrentStream[var.InputCurrentSelected]:
                        var.ViewViCurrentStream[var.InputCurrentSelected].remove(i)
                        print('CurrentStream[ {} ] : remove : {}'.format(var.InputCurrentSelected, i))
                        # ----->Troubleshooting code :
                        # print('CurrentStream {} : deselected : {}'.format(var.InputCurrentSelected, i))
            print('ViewViCurrentStream[{}]:{}'.format(var.InputCurrentSelected,var.ViewViCurrentStream[var.InputCurrentSelected]))
            # remove information and temporaty variable in once
               
            devControl_class.SelecteIOAVSource(ID, TLP, IDInputAVsource, IDOutputAuSource, IDOutputViSource, mode = 'reset')
            



    