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
    Inputs: Takes in a dice roll number
    Purpose: To match a number to an illustration
    Output: The list of strings of the illustration
    """
    rv = []
    
    for num in roll_list:
        
        if num == 1:
            rv.append(dice1())
        
        elif num == 2:
            rv.append(dice2())
        
        elif num ==3:
            rv.append(dice3())
        
        elif num == 4:
            rv.append(dice4())
        
        elif num == 5:
            rv.append(dice5())
        
        else:
            rv.append(dice6())
            
            
            
            
    new = []
    for j in range(len(rv[0])):                                                         #This allows for an illustration of any number of dice
        
        row = ''
        for i in range(len(rv)):
        
            row += rv[i][j]
            row += '  '
            
        new.append(row)
        
    return new
            
            
