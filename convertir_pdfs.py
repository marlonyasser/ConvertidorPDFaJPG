import os
import pymupdf as fitz  # PyMuPDF (versión nueva, alias fitz)

# --- TUS RUTAS EXACTAS ---
carpeta_entrada = r"C:\Users\INFOUNI\Downloads\sistemas\PDFs_Entrada"
carpeta_salida = r"C:\Users\INFOUNI\Downloads\sistemas\PDFs_Convertidos"

# 1. Crear las carpetas si no existen
os.makedirs(carpeta_entrada, exist_ok=True)
os.makedirs(carpeta_salida, exist_ok=True)

# 2. Buscar todos los PDFs
pdfs = [f for f in os.listdir(carpeta_entrada) if f.lower().endswith('.pdf')]

if not pdfs:
    print("⚠ No se encontraron PDFs en la carpeta de entrada.")
else:
    print(f"📄 Se encontraron {len(pdfs)} PDF(s). Iniciando conversión...\n")
    
    # 3. Procesar cada PDF
    for archivo in pdfs:
        nombre_base = os.path.splitext(archivo)[0]
        ruta_pdf = os.path.join(carpeta_entrada, archivo)
        
        # Crear carpeta para este PDF
        carpeta_destino = os.path.join(carpeta_salida, nombre_base)
        os.makedirs(carpeta_destino, exist_ok=True)
        
        print(f"→ Convirtiendo: {archivo}")
        
        # Abrir el PDF
        documento = fitz.open(ruta_pdf)
        
        # Recorrer cada página y guardarla como JPG
        for num_pagina in range(len(documento)):
            pagina = documento.load_page(num_pagina)
            imagen = pagina.get_pixmap(dpi=150)
            
            nombre_imagen = f"{nombre_base}_{num_pagina + 1}.jpg"
            ruta_imagen = os.path.join(carpeta_destino, nombre_imagen)
            
            imagen.save(ruta_imagen)
            print(f"   ✓ {nombre_imagen}")
            
        documento.close()

    print(f"\n✅ ¡Listo! Archivos guardados en: {carpeta_salida}")