import cv2 as cv
from tkinter import ttk, filedialog
from tkinter import *
from PIL import ImageTk, Image
from copy import deepcopy

class MainSolution():
    def __init__(self):
        self.image = None
        self.imgray = None
        self.trsh1 = None
        self.trsh2 = None

    def load_image(self, path):
        if path:
            self.image = cv.imread(path)
            self.imgray = cv.cvtColor(cv.pyrMeanShiftFiltering(self.image, 15, 50), cv.COLOR_BGR2GRAY)

    def filt(self):
        if self.imgray is None:
            return self.get_blank_image()
        img = Image.fromarray(self.imgray)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def global_threshold(self):
        if self.imgray is None:
            return self.get_blank_image()
        ret, thresh1 = cv.threshold(self.imgray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        self.trsh1 = deepcopy(thresh1)
        img = Image.fromarray(thresh1)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def adaptive_threshold(self):
        if self.imgray is None:
            return self.get_blank_image()
        thresh2 = cv.adaptiveThreshold(self.imgray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
        self.trsh2 = deepcopy(thresh2)
        img = Image.fromarray(thresh2)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)
    
    def edge_detection(self):
        if self.image is None:
            return self.get_blank_image()
        edges = cv.Canny(self.image, 100, 200)
        img = Image.fromarray(edges)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)
    
    def non_linear_filter(self):
        if self.imgray is None:
            return self.get_blank_image()
        filtered_image = cv.GaussianBlur(self.imgray, (5, 5), 0)
        img = Image.fromarray(filtered_image)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)
    
    def get_blank_image(self):
        img = Image.new('RGB', (300, 300), color='white')
        return ImageTk.PhotoImage(img)
    

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        ms.load_image(file_path)
        update_images()

def update_images():
    img1 = ms.filt()
    lbl1.configure(image=img1)
    lbl1.image = img1

    img2 = ms.global_threshold()
    lbl2.configure(image=img2)
    lbl2.image = img2

    img3 = ms.adaptive_threshold()
    lbl3.configure(image=img3)
    lbl3.image = img3

    img4 = ms.edge_detection()
    lbl4.configure(image=img4)
    lbl4.image = img4


if __name__ == "__main__":

    root = Tk()
    ms = MainSolution()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"700x700")
    lbl_text1 = ttk.Label(text="Глобальная пороговая обработка")
    lbl_text1.place(x=250, y=10)

    lbl1 = ttk.Label(image=ms.get_blank_image())
    lbl1.place(x=30, y=40, width=300, height=300)

    lbl2 = ttk.Label(image=ms.get_blank_image())
    lbl2.place(x=370, y=40, width=300, height=300)
    
    lbl_text2 = ttk.Label(text="Адаптивная пороговая обработка")
    lbl_text2.place(x=90, y=360)

    lbl3 = ttk.Label(image=ms.get_blank_image())
    lbl3.place(x=30, y=390, width=300, height=300)

    lbl_text3 = ttk.Label(text="Нелинейный фильтр")
    lbl_text3.place(x=480, y=360)

    lbl4 = ttk.Label(image=ms.get_blank_image())
    lbl4.place(x=370, y=390, width=300, height=300)

    btn_open = ttk.Button(root, text="Открыть изображение", command=open_image)
    btn_open.place(x=10, y=10)

    root.mainloop()
