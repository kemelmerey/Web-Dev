def first_two(str):
  if len(str) < 2:
    return "{}".format(str)
  if len(str) >=2:
    first2 = str[:2]
    return first2
  else:
    return "'yields the empty string'"