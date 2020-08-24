# alas-for-the-javascript
Character management for Alas for the Awful Sea. I assume you could modify it for any other Powered by the Apocalypse.

Runs on Python 3 and JavaScript+HTML

Key library for Python is Flask, which also means that I am using the virtual environment that you find more about in the their quickstart. Let me know, how this goes.

Don't forget to change the IP address in the bat file. This can be found in ipconfig in cmd.exe.

The guiding star for this project is ease of play but I suspect you're better off using a paper sheet

Version progression:


    Version 0.1
        1. Create a button that updates the healthpoints    DONE
            This would be done through the form thing and plain text edit
        2. Create a form for making a new character         DONE
            Simple form site that the backend process
        3. Create a page to select an existing character    DONE
        4. Create a character page                          DONE
            Name, Appearance, Stats, Equipment and Special move can be printed as they are given
            How to do bonds? How are they saved?
                For an existing character, it is fine to have the bonds as simple made text
                So there would be a new character form file and a created character file
        5. Landing page that has                            DONE
            Links to Existing characters
            Link to New character creation
        
    Version 0.5
        1. Improve the create a new character               DONE    
            Have X links, maybe do a table
                Can I have it as an argument in the webpage?
                Try to have one page with a NEXT button that hides and shows previous content
            There needs to be a thing that cancels it
                This could be done by saving the file if and only if there has been a sufficient number of NEXTs
            One character, one file to avoid saving weirdness
        2. Propagate file changes everywhere                DONE? Not sure what I meant by this
        3. Redirection when finished making a character     DONE
        5. Add checks on stats                              DONE
        
    Version 0.6
        1. Put everything in a table
        2. Finish everything on a character
            1. Name and Appearance
                    Appearance would be radio buttons
            2. Stats
            3. Bonds
                Simple fields as an entry
            4. Special move info
            5. Equipment info
    
    Version 1.0     
        1. Finish all the characters
        2. Add a link to basic moves
            This might be as an option on a character sheet and it would be hide and display
            
            
    Version 1.5
        1. Create tales???   
        
        
    Version X
        1. Add town sheet
