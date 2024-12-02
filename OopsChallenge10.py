# here we create  computer class and two inner classes (CPU,OS) with get method
class computer:
    def __init__(self,name,cpu,os):
        self.name=name
        self.cpu=self.CPU(cpu)
        self.OS= self.OS(os)

    def __str__(self):
        return ' Name: '+self.name+'\n CPU: '+self.cpu.getCpu()+'\n OS :'+self.OS.getOs()

    class CPU:
        def __init__(self,cpu):
            self.cpu=cpu

        def getCpu(self):
            return self.cpu

    class OS:
        def __init__(self,os):
            self.os=os

        def getOs(self):
            return self.os

comp=computer('Lenovo','I7','Windows')
print(comp)
