
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os
from os import remove
# filename = 'Data.csv'
# data = pd.read_csv(filename, header=0)
lista_errores = []
def generarReporte(path, path_destino):
    #region PDF scraping  
    dir_path = path

    try:
        data = pd.read_csv(dir_path, encoding = 'utf-8', on_bad_lines = 'skip')
        print("El archivo se ha leído correctamente con el encoding:", 'utf-8')
    except UnicodeDecodeError:
        print("Error al intentar leer el archivo con el encoding:", 'utf-8')
        read_file = pd.read_excel (r'' + dir_path, sheet_name = 'Hoja2')
        read_file.to_csv(r'./temp//prueba.csv', encoding = 'utf-8', index = None, header = True)
        data = pd.read_csv('./temp//prueba.csv', encoding = 'utf-8', on_bad_lines = 'skip')

    origen_de_fondos = [] #
    contraparte_imm = [] #
    empresas = [] #  
    obras_finalizadas = [] #
    metraje_saneamiento = 0 #
    colectores_pluviales = 0 #
    conexiones = 0 #
    camaras = 0 #
    impulsion = 0 #
    bocas_de_tormenta = 0 #
    reguera = 0 #
    elementos_suds = 0 #
    reparacion_boca_tormenta = 0 # 
    reparacion_colector = 0 #
    reparacion_conexion_nueva = 0
    reparacion_conexion_rota = 0
    reparacion_registro_roto = 0
    desobstruccion_colector = 0
    desobstruccion_conexion = 0

    threshold = 80  # Umbral para considerar una coincidencia aceptable (ajusta según tus necesidades)
    try:
        for i in range(1, data.shape[0]):
            #O_Origen de Fondos
            #Busca la columna por indice, sino lo encuentra busca la columna por nombre
            r = data.iloc[i].iloc[21] 
            if(pd.isna(r)):
                r = data.iloc[i].loc['O_Origen de Fondos']
            
            if not pd.isna(r):
                best_match = process.extractOne(r, [origen_de_fondos[0] for origen_de_fondos in origen_de_fondos], scorer = fuzz.ratio)
                if best_match is not None and best_match[1] >= threshold:
                    index = [origen_de_fondos[0] for origen_de_fondos in origen_de_fondos].index(best_match[0])
                    origen_de_fondos[index] = (origen_de_fondos[index][0], origen_de_fondos[index][1] + 1)
                else:
                    origen_de_fondos.append((r, 1))
                
                    
            #O_Empresa contratada
            r = data.iloc[i].iloc[22]
            if not pd.isna(r):
                r_lower = r.lower().split(' ')[0].strip()
                best_match = process.extractOne(r_lower, [empresa[0] for empresa in empresas], scorer = fuzz.ratio)
                if best_match is not None and best_match[1] >= threshold:
                    index = [empresa[0] for empresa in empresas].index(best_match[0])
                    empresas[index] = (empresas[index][0], empresas[index][1] + 1)
                else:
                    empresas.append((r_lower.upper(), 1))

                    
            #O_Contraparte_IM
            r = data.iloc[i].iloc[24]
            if(not pd.isna(r)):
                try:
                    index = next(index for index, tupla in enumerate(contraparte_imm) if tupla[0] == r)
                    contraparte_imm[index] = (contraparte_imm[index][0], contraparte_imm[index][1] + 1)
                except StopIteration:
                    contraparte_imm.append((r, 1))
                    
            threshold = 80

            #O_Estado de la obra
            r = data.iloc[i].iloc[37]
            if not pd.isna(r):
                best_match = process.extractOne(r, [obras_finalizadas[0] for obras_finalizadas in obras_finalizadas], scorer = fuzz.ratio)
                if best_match is not None and best_match[1] >= threshold:
                    index = [obras_finalizadas[0] for obras_finalizadas in obras_finalizadas].index(best_match[0])
                    obras_finalizadas[index] = (obras_finalizadas[index][0], obras_finalizadas[index][1] + 1)
                else:
                    obras_finalizadas.append((r, 1))


            #O_Colectores_saneamiento_acumulado_m
            r = data.iloc[i].iloc[39]
            if(not pd.isna(r)):
                metraje_saneamiento += float(str(r).lower().split('m')[0].replace(',', '.'))
            
            #O_Colectores_pluviales_acumulado_m
            r = data.iloc[i].iloc[41]
            if(not pd.isna(r)):
                colectores_pluviales += float(str(r).lower().split('m')[0].replace(',', '.'))
                
            #O_Conexiones_acumulado_u
            r = data.iloc[i].iloc[43]
            if(not pd.isna(r)):
                conexiones += int(str(r).lower().split('u')[0].strip())
                
            #O_Cámaras_acumulado_u
            r = data.iloc[i].iloc[45]
            if(not pd.isna(r)):
                camaras += int(str(r).lower().split('u')[0].strip())

            #O_Impulsión_acumulado_m
            r = data.iloc[i].iloc[49]
            if(not pd.isna(r)):
                impulsion += float(str(r).lower().split('m')[0].replace(',', '.'))
                
            #O_Bocas de tormenta_ acumulado_u
            r = data.iloc[i].iloc[51]
            if(not pd.isna(r)):
                bocas_de_tormenta += int(str(r).lower().split('u')[0].strip())
                
            #O_Reguera_acumulado_u
            r = data.iloc[i].iloc[53]
            if(not pd.isna(r)):
                reguera += int(str(r).lower().split('u')[0].strip())
                
            #O_Elementos SUDS_acumulado_u
            r = data.iloc[i].iloc[54]
            if(not pd.isna(r)):
                elementos_suds += int(str(r).lower().split('u')[0].strip())
                

            r = data.iloc[i].iloc[58]
            if(not pd.isna(r)):
                reparacion_boca_tormenta += int(str(r).lower().split('u')[0].strip())


            r = data.iloc[i].iloc[59]
            if(not pd.isna(r)):
                reparacion_colector += int(str(r).lower().split('u')[0].strip())
                

            r = data.iloc[i].iloc[60]
            if(not pd.isna(r)):
                reparacion_conexion_nueva += int(str(r).lower().split('u')[0].strip())
                

            r = data.iloc[i].iloc[61]
            if(not pd.isna(r)):
                reparacion_conexion_rota += int(str(r).lower().split('u')[0].strip())
                

            r = data.iloc[i].iloc[62]
            if(not pd.isna(r)):
                reparacion_registro_roto += int(str(r).lower().split('u')[0].strip())
                

            r = data.iloc[i].iloc[63]
            if(not pd.isna(r)):
                desobstruccion_colector += int(str(r).lower().split('u')[0].strip())
                

            r = data.iloc[i].iloc[64]
            if(not pd.isna(r)):
                desobstruccion_conexion += int(str(r).lower().split('u')[0].strip())
    
    except Exception as ex:
        print(str(ex))

    #endregion
    
    # cell height
    ch = 4
    w = 25
    class PDF(FPDF):
        def __init__(self):
            super().__init__()
        # def header(self):
        #     self.set_font('Arial', '', 12)
        #     self.cell(0, 8, 'Header', 0, 1, 'C')
        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', '', 12)
            self.cell(0, 8, f'Page {self.page_no()}', 0, 0, 'C')

        def create_table(self, headers, data, border:bool = 1, h_cell:int = 6):
            self.set_font('Arial', 'B', 12)
            for h in headers:
                self.cell(70, h_cell, h, border)
            self.ln()
            self.set_draw_color(25, 25, 25) #black line
            self.line(10, self.get_y(), 200 ,self.get_y()) #coordinate sequence: (x_start, y_start, x_end, y_end)
            self.set_font('Arial', '', 12)
            for row in data:
                self.cell(70, h_cell, str(row[0]), border)
                self.cell(60, h_cell, str(row[1]), border)
                self.ln()
    
    
    #region Creacion de pdf
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 14)
    fecha_csv = "2/6/2023"
    pdf.cell(w = w, h = ch, txt = "Reportes de obras fisicas " + str(fecha_csv))
    pdf.set_draw_color(0, 0, 0) #black line
    pdf.line(5, 16, 205 ,16) #coordinate sequence: (x_start, y_start, x_end, y_end)
    pdf.set_font('Arial', '', 10)
    pdf.ln(ch*2)
    pdf.cell(w = w, h = ch, txt = "Intendencia de Montevideo")
    pdf.ln(ch*1.2)
    pdf.cell(w = w, h = ch, txt = "Estudios y proyectos saneamiento")
    pdf.ln(ch*3)
    
    pdf.set_font('Arial', 'B', 12)
    pdf.line(5, pdf.get_y() - 2, 205 , pdf.get_y() - 2)
    pdf.cell(w = w, h = ch, txt = 'Origenes de fondos', ln = 1)
    pdf.line(5, pdf.get_y() + 2, 205 , pdf.get_y() + 2)
    pdf.ln(ch)
    pdf.set_font('Arial', '', 10)
    
    pdf.ln(ch*2)

    headers_tabla_1 = ["Nombre", "Cantidad"]
    data_tabla_1 = []


    
    
    pdf.line(5, pdf.get_y() + 2, 205 , pdf.get_y() + 2)
    pdf.ln(ch)
    pdf.ln(ch*2)
    for i in range(0, len(origen_de_fondos)):
        origen_array = str(origen_de_fondos[i]).split(',')
        #pdf.cell(w = w, h = ch, txt = str(origen_array[0]).split('(')[1].replace('\'', '') + " " + str(origen_array[1]).replace(')', ''), ln = 1)
        data_tabla_1.append([str(origen_array[0]).split('(')[1].replace('\'', ''), str(origen_array[1]).replace(')', '')])
        
    pdf.create_table(headers_tabla_1, data_tabla_1, False)
        
    pdf.line(5, pdf.get_y(), 205, pdf.get_y())
    pdf.ln(ch)
                
    strings = [item[0] for item in origen_de_fondos]
    numeros = [item[1] for item in origen_de_fondos]
    fig, ax = plt.subplots()
    ax.barh(y=strings, width=numeros, align = 'center')
    exist = os.path.exists(path_destino+'/Charts')
    if not exist:
        os.mkdir(path_destino+'/Charts')
        
    plt.savefig(path_destino+'/Charts/example_pie3.png', transparent=False, facecolor='white', bbox_inches="tight")
    pdf.image(path_destino+'/Charts/example_pie3.png', x = 10, y = None, w = 100, h = 0, type = 'PNG', link = '')
    
    
    pdf.add_page()
    
    pdf.set_font('Arial', 'B', 12)
    pdf.ln(ch*2)    
    pdf.line(5, pdf.get_y() - 2, 205 , pdf.get_y() - 2)
    pdf.cell(w = w, h = ch, txt = 'Contraparte imm', ln = 1)
    pdf.line(5, pdf.get_y() + 2, 205 , pdf.get_y() + 2)
    pdf.ln(ch)
    pdf.set_font('Arial', '', 8)
    
    headers_tabla_2 = ["Contrapartres", "Cantidad"]
    data_tabla_2 = []
    
    for i in range(0, len(contraparte_imm)):
        contraparte_array = str(contraparte_imm[i]).split(',')
        #pdf.cell(w = w, h = ch, txt = str(contraparte_array[0]).replace('(', '').replace(')', '').replace('\'', '') + str(contraparte_array[1]).replace(')', ''), ln = 1)
        data_tabla_2.append([str(contraparte_array[0]).replace('(', '').replace(')', '').replace('\'', ''), str(contraparte_array[1]).replace(')', '')])
    
    pdf.create_table(headers_tabla_2, data_tabla_2, False)
    
    strings = [item[0] for item in contraparte_imm]
    numeros = [item[1] for item in contraparte_imm]
    fig, ax = plt.subplots()
    ax.barh(y = strings, width = numeros, align = 'center')
    plt.savefig(path_destino + '/Charts/example_pie4.png', transparent = False, facecolor = 'white', bbox_inches = "tight")
    pdf.image(path_destino + '/Charts/example_pie4.png', x = 10, y = None, w = 100, h = 0, type = 'PNG', link = '')
    
    pdf.add_page()
    
    pdf.set_font('Arial', 'B', 12)
    pdf.ln(ch*2)
    pdf.line(5, pdf.get_y() - 2, 205 , pdf.get_y() - 2)
    pdf.cell(w = w, h = ch, txt = 'Empresas', ln = 1)
    pdf.line(5, pdf.get_y() + 2, 205 , pdf.get_y() + 2)
    pdf.ln(ch)
    pdf.set_font('Arial', '', 8)
    
    headers_tabla_3 = ["Empresas", "Cantidad"]
    data_tabla_3 = []
    
    for i in range(0, len(empresas)):
        empresas_array = str(empresas[i]).split(',') 
        #pdf.cell(w = w, h = ch, txt = str(empresas_array[0]).replace('(', '').replace(')', '').replace('\'', '') + str(empresas_array[1]).replace(')', ''), ln = 1)
        data_tabla_3.append([str(empresas_array[0]).replace('(', '').replace(')', '').replace('\'', ''), str(empresas_array[1]).replace(')', '')])

    pdf.create_table(headers_tabla_3, data_tabla_3, False)
    
    strings = [item[0] for item in empresas]
    numeros = [item[1] for item in empresas]
    fig, ax = plt.subplots()
    ax.barh(y = strings, width = numeros, align = 'center')
    plt.savefig(path_destino + '/Charts/example_pie.png', transparent = False, facecolor = 'white', bbox_inches = "tight")
    pdf.image(path_destino + '/Charts/example_pie.png', x = 10, y = None, w = 100, h = 0, type = 'PNG', link = '')
    
    pdf.add_page()

    pdf.set_font('Arial', 'B', 10)
    pdf.ln(ch*2)
    pdf.line(5, pdf.get_y() - 2, 205 ,pdf.get_y() - 2)
    pdf.cell(w = w, h = ch, txt = 'Obras finalizadas', ln = 1)
    pdf.line(5, pdf.get_y() + 2, 205 ,pdf.get_y() + 2)
    pdf.ln(ch)
    pdf.set_font('Arial', '', 8)
    
    headers_tabla_4 = ["Estado de obra", "Cantidad"]
    data_tabla_4 = []
    
    for i in range(0, len(obras_finalizadas)):
        obras_array = str(obras_finalizadas[i]).split(',')
        #pdf.cell(w = w, h = ch, txt = str(obras_array[0]).replace('(', '').replace(')', '').replace('\'', '')  + str(obras_array[1]).replace(')', ''), ln = 1)
        data_tabla_4.append([str(obras_array[0]).replace('(', '').replace(')', '').replace('\'', ''), str(obras_array[1]).replace(')', '')])
    
    pdf.create_table(headers_tabla_4, data_tabla_4, False)
    
    strings = [item[0] for item in obras_finalizadas]
    numeros = [item[1] for item in obras_finalizadas]
    fig, ax = plt.subplots()
    ax.barh(y=strings, width=numeros, align='center')
    plt.savefig(path_destino + '/Charts/example_pie2.png', transparent = False, facecolor = 'white', bbox_inches = "tight")
    pdf.image(path_destino + '/Charts/example_pie2.png', x = 10, y = None, w = 100, h = 0, type = 'PNG', link = '')
    
    pdf.add_page()
    
    pdf.set_font('Arial', 'B', 10)
    pdf.ln(ch*2)
    pdf.line(5, pdf.get_y() - 2, 205 ,pdf.get_y() - 2)
    pdf.cell(w = w, h = ch, txt = 'Datos', ln = 1)
    pdf.line(5, pdf.get_y() + 2, 205 ,pdf.get_y() + 2)
    pdf.ln(ch)
    pdf.set_font('Arial', '', 8)
    pdf.cell(w = w+15, h = ch, txt = 'Metraje saneamiento: ' + str(round(metraje_saneamiento, 2)) + 'm', ln = 1)
    pdf.cell(w = w+15, h = ch, txt = 'Colectores pluviales: ' + str(round(colectores_pluviales, 2)) + 'm', ln = 1)
    pdf.cell(w = w+15, h = ch, txt = 'Conexiones: ' + str(round(conexiones, 2)) + 'u', ln = 1)
    pdf.cell(w = w+15, h = ch, txt = 'Camaras: ' + str(round(camaras, 2)) + 'u', ln = 1)
    pdf.cell(w = w+15, h = ch, txt = 'Impulsion: ' + str(round(impulsion, 2)) + 'm', ln = 1)
    pdf.cell(w = w+15, h = ch, txt = 'Bocas de tormenta: ' + str(round(bocas_de_tormenta, 2)) + 'u', ln = 1)
    pdf.cell(w = w+15, h = ch, txt = 'Reguera: ' + str(round(reguera, 2)) + 'u', ln = 1)
    pdf.cell(w = w+15, h = ch, txt = 'Elementos suds: ' + str(round(elementos_suds, 2)) + 'u', ln = 1)
    pdf.cell(w = w+15, h = ch, txt = 'Reparacion colector: ' + str(round(reparacion_colector, 2)) + 'u', ln = 1)
    pdf.cell(w = w+15, h = ch, txt = 'Reparacion registro roto: ' + str(round(reparacion_registro_roto, 2)) + 'u', ln = 1)
    pdf.cell(w = w+15, h = ch, txt = 'Reparacion boca tormenta: ' + str(round(reparacion_boca_tormenta, 2)) + 'u', ln = 1)
    pdf.cell(w = w+15, h = ch, txt = 'Reparacion conexion nueva: ' + str(round(reparacion_conexion_nueva, 2)) + 'u', ln = 1)
    pdf.cell(w = w+15, h = ch, txt = 'Reparacion conexion rota: ' + str(round(reparacion_conexion_rota, 2)) + 'u', ln = 1)
    pdf.cell(w = w+15, h = ch, txt = 'Desobstruccion colector: ' + str(round(desobstruccion_colector, 2)) + 'u', ln = 1)
    pdf.cell(w = w+15, h = ch, txt = 'Desobstruccion conexion: ' + str(round(desobstruccion_conexion, 2)) + 'u', ln = 1)
    p = path_destino + './Reporte3.pdf'
    try:
        pdf.output(f''+p, 'F')
        print("EXITO reporte generado")
    except PermissionError as e:
        print("ERROR !!! " + str(e))
    
    remove('./temp/prueba.csv')
    #endregion