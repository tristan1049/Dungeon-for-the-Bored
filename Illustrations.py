def dice1():
    """
    Purpose: To make an illustration for the 1-side of a die
    Output: List of each row in drawing
    """
    rv = [" _______ ",
          "|       |",
          "|   *   |",
          "|       |",
          "|_______|"]
    return rv
    
def dice2():
    """
    Purpose: To make an illustration for the 2-side of a die
    Output: List of each row in drawing
    """
    rv = [" _______ ",
          "| *     |",
          "|       |",
          "|     * |",
          "|_______|"]
    return rv

def dice3():
    """
    Purpose: To make an illustration for the 3-side of a die
    Output: List of each row in drawing
    """
    rv = [" _______ ",
          "| *     |",
          "|   *   |",
          "|     * |",
          "|_______|"]
    return rv

def dice4():
    """
    Purpose: To make an illustration for the 4-side of a die
    Output: List of each row in drawing
    """
    rv = [" _______ ",
          "| *   * |",
          "|       |",
          "| *   * |",
          "|_______|"]
    return rv

def dice5():
    """
    Purpose: To make an illustration for the 5-side of a die
    Output: List of each row in drawing
    """
    rv = [" _______ ",
          "| *   * |",
          "|   *   |",
          "| *   * |",
          "|_______|"]
    return rv
    
def dice6():
    """
    Purpose: To make an illustration for the 6-side of a die
    Output: List of each row in drawing
    """
    rv = [" _______ ",
          "| *   * |",
          "| *   * |",
          "| *   * |",
          "|_______|"]
    return rv

def match(roll_list):
    """
    Inputs: Takes in a list of dice roll integers
    Purpose: To match each number of a dice roll to an illustration
    Output: The list of strings of the illustration
    """
    rv = []
    dice_list = []
    for num in roll_list:
        if num == 1:
            dice_list.append(dice1())
        elif num == 2:
            dice_list.append(dice2())
        elif num == 3:
            dice_list.append(dice3())
        elif num == 4:
            dice_list.append(dice4())
        elif num == 5:
            dice_list.append(dice5())
        elif num == 6:
            dice_list.append(dice6())
            

    # Join 10 dice strings at a time as a line
    num_lines = ((len(dice_list)-1) // 10) + 1
    for line in range(num_lines):
        # Iterate through each row of the dice illustrations for line
        for j in range(len(dice_list[10*line])):                           
            row = ''
            # Iterate through each die for current row, joining all dice strings 
            # for that row into one string for correct printing
            for i in range(10*line, min(len(dice_list), 10*line + 10)):
                row += dice_list[i][j]
                row += '  '
            rv.append(row)

    return rv
            
            
