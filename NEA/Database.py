import sqlite3
import random
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')

#CONNECT TO DATABASE
conn = sqlite3.connect('Football.db')
c = conn.cursor()
#CREATES DATABASE TABLES IS THEY DO NOT EXIST
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS playerdetails(firstname TEXT, lastname TEXT, squadnumber INT, age INT, position TEXT)') #creates playerdetails table
    c.execute('CREATE TABLE IF NOT EXISTS gamestats(squadnumber TEXT, gamesplayed INT, goals INT, assists INT, yellowcards INT, redcards INT )') #creates gamestats table


    
create_table()

###-----------------------------------------------------LOGIN WINDOW---------------------------------------------------
def getuser():
    text = entusername.get() #gets the value entered in the unsername entry box
    password = entpass.get() #gets the value entered in the password entry box
    text = text.upper() #turns the variable into uppercase text
    #CHECKS THE LOGIN 
    if text == "AARON" and password == "password": #checks the inputs with accepted values
        lbl2.configure(text="Acess granted") #changes label to the text
        mainmenu() #opens the main menu
        window.destroy() #destroys login window
    else:
        lbl2.configure(text= "Access denied") #turns label into text
        messagebox.showinfo("ERROR","Please enter the correct username and password to successfully login.") #call message box to display error message
   
    
#CREATE LOGIN WINDOW
window = Tk()
window.title('Welcome')
window.geometry("335x200")
window.configure(background="crimson")

#CREATE TITLE 
lblnst = Label(window, text="Welcome, please login to continue: ", bg="crimson", font=("Helvetica",16))
lblnst.pack()

#CREATE USERNAME ENTRY BOX
lblusername = Label(window, text="Username:", bg="crimson", font=("Helvatica",12)) 
entusername = Entry(window) #creates variable for data entered
lblusername.pack()
entusername.pack()

#CREATE PASSWORD ENTRY BOX
lblpassword = Label(window, text ="Password:", bg="crimson", font=("Helvatica",12))
entpass = Entry(window,show='*') #creates variable for data entered
lblpassword.pack()
entpass.pack()

#LOGIN BUTTON
btn = Button(window, text="Login",command=getuser,bg="white")
btn.pack()

#LABEL TO SAY IF ACCESS HAS BEEN GAINED
lbl2 = Label(window, text="", bg="crimson" )
lbl2.pack()




###--------------------------------------MAIN MENU-------------------------------------------------------
def mainmenu():
    #CREATE WINDOW
    window2 = Tk()
    window2.title("Main Menu")
    window2.geometry("800x300")
    window2.configure(background="crimson")
    
    #CREATE TITLE LABEL
    mainlabel = Label(window2, text = "What would you like to do?",bg="crimson",font=("Cooper Black",16))
    mainlabel.grid(row=1,column=2,padx=10,pady=10)
    
    #VIEW TEAM BUTTON
    viewteam = Button(window2, text="View team", font=("Ariel",18), command=viewteamm)
    viewteam.grid(column=1,row=2,padx=10,pady=10)

    #EXIT PROGRAM
    exitb = Button(window2,text="Exit", font=("Ariel",23),command=exit)
    exitb.grid(column=6,row=1,padx=10,pady=10)

    #DELETE PLAYER BUTTON
    deleteplayer = Button(window2, text="Delete player", font=("Ariel",18), command=delplayer)
    deleteplayer.grid(column=1,row=3,padx=10,pady=10)

    #ADD PLAYER BUTTON
    addplayer = Button(window2, text="Add player" ,font=("Ariel",18), command=addplayerr)
    addplayer.grid(column=3,row=2,padx=10,pady=10)

    #EDIT PLAYER BUTTON
    editplayer =Button(window2,text="Edit player",font=("Ariel",18), command=editplayerr)
    editplayer.grid(column=3,row=3,padx=10,pady=10)

    #DELETE ALL BUTTON
    deleteall=Button(window2,text="Delete All",font=("Areil",18),command=deletealll)
    deleteall.grid(column=2,row=4,padx=10,pady=10)

    
