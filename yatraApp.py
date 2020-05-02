from tkinter import*
import requests
class Yatra:
    def __init__(self):
        self.root=Tk()

        self.root.title("Train Route")
        self.root.minsize(400,600)
        self.root.maxsize(1000,1200)
        self.root.configure(background="#1abc9c")

        label=Label(self.root,text="Train route",bg="#1abc9c",fg="#ffffff")
        label.configure(font=("constantia",22,"bold"))
        label.pack(pady=(30,10))

        self.train_no=Entry(self.root)
        self.train_no.pack(ipadx=40,ipady=10)

        click=Button(self.root,text="fetch",bg="#ffffff",width=28,height=2,command=lambda:self.fetch())
        click.pack(pady=(10,20))

        self.result=Label(self.root,bg="#c0392b",fg="#ffffff")
        self.result.configure(font=("constantia",14,))
        self.result.pack(pady=(1,1))



        self.root.mainloop()


    def fetch(self):
        train_no=self.train_no.get()
        url="https://api.railwayapi.com/v2/route/train/{}/apikey/kjcqzsbvjx".format(train_no)
        response=requests.get(url)
        data=response.json()
        print(data)
        stations=""
        for i in data["route"]:
            stations=stations+"\n"+i['station']['name']
        self.result.configure(text=stations)
        




obj=Yatra()
