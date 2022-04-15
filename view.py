import tkinter as tk


import resize


def view():
    root = tk.Tk()
    root.geometry('400x400')
    root.title('PictureResize')

    # MAIN FRAME
    frame = tk.Frame(root)
    frame.pack(fill = tk.BOTH, padx=10, pady=10)

    # FILE DROP FRAME
    labelframe = tk.LabelFrame(
        frame, width=300, height=250, text="DROP HERE", bg="white", bd=5,
        relief="ridge"
    )
    labelframe.pack(fill=tk.X)

    # FILE NAME
    global before_picture_entry
    before_picture_label = tk.Label(frame, text="WHAT'S PICTURE")
    before_picture_label.pack(anchor=tk.W)
    before_picture_entry = tk.Entry(frame, width=15)
    before_picture_entry.pack(anchor=tk.W)

    # CHANGE RESOLUTION
    global resolution_entry
    resolution_label = tk.Label(frame, text='SIZE')
    resolution_label.pack(anchor=tk.W)
    resolution_entry = tk.Entry(frame, width=5)
    resolution_entry.pack(anchor=tk.W)

    '''
    TODO
    - add function "SAVE AS"
    - drag and drop
    '''

    # RUN
    runButton = tk.Button(text='RUN', command=resize.run)
    runButton.pack(anchor=tk.W)

    root.mainloop()

def get_values():
    get_filename = before_picture_entry.get()
    get_resolution = resolution_entry.get()
    return get_filename, get_resolution

if __name__ == '__main__':
    view()