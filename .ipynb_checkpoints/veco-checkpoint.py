import turtle

# Tạo màn hình và thiết lập
wn = turtle.Screen()
wn.title("Cờ Tổ Quốc Việt Nam")
wn.bgcolor("white")

# Tạo đối tượng vẽ
pen = turtle.Turtle()
pen.speed(3)

# Hàm vẽ hình chữ nhật
def draw_rectangle(color, width, height):
    pen.begin_fill()
    pen.fillcolor(color)
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()

# Vẽ nền đỏ
pen.penup()
pen.goto(-150, 100)  # Di chuyển đến vị trí bắt đầu
pen.pendown()
draw_rectangle("red", 300, 200)

# Hàm vẽ sao vàng 5 cánh
def draw_star(x, y, radius):
    pen.penup()
    pen.goto(x, y - radius)  # Di chuyển đến vị trí bắt đầu vẽ ngôi sao
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    for _ in range(5):
        pen.forward(radius)
        pen.right(144)
    pen.end_fill()

# Kích thước và vị trí của sao
star_radius = 50
star_x = 0
star_y = 20

# Vẽ sao vàng 5 cánh ở giữa
draw_star(star_x, star_y, star_radius)

# Hoàn tất
pen.hideturtle()
wn.mainloop()
