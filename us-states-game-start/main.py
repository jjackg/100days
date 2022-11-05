import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

def check_answer(answer_state):
    if answer_state in all_states:
        if answer_state in guessed_states:
            pass
        else:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(x = int(state_data.x), y = int(state_data.y))
            t.write(state_data.state.item())


while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt = "What's another State's name?").title()
    check_answer(answer_state)





#print(state_list)

