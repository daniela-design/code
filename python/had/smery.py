# snake = [(1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5)]
snake = [(4, 5), (3, 5), (3, 4), (3, 3), (3, 2), (2, 2), (1, 2)]

# for x, y in snake:

#     if snake[x][0] > snake[x-1][0]:
#         odkud = "left"
#     if snake[y][1] > snake[y-1][1]:
#         odkud = "bottom"

#     if snake[x][0] < snake[x+1][0]:
#         kam = "right"
#     if snake[y][1] < snake[y+1][1]:
#         kam = "top"

#     print(snake[x][0], snake[y][1], odkud, kam)

# for x, y in snake:

#     if snake[x][y] >= snake[x-1][y-1]:
#         odkud = "left"
#     if snake[x][y] >= snake[x-1][y-1]:
#         odkud = "bottom"

#     if snake[x][0] < snake[x+1][0]:
#         kam = "right"
#     if snake[y][1] < snake[y+1][1]:
#         kam = "top"

#     print(snake[x][0], snake[y][1], odkud, kam)

for i in range(len(snake)):
    x = snake[i][0]
    y = snake[i][1]

    vysl = x - snake[i-1][0]
    if i != len(snake)-1:
        vysl2 = y - snake[i+1][1]

    if i == 0:
        source = "end"
    else:
        if vysl == 1:
            source = "left"
        elif vysl == -1:
            source = "right"
        elif vysl == 0:
            source = "bottom"
        else:
            source = "top"
    
    if i == len(snake)-1: 
        dest = "end"
    else:
        if vysl2 == -1:
            dest = "top"
        elif vysl2 == 1:
            dest = "bottom"
        elif vysl2 == 0:
            dest = "right"
        else:
            dest = "left"

    print(x, y, source, dest)

# for i in range(len(snake) +1):
#     if i < len(snake):
#         print(snake[i])