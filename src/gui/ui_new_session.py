# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/new_session.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogNewSession(object):
    def setupUi(self, DialogNewSession):
        DialogNewSession.setObjectName("DialogNewSession")
        DialogNewSession.setWindowModality(QtCore.Qt.NonModal)
        DialogNewSession.resize(290, 202)
        DialogNewSession.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogNewSession)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelNsmFolder = QtWidgets.QLabel(DialogNewSession)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelNsmFolder.sizePolicy().hasHeightForWidth())
        self.labelNsmFolder.setSizePolicy(sizePolicy)
        self.labelNsmFolder.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelNsmFolder.setObjectName("labelNsmFolder")
        self.horizontalLayout.addWidget(self.labelNsmFolder)
        self.currentNsmFolder = QtWidgets.QLabel(DialogNewSession)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentNsmFolder.sizePolicy().hasHeightForWidth())
        self.currentNsmFolder.setSizePolicy(sizePolicy)
        self.currentNsmFolder.setStyleSheet("font-style :  italic")
        self.currentNsmFolder.setObjectName("currentNsmFolder")
        self.horizontalLayout.addWidget(self.currentNsmFolder)
        self.toolButtonFolder = QtWidgets.QToolButton(DialogNewSession)
        icon = QtGui.QIcon.fromTheme("folder-open")
        self.toolButtonFolder.setIcon(icon)
        self.toolButtonFolder.setObjectName("toolButtonFolder")
        self.horizontalLayout.addWidget(self.toolButtonFolder)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.labelNewSessionName = QtWidgets.QLabel(DialogNewSession)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelNewSessionName.sizePolicy().hasHeightForWidth())
        self.labelNewSessionName.setSizePolicy(sizePolicy)
        self.labelNewSessionName.setObjectName("labelNewSessionName")
        self.verticalLayout.addWidget(self.labelNewSessionName)
        self.lineEdit = QtWidgets.QLineEdit(DialogNewSession)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutTemplate = QtWidgets.QHBoxLayout()
        self.horizontalLayoutTemplate.setObjectName("horizontalLayoutTemplate")
        self.labelTemplate = QtWidgets.QLabel(DialogNewSession)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTemplate.sizePolicy().hasHeightForWidth())
        self.labelTemplate.setSizePolicy(sizePolicy)
        self.labelTemplate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTemplate.setObjectName("labelTemplate")
        self.horizontalLayoutTemplate.addWidget(self.labelTemplate)
        self.comboBoxTemplate = QtWidgets.QComboBox(DialogNewSession)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxTemplate.sizePolicy().hasHeightForWidth())
        self.comboBoxTemplate.setSizePolicy(sizePolicy)
        self.comboBoxTemplate.setObjectName("comboBoxTemplate")
        self.horizontalLayoutTemplate.addWidget(self.comboBoxTemplate)
        self.verticalLayout.addLayout(self.horizontalLayoutTemplate)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogNewSession)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogNewSession)
        self.buttonBox.accepted.connect(DialogNewSession.accept)
        self.buttonBox.rejected.connect(DialogNewSession.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogNewSession)

    def retranslateUi(self, DialogNewSession):
        _translate = QtCore.QCoreApplication.translate
        DialogNewSession.setWindowTitle(_translate("DialogNewSession", "New Session"))
        self.labelNsmFolder.setText(_translate("DialogNewSession", "NSM Folder :"))
        self.currentNsmFolder.setText(_translate("DialogNewSession", "/home/user/Ray Sessions"))
        self.toolButtonFolder.setText(_translate("DialogNewSession", "Folder"))
        self.labelNewSessionName.setText(_translate("DialogNewSession", "New Session Name :"))
        self.labelTemplate.setText(_translate("DialogNewSession", "Template :"))

