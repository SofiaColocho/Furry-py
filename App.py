import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, ROW
 
background_color = "#F2FFF0"
main_button_color = "#E0B6FF"
register_button_color = "#F5E642"
alert_button_color = "#C6B6FF"
 
usuarios = {
    "admin": {"password": "1234", "email": "admin@furrylove.com"}
}
 
perros = [
    {
        "nombre": "Lola",
        "raza": "Labrador",
        "edad": "2 años",
        "refugio": "Refugio Esperanza",
        "descripcion": "Lola es una perra alegre y juguetona. Le encanta correr y jugar con niños. Busca una familia amorosa.",
        "imagen": "resources/lola.jpg"
    },
    {
        "nombre": "Rex",
        "raza": "Pastor Alemán",
        "edad": "4 años",
        "refugio": "Milagro de Amor",
        "descripcion": "Rex es leal y protector. Muy inteligente y fácil de entrenar. Ideal para familias activas.",
        "imagen": "resources/rex.jpg"
    },
    {
        "nombre": "Café",
        "raza": "Mestizo",
        "edad": "1 año",
        "refugio": "Refugio Esperanza",
        "descripcion": "Café llegó siendo cachorro. Es curioso, travieso y lleno de energía. Le encanta explorar.",
        "imagen": "resources/cafe.jpg"
    },
    {
        "nombre": "Rocky",
        "raza": "Bulldog",
        "edad": "3 años",
        "refugio": "Patitas Felices",
        "descripcion": "Rocky es tranquilo y cariñoso. Le gusta dormir y recibir mimos. Perfecto para apartamentos.",
        "imagen": "resources/rocky.jpg"
    },
    {
        "nombre": "Luna",
        "raza": "Husky",
        "edad": "2 años",
        "refugio": "Milagro de Amor",
        "descripcion": "Luna es hermosa y enérgica. Necesita espacio para correr y mucho cariño.",
        "imagen": "resources/luna.jpg"
    },
    {
        "nombre": "Toby",
        "raza": "Beagle",
        "edad": "5 años",
        "refugio": "Patitas Felices",
        "descripcion": "Toby es dulce y tranquilo. Ya mayor, busca un hogar donde pueda descansar y ser querido.",
        "imagen": "resources/toby.jpg"
    },
]
 
gatos = [
    {
        "nombre": "Tom",
        "raza": "Siamés",
        "edad": "3 años",
        "refugio": "Refugio Esperanza",
        "descripcion": "Tom es curioso y juguetón. Le encanta explorar cada rincón de la casa y hacer travesuras."
    },
    {
        "nombre": "Tito",
        "raza": "Mestizo",
        "edad": "1 año",
        "refugio": "Patitas Felices",
        "descripcion": "Tito es un gatito joven lleno de energía. Le encanta jugar y es muy cariñoso con las personas."
    },
    {
        "nombre": "Tigra",
        "raza": "Atigrado",
        "edad": "2 años",
        "refugio": "Milagro de Amor",
        "descripcion": "Tigra es independiente pero muy leal. Una vez que te gana la confianza, nunca te abandona."
    },
    {
        "nombre": "Simba",
        "raza": "Persa",
        "edad": "4 años",
        "refugio": "Refugio Esperanza",
        "descripcion": "Simba es majestuoso y tranquilo. Le gusta estar en lugares cómodos y recibir caricias."
    },
    {
        "nombre": "Salem",
        "raza": "Negro puro",
        "edad": "3 años",
        "refugio": "Patitas Felices",
        "descripcion": "Salem es misterioso y elegante. Es muy inteligente y se adapta fácilmente a nuevos hogares."
    },
    {
        "nombre": "Mía",
        "raza": "Angora",
        "edad": "2 años",
        "refugio": "Milagro de Amor",
        "descripcion": "Mía es dulce y delicada. Le encanta que la cepillen y pasar tiempo con su familia."
    },
    {
        "nombre": "Michi",
        "raza": "Mestizo",
        "edad": "1 año",
        "refugio": "Refugio Esperanza",
        "descripcion": "Michi es travieso y divertido. Siempre encuentra la manera de hacerte reír con sus ocurrencias."
    },
    {
        "nombre": "Nube",
        "raza": "Blanco puro",
        "edad": "5 años",
        "refugio": "Patitas Felices",
        "descripcion": "Nube es suave y tranquila como su nombre. Perfecta para hogares tranquilos que buscan compañía."
    },
]
 
