import fs
import fs.move
import os
import re
foundMusic = False
#gets the file system
fileSystem = fs.open_fs('c:/')
#prints the contents of the folder
print(fileSystem.listdir('/Users/Alan Gervin/Documents/GitHub/SortScript/sortFolder/'))
#give a variable name sortFolder to the path provided
sortFolder = '/Users/Alan Gervin/Documents/GitHub/SortScript/sortFolder/'
#
Movies = '/Users/Alan Gervin/Documents/GitHub/SortScript/FinalSorted/Movies/'
Music = '/Users/Alan Gervin/Documents/GitHub/SortScript/FinalSorted/Music/'
TV = '/Users/Alan Gervin/Documents/GitHub/SortScript/FinalSorted/TV/'

def renameItem(item):
    #item we are going to search for rename
        #itemToLower = item.lower()
        resultForE = re.search(r'[E]+\d(\b)', item)
        nameArry = []
        for char in item:
            nameArry.append(char)
        print(nameArry)
        #print(resultForE.span()[0])
        if resultForE:
            startNumber = resultForE.span()[0]
            
            firstCall = slice(0, startNumber)
            startName = nameArry[firstCall]
            startNameFinal = ''
            startName.insert(startNumber-1, '0')
            for char in startName:
                startNameFinal+=char
            
            print(startNameFinal)
            
            midName = '0'
            
            endNumber = resultForE.span()[0]
            #print('this is endNumber'+str(endNumber))
            secondCall = slice(endNumber,len(nameArry))
            endName = nameArry[secondCall]
            endNameFinal = ''
            endName.insert(1, '0')
            for char in endName:
                endNameFinal+=char
            
            print(endNameFinal)
        
            episodeName = startNameFinal+endNameFinal
            print(episodeName)
            return episodeName
        else:
            return item
        


#lists every item in the sortFolder path
for item in fileSystem.listdir(sortFolder):
    
    #print(item)
    titleOriginal = str(item)
    title = titleOriginal.lower()
    print(title+"THIS WAS THE TITLE")

    #if item contains tv in the folder name create folder in final sorted TV folder
    foundTv = title.find('tv')
    if foundTv != -1:
        #print(fileSystem.listdir('/Users/Alan Gervin/Documents/GitHub/SortScript/FinalSorted/TV'))
        #renames folder to have S0 and E0 and creates the folder
        FinalName = (renameItem(titleOriginal))
        print('this is Final NAME >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'+FinalName)
        try:     
            # define the name of the directory to be created
            path = os.path.join(TV,FinalName)
            if not os.path.isdir(path):
                os.mkdir(path)
            print(fileSystem.listdir(TV))
        except:
            #make a directory for item
            print('error series folder not made for {}'.format(title))
    
        #rename folder to have proper name
        sortfolderDir = os.path.abspath('c:/'+sortFolder)
        print(sortfolderDir+"This is the sort folder DDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
        os.chdir(sortfolderDir)
        os.rename(titleOriginal,FinalName)

        #change to new file name    
        newPath = 'c:/'+sortFolder+FinalName

        try:
            os.chdir(os.path.abspath(newPath))
            print(os.getcwd())
        except OSError as error:
            print(error)

        for doc in os.path.join(sortFolder, FinalName):
            print(doc)
        #rename files and copy them to path
        #
        # print(os.path.join(sortFolder,FinalName))
        print(os.getcwd())
        
        for doc in fileSystem.listdir(os.path.join(sortFolder,FinalName)):
            print(doc+'FOLDER NAME')
            finalDocName = renameItem(doc)
            print(finalDocName+'THIS IS FINAL DOC')
            originalPath = os.path.join(sortFolder, FinalName)
            
            try:
                os.chdir(originalPath)
                print(os.getcwd())
            except OSError as error:
                print(error)
            
            os.chdir(originalPath)
            try:   
                os.rename(doc, finalDocName)
            except OSError as error:
                print('happened first')
                print(error)

            


    #get contents of the folder and check if there is a mp3
    content = fileSystem.listdir(os.path.join(sortFolder,FinalName))
    if content:
        for item in content:
            print(item)
            #sort item to music if has .MP3
            if item.find('.mp3') != -1:
                foundMusic = True;    

    #makes folder in Music folder   
    if foundMusic == True:
        FinalName = (renameItem(item))
        parent_dir = Music
        path = os.path.join(parent_dir,FinalName)
        if not os.path.isdir(path):
            os.mkdir(path)
        foundMusic = False
        itemToLower = item.lower()

    else:
        FinalName = (renameItem(item))
        #makes folder in Movies folder
        parent_dir = Movies
        path = os.path.join(parent_dir,FinalName)
        if not os.path.isdir(path):
            os.mkdir(path)

      
        #end = nameArry[secondCall]




