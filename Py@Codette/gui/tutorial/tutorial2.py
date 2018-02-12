#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

class LogoExample(QtGui.QWidget):
    """
    This is a class called LogoExample. 
    What we see b/w the brackets is the parent of this class, the class QWidget from the QtGui module.
    In PyQt, only a window is a object directly of the class QWidget (has no parent).
    """
    
    def __init__(self):
        """
        This is the constuctor of our class.
        It has, first of all, to call the constructor of its parent, in order to be able to inherit all of its attributes.
        """
        super(LogoExample, self).__init__()
        
        # we use self whenever we refer to the methods or variables of the current class.
        self.initUI()
        
        
    def initUI(self):
        """
        Here is where happens the creation of the GUI.
        
        In order to advertise the fact that this method pertains to this class, we pass self as a parameter of the method.
        The method will actually have zero parameters when it will be called.
        The self parameter is there for us to be able to call the method as self.mehod_name().
        """
        
        # set size of the window and where will be positioned on screen.
        self.setGeometry(500, 300, 500, 300)
        # set window title
        self.setWindowTitle('Py@Codette Loggoed Window Example')
        # set icon/logo
        path = "/home/petrutsx/Documents/workshops_repo/Workshops/Py@Codette/"
        self.setWindowIcon(QtGui.QIcon(path+'codette_logo'))        
    
        self.show()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = LogoExample()
    app.exec_()


if __name__ == '__main__':
    main()    