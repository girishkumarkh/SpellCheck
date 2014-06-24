def spellCheck(textFileName):
    """
    >>> spellCheck("test1.txt")
    {'exercsie': 1, 'finised': 1}
    >>> spellCheck("test2.txt")
    {'bechause': 1, 'c++': 1}
    >>> spellCheck("test3.txt")
    {'baylit': 1, '27': 1, 'goffin': 1, 'glenn': 1, 'texters': 1, 'psych-pop': 1, 'artstation': 1, 'award-wining': 1, 'psychedelists': 1, 'pop-folk': 1, 'ian': 1, 'davidson': 1, 'txt2': 2, 'cardiff': 3, 'grimstead': 1, '2010': 1, 'hip-hop': 1}
    >>> spellCheck("test4.txt")
    {'nuffield': 2, 'motor/neuron': 1, 'abnormailities': 1, 'cardiff': 1, 'swansea': 1, 'gower': 1, '3d': 2}
    """
    file = open("words.txt","r")
    wordsList = file.read().split()
    file.close()

    
    file = open(textFileName,"r")
    wordsToCheck = file.read().split()
    file.close()   
    
    for i in range(0,len(wordsList)): wordsList[i] = wordsList[i].replace("\n"," ")
    for i in range(0,len(wordsToCheck)): wordsToCheck[i]=wordsToCheck[i].replace("\n"," ")

    spellingErrors=dict()
    
    for key in wordsToCheck:
        key = key.lower()
        if key not in wordsList:
            if key not in spellingErrors:
                spellingErrors[key]=1
            else:
                spellingErrors[key]+=1
    return spellingErrors


