
if __name__ == "__main__":
    
    #git init = Starts git on a project
    
    #git status = know if the files are commited
    
    #git add = decide with files are going to the stage that then go to the commit
    
    #git commit = save a state of the project in a specific moment like a photo
    
    #git checkout = can be used to move between commints and restoring by the file name to the last commit that we made it 
    
    #git reset (--hard --soft --mixed) == --hard(with this we delete all, the commit and also the changes that we do there)
                                        # --soft(with this we only remove the commit but we have all the files on the stage we 
                                        # can add and modifed the mesagge of the commit but we can modified the files that already
                                        # load in the stage)
                                        # --mixed(is too similar to the soft but here the files aren't in the stage so we can modifed but we
                                        # need to add it to the stage with git add. )
                                        
    #git reflog = here we can see all the things that we make with git
    
    #alis = git config --global alias.s '!git status && git log --oneline' with that we can resume commands of the git 

    #git diff = works to see the diff between 2 branch and 2 commints
    
    #git tag = with this we can say here something important happend in this commit more commun is used when we have a importan realse like v1
    
    #git branch "namenewbranch" = with this we can create a new branch were we can develop asasynchronously of the main branch they can impruve
    #                             the code of the main and we don't have it in the branch that we are working this also influes in the main we can work
    #                             and we don't have the others branch that can be functions that we going to use in the main but they are developing but we 
    #                             also need to continue with the main so for this is what its for 
    
    #git switch = works to change beetween branch 
    
    #git merge "branch to merge on the branch that we are" = with this we bring the code from other branch that is developing, and we add to our branch to see if 
    #                                                        it work fine 
    
    #git stash = works like a commit but temp cuz imagin that you are working on a branch but u need urgently move to another but you doesn't 
    #           finish the word on this branch so you need to save it but make a commit is not the best way cuz you commit an incomplete thing so that 
    #           is a bad pratice and your team will not know what to do so you can save it local so no one will know about it so then you can continue with the development 
    
    #conflicts resolution so imagine that you modifed the code of other branch and you try to merge it so you will get a conflict cuz that code you didn't need to modifed so will 
    #           see your code on the files that you never need to modifed but you do it idk the reason and also the code of the team that work on that so your team and the other
    #           need to decide which code is the better and finally the best way to avoid this is decide how is going to change something more communication  
    
    #To merge something of other branch to the main we do the same git merge "branch" and thats it
    
    #Git Hub 
    
    print("Hello world")
    