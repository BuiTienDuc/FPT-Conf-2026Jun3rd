
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# =========================================
# LINK WEBSITE
# =========================================
URL = "https://fpt-conf-2026jun3rd.streamlit.app/"

# =========================================
# OUTPUT FILE
# =========================================
OUTPUT_FILE = "QR_Code_I_Love_PTIT.png"

# =========================================
# TẠO QR CODE
# =========================================
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=16,
    border=4
)

qr.add_data(URL)
qr.make(fit=True)

qr_img = qr.make_image(
    fill_color="black",
    back_color="white"
).convert("RGB")

qr_width, qr_height = qr_img.size

# =========================================
# CANVAS
# =========================================
padding = 70
bottom_extra = 90

canvas_width = qr_width + padding * 2
canvas_height = qr_height + padding * 2 + bottom_extra

canvas = Image.new(
    "RGBA",
    (canvas_width, canvas_height),
    (255, 255, 255, 255)
)

# =========================================
# ĐỔ BÓNG
# =========================================
shadow = Image.new(
    "RGBA",
    canvas.size,
    (0, 0, 0, 0)
)

shadow_draw = ImageDraw.Draw(shadow)

shadow_draw.rounded_rectangle(
    (
        35,
        35,
        canvas_width - 35,
        canvas_height - 35
    ),
    radius=45,
    fill=(0, 0, 0, 60)
)

shadow = shadow.filter(ImageFilter.GaussianBlur(18))

canvas = Image.alpha_composite(canvas, shadow)

draw = ImageDraw.Draw(canvas)

# =========================================
# KHUNG NGOÀI
# =========================================
draw.rounded_rectangle(
    (
        35,
        25,
        canvas_width - 35,
        canvas_height - 35
    ),
    radius=45,
    fill="white",
    outline="#d71920",
    width=12
)

# =========================================
# KHUNG TRONG
# =========================================
draw.rounded_rectangle(
    (
        55,
        50,
        canvas_width - 55,
        canvas_height - 60
    ),
    radius=35,
    outline="#d71920",
    width=2
)

# =========================================
# DÁN QR
# =========================================
canvas.paste(
    qr_img,
    (padding, padding)
)

# =========================================
# LOGO GIỮA
# =========================================
logo_size = int(qr_width * 0.28)

logo = Image.new(
    "RGBA",
    (logo_size, logo_size),
    (255, 255, 255, 0)
)

logo_draw = ImageDraw.Draw(logo)

# =========================================
# VÒNG TRÒN LOGO
# =========================================
logo_draw.ellipse(
    (
        4,
        4,
        logo_size - 4,
        logo_size - 4
    ),
    fill="white",
    outline="#d71920",
    width=6
)

# =========================================
# FONT
# =========================================
try:

    # chữ I nhỏ bằng love
    font_I = ImageFont.truetype(
        "arialbd.ttf",
        int(logo_size * 0.18)
    )

    # chữ PTIT
    font_big = ImageFont.truetype(
        "arialbd.ttf",
        int(logo_size * 0.25)
    )

    # chữ love
    font_love = ImageFont.truetype(
        "ariali.ttf",
        int(logo_size * 0.18)
    )

except:
    font_I = ImageFont.load_default()
    font_big = ImageFont.load_default()
    font_love = ImageFont.load_default()

# =========================================
# CHỮ I
# =========================================
logo_draw.text(
    (logo_size * 0.24, logo_size * 0.26),
    "I",
    fill="#d71920",
    font=font_I
)

# =========================================
# CHỮ LOVE
# =========================================
logo_draw.text(
    (logo_size * 0.42, logo_size * 0.26),
    "love",
    fill="#d71920",
    font=font_love
)

# =========================================
# CHỮ PTIT
# =========================================
logo_draw.text(
    (logo_size * 0.22, logo_size * 0.50),
    "PTIT",
    fill="#d71920",
    font=font_big
)

# =========================================
# HÀM VẼ TRÁI TIM
# =========================================
def draw_heart(draw_obj, center_x, center_y, size, color):

    r = size * 0.25

    # bên trái
    draw_obj.ellipse(
        (
            center_x - r * 2,
            center_y - r,
            center_x,
            center_y + r
        ),
        fill=color
    )

    # bên phải
    draw_obj.ellipse(
        (
            center_x,
            center_y - r,
            center_x + r * 2,
            center_y + r
        ),
        fill=color
    )

    # tam giác dưới
    draw_obj.polygon(
        [
            (center_x - r * 2, center_y),
            (center_x + r * 2, center_y),
            (center_x, center_y + size)
        ],
        fill=color
    )

# =========================================
# TIM TRÊN
# =========================================
draw_heart(
    logo_draw,
    int(logo_size * 0.76),
    int(logo_size * 0.16),
    int(logo_size * 0.12),
    "#d71920"
)

# =========================================
# TIM DƯỚI
# =========================================
draw_heart(
    logo_draw,
    int(logo_size * 0.50),
    int(logo_size * 0.78),
    int(logo_size * 0.10),
    "#d71920"
)

# =========================================
# DÁN LOGO GIỮA QR
# =========================================
logo_x = padding + (qr_width - logo_size) // 2
logo_y = padding + (qr_height - logo_size) // 2

canvas.paste(
    logo,
    (logo_x, logo_y),
    logo
)

# =========================================
# THANH LINK ĐỎ
# =========================================
bar_x1 = padding + 35
bar_y1 = padding + qr_height + 18
bar_x2 = padding + qr_width - 35
bar_y2 = bar_y1 + 55

draw.rounded_rectangle(
    (
        bar_x1,
        bar_y1,
        bar_x2,
        bar_y2
    ),
    radius=25,
    fill="#d71920"
)

# =========================================
# FONT URL
# =========================================
try:
    font_url = ImageFont.truetype(
        "arialbd.ttf",
        28
    )

except:
    font_url = ImageFont.load_default()

# =========================================
# TEXT URL
# =========================================
draw.text(
    (
        bar_x1 + 25,
        bar_y1 + 12
    ),
    URL,
    fill="white",
    font=font_url
)

# =========================================
# SAVE FILE
# =========================================
canvas.convert("RGB").save(
    OUTPUT_FILE,
    quality=95
)

print("Đã tạo thành công:", OUTPUT_FILE)
