#Convert two list/Tuple to dictionary
a = [ 'a', 'b', 'c', 'd' ]
b = [ 1, 2, 3, 4 ]
print "First list = ", a
print "Second list = ", b
print "My new Dict which combines first and second list = ", dict(zip(a, b))
