# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/client_properties.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(271, 246)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.labelId = QtWidgets.QLabel(Dialog)
        self.labelId.setObjectName("labelId")
        self.gridLayout.addWidget(self.labelId, 2, 4, 1, 3)
        self.labelClientName = QtWidgets.QLabel(Dialog)
        self.labelClientName.setObjectName("labelClientName")
        self.gridLayout.addWidget(self.labelClientName, 3, 4, 1, 3)
        self.label_7 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 2)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        self.labelExecutable = QtWidgets.QLabel(Dialog)
        self.labelExecutable.setObjectName("labelExecutable")
        self.gridLayout.addWidget(self.labelExecutable, 0, 4, 1, 2)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.lineEditLabel = QtWidgets.QLineEdit(Dialog)
        self.lineEditLabel.setObjectName("lineEditLabel")
        self.gridLayout.addWidget(self.lineEditLabel, 4, 4, 1, 5)
        self.lineEditIcon = QtWidgets.QLineEdit(Dialog)
        self.lineEditIcon.setObjectName("lineEditIcon")
        self.gridLayout.addWidget(self.lineEditIcon, 5, 4, 1, 5)
        self.label_9 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.checkBoxSaveStop = QtWidgets.QCheckBox(Dialog)
        self.checkBoxSaveStop.setChecked(True)
        self.checkBoxSaveStop.setObjectName("checkBoxSaveStop")
        self.gridLayout.addWidget(self.checkBoxSaveStop, 6, 0, 1, 9)
        self.labelArguments = QtWidgets.QLabel(Dialog)
        self.labelArguments.setText("")
        self.labelArguments.setObjectName("labelArguments")
        self.gridLayout.addWidget(self.labelArguments, 1, 4, 1, 2)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 2, 1, 1)
        self.toolButtonEditExecutable = QtWidgets.QToolButton(Dialog)
        icon = QtGui.QIcon.fromTheme("edit-rename")
        self.toolButtonEditExecutable.setIcon(icon)
        self.toolButtonEditExecutable.setObjectName("toolButtonEditExecutable")
        self.gridLayout.addWidget(self.toolButtonEditExecutable, 0, 6, 2, 1)
        self.toolButtonIcon = QtWidgets.QToolButton(Dialog)
        self.toolButtonIcon.setStyleSheet("QToolButton{border:none}")
        icon = QtGui.QIcon.fromTheme("application-pdf")
        self.toolButtonIcon.setIcon(icon)
        self.toolButtonIcon.setIconSize(QtCore.QSize(48, 48))
        self.toolButtonIcon.setObjectName("toolButtonIcon")
        self.gridLayout.addWidget(self.toolButtonIcon, 0, 7, 2, 2)
        self.pushButtonSaveChanges = QtWidgets.QPushButton(Dialog)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.pushButtonSaveChanges.setIcon(icon)
        self.pushButtonSaveChanges.setObjectName("pushButtonSaveChanges")
        self.gridLayout.addWidget(self.pushButtonSaveChanges, 7, 1, 1, 8)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Properties"))
        self.labelId.setText(_translate("Dialog", "nsmid"))
        self.labelClientName.setText(_translate("Dialog", "client_name"))
        self.label_7.setText(_translate("Dialog", ":"))
        self.label_11.setText(_translate("Dialog", "Arguments"))
        self.label_8.setText(_translate("Dialog", ":"))
        self.labelExecutable.setText(_translate("Dialog", "executable"))
        self.label_6.setText(_translate("Dialog", "Label"))
        self.label_5.setText(_translate("Dialog", "Icon"))
        self.label_9.setText(_translate("Dialog", ":"))
        self.label_4.setText(_translate("Dialog", ":"))
        self.label.setText(_translate("Dialog", "Executable"))
        self.label_10.setText(_translate("Dialog", ":"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.label_3.setText(_translate("Dialog", "Client id"))
        self.checkBoxSaveStop.setText(_translate("Dialog", "Prevent to stop without recent save"))
        self.label_12.setText(_translate("Dialog", ":"))
        self.toolButtonEditExecutable.setToolTip(_translate("Dialog", "Edit executable"))
        self.toolButtonEditExecutable.setText(_translate("Dialog", "..."))
        self.toolButtonIcon.setText(_translate("Dialog", "..."))
        self.pushButtonSaveChanges.setText(_translate("Dialog", "Save Changes"))

