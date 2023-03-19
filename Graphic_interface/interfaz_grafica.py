import tkinter
import tkinter.messagebox
from tkinter import filedialog
from tkinter import ttk
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
        self.geometry(f"{1205}x{650}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # load images side bar
        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "icono_logotipo.png")), size=(150, 150))
        self.cover_home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "portada_inicio_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "portada_inicio_dark.png")), size=(910, 650))
        self.icon_home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "icono_inicio_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "icono_inicio_dark.png")), size=(45, 45))
        self.icon_image_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "icono_imagen_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "icono_imagen_dark.png")), size=(45, 45))
        self.icon_video_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "icono_video_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "icono_video_dark.png")), size=(45, 45))
        self.icon_streaming_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "icono_streaming_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "icono_streaming_dark.png")), size=(45, 45))
                                             

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
        self.image_frame.grid_columnconfigure(5, weight=1)
        self.image_frame.grid_rowconfigure(5, weight=1)

        self.source_selector_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "seleccion_recursos_imagen.png")), size=(335, 53))
        self.source_selector = customtkinter.CTkLabel(self.image_frame, text="", image=self.source_selector_image)
        self.source_selector.grid(row=0, column=0, columnspan=2, padx=(0,20), pady=(19,0),sticky = "we")

        self.icon_upload_files_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "subir_archivos_imagen_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "subir_archivos_imagen_dark.png")), size=(45, 45))
        self.image_source_selector_button_1 = customtkinter.CTkButton(self.image_frame, text="SELECCIONAR CARPETA \n DE RECURSOS", image=self.icon_upload_files_image, compound="bottom", command= self.image_source_selector_button_1_event, height = 250)
        self.image_source_selector_button_1.grid(row=1, column=0, pady=(20,0)) 

        self.image_source_scrollable_frame = customtkinter.CTkScrollableFrame( self.image_frame, label_text="Elementos seleccionados")
        self.image_source_scrollable_frame.grid(row=1, column=1, padx=(0,60), pady=(20,0))
        self.image_select_source_folder_files = "Sin seleccionar" #Default value
        self.image_source_scrollable_elements = customtkinter.CTkLabel(master = self.image_source_scrollable_frame, text = self.image_select_source_folder_files, anchor="center")
        self.image_source_scrollable_elements.grid(row=0, column=0, padx = (55,0))

       
        self.source_save_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "seleccion_guardado_imagen.png")), size=(335, 53))
        self.source_save = customtkinter.CTkLabel(self.image_frame, text="", image=self.source_save_image)
        self.source_save.grid(row=2, column=0, columnspan=2, padx=(0,20), pady=(20,0),sticky = "we")

        self.icon_download_files_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "bajar_archivos_imagen_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "bajar_archivos_imagen_dark.png")), size=(45, 45))
        self.image_source_save_button_1 = customtkinter.CTkButton(self.image_frame, text="SELECCIONAR CARPETA \n DE GUARDADO", image=self.icon_download_files_image, compound="bottom", command= self.image_source_save_button_1_event, height=165)
        self.image_source_save_button_1.grid(row=3, column=0, rowspan = 2, padx=20, pady=(30,0))
        self.image_source_save_scrollable_frame = customtkinter.CTkScrollableFrame( self.image_frame, label_text="Carpeta seleccionada", height = 100, orientation= "horizontal", width=222)
        self.image_source_save_scrollable_frame.grid(row=3, column=1, rowspan = 2, padx=(0,50), pady=(30,0))
        self.image_select_folder = "Sin seleccionar" #Default value
        self.image_source_save_scrollable_folder = customtkinter.CTkLabel(master = self.image_source_save_scrollable_frame, text = self.image_select_folder, anchor = "w", compound="left")
        self.image_source_save_scrollable_folder.grid(row=0, column=0, padx=(65,0))


       
        self.visual_inference_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "visualizacion_inferencia_imagen.png")), size=(442, 53))
        self.visual_inference = customtkinter.CTkLabel(self.image_frame, text="", image=self.visual_inference_image)
        self.visual_inference.grid(row=0, column=2, padx=(0,0), pady=(19,0),sticky = "we")
        
        self.image_inference_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "inferencia_video_imagen.png")), size=(439, 247))
        self.image_inference_image2 = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "inferencia_video_imagen(2).png")), size=(439, 247))#(329, 247))
        self.inference_image_image = customtkinter.CTkLabel(self.image_frame, text="", image=self.image_inference_image, compound="center", fg_color=('#3b8ed0','#3b8ed0')
                                                                                              , corner_radius=8, height=262)
        self.inference_image_image.grid(row=1, column=2, padx=(0,0), pady=(20, 0))

        self.progressbar_inference_image = customtkinter.CTkLabel(self.image_frame, text="PROGRESO:", font=("Microsoft GothicNeo Bold", 12), anchor = "w")
        self.progressbar_inference_image.grid(row=2, column=2, padx=(0,325))

        self.progressbar = customtkinter.CTkProgressBar(self.image_frame, height = 20)
        self.progressbar.grid(row=2, column=2, padx=(0,40)) #padx=(10, 20), pady=(10, 10), 
        self.progressbar.set(0.75)

        self.progressbar_inference_status_image = customtkinter.CTkLabel(self.image_frame, text="100%(9814/9814)", font=("Microsoft GothicNeo Bold", 12), anchor = "e")
        self.progressbar_inference_status_image.grid(row=2, column=2, padx=(300,0))

        self.progressbar_inference_info_image = customtkinter.CTkLabel(self.image_frame, text="FPS: 30 \n Tiempo de inicio: 9:38 \n Tiempo de inferencia: 10:15", font=("Microsoft GothicNeo Bold", 12))
        self.progressbar_inference_info_image.grid(row=3, column=2, padx=(0,200))

        self.image_inference_reset_button = customtkinter.CTkButton(self.image_frame, text="Resetear", command = self.image_inference_reset_button_event, anchor="center", height = 50) #, image=self.icon_image_image, compound="bottom", command= self.video_source_save_button_1_event) # image=self.icon_image_image,
        self.image_inference_reset_button.grid(row=3, column=2, padx=(200,0), pady=(0,0))

        self.image_inference_start_button = customtkinter.CTkButton(self.image_frame, text="Empezar", command = self.image_inference_start_button_event, anchor="center", height = 50) #, image=self.icon_image_image, compound="bottom", command= self.video_source_save_button_1_event) # image=self.icon_image_image,
        self.image_inference_start_button.grid(row=4, column=2, padx=(0,200), pady=(0,0))

        self.image_inference_stop_button = customtkinter.CTkButton(self.image_frame, text="Detener", command = self.image_inference_stop_button_event, anchor="center", height= 50) #, image=self.icon_image_image, compound="bottom", command= self.video_source_save_button_1_event) # image=self.icon_image_image,
        self.image_inference_stop_button.grid(row=4, column=2, padx=(200,0), pady=(0,0))
        

        # create video frame
        self.video_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.video_frame.grid_columnconfigure(5, weight=1)
        self.video_frame.grid_rowconfigure(5, weight=1)

        self.source_selector_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "seleccion_recursos_imagen.png")), size=(335, 53))
        self.source_selector = customtkinter.CTkLabel(self.video_frame, text="", image=self.source_selector_image)
        self.source_selector.grid(row=0, column=0, columnspan=2, padx=(0,20), pady=(19,0),sticky = "we")

        self.icon_upload_files_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "subir_archivos_imagen_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "subir_archivos_imagen_dark.png")), size=(45, 45))
        self.video_source_selector_button_1 = customtkinter.CTkButton(self.video_frame, text="SELECCIONAR CARPETA \n DE RECURSOS", image=self.icon_upload_files_image, compound="bottom", command= self.video_source_selector_button_1_event, height = 250)
        self.video_source_selector_button_1.grid(row=1, column=0, pady=(20,0)) 

        self.video_source_scrollable_frame = customtkinter.CTkScrollableFrame( self.video_frame, label_text="Elementos seleccionados")
        self.video_source_scrollable_frame.grid(row=1, column=1, padx=(0,60), pady=(20,0))
        self.video_select_source_folder_files = "Sin seleccionar" #Default value
        self.video_source_scrollable_elements = customtkinter.CTkLabel(master = self.video_source_scrollable_frame, text = self.video_select_source_folder_files, anchor="center")
        self.video_source_scrollable_elements.grid(row=0, column=0, padx = (55,0))

       
        self.source_save_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "seleccion_guardado_imagen.png")), size=(335, 53))
        self.source_save = customtkinter.CTkLabel(self.video_frame, text="", image=self.source_save_image)
        self.source_save.grid(row=2, column=0, columnspan=2, padx=(0,20), pady=(20,0),sticky = "we")

        self.icon_download_files_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "bajar_archivos_imagen_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "bajar_archivos_imagen_dark.png")), size=(45, 45))
        self.video_source_save_button_1 = customtkinter.CTkButton(self.video_frame, text="SELECCIONAR CARPETA \n DE GUARDADO", image=self.icon_download_files_image, compound="bottom", command= self.video_source_save_button_1_event, height=165)
        self.video_source_save_button_1.grid(row=3, column=0, rowspan = 2, padx=20, pady=(30,0))
        self.video_source_save_scrollable_frame = customtkinter.CTkScrollableFrame( self.video_frame, label_text="Carpeta seleccionada", height = 100, orientation= "horizontal", width=222)
        self.video_source_save_scrollable_frame.grid(row=3, column=1, rowspan = 2, padx=(0,50), pady=(30,0))
        self.video_select_folder = "Sin seleccionar" #Default value
        self.video_source_save_scrollable_folder = customtkinter.CTkLabel(master = self.video_source_save_scrollable_frame, text = self.video_select_folder, anchor = "w", compound="left")
        self.video_source_save_scrollable_folder.grid(row=0, column=0, padx=(65,0))

       
        self.visual_inference_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "visualizacion_inferencia_imagen.png")), size=(442, 53))
        self.visual_inference = customtkinter.CTkLabel(self.video_frame, text="", image=self.visual_inference_image)
        self.visual_inference.grid(row=0, column=2, padx=(0,0), pady=(19,0),sticky = "we")
        
        self.video_inference_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "inferencia_video_imagen.png")), size=(439, 247))
        self.video_inference_image2 = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "inferencia_video_imagen(2).png")), size=(439, 247))#(329, 247))
        self.inference_video_image = customtkinter.CTkLabel(self.video_frame, text="", image=self.video_inference_image, compound="center", fg_color=('#3b8ed0','#3b8ed0')
                                                                                              , corner_radius=8, height=262)
        self.inference_video_image.grid(row=1, column=2, padx=(0,0), pady=(20, 0))

        self.progressbar_inference_video = customtkinter.CTkLabel(self.video_frame, text="PROGRESO:", font=("Microsoft GothicNeo Bold", 12), anchor = "w")
        self.progressbar_inference_video.grid(row=2, column=2, padx=(0,325))

        self.progressbar = customtkinter.CTkProgressBar(self.video_frame, height = 20)
        self.progressbar.grid(row=2, column=2, padx=(0,40)) #padx=(10, 20), pady=(10, 10), 
        self.progressbar.set(0.75)

        self.progressbar_inference_status_video = customtkinter.CTkLabel(self.video_frame, text="100%(9814/9814)", font=("Microsoft GothicNeo Bold", 12), anchor = "e")
        self.progressbar_inference_status_video.grid(row=2, column=2, padx=(300,0))

        self.progressbar_inference_info_video = customtkinter.CTkLabel(self.video_frame, text="FPS: 30 \n Tiempo de inicio: 9:38 \n Tiempo de inferencia: 10:15", font=("Microsoft GothicNeo Bold", 12))
        self.progressbar_inference_info_video.grid(row=3, column=2, padx=(0,200))

        self.video_inference_reset_button = customtkinter.CTkButton(self.video_frame, text="Resetear", command = self.video_inference_reset_button_event, anchor="center", height = 50) #, image=self.icon_image_image, compound="bottom", command= self.video_source_save_button_1_event) # image=self.icon_image_image,
        self.video_inference_reset_button.grid(row=3, column=2, padx=(200,0), pady=(0,0))

        self.video_inference_start_button = customtkinter.CTkButton(self.video_frame, text="Empezar", command = self.video_inference_start_button_event, anchor="center", height = 50) #, image=self.icon_image_image, compound="bottom", command= self.video_source_save_button_1_event) # image=self.icon_image_image,
        self.video_inference_start_button.grid(row=4, column=2, padx=(0,200), pady=(0,0))

        self.video_inference_stop_button = customtkinter.CTkButton(self.video_frame, text="Detener", command = self.video_inference_stop_button_event, anchor="center", height= 50) #, image=self.icon_image_image, compound="bottom", command= self.video_source_save_button_1_event) # image=self.icon_image_image,
        self.video_inference_stop_button.grid(row=4, column=2, padx=(200,0), pady=(0,0))
        

        # create streaming frame
        self.streaming_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.streaming_frame.grid_columnconfigure(5, weight=1)
        self.streaming_frame.grid_rowconfigure(5, weight=1)

        self.source_selector_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "seleccion_recursos_imagen.png")), size=(335, 53))
        self.source_selector = customtkinter.CTkLabel(self.streaming_frame, text="", image=self.source_selector_image)
        self.source_selector.grid(row=0, column=0, columnspan=2, padx=(0,20), pady=(19,0),sticky = "we")

        self.icon_upload_files_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "subir_archivos_imagen_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "subir_archivos_imagen_dark.png")), size=(45, 45))
        self.streaming_source_selector_button_1 = customtkinter.CTkButton(self.streaming_frame, text="INGRESAR LINK DEL EN \n VIVO", image=self.icon_upload_files_image, compound="bottom", command= self.streaming_source_selector_button_1_event, height = 165)
        self.streaming_source_selector_button_1.grid(row=1, column=0, pady=(20,0)) 

        self.streaming_source_scrollable_frame = customtkinter.CTkScrollableFrame( self.streaming_frame, label_text="Link ingresado", height = 100, orientation= "horizontal", width=222)
        self.streaming_source_scrollable_frame.grid(row=1, column=1, padx=(0,60), pady=(20,0))
        self.streaming_select_source_folder_files = "Sin ingresar" #Default value
        self.streaming_source_scrollable_elements = customtkinter.CTkLabel(master = self.streaming_source_scrollable_frame, text = self.streaming_select_source_folder_files, anchor="center")
        self.streaming_source_scrollable_elements.grid(row=0, column=0, padx = (75,0))

       
        self.source_save_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "seleccion_guardado_imagen.png")), size=(335, 53))
        self.source_save = customtkinter.CTkLabel(self.streaming_frame, text="", image=self.source_save_image)
        self.source_save.grid(row=2, column=0, columnspan=2, padx=(0,20), pady=(20,0),sticky = "we")

        self.icon_download_files_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "bajar_archivos_imagen_light.png")),
                                                 dark_image=Image.open(os.path.join(self.image_path, "bajar_archivos_imagen_dark.png")), size=(45, 45))
        self.streaming_source_save_button_1 = customtkinter.CTkButton(self.streaming_frame, text="SELECCIONAR CARPETA \n DE GUARDADO", image=self.icon_download_files_image, compound="bottom", command= self.streaming_source_save_button_1_event, height=165)
        self.streaming_source_save_button_1.grid(row=3, column=0, rowspan = 2, padx=20, pady=(30,0))
        self.streaming_source_save_scrollable_frame = customtkinter.CTkScrollableFrame( self.streaming_frame, label_text="Carpeta seleccionada", height = 100, orientation= "horizontal", width=222)
        self.streaming_source_save_scrollable_frame.grid(row=3, column=1, rowspan = 2, padx=(0,50), pady=(30,0))
        self.streaming_select_folder = "Sin seleccionar" #Default value
        self.streaming_source_save_scrollable_folder = customtkinter.CTkLabel(master = self.streaming_source_save_scrollable_frame, text = self.streaming_select_folder, anchor = "w", compound="left")
        self.streaming_source_save_scrollable_folder.grid(row=0, column=0, padx=(65,0))

       
        self.visual_inference_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "visualizacion_inferencia_imagen.png")), size=(442, 53))
        self.visual_inference = customtkinter.CTkLabel(self.streaming_frame, text="", image=self.visual_inference_image)
        self.visual_inference.grid(row=0, column=2, padx=(0,0), pady=(19,0),sticky = "we")
        
        self.streaming_inference_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "inferencia_video_imagen.png")), size=(439, 247))
        self.streaming_inference_image2 = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "inferencia_video_imagen(2).png")), size=(439, 247))#(329, 247))
        self.inference_streaming_image = customtkinter.CTkLabel(self.streaming_frame, text="", image=self.streaming_inference_image, compound="center", fg_color=('#3b8ed0','#3b8ed0')
                                                                                              , corner_radius=8, height=262)
        self.inference_streaming_image.grid(row=1, column=2, padx=(0,0), pady=(20, 0))

        self.progressbar_inference_streaming = customtkinter.CTkLabel(self.streaming_frame, text="PROGRESO:", font=("Microsoft GothicNeo Bold", 12), anchor = "w")
        self.progressbar_inference_streaming.grid(row=2, column=2, padx=(0,325))

        self.progressbar = customtkinter.CTkProgressBar(self.streaming_frame, height = 20)
        self.progressbar.grid(row=2, column=2, padx=(0,40)) #padx=(10, 20), pady=(10, 10), 
        self.progressbar.set(0.75)

        self.progressbar_inference_status_streaming = customtkinter.CTkLabel(self.streaming_frame, text="100%(9814/9814)", font=("Microsoft GothicNeo Bold", 12), anchor = "e")
        self.progressbar_inference_status_streaming.grid(row=2, column=2, padx=(300,0))

        self.progressbar_inference_info_streaming = customtkinter.CTkLabel(self.streaming_frame, text="FPS: 30 \n Tiempo de inicio: 9:38 \n Tiempo de inferencia: 10:15", font=("Microsoft GothicNeo Bold", 12))
        self.progressbar_inference_info_streaming.grid(row=3, column=2, padx=(0,200))

        self.streaming_inference_reset_button = customtkinter.CTkButton(self.streaming_frame, text="Resetear", command = self.streaming_inference_reset_button_event, anchor="center", height = 50) #, image=self.icon_image_image, compound="bottom", command= self.streaming_source_save_button_1_event) # image=self.icon_image_image,
        self.streaming_inference_reset_button.grid(row=3, column=2, padx=(200,0), pady=(0,0))

        self.streaming_inference_start_button = customtkinter.CTkButton(self.streaming_frame, text="Empezar", command = self.streaming_inference_start_button_event, anchor="center", height = 50) #, image=self.icon_image_image, compound="bottom", command= self.streaming_source_save_button_1_event) # image=self.icon_image_image,
        self.streaming_inference_start_button.grid(row=4, column=2, padx=(0,200), pady=(0,0))

        self.streaming_inference_stop_button = customtkinter.CTkButton(self.streaming_frame, text="Detener", command = self.streaming_inference_stop_button_event, anchor="center", height= 50) #, image=self.icon_image_image, compound="bottom", command= self.streaming_source_save_button_1_event) # image=self.icon_image_image,
        self.streaming_inference_stop_button.grid(row=4, column=2, padx=(200,0), pady=(0,0))

        # select default frame
        self.select_frame_by_name("home")
        self.state_1_streaming = 0
        self.state_2_streaming = 0
        self.state_1_video = 0
        self.state_2_video = 0
        self.state_1_image = 0
        self.state_2_image = 0
        self.streaming_select_source_folder = "Sin ingresar"
        self.streaming_inference_start_button.configure(state="disabled")
        self.streaming_inference_stop_button.configure(state="disabled")
        self.video_select_source_folder = "Sin seleccionar"
        self.video_inference_start_button.configure(state="disabled")
        self.video_inference_stop_button.configure(state="disabled")
        self.image_select_source_folder = "Sin seleccionar"
        self.image_inference_start_button.configure(state="disabled")
        self.image_inference_stop_button.configure(state="disabled")
        


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
        else:
            self.image_frame.grid_forget()
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

