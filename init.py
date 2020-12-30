from tkinter import *
from tkinter import filedialog
import main
import os
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Stegnography of image data with Quick response Code Intergrity")
try:
    class file:
        def __init__(self):
            self.path=None
            self.folder=None

        def browsefile(self):
            filename = filedialog.askopenfilename()
            pathlabel.config(text=filename)
            return filename
            
        def browsefolder(self):
            folder=filedialog.askdirectory()
            pathlabel.config(text=folder)
            return folder
        def getfilepath(self):
            self.path=self.browsefile()
            return self.path
        def getfolder(self):
            self.folder=self.browsefolder()
            return self.folder

    def encode():
    
        filename=file()
        path=filename.getfilepath()
        pathlabel.place(relx=0.5,rely=0.7, anchor=CENTER)
        pathlabel.config(text="Converting......")
        messagebox.showinfo("Converting ", "Pls wait while the conversion process completes, donot close the window !")
        shape_out=main.encoding(path)
        f = open('key.txt')
        key=f.read()
        f.close()
        shape_hex=encrypt(key,str(shape_out))
        pathlabel.config(text="comlpeted check the shapekey file for the key")
        s=open('shapekey.txt','a')
        s.write(shape_hex)
        s.close()
        messagebox.showinfo("Completed ! ", "check the results folder for QRcodes")
        #encoder will driven here

    def clean():
        basepath=os.getcwd()
        folderpath=basepath+"\\results"
        files=os.listdir(folderpath)
        file_location=folderpath+"\\"
        for _ in files:
            try:
                os.remove(file_location + _)
            except:
                pass

    
    def decode():
        value=textBox.get("1.0","end-1c")
        filename=file()
        folder=filename.getfolder()
        f = open('key.txt')
        key=f.read()
        shapekey=decrypt(key,value)
        main.decoding(shapekey,folder)
        messagebox.showinfo("completed","Success")

    def encrypt(key, msg):
        encryped = []
        for i, c in enumerate(msg):
            key_c = ord(key[i % len(key)])
            msg_c = ord(c)
            encryped.append(chr((msg_c + key_c) % 127))
        return ''.join(encryped)

    def decrypt(key, encryped):
        msg = []
        for i, c in enumerate(encryped):
            key_c = ord(key[i % len(key)])
            enc_c = ord(c)
            msg.append(chr((enc_c - key_c) % 127))
        return ''.join(msg)

except:
    messagebox.showerror("Error","Error Occured ")



encoderbtn = Button(root,text="Encode",command=encode,width=10,height=2,fg="white",bg="green")
encoderbtn.pack()

label = Label(root, text='Shape Key here: ')
label.place(relx=0.4, rely=0.1, anchor='s')

textBox=Text(root, height=2, width=10)
textBox.place(relx=0.5, rely=0.1, anchor='n')






decoderbtn= Button(root,text="Decode",command=decode,width=10,height=2,fg="white",bg="red")
decoderbtn.pack()

encoderbtn.place(relx=0.5,rely=0.5, anchor=CENTER)
decoderbtn.place(relx=0.5,rely=0.3,anchor=CENTER)
pathlabel = Label(root)


pathlabel.pack()
root.mainloop()