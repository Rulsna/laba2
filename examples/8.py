def outer2(out_param):
  def inner2():
    return f'Outer def have value: {out_param}'
  return inner2
value = outer2('TEST')
print(value())
