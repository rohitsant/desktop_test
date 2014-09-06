import numpy
l = []
for y in xrange(1,100):
	r = numpy.random.randint(y)
	l.append(r%y)
l.append(numpy.random.randint(100))
arr = numpy.array(l)
outmat = numpy.reshape(arr,(10,10))
print outmat

