import copy
def Sort(SourceLists,ReferenceList,Reverse = False):
    #Sorts a list of lists -> SourceLists, based on a reference list
    SourceLists = copy.deepcopy(SourceLists)    #Makes a copy of both lists
    ReferenceList = copy.deepcopy(ReferenceList)
    
    for List in SourceLists: #Checks each list, if not the same length as the reference list : will raise error
        if len(List) != len(ReferenceList):
            raise ValueError("A list to be sorted is not equal in length to the reference list, aborting")
        
    NewLists = []
    for x in range(len(SourceLists)):
        NewLists.append([])         #Creates a new list of lists to store the sorted lists in

    while len(ReferenceList) != 0:  #While not all items have been sorted into new lists
        if not Reverse:
            index = ReferenceList.index(min(ReferenceList))  #if not reverse gets the index of the smallest item in the reference list
        else:
            index = ReferenceList.index(max(ReferenceList))  # if reverse gets the maximum one
        ReferenceList.pop(index) #removes the min/max-imum item from reference list
        
        for x in range(len(SourceLists)): #Goes through all the Source Lists and adds them to the respective sorted list
            NewLists[x].append(SourceLists[x][index])
            SourceLists[x].pop(index)  #Removes the item from the original list
            
    return NewLists
        
