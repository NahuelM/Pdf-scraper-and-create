import tabula as tb
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import re
import pathlib
import os


def crearReporte(files_raw, destin_path):


    files = []


    for j in range(0, len(files_raw)):
        if(pathlib.Path(files_raw[j]).suffix == '.pdf'):
            files.append(files_raw[j])
            
    #AVANCE FISICO
    table_obra_1_mes = []
    table_obra_1_porcentaje = []
    table_obra_1_porcentaje_acum = []

    table_obra_1_economia_pesos = []
    table_obra_1_economia_pesos_of = []
    table_obra_1_economia_dolar = []
    table_obra_1_economia_euro = []
    for i in range(0, len(files)):
        df_obra1 = tb.read_pdf(f''+files[i], pages = '2', area = (530, 0, 740, 650), columns = [230, 280, 320, 370, 430, 490], pandas_options = {'header': None}, stream = True)[0]
        df_obra1['border'] = df_obra1.apply(lambda x: 1 if re.findall('^[A-Z].*[a-z]$', str(x[0])) else 0, axis = 1)
        df_obra1['row'] = df_obra1['border'].transform('cumsum')
        table_obra_1_mes.append(df_obra1[3])
        table_obra_1_porcentaje.append(df_obra1[5])
        table_obra_1_porcentaje_acum.append(df_obra1[6])
        
        
        df_obra1_economico = tb.read_pdf(files[i], pages = '2', area = (350, 0, 480, 650), columns = [330, 390, 445, 490], pandas_options = {'header': None}, stream = True)[0]
        df_obra1_economico['border'] = df_obra1_economico.apply(lambda x: 1 if re.findall('^[A-Z].*[a-z]$', str(x[0])) else 0, axis = 1)
        df_obra1_economico['row'] = df_obra1_economico['border'].transform('cumsum')
        table_obra_1_economia_pesos.append(df_obra1_economico[1])
        table_obra_1_economia_dolar.append(df_obra1_economico[2])
        table_obra_1_economia_euro.append(df_obra1_economico[3])
        table_obra_1_economia_pesos_of.append(df_obra1_economico[4])
        
    yarray_col1 = []
    yarray_col2 = []
    yarray_col3 = []
    yarray_col4 = []
    y_conexiones_cons = []
    y_calzada = []
    y_calzada2 = []
    y_sec_rec = []
    y_sendas_nuevas = []
    y_canales = []
    acum_col_1 = 0
    acum_col_2 = 0
    acum_col_3 = 0
    acum_col_4 = 0
    acum_conexiones = 0
    acum_calzada = 0
    acum_sec_rec = 0
    acum_sendas_nuevas = 0
    acum_canales = 0
    acum_calzada2 = 0
    xarray_mes = []

    for i in range(0, len(files)):
        xarray_mes.append(files[i].split('_')[1].split('.')[0])
        
    df = pd.DataFrame(
        {
            'mes' : [],
            'col_01' : [],
            'col_02' : [],
            'conexiones_cons' : [],
            'col_03' : [],
            'col_04' : [],
            'calzada': [],
            'sec_rec': [],
            'canales': [],
            'sendas_nuevas':[],
            'calzada2': []
        })


    y_col1_porcentaje_mes = []
    y_col2_porcentaje_mes = []
    y_conexiones_porcentaje_mes = []
    y_col3_porcentaje_mes = []
    y_col4_porcentaje_mes = []
    y_calzada_porcentaje_mes = []
    y_sec_rec_porcentaje_mes = []
    y_canales_porcentaje_mes = []
    y_sendas_porcentaje_mes = []
    y_calzada2_porcentaje_mes = []

    df_ob1_porcentajes = pd.DataFrame(
        {
            'col_01' : [],
            'col_02' : [],
            'conexiones_cons' : [],
            'col_03' : [],
            'col_04' : [],
            'calzada': [],
            'sec_rec': [],
            'canales': [],
            'sendas_nuevas':[],
            'calzada2': []  
        })



    y_acum_col_1_porcentaje = []
    y_acum_col_2_porcentaje = []
    y_acum_conexiones_porcentaje = []
    y_acum_col_3_porcentaje = []
    y_acum_col_4_porcentaje = []
    y_acum_calzada_porcentaje = []
    y_acum_sec_rec_porcentaje = []
    y_acum_canales_porcentaje = []
    y_acum_sendas_porcentaje = []
    y_acum_calzada2_porcentaje = []
    df_ob1_porcentajes_acum = pd.DataFrame(
        {
            'col_01' : [],
            'col_02' : [],
            'conexiones_cons' : [],
            'col_03' : [],
            'col_04' : [],
            'calzada': [],
            'sec_rec': [],
            'canales': [],
            'sendas_nuevas':[],
            'calzada2': []  
        })

    y_acum_proy_ejec = []
    y_acum_rubro_gen = []
    y_acum_red_san = []
    y_acum_red_pluv = []
    y_acum_lag_bergeiro =[]
    y_acum_imprevisto = []
    y_acum_ampliacion = []
    y_acum_imp_ampliacion = []
    df_ob1_economia = pd.DataFrame({
        'proy_ejec': [],
        'rubro_gen': [],
        'red_san': [],
        'red_pluv': [],
        'lag_bergeiro': [],
        'imprevistos': [],
        'ampliacion': [],
        'imp_ampliacion': [],
        'total_pesos': [],
        'total_euro': [],
        'total_dolar': [],
        'total_pesos_of': []
    })


    for i in range(0, len(table_obra_1_mes)):
        acum_col_1 += int(table_obra_1_mes[i][2])
        acum_col_2 += int(table_obra_1_mes[i][3])  
        acum_conexiones += int(table_obra_1_mes[i][6])
        #acum_calzada2 += int(table_obra_1[i][4])
        acum_col_3 += int(table_obra_1_mes[i][9])
        acum_col_4 += int(table_obra_1_mes[i][10])
        acum_sec_rec += int(table_obra_1_mes[i][11])
        acum_calzada += int(re.sub(r"\s+", "", str(table_obra_1_mes[i][14]).split('.')[0])) #elimina espacios en blanco
        acum_canales += int(table_obra_1_mes[i][12])
        acum_sendas_nuevas += int(table_obra_1_mes[i][15])
        yarray_col1.append(acum_col_1)
        yarray_col2.append(acum_col_2)
        yarray_col3.append(acum_col_3)
        y_conexiones_cons.append(acum_conexiones)
        yarray_col4.append(acum_col_4)
        y_calzada.append(acum_calzada)
        y_sec_rec.append(acum_sec_rec)
        y_sendas_nuevas.append(acum_sendas_nuevas)
        y_canales.append(acum_canales)
        y_calzada2.append(acum_calzada2)
        
        y_col1_porcentaje_mes.append(int(str(table_obra_1_porcentaje[i][2]).split('%')[0]))
        y_col2_porcentaje_mes.append(int(str(table_obra_1_porcentaje[i][3]).split('%')[0]))
        y_conexiones_porcentaje_mes.append(int(str(table_obra_1_porcentaje[i][6]).split('%')[0]))
        y_col3_porcentaje_mes.append(int(str(table_obra_1_porcentaje[i][9]).split('%')[0]))
        y_col4_porcentaje_mes.append(int(str(table_obra_1_porcentaje[i][10]).split('%')[0]))
        y_sec_rec_porcentaje_mes.append(int(str(table_obra_1_porcentaje[i][11]).split('%')[0]))
        y_calzada_porcentaje_mes.append(int(str(table_obra_1_porcentaje[i][14]).split('%')[0]))
        y_canales_porcentaje_mes.append(int(str(table_obra_1_porcentaje[i][12]).split('%')[0]))
        y_sendas_porcentaje_mes.append(int(str(table_obra_1_porcentaje[i][15]).split('%')[0]))
        y_calzada2_porcentaje_mes.append(int(str(table_obra_1_porcentaje[i][5]).split('%')[0]))
        
        y_acum_col_1_porcentaje.append(int(str(table_obra_1_porcentaje_acum[i][2]).split('%')[0]))
        y_acum_col_2_porcentaje.append(int(str(table_obra_1_porcentaje_acum[i][3]).split('%')[0]))
        y_acum_conexiones_porcentaje.append(int(str(table_obra_1_porcentaje_acum[i][6]).split('%')[0]))
        y_acum_col_3_porcentaje.append(int(str(table_obra_1_porcentaje_acum[i][9]).split('%')[0]))
        y_acum_col_4_porcentaje.append(int(str(table_obra_1_porcentaje_acum[i][10]).split('%')[0]))
        y_acum_sec_rec_porcentaje.append(int(str(table_obra_1_porcentaje_acum[i][11]).split('%')[0]))
        y_acum_canales_porcentaje.append(int(str(table_obra_1_porcentaje_acum[i][12]).split('%')[0]))
        y_acum_calzada_porcentaje.append(int(str(table_obra_1_porcentaje_acum[i][14]).split('%')[0]))
        y_acum_sendas_porcentaje.append(int(str(table_obra_1_porcentaje_acum[i][15]).split('%')[0]))
        y_acum_calzada2_porcentaje.append(int(str(table_obra_1_porcentaje_acum[i][5]).split('%')[0]))
        
    
    df['mes'] = xarray_mes
    df['col_01'] = yarray_col1
    df['col_02'] = yarray_col2
    df['conexiones_cons'] = y_conexiones_cons
    df['col_03'] = yarray_col3
    df['col_04'] = yarray_col4
    df['calzada'] = y_calzada
    df['sec_rec'] = y_sec_rec
    df['canales'] = y_canales
    df['sendas_nuevas'] = y_sendas_nuevas
    df['calzada2'] = y_calzada2


    df_ob1_porcentajes['col_01'] = y_col1_porcentaje_mes
    df_ob1_porcentajes['col_02'] = y_col2_porcentaje_mes
    df_ob1_porcentajes['conexiones_cons'] = y_conexiones_porcentaje_mes
    df_ob1_porcentajes['col_03'] = y_col3_porcentaje_mes
    df_ob1_porcentajes['col_04'] = y_col4_porcentaje_mes
    df_ob1_porcentajes['calzada'] = y_calzada_porcentaje_mes
    df_ob1_porcentajes['sec_rec'] = y_sec_rec_porcentaje_mes
    df_ob1_porcentajes['canales'] = y_canales_porcentaje_mes
    df_ob1_porcentajes['sendas_nuevas'] = y_sendas_porcentaje_mes
    df_ob1_porcentajes['calzada2'] = y_calzada2_porcentaje_mes



    df_ob1_porcentajes_acum['col_01'] = y_acum_col_1_porcentaje
    df_ob1_porcentajes_acum['col_02'] = y_acum_col_2_porcentaje
    df_ob1_porcentajes_acum['conexiones_cons'] = y_acum_conexiones_porcentaje
    df_ob1_porcentajes_acum['col_03'] = y_acum_col_3_porcentaje
    df_ob1_porcentajes_acum['col_04'] = y_acum_col_4_porcentaje
    df_ob1_porcentajes_acum['calzada'] = y_acum_calzada_porcentaje
    df_ob1_porcentajes_acum['sec_rec'] = y_acum_sec_rec_porcentaje
    df_ob1_porcentajes_acum['canales'] = y_acum_canales_porcentaje
    df_ob1_porcentajes_acum['sendas_nuevas'] = y_acum_sendas_porcentaje
    df_ob1_porcentajes_acum['calzada2'] = y_acum_calzada2_porcentaje


    exist = os.path.exists(destin_path+'/Charts')
    if not exist:
        os.mkdir(destin_path+'/Charts')

    #RED DE SANEAMIENTO
    plt.plot(xarray_mes, yarray_col1, marker = 'o')
    plt.plot(xarray_mes, yarray_col2, marker = 'o')
    plt.plot(xarray_mes, y_conexiones_cons, marker = 'o')
    plt.plot(xarray_mes, y_calzada2, marker = 'o')
    plt.legend(['colector 200-250mm', 'colector 300-800mm', 'conexiones construidas unidades', 'conexiones habilitadas unidades', 'calzada'])
    plt.title("Grafica")
    plt.savefig(destin_path+'/Charts/example_chart.png', transparent = False,  facecolor = 'white', bbox_inches = "tight")

    #RED DE PLUVIALES
    plt.cla()
    plt.plot(xarray_mes, yarray_col3, marker = 'o')
    plt.plot(xarray_mes, yarray_col4, marker = 'o')
    plt.plot(xarray_mes, y_calzada, marker = 'o')
    plt.plot(xarray_mes, y_sec_rec, marker = 'o')
    plt.plot(xarray_mes, y_canales, marker = 'o')
    plt.plot(xarray_mes, y_sendas_nuevas, marker = 'o')
    plt.legend(['colector 500-800mm', 'colecotres >= 1000mm', 'calzada', 'sec_rec', 'canales', 'sendas'])

    plt.savefig(destin_path+'/Charts/example_chart2.png', transparent=False, facecolor='white', bbox_inches="tight")

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
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(w = 0, h = 20, txt = "OBRA: Redes de saneamiento y drenaje pluvial para el barrio Manga", ln=1)
    pdf.set_font('Arial', '', 12)
    pdf.cell(w = w, h = ch, txt = "Red de saneamiento", ln = 0)
    pdf.ln(ch)
    pdf.image(destin_path+'/Charts/example_chart.png', x = 10, y = None, w = 100, h = 0, type = 'PNG', link = '')
    pdf.ln(ch)
    pdf.ln(ch)
    
    
    # Table Header
    pdf.set_font('Arial', 'B', 7)
    pdf.cell(w = w, h = ch, txt = 'fecha', border = 1, ln = 0, align = 'C')
    pdf.cell(w = w, h = ch, txt = 'colectores 200-250mm', border = 1, ln = 0, align = 'C')
    pdf.cell(w = w, h = ch, txt = 'colectores 300-800mm', border = 1, ln = 0, align = 'C')
    pdf.cell(w = w, h = ch, txt = 'conexiones cons', border = 1, ln = 0, align = 'C')
    pdf.cell(w = w, h = ch, txt = 'calzada', border = 1, ln = 1, align = 'C')

    pdf.cell(w = w, h = ch, txt = '', border = 1, ln = 0, align = 'C')
    for i in range(4):
        aux = 0 if i < 3 else 1
        pdf.cell(w = w/3, h = ch, txt = 'mes', border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = '%', border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = 'acum', border = 1, ln = aux, align = 'C')
        
    # Table contents
    pdf.set_font('Arial', '', 8)
    for i in range(0, len(df)):
        pdf.cell(w = w, h = ch, txt = df['mes'].iloc[i], border = 1, ln = 0, align = 'C')
        
        pdf.cell(w = w/3, h = ch, txt = df['col_01'].iloc[i].astype(str), border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes['col_01'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes_acum['col_01'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        
        pdf.cell(w = w/3, h = ch, txt = df['col_02'].iloc[i].astype(str), border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes['col_02'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes_acum['col_02'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        
        
        pdf.cell(w = w/3, h = ch, txt = df['conexiones_cons'].iloc[i].astype(str), border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes['conexiones_cons'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes_acum['conexiones_cons'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        
        pdf.cell(w = w/3, h = ch, txt = df['calzada2'].iloc[i].astype(str), border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes['calzada2'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes_acum['calzada2'].iloc[i].astype(str) + '%', border = 1, ln = 1, align = 'C')
    
    
    pdf.ln(w/2)
    pdf.set_font('Arial', '', 12)
    pdf.cell(w = w, h = ch, txt = "Avance economico ", ln = 1)
        # Table Header
    pdf.ln(ch/2)
    pdf.set_font('Arial', 'B', 7)
    pdf.cell(w = w, h = ch, txt = 'fecha', border = 1, ln = 0, align = 'C')
    pdf.cell(w = w, h = ch, txt = 'miles pesos', border = 1, ln = 0, align = 'C')
    pdf.cell(w = w, h = ch, txt = 'miles euros', border = 1, ln = 0, align = 'C')
    pdf.cell(w = w, h = ch, txt = 'miles dolares', border = 1, ln = 0, align = 'C')
    pdf.cell(w = w, h = ch, txt = 'miles pesos Of', border = 1, ln = 1, align = 'C')

    # for i in range(4):
    #     aux = 0 if i < 3 else 1
    #     pdf.cell(w = w/3, h = ch, txt = 'mes', border = 1, ln = 0, align = 'C')
    #     pdf.cell(w = w/3, h = ch, txt = '%', border = 1, ln = 0, align = 'C')
    #     pdf.cell(w = w/3, h = ch, txt = 'acum', border = 1, ln = aux, align = 'C')


    # Table contents
    pdf.set_font('Arial', '', 8)
    for i in range(0, len(df)):
        pdf.cell(w = w, h = ch, txt = df['mes'].iloc[i], border = 1, ln = 0, align = 'C')
        
        pdf.cell(w = w, h = ch, txt = str(table_obra_1_economia_pesos[i][12]), border = 1, ln = 0, align = 'C')
        pdf.cell(w = w, h = ch, txt = str(table_obra_1_economia_euro[i][12]), border = 1, ln = 0, align = 'C')
        pdf.cell(w = w, h = ch, txt = str(table_obra_1_economia_dolar[i][12]), border = 1, ln = 0, align = 'C')
        pdf.cell(w = w, h = ch, txt = str(table_obra_1_economia_pesos_of[i][12]), border = 1, ln = 1, align = 'C')

        

    pdf.ln(ch)
    pdf.ln(ch)

    pdf.set_font('Arial', '', 12)
    pdf.ln(ch)
    pdf.cell(w = w, h = ch, txt = "Red de pluviales", ln = 1)
    pdf.ln(ch)
    pdf.image(destin_path+'/Charts/example_chart2.png', x = 10, y = None, w = 100, h = 0, type = 'PNG', link = '')
    pdf.ln(ch)
    pdf.ln(ch)


    # Table Header
    pdf.set_font('Arial', 'B', 7)
    pdf.cell(w = w, h = ch, txt = 'fecha', border = 1, ln = 0, align = 'C')
    pdf.cell(w = w, h = ch, txt = 'colecotres 500-800 mm', border = 1, ln = 0, align = 'C')
    pdf.cell(w = w, h = ch, txt = 'colecotres >= 1000 mm', border = 1, ln = 0, align = 'C')
    pdf.cell(w = w, h = ch, txt = 'calzada', border = 1, ln = 0, align = 'C')
    pdf.cell(w = w, h = ch, txt = 'Sec_rectangulares', border = 1, ln = 0, align = 'C')
    pdf.cell(w = w, h = ch, txt = 'canales', border = 1, ln = 0, align = 'C')
    pdf.cell(w = w, h = ch, txt = 'sendas', border = 1, ln = 1, align = 'C')

    pdf.cell(w = w, h = ch, txt = '', border = 1, ln = 0, align = 'C')
    for i in range(6):
        aux = 0 if i < 5 else 1
        pdf.cell(w = w/3, h = ch, txt = 'mes', border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = '%', border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = 'acum', border = 1, ln = aux, align = 'C')


    # Table contents
    pdf.set_font('Arial', '', 8)
    for i in range(0, len(df)):
        pdf.cell(w = w, h = ch, txt = df['mes'].iloc[i], border = 1, ln = 0, align = 'C')
        
        pdf.cell(w = w/3, h = ch, txt = df['col_03'].iloc[i].astype(str), border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes['col_03'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes_acum['col_03'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        
        pdf.cell(w = w/3, h = ch, txt = df['col_04'].iloc[i].astype(str), border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes['col_04'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes_acum['col_04'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        
        pdf.cell(w = w/3, h = ch, txt = df['calzada'].iloc[i].astype(str), border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes['calzada'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes_acum['calzada'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        
        pdf.cell(w = w/3, h = ch, txt = df['sec_rec'].iloc[i].astype(str), border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes['sec_rec'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes_acum['sec_rec'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        
        pdf.cell(w = w/3, h = ch, txt = df['canales'].iloc[i].astype(str), border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes['canales'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes_acum['canales'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        
        
        pdf.cell(w = w/3, h = ch, txt = df['sendas_nuevas'].iloc[i].astype(str), border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes['sendas_nuevas'].iloc[i].astype(str) + '%', border = 1, ln = 0, align = 'C')
        pdf.cell(w = w/3, h = ch, txt = df_ob1_porcentajes_acum['sendas_nuevas'].iloc[i].astype(str) + '%', border = 1, ln = 1, align = 'C')
    pdf.ln(ch)

    p = destin_path + './Reporte.pdf'
    pdf.output(f''+p, 'F')




    #pyuic5 -x test.ui -o test.py
    #pyinstaller --onefile -w -i "icon.ico" test.py


    #AVANCE ECONOMICO