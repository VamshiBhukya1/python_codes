import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
class WeedDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automated Weed Detection in Fields")

        self.image_label = tk.Label(root, text="Upload an Image to Begin", width=50, height=15, bg="lightgrey")
        self.image_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        tk.Button(root, text="Upload Image", command=self.upload_image).grid(row=1, column=0, columnspan=2, pady=10)

        tk.Button(root, text="Detect Weeds", command=self.detect_weeds).grid(row=2, column=0, columnspan=2, pady=10)

        tk.Label(root, text="Detection Results:", font=("Arial", 12)).grid(row=3, column=0, columnspan=2, pady=10)
        self.results_label = tk.Label(root, text="", wraplength=400, justify="left")
        self.results_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.image_path = None
    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if self.image_path:
            img = Image.open(self.image_path)
            img.thumbnail((400, 400))
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img, text="")
            self.image_label.image = img
            self.results_label.config(text="")
        else:
            messagebox.showwarning("No Image Selected", "Please upload an image to proceed.")
    def detect_weeds(self):
        if not self.image_path:
            messagebox.showwarning("No Image", "Please upload an image first.")
            return

        result_text = self.process_image(self.image_path)
        self.results_label.config(text=result_text)

    @staticmethod
    def process_image(image_path):
        image = cv2.imread(image_path)
        if image is None:
            return "Error: Could not load the image."

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        _, binary = cv2.threshold(blurred, 128, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        weed_count = len(contours)
        result = f"Weed Detection Complete!\nNumber of weeds detected: {weed_count}"

        return result


if __name__ == "__main__":
    root = tk.Tk()
    app = WeedDetectionApp(root)
    root.mainloop()
