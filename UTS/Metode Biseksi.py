def bisection(f, a, b, e=0.5, N = 50):
  xa = a
  xb = b
  
  if f(xa)*f(xb) >= 0:
    print("ERROR")
    return None
    
  for n in range (1,N):
    xm = (xa + xb)/2
    if abs(f(xm)) < e:
      return xm, n
    else:
      if f(xa)*f(xm) < 0:
        xb = xm
      elif f(xb)*f(xm) < 0:
        xa = xm
  return xm, n

f = lambda x: 2*x**3-4*x**2-24
a = input('Nilai a:')
b = input('Nilai B:')
a = float(a)
b = float(b)

x_root, iteration = bisection(f,a,b)
print('Result : ',"%.4f" % x_root)
print('In %d iteration' %iteration)
