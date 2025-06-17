import customtkinter as ctk

class GradeCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora de Notas")
        self.geometry("450x550")

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Calculadora de Nota Final", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # --- Frame para la cantidad de notas ---
        self.grades_count_frame = ctk.CTkFrame(self)
        self.grades_count_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.grades_count_frame.grid_columnconfigure(1, weight=1)

        self.grades_count_label = ctk.CTkLabel(self.grades_count_frame, text="Cantidad de notas:")
        self.grades_count_label.grid(row=0, column=0, padx=10, pady=10)

        self.grades_count_entry = ctk.CTkEntry(self.grades_count_frame, placeholder_text="Ej: 3")
        self.grades_count_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.generate_button = ctk.CTkButton(self.grades_count_frame, text="Generar Campos", command=self.generate_grade_fields)
        self.generate_button.grid(row=0, column=2, padx=10, pady=10)

        # --- Frame para las notas individuales (scrollable) ---
        self.grades_frame = ctk.CTkScrollableFrame(self, label_text="Notas y Porcentajes")
        self.grades_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        self.grid_rowconfigure(2, weight=1)
        self.grades_frame.grid_columnconfigure((1, 3), weight=1)

        self.grade_entries = []

        # --- Frame para el cálculo y resultado ---
        self.result_frame = ctk.CTkFrame(self)
        self.result_frame.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="ew")
        self.result_frame.grid_columnconfigure(0, weight=1)

        self.calculate_button = ctk.CTkButton(self.result_frame, text="Calcular Nota Necesaria", command=self.calculate_final_grade)
        self.calculate_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.result_label = ctk.CTkLabel(self.result_frame, text="", font=ctk.CTkFont(size=14), justify="left")
        self.result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def generate_grade_fields(self):
        # Limpiar campos anteriores
        for widget in self.grades_frame.winfo_children():
            widget.destroy()
        self.grade_entries = []
        self.result_label.configure(text="")

        try:
            num_grades = int(self.grades_count_entry.get())
            if not (0 < num_grades < 20):
                self.result_label.configure(text="Error: Ingrese un número de notas entre 1 y 19.", text_color="orange")
                return
        except (ValueError, TypeError):
            self.result_label.configure(text="Error: Ingrese un número válido.", text_color="orange")
            return
        
        # Crear nuevos campos
        for i in range(num_grades):
            grade_label = ctk.CTkLabel(self.grades_frame, text=f"Nota {i+1}:")
            grade_label.grid(row=i, column=0, padx=(10,5), pady=5, sticky="w")
            
            grade_entry = ctk.CTkEntry(self.grades_frame, placeholder_text="1.0-7.0")
            grade_entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            
            weight_label = ctk.CTkLabel(self.grades_frame, text=f"Peso %:")
            weight_label.grid(row=i, column=2, padx=(10,5), pady=5, sticky="w")

            weight_entry = ctk.CTkEntry(self.grades_frame, placeholder_text="Ej: 30")
            weight_entry.grid(row=i, column=3, padx=5, pady=5, sticky="ew")
            
            self.grade_entries.append((grade_entry, weight_entry))

    def calculate_final_grade(self):
        nota_obtenida = []
        peso_de_la_nota = []

        if not self.grade_entries:
            self.result_label.configure(text="Error: Genere los campos de notas primero.", text_color="orange")
            return

        try:
            for i, (grade_entry, weight_entry) in enumerate(self.grade_entries):
                nota_str = grade_entry.get()
                peso_str = weight_entry.get()
                if not nota_str or not peso_str:
                    self.result_label.configure(text=f"Error: Rellene todos los campos (fila {i+1}).", text_color="orange")
                    return

                nota = float(nota_str)
                peso = float(peso_str)
                
                if not (1.0 <= nota <= 7.0):
                     self.result_label.configure(text=f"Error: La nota {i+1} debe estar entre 1.0 y 7.0", text_color="orange")
                     return
                
                if not (0 < peso <= 100):
                    self.result_label.configure(text=f"Error: El peso {i+1} debe ser > 0 y <= 100", text_color="orange")
                    return

                nota_obtenida.append(nota)
                peso_de_la_nota.append(peso)

        except (ValueError, TypeError):
            self.result_label.configure(text="Error: Ingrese valores numéricos válidos.", text_color="orange")
            return

        total_weight = sum(peso_de_la_nota)
        if total_weight > 100:
            self.result_label.configure(text=f"Error: El peso total ({total_weight}%) supera el 100%.", text_color="orange")
            return

        peso_faltante = 100 - total_weight
        nota_minima_aprobacion = 4.0
        nota_ponderada_actual = sum(n * (p / 100) for n, p in zip(nota_obtenida, peso_de_la_nota))

        if peso_faltante <= 0:
            resultado_final = "Ya se ha evaluado el 100% del curso.\n"
            resultado_final += f"Tu nota final es: {nota_ponderada_actual:.2f}"
            color = "green" if nota_ponderada_actual >= nota_minima_aprobacion else "red"
            self.result_label.configure(text=resultado_final, text_color=color)
            return

        nota_necesaria = (nota_minima_aprobacion - nota_ponderada_actual) * 100 / peso_faltante
        
        summary_text = (f"Nota ponderada actual: {nota_ponderada_actual:.2f}\n"
                        f"Peso del examen final: {peso_faltante}%")

        if nota_necesaria > 7.0:
            result_text = f"Necesitas un {nota_necesaria:.2f}. ¡Es imposible aprobar!"
            color = "red"
        elif nota_necesaria <= 1.0:
            result_text = f"¡Ya aprobaste! Necesitas un 1.0 en el examen."
            color = "green"
        else:
            result_text = f"Necesitas un {nota_necesaria:.2f} en el examen final."
            # Usa el color por defecto del tema
            color = ctk.ThemeManager.theme["CTkLabel"]["text_color"]


        self.result_label.configure(text=f"{summary_text}\n\n{result_text}", text_color=color)


if __name__ == "__main__":
    app = GradeCalculator()
    app.mainloop()


