classDiagram
    class TennisGame {
        +int num_balls
        +list balls
        +int ball_speed
        +float speed_increase_percentage
        +turtle.Screen screen
        +turtle.Turtle paddle
        +int score
        +turtle.Turtle score_display

        +__init__(num_balls: int)
        +create_balls()
        +move_paddle()
        +move_balls()
        +randomize_ball_angle(ball: turtle.Turtle)
        +adjust_ball_angle(ball: turtle.Turtle)
        +draw_walls()
        +game_over()
        +play_game()
    }

    class turtle.Turtle {
        +void shape()
        +void color()
        +void penup()
        +void setx(x: int)
        +void sety(y: int)
        +void goto(x: int, y: int)
        +void write()
        +void hideturtle()
        +void clear()
        +void speed()
        +void pensize()
        +void pendown()
    }

    class pyautogui {
        +tuple position()
    }

    TennisGame "1" *-- "*" turtle.Turtle : uses
    TennisGame "1" *-- "*" pyautogui : uses
    turtle.Turtle "1" o-- "*" pyautogui : used by
