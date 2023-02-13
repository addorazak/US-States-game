import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another State "
                                                                                             "name?:").capitalize()

    # Exiting when not done
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # states_to_learn.csv
        missing_states_dic = {
            "states": missing_states
        }
        new_data = pandas.DataFrame(missing_states_dic)
        # Creates a new csv file with the states you couldn't guess right
        new_data.to_csv("states_to_learn.csv")
        break
    # If answer_state is one of the states in all the states of the 50_states.csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        # if they get it right:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Create a turtle to write the name of the state at the state's x and y coordinate
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# Use this code to get all the coordinates of each State
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
