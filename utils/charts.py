import plotly.express as px


def line_chart(df,x,y,title):

    fig = px.line(
        df,
        x=x,
        y=y,
        title=title,
        markers=True
    )

    return fig


def bar_chart(df,x,y,title):

    fig = px.bar(
        df,
        x=x,
        y=y,
        title=title
    )

    return fig


def scatter_chart(df,x,y,title):

    fig = px.scatter(
        df,
        x=x,
        y=y,
        title=title
    )

    return fig
