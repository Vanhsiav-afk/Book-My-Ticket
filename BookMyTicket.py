from guizero import App,Combo,Text,CheckBox,ButtonGroup,PushButton,info
def do_booking():
    info("Booking","Thank You For Booking")
    print(film_choice.value)
    if vip_seat.value==1:
        print("Vip Seat")
    else:
        print("Normal Seat")
    print(row_choice.value)
app=App(title="A new App",width=300,height=200,layout='grid')
film_choice=Combo(app,options=["Star Wars","Frozen","Lion King"],grid=[1,0],align="left")
film_description=Text(app,text="Which Movie?",grid=[0,0],align="left")
vip_seat=CheckBox(app,text="VIP Seat?",grid=[1,1],align="left")
type=Text(app,text="Seat Type?",grid=[0,1],align="left")
row_choice=ButtonGroup(app,options=[["Front","F"],["Middle","M"],["Back","B"]],selected="M",horizontal=True,grid=[1,2],align="left")
location=Text(app,text="Seat Location",grid=[0,2],align='left')
book=PushButton(app, command=do_booking, text="Book Seat",grid=[1,3],align='left')
app.display()
