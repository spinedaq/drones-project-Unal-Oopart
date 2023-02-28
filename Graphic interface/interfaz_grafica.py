import tkinter
import tkinter.messagebox
from tkinter import filedialog
import customtkinter
import os
from PIL import Image


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Programa de detección")
        self.geometry(f"{1100}x{650}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # load images side bar
        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imagenes")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "icono_logotipo.png")), size=(150, 150))
        self.cover_home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "portada_inicio_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "portada_inicio_dark.png")), size=(800, 650))
        self.icon_home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "icono_inicio_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "icono_inicio_dark.png")), size=(45, 45))
        self.icon_image_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "icono_imagen_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "icono_imagen_dark.png")), size=(45, 45))
        self.icon_video_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "icono_video_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "icono_video_dark.png")), size=(45, 45))
        self.icon_streaming_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "icono_streaming_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "icono_streaming_dark.png")), size=(45, 45))

        # load images sections
        self.video_inference_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "inferencia_video_imagen.png")), size=(338, 190))                                      

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="", image=self.logo_image, compound="top", font=("Microsoft GothicNeo", 20))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Seleccionar apariencia:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Claro", "Oscuro", "Sistema"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        
        self.home_button = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, border_width=0, height=40, border_spacing=10, text="Inicio",
                                                  fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                 image=self.icon_home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, padx=50, pady=10)

        self.image_button = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, border_width=0, height=40, border_spacing=10, text="Imagen",
                                                  fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                 image=self.icon_image_image, anchor="w", command=self.image_button_event)
        self.image_button.grid(row=2, column=0, padx=50, pady=10)
        
        self.video_button = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height=40, border_spacing=10, text="Video",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.icon_video_image, anchor="w", command=self.video_button_event)
        self.video_button.grid(row=3, column=0, padx=50, pady=10)

        self.streaming_button = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height=40, border_spacing=10, text="En vivo",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.icon_streaming_image, anchor="w", command=self.streaming_button_event)
        self.streaming_button.grid(row=4, column=0, padx=50, pady=10) 

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.cover_image = customtkinter.CTkLabel(self.home_frame, text="", image=self.cover_home_image)
        self.cover_image.grid(row=0, column=0)
        

        # create image frame
        self.image_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.image_frame.grid_columnconfigure(0, weight=1)

        self.image_frame_button_1 = customtkinter.CTkButton(self.image_frame, text="Boton 1", image=self.icon_image_image, compound="left")
        self.image_frame_button_1.grid(row=2, column=0, padx=(20), pady=(10))
        self.image_frame_button_2 = customtkinter.CTkButton(self.image_frame, text="Boton 2", image=self.icon_image_image, compound="right")
        self.image_frame_button_2.grid(row=3, column=0, padx=20, pady=10)
        self.image_frame_button_3 = customtkinter.CTkButton(self.image_frame, text="Boton 3", image=self.icon_image_image, compound="top")
        self.image_frame_button_3.grid(row=4, column=0, padx=20, pady=10)
        self.image_frame_button_4 = customtkinter.CTkButton(self.image_frame, text="Boton 4", image=self.icon_image_image, compound="bottom") #, anchor="w")
        self.image_frame_button_4.grid(row=5, column=0, padx=(20), pady=(10))
        

        # create video frame
        self.video_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.video_frame.grid_columnconfigure(5, weight=1)
        self.video_frame.grid_rowconfigure(5, weight=1)

        self.source_selector_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "seleccion_recursos_imagen.png")), size=(335, 53))
        self.source_selector = customtkinter.CTkLabel(self.video_frame, text="", image=self.source_selector_image)
        self.source_selector.grid(row=0, column=0, columnspan=2, padx=(20,0), pady=(19,0),sticky = "we")

        self.video_source_selector_button_1 = customtkinter.CTkButton(self.video_frame, text="Botón", image=self.icon_image_image, compound="bottom", command= self.video_source_selector_button_1_event)
        self.video_source_selector_button_1.grid(row=1, column=0, padx=20, pady=10) 

        self.video_source_selector_button_2 = customtkinter.CTkButton(self.video_frame, text="Botón", image=self.icon_image_image, compound="bottom", command= self.video_source_selector_button_2_event)
        self.video_source_selector_button_2.grid(row=1, column=1, padx=20, pady=10) 
        
       
        self.source_save_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "seleccion_guardado_imagen.png")), size=(335, 53))
        self.source_save = customtkinter.CTkLabel(self.video_frame, text="", image=self.source_save_image)
        self.source_save.grid(row=2, column=0, columnspan=2, padx=(20,0), pady=(0,0),sticky = "we")

        self.video_source_save_button_1 = customtkinter.CTkButton(self.video_frame, text="Botón", image=self.icon_image_image, compound="bottom", command= self.video_source_save_button_1_event)
        self.video_source_save_button_1.grid(row=3, column=0, padx=20, pady=10)

        self.video_source_save_button_2= customtkinter.CTkButton(self.video_frame, text="Botón", image=self.icon_image_image, compound="bottom")
        self.video_source_save_button_2.grid(row=4, column=0, padx=20, pady=10)

       
        self.visual_inference_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "visualizacion_inferencia_imagen.png")), size=(442, 53))
        self.visual_inference = customtkinter.CTkLabel(self.video_frame, text="", image=self.visual_inference_image)
        self.visual_inference.grid(row=0, column=2, padx=(20,0), pady=(19,0),sticky = "we")
        
        self.video_inference_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "inferencia_video_imagen.png")), size=(439, 247))
        self.video_inference_image2 = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "inferencia_video_imagen(2).png")), size=(329, 247))
        self.inference_video_image = customtkinter.CTkLabel(self.video_frame, text="", image=self.video_inference_image, compound="center", fg_color=('#3b8ed0','#3b8ed0')
                                                                                              , corner_radius=8, height=262)
        self.inference_video_image.grid(row=1, column=2, padx=(25,0), pady=(20, 0))

        self.progressbar_inference_video = customtkinter.CTkLabel(self.video_frame, text="Progreso: ", font=("Microsoft GothicNeo Bold", 12), anchor = "w")
        self.progressbar_inference_video.grid(row=2, column=2, padx=(0,300))

        self.progressbar = customtkinter.CTkProgressBar(self.video_frame)
        self.progressbar.grid(row=2, column=2, padx=(0,20)) #padx=(10, 20), pady=(10, 10), 
        self.progressbar.set(0.75)

        self.progressbar_inference_video2 = customtkinter.CTkLabel(self.video_frame, text="100%(9814/9814)", font=("Microsoft GothicNeo Bold", 12), anchor = "e")
        self.progressbar_inference_video2.grid(row=2, column=2, padx=(300,0))
        

        # create streaming frame
        self.streaming_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.streaming_frame.grid_columnconfigure(0, weight=1)

        self.streaming_frame_button_1 = customtkinter.CTkButton(self.streaming_frame, text="Boton 4", image=self.icon_image_image, compound="bottom")
        self.streaming_frame_button_1.grid(row=2, column=0, padx=20, pady=10)
        self.streaming_frame_button_2 = customtkinter.CTkButton(self.streaming_frame, text="Boton 2", image=self.icon_image_image, compound="right")
        self.streaming_frame_button_2.grid(row=3, column=0, padx=20, pady=10)
        self.streaming_frame_button_3 = customtkinter.CTkButton(self.streaming_frame, text="Boton 3", image=self.icon_image_image, compound="top")
        self.streaming_frame_button_3.grid(row=4, column=0, padx=20, pady=10)
        self.streaming_frame_button_4 = customtkinter.CTkButton(self.streaming_frame, text="Boton 4", image=self.icon_image_image, compound="left") #, anchor="w")
        self.streaming_frame_button_4.grid(row=5, column=0, padx=20, pady=10)

        # select default frame
        self.select_frame_by_name("home")
        self.a = 1
        self.select_source_folder = "Sin seleccionar"
        self.select_source_folder_files = "Sin seleccionar"
        self.select_folder = "Sin seleccionar"
        b = 1

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=('#0081c0', '#144870') if name == "home" else "transparent", border_width=0, corner_radius=8)
        self.image_button.configure(fg_color=('#0081c0', '#144870') if name == "image" else "transparent", border_width=0, corner_radius=8)
        self.video_button.configure(fg_color=('#0081c0', '#144870') if name == "video" else "transparent",border_width=0, corner_radius=8)
        self.streaming_button.configure(fg_color=('#0081c0', '#144870') if name == "streaming" else "transparent", border_width=0, corner_radius=8)

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "image":
            self.image_frame.grid(row=0, column=1, sticky="nsew")
            print("condición")
        else:
            self.image_frame.grid_forget()
            print("descondición")
        if name == "video":
            self.video_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.video_frame.grid_forget()
        if name == "streaming":
            self.streaming_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.streaming_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def image_button_event(self):
        self.select_frame_by_name("image")

    def video_button_event(self):
        self.select_frame_by_name("video")

    def streaming_button_event(self):
        self.select_frame_by_name("streaming")
    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        self.appearance = {"Claro":"Light", "Oscuro":"Dark","Sistema":"System"}
        customtkinter.set_appearance_mode(self.appearance[new_appearance_mode]) 

    def video_source_selector_button_1_event(self):
        if self.a == 1:
            self.inference_video_image.configure(image=self.video_inference_image2)
            self.a = 2        
        else:
            self.inference_video_image.configure(image=self.video_inference_image)
            self.a = 1     

    def video_source_selector_button_2_event(self):
        self.select_source_folder = filedialog.askdirectory()
        print(self.select_source_folder)
        self.select_source_folder_files = []
        for file in os.listdir(self.select_source_folder):
            if os.path.isfile(os.path.join(self.select_source_folder, file)):
                self.select_source_folder_files.append(file)
        print(self.select_source_folder_files)

    def video_source_save_button_1_event(self):
        self.select_folder = filedialog.askdirectory()
        print(self.select_folder)
    

if __name__ == "__main__":
    app = App()
    app.mainloop()