refugios = [
    {
        "nombre": "Milagro de Amor",
        "direccion": "Calle 5, San Salvador",
        "telefono": "7777-1111",
        "descripcion": "Refugio dedicado al rescate y adopción de perros y gatos desde 2010. Más de 500 animales adoptados."
    },
    {
        "nombre": "Échame una Pata",
        "direccion": "Avenida 12, Santa Ana",
        "telefono": "7777-2222",
        "descripcion": "Organización sin fines de lucro que rescata animales en situación de calle y los prepara para adopción."
    },
    {
        "nombre": "Casa Roly",
        "direccion": "Colonia Escalón, San Salvador",
        "telefono": "7777-3333",
        "descripcion": "Refugio familiar con espacio para más de 80 animales. Especializado en rehabilitación de mascotas maltratadas."
    },
    {
        "nombre": "El Campito",
        "direccion": "Km 25, Carretera a Sonsonate",
        "telefono": "7777-4444",
        "descripcion": "Amplio refugio rural con espacio para perros grandes. Buscan familias con jardín para sus peludos."
    },
    {
        "nombre": "Refugio Felino Cat Shelter",
        "direccion": "Colonia San Benito, San Salvador",
        "telefono": "7777-5555",
        "descripcion": "Refugio exclusivo para gatos. Tienen más de 60 gatitos esperando un hogar lleno de amor."
    },
]
 
