# 0 图像
zero = [
    '', '*', '',
    '*', '', '*',
    '*', '', '*',
    '', '*', '',
]

# 1 图像
one = [
	'*', '*', '',
	'', '*', '',
	'', '*', '',
	'', '*', '',
]


# 输入层：直接将图像作为输入层

# 隐藏层 3 个恶魔
# 恶魔1偏心 4 & 7
# 恶魔2偏心 5 & 8
# 恶魔3偏心 6 & 9
def demon_1(px_4, px_7):
	if px_4 == '*' and px_7 == '*':
		return True
	return False

def demon_2(px_5, px_8):
	if px_5 == '*' and px_8 == '*':
		return True
	return False

def demon_3(px_6, px_9):
	if px_6 == '*' and px_9 == '*':
		return True
	return False

# 输出层 2 个恶魔
# 恶魔o1偏心隐藏层 恶魔1 和 恶魔3，输出 0
# 恶魔o2偏心隐藏层 恶魔2，输出 1

def demon_o1(d_1, d_3):
	return d_1 and d_3

def demon_o2(d_2):
	return d_2

if __name__ == '__main__':
	target = one
	d_1 = demon_1(target[3], target[6])
	d_2 = demon_2(target[4], target[7])
	d_3 = demon_3(target[5], target[8])
	o1 = demon_o1(d_1, d_3)
	o2 = demon_o2(d_2)
	if o1:
		print('结果是: 0')
	if o2:
		print('结果是: 1')