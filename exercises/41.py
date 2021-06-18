def existsFile(path):
    try:
        fileExistence = open(path)
    except:
        fileExistence = False
    else:
        fileExistence = True
    return fileExistence


existsFile("text.txt")
