from tkinter import *
import random




class MineOptions:
    def __init__(self):
        global clicked_mines
        clicked_mines = []



    def BOOM(mine):
        if (mine == "1"):
            mine1.config(bg='#FF0000')

        elif (mine == "2"):
            mine2.config(bg='#FF0000')

        elif (mine == "3"):
            mine3.config(bg='#FF0000')

        elif (mine == "4"):
            mine4.config(bg='#FF0000')

        elif (mine == "5"):
            mine5.config(bg='#FF0000')

        elif (mine == "6"):
            mine6.config(bg='#FF0000')

        elif (mine == "7"):
            mine7.config(bg='#FF0000')

        elif (mine == "8"):
            mine8.config(bg='#FF0000')

        elif (mine == "9"):
            mine9.config(bg='#FF0000')

        elif (mine == "10"):
            mine10.config(bg='#FF0000')

        elif (mine == "11"):
            mine11.config(bg='#FF0000')

        elif (mine == "12"):
            mine12.config(bg='#FF0000')

        elif (mine == "13"):
            mine13.config(bg='#FF0000')

        elif (mine == "14"):
            mine14.config(bg='#FF0000')

        elif (mine == "15"):
            mine15.config(bg='#FF0000')

        elif (mine == "16"):
            mine16.config(bg='#FF0000')

        elif (mine == "17"):
            mine17.config(bg='#FF0000')

        elif (mine == "18"):
            mine18.config(bg='#FF0000')

        elif (mine == "19"):
            mine19.config(bg='#FF0000')

        elif (mine == "20"):
            mine20.config(bg='#FF0000')

        elif (mine == "21"):
            mine21.config(bg='#FF0000')

        elif(mine == "22"):
            mine22.config(bg='#FF0000')

        elif (mine == "23"):
            mine23.config(bg='#FF0000')

        elif (mine == "24"):
            mine24.config(bg='#FF0000')

        elif (mine == "25"):
            mine25.config(bg='#FF0000')

        elif (mine == "26"):
            mine26.config(bg='#FF0000')

        elif (mine == "27"):
            mine27.config(bg='#FF0000')

        elif (mine == "28"):
            mine28.config(bg='#FF0000')

        elif (mine == "29"):
            mine29.config(bg='#FF0000')

        elif (mine == "30"):
            mine30.config(bg='#FF0000')

        elif (mine == "31"):
            mine31.config(bg='#FF0000')

        elif (mine == "32"):
            mine32.config(bg='#FF0000')

        elif (mine == "33"):
            mine33.config(bg='#FF0000')

        elif (mine == "34"):
            mine34.config(bg='#FF0000')

        elif (mine == "35"):
            mine35.config(bg='#FF0000')

        elif (mine == "36"):
            mine36.config(bg='#FF0000')

        Failed['text'] = '!!BOOM!!'



    def destroyMine(mine):
        if(mine == "1"):
            mine1.destroy()

        elif(mine == "2"):
            mine2.destroy()

        elif(mine == "3"):
            mine3.destroy()

        elif(mine == "4"):
            mine4.destroy()

        elif(mine == "5"):
            mine5.destroy()

        elif(mine == "6"):
            mine6.destroy()

        elif(mine == "7"):
            mine7.destroy()

        elif(mine == "8"):
            mine8.destroy()

        elif(mine == "9"):
            mine9.destroy()

        elif(mine == "10"):
            mine10.destroy()

        elif(mine == "11"):
            mine11.destroy()

        elif(mine == "12"):
            mine12.destroy()

        elif(mine == "13"):
            mine13.destroy()

        elif(mine == "14"):
            mine14.destroy()

        elif(mine == "15"):
            mine15.destroy()

        elif(mine == "16"):
            mine16.destroy()

        elif(mine == "17"):
            mine17.destroy()

        elif(mine == "18"):
            mine18.destroy()

        elif(mine == "19"):
            mine19.destroy()

        elif(mine == "20"):
            mine20.destroy()

        elif(mine == "21"):
            mine21.destroy()

        elif(mine == "22"):
            mine22.destroy()

        elif(mine == "23"):
            mine23.destroy()

        elif(mine == "24"):
            mine24.destroy()

        elif(mine == "25"):
            mine25.destroy()

        elif(mine == "26"):
            mine26.destroy()

        elif(mine == "27"):
            mine27.destroy()

        elif(mine == "28"):
            mine28.destroy()

        elif(mine == "29"):
            mine29.destroy()

        elif(mine == "30"):
            mine30.destroy()

        elif(mine == "31"):
            mine31.destroy()

        elif(mine == "32"):
            mine32.destroy()

        elif(mine == "33"):
            mine33.destroy()

        elif(mine == "34"):
            mine34.destroy()

        elif(mine == "35"):
            mine35.destroy()

        elif(mine == "36"):
            mine36.destroy()






    def checkMine():
        for mine in clicked_mines:
            if(mine in boxMine):
                MineOptions.BOOM(mine)

            else:
                MineOptions.destroyMine(mine)

    def clickedMines(clicked):
        clicked_mines.append(clicked)

        MineOptions.checkMine()


    def setMine():
        word = "a"*mineCount
        for i in word:
            choosenBox = random.choice(mineList)
            #print("!!!", choosenBox)

            if(choosenBox not in boxMine):
                boxMine.add(choosenBox)

            else:
                pass
                #MineOptions.setMine()





