import pymongo
from gridfs import GridFS
from PySide6.QtWidgets import QFileDialog, QMessageBox, QApplication, QMainWindow, QTableView, QAbstractItemView, QHeaderView
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from Ui_main_menu import Ui_MainWindow
import hashlib
import mimetypes
from current_user import read_current_user
import os

class FileTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        super(FileTableModel, self).__init__()
        self._data = data or []

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return 4  # 文件名、文件类型、上传时间、文件大小

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return self._data[row][col]
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return ["文件名称", "文件类型", "上传时间", "文件大小"][section]
        return None

class MainMenuInterface(object):
    def __init__(self, ui_main_window, ui_setup):
        self.username = read_current_user()
        self.ui = ui_main_window
        self.ui_setup = ui_setup  # 使用传入的已初始化的 UI
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client['cloud_drive']
        self.fs = GridFS(self.db)
        # 绑定按钮事件
        self.ui_setup.pushButton_2.clicked.connect(self.upload_file)
        self.ui_setup.pushButton.clicked.connect(self.refresh_list)
        self.ui_setup.pushButton_3.clicked.connect(self.download_file)
        # self.ui_setup.pushButton_4.clicked.connect(self.share_file)
        self.ui_setup.pushButton_5.clicked.connect(self.delete_file)  # 绑定删除按钮事件
        self.ui_setup.pushButton_6.clicked.connect(self.search_file)
        self.ui_setup.label.setText(f"欢迎，用户{self.username}！")
        # 使用 tableView 显示文件列表并维护 file id 映射
        self.file_ids = []
        self.tableView = self.ui_setup.tableView
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setAlternatingRowColors(True)
        self.model = FileTableModel()
        self.tableView.setModel(self.model)

        # Adjust column widths to stretch and fit the table view
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)  # 文件名称
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)  # 文件类型
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)  # 上传时间
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)  # 文件大小
        #启动程序就刷新列表
        self.refresh_list()

    def upload_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(None, "选择文件", "", "所有文件 (*);;", options=options)
        if file_name:
            try:
                with open(file_name, 'rb') as f:
                    file_data = f.read()

                # Generate file hash
                file_hash = hashlib.sha256(file_data).hexdigest()

                # Detect file type
                file_type, _ = mimetypes.guess_type(file_name)
                if not file_type:
                    file_type = "application/octet-stream"  # Default to binary if unknown
                user = read_current_user()

                # Use only the base name of the file instead of full path
                file_base_name = os.path.basename(file_name)

                # Generate metadata
                metadata = {
                    "fileHash": file_hash,
                    "owner_id": user,      # Replace with actual user ID logic
                    "file_type": file_type
                }

                # Upload file to MongoDB using GridFS
                file_id = self.fs.put(file_data, filename=file_base_name, metadata=metadata)
                self.refresh_list()
                # Show success message
                QMessageBox.information(None, "成功", "文件上传成功！")
            except Exception as e:
                QMessageBox.critical(None, "错误", f"文件上传失败: {str(e)}")
        

    def refresh_list(self):
        """刷新文件列表"""
        try:
            # Fetch files metadata from MongoDB
            files = self.fs.find({"metadata.owner_id": read_current_user()}).sort("uploadDate", -1)
            
            # 将查询结果转换为列表（因为 cursor 只能迭代一次）
            files_list = list(files)

            # 准备数据并记录 file_id 映射
            data = []
            self.file_ids = []
            for file in files_list:
                self.file_ids.append(file._id)
                metadata = file.metadata or {}
                upload_time = file.upload_date.strftime("%Y-%m-%d %H:%M:%S")
                # 使用 GridOut.length 如果可用以避免重复读取数据
                file_size = getattr(file, 'length', None)
                if file_size is None:
                    try:
                        file_size = len(file.read())
                    except Exception:
                        file_size = 0
                data.append([file.filename, metadata.get('file_type', ''), upload_time, f"{file_size} bytes"])

            # Update table model
            self.model = FileTableModel(data)
            self.tableView.setModel(self.model)
        except Exception as e:
            QMessageBox.critical(None, "错误", f"刷新文件列表失败: {str(e)}")

    def download_file(self):
        """下载文件"""
        try:
            # Get selected row from tableView
            selected_indexes = self.tableView.selectionModel().selectedRows()
            if not selected_indexes:
                QMessageBox.warning(None, "警告", "请先选择一个文件")
                return

            row = selected_indexes[0].row()
            file_id = self.file_ids[row]

            # Retrieve file from MongoDB
            file = self.fs.get(file_id)
            
            # Save file locally
            options = QFileDialog.Options()
            save_path, _ = QFileDialog.getSaveFileName(None, "保存文件", file.filename, options=options)
            if save_path:
                with open(save_path, 'wb') as f:
                    f.write(file.read())
                QMessageBox.information(None, "成功", "文件下载成功！")
        except Exception as e:
            QMessageBox.critical(None, "错误", f"文件下载失败: {str(e)}")

    def search_file(self):
        search_text = self.ui_setup.plainTextEdit.toPlainText()
        if not search_text:
            QMessageBox.warning(None, "提示", "请输入查询内容")
            return
        
        try:
            files = self.fs.find({"filename": {"$regex": f".*{search_text}.*"}})
            data = []
            for file in files:
                metadata = file.metadata or {}
                upload_time = file.upload_date.strftime("%Y-%m-%d %H:%M:%S")
                file_size = getattr(file, 'length', 0)
                data.append([file.filename, metadata.get('file_type', ''), upload_time, f"{file_size} bytes"])
            
            # Update table model
            self.model = FileTableModel(data)
            self.tableView.setModel(self.model)
        except Exception as e:
            QMessageBox.critical(None, "错误", f"查询失败: {str(e)}")

    # def share_file(self):


    def delete_file(self):
        """删除文件"""
        try:
            # Get selected row from tableView
            selected_indexes = self.tableView.selectionModel().selectedRows()
            if not selected_indexes:
                QMessageBox.warning(None, "警告", "请先选择一个文件")
                return

            # Confirm deletion with user
            reply = QMessageBox.question(None, '确认', '确定要删除该文件吗？',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                return

            row = selected_indexes[0].row()
            file_id = self.file_ids[row]

            # Delete file from MongoDB using GridFS
            self.fs.delete(file_id)

            # Refresh the file list to reflect changes
            self.refresh_list()
            QMessageBox.information(None, "成功", "文件删除成功！")
        except Exception as e:
            QMessageBox.critical(None, "错误", f"文件删除失败: {str(e)}")

if __name__ == "__main__":
    app = QApplication([])
    main_window = QMainWindow()
    ui_setup = Ui_MainWindow()
    ui_setup.setupUi(main_window)
    main_menu_interface = MainMenuInterface(main_window, ui_setup)
    main_window.show()
    app.exec()