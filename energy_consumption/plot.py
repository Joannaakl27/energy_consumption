import plotly.express as px


def fossil_share_elec(df, value):

    if value == "All":

        fig = px.line(x=df["year"].unique(),
                    y=df.groupby('year').fossil_share_elec.mean())

    else:
        fig = px.line(x=df[df['country'] == value].year,
                      y=df[df["country"] == value].fossil_share_elec)

    return fig
