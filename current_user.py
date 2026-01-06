import os

def write_current_user(username):
    """
    将当前用户名写入文件
    """
    with open("current_user.txt", "w", encoding="utf-8") as f:
        f.write(username)

def read_current_user():
    """
    从文件中读取当前用户名
    """
    if not os.path.exists("current_user.txt"):
        return None
    with open("current_user.txt", "r", encoding="utf-8") as f:
        return f.read().strip()