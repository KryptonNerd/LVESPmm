from PyQt5 import QtWidgets, uic
import sys
from ESPMM import ESPMM_calc

ESPMM_Result = None
steps_options = [400,200,48]
steps_options_txt = map(str, steps_options)
usteps_options = [1,2,4,8,16,32,64,128,256]
usteps_options_txt = map(str, usteps_options)

class LVESPmm_GUI(QtWidgets.QWidget):
    def __init__(self):
        super(LVESPmm_GUI, self).__init__()
        uic.loadUi('LVESPmm_GUI.ui', self)

        self.pushButton_calc.clicked.connect(self.Calc)
        self.comboBox_steps.addItems(steps_options_txt)
        self.comboBox_steps.setEnabled(True)
        self.comboBox_steps.setCurrentIndex(1)
        self.comboBox_usteps.addItems(usteps_options_txt)
        self.comboBox_usteps.setCurrentIndex(4)
        self.comboBox_usteps.setEnabled(True)
        self.lineEdit_pitch.setEnabled(True)
        self.lineEdit_starts.setEnabled(True)
        self.lineEdit_rs.setEnabled(True)
        self.lineEdit_rb.setEnabled(True)
        self.lcdNumber_espmm.display("-")



    def Calc(self):
        if self.lineEdit_pitch.text() == '' or self.lineEdit_starts.text() == '' or self.lineEdit_rs.text() == '' or self.lineEdit_rb.text() == '' or self.comboBox_steps.currentText() == '' or self.comboBox_usteps.currentText() == '':
            QtWidgets.QMessageBox.about(self, "LVESPmm", "Some fields are blank")
        else:
            pitch = float(self.lineEdit_pitch.text())
            starts = float(self.lineEdit_starts.text())
            rs = float(self.lineEdit_rs.text())
            rb = float(self.lineEdit_rb.text())
            steps = float(steps_options[self.comboBox_steps.currentIndex()])
            usteps = float(usteps_options[self.comboBox_usteps.currentIndex()])

            ESPMM_Result = ESPMM_calc(pitch, starts, rs, rb, steps, usteps)
            self.lcdNumber_espmm.display(float(ESPMM_Result))


    

app = QtWidgets.QApplication([])
win = LVESPmm_GUI()
win.show()
sys.exit(app.exec())