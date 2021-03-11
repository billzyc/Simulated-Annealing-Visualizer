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
        scale = np.sqrt(self.t_max)
        p_x, p_y, p_t = [], [], []
        initial_x = np.random.uniform(0, 25)
        initial_y = self.hill_function(initial_x)
        p_x.append(initial_x)
        p_y.append(initial_y)
        p_t.append(t)

        while(t > self.t_min):
            t = t-self.dt
            new_x = self.min_x - 1
            while(new_x < self.min_x or new_x > self.max_x):
                new_x = p_x[-1] + np.random.uniform(-1, 1)*scale
            new_y = self.hill_function(new_x)
            dy = new_y - p_y[-1]
            if dy > 0 or np.exp(dy/t) > np.random.rand():
                p_x.append(new_x)
                p_y.append(new_y)
            else:
                p_x.append(p_x[-1])
                p_y.append(p_y[-1])
            p_t.append(t)
        return {'x': p_x, 'y': p_y, 't': p_t}
