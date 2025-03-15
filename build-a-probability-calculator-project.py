import copy
import random

class Hat:
    def __init__(self, **contents):
        self.contents = []
        for key, times in contents.items():
            for _ in range(times):
                self.contents.append(key)

    def draw(self, qty):
        qty = min(qty, len(self.contents))
        takeouts = [self.contents.pop(random.randrange(len(self.contents))) for _ in range(qty)]
        return takeouts

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    balls_include = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        takeout_balls = hat_copy.draw(num_balls_drawn)
        ball_i = sum([1 for k, i in expected_balls.items() if takeout_balls.count(k) >= i])
        balls_include += 1 if ball_i == len(expected_balls) else 0
    
    print(balls_include)
    return balls_include / num_experiments
        

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)
