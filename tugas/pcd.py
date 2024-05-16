import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
import math
import random


def calculate_mse(image1, image2):
    mse = np.mean((image1 - image2) ** 2)
    return mse


def calculate_psnr(image1, image2):
    mse = calculate_mse(image1, image2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    return psnr


def add_gaussian_noise(image, mean=0, stddev=25):
    row, col, ch = image.shape
    gauss = np.random.normal(mean, stddev, (row, col, ch))
    noisy_image = image + gauss
    noisy_image = np.clip(noisy_image, 0, 255)
    return noisy_image.astype(np.uint8)


def add_rayleigh_noise(image, scale=25):
    row, col, ch = image.shape
    rayleigh = np.random.rayleigh(scale, (row, col, ch))
    noisy_image = image + rayleigh
    noisy_image = np.clip(noisy_image, 0, 255)
    return noisy_image.astype(np.uint8)


def add_exponential_noise(image, scale=25):
    row, col, ch = image.shape
    exponential_noise = np.random.exponential(scale, (row, col, ch))
    noisy_image = image + exponential_noise
    noisy_image = np.clip(noisy_image, 0, 255)
    return noisy_image.astype(np.uint8)


def add_uniform_noise(image, low=0, high=50):
    row, col, ch = image.shape
    uniform_noise = np.random.uniform(low, high, (row, col, ch))
    noisy_image = image + uniform_noise
    noisy_image = np.clip(noisy_image, 0, 255)
    return noisy_image.astype(np.uint8)


def add_salt_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02):
    noisy_image = np.copy(image)
    num_salt = np.ceil(salt_prob * image.size * (1 / image.shape[2]))
    num_pepper = np.ceil(pepper_prob * image.size * (1 / image.shape[2]))
    for _ in range(int(num_salt)):
        i = random.randint(0, image.shape[0] - 1)
        j = random.randint(0, image.shape[1] - 1)
        noisy_image[i, j] = [255, 255, 255]
    for _ in range(int(num_pepper)):
        i = random.randint(0, image.shape[0] - 1)
        j = random.randint(0, image.shape[1] - 1)
        noisy_image[i, j] = [0, 0, 0]
    return noisy_image.astype(np.uint8)


def geometric_mean_filter(image, kernel_size=3):
    image_float = image.astype(float)
    log_image = np.log(image_float + 1)
    convolved = cv2.filter2D(
        log_image, -1, np.ones((kernel_size, kernel_size), np.float32))
    mean_log_image = convolved / (kernel_size ** 2)
    geometric_mean_image = np.exp(mean_log_image) - 1
    geometric_mean_image = np.clip(geometric_mean_image, 0, 255)
    return geometric_mean_image.astype(np.uint8)


def harmonic_mean_filter(image, kernel_size=3):
    image_float = image.astype(float)
    harmonic_image = kernel_size ** 2 / \
        cv2.filter2D(1. / (image_float + 1e-6), -1,
                     np.ones((kernel_size, kernel_size), np.float32))
    harmonic_image = np.clip(harmonic_image, 0, 255)
    return harmonic_image.astype(np.uint8)


def max_filter(image, kernel_size=3):
    return cv2.dilate(image, np.ones((kernel_size, kernel_size), np.float32))


def min_filter(image, kernel_size=3):
    return cv2.erode(image, np.ones((kernel_size, kernel_size), np.float32))


def midpoint_filter(image, kernel_size=3):
    min_filter = cv2.erode(image, np.ones(
        (kernel_size, kernel_size), np.float32))
    max_filter = cv2.dilate(image, np.ones(
        (kernel_size, kernel_size), np.float32))
    midpoint_image = (min_filter + max_filter) / 2
    return midpoint_image.astype(np.uint8)

# GUI App


class MeanFilterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NOISE")

        self.image = None
        self.processed_image = None

        self.load_button = tk.Button(
            self, text="Load Image", command=self.load_image)
        self.load_button.grid(row=0, column=0, pady=10)

        self.gaussian_noise_button = tk.Button(
            self, text="Gaussian Noise", command=self.apply_gaussian_noise)
        self.gaussian_noise_button.grid(row=0, column=1, pady=2)

        self.rayleigh_noise_button = tk.Button(
            self, text="Rayleigh Noise", command=self.apply_rayleigh_noise)
        self.rayleigh_noise_button.grid(row=0, column=2, pady=2)

        self.exponential_noise_button = tk.Button(
            self, text="Exponential Noise", command=self.apply_exponential_noise)
        self.exponential_noise_button.grid(row=0, column=3, pady=2)

        self.uniform_noise_button = tk.Button(
            self, text="Uniform Noise", command=self.apply_uniform_noise)
        self.uniform_noise_button.grid(row=0, column=4, pady=2)

        self.salt_pepper_noise_button = tk.Button(
            self, text="Salt & Pepper Noise", command=self.apply_salt_pepper_noise)
        self.salt_pepper_noise_button.grid(row=0, column=5, pady=2)

        self.geo_button = tk.Button(
            self, text="Geometric Mean Filter", command=self.apply_geometric_mean)
        self.geo_button.grid(row=0, column=6, pady=2)

        self.harmonic_button = tk.Button(
            self, text="Harmonic Mean Filter", command=self.apply_harmonic_mean)
        self.harmonic_button.grid(row=0, column=7, pady=2)

        self.max_button = tk.Button(
            self, text="Max Filter", command=self.apply_max_filter)
        self.max_button.grid(row=0, column=8, pady=2)

        self.min_button = tk.Button(
            self, text="Min Filter", command=self.apply_min_filter)
        self.min_button.grid(row=0, column=9, pady=2)

        self.midpoint_button = tk.Button(
            self, text="Midpoint Filter", command=self.apply_midpoint)
        self.midpoint_button.grid(row=0, column=10, pady=2)

        self.save_button = tk.Button(
            self, text="Save Image", command=self.save_image)
        self.save_button.grid(row=0, column=11, pady=10)

        self.image_label = tk.Label(self)
        self.image_label.grid(row=1, column=0, columnspan=12, pady=2)

    def load_image(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")]
        )
        if not filepath:
            return
        self.image = Image.open(filepath)
        self.update_image_display(self.image)

    def apply_gaussian_noise(self):
        image_cv = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        noisy_image_cv = add_gaussian_noise(image_cv)
        self.processed_image = Image.fromarray(
            cv2.cvtColor(noisy_image_cv, cv2.COLOR_BGR2RGB))
        mse = calculate_mse(np.array(self.image),
                            np.array(self.processed_image))
        psnr = calculate_psnr(np.array(self.image),
                              np.array(self.processed_image))
        print(f"MSE: {mse}, PSNR: {psnr}")
        self.update_image_display(self.processed_image)

    def apply_rayleigh_noise(self):
        image_cv = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        noisy_image_cv = add_rayleigh_noise(image_cv)
        self.processed_image = Image.fromarray(
            cv2.cvtColor(noisy_image_cv, cv2.COLOR_BGR2RGB))
        mse = calculate_mse(np.array(self.image),
                            np.array(self.processed_image))
        psnr = calculate_psnr(np.array(self.image),
                              np.array(self.processed_image))
        print(f"MSE: {mse}, PSNR: {psnr}")
        self.update_image_display(self.processed_image)

    def apply_exponential_noise(self):
        image_cv = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        noisy_image_cv = add_exponential_noise(image_cv)
        self.processed_image = Image.fromarray(
            cv2.cvtColor(noisy_image_cv, cv2.COLOR_BGR2RGB))
        mse = calculate_mse(np.array(self.image),
                            np.array(self.processed_image))
        psnr = calculate_psnr(np.array(self.image),
                              np.array(self.processed_image))
        print(f"MSE: {mse}, PSNR: {psnr}")
        self.update_image_display(self.processed_image)

    def apply_uniform_noise(self):
        image_cv = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        noisy_image_cv = add_uniform_noise(image_cv)
        self.processed_image = Image.fromarray(
            cv2.cvtColor(noisy_image_cv, cv2.COLOR_BGR2RGB))
        mse = calculate_mse(np.array(self.image),
                            np.array(self.processed_image))
        psnr = calculate_psnr(np.array(self.image),
                              np.array(self.processed_image))
        print(f"MSE: {mse}, PSNR: {psnr}")
        self.update_image_display(self.processed_image)

    def apply_salt_pepper_noise(self):
        image_cv = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        noisy_image_cv = add_salt_pepper_noise(image_cv)
        self.processed_image = Image.fromarray(
            cv2.cvtColor(noisy_image_cv, cv2.COLOR_BGR2RGB))
        mse = calculate_mse(np.array(self.image),
                            np.array(self.processed_image))
        psnr = calculate_psnr(np.array(self.image),
                              np.array(self.processed_image))
        print(f"MSE: {mse}, PSNR: {psnr}")
        self.update_image_display(self.processed_image)

    def apply_geometric_mean(self):
        image_cv = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        filtered_image_cv = geometric_mean_filter(image_cv)
        self.processed_image = Image.fromarray(
            cv2.cvtColor(filtered_image_cv, cv2.COLOR_BGR2RGB))
        mse = calculate_mse(np.array(self.image),
                            np.array(self.processed_image))
        psnr = calculate_psnr(np.array(self.image),
                              np.array(self.processed_image))
        print(f"MSE: {mse}, PSNR: {psnr}")
        self.update_image_display(self.processed_image)

    def apply_harmonic_mean(self):
        image_cv = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        filtered_image_cv = harmonic_mean_filter(image_cv)
        self.processed_image = Image.fromarray(
            cv2.cvtColor(filtered_image_cv, cv2.COLOR_BGR2RGB))
        mse = calculate_mse(np.array(self.image),
                            np.array(self.processed_image))
        psnr = calculate_psnr(np.array(self.image),
                              np.array(self.processed_image))
        print(f"MSE: {mse}, PSNR: {psnr}")
        self.update_image_display(self.processed_image)

    def apply_max_filter(self):
        image_cv = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        filtered_image_cv = max_filter(image_cv)
        self.processed_image = Image.fromarray(
            cv2.cvtColor(filtered_image_cv, cv2.COLOR_BGR2RGB))
        mse = calculate_mse(np.array(self.image),
                            np.array(self.processed_image))
        psnr = calculate_psnr(np.array(self.image),
                              np.array(self.processed_image))
        print(f"MSE: {mse}, PSNR: {psnr}")
        self.update_image_display(self.processed_image)

    def apply_min_filter(self):
        image_cv = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        filtered_image_cv = min_filter(image_cv)
        self.processed_image = Image.fromarray(
            cv2.cvtColor(filtered_image_cv, cv2.COLOR_BGR2RGB))
        mse = calculate_mse(np.array(self.image),
                            np.array(self.processed_image))
        psnr = calculate_psnr(np.array(self.image),
                              np.array(self.processed_image))
        print(f"MSE: {mse}, PSNR: {psnr}")
        self.update_image_display(self.processed_image)

    def apply_midpoint(self):
        image_cv = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        filtered_image_cv = midpoint_filter(image_cv)
        self.processed_image = Image.fromarray(
            cv2.cvtColor(filtered_image_cv, cv2.COLOR_BGR2RGB))
        mse = calculate_mse(np.array(self.image),
                            np.array(self.processed_image))
        psnr = calculate_psnr(np.array(self.image),
                              np.array(self.processed_image))
        print(f"MSE: {mse}, PSNR: {psnr}")
        self.update_image_display(self.processed_image)

    def save_image(self):
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")],
        )
        if not save_path:
            return

        self.processed_image.save(save_path)
        messagebox.showinfo("Saved", f"Image saved to {save_path}")

    def update_image_display(self, image):
        image.thumbnail((400, 400), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(image)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk


# Menjalankan aplikasi
if __name__ == "__main__":
    app = MeanFilterApp()
    app.mainloop()
