"""
git常用命令
"""
import sys, os

# 提交代码到远程仓库
os.system("git pull")
os.system("git add .")
os.system("git commit -m {}".format(sys.argv[1]))
os.system("git push")