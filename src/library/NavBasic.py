# Extron Library imports
from extronlib.system import MESet, Wait
from extronlib.ui import Button, Label
# Project imports
from modules.helper.ModuleSupport import eventEx
from extronlib.device import ProcessorDevice, UIDevice
import variables as var

# from ui.tlpStart import IDStartPageDict

class TLP_class:
    #=Ref======================================================

    #=================================================================
    def PressToBegin(TLP: UIDevice, IDDict: dict, name : str):

        UIhost = TLP
        lblStartText = Label(UIhost, IDDict.get('IDStaTile')) 
        lblStartText.SetText(name)
        lblStartTitle = Label(UIhost, IDDict.get('IDStaText'))
        lblStartTitle.SetText('Testing')

        btnPressToBegin = Button(UIhost, IDDict.get('IDPrToBegin'))
        @eventEx(btnPressToBegin, 'Pressed')
        def btnPressToBeginPressed(button: Button, state: str):
            print(button.Name, state)
            UIhost.ShowPopup('Password Popup')

    #=================================================================
    def LoginAVSystem(TLP: UIDevice, IDDict: dict):

        UIhost = TLP
        btnPassNo1 = Button(UIhost, IDDict.get('btnPassNo1'))
        btnPassNo2 = Button(UIhost, IDDict.get('btnPassNo2'))
        btnPassNo3 = Button(UIhost, IDDict.get('btnPassNo3'))
        btnPassNo4 = Button(UIhost, IDDict.get('btnPassNo4'))
        btnPassNo5 = Button(UIhost, IDDict.get('btnPassNo5'))
        btnPassNo6 = Button(UIhost, IDDict.get('btnPassNo6'))
        btnPassNo7 = Button(UIhost, IDDict.get('btnPassNo7'))
        btnPassNo8 = Button(UIhost, IDDict.get('btnPassNo8'))
        btnPassNo9 = Button(UIhost, IDDict.get('btnPassNo9'))
        btnPassNo0 = Button(UIhost, IDDict.get('btnPassNo0'))
        btnPassDel = Button(UIhost, IDDict.get('btnPassDel'))
        btnPassGroupDict = {
        btnPassNo1 : "1",
        btnPassNo2 : "2",
        btnPassNo3 : "3",
        btnPassNo4 : "4",
        btnPassNo5 : "5",
        btnPassNo6 : "6",
        btnPassNo7 : "7",
        btnPassNo8 : "8",
        btnPassNo9 : "9",
        btnPassNo0 : "0"
        }
        
        
        # define feedback light
        btnPassLight1 = Button(UIhost, IDDict.get('btnPassLight1'))
        btnPassLight2 = Button(UIhost, IDDict.get('btnPassLight2'))
        btnPassLight3 = Button(UIhost, IDDict.get('btnPassLight3'))
        btnPassLight4 = Button(UIhost, IDDict.get('btnPassLight4'))
        btnPassLightGroup = [btnPassLight1, btnPassLight2, btnPassLight3, btnPassLight4]
        # define navigation to return to start page
        lblLoginSystem = Label(UIhost, IDDict.get('lblLoginSystem'))
        btnPassBackToStart = Button(UIhost, IDDict.get('btnPassBackToStart'))        
        @eventEx(btnPassBackToStart, 'Pressed')
        def btnPassBackressed(button: Button, state: str):
            print(button.Name, state)
            lblLoginSystem.SetText('Login to system')
            UIhost.HideAllPopups()
            UIhost.ShowPage('Start')
       
        
    
        # Check password Input
    
        keyPassMaster = IDDict.get('keyPassMaster')
        keyRef =""
        keyCount = 0
        def turnLight(count : int):
            for i in range(3):
                if i < count:
                    btnPassLightGroup[i].SetState(1)
                else:
                    btnPassLightGroup[i].SetState(0)

        btnPassGroup = MESet([btnPassNo1, btnPassNo2, btnPassNo3, btnPassNo4, btnPassNo5,
                              btnPassNo6, btnPassNo7, btnPassNo8, btnPassNo9, btnPassNo0, btnPassDel])
        @eventEx(btnPassGroup.Objects, 'Pressed')
        def btnPassPressed(button: Button, state: str):
            nonlocal keyCount
            nonlocal keyRef
            print(button.Name, state)
            if (button == btnPassDel) & (keyCount >0):
                keyRef = keyRef[:-1]
                keyCount -= 1
                print(keyRef)
                turnLight(keyCount)
            elif (button != btnPassDel) & (keyCount < 4):
                keyRef = keyRef + btnPassGroupDict.get(button)
                keyCount += 1
                print(keyRef, keyPassMaster)
                turnLight(keyCount)

            if keyCount == 4:
                if keyRef == keyPassMaster:
                    UIhost.HidePopup('Password Popup')
                    UIhost.ShowPage('Main')
                    UIhost.ShowPopup(IDDict.get('nextPagePw'))
                else:
                    lblLoginSystem.SetText('Password is incorrect, Please again!')
                Wait(1)
                keyCount = 0
                keyRef = ""
                turnLight(keyCount)
  
    # ==============================================================================================================================
    
    def Roommode(ID: int, TLP: UIDevice, IDRoommodeDict: dict, IDControlDict: dict, IDPopupPageDict: dict):
        
        UIhost = TLP
        btnRoomModeSelect = Button(UIhost, IDRoommodeDict.get('RoomModeSelect'))
        @eventEx(btnRoomModeSelect, 'Pressed')
        def RoomModeSelectPressed(button: Button, state: str):
            print(button.Name, state)
            UIhost.ShowPopup('Room mode')            

        lblRoomModeText = Label(UIhost, IDRoommodeDict.get('IDRoomText'))        
        btnModeRoomA = Button(UIhost, IDRoommodeDict.get('Room_1'))
        btnModeRoomB = Button(UIhost, IDRoommodeDict.get('Room_2'))
        btnModeCombine = Button(UIhost, IDRoommodeDict.get('Combine_12'))
        btnRoomModeDict = {
            btnModeRoomA: IDRoommodeDict.get('Room_1_name'),
            btnModeRoomB: IDRoommodeDict.get('Room_2_name'),
            btnModeCombine: IDRoommodeDict.get('Combine_12_name')
        }
        btnRoomModeGroup = MESet([btnModeRoomA, btnModeRoomB, btnModeCombine])
        @eventEx(btnRoomModeGroup.Objects, 'Pressed')
        def btnRoomModePressed(button: Button, state):
            print(button.Name, state)
            btnRoomModeGroup.SetCurrent(button)

            var.RModeVar[ID] = str(btnRoomModeDict.get(button))
            print('ID:{}, RModeVar:{}'.format(ID,var.RModeVar[ID]))
            lblRoomModeText.SetText(var.RModeVar[ID])
            UIhost.HidePopup('Room mode')
            #Call navigate Control - Room mode
            TLP_class.navControlRoommode(TLP, ID, var.Ctrlvar[ID], var.RModeVar[ID], IDRoommodeDict, IDControlDict, IDPopupPageDict)

    def Controlmode(ID: int, TLP: UIDevice, IDRoommodeDict: dict, IDControlDict: dict, IDPopupPageDict: dict):
        UIhost = TLP
        btnVideoSwitch = Button(UIhost, IDControlDict.get('ViSwitch'))
        btnAudio = Button(UIhost, IDControlDict.get('Audio'))
        btnCamera = Button(UIhost, IDControlDict.get('Camera'))
        btnControlGroupDict = {
            btnVideoSwitch: IDControlDict.get('ViSwitch_name'),
            btnAudio      : IDControlDict.get('Audio_name'),
            btnCamera     : IDControlDict.get('Cam_name')
        }
        btnControlGroup = MESet([btnVideoSwitch, btnAudio, btnCamera])
        @eventEx(btnControlGroup.Objects, 'Pressed')
        def btnControlGroupPressed(button: Button, state):
            print(button.Name, state)
            btnControlGroup.SetCurrent(button)

            var.Ctrlvar[ID] = btnControlGroupDict.get(button)
            print('ID:{}, RModeVar:{}'.format(ID,var.Ctrlvar[ID]))
            #Call navigate Control - Room mode
            TLP_class.navControlRoommode(TLP, ID, var.Ctrlvar[ID], var.RModeVar[ID], IDRoommodeDict, IDControlDict, IDPopupPageDict)
            
        
    def navControlRoommode(TLP:UIDevice, ID: int, CtrlvarRef: str, RModeVarRef: str, IDRoommodeDict: dict, IDControlDict: dict, IDPopupPageDict: dict):
        
        print('ID : {} , Room mode: {} , Control: {}'.format(ID,RModeVarRef,CtrlvarRef))

        if CtrlvarRef == IDControlDict.get('ViSwitch_name'):                                   # if Video switch
            if (RModeVarRef == IDRoommodeDict.get('Room_1_name')):                              # if Ballroom 01 -> showpopup "BR1 video switch"
                print('Set mode done: ID: {} : {} - {}'.format(ID,RModeVarRef,CtrlvarRef))
                print(IDPopupPageDict.get('BR1_vswitch'))
                TLP.ShowPopup(IDPopupPageDict.get('BR1_vswitch'))           
            elif (RModeVarRef == IDRoommodeDict.get('Room_2_name')):                            # if Ballroom 02 -> showpopup "BR2 video switch"
                print('Set mode done: ID: {} : {} - {}'.format(ID,RModeVarRef,CtrlvarRef))
                print(IDPopupPageDict.get('BR2_vswitch'))
                TLP.ShowPopup(IDPopupPageDict.get('BR2_vswitch'))
            elif (RModeVarRef == IDRoommodeDict.get('Combine_12_name')):                             # if Ballroom combine -> showpopup "BRAll video switch"
                print('Set mode done: ID: {} : {} - {}'.format(ID,RModeVarRef,CtrlvarRef))
                print(IDPopupPageDict.get('BRCombine_vswitch'))
                TLP.ShowPopup(IDPopupPageDict.get('BRCombine_vswitch'))
        elif CtrlvarRef == IDControlDict.get('Audio_name'):                
                if (RModeVarRef == IDRoommodeDict.get('Room_1_name')):
                    print('Set mode done: ID: {} : {} - {}'.format(ID,RModeVarRef,CtrlvarRef))
                    TLP.ShowPopup(IDPopupPageDict.get('BR1_Audio'))  
                elif (RModeVarRef == IDRoommodeDict.get('Room_2_name')):
                    print('Set mode done: ID: {} : {} - {}'.format(ID,RModeVarRef,CtrlvarRef))
                    TLP.ShowPopup(IDPopupPageDict.get('BR2_Audio'))
                elif (RModeVarRef == IDRoommodeDict.get('Combine_12_name')):
                    print('Set mode done: ID: {} : {} - {}'.format(ID,RModeVarRef,CtrlvarRef))
                    TLP.ShowPopup(IDPopupPageDict.get('BRCombine_Audio'))
        elif CtrlvarRef == IDControlDict.get('Cam_name'):
            if (RModeVarRef == IDRoommodeDict.get('Room_1_name')):                              # if Ballroom 01 -> showpopup "BR1 video switch"
                print('Set mode done: ID: {} : {} - {}'.format(ID,RModeVarRef,CtrlvarRef))
                print(IDPopupPageDict.get('BR1_CamControl'))
                TLP.ShowPopup(IDPopupPageDict.get('BR1_CamControl'))           
            elif (RModeVarRef == IDRoommodeDict.get('Room_2_name')):                            # if Ballroom 02 -> showpopup "BR2 video switch"
                print('Set mode done: ID: {} : {} - {}'.format(ID,RModeVarRef,CtrlvarRef))
                print(IDPopupPageDict.get('BR2_CamControl'))
                TLP.ShowPopup(IDPopupPageDict.get('BR2_CamControl'))
            elif (RModeVarRef == IDRoommodeDict.get('Combine_12_name')):                             # if Ballroom combine -> showpopup "BRAll video switch"
                print('Set mode done: ID: {} : {} - {}'.format(ID,RModeVarRef,CtrlvarRef))
                print(IDPopupPageDict.get('BR1_CamControl'))
                TLP.ShowPopup(IDPopupPageDict.get('BR1_CamControl'))
            
            