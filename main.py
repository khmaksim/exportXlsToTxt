from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
import sys, os
import form
import export

class Widget(QWidget, form.Ui_Form):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.messageLabel.clear()
		# self.messageLabel.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600; color:#4deb13;">Завершено</span></p></body></html>')

		self.exportButton.clicked.connect(self.exportButtonClicked)		
		self.selectFileButton.clicked.connect(self.selectFile)
		self.selectDirButton.clicked.connect(self.selectDirectory)
		self.selectedFileXlsLineEdit.textChanged.connect(self.enableExportButton)
		self.selectedDirectoryLineEdit.textChanged.connect(self.enableExportButton)
		
	def selectFile(self):
		fileXls, filterFile = QFileDialog.getOpenFileName(self, "Выберите XLS файл", filter="Файл MS Excel (*.xls *.xlsx)")
		if fileXls is not None and os.path.isfile(fileXls):
			self.selectedFileXlsLineEdit.setText(fileXls.replace('/', '\\'))
			
	def selectDirectory(self):
		directory = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения")
		if directory is not None and os.path.exists(directory):
			self.selectedDirectoryLineEdit.setText(directory.replace('/', '\\'))

	def enableExportButton(self):
		if self.selectedDirectoryLineEdit.text() != '' and self.selectedFileXlsLineEdit.text() != '':
			self.exportButton.setEnabled(True)
		else:
			self.exportButton.setEnabled(False)

	def exportButtonClicked(self):
		if export.exportXlsToTxt(self.selectedFileXlsLineEdit.text(), self.selectedDirectoryLineEdit.text()):
			self.messageLabel.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600; color:#4deb13;">Завершено</span></p></body></html>')
		else:
			self.messageLabel.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600; color:#f00d2f;">Ошибка экспорта данных</span></p></body></html>')


def main():
	app = QApplication(sys.argv)
	widget = Widget()
	widget.resize(400, 200)
	widget.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()