###-----------------------------------------------------VIEW TEAM-------------------------------------
def viewteamm():

    def createallgraph(yaxis):
        #GETS DATA TO BE PLOTTED
        c.execute('SELECT lastname FROM playerdetails')
        data = c.fetchall()

        x_axis=[]
        y_axis=[]

        #PUTS DATA INTO LISTS FOR X AND Y AXIS
        for row in data:
            x_axis.append(row[0])
        
        for row in yaxis:
            y_axis.append(row[0])

        #PLOTS THE GRAPH
        plt.bar(x_axis, y_axis, align='center')
        plt.xlabel('Player')
        plt.legend()
        plt.show()        

    #SELECTS GOALS FROM TABLE AND RETURNS YAXIS TO PLOT IN GRAPH
    def creategraphgoals():
        c.execute('SELECT goals FROM gamestats')
        yaxis = c.fetchall()
        createallgraph(yaxis)
    #SELECTS ASSISTS FROM TABLE AND RETURNS YAXIS TO PLOT IN GRAPH 
    def creategraphassists():
        c.execute('SELECT assists FROM gamestats')
        yaxis=c.fetchall()
        createallgraph(yaxis)
    #SELECTS YELLOW CARDS FROM TALE AND RETURNS YAXIS TO PLOT IN GRAPH 
    def creategraphyellow():
        c.execute('SELECT yellowcards FROM gamestats')
        yaxis=c.fetchall()
        createallgraph(yaxis)
    #SELECTS RED CARDS FROM TABLE AND RETURNS YAXIS TO PLOT IN GRAPH
    def creategraphred():
        c.execute('SELECT redcards FROM gamestats')
        yaxis=c.fetchall()
        createallgraph(yaxis)
    #SELECTS GAMES PLAYED FROM TABLE AND RETURNS YAXIS TO PLOT IN GRPAH
    def creategraphplayed():
        c.execute('SELECT gamesplayed FROM gamestats')
        yaxis=c.fetchall()
        createallgraph(yaxis)


        
    def allplayergraph():
        #CREATE WINDOW
        playerg=Tk()
        playerg.title("Graph")
        playerg.geometry("800x200")
        playerg.configure(background="crimson")
        #TITLE LABEL
        question = Label(playerg, text= "What would you like to compare?",bg="crimson",font=("Cooper Black",16))
        question.grid(column=3,row=1,padx=10,pady=10)
        #GETS DATA FOR GOALS SCORED
        goalsb = Button(playerg, text="Goals", font=("Ariel",16),command=creategraphgoals)
        goalsb.grid(column=1,row=3,padx=10,pady=10)
        #GETS DATA FOR ASSISTS MADE                  
        assistsb = Button(playerg, text="Assists", font=("Ariel",16),command=creategraphassists)
        assistsb.grid(column=2,row=3,padx=10,pady=10)
        #GETS DATA FOR GAMES PLAYED                    
        gamesplayedb=Button(playerg, text="Games Played", font=("Ariel",12),command=creategraphplayed)
        gamesplayedb.grid(column=3,row=3,padx=10,pady=10)
        #GETS DATA FOR YELLOW CARDS                    
        yellowb=Button(playerg, text="Yellow Cards", font=("Ariel",12),command=creategraphyellow)
        yellowb.grid(column=4,row=3,padx=10,pady=10)
        #GETS DATA FOR RED CARDS RECIEVED                    
        redb =Button(playerg, text="Red Cards", font=("Ariel",12),command=creategraphred)
        redb.grid(column=5,row=3,padx=10,pady=10)
        #CANCEL BUTTON
        cancelb = Button(playerg, text="Cancel", font=("Ariel",12),command=playerg.destroy)
        cancelb.grid(column=5,row=1,padx=10,pady=10)

    





    def oneplayergraph():
        
        def checkandgraph():
            squadnum = enter.get()
            x_axis=['Games Played','Goals','Assists','Yellow Cards','Red cards']
            y_axis=[]
            #CHECKS TO SEE IF THE SQUADNUMBER EXISTS
            c.execute('''SELECT * FROM playerdetails WHERE squadnumber = ?''', (squadnum,))
            check = c.fetchone()
            if check is None:
            #PRODUCES ERROR MESSAGE
                error1.configure(text="This player does not exist")
            else:
            #ENTERS DATA FOR Y xis
                c.execute('''SELECT gamesplayed, goals, assists, yellowcards, redcards FROM gamestats WHERE squadnumber = ?''', (squadnum,))
                player = c.fetchall()
                for column in player:
                    y_axis.append(column[0])
                    y_axis.append(column[1])
                    y_axis.append(column[2])
                    y_axis.append(column[3])
                    y_axis.append(column[4]) #puts the player details in the y axis list

                c.execute('''SELECT firstname, lastname FROM playerdetails WHERE squadnumber = ?''', (squadnum,))
                name=c.fetchall() #selects the player name from the database and puts it as the title of the bar chart
                #CREATE BAR CHART
                plt.bar(x_axis, y_axis, align='center')
                plt.title(name)
                plt.legend()
                plt.show()


        #CREATES WINDOW AND TITLE LABEL
        selectplayer = Tk()
        question = Label(selectplayer, text= "Which player would you like to see?",bg="crimson",font=("Cooper Black",16))
        selectplayer.title("Graph")
        selectplayer.geometry("500x200")
        selectplayer.configure(background="crimson")
        
        #TELLS THEM WHAT TO DO
        instruc = Label(selectplayer, text= "Enter the player squadnumber",bg="crimson",font=("Cooper Black",16))
        instruc.grid(column=2,row=1,padx=10,pady=10)
        #CREATE THE ENTER BUTTON
        enter = Entry(selectplayer)
        enter.grid(column=2,row=2,padx=10,pady=10)
        enterb = Button(selectplayer, text="Enter", font=("Ariel",12),command=checkandgraph)
        enterb.grid(column=2,row=3,padx=10,pady=10)
        #CREATES ERROR MESSAGE
        error1 = Label(selectplayer,text="",bg="crimson",font=("Ariel",12))
        error1.grid(column=2,row=4,padx=10,pady=10)
        #CREATES EXIT BUTTON
        exitwindow = Button(selectplayer,text="Exit",font=("Ariel",18),command=selectplayer.destroy)
        exitwindow.grid(column=3,row=1,padx=10,pady=10)



            
            
    def graphdata():
        graphdata=Tk()
        graphdata.title("Graph Data")
        graphdata.geometry("800x200")
        graphdata.configure(background="crimson")
        
        #MAIN LABEL
        question = Label(graphdata, text = "What would you like to make a graph on?", bg="crimson",font=("Cooper Black",16))
        question.grid(column=2,row=1,padx=10,pady=10)

        #BUTTON TO GRAPH ALL PLAYERS
        allplayers = Button(graphdata, text="All Players", font=("Ariel",18),command=allplayergraph)
        allplayers.grid(column=1,row=2,padx=10,pady=10)
        #BUTTON TO GRAPH ONE PLAYER
        oneplayer= Button(graphdata,text="One player", font=("Ariel",18),command=oneplayergraph)
        oneplayer.grid(column=3,row=2,padx=10,pady=10)
        #EXIT
        exit1 = Button(graphdata,text="Exit",font=("Ariel",18),command=graphdata.destroy)
        exit1.grid(column=3,row=1,padx=10,pady=10)


    #SELECT DATA FROM DATABASE
    c.execute('''SELECT firstname, lastname, playerdetails.squadnumber, age, position, gamesplayed, goals, assists, yellowcards, redcards from playerdetails, gamestats WHERE playerdetails.squadnumber = gamestats.squadnumber ''')
    playerdetails = c.fetchall()
    
    #CREATES TABLE
    viewteam= Tk()
    viewteam.title("Team")
    viewteam.configure(background="crimson")
    tree = ttk.Treeview(viewteam, columns=('col1','col2','col3','col4','col5','col6','col7','col8','col9','col10'))

    #GIVES COLUMNS HEADINGS
    tree.column('col1', width=100, anchor='center')
    tree.column('col2', width=100, anchor='center')
    tree.column('col3', width=100, anchor='center')
    tree.column('col4', width=100, anchor='center')
    tree.column('col5', width=100, anchor='center')
    tree.column('col6', width=100, anchor='center')
    tree.column('col7', width=100, anchor='center')
    tree.column('col8', width=100, anchor='center')
    tree.column('col9', width=100, anchor='center')
    tree.column('col10', width=100, anchor='center')
    tree.heading('col1', text='Firstname')
    tree.heading('col2', text='Last Name')
    tree.heading('col3', text='Squadnumber')
    tree.heading('col4', text='Age')
    tree.heading('col5', text='Position')
    tree.heading('col6', text='Games Played')
    tree.heading('col7', text='Goals')
    tree.heading('col8', text='Assists')
    tree.heading('col9', text='Yellow Cards')
    tree.heading('col10', text='Red Cards')

    #INSERTS DATA INTO TABLE
    for row in playerdetails:
        tree.insert('', 'end', text="", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8] ,row[9]))
    tree.grid(column=1,row=1,padx=1,pady=1)
    
    #EXIT BUTTON
    exitt = Button(viewteam,text="Exit", font=("Ariel",18),command=viewteam.destroy)
    exitt.grid(column=2,row=1,padx=5,pady=10)

    #GRAPH BUTTON
    graphforall = Button(viewteam,text="Graph", font=("Ariel",18),command=graphdata)
    graphforall.grid(column=1,row=2,padx=1,pady=10)

    


