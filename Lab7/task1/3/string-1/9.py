def combo_string(a, b):
  if len(a)>len(b):
    return "{}{}{}".format(b,a,b)
  if len(a)<len(b):
    return "{}{}{}".format(a,b,a)