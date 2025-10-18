#!/usr/bin/env python3

import logging

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',
    encoding='utf-8'
)

# 使用
logger = logging.getLogger("my_app")
logger.info("程序启动")

# 创建记录器
logger = logging.getLogger("my_module")
logger.setLevel(logging.DEBUG)

# 控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# 文件处理器
file_handler = logging.FileHandler("debug.log", mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# 格式化
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 添加处理器
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 使用
logger.debug("调试信息")  # 仅写入文件
logger.warning("警告！")  # 同时输出到控制台和文件

from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(
    "app.log", maxBytes=1e6, backupCount=3  # 每个文件1MB，保留3个备份
)
logger.addHandler(handler)