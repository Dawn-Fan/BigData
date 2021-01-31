import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QDirModel, QLabel, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 300)
        self.model = QDirModel(self)                            # 1
        self.model.setReadOnly(False)
        self.model.setSorting(QDir.Name | QDir.IgnoreCase)

        self.tree = QTreeView(self)                             # 2
        self.tree.setModel(self.model)
        self.tree.clicked.connect(self.show_info)
        self.index = self.model.index(QDir.currentPath())
        self.tree.expand(self.index)
        self.tree.scrollTo(self.index)

        self.info_label = QLabel(self)                          # 3

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.tree)
        self.v_layout.addWidget(self.info_label)
        self.setLayout(self.v_layout)

    def show_info(self):                                        # 4
        index = self.tree.currentIndex()
        file_name = self.model.fileName(index)
        file_path = self.model.filePath(index)
        file_info = 'File Name: {}\nFile Path: {}'.format(file_name, file_path)
        self.info_label.setText(file_info)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())