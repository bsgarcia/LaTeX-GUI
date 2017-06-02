from PyQt5.QtWidgets import (QApplication, QPlainTextEdit, QVBoxLayout, 
                             QComboBox, QMessageBox,QPushButton, 
                             QWidget, QLineEdit)
from subprocess import Popen, PIPE
import os
import sys


class LatexVimCompiler(QWidget):

    def __init__(self):
        super().__init__() 

        self.layout = QVBoxLayout(self)
        
        self.file_to_compile = QLineEdit(self)
        self.compile_btn = QPushButton(self)

        self.output = QPlainTextEdit(self)
        
        self.mode = QComboBox(self)
        
        self.set_up()
        self.init_UI()

    def set_up(self):
        
        # cd into file directory
        os.chdir("/".join(sys.argv[1].split("/")[:-1]))

        self.file_to_compile.setText(sys.argv[1])

        self.compile_btn.setText("Compile")
        self.compile_btn.clicked.connect(self.compile)
        self.compile_btn.setAutoDefault(True)

        self.output.setReadOnly(True)

        self.mode.addItem("PdfLaTex")
        self.mode.addItem("XeLaTex")

        self.pdf_file = sys.argv[1][:-3] + "pdf" 

        self.widgets = [self.file_to_compile,
                        self.mode, 
                        self.output, 
                        self.compile_btn
                        ]
        
    def compile(self):

        mode = str(self.mode.currentText()).lower()
        
        process = Popen([mode, sys.argv[1]], stdout=PIPE)

        out = str(process.stdout.read(), 'utf-8')
        self.output.appendPlainText(out)

        if "fatal error" and "emergency stop" not in out.lower():
            Popen(["xdg-open", self.pdf_file])

        else:
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Critical)
            msgbox.setWindowTitle("Error")
            msgbox.setText("File compilation failed!")

            msgbox.exec_()
               
    def fill_layout(self):
        
        for w in self.widgets:
            self.layout.addWidget(w)

    def init_UI(self):

        self.fill_layout()
        self.setWindowTitle("Vim LaTex Plugin")
        self.setGeometry(0, 0, 500, 300)
        self.show()

    @staticmethod
    def main():

        app = QApplication(sys.argv)
        win = LatexVimCompiler()
        sys.exit(app.exec_())


if __name__ == '__main__':

    LatexVimCompiler.main()
