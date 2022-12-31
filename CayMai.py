import turtle as T
import random
import time



def Tree(branch, t):
	time.sleep(0.0005)
	if branch > 3:
		if 8 <= branch <= 12:
			if random.randint(0, 2) == 0:
				t.color('#82CD47')
			else:
				t.color('#FFFF00')
			t.pensize(branch / 3)
		elif branch < 8:
			if random.randint(0, 1) == 0:
				t.color('wheat')
			else:
				t.color('#FFFF00') 
			t.pensize(branch / 2)
		else:
			t.color('sienna')
			t.pensize(branch / 10)
		t.forward(branch)
		a = 1.5 * random.random()
		t.right(20 * a)
		b = 1.5 * random.random()
		Tree(branch - 10 * b, t)
		t.left(40 * a)
		Tree(branch - 10 * b, t)
		t.right(20 * a)
		t.up()
		t.backward(branch)
		t.down()

def Petal(m, t):
	for i in range(m):
		a = 200 - 400 * random.random()
		b = 10 - 20 * random.random()
		t.up()
		t.forward(b)
		t.left(90)
		t.forward(a)
		t.down()
		t.color('#FFFF00')
		t.circle(1)
		t.up()
		t.backward(a)
		t.right(90)
		t.backward(b)

t = T.Turtle()

w = T.Screen()
t.hideturtle()  
t.getscreen().tracer(5, 0)
w.screensize(bg='wheat')  
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('#FFFF00')

Tree(60, t)

text = T.Turtle()
text.left(90)
text.up()
text.backward(150)
text.down()
text.color('#FFFF00')
text.color('red')

Petal(200, t)
w.exitonclick()


# Christmas tree:

n = 100.0

speed("fastest")
screensize(bg='seashell')
left(90)
forward(3*n)
color("orange", "yellow")
begin_fill()
left(126)

for i in range(5):
	forward(n/5)
	right(144)
	forward(n/5)
	left(72)
end_fill()
right(126)

color("dark green")
backward(n*4.8)
def tree(d, s):
	if d <= 0: return
	forward(s)
	tree(d-1, s*.8)
	right(120)
	tree(d-3, s*.5)
	right(120)
	tree(d-3, s*.5)
	right(120)
	backward(s)
tree(15, n)
backward(n/2)


for i in range(200):
	a = 200 - 400 * random.random()
	b = 10 - 20 * random.random()
	up()
	forward(b)
	left(90)
	forward(a)
	down()
	if random.randint(0, 1) == 0:
		color('#FFF89C')
	else:
		color('wheat')
	circle(2)
	up()
	backward(a)
	right(90)
	backward(b)

time.sleep(60)