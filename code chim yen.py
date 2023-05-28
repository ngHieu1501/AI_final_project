#%%code
from PIL import Image, ImageTk
import PySimpleGUI as sg
import os.path
import io
import tensorflow as tf
import numpy as np
from keras.utils import to_categorical, load_img, img_to_array
# First the window layout in 2 columns

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("the predicted picture:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)


# load model 


# tải mô hình tổ yến ở đây
new_model = tf.keras.models.load_model('C:\Users\ADMIN\Desktop\hình ảnh tổ yến\ to yen.h5')




classes = ['co trung', ' to co chim me', 'to co chim non', 'to yen' ]
# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif",".jpg",".JPG"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            image = Image.open(filename)
            image.thumbnail((400, 400))
            img = load_img(filename, target_size =(200,200,3))
            imgre = img_to_array(img)
            imgre = imgre.reshape(1,200,200,3)
            imgre = imgre.astype('float32')/255
            #predict = new_model.predict(imgre)
            
            #predict_classes =[np.argmax(element) for element in predict]
            #predict_classes
            #classes[predict_classes[0]]
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            #window["-TOUT-"].update(classes[predict_classes[0]])
            window["-IMAGE-"].update(
                data = bio.getvalue()
                )

        except:
            pass

window.close()