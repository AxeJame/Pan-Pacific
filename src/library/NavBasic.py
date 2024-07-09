# Extron Library imports
from extronlib.system import MESet
from extronlib.ui import Button, Label
# Project imports
from modules.helper.ModuleSupport import eventEx
from extronlib.device import ProcessorDevice, UIDevice

# from ui.tlpStart import IDStartPageDict


class TLP_class:
    def PressToBegin(TLP: UIDevice, IDDict: dict):

        UIhost = TLP
        lblStartText = Label(UIhost, IDDict.get('IDStaTile')) 
        lblStartText.SetText('test 01')

        lblStartTitle = Label(UIhost, IDDict.get('IDStaText'))
        btnPressToBegin = Button(UIhost, IDDict.get('IDPrToBegin'))
        @eventEx(btnPressToBegin, 'Pressed')
        def btnPressToBeginPressed(button: Button, state: str):
            print(button.Name, state)
            if button.State == 0:
                lblStartTitle.SetText('BallroomB')
                button.SetState(1)
                UIhost.ShowPage('Password page')
            else: 
                lblStartTitle.SetText('BallrB')
                button.SetState(0)
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
                print(keyRef)
                turnLight(keyCount)

            if keyCount == 4:
                if keyRef == keyPassMaster:
                    UIhost.ShowPage(IDDict.get('nextPagePw'))
                else:
                    lblLoginSystem.SetText('Password is incorrect, Please again!')
                keyCount = 0
                keyRef = ""
                turnLight(keyCount)
  
# ==============================================================================================================================