###----------------------------------------DELETING A PLAYER-------------------------------------------
def delplayer():

    #DELETES PLAYER FROM DATABASE
    def del_and_update():
        delete = squad_number.get()
        #CHECKS TO SEE IF THE SQUADNUMBER EXISTS
        c.execute('''SELECT * FROM playerdetails WHERE squadnumber = ?''', (delete,))
        check = c.fetchone()
        if check is None:
        #PRODUCES ERROR MESSAGE
            error_lbl.configure(text="This player does not exist")
        else:
            c.execute('''DELETE FROM playerdetails WHERE playerdetails.squadnumber = ? ''',(delete,))
            c.execute('''DELETE FROM gamestats WHERE gamestats.squadnumber = ? ''',(delete,)) #deltes data from player with matching squad number from both tables in the database
            error_lbl.configure(text="This player has been deleted") #tells user the player has been successfully deleted
            squad_number.delete(0,END)
            conn.commit()

    #CREATES WINDOW
    delplayer = Tk()
    delplayer.title("Delete player")
    delplayer.geometry("500x500")
    delplayer.configure(background="crimson")

    #TABLE LABEL
    deleteplayer=Label(delplayer, font=("Ariel",20), text="Delete Player", background="crimson")
    deleteplayer.grid(column=1,row=1,padx=10,pady=10)

    #NAME LABEL
    squadnum = Label(delplayer,font=("Ariel",12),text="Player Squadnumber", background="crimson")
    squad_number = Entry(delplayer)
    squadnum.grid(column=1,row=2,padx=10,pady=10)
    squad_number.grid(column=2,row=2,padx=10,pady=10)

    #DELETE BUTTON
    delplayerb = Button(delplayer,text="Delete Player", font=("Ariel",23),command=del_and_update)
    delplayerb.grid(column=2,row=3)

    #ERROR LABEL
    error_lbl = Label(delplayer,text="",bg="crimson",font=("Ariel",12))
    error_lbl.grid(column=2,row=4,padx=10,pady=10)

    #CREATES EXIT BUTTON
    exitb = Button(delplayer,text="Exit", font=("Ariel",23),command=delplayer.destroy)
    exitb.grid(column=5,row=1,padx=10,pady=10)

