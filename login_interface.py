import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QObject
from Ui_login_menu import Ui_MainWindow as Ui_LoginWindow
from Ui_main_menu import Ui_MainWindow as Ui_MainMenu
import pymysql
from mainmenu_interface import MainMenuInterface
from current_user import write_current_user
from regist_interface import RegistInterface

class LoginInterface(QObject):
    def __init__(self, parent_widget, ui, app):
        super().__init__(parent_widget)
        self.parent_widget = parent_widget  # 存储 QWidget 父窗口
        self.ui = ui
        self.app = app  # 存储应用实例以保持主菜单窗口的生命周期
        self.main_window = None  # 用于存储主菜单窗口实例
        self.main_menu_interface = None  # 用于存储主菜单接口实例
        self.regist_window = None  # 用于存储注册窗口实例
        
        # 连接数据库
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',  # 需要替换为实际密码
            database='netdisk',  # 需要替换为实际数据库名
            charset='utf8'
        )
        # 通过 ui 参数访问控件并正确绑定事件
        self.ui.pushButton.clicked.connect(self.login_check)
        self.ui.pushButton_2.clicked.connect(self.open_regist_window)

    def open_regist_window(self):
        if not self.regist_window:
            self.regist_window = RegistInterface()
        self.regist_window.show()

    def login_check(self):
        # 从lineEdit和lineEdit_2获取账号和密码
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        
        # 查询数据库验证账号密码
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM users WHERE username=%s AND password=%s"
                cursor.execute(sql, (username, password))
                result = cursor.fetchone()
                
                if result:
                    # 登录成功
                    write_current_user(username)  # 写入当前用户
                    QMessageBox.information(self.parent_widget, '提示', '登录成功')

                    # 打开主菜单窗口
                    self.main_window = QMainWindow()
                    ui_main_menu = Ui_MainMenu()
                    ui_main_menu.setupUi(self.main_window)  # 初始化UI
                    self.main_menu_interface = MainMenuInterface(self.main_window, ui_main_menu)  # 传递已初始化的UI
                    self.main_window.show()
                    
                    # 关闭当前登录窗口
                    self.parent_widget.close()

                else:
                    # 登录失败
                    QMessageBox.warning(self.parent_widget, '提示', '用户名或密码错误')
        except Exception as e:
            QMessageBox.critical(self.parent_widget, '错误', f'数据库查询出错: {str(e)}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui_login_menu = Ui_LoginWindow()
    ui_login_menu.setupUi(main_window)
    
    # 初始化登录界面逻辑
    login_interface = LoginInterface(main_window, ui_login_menu, app)
    
    # 显示主窗口
    main_window.show()
    
    # 启动事件循环
    sys.exit(app.exec())
