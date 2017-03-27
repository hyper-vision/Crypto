import Tkinter
import tkFileDialog as filedialog
from ttk import *
import tkMessageBox, hashlib

try:
    import Crypt_Main as Crypt
except:
    print("Modules do not exist!")

entryKey = "root"


class Begin(Tkinter.Tk):
    def __init__(self):
        leftMargin = 5
        Tkinter.Tk.__init__(self)
        self.geometry('{}x{}'.format(220, 114))
        self.title("Password")
        self.passLabel = Label(self, text="Password: ").place(x=leftMargin, y=5)
        self.e = Entry(self, show="*")
        self.e.place(x=leftMargin+80, y=5)
        self.submit = Button(self, text="Submit", command=lambda: self.auth()).place(x=leftMargin+131, y=50)
        self.cancel = Button(self, text="Cancel", command=lambda: self.cls()).place(x=leftMargin+131, y=80)

    def auth(self):
        var = self.e.get();
        if var == entryKey:
            self.destroy()
            app = CryptApp()
            app.mainloop()
        else:
            tkMessageBox.showerror(title="Error", message="Wrong Password")

    def cls(self):
        self.destroy()

class CryptApp(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.title("Securitron")
        self.geometry('{}x{}'.format(350, 200))
        self.pathLabel = Label(self, text="File Path:").grid(row=2, column=1)
        self.keyLabel = Label(self, text="Key:").grid(row=3, column=1)
        self.confLabel = Label(self, text="Confirm Key:").grid(row=4, column=1)
        self.e = Entry(self)
        self.e.grid(row=2, column=2)
        self.keyE = Entry(self, show="*")
        self.keyE.grid(row=3, column=2)
        self.kConf = Entry(self, show="*")
        self.kConf.grid(row=4, column=2)
        self.encrypt = Button(self, text="Encrypt", command=lambda: self.enc()).grid(row=2, column=3)
        self.decrypt = Button(self, text="Decrypt", command=lambda: self.dec()).grid(row=2, column=4)
        self.open = Button(self, text="Open File", command=lambda: self.opn()).grid(row=3, column=3)
        self.close = Button(self, text="Close", command=lambda: self.cls()).grid(row=3, column=4)

    def enc(self):
        try:
            path = self.e.get()
            key = self.keyE.get()
            conf = self.kConf.get()
            if key == '':
                tkMessageBox.showerror(title="No Key",
                                       message="No key has been specified!\n\nPlease ensure that the 'Key' field is not left blank!")
            elif conf != key:
                tkMessageBox.showerror(title="Key Mismatch",
                                       message="The keys entered do not match! Make sure the keys are identical.")
            else:
                hashedKey = hashlib.sha256(key).digest()
                Crypt.encrypt_file(hashedKey, path)
                self.kConf.delete(0, 'end')
                self.keyE.delete(0, 'end')
        except:
            tkMessageBox.showerror(title="Error", message="Could not open file!\n\nMake sure the path is correct!")

    def dec(self):
        try:
            path = self.e.get()
            key = self.keyE.get()
            conf = self.kConf.get()
            if key == '':
                tkMessageBox.showerror(title="No Key",
                                       message="No key has been specified!\n\nPlease ensure that the 'Key' field is not left blank!")
            elif conf != key:
                tkMessageBox.showerror(title="Key Mismatch",
                                       message="The keys entered do not match! Make sure the keys are identical.")
            else:
                hashedKey = hashlib.sha256(key).digest()
                Crypt.decrypt_file(hashedKey, path)
                self.kConf.delete(0, 'end')
                self.keyE.delete(0, 'end')
        except:
            tkMessageBox.showerror(title="Error", message="Could not open file!\n\nMake sure the path is correct!")      

    def opn(self):
        self.fileName = filedialog.askopenfilename(filetypes=(("Encrypted files", "*.enc"), ("PDF", "*.pdf"), ("Executable", "*.exe"), ("Word", "*.docx") , ("All files", "*.*")))
        fname = self.fileName
        self.e.delete(0, 'end')
        self.kConf.delete(0, 'end')
        self.keyE.delete(0, 'end')
        self.e.insert(0, fname)

    def cls(self):
        self.destroy()


app = Begin()
app.mainloop()