#Functions image
    def image_source_selector_button_1_event(self):
        if self.state_2_image == 1:
            self.inference_image_image.configure(image=self.image_inference_image2)
            self.state_1_image = 1
            self.image_inference_start_button.configure(state="enabled")
            self.image_inference_stop_button.configure(state="disabled")       
        else:
            self.inference_image_image.configure(image=self.image_inference_image)
            self.state_1_image = 1
        self.image_select_source_folder = filedialog.askdirectory()
        print(self.image_select_source_folder)
        self.image_select_source_folder_files = []
        self.image_select_source_folder_files.clear()
        for file in os.listdir(self.image_select_source_folder):
            if os.path.isfile(os.path.join(self.image_select_source_folder, file)):
                self.image_select_source_folder_files.append(file)
        print(self.image_select_source_folder_files)
        self.image_source_scrollable_frame.destroy()
        self.image_source_scrollable_frame = customtkinter.CTkScrollableFrame( self.image_frame, label_text="Elementos seleccionados")#, orientation="horizontal")
        self.image_source_scrollable_frame.grid(row=1, column=1, padx=(0,60), pady=(20,0))
        for i in range(len(self.image_select_source_folder_files)):
            self.image_source_scrollable_elements = customtkinter.CTkLabel(master = self.image_source_scrollable_frame, text = self.image_select_source_folder_files[i], anchor = "w", compound="left")
            self.image_source_scrollable_elements.grid(row=i, column=0, padx=(0,0))


    def image_source_save_button_1_event(self):
        self.image_select_folder = filedialog.askdirectory()
        print(self.image_select_folder)
        self.image_source_save_scrollable_frame.destroy()
        self.image_source_save_scrollable_frame = customtkinter.CTkScrollableFrame( self.image_frame, label_text="Carpeta seleccionada", height = 100, orientation= "horizontal", width=222)
        self.image_source_save_scrollable_frame.grid(row=3, column=1, rowspan=2, padx=(0,50), pady=(30,0))
        self.image_source_save_scrollable_folder = customtkinter.CTkLabel(master = self.image_source_save_scrollable_frame, text = self.image_select_folder, anchor = "w", compound="left")
        self.image_source_save_scrollable_folder.grid(row=0, column=0, padx=(0,0))
        if self.state_1_image == 1:
            self.state_2_image = 1
            self.image_inference_start_button.configure(state="enabled")
            self.image_inference_stop_button.configure(state="disabled")
        else:
            self.state_2_image = 1


    def image_inference_reset_button_event(self):
        self.image_source_scrollable_frame.destroy()
        self.image_source_scrollable_frame = customtkinter.CTkScrollableFrame( self.image_frame, label_text="Elementos seleccionados")
        self.image_source_scrollable_frame.grid(row=1, column=1, padx=(0,60), pady=(20,0))
        self.image_select_source_folder_files = "Sin seleccionar" #Default value
        self.image_source_scrollable_elements = customtkinter.CTkLabel(master = self.image_source_scrollable_frame, text = self.image_select_source_folder_files, anchor="center")
        self.image_source_scrollable_elements.grid(row=0, column=0, padx = (55,0))
        
        self.image_source_save_button_1 = customtkinter.CTkButton(self.image_frame, text="SELECCIONAR CARPETA \n DE GUARDADO", image=self.icon_download_files_image, compound="bottom", command= self.image_source_save_button_1_event, height=165)
        self.image_source_save_button_1.grid(row=3, column=0, rowspan = 2, padx=20, pady=(30,0))
        self.image_source_save_scrollable_frame = customtkinter.CTkScrollableFrame( self.image_frame, label_text="Carpeta seleccionada", height = 100, orientation= "horizontal", width=222)
        self.image_source_save_scrollable_frame.grid(row=3, column=1, rowspan = 2, padx=(0,50), pady=(30,0))
        self.image_select_folder = "Sin seleccionar" #Default value
        self.image_source_save_scrollable_folder = customtkinter.CTkLabel(master = self.image_source_save_scrollable_frame, text = self.image_select_folder, anchor = "w", compound="left")
        self.image_source_save_scrollable_folder.grid(row=0, column=0, padx=(65,0))

        self.state_2_image = 0
        self.state_1_image = 0
        self.image_inference_start_button.configure(state="disabled")
        self.image_inference_stop_button.configure(state="disabled")

    
    def image_inference_start_button_event(self):
        self.image_inference_start_button.configure(state="disabled")
        self.image_inference_stop_button.configure(state="enabled")
    
    
    def image_inference_stop_button_event(self):
        self.image_inference_start_button.configure(state="enabled")
        self.image_inference_stop_button.configure(state="disabled")        
    

