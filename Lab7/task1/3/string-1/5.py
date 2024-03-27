def extra_end(str):
  if len(str) < 2:
    return 0
  last2 = str[len(str)-2:]
  return last2+last2+last2