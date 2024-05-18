'''
    Provides the template for the hover tooltips.
'''
from modes import MODES


def get_hover_template(name, mode):
    '''
        Sets the template for the hover tooltips.

        The template contains:
            * A title stating player name with:
                - Font family: Grenze Gotish
                - Font size: 24px
                - Font color: Black
            * The number of lines spoken by the player, formatted as:
                - The number of lines if the mode is 'Count ("X lines").
                - The percent of lines fomatted with two
                    decimal points followed by a '%' symbol
                    if the mode is 'Percent' ("Y% of lines").

        Args:
            name: The hovered element's player's name
            mode: The current display mode
        Returns:
            The hover template with the elements descibed above
    '''
    # TODO: Generate and return the over template
    # Defining the hover content based on the mode
    if mode == MODES['count']:
        line_info = f"<br>%{{y}} {MODES['count']} lines"  # y will dynamically represent the count of lines
    elif mode == MODES['percent']:
        line_info = f"<br>%{{y:.2f}}% {MODES['percent']} of lines"  # y will dynamically represent the percentage

    # Defining the hover template with styling
    hover_template = f"""
    <b style='font-family: Grenze Gotish; font-size: 24px; color: black;'>{name}</b>
    {line_info}
    <extra></extra>
    """

    return hover_template
