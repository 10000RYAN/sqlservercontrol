import tkinter as tk
import os
import webbrowser

app = tk.Tk()
app.title("SQL server启动停止管理器 v1.0")
app.geometry('400x240')
app.configure(bg='#111')
app.resizable(0, 0)

service = "MSSQLSERVER"


def start():
    os.system(f"net start {service}")


def stop():
    os.system(f"net stop {service}")


def website():
    webbrowser.open("https://zhongcaoz.com/system-optimization/46.html")


home_label = tk.Label(app,
                      bg="#111",
                      fg="#fff",
                      text="一个简单（简陋）的SQL server启动停止切换工具，防止SQL server\n"
                           "后台驻留拖慢电脑速度。建议定期到官网检查是否有更新。"
                      ).pack(expand=True, padx="10px")

start_label = tk.Label(app,
                       bg="#111",
                       fg="#fff",
                       text="使用SQL server前请先启用SQL server服务。"
                       ).pack()
start_btn = tk.Button(app,
                      bg="#295",
                      fg="#fff",
                      text="启动SQL server",
                      command=start
                      ).pack(fill="x", padx="10px", pady="5px")
stop_label = tk.Label(app,
                      bg="#111",
                      fg="#fff",
                      text="SQL server不使用时停止服务可加快电脑速度。"
                      ).pack()

stop_btn = tk.Button(app,
                     bg="#c22",
                     fg="#fff",
                     text="停止SQL server",
                     command=stop
                     ).pack(fill="x", padx="10px", pady="5px")
web_btn = tk.Button(app,
                    bg="#16a",
                    fg="#fff",
                    text="官网（可获取说明和更新）",
                    command=website).pack(fill="x", padx="10px", pady="5px")

if __name__ == '__main__':
    app.mainloop()
