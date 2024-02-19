from discord import File
from easy_pil import Editor, load_image_async, Font

async def generate(title:str, subtitle:str, background:str, picture:str):
    Background = Editor(background).resize((549, 309))
    imageProfile = await load_image_async(picture)
    
    profile = Editor(imageProfile).resize((120, 120)).circle_image()
    poppins = Font.poppins(size=30, variant='bold')
    
    poppinsSmall = Font.poppins(size=20, variant='bold')
    
    Background.paste(profile, (215, 30))
    Background.ellipse((215, 30), 120, 120, outline='white', stroke_width=5)
    
    Background.text((278, 180), title, color='black', font=poppins, align='center')
    Background.text((275, 180), title, color='white', font=poppins, align='center')
    
    Background.text((277, 225), subtitle, color='black', font=poppinsSmall, align='center')
    Background.text((275, 225), subtitle, color='white', font=poppinsSmall, align='center')
    
    return File(fp=Background.image_bytes, filename='welcomeUser.png')