def rain(buildings):
    """How much rain is trapped in Codelandia?"""

    # variable for the "boundary" buildings
    # variable for amount of potential rain captured
    # variable for current running total of rain

    # loop through buildings
    # if there's a current boundry, calculate potential rain captured on top of the current building
    # when we get to another "boundary" building, add the potential rain captured to running total,
    # reset potential to 0
    # reset current "boundary" to the current building

    boundaries = []

    for i, height in enumerate(buildings[1:]):
        if height > buildings[i - 1] and height < buildings[i + 1]:
            boundaries.append(i)

    for boundary in boundaries:
        


        # if height > buildings[left]:
        #     left = i
        # elif height > buildings[i - 1]:
        #     right = i
        #     