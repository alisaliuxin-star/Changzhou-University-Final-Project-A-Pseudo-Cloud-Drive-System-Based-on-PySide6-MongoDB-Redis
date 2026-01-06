import sys
from PySide6.QtWidgets import QApplication, QDialog,QMessageBox
from Ui_regist_menu import Ui_Dialog
from pymysql import *

class RegistInterface(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("注册账户")
        self.ui.pushButton.clicked.connect(self.register_user)

    def register_user(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        comfirm_password = self.ui.lineEdit_3.text()
        if password != comfirm_password:
            QMessageBox.warning(self, "错误", "两次输入的密码不一致")
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            return
        try:
            connection = connect(
                host='localhost',
                user='root',
                password='123456',  # 需要替换为实际密码
                database='netdisk',  # 需要替换为实际数据库名
                charset='utf8'
            )
            with connection.cursor() as cursor:
                # 查询用户名是否存在
                check_sql = "SELECT COUNT(*) FROM users WHERE username = %s"
                cursor.execute(check_sql, (username,))
                result = cursor.fetchone()
                if result[0] > 0:
                    QMessageBox.warning(self, "错误", "用户名已存在")
                    return
                
                sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
                cursor.execute(sql, (username, password))
                connection.commit()
                QMessageBox.information(self, "成功", "注册成功！")
                self.close()  # 关闭注册窗口
        except Exception as e:
            QMessageBox.critical(self, "错误", f"注册失败: {str(e)}")
        finally:
            if connection:
                connection.close()

def main():
    app = QApplication(sys.argv)
    window = RegistInterface()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
