#This will through error
def f(): 
	print s
	s = "Me too."
	print s


s = "I hate spam." 
f()
print s

Error:-
UnboundLocalError: local variable 's' referenced before assignment

#Because Python "assumes" that we want a local variable due to the assignment to s inside of f(), 
#so the first print statement throws this error message. 
#Any variable which is changed or created inside of a function is local, if it hasn't been declared as a global variable. 
#To tell Python, that we want to use the global variable, we have to use the keyword "global", 
#as can be seen in the following example: 
def f():
    global s
    print s
    s = "That's clear."
    print s 


s = "Python is great!" 
f()
print s
