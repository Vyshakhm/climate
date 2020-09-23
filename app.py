from tkinter import *
from PIL import ImageTk, Image
import os
import requests
import json

os.system("cls")

class Application(Frame):
	def __init__(self,master=None):
		super().__init__(master)
		self.master=master
		self.show_weather()



	def show_weather(self):
		self.winfo_toplevel().title("weather")

		self.background_image= ImageTk.PhotoImage(Image.open("photo1.jpg"))
		self.background_label=Label(self.master,image=self.background_image)
		self.background_label.place(width=500,height=400)

		self.frame1=Frame(self.master,bg="#f7faf9",bd=5)
		self.frame1.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor="n")

		self.text_box=Entry(self.frame1,font="helvetica")
		self.text_box.place(relwidth=0.65,relheight=1)

		self.btn=Button(self.frame1,text="Get Weather",width=20,height=5,relief="groove",font="helvetica",command=lambda:get_weather(self.text_box.get()))
		self.btn.place(relx=0.7,relwidth=0.3,relheight=1)


		def get_weather(text):

			get_api=requests.get('http://api.weatherapi.com/v1/current.json?key=af3d2d6e844f4b11b94102443202804&q='+text)
			api=json.loads(get_api.content)
			#retrieving the data
			city=api['location']['name']
			temp=api['current']['temp_c']
			sky=api['current']['condition']['text']
			wind=api['current']['wind_kph']
			humi=api['current']['humidity']

			frame2=Frame(root,bg="#f7faf9",bd=5)
			frame2.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor="n")

			label1=Label(frame2,text=city+"\n "+ "tempreture"+" "+str(temp)+"^C"+"\n "+"weather is"+ " "+sky +"\n "+"wind"+" "+str(wind)+"\n "+"humiditi"+ " "+str(humi),font="helvetica",fg="black")
			label1.place(relwidth=1,relheight=1)

			city.delete(0,END)
			str(temp).delete(0,END)
			sky.delete(0,END)
			str(wind).delete(0,END)
			str(humi).delete(0,END)

root=Tk()
root.iconbitmap("sun.png")
root.geometry("500x350")
root.resizable(False,False)
app=Application(master=root)
app.mainloop()