import numpy as np


class SA:
    def __init__(self, min_x, max_x, t_max, t_min, dt):
        self.min_x = min_x
        self.max_x = max_x
        self.t_max = t_max
        self.t_min = t_min
        self.dt = dt

    def hill_function(self, x):
        return x*np.cos(x)

    def plot_hill(self):
        x = np.linspace(self.min_x, self.max_x, 1000)
        y = self.hill_function(x)
        return (x, y)

    def run(self):
        t = self.t_max

        p_x, p_y, p_t = [], [], []
        initial_x = np.random.uniform(0, 25)
        initial_y = self.hill_function(initial_x)
        p_x.append(initial_x)
        p_y.append(initial_y)

        while(t > self.t_min):
            p_t.append(t)
            new_x = np.random.uniform(0, 25)
            new_y = self.hill_function(new_x)
            dy = new_y - p_y[-1]
            if dy > 0 or np.exp(dy/t) > np.random.rand():
                p_x.append(new_x)
                p_y.append(new_y)
            t = t-self.dt
        return {'x': p_x, 'y': p_y, 't': p_t}
