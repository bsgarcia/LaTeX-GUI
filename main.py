from PyQt5.QtWidgets import (QApplication, QPlainTextEdit, QVBoxLayout,
                             QComboBox, QMessageBox, QPushButton,
                             QWidget, QLineEdit, QCheckBox)
from PyQt5 import Qt
from subprocess import Popen, getoutput
import os
import sys


class LatexGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.file_to_compile = QLineEdit(self)
        self.compile_btn = QPushButton(self)

        self.output = QPlainTextEdit(self)
        
        self.bib = QCheckBox(self)
        self.mode = QComboBox(self)
        # self.m
        # self.mode.setAlignment(Qt.AlignRight)

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

        self.mode.addItem("PdfLaTeX")
        self.mode.addItem("XeLaTeX")
        self.mode.addItem("LuaLaTex")
        self.bib.setText("BibTeX")

        self.pdf_file = sys.argv[1][:-3] + "pdf"

        self.widgets = [self.file_to_compile,
                        self.mode,
                        self.bib,
                        self.output,
                        self.compile_btn]

    def compile(self):

        mode = str(self.mode.currentText()).lower()
        cmd = "--halt-on-error"
        output = getoutput(" ".join([mode, cmd, sys.argv[1]]))

        try:
            self.output.appendPlainText(output)

            err = ["emergency", "error"]

            if all(e not in output.lower() for e in err):

                if self.bib.isChecked():

                    output = getoutput(" ".join(["bibtex", cmd, sys.argv[1][:-4]]))
                    self.output.appendPlainText(output)
                    output = getoutput(" ".join([mode, cmd, sys.argv[1]]))
                    self.output.appendPlainText(output)
                
                Popen(["xdg-open", self.pdf_file])

            else:
                self.show_error(text="Error during compilation!")

        except Exception as e:
            self.show_error(text=str(e))



    def fill_layout(self):

        for w in self.widgets:
            self.layout.addWidget(w)

    def init_UI(self):

        self.fill_layout()
        self.setWindowTitle("LaTeX GUI")
        self.setGeometry(0, 0, 500, 300)
        self.show()

    @staticmethod
    def show_error(text):

        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Critical)
        msgbox.setWindowTitle("Error")
        msgbox.setText(text)
        msgbox.exec_()

    @staticmethod
    def main():

        app = QApplication(sys.argv)
        win = LatexGUI()
        sys.exit(app.exec_())


if __name__ == '__main__':

    LatexGUI.main()
