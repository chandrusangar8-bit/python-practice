class dad():
    def mobile(self):
        print("dad's mobile")
class mom():
    def tab(self):
        print("mom'tab")
class son(dad,mom):
    def laptop(self):
        print("son's laptop")

ram=son()
ram.mobile()
ram.tab()
ram.laptop() 
        

