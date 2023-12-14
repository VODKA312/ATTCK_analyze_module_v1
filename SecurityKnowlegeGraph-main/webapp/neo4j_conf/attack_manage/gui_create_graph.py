import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cretate_graph import load_graph
import webbrowser
from py2neo import Graph, Node, Relationship, NodeMatcher

def browse_button():
    global cache_path
    cache_path = filedialog.askdirectory()
    if not cache_path:
        print("请选择一个目录。")
    else:
        print("选择的目录:", cache_path)

def browse_neo4j_web():
    neo4j_web_path = "http://localhost:7474/browser/"
    webbrowser.open(neo4j_web_path)
    print("已在默认的 web 浏览器中打开 Neo4j web 数据库。")

def authorize():
    username = username_entry.get()
    password = password_entry.get()

    neo4j_host = 'localhost'
    neo4j_port = 7687

    try:
        print(f"Attempting to connect with username: {username} and password: {password}")
        graph = Graph(f"neo4j://{neo4j_host}:{neo4j_port}", auth=(username, password))
        matcher = NodeMatcher(graph)
        print("授权成功。")
        messagebox.showinfo("授权成功", "您已成功授权。")
    except Exception as e:
        print(f"授权失败: {e}")
        messagebox.showerror("授权失败", "无效的用户名或密码。请重试。")


def generate_graph():
    if cache_path:
        load_graph(cache_path)
        print("知识图谱生成成功。")
    else:
        print("请先选择 cache_data 目录。")

# Create the main window
root = tk.Tk()
root.title("知识图谱生成器")

# Set window size (width x height)
root.geometry("300x400")  # Adjust the size according to your preference

# Entry widget for Neo4j username
label_username = tk.Label(root, text="请输入 Neo4j 数据库用户名:")
label_username.pack(pady=5)  # Increase vertical spacing

# Use SimSun (宋体) font for Chinese characters
username_entry = tk.Entry(root, font=("SimSun", 12))
username_entry.pack(pady=5)  # Increase vertical spacing

# Entry widget for Neo4j password
label_password = tk.Label(root, text="请输入 Neo4j 数据库用户密码:")
label_password.pack(pady=5)  # Increase vertical spacing

# Use SimSun (宋体) font for Chinese characters
password_entry = tk.Entry(root, show="*", font=("SimSun", 12))
password_entry.pack(pady=5)  # Increase vertical spacing

# Authorization button
authorize_button = tk.Button(root, text="验证用户有效性", command=authorize)
authorize_button.pack(pady=10)  # Increase vertical spacing

# Create and place widgets
label = tk.Label(root, text="请选择构建图谱数据源文件夹:")
label.pack(pady=5)  # Increase vertical spacing

browse_button = tk.Button(root, text="点击选择", command=browse_button)
browse_button.pack(pady=5)  # Increase vertical spacing

label_neo4j = tk.Label(root, text="Neo4j web 数据库 URL:")
label_neo4j.pack(pady=5)  # Increase vertical spacing

label = tk.Label(root, text="生成安全知识图谱:")
label.pack(pady=5)  # Increase vertical spacing

generate_button = tk.Button(root, text="生成知识图谱", command=generate_graph)
generate_button.pack(pady=10)  # Increase vertical spacing

browse_button_neo4j = tk.Button(root, text="在浏览器中打开", command=browse_neo4j_web)
browse_button_neo4j.pack(pady=10)  # Increase vertical spacing

# Run the Tkinter event loop
root.mainloop()
