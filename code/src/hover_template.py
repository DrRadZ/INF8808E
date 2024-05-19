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
    #Displaying Act number as title and number of lines or % of lines depending on mode based on requirement from subject tp2
    if mode=='Count':
        hover_template =('<span style="font-family: Grenze Gotisch; font-size: 24px; font-color: Black">%{x}</span><br></br>'
        +'<br><b></b>%{y} lines</br><extra></extra>')
    else:
        hover_template =('<span style="font-family: Grenze Gotisch; font-size: 24px; font-color: Black">%{x}</span><br></br>'
        +'<br><b></b>%{y}% of lines</br><extra></extra>')
    return hover_template