###-----------------------------------------ADD A PLAYER---------------------------------------------
def addplayerr():

    #ADDS PLAYER TO DATABASE
    def user_input():
        first_name = player_firstname.get()
        last_name = player_lastname.get()
        age_ = age.get()
        position_ = variable.get()
        gamesplayed_ = games_played.get()
        goals_ = goals_scored.get()
        assists_ = assist.get()
        yellowcards_ = yellow_cards.get()
        redcards_ = red_cards.get()
        squadnumber = squad_number.get() #gets the variables from the entry boxes
        c.execute('''SELECT * FROM playerdetails WHERE squadnumber = ?''', (squadnumber,))
        check_exists = c.fetchone()
        if len(first_name)>15:
            messagebox.showinfo("ERROR","Please enter make sure the firstname of the player is less than 16 characters and only contains text.") #checks to see if firstname is less than 15 characters
        elif len(last_name)>15:
            messagebox.showinfo("ERROR","Please make sure the surname of the player is less than 16 characters and only contains text.") #checks that only text has been entered
        elif len(age_) > 2 :
            messagebox.showinfo("ERROR","Please make sure the age of the player is a umber and is smaller than 100.") #checks the age entered is less than 100
        elif check_exists is not None:
            messagebox.showinfo("ERROR","A player with that squad number already exists.") #checks the player exists in the database
        elif first_name.isalpha() and last_name.isalpha() and age_.isdigit() and gamesplayed_.isdigit() and goals_.isdigit() and assists_.isdigit() and yellowcards_.isdigit() and redcards_.isdigit() and squadnumber.isdigit(): 
            c.execute("INSERT INTO playerdetails(firstname, lastname, squadnumber, age, position) VALUES (?, ?, ?, ?, ?)",
                        (first_name, last_name, squadnumber, age_, position_))
            c.execute("INSERT INTO gamestats(squadnumber, gamesplayed, goals, assists, yellowcards, redcards) VALUES (?, ?, ?, ?, ?, ?)",
                      (squadnumber, gamesplayed_, goals_, assists_, yellowcards_, redcards_))  #checks to see if if correct characters/number have been enterd and if so adds the player into the database
            player_firstname.delete(0,END)
            player_lastname.delete(0,END)
            age.delete(0,END)
            position = ""
            games_played.delete(0,END)
            goals_scored.delete(0,END)
            assist.delete(0,END)
            yellow_cards.delete(0,END)
            red_cards.delete(0,END)
            squad_number.delete(0,END) #clears the entry boxes
            conn.commit()
        else:
            messagebox.showinfo("ERROR","Please make sure the correct details have been entered in the correct format.") #displays error message

    #CREATE WINDOW
    addplayer = Tk()
    addplayer.title("Add player")
    addplayer.geometry("500x600")
    addplayer.configure(background="crimson")

    #CREATE ADDPLAYER LABEL
    newplayer=Label(addplayer, font=("Ariel",20), text="Add player", background="crimson")
    newplayer.grid(column = 1, row = 1, padx = 10, pady= 10)

    #FIRSTNAME ENTRY BOX
    player_firstname = Entry(addplayer)
    player_first = Label(addplayer, font=("Ariel",12), text="First name", background="crimson")
    player_first.grid(column = 1, row= 3,padx=10, pady= 10)
    player_firstname.grid(column = 2, row= 3, padx=10,pady=10)

    #LASTNAME ENTRY BOX
    player_lastname = Entry(addplayer)
    player_last = Label(addplayer, font=("Ariel",12), text="Surname", background="crimson")
    player_last.grid(column=1,row=4,padx=10,pady=10)
    player_lastname.grid(column=2,row=4,padx=10,pady=10)

    #AGE ENTRY BOX
    age = Entry(addplayer)
    age2 = Label(addplayer, font=("Ariel",12), text="Age",background="crimson")
    age2.grid(column = 1, row= 6,padx=10,pady=10)
    age.grid(column=2,row=6,padx=10,pady=10)

    #POSITION ENTRY BOX
    variable = StringVar(addplayer)
    variable.set("")
    position = OptionMenu(addplayer, variable, "GK", "LB", "RB", "CB", "CDM", "CM", "CAM", "LM", "RM", "RW", "LW", "ST") #creates a dropdown box
    pos = Label(addplayer, font=("Ariel",12), text="Position", background="crimson")
    pos.grid(column=1,row=7,padx=10,pady=10)
    position.grid(column=2,row=7,padx=10,pady=10)

    #GAMES PLAYED ENTRY BOX
    games_played = Entry(addplayer)
    games = Label(addplayer, font=("Ariel",12), text="Games Played", background="crimson")
    games.grid(column=1,row=8,padx=10,pady=10)
    games_played.grid(column=2,row=8,padx=10,pady=10)

    #GOALS SCORED ENTRY BOX
    goals_scored = Entry(addplayer)
    goals = Label(addplayer, font=("Ariel",12), text="Goals Scored", background="crimson")
    goals.grid(column=1,row=9,padx=10,pady=10)
    goals_scored.grid(column=2,row=9,padx=10,pady=10)

    #ASSISTS ENTRY BOX
    assist = Entry(addplayer)
    assissts = Label(addplayer, font=("Ariel",12), text="Assists", background="crimson")
    assissts.grid(column=1,row=10,padx=10,pady=10)
    assist.grid(column=2,row=10,padx=10,pady=10)

    #YELLOW CARDS ETRY BOX
    yellow_cards = Entry(addplayer)
    yellow = Label(addplayer, font=("Ariel",12), text="Yellow Cards", background="crimson")
    yellow.grid(column=1,row=11,padx=10,pady=10)
    yellow_cards.grid(column=2,row=11,padx=10,pady=10)

    #RED CARDS ENTRY BOX
    red_cards = Entry(addplayer)
    red = Label(addplayer, font=("Ariel",12), text="Red Cards", background="crimson")
    red.grid(column=1,row=12,padx=10,pady=10)
    red_cards.grid(column=2,row=12,padx=10,pady=10)

    #ADD PLAYER BUTTON
    addplayerb = Button(addplayer,text="Add Player", font=("Ariel",23),command=user_input)
    addplayerb.grid(column=2,row=13)

    #EXIT BUTTON
    exitb = Button(addplayer,text="Exit", font=("Ariel",23),command=addplayer.destroy)
    exitb.grid(column=5,row=1,padx=10,pady=10)

    #SQUAD NUMBER ENTRY
    squad_number = Entry(addplayer)
    squad = Label(addplayer, font=("Ariel",12), text="Squad Number", background="crimson")
    squad.grid(column=1,row=5,padx=10,pady=10)
    squad_number.grid(column=2,row=5,padx=10,pady=10)



    
