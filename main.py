from tkinter import *
from tkinter import messagebox 
from tkinter import ttk 
import pandas as pd
import os
import csv
import time
import datetime
import shutil
import cv2
from PIL import ImageTk
import PIL.Image
import numpy as np


def startapp(container):
    
    lb1 = Label(container, text = "Automatic Door Unlock System", font=('Courier', 18, "bold"), bg='black',
                          fg='white')
    lb1.place(relwidth=1, relheight = 0.1)
    
    
    def login_(frame):
        for widget in frame.winfo_children():
            widget.destroy()
            
        login_page(frame)
    

    img = PIL.Image.open('static/main.jpg') 
    img = img.resize((400,280))
    
    img = ImageTk.PhotoImage(img) 
       
    panel = Label(container, image = img) 
    panel.image = img 
    panel.place(relwidth=1, y = 40)
    
    ttk.Style().configure("TButton", padding=8, relief="flat",font=('Courier', 10, "bold"),
            background="#2c91e0",foreground='green')
    
    bnt1 = ttk.Button(container, text = 'Admin', command = lambda : login_(container))
    bnt1.place(x = 40, y = 110)
    bnt2 = ttk.Button(container, text = 'Doorbell', command = lambda : doorbell())
    bnt2.place(x = 40, y = 210)


def login_page(container):
    
    lb1 = Label(container, text = "Login Page", font=('Helvetica', 15, "bold"), bg='black',
                          fg='white')
    lb1.place(relwidth=1, relheight = 0.1)

    
    
    def admin_login(frame, entry1, entry2):
        df = pd.read_csv('User.csv')
        name = df['Name'].values
        password = df['Password'].values
        
        if (entry1 == '' or entry2 == ''):
            messagebox.showerror('Error', "Invalid Username or Password")
        elif (np.any(entry1 == 'newuser' or entry1 == name)  and  np.any(entry2 == "newuser" or entry2 == password)):
            for widget in frame.winfo_children():
                widget.destroy()
            admin(frame)
        else:
            messagebox.showerror('Error', "Invalid Username or Password")
        
    
    def back_to_main(frame):
        for widget in frame.winfo_children():
            widget.destroy()
            
        startapp(frame)
        
    img = PIL.Image.open('static/login.png') 
    img = img.resize((150,150))
    
    img = ImageTk.PhotoImage(img) 
       
    panel = Label(container, image = img) 
    panel.image = img 
    panel.place(x= 350, y = 70)  
    
    lb2 = Label(container, text = "Username : ", font=('Helvetica', 12, "bold"), foreground="#263942")
    lb2.place(x = 40, y = 110)
    
    lb3 = Label(container, text = "Password : ",font=('Helvetica', 12, "bold"), foreground="#263942")
    lb3.place(x = 40, y = 150)
    
    entry1 = Entry(container, font = ("Helvetica", 12))
    entry1.place(x = 140, y = 110)
    
    entry2 = Entry(container, show = '*', font = ("Helvetica", 12))
    entry2.place(x = 140, y = 150)
        
    ttk.Style().configure("TButton", padding=6, relief="flat",
            background="#ccc",foreground='green')
    bnt1 = ttk.Button(container, text = 'Login', command = lambda : admin_login(container, entry1.get(), entry2.get()))
    bnt1.place(x = 70, y = 220)
    bnt3 = ttk.Button(container, text = 'Back', command = lambda : back_to_main(container))
    bnt3.place(x = 200, y = 220)
    
    
def admin(container):
    lb1 = Label(container, text = "Admin Page", font=('Courier', 18, "bold"), bg='black',
                          fg='white')
    lb1.place(relwidth=1, relheight = 0.1)
    
    
    
    def user_list_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()
            
        user_list(frame)
        
    def creat_new_user_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()
            
        newuser(frame)
    
    
    def back_to_main(frame):
        for widget in frame.winfo_children():
            widget.destroy()
            
        startapp(frame)
        
    img = PIL.Image.open('static/user.png') 
    img = img.resize((200,200))
    
    img = ImageTk.PhotoImage(img) 
       
    panel = Label(container, image = img) 
    panel.image = img 
    panel.place(x= 220, y = 70)    
    
    ttk.Style().configure("TButton", padding=6, relief="flat",font=('Courier', 10, "bold"),
            background="#2c91e0",foreground='green')
    
    bnt1 = ttk.Button(container, text = 'Existing Users', command = lambda : user_list_frame(container))
    bnt1.place(x = 50, y = 90)
    bnt2 = ttk.Button(container, text = 'Creat New User', command = lambda : creat_new_user_frame(container))
    bnt2.place(x = 50, y = 170)
    bnt3 = ttk.Button(container, text = 'Back', command = lambda : back_to_main(container))
    bnt3.place(x = 50, y = 250)
    
    
