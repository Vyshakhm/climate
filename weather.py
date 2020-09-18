#little weather finding application with in my knowledge. 
#importing modules
from tkinter import *
from PIL import ImageTk, Image
import os
#For reqesting server permission
import requests
import json
#clearing screen
os.system("clear")
#parent window
root=Tk()
root.title("wheather update") 
root.iconbitmap("sun.png")
root.geometry("500x350")
root.resizable(False,False)

canvas=Canvas(root,height=400,width=600)
background_image= ImageTk.PhotoImage(Image.open("photo1.jpg"))
background_label=Label(canvas,image=background_image)
background_label.place(width=500,height=400)
canvas.pack()
#frames for seperating
frame1=Frame(root,bg="#f7faf9",bd=5)
frame1.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor="n")

frame1=Frame(root,bg="#f7faf9",bd=5)
frame1.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor="n")
#for searching
text_box=Entry(frame1,font="helvetica")
text_box.place(relwidth=0.65,relheight=1)

btn=Button(frame1,text="Get Weather",width=20,height=5,relief="groove",font="helvetica",command=lambda:get_weather(text_box.get()))
btn.place(relx=0.7,relwidth=0.3,relheight=1)

#function for get weather data
def get_weather(text):
	#weather_key="f6819b150ebd49128a862fb02c59f79e"
	#url="http://api.openweathermap.org/data/2.5/forecast?q=city&appid=f6819b150ebd49128a862fb02c59f79e"
	
	#establishing connection with server
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

	#deleting the existing when click button
	city.delete(0,END)
	str(temp).delete(0,END)
	sky.delete(0,END)
	str(wind).delete(0,END)
	str(humi).delete(0,END)
#closing loop
root.mainloop()



#########################code bloopers############################
##################################################################
#params={"q":city}
#response=requests.get("http://api.openweathermap.org/data/2.5/forecast?q=city&appid=f6819b150ebd49128a862fb02c59f79e")
#print(response.json())
#api=json.loads(response.content)
#print(api)
#back_g  = PhotoImage(file="fogg.png")
#bg_label=Label(root,iamge=back_g)
#bg_label.pack()