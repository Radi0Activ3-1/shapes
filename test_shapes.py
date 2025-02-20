import shapes

def test_rectangle():
    shapes.rectangle(3, 4)
    shapes.rectangle(5, 6)

def test_circle():
    shapes.circle(5)
    shapes.circle(7)

if __name__ == "__main__":
    test_rectangle()
    test_circle()