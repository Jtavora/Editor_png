import os
from PIL import ImageFont, ImageDraw, Image  

pessoas = []
DIRETORIO = 'certificados/'

def remover_antigos():
    for i in os.listdir(DIRETORIO):
        if i != '.gitignore':
            os.remove(os.path.join(DIRETORIO, i))

def gerar_certificado(dados):
    print(f'Gerando pdf...')
    image = Image.open("Model.png")  
    draw = ImageDraw.Draw(image)  

    #NOME DO ALUNO
    font_size = 70 
    font = ImageFont.load_default()
    font = font.font_variant(size=font_size)  # Ajusta o tamanho da fonte
    y_position = 990  # Ajusta a coordenada y para subir o texto
    draw.text((450, y_position), nome.strip(), font=font, fill=(0, 0, 0, 255))

    #NOME DO COORDENADOR
    font_size = 50  # Tamanho da fonte
    font = ImageFont.load_default()
    font = font.font_variant(size=font_size)  # Ajusta o tamanho da fonte
    y_position = 1425  # Ajusta a coordenada y para subir o texto
    x_position = 1130
    draw.text((x_position, y_position), "Cord. Eduardo", font=font, fill=(0, 0, 0, 255))

    #NOME DO PROFESSOR
    font_size = 50  # Tamanho da fonte
    font = ImageFont.load_default()
    font = font.font_variant(size=font_size)  # Ajusta o tamanho da fonte
    y_position = 1425  # Ajusta a coordenada y para subir o texto
    x_position = 540
    draw.text((x_position, y_position), "Prof. Eduardo", font=font, fill=(0, 0, 0, 255))

    #DIA
    font_size = 40  # Tamanho da fonte
    font = ImageFont.load_default()
    font = font.font_variant(size=font_size)  # Ajusta o tamanho da fonte
    y_position = 1141 # Ajusta a coordenada y para subir o texto
    x_position = 1130
    draw.text((x_position, y_position), "30/09/2003", font=font, fill=(0, 0, 0, 255))

    #CURSO
    font_size = 100
    font = ImageFont.load_default()
    font = font.font_variant(size=font_size)  # Ajusta o tamanho da fonte
    y_position = 750  # Ajusta a coordenada y para subir o texto
    x_position = 625
    draw.text((x_position, y_position), "Introducao a computacao", font=font, fill=(0, 0, 0, 255))

    #SALVE PDF
    image.save(os.path.join(DIRETORIO, f"{nome.strip()}.png"))
