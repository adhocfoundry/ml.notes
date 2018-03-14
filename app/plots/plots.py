import matplotlib.pyplot as plt


class Plots:
    def plt_ini(self, figw=16.0, figh=6.0, rows=1, cols=1):
        fig, axes = plt.subplots(cols, rows, sharex=True, sharey=True,
                                 figsize=(figw, figh))
        plt.subplots_adjust(left=1 / figw, right=1 - 1 / figw, bottom=1 / figh, top=1 - 1 / figh)

        # Initialize the figure
        plt.style.use('seaborn-darkgrid')
        return fig, axes