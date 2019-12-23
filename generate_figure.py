import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
import pickle

def sent_vs_time():
    figsize = (7.2047, 3.5)
    fig, all_axes = plt.subplots(2, 1, sharex=True, figsize=figsize)
    lw = .3
    ms = 4
    ls = (0, (5, 5))
    ylim = [0.2, 0.7]
    plot_data_path = os.path.join('data', 'sentiment_vs_time_plot_data.pkl')
    plot_save_path = os.path.join('figures', 'sentiment_vs_time.png')

    # load plot data
    with open(plot_data_path, 'rb') as f:
        data = pickle.load(f)

    # This is needed for to_pydatetime() conversion (conversion between pandas and matplotlib datetime)
    register_matplotlib_converters()
    ax_sentiment, ax_activity  = all_axes

    # plot
    ax_sentiment.plot(data['sentiment']['x'], data['sentiment']['y'], '.', zorder=1, ms=ms)
    ax_activity.fill_between(data['activity']['x'], data['activity']['y'], zorder=1)
    ax_sentiment.plot(data['sentiment_loess']['x'], data['sentiment_loess']['y'])

    # set ylims on sentiment index
    for ax in all_axes:
        y_min, y_max = ax.get_ylim()
        diff = y_max - y_min
        if y_min != 0:
            y_min -= diff*.05
        y_max += diff*.05
        ax.set_ylim([y_min, y_max])
    if ylim is not None:
        ax_sentiment.set_ylim(ylim)

    # date xticks formatting
    ax_activity.xaxis.set_minor_locator(mdates.MonthLocator())
    ax_activity.xaxis.set_major_locator(mdates.YearLocator())
    ax_activity.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    # axis labels
    ax_sentiment.set_ylabel('Sentiment index $s$')
    ax_activity.set_ylabel('Daily counts')
    ax_activity.xaxis.label.set_visible(False)

    # remove space between plots
    plt.subplots_adjust(wspace=0, hspace=0.1)

    # Zero-sentiment line
    ax_sentiment.axhline(0, color='.8', lw=lw, zorder=-1)

    # tick direction
    ax_activity.tick_params(axis='x', direction='out', which='minor', zorder=2, size=2)
    ax_activity.tick_params(axis='x', direction='out', which='major', zorder=2, size=4)
    ax_activity.spines['bottom'].set_zorder(2)

    # save
    print(f'Saving figure to {plot_save_path}')
    plt.savefig(plot_save_path)

if __name__ == "__main__":
    sent_vs_time()
