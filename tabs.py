import sys

i = 1
tabList = None

class Tab:
    def __init__(self, data, prev = None):
        self.data = data
        self.next = None
        self.prev = prev


class TabLinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def openTab(self, tab):
        temp = self.head
        if temp is None:
            self.current = self.head = Tab(tab)
            return
        while(temp.next):
            temp = temp.next
        # print("prev", self.current.data)
        self.current = temp.next = Tab(tab, self.current)
        return

    def switchTabs(self, tab):
        current = self.head
        while(current):
            if(current.data == tab):
                current.prev = self.current
                self.current = current
            current = current.next

    def closeTab(self, tab):
        current = self.head
        prev = None
        # print(tab," to be closed", self.)
        if(current is None):
            print("Browser is already closed!")
        elif(current.data == tab):
            self.current = current.prev
            self.head = current.next
            current = None
        else:
            while(current):
                if(current.data == tab):
                    break
                prev = current
                current = current.next
            if(current is None):
                print("No Tabs Open!")
            else:
                prev.next = current.next
                self.current = current.prev
                current = None
        return


    def traverseTabs(self):
        current = self.head
        while(current):
            if current.prev:
                print("name->"+current.data+"    "+"prev->"+str(current.prev.data))
            else:
                print("name->"+current.data+"    "+"prev->None")
            current = current.next
        return

    def printCurrentTab(self):
        if(self.current):
            print("current->",self.current.data)
        
    def getPreviousTab(self):
        if(self.current and self.current.prev):
            print("Previous->",self.current.prev.data)

    def getCurrentTab(self):
        return self.current
    


    

def makeChoiceAndReturnFunction(ch):
    beforeOpeningDict = {"0":"exitFromProgram","1":"openBrowser","2":"openNewTab","3":"switchTab","4":"closeTab"}
    func = beforeOpeningDict.get(ch, "nothing")
    return func
        
def openBrowser():
    global tabList, i
    tabList = TabLinkedList()
    tabName = "tab"+str(i)
    tabList.openTab(tabName)
    tabList.printCurrentTab()
    print("Browser Opened with Tab Name " + tabName)
    return

def exitFromProgram():
    sys.exit(1)
    return

def openNewTab():
    global tabList
    name = input("Tab Name?\n")
    tabList.openTab(name)
    tabList.printCurrentTab()
    return

def switchTab():
    global tabList
    tabList.traverseTabs()
    tabName = input("which tab?\n")
    print("switching to..", tabName)
    tabList.switchTabs(tabName)
    tabList.printCurrentTab()

def closeTab():
    global tabList
    tabList.closeTab(tabList.getCurrentTab().data)
    tabList.printCurrentTab()
    

if __name__ == "__main__": 
    while True:
        print("Choose!\n0. Exit\n1. Open Browser\n2. Open New Tab\n3. Switch Tab\n4. Close Tab")
        ch = input()
        func = makeChoiceAndReturnFunction(ch)
        locals()[func]()
        
