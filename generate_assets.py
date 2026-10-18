import os
import math
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = "/home/developer/.gemini/antigravity-ide/scratch/apps-femininos/app-contracoes-parto/store_assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

def get_font(size, bold=False):
    possible_fonts = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf" if bold else "/usr/share/fonts/truetype/freefont/FreeSans.ttf"
    ]
    for p in possible_fonts:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def draw_gradient(draw, width, height, color1, color2):
    for y in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * y / height)
        g = int(color1[1] + (color2[1] - color1[1]) * y / height)
        b = int(color1[2] + (color2[2] - color1[2]) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

def create_icon():
    img = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    bg = Image.new("RGB", (512, 512), (255, 255, 255))
    bg_draw = ImageDraw.Draw(bg)
    draw_gradient(bg_draw, 512, 512, (237, 100, 166), (184, 50, 128)) # Gentle maternal rose
    
    mask = Image.new("L", (512, 512), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, 512, 512], radius=110, fill=255)
    
    img = Image.composite(bg, Image.new("RGBA", (512, 512), (0,0,0,0)), mask)
    draw = ImageDraw.Draw(img)
    
    # Elegant contraction wave arc
    center = (256, 230)
    draw.arc([center[0]-140, center[1]-140, center[0]+140, center[1]+140], start=-140, end=40, fill=(255, 255, 255, 220), width=24)
    
    # Heart / baby kick wave curve in center
    points = [
        (160, 240), (210, 240), (235, 170), (256, 290), (277, 210), (300, 240), (350, 240)
    ]
    draw.line(points, fill=(255, 255, 255), width=18, joint="curve")
    
    f_sub = get_font(30, bold=True)
    text = "PARTOFÁCIL"
    tbox = draw.textbbox((0, 0), text, font=f_sub)
    draw.text((256 - (tbox[2]-tbox[0])//2, 360), text, fill=(255, 240, 248), font=f_sub)
    
    img.save(os.path.join(ASSETS_DIR, "icon-512.png"))
    print("Icon generated.")

def create_feature_graphic():
    width, height = 1024, 500
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)
    draw_gradient(draw, width, height, (213, 63, 140), (151, 38, 109))
    
    # Soft concentric circles
    for r in [200, 150, 100]:
        draw.ellipse([780 - r, 250 - r, 780 + r, 250 + r], outline=(255, 255, 255, 35), width=3)
    
    f_title = get_font(46, bold=True)
    f_sub = get_font(24, bold=False)
    f_pill = get_font(20, bold=True)
    
    draw.text((60, 100), "PartoFácil", fill=(255, 255, 255), font=f_title)
    draw.text((60, 160), "Contador de Contrações & Trabalho de Parto", fill=(254, 215, 226), font=get_font(28, bold=True))
    draw.text((60, 215), "Monitore intervalos, duração e intensidade com\nprecisão e calma no momento mais especial.", fill=(255, 245, 247), font=f_sub)
    
    badges = ["1-Toque Cronômetro", "Regra 5-1-1 Médica", "100% Offline"]
    bx = 60
    for b in badges:
        bw = len(b) * 11 + 24
        draw.rounded_rectangle([bx, 340, bx + bw, 385], radius=22, fill=(255, 255, 255, 40), outline=(255, 255, 255, 120), width=2)
        draw.text((bx + 14, 350), b, fill=(255, 255, 255), font=f_pill)
        bx += bw + 16
        
    img.save(os.path.join(ASSETS_DIR, "feature-graphic-1024x500.png"))
    print("Feature graphic generated.")

def create_screenshots():
    width, height = 1080, 1920
    screens = [
        {
            "filename": "phone-1.png",
            "tag": "CRONÔMETRO SIMPLES",
            "title": "Cronômetro com Apenas 1 Toque",
            "desc": "Toque na tela para iniciar e finalizar cada contração sem complicações.",
            "card_title": "Contração em Andamento",
            "card_val": "00:48",
            "card_sub": "Último intervalo: 5 min atrás",
            "status": "Intensidade: Moderada"
        },
        {
            "filename": "phone-2.png",
            "tag": "ANÁLISE OBSTÉTRICA",
            "title": "Saiba a Hora de ir para a Maternidade",
            "desc": "Algoritmo obstétrico que acompanha a evolução e constância das contrações.",
            "card_title": "Padrão de Trabalho de Parto",
            "card_val": "5 - 1 - 1",
            "card_sub": "Contrações regulares a cada 5 minutos",
            "status": "Hora de avisar seu médico ou maternidade"
        },
        {
            "filename": "phone-3.png",
            "tag": "HISTÓRICO COMPLETO",
            "title": "Linha do Tempo e Intervalos Claros",
            "desc": "Visualize médias de duração, frequência e notas sobre a bolsa e sintomas.",
            "card_title": "Média da Última Hora",
            "card_val": "45s / 4m",
            "card_sub": "12 contrações registradas",
            "status": "Evolução estável e progressiva"
        },
        {
            "filename": "phone-4.png",
            "tag": "RELATÓRIO MÉDICO",
            "title": "Compartilhe com seu Obstetra",
            "desc": "Exporte os dados em formato CSV para enviar pelo WhatsApp ou prontuário.",
            "card_title": "Relatório Obstétrico",
            "card_val": "Pronto",
            "card_sub": "Dados organizados cronologicamente",
            "status": "Privacidade total: dados no seu celular"
        }
    ]
    
    for s in screens:
        img = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(img)
        draw_gradient(draw, width, height, (253, 242, 248), (251, 207, 232))
        
        f_tag = get_font(32, bold=True)
        f_head = get_font(54, bold=True)
        f_body = get_font(32, bold=False)
        
        draw.text((90, 140), s["tag"], fill=(213, 63, 140), font=f_tag)
        
        title_lines = [s["title"][:26], s["title"][26:]] if len(s["title"]) > 26 else [s["title"]]
        y = 200
        for l in title_lines:
            if l.strip():
                draw.text((90, y), l.strip(), fill=(45, 55, 72), font=f_head)
                y += 70
                
        draw.text((90, y + 20), s["desc"], fill=(100, 116, 139), font=f_body)
        
        card_top = 580
        draw.rounded_rectangle([90, card_top, width - 90, height - 120], radius=50, fill=(255, 255, 255), outline=(230, 230, 230), width=4)
        
        draw.rounded_rectangle([130, card_top + 50, width - 130, card_top + 130], radius=24, fill=(253, 242, 248))
        draw.text((160, card_top + 72), "PartoFácil - Monitor", fill=(213, 63, 140), font=get_font(32, bold=True))
        
        cx = width // 2
        cy = card_top + 460
        r = 210
        draw.arc([cx - r, cy - r, cx + r, cy + r], start=-90, end=270, fill=(245, 245, 245), width=36)
        draw.arc([cx - r, cy - r, cx + r, cy + r], start=-90, end=160, fill=(213, 63, 140), width=36)
        
        draw.text((cx - 190, cy - 80), s["card_title"], fill=(100, 116, 139), font=get_font(30, bold=False))
        draw.text((cx - 140, cy - 20), s["card_val"], fill=(45, 55, 72), font=get_font(68, bold=True))
        draw.text((cx - 190, cy + 80), s["card_sub"], fill=(140, 150, 160), font=get_font(26, bold=False))
        
        py = card_top + 800
        draw.rounded_rectangle([150, py, width - 150, py + 120], radius=24, fill=(254, 235, 246))
        draw.text((190, py + 40), s["status"], fill=(151, 38, 109), font=get_font(32, bold=True))
        
        by = card_top + 980
        draw.rounded_rectangle([150, by, width - 150, by + 100], radius=30, fill=(213, 63, 140))
        draw.text((cx - 120, by + 30), "Nova Contração", fill=(255, 255, 255), font=get_font(34, bold=True))
        
        img.save(os.path.join(ASSETS_DIR, s["filename"]))
        print(f"Saved {s['filename']}")

if __name__ == "__main__":
    create_icon()
    create_feature_graphic()
    create_screenshots()
