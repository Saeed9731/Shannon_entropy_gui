from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from xlsxwriter import Workbook
from Shannon_entropy import pi_entropy000620
from  jensen_shannon import jensen_shanon_DV
from os.path import join

lok_icon = "graphic_pi_2_2_5\image"
# auto-py-to-exe
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
    def data(self, index, role):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]
            return value

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

class Ui_ShannonEntropy(object):
        
    def setupUi(self, ShannonEntropy):
        # ShannonEntropy.setObjectName("ShannonEntropy")
        ShannonEntropy.setGeometry(350,50, 828, 665)
        ShannonEntropy.setWindowIcon(QtGui.QIcon(join(lok_icon, "icon.png")))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ShannonEntropy.sizePolicy().hasHeightForWidth())
        ShannonEntropy.setSizePolicy(sizePolicy)
        # ShannonEntropy.setMinimumSize(QtCore.QSize(828, 740))
        # ShannonEntropy.setMaximumSize(QtCore.QSize(828, 740))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        ShannonEntropy.setFont(font)
        ShannonEntropy.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        ShannonEntropy.setWindowOpacity(1.0)
        ShannonEntropy.setStyleSheet("QMenuBar {\n"
        "       background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
        "                                      stop:0 #3F0760, stop:1 #700B97);\n"
        "       spacing: 3px; /* spacing between menu bar items */\n"
   
        "       color: rgb(213, 245, 255);\n"
        "}\n"
        "QMenuBar::item {\n"
        "    padding: 1px 4px;\n"
        "    background: transparent;\n"
        "    border-radius: 4px;\n"
        "}\n"
        "QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
        "       background: rgb(143, 120, 255);\n"
        "}\n"
        "QMenuBar::item:pressed {\n"
        "    background: #888888;\n"
        "}\n"
        "QMainWindow {\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                     stop: 0 #9796f0, stop:1 #fbc7d4);\n"
        "}\n"
        )
        # ShannonEntropy.setIconSize(QtCore.QSize(50, 50))
        self.centralwidget = QtWidgets.QWidget(ShannonEntropy)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 2, 435, 71))
        self.label.setStyleSheet("font: 14pt \"Berlin Sans FB Demi\";\n""color: #4d056c;\n")
        self.Step_1 = QtWidgets.QLabel(self.centralwidget)
        self.Step_1.setGeometry(QtCore.QRect(375, 80, 111, 31))
        self.Step_1.setStyleSheet("color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
        "stop: 0 #670002, stop:1 #670002);\n"
        "font: 75 14pt \"Franklin Gothic Medium\"")
        self.Load_pi_digits = QtWidgets.QPushButton(self.centralwidget)
        self.Load_pi_digits.setGeometry(QtCore.QRect(110, 310, 151, 81))
        self.Load_pi_digits.setStyleSheet("QPushButton {\n"
        "    border: 2px solid ;\n"
        "    color: rgb(105, 210, 255);\n"
        "    border-radius: 6px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #3F0760, stop:1 #700B97);\n"
        "    min-width: 80px;\n"
        "    color: rgb(213, 245, 255);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #8E06C2, stop: 1 #3F0760);\n"
        "}\n"
        "QPushButton:default {\n"
        "    border-color: navy; /* make the default button prominent */\n"
        "}")
        self.Load_pi_digits.clicked.connect(self.Load_pi_digits1)
        #...................
        self.Step_4 = QtWidgets.QLabel(self.centralwidget)
        self.Step_4.setGeometry(QtCore.QRect(165, 400, 91, 31))
        self.Step_4.setStyleSheet("color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
        "stop: 0 #670002, stop:1 #670002);\n"
        "font: 75 12pt \"Franklin Gothic Medium\";")
        #...................
        self.Step_3 = QtWidgets.QLabel(self.centralwidget)
        self.Step_3.setGeometry(QtCore.QRect(165, 275, 81, 41))
        self.Step_3.setStyleSheet("color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
        "stop: 0 #670002, stop:1 #670002);\n"
        "font: 75 12pt \"Franklin Gothic Medium\";")
        self.Start_Processing = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Processing.setGeometry(QtCore.QRect(110, 430, 151, 81))
        self.Start_Processing.setStyleSheet("QPushButton {\n"
        "    border: 2px solid ;\n"
        "    color: rgb(105, 210, 255);\n"
        "    border-radius: 6px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #3F0760, stop:1 #700B97);\n"
        "    min-width: 80px;\n"
        "    color: rgb(213, 245, 255);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #8E06C2, stop: 1 #3F0760);\n"
        "}"
        "QPushButton:default {\n"
        "    border-color: navy; /* make the default button prominent */\n""}"
        )
        self.Start_Processing.clicked.connect(self.Start_Processing1)
        #...................
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setEnabled(True)
        self.Exit.setGeometry(QtCore.QRect(70, 573, 221, 51))
        self.Exit.setStyleSheet("\n"
        "QPushButton {\n"
        "    border: 2px solid ;\n"
        "    border-radius: 6px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #5A082E, stop: 1 #9E0B28);\n"
        "    min-width: 80px;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 9E0B28, stop: 1 #5A082E);\n"
        "}"

        "QPushButton:default {\n"
        "    border-color: navy; /* make the default button prominent */\n"
        "}")
        self.Exit.clicked.connect(self.Exit1)
        #...................
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 90, 581, 61))
        self.Step_Digicts = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.Step_Digicts.setContentsMargins(0, 0, 0, 0)

        self.first_typedigicts = QtWidgets.QLabel(self.layoutWidget)
        self.first_typedigicts.setStyleSheet("color: #F31D31;\n"
        "font: 70 11pt \"Arial Rounded MT Bold\";")
        self.Step_Digicts.addWidget(self.first_typedigicts)
        self.get_step_digicts = QtWidgets.QSpinBox(self.layoutWidget)
        self.get_step_digicts.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.get_step_digicts.setMinimum(1)
        self.get_step_digicts.setMaximum(10)
        self.get_step_digicts.setProperty("value", 1)
        self.get_step_digicts.setStyleSheet("QSpinBox {\n"
        "    border: 2px solid ;\n"
        "    color: rgb(105, 210, 255);\n"
        "    border-radius: 6px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #3F0760, stop:1 #700B97);\n"
        "    min-width: 80px;\n"
        "    color: rgb(213, 245, 255);\n"
        "}")
        self.Step_Digicts.addWidget(self.get_step_digicts)
        self.tableView_Out_pot = QtWidgets.QTableView(self.centralwidget)
        self.tableView_Out_pot.setGeometry(QtCore.QRect(380, 150, 391, 361))
        self.tableView_Out_pot.setStyleSheet("QTableView {\n"
        "    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
        "                                stop: 0  #9796f0, stop:1 #fbc7d4);\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #3F0760, stop:1 #700B97);\n"
        "    border: 0px solid ;\n"
        "    color:  rgb(105, 210, 255);\n"
        "    border-radius: 12px;\n"
        "}\n"
        )
        self.groupBox_step_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_step_2.setGeometry(QtCore.QRect(110, 177, 151, 81))
        self.groupBox_step_2.setStyleSheet("QGroupBox {\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #3F0760, stop:1 #700B97);\n"
        "    border: 2px solid ;\n"
        "    color: rgb(105, 210, 255);\n"
        "    border-radius: 5px;\n"
        "    color: rgb(213, 245, 255);\n"
        "    margin-top: 1.2ex; /* leave space at the top for the title */\n"
        "}"
        "QGroupBox::title {\n"
        "    subcontrol-origin: margin;\n"
        "    subcontrol-position: top center; /* position at the top center */\n"
        "    padding: 0 3px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #3F0760, stop:1 #700B97);\n"
        "}")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_step_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 131, 51))

        self.step_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.step_2.setContentsMargins(0, 0, 0, 0)

        self.Shannon_entropy = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Shannon_entropy.setStyleSheet("color: rgb(213, 245, 255);")
        self.step_2.addWidget(self.Shannon_entropy)
        self.Jensen_shanon = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Jensen_shanon.setStyleSheet("color: rgb(213, 245, 255);")
        self.step_2.addWidget(self.Jensen_shanon)

        self.groupBox_Run_time = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Run_time.setGeometry(QtCore.QRect(510, 560, 131, 71))
        self.groupBox_Run_time.setStyleSheet("QGroupBox {\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #3F0760, stop:1 #700B97);\n"
        "    border: 2px solid ;\n"
        "    color: rgb(105, 210, 255);\n"
        "    border-radius: 5px;\n"
        "    color: rgb(213, 245, 255);\n"
        "    margin-top: 1.2ex; /* leave space at the top for the title */\n"
        "}"
        "QGroupBox::title {\n"
        "    subcontrol-origin: margin;\n"
        "    subcontrol-position: top center; /* position at the top center */\n"
        "    padding: 0 3px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #3F0760, stop:1 #700B97);\n"
        "}")
        self.Run_Time = QtWidgets.QLCDNumber(self.groupBox_Run_time)
        self.Run_Time.setGeometry(QtCore.QRect(10, 20, 111, 41))
        self.Run_Time.setStyleSheet("QLCDNumber {"
        "    background-color: solid;"
        "    border-radius: 0px;"
        "    color: red;"
        "    border-style: solid;"
        "}")
        self.File_lock = QtWidgets.QTextEdit(self.centralwidget)
        self.File_lock.setGeometry(QtCore.QRect(397, 520, 360, 30))
        self.File_lock.setStyleSheet("    border: 2px solid ;\n"
        "    border-radius: 6px;\n"
        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
        "                                      stop: 0 #3F0760, stop:1 #700B97);\n"
        "    color: rgb(213, 245, 255);\n"
        "    min-width: 80px;")
        ShannonEntropy.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ShannonEntropy)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 828, 23))
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuHelp = QtWidgets.QMenu(self.menubar)

        ShannonEntropy.setMenuBar(self.menubar)
        self.actionNew_File = QtGui.QAction(QtGui.QIcon(join(lok_icon, "blue-folder-open-document.png")),
                "actionNew_File",ShannonEntropy)
        
        self.actionNew_File.triggered.connect(self.Load_pi_digits1)
        #.........................................
        self.actionSave = QtGui.QAction(ShannonEntropy)

        self.actionSave_2 = QtGui.QAction(QtGui.QIcon(join(lok_icon, "disk.png")),
                "actionSave_2",ShannonEntropy)
        self.actionSave_2.triggered.connect(self.Save2)
        #..........................
        self.actionSave_as = QtGui.QAction(QtGui.QIcon(join(lok_icon, "disk--pencil.png")),
                "actionSave_as",ShannonEntropy)
        self.actionSave_as.triggered.connect(self.Save_As2)
        # ..........................
        self.actionSave_As_Exel_File = QtGui.QAction(QtGui.QIcon(join(lok_icon, "printer.png")),
                "actionSave_As_Exel_File",ShannonEntropy)
        self.actionSave_As_Exel_File.triggered.connect(self.Save_as_Exel2)
        #..........................
        self.actionStart_Processing = QtGui.QAction(QtGui.QIcon(join(lok_icon, "ui-tab--plus.png")),
                "actionStart_Processing",ShannonEntropy)
        self.actionStart_Processing.triggered.connect(self.Start_Processing1)

        self.actionExit = QtGui.QAction(QtGui.QIcon(join(lok_icon, "arrow-curve-180-left.png")),
                "actionExit",ShannonEntropy)
        self.actionExit.triggered.connect(self.Exit1)

        self.actionHelp = QtGui.QAction(QtGui.QIcon(join(lok_icon, "question.png")),
                "actionHelp",ShannonEntropy)
        self.actionHelp.triggered.connect(self.Hlep1)

        self.actionabout_us = QtGui.QAction(QtGui.QIcon(join(lok_icon, "clipboard-paste-document-text.png")),
                "actionabout_us",ShannonEntropy)
        self.actionabout_us.triggered.connect(self.INTRODUTION)

        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_2)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionSave_As_Exel_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionStart_Processing)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionabout_us)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(ShannonEntropy)
        QtCore.QMetaObject.connectSlotsByName(ShannonEntropy)
        self.pi_file = False
        self.path = None

    def retranslateUi(self, ShannonEntropy):
        _translate = QtCore.QCoreApplication.translate
        ShannonEntropy.setWindowTitle(_translate("ShannonEntropy", "Shannon Entropy & Jensen Shannon Divergence"))
        self.label.setText(_translate("ShannonEntropy", " Shannon entropy and Jensen shannon Divergence"))
        self.Step_1.setText(_translate("ShannonEntropy", "Step 1"))
        self.Load_pi_digits.setText(_translate("ShannonEntropy", "Load pi digits"))
        self.Step_4.setText(_translate("ShannonEntropy", "Step 4"))
        self.Step_3.setText(_translate("ShannonEntropy", "Step 3"))
        self.Start_Processing.setText(_translate("ShannonEntropy", "Start Processing"))
        self.Exit.setText(_translate("ShannonEntropy", "Exit"))
        self.first_typedigicts.setText(_translate("ShannonEntropy", "First Determine the Situation Of Step (one, double, triple   or...) :"))
        self.groupBox_step_2.setTitle(_translate("ShannonEntropy", "Step 2"))
        self.Shannon_entropy.setText(_translate("ShannonEntropy", "Shannon entropy"))
        self.Jensen_shanon.setText(_translate("ShannonEntropy", "Jensen shanon Dv"))
        self.groupBox_Run_time.setTitle(_translate("ShannonEntropy", "Run time"))
        self.menuFile.setTitle(_translate("ShannonEntropy", "File"))
        self.menuEdit.setTitle(_translate("ShannonEntropy", "Edit"))
        self.menuHelp.setTitle(_translate("ShannonEntropy", "Help"))
        self.actionNew_File.setText(_translate("ShannonEntropy", "New File"))
        self.actionSave.setText(_translate("ShannonEntropy", "Save"))
        self.actionSave_2.setText(_translate("ShannonEntropy", "Save"))
        self.actionSave_as.setText(_translate("ShannonEntropy", "Save as"))
        self.actionSave_As_Exel_File.setText(_translate("ShannonEntropy", "Save As Exel File"))
        self.actionStart_Processing.setText(_translate("ShannonEntropy", "Start prosses"))
        self.actionExit.setText(_translate("ShannonEntropy", "Exit"))
        self.actionHelp.setText(_translate("ShannonEntropy", "Help"))
        self.actionabout_us.setText(_translate("ShannonEntropy", "about us"))

    def Load_pi_digits1(self):
          loc, _ =  QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QMainWindow(), "Save file", "", "Text documents (*.txt)")
          self.pi_file = loc
          self.File_lock.setPlainText(self.pi_file)
          _translate = QtCore.QCoreApplication.translate
          ShannonEntropy.setWindowTitle(_translate("ShannonEntropy", "Shanon Entropy and Jensen Shanon - " + self.pi_file))
          _translate = None
    def Start_Processing1(self):

        n = self.get_step_digicts.value()
        if self.pi_file:
                if self.Shannon_entropy.isChecked():
                        self.data, e1, t = pi_entropy000620(self.pi_file, n)
                elif self.Jensen_shanon.isChecked():
                        self.data, t = jensen_shanon_DV(self.pi_file, n)
                        e1 = None
                else:
                        self.data, e1, t = pi_entropy000620(self.pi_file, n)
                self.File_lock.setPlainText("e1 = " + str(e1))
                self.Run_Time.display(t)
                self.model = TableModel(self.data)
                self.tableView_Out_pot.setModel(self.model)
                QMessageBox.information(ShannonEntropy, "Out Pot", "e1 = {} \n\n runtime: {}".format(e1, t))
        else:
                QMessageBox.critical(ShannonEntropy,"Load Eror", "Pleas Load your data")
    def Save_As2(self):
            try:
                path, _ = QtWidgets.QFileDialog.getSaveFileName(ShannonEntropy, "Save file", "Shannonn Entropy and Jensen-ShannonDV",
                "Text documents (*.txt)")
                self.path = path
                with open(self.path, 'w') as f:
                        for i, j in self.data:
                                f.write("{} \t {} \n".format(i, j))
            except FileNotFoundError or AttributeError:
                    return 0
    def Save_as_Exel2(self):
            path, _ = QtWidgets.QFileDialog.getSaveFileName(ShannonEntropy, "Save file Exel", "Shannon Entropy and Jensen-ShannonDV",
             "Text documents (*.xlsx)")
            f = Workbook(str(path))   
            worksheet = f.add_worksheet("My sheet")
            # Start from the first cell. Rows and
            # columns are zero indexed.
            row = 0
            col = 0
            # Iterate over the data and write it out row by row.   
            try:
                    for name, score in (self.data):
                            worksheet.write(row, col, name)
                            worksheet.write(row, col + 1, score)
                            row += 1 
                    f.close()
            except:
                    return 0
    def Save2(self):
            if self.path == None:
                    self.Save_As2()
                    return 0
            elif self.path[-3:] == "txt":
                    try:
                        with open(self.path, 'w') as f:
                                for i, j in self.data:
                                        f.write("{} \t {} \n".format(i, j))
                        return 0
                    except AttributeError:
                            return 0


    def Hlep1(self):
            QMessageBox.information(ShannonEntropy, "Help", "Step 1: first type intiger positive number for world length\
 if you enter Big lenght the program mabe crash.  \
                            \n\n Step 2: second select which on Shannon entropy OR Jensen shanon for proses\
        \nif you don't choose something swich to default and the program consither the Shannon entropy \
                            \n\n step 3: upload yor file the file format must is name.txt \
                            \n\n step 4: Start Calculating \
                            \n\n Thank you for your attention")
            return 0
    def INTRODUTION(self):
            QMessageBox.information(ShannonEntropy, "about us", "we calculat The Shanon entropy and jensen shanon \
            \n\n Professor's name: Dr.Ali Mehri\
            \nstudent name: Saeed Mahmoudi")
            return 0
    def Exit1(self):
            QtWidgets.QApplication.instance().quit()

# https://stackoverflow.com/questions/22460003/pyqts-qmainwindow-closeevent-is-never-called
class MyWindow(QtWidgets.QMainWindow):
    def closeEvent(self,event):
        button = QMessageBox.question(ShannonEntropy,"Quit?","Are you sure you want to Quit? ")
        if button == QMessageBox.StandardButton.Yes:
                event.accept()
        else:
                event.ignore()

#https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShannonEntropy = MyWindow()
    ui = Ui_ShannonEntropy()
    ui.setupUi(ShannonEntropy)
    ShannonEntropy.show()
    sys.exit(app.exec())