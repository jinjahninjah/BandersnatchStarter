from altair import Chart, Tooltip


def chart(df, x, y, target) -> Chart:
    return Chart(
        df,
        title=f"{y} by {x} for {target}"
    ).mark_circle().encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.keys().tolist())
    ).properties(
        height=420,
        width=420,
    )
