# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Sep 17 01:11:52 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1206, 978)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/run.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidgetMode = QtGui.QTabWidget(self.centralwidget)
        self.tabWidgetMode.setGeometry(QtCore.QRect(10, 10, 421, 331))
        self.tabWidgetMode.setObjectName(_fromUtf8("tabWidgetMode"))
        self.tabTareDrag = QtGui.QWidget()
        self.tabTareDrag.setObjectName(_fromUtf8("tabTareDrag"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.tabTareDrag)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 151, 111))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.doubleSpinBox_tareDragStepU = QtGui.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.doubleSpinBox_tareDragStepU.setProperty("value", 0.5)
        self.doubleSpinBox_tareDragStepU.setObjectName(_fromUtf8("doubleSpinBox_tareDragStepU"))
        self.gridLayout_3.addWidget(self.doubleSpinBox_tareDragStepU, 2, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_3.addWidget(self.label_18, 2, 0, 1, 1)
        self.doubleSpinBox_tareDragEndU = QtGui.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.doubleSpinBox_tareDragEndU.setProperty("value", 0.1)
        self.doubleSpinBox_tareDragEndU.setObjectName(_fromUtf8("doubleSpinBox_tareDragEndU"))
        self.gridLayout_3.addWidget(self.doubleSpinBox_tareDragEndU, 1, 1, 1, 1)
        self.doubleSpinBox_tareDragStartU = QtGui.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.doubleSpinBox_tareDragStartU.setProperty("value", 1.0)
        self.doubleSpinBox_tareDragStartU.setObjectName(_fromUtf8("doubleSpinBox_tareDragStartU"))
        self.gridLayout_3.addWidget(self.doubleSpinBox_tareDragStartU, 0, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)
        self.tabWidgetMode.addTab(self.tabTareDrag, _fromUtf8(""))
        self.tabTareTorque = QtGui.QWidget()
        self.tabTareTorque.setObjectName(_fromUtf8("tabTareTorque"))
        self.gridLayoutWidget = QtGui.QWidget(self.tabTareTorque)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 151))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.doubleSpinBox_tareTorqueStepTsr = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_tareTorqueStepTsr.setObjectName(_fromUtf8("doubleSpinBox_tareTorqueStepTsr"))
        self.gridLayout.addWidget(self.doubleSpinBox_tareTorqueStepTsr, 3, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.doubleSpinBox_tareTorqueRefU = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_tareTorqueRefU.setProperty("value", 1.0)
        self.doubleSpinBox_tareTorqueRefU.setObjectName(_fromUtf8("doubleSpinBox_tareTorqueRefU"))
        self.gridLayout.addWidget(self.doubleSpinBox_tareTorqueRefU, 0, 1, 1, 1)
        self.doubleSpinBox_tareTorqueStartTsr = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_tareTorqueStartTsr.setProperty("value", 0.1)
        self.doubleSpinBox_tareTorqueStartTsr.setObjectName(_fromUtf8("doubleSpinBox_tareTorqueStartTsr"))
        self.gridLayout.addWidget(self.doubleSpinBox_tareTorqueStartTsr, 1, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.doubleSpinBox_tareTorqueEndTsr = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_tareTorqueEndTsr.setProperty("value", 3.1)
        self.doubleSpinBox_tareTorqueEndTsr.setObjectName(_fromUtf8("doubleSpinBox_tareTorqueEndTsr"))
        self.gridLayout.addWidget(self.doubleSpinBox_tareTorqueEndTsr, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_startTsrRpm = QtGui.QLabel(self.gridLayoutWidget)
        self.label_startTsrRpm.setObjectName(_fromUtf8("label_startTsrRpm"))
        self.gridLayout.addWidget(self.label_startTsrRpm, 1, 2, 1, 1)
        self.label_stopTsrRpm = QtGui.QLabel(self.gridLayoutWidget)
        self.label_stopTsrRpm.setObjectName(_fromUtf8("label_stopTsrRpm"))
        self.gridLayout.addWidget(self.label_stopTsrRpm, 2, 2, 1, 1)
        self.tabWidgetMode.addTab(self.tabTareTorque, _fromUtf8(""))
        self.tabSingleRun = QtGui.QWidget()
        self.tabSingleRun.setObjectName(_fromUtf8("tabSingleRun"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.tabSingleRun)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 201, 111))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_4)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.doubleSpinBox_towspeed = QtGui.QDoubleSpinBox(self.gridLayoutWidget_4)
        self.doubleSpinBox_towspeed.setMaximum(2.0)
        self.doubleSpinBox_towspeed.setSingleStep(0.1)
        self.doubleSpinBox_towspeed.setProperty("value", 1.0)
        self.doubleSpinBox_towspeed.setObjectName(_fromUtf8("doubleSpinBox_towspeed"))
        self.gridLayout_4.addWidget(self.doubleSpinBox_towspeed, 0, 1, 1, 1)
        self.lineEdit_singleRunName = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_singleRunName.setObjectName(_fromUtf8("lineEdit_singleRunName"))
        self.gridLayout_4.addWidget(self.lineEdit_singleRunName, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget_4)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.doubleSpinBox_tsr = QtGui.QDoubleSpinBox(self.gridLayoutWidget_4)
        self.doubleSpinBox_tsr.setMaximum(5.0)
        self.doubleSpinBox_tsr.setSingleStep(0.1)
        self.doubleSpinBox_tsr.setProperty("value", 2.0)
        self.doubleSpinBox_tsr.setObjectName(_fromUtf8("doubleSpinBox_tsr"))
        self.gridLayout_4.addWidget(self.doubleSpinBox_tsr, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget_4)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_Re_D = QtGui.QLabel(self.gridLayoutWidget_4)
        self.label_Re_D.setObjectName(_fromUtf8("label_Re_D"))
        self.gridLayout_4.addWidget(self.label_Re_D, 0, 2, 1, 1)
        self.tabWidgetMode.addTab(self.tabSingleRun, _fromUtf8(""))
        self.tabMultipleRuns = QtGui.QWidget()
        self.tabMultipleRuns.setObjectName(_fromUtf8("tabMultipleRuns"))
        self.tableWidget = QtGui.QTableWidget(self.tabMultipleRuns)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 391, 241))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(65)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.verticalHeader().setDefaultSectionSize(15)
        self.tableWidget.verticalHeader().setMinimumSectionSize(15)
        self.tabWidgetMode.addTab(self.tabMultipleRuns, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidgetMode.addTab(self.tab, _fromUtf8(""))
        self.dockWidgetNISignals = QtGui.QDockWidget(self.centralwidget)
        self.dockWidgetNISignals.setGeometry(QtCore.QRect(440, 0, 391, 881))
        self.dockWidgetNISignals.setFloating(False)
        self.dockWidgetNISignals.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidgetNISignals.setObjectName(_fromUtf8("dockWidgetNISignals"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.dockWidgetContents_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 5, 371, 851))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.plotTorque = CurveWidget(self.verticalLayoutWidget_2)
        self.plotTorque.setOrientation(QtCore.Qt.Horizontal)
        self.plotTorque.setObjectName(_fromUtf8("plotTorque"))
        self.verticalLayout_2.addWidget(self.plotTorque)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.plotDrag = CurveWidget(self.verticalLayoutWidget_2)
        self.plotDrag.setOrientation(QtCore.Qt.Horizontal)
        self.plotDrag.setObjectName(_fromUtf8("plotDrag"))
        self.verticalLayout_2.addWidget(self.plotDrag)
        self.label_12 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_2.addWidget(self.label_12)
        self.plotDragL = CurveWidget(self.verticalLayoutWidget_2)
        self.plotDragL.setOrientation(QtCore.Qt.Horizontal)
        self.plotDragL.setObjectName(_fromUtf8("plotDragL"))
        self.verticalLayout_2.addWidget(self.plotDragL)
        self.label_13 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_2.addWidget(self.label_13)
        self.plotDragR = CurveWidget(self.verticalLayoutWidget_2)
        self.plotDragR.setOrientation(QtCore.Qt.Horizontal)
        self.plotDragR.setObjectName(_fromUtf8("plotDragR"))
        self.verticalLayout_2.addWidget(self.plotDragR)
        self.label_16 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_2.addWidget(self.label_16)
        self.plotRPM_ni = CurveWidget(self.verticalLayoutWidget_2)
        self.plotRPM_ni.setOrientation(QtCore.Qt.Horizontal)
        self.plotRPM_ni.setObjectName(_fromUtf8("plotRPM_ni"))
        self.verticalLayout_2.addWidget(self.plotRPM_ni)
        self.dockWidgetNISignals.setWidget(self.dockWidgetContents_2)
        self.dockWidget_acscontrol = QtGui.QDockWidget(self.centralwidget)
        self.dockWidget_acscontrol.setGeometry(QtCore.QRect(10, 340, 421, 531))
        self.dockWidget_acscontrol.setFloating(False)
        self.dockWidget_acscontrol.setObjectName(_fromUtf8("dockWidget_acscontrol"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.verticalLayoutWidget = QtGui.QWidget(self.dockWidgetContents_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 401, 501))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget_acs = QtGui.QTableWidget(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_acs.sizePolicy().hasHeightForWidth())
        self.tableWidget_acs.setSizePolicy(sizePolicy)
        self.tableWidget_acs.setMinimumSize(QtCore.QSize(0, 112))
        self.tableWidget_acs.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_acs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_acs.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_acs.setProperty("showDropIndicator", True)
        self.tableWidget_acs.setDragDropOverwriteMode(False)
        self.tableWidget_acs.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidget_acs.setShowGrid(True)
        self.tableWidget_acs.setObjectName(_fromUtf8("tableWidget_acs"))
        self.tableWidget_acs.setColumnCount(6)
        self.tableWidget_acs.setRowCount(4)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_acs.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_acs.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_acs.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_acs.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_acs.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_acs.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_acs.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_acs.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_acs.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_acs.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_acs.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_acs.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_acs.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_acs.setItem(3, 0, item)
        self.tableWidget_acs.horizontalHeader().setDefaultSectionSize(64)
        self.tableWidget_acs.horizontalHeader().setMinimumSectionSize(23)
        self.tableWidget_acs.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_acs.verticalHeader().setVisible(False)
        self.tableWidget_acs.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_acs.verticalHeader().setDefaultSectionSize(22)
        self.tableWidget_acs.verticalHeader().setHighlightSections(False)
        self.tableWidget_acs.verticalHeader().setMinimumSectionSize(15)
        self.tableWidget_acs.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_acs.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget_acs)
        self.label_26 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.verticalLayout.addWidget(self.label_26)
        self.plotTowSpeed = CurveWidget(self.verticalLayoutWidget)
        self.plotTowSpeed.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.plotTowSpeed.setOrientation(QtCore.Qt.Horizontal)
        self.plotTowSpeed.setObjectName(_fromUtf8("plotTowSpeed"))
        self.verticalLayout.addWidget(self.plotTowSpeed)
        self.label_28 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.verticalLayout.addWidget(self.label_28)
        self.plotTurbineTSR = CurveWidget(self.verticalLayoutWidget)
        self.plotTurbineTSR.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.plotTurbineTSR.setOrientation(QtCore.Qt.Horizontal)
        self.plotTurbineTSR.setObjectName(_fromUtf8("plotTurbineTSR"))
        self.verticalLayout.addWidget(self.plotTurbineTSR)
        self.label_27 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.verticalLayout.addWidget(self.label_27)
        self.plotRPM_acs = CurveWidget(self.verticalLayoutWidget)
        self.plotRPM_acs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.plotRPM_acs.setOrientation(QtCore.Qt.Horizontal)
        self.plotRPM_acs.setObjectName(_fromUtf8("plotRPM_acs"))
        self.verticalLayout.addWidget(self.plotRPM_acs)
        self.dockWidget_acscontrol.setWidget(self.dockWidgetContents_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1206, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHoming = QtGui.QMenu(self.menubar)
        self.menuHoming.setObjectName(_fromUtf8("menuHoming"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuSetings = QtGui.QMenu(self.menubar)
        self.menuSetings.setObjectName(_fromUtf8("menuSetings"))
        self.menuTest_Plan = QtGui.QMenu(self.menubar)
        self.menuTest_Plan.setObjectName(_fromUtf8("menuTest_Plan"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidgetVectrino = QtGui.QDockWidget(MainWindow)
        self.dockWidgetVectrino.setMinimumSize(QtCore.QSize(369, 38))
        self.dockWidgetVectrino.setObjectName(_fromUtf8("dockWidgetVectrino"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.dockWidgetContents)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 1, 351, 861))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_vecu = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_vecu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vecu.setObjectName(_fromUtf8("label_vecu"))
        self.verticalLayout_3.addWidget(self.label_vecu)
        self.plotVecU = CurveWidget(self.verticalLayoutWidget_3)
        self.plotVecU.setOrientation(QtCore.Qt.Horizontal)
        self.plotVecU.setObjectName(_fromUtf8("plotVecU"))
        self.verticalLayout_3.addWidget(self.plotVecU)
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_3.addWidget(self.label_11)
        self.plotVecV = CurveWidget(self.verticalLayoutWidget_3)
        self.plotVecV.setOrientation(QtCore.Qt.Horizontal)
        self.plotVecV.setObjectName(_fromUtf8("plotVecV"))
        self.verticalLayout_3.addWidget(self.plotVecV)
        self.label_14 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_3.addWidget(self.label_14)
        self.plotVecW = CurveWidget(self.verticalLayoutWidget_3)
        self.plotVecW.setOrientation(QtCore.Qt.Horizontal)
        self.plotVecW.setObjectName(_fromUtf8("plotVecW"))
        self.verticalLayout_3.addWidget(self.plotVecW)
        self.label_15 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_3.addWidget(self.label_15)
        self.plotVecCorr = CurveWidget(self.verticalLayoutWidget_3)
        self.plotVecCorr.setOrientation(QtCore.Qt.Horizontal)
        self.plotVecCorr.setObjectName(_fromUtf8("plotVecCorr"))
        self.verticalLayout_3.addWidget(self.plotVecCorr)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.plotVecSNR = CurveWidget(self.verticalLayoutWidget_3)
        self.plotVecSNR.setOrientation(QtCore.Qt.Horizontal)
        self.plotVecSNR.setObjectName(_fromUtf8("plotVecSNR"))
        self.verticalLayout_3.addWidget(self.plotVecSNR)
        self.dockWidgetVectrino.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetVectrino)
        self.toolBar_DAQ = QtGui.QToolBar(MainWindow)
        self.toolBar_DAQ.setObjectName(_fromUtf8("toolBar_DAQ"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_DAQ)
        self.toolBar_motion = QtGui.QToolBar(MainWindow)
        self.toolBar_motion.setObjectName(_fromUtf8("toolBar_motion"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_motion)
        self.toolBar_directory = QtGui.QToolBar(MainWindow)
        self.toolBar_directory.setObjectName(_fromUtf8("toolBar_directory"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_directory)
        self.actionStart = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStart.setIcon(icon1)
        self.actionStart.setObjectName(_fromUtf8("actionStart"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionCOM_Port = QtGui.QAction(MainWindow)
        self.actionCOM_Port.setObjectName(_fromUtf8("actionCOM_Port"))
        self.actionHome_Tow = QtGui.QAction(MainWindow)
        self.actionHome_Tow.setObjectName(_fromUtf8("actionHome_Tow"))
        self.actionEnable_Tow = QtGui.QAction(MainWindow)
        self.actionEnable_Tow.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/tow_icon_b.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnable_Tow.setIcon(icon2)
        self.actionEnable_Tow.setObjectName(_fromUtf8("actionEnable_Tow"))
        self.actionHome_Turbine = QtGui.QAction(MainWindow)
        self.actionHome_Turbine.setObjectName(_fromUtf8("actionHome_Turbine"))
        self.actionHome_y = QtGui.QAction(MainWindow)
        self.actionHome_y.setObjectName(_fromUtf8("actionHome_y"))
        self.actionHome_z = QtGui.QAction(MainWindow)
        self.actionHome_z.setObjectName(_fromUtf8("actionHome_z"))
        self.actionEdit_Configuration = QtGui.QAction(MainWindow)
        self.actionEdit_Configuration.setObjectName(_fromUtf8("actionEdit_Configuration"))
        self.actionMonitor_NI = QtGui.QAction(MainWindow)
        self.actionMonitor_NI.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/max.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMonitor_NI.setIcon(icon3)
        self.actionMonitor_NI.setObjectName(_fromUtf8("actionMonitor_NI"))
        self.actionMonitor_Vectrino = QtGui.QAction(MainWindow)
        self.actionMonitor_Vectrino.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/vectrino.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMonitor_Vectrino.setIcon(icon4)
        self.actionMonitor_Vectrino.setObjectName(_fromUtf8("actionMonitor_Vectrino"))
        self.actionVectrino = QtGui.QAction(MainWindow)
        self.actionVectrino.setObjectName(_fromUtf8("actionVectrino"))
        self.actionTurbine_Characteristics = QtGui.QAction(MainWindow)
        self.actionTurbine_Characteristics.setObjectName(_fromUtf8("actionTurbine_Characteristics"))
        self.actionImportTestPlan = QtGui.QAction(MainWindow)
        self.actionImportTestPlan.setObjectName(_fromUtf8("actionImportTestPlan"))
        self.actionStop = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/stop_normal_red.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon5)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.actionAbort = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/agt_stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbort.setIcon(icon6)
        self.actionAbort.setObjectName(_fromUtf8("actionAbort"))
        self.actionEnable_Turbine = QtGui.QAction(MainWindow)
        self.actionEnable_Turbine.setCheckable(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/turbine.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnable_Turbine.setIcon(icon7)
        self.actionEnable_Turbine.setObjectName(_fromUtf8("actionEnable_Turbine"))
        self.actionEnable_y = QtGui.QAction(MainWindow)
        self.actionEnable_y.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/agt_back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnable_y.setIcon(icon8)
        self.actionEnable_y.setObjectName(_fromUtf8("actionEnable_y"))
        self.actionEnable_z = QtGui.QAction(MainWindow)
        self.actionEnable_z.setCheckable(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnable_z.setIcon(icon9)
        self.actionEnable_z.setObjectName(_fromUtf8("actionEnable_z"))
        self.menuFile.addAction(self.actionQuit)
        self.menuHoming.addAction(self.actionHome_Tow)
        self.menuHoming.addAction(self.actionHome_Turbine)
        self.menuHoming.addAction(self.actionHome_y)
        self.menuHoming.addAction(self.actionHome_z)
        self.menuSetings.addAction(self.actionVectrino)
        self.menuSetings.addAction(self.actionTurbine_Characteristics)
        self.menuTest_Plan.addAction(self.actionImportTestPlan)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSetings.menuAction())
        self.menubar.addAction(self.menuHoming.menuAction())
        self.menubar.addAction(self.menuTest_Plan.menuAction())
        self.toolBar.addAction(self.actionStart)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addAction(self.actionAbort)
        self.toolBar_DAQ.addAction(self.actionMonitor_NI)
        self.toolBar_DAQ.addAction(self.actionMonitor_Vectrino)
        self.toolBar_motion.addAction(self.actionEnable_Tow)
        self.toolBar_motion.addAction(self.actionEnable_Turbine)
        self.toolBar_motion.addAction(self.actionEnable_y)
        self.toolBar_motion.addAction(self.actionEnable_z)

        self.retranslateUi(MainWindow)
        self.tabWidgetMode.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "TurbineDAQ", None))
        self.label_19.setText(_translate("MainWindow", "End U (m/s)", None))
        self.label_18.setText(_translate("MainWindow", "Step (m/s)", None))
        self.label_17.setText(_translate("MainWindow", "Start U (m/s)", None))
        self.tabWidgetMode.setTabText(self.tabWidgetMode.indexOf(self.tabTareDrag), _translate("MainWindow", "Tare Drag", None))
        self.label_9.setText(_translate("MainWindow", "U_ref (m/s)", None))
        self.label_8.setText(_translate("MainWindow", "End TSR", None))
        self.label_7.setText(_translate("MainWindow", "Start TSR", None))
        self.label_4.setText(_translate("MainWindow", "Step", None))
        self.label_startTsrRpm.setText(_translate("MainWindow", "= RPM", None))
        self.label_stopTsrRpm.setText(_translate("MainWindow", "= RPM", None))
        self.tabWidgetMode.setTabText(self.tabWidgetMode.indexOf(self.tabTareTorque), _translate("MainWindow", "Tare Torque", None))
        self.label_3.setText(_translate("MainWindow", "Tow Speed (m/s)", None))
        self.label_6.setText(_translate("MainWindow", "Tip Speed Ratio", None))
        self.label_10.setText(_translate("MainWindow", "Name", None))
        self.label_Re_D.setText(_translate("MainWindow", "Re_D =", None))
        self.tabWidgetMode.setTabText(self.tabWidgetMode.indexOf(self.tabSingleRun), _translate("MainWindow", "Single Run", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Run", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "U (m/s)", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "λ", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "y/R", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "z/H", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Done?", None))
        self.tabWidgetMode.setTabText(self.tabWidgetMode.indexOf(self.tabMultipleRuns), _translate("MainWindow", "Test Plan", None))
        self.tabWidgetMode.setTabText(self.tabWidgetMode.indexOf(self.tab), _translate("MainWindow", "Processing", None))
        self.dockWidgetNISignals.setWindowTitle(_translate("MainWindow", "NI Signals", None))
        self.label.setText(_translate("MainWindow", "Torque (Nm)", None))
        self.label_2.setText(_translate("MainWindow", "Drag (N)", None))
        self.label_12.setText(_translate("MainWindow", "Drag Left (N)", None))
        self.label_13.setText(_translate("MainWindow", "Drag Right (N)", None))
        self.label_16.setText(_translate("MainWindow", "Turbine RPM", None))
        self.dockWidget_acscontrol.setWindowTitle(_translate("MainWindow", "ACS Controller", None))
        item = self.tableWidget_acs.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Axis", None))
        item = self.tableWidget_acs.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Home Ct.", None))
        item = self.tableWidget_acs.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "RPOS", None))
        item = self.tableWidget_acs.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "FPOS", None))
        item = self.tableWidget_acs.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "RVEL", None))
        item = self.tableWidget_acs.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "FVEL", None))
        __sortingEnabled = self.tableWidget_acs.isSortingEnabled()
        self.tableWidget_acs.setSortingEnabled(False)
        item = self.tableWidget_acs.item(0, 0)
        item.setText(_translate("MainWindow", "tow", None))
        item = self.tableWidget_acs.item(1, 0)
        item.setText(_translate("MainWindow", "turbine", None))
        item = self.tableWidget_acs.item(2, 0)
        item.setText(_translate("MainWindow", "y", None))
        item = self.tableWidget_acs.item(3, 0)
        item.setText(_translate("MainWindow", "z", None))
        self.tableWidget_acs.setSortingEnabled(__sortingEnabled)
        self.label_26.setText(_translate("MainWindow", "Tow Speed (m/s)", None))
        self.label_28.setText(_translate("MainWindow", "Turbine Tip Speed Ratio", None))
        self.label_27.setText(_translate("MainWindow", "Turbine RPM", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHoming.setTitle(_translate("MainWindow", "Homing", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuSetings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuTest_Plan.setTitle(_translate("MainWindow", "Test Plan", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.dockWidgetVectrino.setWindowTitle(_translate("MainWindow", "Vectrino", None))
        self.label_vecu.setText(_translate("MainWindow", "u (m/s)", None))
        self.label_11.setText(_translate("MainWindow", "v (m/s)", None))
        self.label_14.setText(_translate("MainWindow", "w (m/s)", None))
        self.label_15.setText(_translate("MainWindow", "Correlation (%)", None))
        self.label_5.setText(_translate("MainWindow", "SNR (dB)", None))
        self.toolBar_DAQ.setWindowTitle(_translate("MainWindow", "toolBar_2", None))
        self.toolBar_motion.setWindowTitle(_translate("MainWindow", "toolBar_2", None))
        self.toolBar_directory.setWindowTitle(_translate("MainWindow", "toolBar_2", None))
        self.actionStart.setText(_translate("MainWindow", "Start", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionCOM_Port.setText(_translate("MainWindow", "COM Port", None))
        self.actionHome_Tow.setText(_translate("MainWindow", "Home Tow Axis", None))
        self.actionEnable_Tow.setText(_translate("MainWindow", "Enable Tow", None))
        self.actionEnable_Tow.setToolTip(_translate("MainWindow", "Tow Axis Enable", None))
        self.actionHome_Turbine.setText(_translate("MainWindow", "Home Turbine Axis", None))
        self.actionHome_y.setText(_translate("MainWindow", "Home y-axis", None))
        self.actionHome_z.setText(_translate("MainWindow", "Home z-axis", None))
        self.actionEdit_Configuration.setText(_translate("MainWindow", "Edit Configuration...", None))
        self.actionMonitor_NI.setText(_translate("MainWindow", "Monitor NI Signals", None))
        self.actionMonitor_NI.setToolTip(_translate("MainWindow", "Monitor NI Signals", None))
        self.actionMonitor_Vectrino.setText(_translate("MainWindow", "Monitor Vectrino", None))
        self.actionMonitor_Vectrino.setToolTip(_translate("MainWindow", "Monitor Vectrino Signals", None))
        self.actionVectrino.setText(_translate("MainWindow", "Vectrino...", None))
        self.actionTurbine_Characteristics.setText(_translate("MainWindow", "Turbine Characteristics...", None))
        self.actionImportTestPlan.setText(_translate("MainWindow", "Import...", None))
        self.actionStop.setText(_translate("MainWindow", "Stop", None))
        self.actionStop.setToolTip(_translate("MainWindow", "Stop after current run completes", None))
        self.actionAbort.setText(_translate("MainWindow", "Abort", None))
        self.actionAbort.setToolTip(_translate("MainWindow", "Stop immediately and abort run", None))
        self.actionEnable_Turbine.setText(_translate("MainWindow", "Enable Turbine", None))
        self.actionEnable_y.setText(_translate("MainWindow", "Enable y", None))
        self.actionEnable_z.setText(_translate("MainWindow", "Enable z", None))

from guiqwt.plot import CurveWidget
import resources_rc