#Functions video
    def video_source_selector_button_1_event(self):
        if self.state_2_video == 1:
            self.inference_video_image.configure(image=self.video_inference_image2)
            self.state_1_video = 1
            self.video_inference_start_button.configure(state="enabled")
            self.video_inference_stop_button.configure(state="disabled")       
        else:
            self.inference_video_image.configure(image=self.video_inference_image)
            self.state_1_video = 1
        self.video_select_source_folder = filedialog.askdirectory()
        print(self.video_select_source_folder)
        self.video_select_source_folder_files = []
        self.video_select_source_folder_files.clear()
        for file in os.listdir(self.video_select_source_folder):
            if os.path.isfile(os.path.join(self.video_select_source_folder, file)):
                self.video_select_source_folder_files.append(file)
        print(self.video_select_source_folder_files)
        self.video_source_scrollable_frame.destroy()
        self.video_source_scrollable_frame = customtkinter.CTkScrollableFrame( self.video_frame, label_text="Elementos seleccionados")#, orientation="horizontal")
        self.video_source_scrollable_frame.grid(row=1, column=1, padx=(0,60), pady=(20,0))
        for i in range(len(self.video_select_source_folder_files)):
            self.video_source_scrollable_elements = customtkinter.CTkLabel(master = self.video_source_scrollable_frame, text = self.video_select_source_folder_files[i], anchor = "w", compound="left")
            self.video_source_scrollable_elements.grid(row=i, column=0, padx=(0,0))
    

    def video_source_save_button_1_event(self):
        self.video_select_folder = filedialog.askdirectory()
        print(self.video_select_folder)
        self.video_source_save_scrollable_frame.destroy()
        self.video_source_save_scrollable_frame = customtkinter.CTkScrollableFrame( self.video_frame, label_text="Carpeta seleccionada", height = 100, orientation= "horizontal", width=222)
        self.video_source_save_scrollable_frame.grid(row=3, column=1, rowspan=2, padx=(0,50), pady=(30,0))
        self.video_source_save_scrollable_folder = customtkinter.CTkLabel(master = self.video_source_save_scrollable_frame, text = self.video_select_folder, anchor = "w", compound="left")
        self.video_source_save_scrollable_folder.grid(row=0, column=0, padx=(0,0))
        if self.state_1_video == 1:
            self.state_2_video = 1
            self.video_inference_start_button.configure(state="enabled")
            self.video_inference_stop_button.configure(state="disabled")
        else:
            self.state_2_video = 1

    
    def video_inference_reset_button_event(self):
        self.video_source_scrollable_frame.destroy()
        self.video_source_scrollable_frame = customtkinter.CTkScrollableFrame( self.video_frame, label_text="Elementos seleccionados")
        self.video_source_scrollable_frame.grid(row=1, column=1, padx=(0,60), pady=(20,0))
        self.video_select_source_folder_files = "Sin seleccionar" #Default value
        self.video_source_scrollable_elements = customtkinter.CTkLabel(master = self.video_source_scrollable_frame, text = self.video_select_source_folder_files, anchor="center")
        self.video_source_scrollable_elements.grid(row=0, column=0, padx = (55,0))
        
        self.video_source_save_button_1 = customtkinter.CTkButton(self.video_frame, text="SELECCIONAR CARPETA \n DE GUARDADO", image=self.icon_download_files_image, compound="bottom", command= self.video_source_save_button_1_event, height=165)
        self.video_source_save_button_1.grid(row=3, column=0, rowspan = 2, padx=20, pady=(30,0))
        self.video_source_save_scrollable_frame = customtkinter.CTkScrollableFrame( self.video_frame, label_text="Carpeta seleccionada", height = 100, orientation= "horizontal", width=222)
        self.video_source_save_scrollable_frame.grid(row=3, column=1, rowspan = 2, padx=(0,50), pady=(30,0))
        self.video_select_folder = "Sin seleccionar" #Default value
        self.video_source_save_scrollable_folder = customtkinter.CTkLabel(master = self.video_source_save_scrollable_frame, text = self.video_select_folder, anchor = "w", compound="left")
        self.video_source_save_scrollable_folder.grid(row=0, column=0, padx=(65,0))

        self.state_2_video = 0
        self.state_1_video = 0
        self.video_inference_start_button.configure(state="disabled")
        self.video_inference_stop_button.configure(state="disabled")


    def video_inference_start_button_event(self):
        self.video_inference_start_button.configure(state="disabled")
        self.video_inference_stop_button.configure(state="enabled")

    
    def video_inference_stop_button_event(self):
        self.video_inference_start_button.configure(state="enabled")
        self.video_inference_stop_button.configure(state="disabled")
            

