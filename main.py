from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyDictionary import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 574)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.CheckBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CheckBtn.setEnabled(True)
        self.CheckBtn.clicked.connect(self.checkWord)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBtn.sizePolicy().hasHeightForWidth())
        self.CheckBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setBold(False)
        font.setWeight(50)
        self.CheckBtn.setFont(font)
        self.CheckBtn.setObjectName("CheckBtn")
        self.gridLayout.addWidget(self.CheckBtn, 0, 1, 1, 1)
        self.WordInput = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.WordInput.setFont(font)
        self.WordInput.setObjectName("WordInput")
        self.gridLayout.addWidget(self.WordInput, 0, 0, 1, 1)
        self.Tab = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.Tab.setFont(font)
        self.Tab.setObjectName("Tab")
        self.MeaningTab = QtWidgets.QWidget()
        self.MeaningTab.setObjectName("MeaningTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MeaningTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MeaningOutput = QtWidgets.QTextBrowser(self.MeaningTab)
        self.MeaningOutput.setObjectName("MeaningOutput")
        self.horizontalLayout.addWidget(self.MeaningOutput)
        self.Tab.addTab(self.MeaningTab, "")
        self.SynTab = QtWidgets.QWidget()
        self.SynTab.setObjectName("SynTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.SynTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SynOutput = QtWidgets.QTextBrowser(self.SynTab)
        self.SynOutput.setObjectName("SynOutput")
        self.horizontalLayout_2.addWidget(self.SynOutput)
        self.Tab.addTab(self.SynTab, "")
        self.Antotab = QtWidgets.QWidget()
        self.Antotab.setObjectName("Antotab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Antotab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.AnOutput = QtWidgets.QTextBrowser(self.Antotab)
        self.AnOutput.setObjectName("AnOutput")
        self.horizontalLayout_3.addWidget(self.AnOutput)
        self.Tab.addTab(self.Antotab, "")
        self.TranlateTab = QtWidgets.QWidget()
        self.TranlateTab.setObjectName("TranlateTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.TranlateTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.TranlateTab)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 1, 0, 1, 9)
        self.label = QtWidgets.QLabel(self.TranlateTab)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.LangList = QtWidgets.QComboBox(self.TranlateTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LangList.setFont(font)
        self.LangList.setObjectName("LangList")
        self.LangList.addItem("")
        self.LangList.addItem("")
        self.LangList.addItem("")
        self.LangList.addItem("")
        self.LangList.addItem("")
        self.LangList.addItem("")
        self.LangList.addItem("")
        self.LangList.addItem("")
        self.LangList.addItem("")
        self.gridLayout_3.addWidget(self.LangList, 0, 1, 1, 8)
        self.Tab.addTab(self.TranlateTab, "")
        self.gridLayout.addWidget(self.Tab, 1, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dictionary = PyDictionary()
        self.retranslateUi(MainWindow)
        self.Tab.setCurrentIndex(0)
        self.MeaningOutput.setFontPointSize(12)
        self.SynOutput.setFontPointSize(12)
        self.AnOutput.setFontPointSize(12)
        self.textBrowser.setFontPointSize(12)
        self.LangList.currentIndexChanged.connect(self.translateWord)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JDictonary"))
        self.CheckBtn.setText(_translate("MainWindow", "Check"))
        self.WordInput.setPlaceholderText(_translate("MainWindow", "Enter a word"))
        self.Tab.setTabText(self.Tab.indexOf(self.MeaningTab), _translate("MainWindow", "Meaning"))
        self.Tab.setTabText(self.Tab.indexOf(self.SynTab), _translate("MainWindow", "Synonym"))
        self.Tab.setTabText(self.Tab.indexOf(self.Antotab), _translate("MainWindow", "Antonym"))
        self.label.setText(_translate("MainWindow", "Language"))
        self.LangList.setItemText(0, _translate("MainWindow", "Chineese"))
        self.LangList.setItemText(1, _translate("MainWindow", "Hindi"))
        self.LangList.setItemText(2, _translate("MainWindow", "Arabic"))
        self.LangList.setItemText(3, _translate("MainWindow", "Spanish"))
        self.LangList.setItemText(4, _translate("MainWindow", "French"))
        self.LangList.setItemText(5, _translate("MainWindow", "Latin"))
        self.LangList.setItemText(6, _translate("MainWindow", "Malayalam"))
        self.LangList.setItemText(7, _translate("MainWindow", "Tamil"))
        self.LangList.setItemText(8, _translate("MainWindow", "Kannada"))
        self.Tab.setTabText(self.Tab.indexOf(self.TranlateTab), _translate("MainWindow", "Translate"))
    def checkWord(self):
    	self.word = self.WordInput.text()
    	print(self.word)
    	try:
	    	self.updateMeaningTab() 
	    	self.updateSynTab()
	    	self.updateAnTab()
	    	self.updateTransalateTab()
    	except:
	    	QMessageBox.critical(MainWindow,'Error!','Bad network connection!')

    def updateMeaningTab(self):
    	WordMeaningData = self.dictionary.meaning(self.word)
    	MeaningKeys = list(WordMeaningData.keys())
    	MeaningValues = list(WordMeaningData.values())
    	self.MeaningText=''
    	for key in MeaningKeys:
    		nkey = key
    		nkey+=" :-"
    		self.MeaningText+=nkey
    		self.MeaningText+="\n======\n\n"
    		for MeaningStr in WordMeaningData[key]:
    			if('(' in MeaningStr):
    				MeaningStr="->"+MeaningStr
    				self.MeaningText+=MeaningStr
    				self.MeaningText+=")\n\n"
    			else:
    				MeaningStr="->"+MeaningStr
    				self.MeaningText+=MeaningStr
    				self.MeaningText+="\n\n"
    	self.MeaningText+="\n"
    	self.MeaningOutput.setText(self.MeaningText)
    def updateSynTab(self):
    	WordMeaningData = self.dictionary.synonym(self.word)
    	self.SynonymText = ''
    	if(WordMeaningData==None):
    		self.SynonymText='Synonyms for {} are not available'.format(self.word)
    	else:
    		for count,i in enumerate(WordMeaningData):
    			self.SynonymText+=count+1
    			self.SynonymText+=". "
    			self.SynonymText+=i
    			self.SynonymText+="\n\n"
    	self.SynOutput.setText(self.SynonymText)
    def updateAnTab(self):
    	WordMeaningData = self.dictionary.antonym(self.word)
    	self.AntonymText = ''
    	if(WordMeaningData==None):
    		self.AntonymText = 'Antonyms for {} are not available'.format(self.word)
    	else:
    		for count,i in enumerate(WordMeaningData):
    			self.AntonymText+=count+1
    			self.AntonymText+=". "
    			self.AntonymText+=i
    			self.AntonymText+="\n\n"
    	self.AnOutput.setText(self.AntonymText)
    def updateTransalateTab(self):
    	WordMeaningData = self.dictionary.translate(self.word,'zh')
    	self.textBrowser.setText(WordMeaningData)
    def translateWord(self):
    	lang = self.LangList.currentText()
    	print('Lang = ',lang)
    	if(lang=='Chineese'):
    		WordMeaningData = self.dictionary.translate(self.word,'zh')
    	elif(lang=='Arabic'):
    		WordMeaningData = self.dictionary.translate(self.word,'ar')
    	elif(lang=='Hindi'):
    		WordMeaningData = self.dictionary.translate(self.word,'hi')
    	elif(lang=='Spanish'):
    		WordMeaningData = self.dictionary.translate(self.word,'es')
    	elif(lang=='French'):
    		WordMeaningData = self.dictionary.translate(self.word,'fr')
    	elif(lang=='Kannada'):
    		WordMeaningData = self.dictionary.translate(self.word,'kn')
    	elif(lang=='Tamil'):
    		WordMeaningData = self.dictionary.translate(self.word,'ta')
    	elif(lang=='Latin'):
    		WordMeaningData = self.dictionary.translate(self.word,'la')
    	elif(lang=='Malayalam'):
    		WordMeaningData = self.dictionary.translate(self.word,'ml')
    	self.textBrowser.setText(WordMeaningData)   	



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
