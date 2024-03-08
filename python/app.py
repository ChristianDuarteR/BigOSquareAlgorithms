import matplotlib

import executing_time_gathering
import matplotlib.pyplot as plot

matplotlib.use('TkAgg')
import pandas as pd

if __name__ == "__main__":
    minimum_size = 500
    maximum_size = 1500
    step = 50
    samples_by_size = 5

    table = executing_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)
    df = pd.DataFrame(table,
                      columns=["Size", "Bubble Improved",
                               "Shell Sort", "Longest SubSqe"])
    print(df)

    df.plot(x="Size",
            y=["Bubble Improved", "Shell Sort", "Longest SubSqe"], kind="line", marker="x")

    plot.plot(df)
    plot.show()
