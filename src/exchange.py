#!/usr/bin/env python3

data = b"\x00\x03\x03\t"

# 方法1：转成 \xNN 格式
hex_str = ''.join(f"\\x{b:02x}" for b in data)
print("转义形式:", hex_str)

# 方法2：不可见字符用 '.' 替代
visible_str = ''.join(chr(b) if 32 <= b < 127 else '.' for b in data)
print("可见形式:", visible_str)