def newuser(container):
    
    new_user = StringVar()
    new_user_password = StringVar()
    num_images = IntVar()
    
    
    lb1 = Label(container, text = "New User Registeration",font=('Helvetica', 15, "bold"), bg='black',
                          fg='white')
    lb1.place(relwidth=1, relheight = 0.1)
    
    lb2 = Label(container, text = "Name : ", font = ("Helvetica", 12), foreground="#263942")
    lb2.place(x = 50, y = 100)
    
    entry = Entry(container, textvariable = new_user, font = ("Helvetica", 10), foreground="#263942")
    entry.place(x = 170, y = 100)
    
    lb3 = Label(container, text = "Password : ", font = ("Helvetica", 12), foreground="#263942")
    lb3.place(x = 50, y = 150)
    
    entry1 = Entry(container, textvariable = new_user_password, font = ("Helvetica", 10), foreground="#263942")
    entry1.place(x = 170, y = 150)
    
    
    def creat_dataset(container, new_user,  btn1, btn2, btn3, num_images):
        
        data = pd.read_csv('User.csv')
        if (new_user in list(data['Name'])):
            messagebox.showerror('Error', 'User already exist')
            return
        creatdataset(container, new_user,  btn1, btn2, btn3, num_images)
        return
        
    def train_model(new_user, new_user_password,btn1, btn2, btn3):
        entry.delete(0,'end')
        entry1.delete(0,'end')
        
        train_model_of_user(new_user, new_user_password, btn1, btn2, btn3)
    
    
    def back_to_main(frame):
        for widget in frame.winfo_children():
            widget.destroy()
            
        admin(frame)
        
    
    ttk.Style().configure("TButton", padding=6, relief="flat",
            background="#ccc",foreground='green')
    btn1 = ttk.Button(container, text = 'Train Dataset', command = lambda : train_model(new_user.get(), new_user_password.get(), btn1, btn2, btn3))
    btn1.place(x = 50, y = 220)
    btn2 = ttk.Button(container, text = 'Creat Dataset', command = lambda : creat_dataset(container, new_user.get(),  btn1, btn2, btn3, num_images))
    btn2.place(x = 180, y = 220)
    btn3 = ttk.Button(container, text = 'Back', command = lambda : back_to_main(container))
    btn3.place(x = 310, y = 220)

def creatdataset(container, name_user, btn1, btn2, btn3, num_images):

    path = "dataset\{}".format(name_user) 
    
    num_of_images = 0
    detector = cv2.CascadeClassifier("static/haarcascade_frontalface_default.xml")
    try:
        os.makedirs(path)
    except:
        print('Directory Already Created')       
        
    video = cv2.VideoCapture(0)
    
    
    while True:
        ret, frame = video.read()
        grayimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        new_img = None
        faces = detector.detectMultiScale(image=grayimg, scaleFactor=1.05, minNeighbors=5)
        key = 0 
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
            new_img = frame[y:y+h, x:x+w]
            cv2.putText(frame, "Face Detected", (x, y-5), cv2.FONT_HERSHEY_PLAIN, 0.8, (0, 0, 255))
            cv2.putText(frame, str(str(num_of_images)+" images captured"), (x, y+h+20), cv2.FONT_HERSHEY_PLAIN, 0.8, (0, 0, 255))
            cv2.imshow("FaceDetection", frame)
            key = cv2.waitKey(1) & 0xFF == ord('q')
        try:
            cv2.imwrite(str(path+"/"+str(num_of_images)+name_user+".jpg"),new_img)
            num_of_images += 1
        except :
            pass
        
        if num_of_images > 300:
            break
    cv2.destroyAllWindows()
  
   
    num_images.set(num_of_images)
    
    text = f"Images captuared : {num_images.get()}"
    label1 = Label(container, text = text, font = "Helvetica", foreground="red")
    label1.config(font=("Helvetica", 12))
    label1.place(x = 150,y = 280)
    return

                        

def train_model_of_user(new_user, new_user_password,btn1, btn2, btn3):
    path = os.path.join(os.getcwd()+"/dataset/"+new_user+"/")
    
    faces = [] 
    ids = []
    
    for root, dirs, files in os.walk(path):
        pictures = files
        
    for pic in pictures:
        imgpath = path+pic 
        img = PIL.Image.open(imgpath).convert('L')
        face = np.array(img, 'uint8')
        id = int(pic.split(new_user)[0])
        faces.append(face)
        ids.append(id)
    
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(ids))
    recognizer.write("classifier/"+new_user+"_classifier.xml")
    btn2['state'] = 'disabled'
    btn3['state'] = "normal"
    btn1['state'] = "normal"
    
    data = pd.read_csv('User.csv')
    data.loc[len(data)] = [new_user, new_user_password]
    data.set_index('Name',inplace=True)
    data.to_csv('User.csv')
    
    messagebox.showinfo("Notififcation","Succesfully Trained the model")
    
    
    
