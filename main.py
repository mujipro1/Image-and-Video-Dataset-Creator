"""
GUI module for AI toolkit
Provides Functionality to upload files and process them

Developed By : Mujtaba Shafqat

"""

from tkinter import *
from tkinter import filedialog
from tkinterdnd2 import *
from tkinter import ttk
from datasetProcessor import DatasetEngine
import threading

# env variables
_primary = '#CDCDCD'
_secondary = '#A5A5A5'
_alert = '#0F9552'
_topBar = '#2c2f33'
_title = 'Powers DSB'

supportedFiles = ['.pdf', '.mp4', '.png', '.jpg', '.jpeg', '.mov', '.avi', '.webm']


class App:
    """Main GUI class"""
    root = TkinterDnD.Tk()
    def __init__(self):
        """constructor for GUI class"""
        root = self.root
        root.minsize(500, 600)
        root.state('zoomed')
        root.title(_title)
        
        self.files = []        
        
        Label(root, background=_topBar,text=_title, font=("Arial", 16),
            fg="white", height=2).pack(fill=X)
        
        frame = Frame(root, background=_primary, width=400, height=500)
        frame.pack(side=LEFT,padx=80, pady=50)
        frame.pack_propagate(0)
        
        frame.drop_target_register(DND_FILES)
        frame.dnd_bind('<<Drop>>', self.show_files)        
        
        button1 = Label(frame, text="Upload",
                        width=30, height=3, bg=_secondary, font="Arial 12",
                        fg="white", relief='flat')
        button1.bind("<Button-1>", lambda e: self.open_files())
        
        fileFrame = Frame(root, background=_secondary, width=480, height=500)
        fileFrame.pack(side=LEFT, padx=0, pady=20)
        fileFrame.pack_propagate(0)
        
        scrollframe = Frame(fileFrame, height=500)
        scrollframe.pack(side=RIGHT, fill=Y)
        
        self.treeview = ttk.Treeview(fileFrame, height=490, selectmode='browse')
        self.treeview.pack(side=LEFT, fill=BOTH, expand=True)
        self.treeview.heading('#0', text='Files', anchor='c')
        
        yscrollbar = ttk.Scrollbar(scrollframe, orient='vertical', command=self.treeview.yview)
        yscrollbar.pack(fill=Y, side=RIGHT, expand=True)
        
        self.treeview.configure(yscrollcommand=yscrollbar.set)
                
        button1.bind("<Enter>", self._enter)
        button1.bind("<Leave>", self._leave)
        
        button1.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        self.Draglabel = Label(frame, text="or \n\n Drag and drop files here",
                      bg=_primary, fg="#656565",
                      font="Arial 12")
        self.Draglabel.place(relx=0.5, rely=0.56, anchor=CENTER)
        
        btnFrame = Frame(root,width=200, height=500)
        btnFrame.pack(side=LEFT, pady=0)
        btnFrame.pack_propagate(0)

        removeButton = Button(btnFrame, text="Remove", relief='flat',
                              width=8, bg=_primary, font="Arial 10"
                              ,command=self.remove)
        removeButton.pack(side=TOP, padx=10)
        
        internalFrame = Frame(btnFrame,width=200, height=260)
        internalFrame.pack(side=TOP, padx=20)
        internalFrame.pack_propagate(0)

        # Add 2 radio buttons for augmentation horizontal and vertical
        self.augment = IntVar()
        self.augment.set(0)
        self.augmentCheck = Checkbutton(internalFrame, text="Augment horizontally", variable=self.augment, onvalue=1, offvalue=0, font="Arial 10")
        self.augmentCheck.place(x=0, y=30)

        self.augment2 = IntVar()
        self.augment2.set(0)
        self.augmentCheck2 = Checkbutton(internalFrame, text="Augment vertically", variable=self.augment2, onvalue=1, offvalue=0, font="Arial 10")
        self.augmentCheck2.place(x=0, y=60)

        # Enter the name of the dataset
        self.label = Label(internalFrame, text="Enter dataset name:", font="Arial 10")
        self.label.place(x=0, y=110)
        self.datasetName = Entry(internalFrame, width=20, font="Arial 10")
        self.datasetName.place(x=0, y=140)
        self.datasetName.insert(0, "Dataset")

        # Enter the desired size of the images in the dataset
        self.label = Label(internalFrame, text="Enter image size:", font="Arial 10")
        self.label.place(x=0, y=190)
        self.imageSize = Entry(internalFrame, width=20, font="Arial 10")
        self.imageSize.place(x=0, y=220)
        self.imageSize.insert(0, 224)

        processButton = Button(btnFrame, text="Process", relief='flat',
                               width=8, bg=_alert, fg="white", font="Arial 10"
                               , command=self.process)
        processButton.pack(side=TOP, padx=10, pady=10)

        removeButton.bind("<Enter>", self._enter)
        removeButton.bind("<Leave>", self._leave)
        
        processButton.bind("<Enter>", self._enter)
        processButton.bind("<Leave>", self._leave)
        
        
    def notify(self, message:str, flag: bool):
        """
        Shows the passed message as notification alert
        - flag = 1 for success
        - flag = 0 for error
        """
        alert = Label(self.root,font=("Arial", 12),
                            fg="white", height=2, width=20)
        
        if flag:
            alert.config(text=message, bg=_alert)
            alert.place(x=25, y=20)
            self.root.after(1500, alert.place_forget)
        else:
            alert.config(text=message, bg="red")
            alert.place(x=25, y=20)
            self.root.after(1500, alert.place_forget)
            
            
    def remove(self):
        """Remove selected file from the list"""
        if len(self.treeview.selection()) == 0:
            self.notify("No file selected!", 0)
            return
        self.files.remove(self.treeview.item(self.treeview.selection())['text'])
        self.treeview.delete(self.treeview.selection())
        self.notify("File removed!", 1)
        
        
    def show_files(self, event):
        """Show files in the list"""
        file = event.data[1:-1]
        for i in supportedFiles:
            if i in file:
                self.files.append(file)
                self.populateFrame()
                self.notify("File Uploaded!", 1)
                break
        else:
            self.notify("Unsupported File!", 0)
    
    
    def populateFrame(self):
        """Populate the list with files"""
        parent = self.treeview.get_children()
        for i in parent:
            self.treeview.delete(i)
            
        for i in range(len(self.files)):
            self.treeview.insert('', 'end', text=self.files[i]) 


    def _enter(self, e):
        """Utility function for mouse hover effect"""
        e.widget.config(cursor='hand2')
        
    def _leave(self, e):
        """Utility function for mouse hover effect"""
        e.widget.config(cursor='arrow')
        
        
    def open_files(self):
        """Open file dialog to select files"""
        files = filedialog.askopenfilenames(
            title="Select files",
            filetypes=(
                ("Video files", "*.mp4"),
                ("Image files", "*.png;*.jpg;*.jpeg"),
                ("PDF files", "*.pdf"),
                ("All files", "*.*")
            ),
        )
        
        if len(files) > 0:
            if len(files) == 1:
                self.notify("File Uploaded!", 1)
            else:
                self.notify("Files Uploaded!", 1)
        
        for i in files:
            self.files.append(i)
        self.populateFrame()

    def getFiles(self):
        """Return the list of files"""
        return self.files
                    
    def run(self):
        """Run the GUI"""
        self.root.mainloop()
                
    def process(self):
        """Process the files"""
        if len(self.files) > 0:
           
            t1 = threading.Thread(target=self._process)
            t1.start()
            
        else:
            self.notify("No files to process!", 0)
    
    def _process(self):
        """Process the files"""
        datasetName = self.datasetName.get()
        if datasetName == "":
            self.notify("Invalid dataset name!", 0)
            return

        imageSize = self.imageSize.get()
        if imageSize == "":
            self.notify("Invalid image size!", 0)
            return
        if not imageSize.isdigit():
            self.notify("Invalid image size!", 0)
            return
        imageSize = int(imageSize)
        
        for i in self.files:
            extension = i.split('.')[-1]
            if not extension in supportedFiles:
                self.notify("Unsupported File!", 0)
                return                
             
        self.PAlert = Label(self.root,font=("Arial", 12),
                        fg="white", height=2, width=20)
    
        self.PAlert.config(text="Processing...", bg=_alert)
        self.PAlert.place(x=25, y=20)
        
        dataset = DatasetEngine(self.files, self, datasetName, [self.augment.get(), self.augment2.get()], imageSize)
        
        
if __name__ == '__main__':
    """Main function"""
    app = App()
    app.run()