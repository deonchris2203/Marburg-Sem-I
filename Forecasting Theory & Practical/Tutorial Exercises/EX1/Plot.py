import matplotlib.pyplot as plt



fig, axes = plt.subplots(
    2, 1, figsize=(14, 9), sharex=True, sharey=True
)

plots = [
    (
        axes[0], "Raw ensemble",
        "ens_mean", "raw_lower", "raw_upper", "gray"
    ),
    (
        axes[1], "Gaussian EMOS",
        "emos_mean", "emos_lower", "emos_upper", "royalblue"
    )
]

for ax, title, mean_col, lower_col, upper_col, color in plots:
    ax.fill_between(
        test.index,
        test[lower_col].to_numpy(),
        test[upper_col].to_numpy(),
        color=color,
        alpha=0.25,
        label="90% prediction interval"
    )

    ax.plot(
        test.index, test[mean_col],
        color=color, linewidth=1.5, label="Predictive mean"
    )

    ax.plot(
        test.index, test["obs"],
        color="black", linewidth=1,
        marker=".", markersize=3, label="Observation"
    )

    ax.set_title(title)
    ax.set_ylabel("T2M (dataset units)")
    ax.grid(alpha=0.25)
    ax.legend(loc="best")

axes[-1].set_xlabel("Date")
fig.autofmt_xdate()
plt.tight_layout()
plt.show()