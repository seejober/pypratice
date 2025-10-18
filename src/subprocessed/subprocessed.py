#！/usr/bin/env python3

import subprocess

# 执行一个简单的 shell 命令
result = subprocess.run(['ipconfig'], capture_output=True, text=True)

# 打印命令的输出
print(result.stdout)

# 启动一个子进程
process = subprocess.Popen(['ping', 'baidu.com'], stdout=subprocess.PIPE, text=True)

# 读取子进程的输出
while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(output.strip())

# 获取子进程的退出状态码
return_code = process.poll()
print(f"Process finished with return code {return_code}")