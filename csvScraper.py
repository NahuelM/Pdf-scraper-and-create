
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os
from os import remove
# filename = 'Data.csv'
# data = pd.read_csv(filename, header=0)
def generarReporte(path, path_destino):
    dir_path = path
    # files_raw = os.listdir(dir_path)

    # files = []


    # for j in range(0, len(files_raw)):
    #     if(pathlib.Path(files_raw[j]).suffix == '.csv'):
    #         files.append(files_raw[j])
            

    #data = pd.read_excel(, header=0, sheet_name='Hoja2')
    #data = pd.read_csv(dir_path + '/' + files[0], encoding='utf-8')
    

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
    for i in range(1, data.shape[0]):
        r = data.iloc[i].iloc[21]
        if not pd.isna(r):
            best_match = process.extractOne(r, [origen_de_fondos[0] for origen_de_fondos in origen_de_fondos], scorer = fuzz.ratio)
            if best_match is not None and best_match[1] >= threshold:
                index = [origen_de_fondos[0] for origen_de_fondos in origen_de_fondos].index(best_match[0])
                origen_de_fondos[index] = (origen_de_fondos[index][0], origen_de_fondos[index][1] + 1)
            else:
                origen_de_fondos.append((r, 1))

                

        r = data.iloc[i].iloc[22]
        if not pd.isna(r):
            r_lower = r.lower().split(' ')[0].strip()
            best_match = process.extractOne(r_lower, [empresa[0] for empresa in empresas], scorer = fuzz.ratio)
            if best_match is not None and best_match[1] >= threshold:
                index = [empresa[0] for empresa in empresas].index(best_match[0])
                empresas[index] = (empresas[index][0], empresas[index][1] + 1)
            else:
                empresas.append((r_lower.upper(), 1))

                

        r = data.iloc[i].iloc[24]
        if(not pd.isna(r)):
            try:
                index = next(index for index, tupla in enumerate(contraparte_imm) if tupla[0] == r)
                contraparte_imm[index] = (contraparte_imm[index][0], contraparte_imm[index][1] + 1)
            except StopIteration:
                contraparte_imm.append((r, 1))
                
        threshold = 80

        r = data.iloc[i].iloc[37]
        if not pd.isna(r):
            best_match = process.extractOne(r, [obras_finalizadas[0] for obras_finalizadas in obras_finalizadas], scorer = fuzz.ratio)
            if best_match is not None and best_match[1] >= threshold:
                index = [obras_finalizadas[0] for obras_finalizadas in obras_finalizadas].index(best_match[0])
                obras_finalizadas[index] = (obras_finalizadas[index][0], obras_finalizadas[index][1] + 1)
            else:
                obras_finalizadas.append((r, 1))



        r = data.iloc[i].iloc[39]
        if(not pd.isna(r)):
            metraje_saneamiento += float(str(r).lower().split('m')[0].replace(',', '.'))
        
        
        r = data.iloc[i].iloc[41]
        if(not pd.isna(r)):
            colectores_pluviales += float(str(r).lower().split('m')[0].replace(',', '.'))
            

        r = data.iloc[i].iloc[43]
        if(not pd.isna(r)):
            conexiones += int(str(r).lower().split('u')[0].strip())
            

        r = data.iloc[i].iloc[45]
        if(not pd.isna(r)):
            camaras += int(str(r).lower().split('u')[0].strip())


        r = data.iloc[i].iloc[49]
        if(not pd.isna(r)):
            impulsion += float(str(r).lower().split('m')[0].replace(',', '.'))
            

        r = data.iloc[i].iloc[51]
        if(not pd.isna(r)):
            bocas_de_tormenta += int(str(r).lower().split('u')[0].strip())
            

        r = data.iloc[i].iloc[53]
        if(not pd.isna(r)):
            reguera += int(str(r).lower().split('u')[0].strip())
            

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
            
            
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(w = w, h = ch, txt = 'Origenes de fondos', ln = 1)
    pdf.set_font('Arial', '', 8)
    for i in range(0, len(origen_de_fondos)):
        pdf.cell(w = w, h = ch, txt = str(origen_de_fondos[i]), ln = 1)
    
    strings = [item[0] for item in origen_de_fondos]
    numeros = [item[1] for item in origen_de_fondos]
    fig, ax = plt.subplots()
    ax.barh(y=strings, width=numeros, align='center')
    exist = os.path.exists(path_destino+'/Charts')
    if not exist:
        os.mkdir(path_destino+'/Charts')
        
    plt.savefig(path_destino+'/Charts/example_pie3.png', transparent=False, facecolor='white', bbox_inches="tight")
    pdf.image(path_destino+'/Charts/example_pie3.png', x = 10, y = None, w = 100, h = 0, type = 'PNG', link = '')
    
    
    pdf.set_font('Arial', 'B', 10)
    pdf.ln(ch*2)    
    pdf.cell(w = w, h = ch, txt = 'Contraparte imm', ln = 1)
    pdf.set_font('Arial', '', 8)
    for i in range(0, len(contraparte_imm)):
        pdf.cell(w = w, h = ch, txt = str(contraparte_imm[i]), ln = 1)
    
    strings = [item[0] for item in contraparte_imm]
    numeros = [item[1] for item in contraparte_imm]
    fig, ax = plt.subplots()
    ax.barh(y=strings, width=numeros, align='center')
    plt.savefig(path_destino+'/Charts/example_pie4.png', transparent=False, facecolor='white', bbox_inches="tight")
    pdf.image(path_destino+'/Charts/example_pie4.png', x = 10, y = None, w = 100, h = 0, type = 'PNG', link = '')
    
    pdf.set_font('Arial', 'B', 10)
    pdf.ln(ch*2)
    pdf.cell(w = w, h = ch, txt = 'Empresas', ln = 1)
    pdf.set_font('Arial', '', 8)
    for i in range(0, len(empresas)):
        pdf.cell(w = w, h = ch, txt = str(empresas[i]), ln = 1)

    strings = [item[0] for item in empresas]
    numeros = [item[1] for item in empresas]
    fig, ax = plt.subplots()
    ax.barh(y=strings, width=numeros, align='center')
    plt.savefig(path_destino+'/Charts/example_pie.png', transparent=False, facecolor='white', bbox_inches="tight")
    pdf.image(path_destino+'/Charts/example_pie.png', x = 10, y = None, w = 100, h = 0, type = 'PNG', link = '')
    
    
    
    pdf.set_font('Arial', 'B', 10)
    pdf.ln(ch*2)
    pdf.cell(w = w, h = ch, txt = 'Obras finalizadas', ln = 1)
    pdf.set_font('Arial', '', 8)
    for i in range(0, len(obras_finalizadas)):
        pdf.cell(w = w, h = ch, txt = str(obras_finalizadas[i]), ln = 1)
    
    strings = [item[0] for item in obras_finalizadas]
    numeros = [item[1] for item in obras_finalizadas]
    fig, ax = plt.subplots()
    ax.barh(y=strings, width=numeros, align='center')
    plt.savefig(path_destino+'/Charts/example_pie2.png', transparent=False, facecolor='white', bbox_inches="tight")
    pdf.image(path_destino+'/Charts/example_pie2.png', x = 10, y = None, w = 100, h = 0, type = 'PNG', link = '')
    
    pdf.set_font('Arial', 'B', 10)
    pdf.ln(ch*2)
    pdf.cell(w = w, h = ch, txt = 'Datos', ln = 1)
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