import curses

screen = curses.initscr()

f = 'Fight'
b = 'Bag'
s = "Stats"
r = "Run"
pic = ("""\

                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /


                    """)

screen.addstr(17,30,f)
screen.addstr(17,150,b)
screen.addstr(19,30,s)
screen.addstr(19,150,r)
screen.addstr(4,150,pic)
screen.border(0)
box1 = screen.subwin(8, 178, 15, 20)
box1.box()
screen.getch()
curses.endwin()