productos = [
    {
        "nombre": "Cama para gato",
        "precio": "30",
        "categoria": "Descanso",
        "descripcion": "Cama suave y acogedora ideal para gatos. Tamaño mediano, fácil de lavar.",
        "disponible": True
    },
    {
        "nombre": "Pelotas para perro",
        "precio": "$2",
        "categoria": "Juguetes",
        "descripcion": "Set de 3 pelotas resistentes de goma para perros. Ideales para jugar en exteriores.",
        "disponible": True
    },
    {
        "nombre": "Collar para gato",
        "precio": "$5",
        "categoria": "Accesorios",
        "descripcion": "Collar ajustable con cascabel para gatos. Disponible en varios colores.",
        "disponible": True
    },
    {
        "nombre": "Collar para perro",
        "precio": "$5.50",
        "categoria": "Accesorios",
        "descripcion": "Collar resistente de nylon para perros medianos. Con hebilla de seguridad.",
        "disponible": True
    },
    {
        "nombre": "Traje de dinosaurio",
        "precio": "$15",
        "categoria": "Ropa",
        "descripcion": "Divertido disfraz de dinosaurio para perros pequeños. Perfecto para Halloween.",
        "disponible": True
    },
    {
        "nombre": "Peluches para gato",
        "precio": "$7.80",
        "categoria": "Juguetes",
        "descripcion": "Set de peluches con catnip para gatos. Estimula el juego natural del gato.",
        "disponible": True
    },
    {
        "nombre": "Plato para perro",
        "precio": "$7.50",
        "categoria": "Alimentación",
        "descripcion": "Plato antideslizante de acero inoxidable para perros. Fácil de limpiar.",
        "disponible": True
    },
    {
        "nombre": "Comida para perro",
        "precio": "$4.95",
        "categoria": "Alimentación",
        "descripcion": "Alimento balanceado para perros adultos. Bolsa de 1kg con vitaminas y minerales.",
        "disponible": True
    },
    {
        "nombre": "Traje de banana",
        "precio": "$7.00",
        "categoria": "Ropa",
        "descripcion": "Gracioso disfraz de banana para perros pequeños. Muy suave y cómodo.",
        "disponible": True
    },
    {
        "nombre": "Suéter para perro",
        "precio": "$7.00",
        "categoria": "Ropa",
        "descripcion": "Suéter tejido abrigador para perros pequeños y medianos. Ideal para el frío.",
        "disponible": True
    },
    {
        "nombre": "Camisas para perro",
        "precio": "$5.00",
        "categoria": "Ropa",
        "descripcion": "Camisa de algodón transpirable para perros. Disponible en tallas XS, S y M.",
        "disponible": True
    },
    {
        "nombre": "Comida para gato",
        "precio": "$8.00",
        "categoria": "Alimentación",
        "descripcion": "Alimento premium para gatos adultos. Bolsa de 1kg con taurina y omega 3.",
        "disponible": True
    },
    {
        "nombre": "Comida para gato",
        "precio": "$8.00",
        "categoria": "Alimentación",
        "descripcion": "Alimento premium para gatos adultos. Bolsa de 1kg con taurina y omega 3.",
        "disponible": True
    },
    {
        "nombre": "Comida para gato",
        "precio": "$8.00",
        "categoria": "Alimentación",
        "descripcion": "Alimento premium para gatos adultos. Bolsa de 1kg con taurina y omega 3.",
        "disponible": True
    },
]
 
 
class FurryLoveApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.mostrar_bienvenida()
        self.main_window.show()
 
    def cargar_imagen(self, ruta):
        try:
            ruta_completa = self.paths.app / ruta
            return toga.Image(ruta_completa)
        except Exception as e:
            print(f"Error cargando imagen {ruta}: {e}")
            return None
 
    # ──────────────── BIENVENIDA ────────────────
    def mostrar_bienvenida(self):
        titulo = toga.Label(
            "🐾 FurryLove",
            style=Pack(font_size=28, text_align=CENTER, padding_bottom=10)
        )
        subtitulo = toga.Label(
            "Tu app de mascotas favorita",
            style=Pack(font_size=14, text_align=CENTER, padding_bottom=30)
        )
        btn_ingresar = toga.Button(
            "Get started",
            on_press=self.ir_a_opciones,
            style=Pack(flex=1, font_size=20, padding=10, background_color=main_button_color)
        )
        layout = toga.Box(
            children=[titulo, subtitulo, btn_ingresar],
            style=Pack(direction=COLUMN, padding=40, gap=20, background_color=background_color, flex=1)
        )
        self.main_window.content = layout
 
    # ──────────────── OPCIONES (login/registro) ────────────────
    def mostrar_opciones(self):
        titulo = toga.Label(
            "🐾 FurryLove",
            style=Pack(font_size=28, text_align=CENTER, padding_bottom=20)
        )
        btn_login = toga.Button(
            "Iniciar sesión",
            on_press=self.ir_a_login,
            style=Pack(flex=1, font_size=20, padding=10, background_color=main_button_color)
        )
        btn_registro = toga.Button(
            "Registrarse",
            on_press=self.ir_a_registro,
            style=Pack(flex=1, font_size=20, padding=10, background_color=register_button_color)
        )
        layout = toga.Box(
            children=[titulo, btn_login, btn_registro],
            style=Pack(direction=COLUMN, padding=40, gap=20, background_color=background_color, flex=1)
        )
        self.main_window.content = layout
 
    def ir_a_opciones(self, widget):
        self.mostrar_opciones()
 
    def ir_a_login(self, widget):
        self.mostrar_login()
 
    def ir_a_registro(self, widget):
        self.mostrar_registro()
 
    # ──────────────── LOGIN ────────────────
    def mostrar_login(self):
        titulo = toga.Label(
            "Iniciar sesión",
            style=Pack(font_size=26, text_align=CENTER, padding_bottom=10)
        )
        self.input_usuario = toga.TextInput(
            placeholder="Usuario",
            style=Pack(font_size=18, padding=5, flex=1)
        )
        self.input_clave = toga.PasswordInput(
            placeholder="Contraseña",
            style=Pack(font_size=18, padding=5, flex=1)
        )
        btn_ingresar = toga.Button(
            "Iniciar sesión",
            on_press=self.validar_login,
            style=Pack(font_size=20, padding=10, background_color=main_button_color)
        )
        btn_volver = toga.Button(
            "Volver",
            on_press=self.volver_a_opciones,
            style=Pack(font_size=16, padding=10, background_color=alert_button_color)
        )
        layout = toga.Box(
            children=[titulo, self.input_usuario, self.input_clave, btn_ingresar, btn_volver],
            style=Pack(direction=COLUMN, padding=40, gap=15, background_color=background_color, flex=1)
        )
        self.main_window.content = layout
 
    def validar_login(self, widget):
        user = self.input_usuario.value.strip()
        pwd = self.input_clave.value.strip()
        if user in usuarios and usuarios[user]["password"] == pwd:
            self.mostrar_menu_principal(user)
        else:
            self.main_window.error_dialog("Error", "Usuario o contraseña incorrectos.")
 
    def volver_a_opciones(self, widget):
        self.mostrar_opciones()
 
    # ──────────────── REGISTRO ────────────────
    def mostrar_registro(self):
        titulo = toga.Label(
            "Crear cuenta",
            style=Pack(font_size=26, text_align=CENTER, padding_bottom=10)
        )
        self.reg_usuario = toga.TextInput(
            placeholder="Nombre de usuario",
            style=Pack(font_size=18, padding=5, flex=1)
        )
        self.reg_email = toga.TextInput(
            placeholder="Correo electrónico",
            style=Pack(font_size=18, padding=5, flex=1)
        )
        self.reg_clave = toga.PasswordInput(
            placeholder="Contraseña",
            style=Pack(font_size=18, padding=5, flex=1)
        )
        self.reg_clave2 = toga.PasswordInput(
            placeholder="Confirmar contraseña",
            style=Pack(font_size=18, padding=5, flex=1)
        )
        btn_registrar = toga.Button(
            "REGISTRARSE",
            on_press=self.guardar_registro,
            style=Pack(font_size=20, padding=10, background_color=register_button_color)
        )
        btn_volver = toga.Button(
            "Volver",
            on_press=self.volver_a_opciones,
            style=Pack(font_size=16, padding=10, background_color=alert_button_color)
        )
        layout = toga.Box(
            children=[titulo, self.reg_usuario, self.reg_email, self.reg_clave, self.reg_clave2, btn_registrar, btn_volver],
            style=Pack(direction=COLUMN, padding=40, gap=15, background_color=background_color, flex=1)
        )
        self.main_window.content = layout
 
    def guardar_registro(self, widget):
        user = self.reg_usuario.value.strip()
        email = self.reg_email.value.strip()
        pwd = self.reg_clave.value.strip()
        pwd2 = self.reg_clave2.value.strip()
 
        if not user or not email or not pwd or not pwd2:
            self.main_window.error_dialog("Error", "Por favor completa todos los campos.")
            return
        if user in usuarios:
            self.main_window.error_dialog("Error", "Ese nombre de usuario ya existe.")
            return
        if "@" not in email or "." not in email:
            self.main_window.error_dialog("Error", "Ingresa un correo electrónico válido.")
            return
        if len(pwd) < 4:
            self.main_window.error_dialog("Error", "La contraseña debe tener al menos 4 caracteres.")
            return
        if pwd != pwd2:
            self.main_window.error_dialog("Error", "Las contraseñas no coinciden.")
            return
 
        usuarios[user] = {"password": pwd, "email": email}
        self.main_window.info_dialog("¡Éxito!", f"Cuenta creada para {user}. ¡Bienvenido! 🐾")
        self.mostrar_menu_principal(user)
 
    # ──────────────── MENÚ PRINCIPAL ────────────────
    def mostrar_menu_principal(self, user):
        self.usuario_actual = user
        saludo = toga.Label(
            f"¡Bienvenido, {user}! 🐾",
            style=Pack(font_size=24, text_align=CENTER, padding_bottom=5)
        )
        descripcion = toga.Label(
            "¿Qué deseas ver hoy?",
            style=Pack(font_size=16, text_align=CENTER, padding_bottom=10)
        )
        btn_perros = toga.Button(
            "🐶 Perros",
            on_press=self.ir_a_perros,
            style=Pack(font_size=18, padding=10, background_color=main_button_color)
        )
        btn_gatos = toga.Button(
            "🐱 Gatos",
            on_press=self.ir_a_gatos,
            style=Pack(font_size=18, padding=10, background_color=main_button_color)
        )
        btn_refugios = toga.Button(
            "🏠 Refugios",
            on_press=self.ir_a_refugios,
            style=Pack(font_size=18, padding=10, background_color=main_button_color)
        )
        btn_furryshop = toga.Button(
            "🛍️ FurryShop",
            on_press=self.ir_a_furryshop,
            style=Pack(font_size=18, padding=10, background_color=main_button_color)
        )
        btn_salir = toga.Button(
            "Cerrar sesión",
            on_press=self.volver_a_opciones,
            style=Pack(font_size=16, padding=10, background_color=alert_button_color)
        )
        layout = toga.Box(
            children=[saludo, descripcion, btn_perros, btn_gatos, btn_refugios, btn_furryshop, btn_salir],
            style=Pack(direction=COLUMN, padding=40, gap=15, background_color=background_color, flex=1)
        )
        self.main_window.content = layout
 
    # ──────────────── PERROS ────────────────
    def ir_a_perros(self, widget):
        self.mostrar_lista_perros()
 
    def mostrar_lista_perros(self):
        titulo = toga.Label(
            "🐶 Perros en adopción",
            style=Pack(font_size=22, text_align=CENTER, padding_bottom=10)
        )
        lista = toga.Box(style=Pack(direction=COLUMN, gap=10))
        for perro in perros:
            def ver_detalle(widget, p=perro):
                self.mostrar_detalle_perro(p)
            btn = toga.Button(
                f"🐶 {perro['nombre']}  |  {perro['raza']}  |  {perro['edad']}",
                on_press=ver_detalle,
                style=Pack(font_size=15, padding=12, background_color="#FFFFFF")
            )
            lista.add(btn)
        btn_volver = toga.Button(
            "← Volver",
            on_press=lambda w: self.mostrar_menu_principal(self.usuario_actual),
            style=Pack(font_size=16, padding=10, background_color=alert_button_color)
        )
        contenido = toga.Box(
            children=[titulo, lista, btn_volver],
            style=Pack(direction=COLUMN, padding=20, gap=10, background_color=background_color)
        )
        scroll = toga.ScrollContainer(content=contenido, style=Pack(flex=1))
        self.main_window.content = scroll
 
    def mostrar_detalle_perro(self, perro):
        children = []
 
        img = self.cargar_imagen(perro["imagen"])
        if img:
            img_view = toga.ImageView(img, style=Pack(width=200, height=200, padding_bottom=15))
            children.append(img_view)
 
        children += [
            toga.Label(perro["nombre"], style=Pack(font_size=28, padding_bottom=2)),
            toga.Label(perro["raza"], style=Pack(font_size=16, padding_bottom=5)),
            toga.Label(f"🕐 {perro['edad']}", style=Pack(font_size=15, padding_bottom=5)),
            toga.Label(f"📍 {perro['refugio']}", style=Pack(font_size=14, padding_bottom=15)),
            toga.Label("Sobre él", style=Pack(font_size=18, padding_bottom=5)),
            toga.Label(perro["descripcion"], style=Pack(font_size=14, padding_bottom=20)),
            toga.Button(
                "🐾 ADOPTAR",
                on_press=lambda w: self.main_window.info_dialog(
                    "¡Gracias!", f"Pronto nos pondremos en contacto contigo sobre {perro['nombre']}. 🐾"
                ),
                style=Pack(font_size=20, padding=15, background_color=register_button_color)
            ),
            toga.Button(
                "← Volver",
                on_press=lambda w: self.mostrar_lista_perros(),
                style=Pack(font_size=15, padding=10, background_color=alert_button_color)
            ),
        ]
 
        layout = toga.Box(
            children=children,
            style=Pack(direction=COLUMN, padding=30, gap=5, background_color=background_color, flex=1)
        )
        scroll = toga.ScrollContainer(content=layout, style=Pack(flex=1))
        self.main_window.content = scroll
 
    # ──────────────── GATOS ────────────────
    def ir_a_gatos(self, widget):
        self.mostrar_lista_gatos()
 
    def mostrar_lista_gatos(self):
        titulo = toga.Label(
            "🐱 Gatos en adopción",
            style=Pack(font_size=22, text_align=CENTER, padding_bottom=10)
        )
        lista = toga.Box(style=Pack(direction=COLUMN, gap=10))
        for gato in gatos:
            def ver_detalle(widget, g=gato):
                self.mostrar_detalle_gato(g)
            btn = toga.Button(
                f"🐱 {gato['nombre']}  |  {gato['raza']}  |  {gato['edad']}",
                on_press=ver_detalle,
                style=Pack(font_size=15, padding=12, background_color="#FFFFFF")
            )
            lista.add(btn)
        btn_volver = toga.Button(
            "← Volver",
            on_press=lambda w: self.mostrar_menu_principal(self.usuario_actual),
            style=Pack(font_size=16, padding=10, background_color=alert_button_color)
        )
        contenido = toga.Box(
            children=[titulo, lista, btn_volver],
            style=Pack(direction=COLUMN, padding=20, gap=10, background_color=background_color)
        )
        scroll = toga.ScrollContainer(content=contenido, style=Pack(flex=1))
        self.main_window.content = scroll
 
    def mostrar_detalle_gato(self, gato):
        nombre = toga.Label(gato["nombre"], style=Pack(font_size=28, padding_bottom=2))
        raza = toga.Label(gato["raza"], style=Pack(font_size=16, padding_bottom=5))
        edad = toga.Label(f"🕐 {gato['edad']}", style=Pack(font_size=15, padding_bottom=5))
        refugio = toga.Label(f"📍 {gato['refugio']}", style=Pack(font_size=14, padding_bottom=15))
        titulo_sobre = toga.Label("Sobre él", style=Pack(font_size=18, padding_bottom=5))
        descripcion = toga.Label(gato["descripcion"], style=Pack(font_size=14, padding_bottom=20))
        btn_adoptar = toga.Button(
            "🐾 ADOPTAR",
            on_press=lambda w: self.main_window.info_dialog(
                "¡Gracias!", f"Pronto nos pondremos en contacto contigo sobre {gato['nombre']}. 🐾"
            ),
            style=Pack(font_size=20, padding=15, background_color=register_button_color)
        )
        btn_volver = toga.Button(
            "← Volver",
            on_press=lambda w: self.mostrar_lista_gatos(),
            style=Pack(font_size=15, padding=10, background_color=alert_button_color)
        )
        layout = toga.Box(
            children=[nombre, raza, edad, refugio, titulo_sobre, descripcion, btn_adoptar, btn_volver],
            style=Pack(direction=COLUMN, padding=30, gap=5, background_color=background_color, flex=1)
        )
        scroll = toga.ScrollContainer(content=layout, style=Pack(flex=1))
        self.main_window.content = scroll
 
    # ──────────────── REFUGIOS ────────────────
    def ir_a_refugios(self, widget):
        self.mostrar_lista_refugios()
 
    def mostrar_lista_refugios(self):
        titulo = toga.Label(
            "🏠 Refugios",
            style=Pack(font_size=22, text_align=CENTER, padding_bottom=10)
        )
        lista = toga.Box(style=Pack(direction=COLUMN, gap=10))
        for refugio in refugios:
            def ver_detalle(widget, r=refugio):
                self.mostrar_detalle_refugio(r)
            btn = toga.Button(
                f"🏠 {refugio['nombre']}",
                on_press=ver_detalle,
                style=Pack(font_size=15, padding=12, background_color="#FFFFFF")
            )
            lista.add(btn)
        btn_volver = toga.Button(
            "← Volver",
            on_press=lambda w: self.mostrar_menu_principal(self.usuario_actual),
            style=Pack(font_size=16, padding=10, background_color=alert_button_color)
        )
        contenido = toga.Box(
            children=[titulo, lista, btn_volver],
            style=Pack(direction=COLUMN, padding=20, gap=10, background_color=background_color)
        )
        scroll = toga.ScrollContainer(content=contenido, style=Pack(flex=1))
        self.main_window.content = scroll
 
    def mostrar_detalle_refugio(self, refugio):
        nombre = toga.Label(refugio["nombre"], style=Pack(font_size=24, padding_bottom=5))
        direccion = toga.Label(f"📍 {refugio['direccion']}", style=Pack(font_size=14, padding_bottom=5))
        telefono = toga.Label(f"📞 {refugio['telefono']}", style=Pack(font_size=14, padding_bottom=10))
        titulo_sobre = toga.Label("Sobre el refugio", style=Pack(font_size=18, padding_bottom=5))
        descripcion = toga.Label(refugio["descripcion"], style=Pack(font_size=14, padding_bottom=20))
        btn_contactar = toga.Button(
            "📞 CONTACTAR",
            on_press=lambda w: self.main_window.info_dialog(
                "Contacto", f"Llama al {refugio['telefono']} para más información sobre {refugio['nombre']}. 🐾"
            ),
            style=Pack(font_size=20, padding=15, background_color=register_button_color)
        )
        btn_volver = toga.Button(
            "← Volver",
            on_press=lambda w: self.mostrar_lista_refugios(),
            style=Pack(font_size=15, padding=10, background_color=alert_button_color)
        )
        layout = toga.Box(
            children=[nombre, direccion, telefono, titulo_sobre, descripcion, btn_contactar, btn_volver],
            style=Pack(direction=COLUMN, padding=30, gap=5, background_color=background_color, flex=1)
        )
        scroll = toga.ScrollContainer(content=layout, style=Pack(flex=1))
        self.main_window.content = scroll
 
    # ──────────────── FURRYSHOP ────────────────
    def ir_a_furryshop(self, widget):
        self.mostrar_furryshop()
 
    def mostrar_furryshop(self):
        titulo = toga.Label(
            "🛍️ FurryShop",
            style=Pack(font_size=22, text_align=CENTER, padding_bottom=5)
        )
        subtitulo = toga.Label(
            "Todo para tu mascota 🐾",
            style=Pack(font_size=14, text_align=CENTER, padding_bottom=15)
        )
        lista = toga.Box(style=Pack(direction=COLUMN, gap=8))
        for producto in productos:
            def ver_producto(widget, p=producto):
                self.mostrar_detalle_producto(p)
            emoji = "🛍️"
            if producto["categoria"] == "Juguetes":
                emoji = "🎾"
            elif producto["categoria"] == "Ropa":
                emoji = "👕"
            elif producto["categoria"] == "Alimentación":
                emoji = "🍖"
            elif producto["categoria"] == "Descanso":
                emoji = "🛏️"
            elif producto["categoria"] == "Accesorios":
                emoji = "🏷️"
            fila = toga.Button(
                f"{emoji} {producto['nombre']}  —  {producto['precio']}  |  {producto['categoria']}",
                on_press=ver_producto,
                style=Pack(font_size=14, padding=12, background_color="#FFFFFF")
            )
            lista.add(fila)
        btn_volver = toga.Button(
            "← Volver",
            on_press=lambda w: self.mostrar_menu_principal(self.usuario_actual),
            style=Pack(font_size=16, padding=10, background_color=alert_button_color)
        )
        contenido = toga.Box(
            children=[titulo, subtitulo, lista, btn_volver],
            style=Pack(direction=COLUMN, padding=20, gap=8, background_color=background_color)
        )
        scroll = toga.ScrollContainer(content=contenido, style=Pack(flex=1))
        self.main_window.content = scroll
 
    def mostrar_detalle_producto(self, producto):
        emoji = "🛍️"
        if producto["categoria"] == "Juguetes":
            emoji = "🎾"
        elif producto["categoria"] == "Ropa":
            emoji = "👕"
        elif producto["categoria"] == "Alimentación":
            emoji = "🍖"
        elif producto["categoria"] == "Descanso":
            emoji = "🛏️"
        elif producto["categoria"] == "Accesorios":
            emoji = "🏷️"
        nombre = toga.Label(f"{emoji} {producto['nombre']}", style=Pack(font_size=24, padding_bottom=5))
        precio = toga.Label(f"💲 {producto['precio']}", style=Pack(font_size=20, padding_bottom=5))
        categoria = toga.Label(f"📦 Categoría: {producto['categoria']}", style=Pack(font_size=14, padding_bottom=10))
        disponible = toga.Label(
            "✅ Disponible" if producto["disponible"] else "❌ Agotado",
            style=Pack(font_size=14, padding_bottom=15)
        )
        titulo_desc = toga.Label("Descripción", style=Pack(font_size=18, padding_bottom=5))
        descripcion = toga.Label(producto["descripcion"], style=Pack(font_size=14, padding_bottom=20))
        btn_comprar = toga.Button(
            "🛒 COMPRAR",
            on_press=lambda w: self.main_window.info_dialog(
                "¡Gracias!", f"Tu pedido de '{producto['nombre']}' por {producto['precio']} fue registrado. 🐾"
            ),
            style=Pack(font_size=20, padding=15, background_color=register_button_color)
        )
        btn_volver = toga.Button(
            "← Volver",
            on_press=lambda w: self.mostrar_furryshop(),
            style=Pack(font_size=15, padding=10, background_color=alert_button_color)
        )
        layout = toga.Box(
            children=[nombre, precio, categoria, disponible, titulo_desc, descripcion, btn_comprar, btn_volver],
            style=Pack(direction=COLUMN, padding=30, gap=5, background_color=background_color, flex=1)
        )
        scroll = toga.ScrollContainer(content=layout, style=Pack(flex=1))
        self.main_window.content = scroll
 
 
def main():
    return FurryLoveApp("furryLove", "org.beeware.furrylove")