#Functions streaming
    def streaming_source_selector_button_1_event(self):
        if self.state_2_streaming == 1:
            self.inference_streaming_image.configure(image=self.streaming_inference_image2)
            self.state_1_streaming = 1
            self.streaming_inference_start_button.configure(state="enabled")
            self.streaming_inference_stop_button.configure(state="disabled")       
        else:
            self.inference_streaming_image.configure(image=self.streaming_inference_image)
            self.state_1_streaming = 1
        self.streaming_select_source_folder = customtkinter.CTkInputDialog(text="Ingresa el link del en vivo", title="Ingreso de link")
        self.streaming_select_source_folder = self.streaming_select_source_folder.get_input()
        print(self.streaming_select_source_folder)
        self.streaming_select_source_folder_files = []
        self.streaming_select_source_folder_files.clear()
        self.streaming_select_source_folder_files = self.streaming_select_source_folder
        self.streaming_source_scrollable_frame.destroy()
        self.streaming_source_scrollable_frame = customtkinter.CTkScrollableFrame( self.streaming_frame, label_text="En vivo seleccionado", height = 100, orientation= "horizontal", width=222)
        self.streaming_source_scrollable_frame.grid(row=1, column=1, padx=(0,60), pady=(20,0))
        self.streaming_source_scrollable_elements = customtkinter.CTkLabel(master = self.streaming_source_scrollable_frame, text = self.streaming_select_source_folder_files, anchor = "w", compound="left")
        self.streaming_source_scrollable_elements.grid(row=0, column=0, padx=(0,0))


    def streaming_source_save_button_1_event(self):
        self.streaming_select_folder = filedialog.askdirectory()
        print(self.streaming_select_folder)
        self.streaming_source_save_scrollable_frame.destroy()
        self.streaming_source_save_scrollable_frame = customtkinter.CTkScrollableFrame( self.streaming_frame, label_text="Carpeta seleccionada", height = 100, orientation= "horizontal", width=222)
        self.streaming_source_save_scrollable_frame.grid(row=3, column=1, rowspan=2, padx=(0,50), pady=(30,0))
        self.streaming_source_save_scrollable_folder = customtkinter.CTkLabel(master = self.streaming_source_save_scrollable_frame, text = self.streaming_select_folder, anchor = "w", compound="left")
        self.streaming_source_save_scrollable_folder.grid(row=0, column=0, padx=(0,0))
        if self.state_1_streaming == 1:
            self.state_2_streaming = 1
            self.streaming_inference_start_button.configure(state="enabled")
            self.streaming_inference_stop_button.configure(state="disabled")
        else:
            self.state_2_streaming = 1


    def streaming_inference_reset_button_event(self):
        self.streaming_source_scrollable_frame.destroy()
        self.streaming_source_scrollable_frame = customtkinter.CTkScrollableFrame( self.streaming_frame, label_text="En vivo seleccionado", height = 100, orientation= "horizontal", width=222)
        self.streaming_source_scrollable_frame.grid(row=1, column=1, padx=(0,60), pady=(20,0))
        self.streaming_select_source_folder_files = "Sin ingresar" #Default value
        self.streaming_source_scrollable_elements = customtkinter.CTkLabel(master = self.streaming_source_scrollable_frame, text = self.streaming_select_source_folder_files, anchor="center")
        self.streaming_source_scrollable_elements.grid(row=0, column=0, padx = (75,0))
        
        self.streaming_source_save_button_1 = customtkinter.CTkButton(self.streaming_frame, text="SELECCIONAR CARPETA \n DE GUARDADO", image=self.icon_download_files_image, compound="bottom", command= self.streaming_source_save_button_1_event, height=165)
        self.streaming_source_save_button_1.grid(row=3, column=0, rowspan = 2, padx=20, pady=(30,0))
        self.streaming_source_save_scrollable_frame = customtkinter.CTkScrollableFrame( self.streaming_frame, label_text="Carpeta seleccionada", height = 100, orientation= "horizontal", width=222)
        self.streaming_source_save_scrollable_frame.grid(row=3, column=1, rowspan = 2, padx=(0,50), pady=(30,0))
        self.streaming_select_folder = "Sin seleccionar" #Default value
        self.streaming_source_save_scrollable_folder = customtkinter.CTkLabel(master = self.streaming_source_save_scrollable_frame, text = self.streaming_select_folder, anchor = "w", compound="left")
        self.streaming_source_save_scrollable_folder.grid(row=0, column=0, padx=(65,0))

        self.state_2_streaming = 0
        self.state_1_streaming = 0
        self.streaming_inference_start_button.configure(state="disabled")
        self.streaming_inference_stop_button.configure(state="disabled")

    
    def streaming_inference_start_button_event(self):
        self.streaming_inference_start_button.configure(state="disabled")
        self.streaming_inference_stop_button.configure(state="enabled")
    
    
    def streaming_inference_stop_button_event(self):
        self.streaming_inference_start_button.configure(state="enabled")
        self.streaming_inference_stop_button.configure(state="disabled") 


if __name__ == "__main__":
    app = App()
    app.mainloop()
