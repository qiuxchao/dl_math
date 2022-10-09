# -*- coding: utf-8 -*-

# 神经元激活函数： y = a(w1*x1 + w2*x2 + w3*x3 - 阈值)
# 注：a 是我们自己定义的函数

params = [
  {
    'value': 1,
    'weight': 1,
  },
  {
      'value': 2,
      'weight': 2,
  },
  {
      'value': 3,
      'weight': 3,
  },
]


def f(params, threshold) -> 0 | 1:
  curt_th = 0
  for i in params:
    curt_th += i['value'] * i['weight']
  result = 0
  if curt_th > threshold:
    result = 1
  return result

print(f(params, 15))