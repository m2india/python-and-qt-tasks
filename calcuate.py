from PyQt4 import QtGui,QtCore
from math import sqrt
import sys

class program(QtGui.QMainWindow):
    
    def __init__(self):
        super(program,self).__init__()
        self.smallFont = QtGui.QFont('Arial',10,5);self.font = QtGui.QFont('Arial',13,5)
        self.equation = ''
        self.done = False
        self.initGui()
        
    def initGui(self):
    #main display    
        def initWidgets():
            self.mainTextBox = QtGui.QLineEdit(self)
            self.mainTextBox.name = 'mainTextBox'
            self.mainTextBox.setGeometry(10,50,230,30)
            self.mainTextBox.setFont(self.font)
            self.mainTextBox.setReadOnly(True)
            self.mainTextBox.setAlignment(QtCore.Qt.AlignRight)
      #sub display
            self.subTextBox = QtGui.QLineEdit(self)
            self.subTextBox.name = 'subTextBox'
            self.subTextBox.setGeometry(10,20,230,20)
            self.subTextBox.setFont(self.smallFont)
            self.subTextBox.setReadOnly(True)
            self.subTextBox.setAlignment(QtCore.Qt.AlignRight)
            
            rect = QtCore.QRect
            dict = {'CE':rect(10,100,50,30),'C':rect(70,100,50,30),'+/-':rect(130,100,50,30),'sqrt':rect(190,100,50,30),'7':rect(10,140,30,30),'8'
			:rect(50,140,30,30),
                    '9':rect(90,140,30,30),'/':rect(130,140,50,30),'1/x':rect(190,140,50,30),'4':rect(10,180,30,30),'5':rect(50,180,30,30),'6':rect(90,180,30,30),
                    '*':rect(130,180,50,30),'**':rect(190,180,50,30),'1':rect(10,220,30,30),'2':rect(50,220,30,30),'3':rect(90,220,30,30),'+':rect(130,220,50,30),
                    '0':rect(10,260,70,30),'.':rect(90,260,30,30),'-':rect(130,260,50,30),'=':rect(190,220,50,70)}
            
            for a in dict:
                btn = QtGui.QPushButton(a,self)
                btn.name = a
                btn.setGeometry(dict[a])
                btn.setFont(self.font)
                btn.clicked.connect(self.actions) # connections
        
        self.setWindowTitle('Calculator')
        self.setFixedSize(248,294)
        self.setFont(self.font)
        initWidgets()
        self.show()

    def actions(self):
        sender= self.sender()
        numberList = ['1','2','3','4','5','6','7','8','9','0']
        operatorList = ['+','-','/','*','**']
        
        if self.done == True:
            self.mainTextBox.setText('')
            self.subTextBox.setText('')
        
        self.done = False
        
        if sender.name in numberList:
            self.mainTextBox.setText(self.mainTextBox.text()+sender.name)

        elif sender.name in operatorList:
            if self.mainTextBox.text() != '':
                self.subTextBox.setText(self.subTextBox.text()+self.mainTextBox.text()+sender.name)
                self.equation += self.mainTextBox.text()+sender.name
                self.mainTextBox.setText('')
                self.lastChar = sender.name
        
        elif sender.name == 'CE':
            self.mainTextBox.setText('')
            self.equation = ''
        
        elif sender.name == 'C':
            self.mainTextBox.setText('')
            self.subTextBox.setText('')
        
        elif sender.name == '+/-':
            num = int(self.mainTextBox.text())
            self.mainTextBox.setText(str(num-num*2))
        
        elif sender.name == '.':
            if not '.' in self.mainTextBox.text():
                self.mainTextBox.setText(self.mainTextBox.text()+sender.name)
        
        elif sender.name == 'sqrt':
            num = float(self.mainTextBox.text())
            self.mainTextBox.setText(str(sqrt(num)))
        
        elif sender.name == '1/x':
            num = float(self.mainTextBox.text())
            self.mainTextBox.setText(str(1/num))
        
                
        elif sender.name == '=' and self.equation != '':
            if self.mainTextBox.text() != '':
                self.subTextBox.setText(self.subTextBox.text()+self.mainTextBox.text()+'=')
                self.equation += self.mainTextBox.text()
                res = eval(str(self.equation))
                self.mainTextBox.setText(str(res))
                self.equation = ''
                self.done = True
            
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv);app.setStyle('cleanlooks')
    gui = program()
    sys.exit(app.exec_())
