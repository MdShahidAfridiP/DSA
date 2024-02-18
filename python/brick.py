def ordered_compositions(n):
  """
  Yield all ordered compositions of n.
  """
  if n == 1:
    yield [1]
  else:
    for composition in ordered_compositions(n - 1):
      composition[-1] += 1 # add 1
      yield composition
      composition[-1] -= 1 # remove the added 1
      composition.append(1) # other way to add 1
      yield composition
      composition.pop() # remove added 1

for composition in ordered_compositions(10):
   print(composition)