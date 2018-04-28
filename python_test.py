
def arg_test(arg1, arg2, *argv, **kwargv):
  print('arg1:' + arg1)
  print('arg2:' + arg2)
  for arg in argv:
    print("arg in *argv :" + arg)
  if kwargv is not None:
    for key, value in kwargv.items():
      print("kwargs key =" + key + ", value =" + value)




arg_test('a', 'b', 'c', 'd', kwarg1='e')

args = ('a', 'b', 'c', 'd')
arg_test(*args)

kwargs = {'kwarg1':'e', 'kwarg2':'f'}

arg_test('a', 'b', **kwargs)




