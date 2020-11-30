#charged dat as data object
inp = list([x.word for x in dat.L])
imperfective = []
perfective = []
notverb = []
error = []
for x in inp:
  x = word(x,'')
  main.check(x)
  if x.error == False:
    x = verb(x.word)
    if conjugate.check_verb(x) == 0:
      imperfective.append(x.infinitive)
    elif conjugate.check_verb(x) == 1:
      perfective.append(x.infinitive)
    else:
      continue
  else: 
    error.append(x.word)

n = max([len(imperfective),len(perfective),len(error),len(notverb)])
while len(imperfective) < n:
  imperfective.append('')
while len(perfective) < n:
  perfective.append('')
while len(error) < n:
  error.append('')
x = {'imperfective':imperfective,'perfective':perfective,'error':error}
x = pd.DataFrame.from_dict(x)
print(x)
f = open('tonight','w')
for x in imperfective:
  f.write(x.rstrip("\n"))
  f.write("\n")
for x in perfective:
  f.write(x.rstrip("\n"))
  f.write("\n")