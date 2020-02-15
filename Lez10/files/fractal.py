import turtle

def koch(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(order-1, size/3)
            turtle.left(angle)