def delete_selected(frame,listbox):
    a = listbox.get(listbox.curselection()).split(' ')
    path = os.getcwd()
    print("Path : ",path)
    path1 = path + f"\dataset\{a[1]}"
    path2 = path + f"\classifier\{a[1]}_classifier.xml"
    print(path,path1,path2)
    shutil.rmtree(path1)
    os.remove(path2)
    
    
    data = pd.read_csv('User.csv')
    new_data = data[data.Name != a[1]]
    new_data.set_index('Name',inplace = True)
    new_data.to_csv('User.csv')
    
    
        
    for widget in frame.winfo_children():
        widget.destroy()
        
    user_list(frame)


def user_list(container):
    
    lb1 = Label(container, text = "List of User", font=('Helvetica', 15, "bold"), bg='black',
                          fg='white')
    lb1.place(relwidth=1, relheight = 0.1)
    
    
 
    listbox = Listbox(container, height = 10, width = 15, yscrollcommand = True, font = "Helvetica", bg = "#ccc") 
    try:
        data = pd.read_csv('User.csv')
        z = list(data.Name)
        for i in range(len(z)):
            listbox.insert(i+1 ,f"{i+1}. {z[i]}")
        listbox.place(x = 70, y = 70) 
    except:
        messagebox.showinfo('Info','Please Train the user')
    
    def back_to_main(frame):
        for widget in frame.winfo_children():
            widget.destroy()
            
        admin(frame)
        
    
    ttk.Style().configure("TButton", padding=6, relief="flat",
            background="#ccc",foreground='green')
    bnt1 = ttk.Button(container, text = 'Delete Name', command = lambda :  delete_selected(container,listbox))
    bnt1.place(x = 300, y = 90)
    bnt2 = ttk.Button(container, text = 'Back', command = lambda : back_to_main(container))
    bnt2.place(x = 300, y = 170)
    

    

def doorbell():
    data = pd.read_csv('User.csv')
    names = list(data.Name)
    facedet = cv2.CascadeClassifier("static/haarcascade_frontalface_default.xml")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    video = cv2.VideoCapture(0)
    
    for i in names:
        name = i
        recognizer.read(f"classifier\{name}_classifier.xml")
        pred = 0
        while True:
            ret, frame = video.read()
            grayimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = facedet.detectMultiScale(grayimg,1.3,5)
            
            for x, y, w, h in faces:
                roi_gray = grayimg[y:y+h,x:x+w]
                id,confidence = recognizer.predict(roi_gray)
                confidence = 100 - int(confidence)
                
                if confidence > 50:
                    pred += +1
                    text = name.upper()
                    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    frame = cv2.putText(frame, text, (x, y-4), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1, cv2.LINE_AA)
                    print("Matched Face")
                    
                    if(pred == 5):
                        time_now = datetime.datetime.now()
                        #path = os.getcwd() + f"\\results\\{name}{time_now}.jpg"
                        s = "results\\"+ str(name) + str(time_now.date()) + "-" + str(time_now.hour) + "-" +str(time_now.minute) + "-" +str(time_now.second)
                        cv2.imwrite(s+".jpg", frame)
                        cv2.waitKey(2000)
                        video.release()
                        cv2.destroyAllWindows()
                        excel_data = pd.read_excel('entries.xlsx')
                        excel_data.loc[len(excel_data)] = [name,datetime.datetime.now()]
                        excel_data.to_excel('entries.xlsx',index = False)
                        messagebox.showinfo("Notification","User Detected Open the door")
                        return    
                else:   
                    text = "UnknownFace"
                    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    frame = cv2.putText(frame, text, (x, y-4),  cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,255), 1, cv2.LINE_AA)

            cv2.imshow("image", frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
                    
    messagebox.showerror("Error","Unauthorized Person doors are closed")

    video.release()
    cv2.destroyAllWindows()
            
        
    

root = Tk()
root.geometry('550x350')
root.resizable(False,False)
container = Frame(root)
container.pack(side = "top", fill = "both", expand = True)
container.grid_rowconfigure(0, weight = 1)
container.grid_columnconfigure(0, weight = 1)
startapp(container)


root.mainloop()


