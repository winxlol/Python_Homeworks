rows = int(input())


maze = []

for row in range(rows):
    current_row = input()

    current_row = [el for el in current_row]

    maze.append(current_row)

while True:

    for maze_row in range(len(maze)):
        if "k" in maze[0] or "k" in maze[-1]:
            break
        for index, position_info in enumerate(maze[maze_row]):
            if position_info == "k":
                k_position = index

                if maze[maze_row][index - 1] == " ":
                    maze[maze_row][index - 1] = "k"
                    maze[maze_row][index] = "#"
                elif maze[maze_row][index + 1] == " ":
                    maze[maze_row][index + 1] = "k"
                    maze[maze_row][index] = "#"
                elif maze[maze_row - 1][index] == " ":
                    maze[maze_row - 1][index] = "k"
                    maze[maze_row][index] = "#"
                elif maze[maze_row + 1][index] == " ":
                    maze[maze_row + 1][index] = "k"
                    maze[maze_row][index] = "#"

                flag = True

