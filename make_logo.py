from pathlib import Path
from PIL import Image, ImageDraw

folder = Path.home() / "Desktop" / "BADRO_Data_Cleaner"
folder.mkdir(parents=True, exist_ok=True)

im = Image.new("RGB", (512, 512), "#101B35")
d = ImageDraw.Draw(im)

# Document
d.rounded_rectangle((125, 65, 365, 340), radius=24, fill="#FFFFFF")
d.polygon([(295, 65), (365, 135), (295, 135)], fill="#B9D8FF")

# CSV label
d.rounded_rectangle((155, 150, 270, 205), radius=12, fill="#159D76")
d.text((178, 166), "CSV", fill="white")

# Spreadsheet lines
for y in (235, 270, 305):
    d.rounded_rectangle((160, y, 325, y + 9), radius=4, fill="#B8C8DB")

# Cleaning brush
d.line((245, 350, 355, 235), fill="#39A7FF", width=24)
d.rounded_rectangle((320, 205, 390, 250), radius=12, fill="#39A7FF")
d.line((310, 280, 365, 315), fill="#38D6A3", width=10)
d.line((305, 295, 350, 335), fill="#38D6A3", width=8)
d.line((295, 305, 335, 350), fill="#38D6A3", width=7)

# Brand name
d.text((125, 390), "BADRO", fill="white", stroke_width=1)
d.text((125, 430), "DATA CLEANER", fill="#45D6A5")

png = folder / "badro_logo.png"
ico = folder / "badro_logo.ico"
im.save(png)
im.save(ico, format="ICO", sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)])

print("Logo created:", png)
print("Windows icon created:", ico)