###-----------------------------------------EDIT A PLAYER--------------------------------------------
def editplayerr():
    editplayer = Tk()
    editplayer.title("Edit player")
    editplayer.geometry("800x200")
    editplayer.configure(background="crimson")

    def changedata():
        squadnum=ent.get()
        changedata = Tk()
        changedata.title("Edit Player")
        changedata.geometry("500x600")
        changedata.configure(background="crimson")
        
        #TITLE LABEL
        title=Label(changedata,text="Edit The Data",font=("Cooper Black",20),background="crimson")
        title.grid(column=1,row=1,padx=10,pady=10)

        #FISRTNAME EDIT
        first = Label(changedata,text="Firstname",font=("Ariel",12),background="crimson")
        first.grid(column=1,row=2,padx=10,pady=10)
        firstname = Entry(changedata)
        firstname.grid(column=2,row=2,padx=10,pady=10)

        #LASTNAME EDIT
        last=Label(changedata,text="Surname",font=("Ariel",12),background="crimson")
        last.grid(column=1,row=3,padx=10,pady=10)
        lastname=Entry(changedata)
        lastname.grid(column=2,row=3,padx=10,pady=10)

        #SQUAD NUMBER EDIT
        squadnum = Label(changedata,text="Squad Number",font=("Ariel",12),background="crimson")
        squadnum.grid(column=1,row=4,padx=10,pady=10)
        squadnumber1=Entry(changedata)
        squadnumber1.grid(column=2,row=4,padx=10,pady=10)

        #AGE EDIT
        age = Label(changedata,text="Age",font=("Ariel",12),background="crimson")
        age.grid(column=1,row=5,padx=10,pady=10)
        age2=Entry(changedata)
        age2.grid(column=2,row=5,padx=10,pady=10)

        #POSITION EDIT
        variable = StringVar(changedata)
        variable.set("")
        position = OptionMenu(changedata, variable, "GK", "LB", "RB", "CB", "CDM", "CM", "CAM", "LM", "RM", "RW", "LW", "ST") #create sdropdown menu
        pos = Label(changedata, font=("Ariel",12), text="Position", background="crimson")
        pos.grid(column=1,row=6,padx=10,pady=10)
        position.grid(column=2,row=6,padx=10,pady=10)

        #GAMES PLAYED
        games = Label(changedata,text="Games Played",font=("Ariel",12),background="crimson")
        games.grid(column=1,row=7,padx=10,pady=10)
        gamesplayed=Entry(changedata)
        gamesplayed.grid(column=2,row=7,padx=10,pady=10)

        #GOALS EDIT
        goals = Label(changedata,text="Goals Scored",font=("Ariel",12),background="crimson")
        goals.grid(column=1,row=8,padx=10,pady=10)
        goals2 = Entry(changedata)
        goals2.grid(column=2,row=8,padx=10,pady=10)

        #ASSISTS EDIT
        assists = Label(changedata,text="Assists",font=("Ariel",12),background="crimson")
        assists.grid(column=1,row=9,padx=10,pady=10)
        assists2 =Entry(changedata)
        assists2.grid(column=2,row=9,padx=10,pady=10)

        #YELLOW CARDS
        yellow= Label(changedata,text="Yellow Cards",font=("Ariel",12),background="crimson")
        yellow.grid(column=1,row=10,padx=10,pady=10)
        yellowcards=Entry(changedata)
        yellowcards.grid(column=2,row=10,padx=10,pady=10)

        #RED CARDS
        red= Label(changedata,text="Red Cards",font=("Ariel",12),background="crimson")
        red.grid(column=1,row=11,padx=10,pady=10)
        redcards=Entry(changedata)
        redcards.grid(column=2,row=11,padx=10,pady=10)
        
        #INSERT DATA TO BE CHANGED
        squadnum=ent.get()
        player = c.execute('SELECT firstname, lastname, squadnumber, age FROM playerdetails WHERE playerdetails.squadnumber = ?', (squadnum,))
        for row in player:
            playerfirstname = row[0]
            playerlastname = row[1]
            playersquadnumber = row[2]
            playerage = row[3]
            firstname.insert(END, playerfirstname)
            lastname.insert(END, playerlastname)
            squadnumber1.insert(END, playersquadnumber)
            age2.insert(END, playerage)
        stats = c.execute('SELECT gamesplayed, goals, assists, yellowcards, redcards FROM gamestats WHERE gamestats.squadnumber = ?', (squadnum,))
        for row in stats:
            playergp = row[0]
            playergoals = row[1]
            playerassists = row[2]
            playeryellowcards = row[3]
            playerredcards = row[4]
            gamesplayed.insert(END, playergp)
            goals2.insert(END, playergoals)
            assists2.insert(END, playerassists)
            yellowcards.insert(END, playeryellowcards)
            redcards.insert(END, playerredcards) #gets the data from the database and inserts it into the entry boxes matching the data (eg. firstname will go into the firstname entry box to be changed if needed)
            

            def addeditteddata():
                c.execute('''DELETE FROM playerdetails WHERE playerdetails.squadnumber = ? ''', (squadnum,))
                c.execute('''DELETE FROM gamestats WHERE gamestats.squadnumber = ? ''',(squadnum,)) #deletes old data from the database
                conn.commit()
                first_name = firstname.get()
                last_name = lastname.get()
                age_ = age2.get()
                position_ = variable.get()
                gamesplayed_ = gamesplayed.get()
                goals_ = goals2.get()
                assists_ = assists2.get()
                yellowcards_ = yellowcards.get()
                redcards_ = redcards.get()
                squadnumber = squadnumber1.get() #ggets variables from entry boxes
                c.execute('''SELECT * FROM playerdetails WHERE squadnumber = ?''', (squadnumber,))
                check_exists = c.fetchone()
                if len(first_name)>15:
                    messagebox.showinfo("ERROR","Please enter make sure the firstname of the player is less than 16 characters and only contains text.") #checks that the firstname is less than 16 characters long
                elif len(last_name)>15:
                    messagebox.showinfo("ERROR","Please make sure the surname of the player is less than 16 characters and only contains text.") #checks only text has been entered
                elif len(age_) > 2 :
                    messagebox.showinfo("ERROR","Please make sure the age of the player is a umber and is smaller than 100.") #checks age is less than 100
                elif check_exists is not None:
                    messagebox.showinfo("ERROR","A player with that squad number already exists.") #checks that a player with (new) squad number does not already exit
                elif first_name.isalpha() and last_name.isalpha() and age_.isdigit() and gamesplayed_.isdigit() and goals_.isdigit() and assists_.isdigit() and yellowcards_.isdigit() and redcards_.isdigit() and squadnumber.isdigit(): 
                    c.execute("INSERT INTO playerdetails(firstname, lastname, squadnumber, age, position) VALUES (?, ?, ?, ?, ?)",
                                (first_name, last_name, squadnumber, age_, position_))
                    c.execute("INSERT INTO gamestats(squadnumber, gamesplayed, goals, assists, yellowcards, redcards) VALUES (?, ?, ?, ?, ?, ?)",
                              (squadnumber, gamesplayed_, goals_, assists_, yellowcards_, redcards_))  #inserts new data into the database to replace the old outdated data 
                    firstname.delete(0,END)
                    lastname.delete(0,END)
                    age2.delete(0,END)
                    position = ""
                    gamesplayed.delete(0,END)
                    goals2.delete(0,END)
                    assists2.delete(0,END)
                    yellowcards.delete(0,END)
                    redcards.delete(0,END)
                    squadnumber1.delete(0,END)
                    conn.commit()
                    changedata.destroy() #clears entry boxes
                else:
                    messagebox.showinfo("ERROR","Please make sure the correct details have been entered in the correct format.") #displays error message
                    
                
                

        #ENTER BUTTON
            enter=Button(changedata,text="Enter",font=("Ariel",20),command = addeditteddata)
            enter.grid(column=2,row=12,padx=10,pady=10)
            
            
        
        
        

    def checkdata():
        squadnum = ent.get()
        c.execute('SELECT * FROM playerdetails WHERE squadnumber=?', (squadnum,))
        row = c.fetchone()
        if row is None:
            errorlbl.configure(text="No player with that squad number exists") #dispalys error label is no match
        else:
            changedata()
            editplayer.destroy()
              
        


    #ENTRY LABEL
    playernum = Label(editplayer, font=("Ariel",11),text="Please enter the squad number of the player you wish to edit:",background="crimson")
    playernum.grid(column=1,row=2,padx=10,pady=10)
    ent = Entry(editplayer)
    ent.grid(column=2,row=2,padx=10,pady=10)

    #EXIT BUTTON
    exitb = Button(editplayer,text="Exit", font=("Ariel",23),command=editplayer.destroy)
    exitb.grid(column=5,row=1,padx=10,pady=10)

    #ENTER BUTTON
    enter = Button(editplayer,text="Enter",font=("Ariel",20),command=checkdata)
    enter.grid(column=5,row=3,padx=10,pady=10)

    #ERROR LABEL
    errorlbl = Label(editplayer,text="",font=("Ariel",12),background="crimson")
    errorlbl.grid(column=1,row=3,padx=10,pady=10)

    

###DELETE ALL FROM DATABASE--------------------------------------------------------------------------------------------------------------------
def deletealll():
    #CREATES WINDOW
    deleteall = Tk()
    deleteall.title("Are You Sure?")
    deleteall.geometry("700x150")
    deleteall.configure(background="crimson")

    def delalldata():
        c.execute('DELETE FROM playerdetails')
        c.execute('DELETE FROM gamestats')
        deleteall.destroy() #deletes all from database
        
        

    #explain label
    explain=Label(deleteall,text="Are you sure you want to delete everything in the database?",font=("Cooper black",12),background="crimson")
    explain.grid(column=2,row=1,padx=10,pady=10)

    #YES BUTTON
    yes=Button(deleteall,text="Yes",font=("Cooper Black",10),command=delalldata)
    yes.grid(column=1,row=3,padx=10,pady=10)

    #NO BUTTON
    no=Button(deleteall,text="No",font=("Cooper Black",10),command=deleteall.destroy)
    no.grid(column=3,row=3,padx=10,pady=10)
    
    
       
