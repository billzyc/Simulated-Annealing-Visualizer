import matplotlib.animation
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import os
from SA import SA


def main():

    min_x, max_x = 0, 30
    t_max = 1000
    t_min = 0
    dt = 0.05
    fig, ax = plt.subplots()

    annealer = SA(min_x, max_x, t_max, t_min, dt)
    p = annealer.run()
    p_x, p_y, p_t = p['x'], p['y'], p['t']
    x, y, t = p_x[0], p_y[0], p_t[0]
    sc = ax.scatter(x, y)
    t_text = ax.text(0, 8, f't={t:.1f}')

    def animate(i):
        x = p_x[i]
        y = p_y[i]
        t_text.set_text(f't={p_t[i]:.1f}')
        sc.set_offsets(np.c_[x, y])

    ani = matplotlib.animation.FuncAnimation(fig, animate,
                                             frames=len(p_x), interval=1, repeat=False)

    hill_x, hill_y = annealer.plot_hill()
    plt.plot(hill_x, hill_y, color='black')
    writervideo = animation.FFMpegWriter(fps=60)

    figure_num = 1
    while os.path.exists(f'./animation{figure_num}.mp4'):
        figure_num += 1
    ani.save(f'./animation{figure_num}.mp4',
             writer=writervideo)
    print(f'plot saved to ./animation{figure_num}.mp4')


if __name__ == '__main__':
    main()
