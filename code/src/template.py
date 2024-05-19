'''
    Creates the theme to be used in our bar chart.
'''
import plotly.graph_objects as go
import plotly.io as pio

THEME = {
    'bar_colors': [
        '#861388',
        '#d4a0a7',
        '#dbd053',
        '#1b998b',
        '#A0CED9',
        '#3e6680'
    ],
    'background_color': '#ebf2fa',
    'font_family': 'Montserrat',
    'font_color': '#898989',
    'label_font_size': 16,
    'label_background_color': '#ffffff'
}


def create_template():
    '''
        Adds a new layout template to pio's templates.

        The template sets the font color and
        font to the values defined above in
        the THEME dictionary.

        The plot background and paper background
        are the background color defined
        above in the THEME dictionary.

        Also, sets the hover label to have a
        background color and font size
        as defined for the label in the THEME dictionary.
        The hover label's font color is the same
        as the theme's overall font color. The hover mode
        is set to 'closest'.

        Also sets the colors for the bars in
        the bar chart to those defined in
        the THEME dictionary.

    '''
    # TODO : Define a theme as defined above
    # Create a new template based on an existing template
    custom_template = go.layout.Template(
        layout=go.Layout(
            font=dict(
                color=THEME['font_color'],
                family=THEME['font_family']
            ),
            paper_bgcolor=THEME['background_color'],
            plot_bgcolor=THEME['background_color'],
            hovermode='closest',
            barmode='stack',
        ),
        data={
            'bar': [
                go.Bar(
                    marker=dict(
                        color=THEME['bar_colors']
                    ),
                    hoverlabel=dict(
                        bgcolor=THEME['label_background_color'],
                        font=dict(
                            size=THEME['label_font_size'],
                            color=THEME['font_color']
                        ),
                        bordercolor=THEME['font_color']
                    )
                )
            ]
        }
    )

    # Register this custom template under 'custom_template'
    pio.templates['custom_template'] = custom_template

# Call create_template to register the custom template
    return custom_template



