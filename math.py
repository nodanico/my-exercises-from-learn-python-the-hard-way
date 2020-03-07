def add(a, b):
    return a + b
    

print "Let's add some numbers!"
print "Enter first number:",
a = int(raw_input(">"))
print "Enter second number:",
b = int(raw_input(">"))

answer = add(a, b)

print "So the answer to %r plus %r is %r!" % (a, b, answer)