class inWindow:
    def __init__(self):
        MineOptions()

        global totalBoxCount, mineList, boxMine
        totalBoxCount = 35

        mineList = ["1","2","3","4","5","6","7","8","9","10",
                 "11","12","13","14","15","16","17","18","19","20",
                 "21","21","23","24","25","26","27","28","29","30",
                 "31","32","33","34","35"]

        boxMine = set()


        #setMineCount
        inWindow.setMineCount()

        #setMine
        MineOptions.setMine()

        #Main
        inWindow.Main()


        #Mines3
        inWindow.MinesLoc()

        print(boxMine)
        print(len(boxMine))





    def MinesLoc():
        global mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10
        global mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20
        global mine21, mine22, mine23, mine24, mine25, mine26, mine27, mine28, mine29, mine30
        global mine31, mine32, mine33, mine34, mine35, mine36

        #SATIR 1
        mine1 = Button(p,
                       text=" "*8,
                       bd=7, command=lambda : MineOptions.clickedMines("1"))
        mine1.place(x = 100, y=  175)

        mine2 = Button(p,
                       text=" "*8,
                       bd=7, command=lambda : MineOptions.clickedMines("2"))
        mine2.place(x = 150, y=  175)

        mine3 = Button(p,
                       text=" "*8,
                       bd=7, command=lambda : MineOptions.clickedMines("3"))
        mine3.place(x = 200, y=  175)

        mine4 = Button(p,
                       text=" "*8,
                       bd=7, command=lambda : MineOptions.clickedMines("4"))
        mine4.place(x = 250, y=  175)

        mine5 = Button(p,
                       text=" "*8,
                       bd=7, command=lambda : MineOptions.clickedMines("5"))
        mine5.place(x = 300, y=  175)

        mine6 = Button(p,
                       text=" "*8,
                       bd=7, command=lambda : MineOptions.clickedMines("6"))
        mine6.place(x = 350, y=  175)

        mine7 = Button(p,
                       text=" "*8,
                       bd=7, command=lambda : MineOptions.clickedMines("7"))
        mine7.place(x = 400, y=  175)

        #SATIR 2

        mine8 = Button(p,
                       text=" "*8,
                       bd=7, command=lambda : MineOptions.clickedMines("8"))
        mine8.place(x = 100, y=  215)

        mine9 = Button(p,
                       text=" "*8,
                       bd=7, command=lambda : MineOptions.clickedMines("9"))
        mine9.place(x = 150, y=  215)

        mine10 = Button(p,
                       text=" "*8,
                       bd=7, command=lambda : MineOptions.clickedMines("10"))
        mine10.place(x = 200, y=  215)

        mine11 = Button(p,
                       text=" "*8,
                       bd=7, command=lambda : MineOptions.clickedMines("11"))
        mine11.place(x = 250, y=  215)

        mine12 = Button(p,
                       text=" "*8,
                       bd=7, command=lambda : MineOptions.clickedMines("12"))
        mine12.place(x = 300, y=  215)

        mine13 = Button(p,
                       text=" "*8,
                       bd=7, command=lambda : MineOptions.clickedMines("13"))
        mine13.place(x = 350, y=  215)

        mine14 = Button(p,
                       text=" "*8,
                       bd=7, command=lambda : MineOptions.clickedMines("14"))
        mine14.place(x = 400, y=  215)

        # SATIR 3

        mine15 = Button(p,
                       text=" " * 8,
                       bd=7, command=lambda : MineOptions.clickedMines("15"))
        mine15.place(x=100, y=255)

        mine16 = Button(p,
                       text=" " * 8,
                       bd=7, command=lambda : MineOptions.clickedMines("16"))
        mine16.place(x=150, y=255)

        mine17 = Button(p,
                        text=" " * 8,
                        bd=7, command=lambda : MineOptions.clickedMines("17"))
        mine17.place(x=200, y=255)

        mine18 = Button(p,
                        text=" " * 8,
                        bd=7, command=lambda : MineOptions.clickedMines("18"))
        mine18.place(x=250, y=255)

        mine19 = Button(p,
                        text=" " * 8,
                        bd=7, command=lambda : MineOptions.clickedMines("19"))
        mine19.place(x=300, y=255)

        mine20 = Button(p,
                        text=" " * 8,
                        bd=7, command=lambda : MineOptions.clickedMines("20"))
        mine20.place(x=350, y=255)

        mine21 = Button(p,
                        text=" " * 8,
                        bd=7, command=lambda : MineOptions.clickedMines("21"))
        mine21.place(x=400, y=255)

        # SATIR 4

        mine22 = Button(p,
                       text=" " * 8,
                       bd=7, command=lambda : MineOptions.clickedMines("22"))
        mine22.place(x=100, y=295)

        mine23 = Button(p,
                       text=" " * 8,
                       bd=7, command=lambda : MineOptions.clickedMines("23"))
        mine23.place(x=150, y=295)

        mine24 = Button(p,
                        text=" " * 8,
                        bd=7, command=lambda : MineOptions.clickedMines("24"))
        mine24.place(x=200, y=295)

        mine25 = Button(p,
                        text=" " * 8,
                        bd=7, command=lambda : MineOptions.clickedMines("25"))
        mine25.place(x=250, y=295)

        mine26 = Button(p,
                        text=" " * 8,
                        bd=7, command=lambda : MineOptions.clickedMines("26"))
        mine26.place(x=300, y=295)

        mine27 = Button(p,
                        text=" " * 8,
                        bd=7, command=lambda : MineOptions.clickedMines("27"))
        mine27.place(x=350, y=295)

        mine28 = Button(p,
                        text=" " * 8,
                        bd=7, command=lambda : MineOptions.clickedMines("28"))
        mine28.place(x=400, y=295)

        # SATIR 5

        mine29 = Button(p,
                       text=" " * 8,
                       bd=7, command=lambda : MineOptions.clickedMines("29"))
        mine29.place(x=100, y=335)

        mine30 = Button(p,
                       text=" " * 8,
                       bd=7, command=lambda : MineOptions.clickedMines("30"))
        mine30.place(x=150, y=335)

        mine31 = Button(p,
                        text=" " * 8,
                        bd=7, command=lambda : MineOptions.clickedMines("31"))
        mine31.place(x=200, y=335)

        mine32 = Button(p,
                        text=" " * 8,
                        bd=7, command=lambda : MineOptions.clickedMines("32"))
        mine32.place(x=250, y=335)

        mine33 = Button(p,
                        text=" " * 8,
                        bd=7, command=lambda : MineOptions.clickedMines("33"))
        mine33.place(x=300, y=335)

        mine34 = Button(p,
                        text=" " * 8,
                        bd=7, command=lambda : MineOptions.clickedMines("34"))
        mine34.place(x=350, y=335)

        mine35 = Button(p,
                        text=" " * 8,
                        bd=7, command=lambda : MineOptions.clickedMines("35"))
        mine35.place(x=400, y=335)





    def setMineCount():
        global mineCount
        #mineCount = random.randrange(0, totalBoxCount-15)
        mineCount = 10

        if(mineCount < 5):
            inWindow.setMineCount()




    def Main():
        global Failed

        leftMines = Label(p,
                          text="Left Mines: "+str(mineCount),
                          font=("arial", 14, "bold"))
        leftMines.place(x = 240, y = 21)


        Failed = Label(p,
                       text="",
                       font=("arial",17,"bold"), fg='#FF0000')
        Failed.place(x = 90, y = 400)





class Window:
    def __init__(self):
        self.geometry = "550x500+550+250"
        self.title = "MAYIN TARLASI"

        self.setWindow(self.geometry, self.title)

    def setWindow(self, g, t):
        global p

        p = Tk()
        p.geometry(g)
        p.title(t)


        inWindow()




        p.mainloop()









if(__name__ == '__main__'):
    Window()