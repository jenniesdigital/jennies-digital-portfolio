import os
import shutil
from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageFont

WORKSPACE = r'C:\AI-Projects\JennieAI\jennies-digital-portfolio'
os.chdir(WORKSPACE)

os.makedirs('assets/css', exist_ok=True)
os.makedirs('assets/js', exist_ok=True)
os.makedirs('assets/images', exist_ok=True)
os.makedirs('assets/documents', exist_ok=True)
os.makedirs('work', exist_ok=True)
os.makedirs('lab', exist_ok=True)
os.makedirs('blog', exist_ok=True)

resume_src = r'assets/documents/JENNIFER OHAERI-EHIEM _ PRODUCT MARKETING MANAGER.pdf'
if os.path.exists(resume_src):
    shutil.copyfile(resume_src, 'assets/documents/jennifer-pmm-resume.pdf')
    shutil.copyfile(resume_src, 'assets/jennifer-pmm-resume.pdf')
    print('Resume PDF copied and synced successfully')

# -------------------------------------------------------------
# 0. MOCKUP GENERATORS (KOPPOH IPAD, WHATSAPP LAPTOP & OPAY 3D TABLET)
# -------------------------------------------------------------
def generate_mockups():
    # 1. Koppoh iPad Mockup
    koppoh_src = 'assets/images/work-koppoh.png'
    if os.path.exists(koppoh_src):
        screen_img = Image.open(koppoh_src).convert('RGBA')
        canvas_w, canvas_h = 1920, 1150
        bg_color = (230, 92, 0, 255) # Plain Brand Orange #e65c00

        ipad_w = 1480
        ipad_h = 890
        ipad_r = 40
        bezel = 24

        canvas = Image.new('RGBA', (canvas_w, canvas_h), bg_color)
        chassis = Image.new('RGBA', (ipad_w, ipad_h), (0, 0, 0, 0))
        draw_chassis = ImageDraw.Draw(chassis)

        draw_chassis.rounded_rectangle([0, 0, ipad_w, ipad_h], radius=ipad_r, fill=(24, 24, 26, 255), outline=(45, 45, 48, 255), width=3)

        screen_w = ipad_w - (bezel * 2)
        screen_h = ipad_h - (bezel * 2)
        screen_resized = screen_img.resize((screen_w, screen_h), Image.Resampling.LANCZOS)

        screen_mask = Image.new('L', (screen_w, screen_h), 0)
        draw_mask = ImageDraw.Draw(screen_mask)
        draw_mask.rounded_rectangle([0, 0, screen_w, screen_h], radius=18, fill=255)
        chassis.paste(screen_resized, (bezel, bezel), screen_mask)

        camera_r = 4
        cam_x = ipad_w // 2
        cam_y = bezel // 2
        draw_chassis.ellipse([cam_x - camera_r, cam_y - camera_r, cam_x + camera_r, cam_y + camera_r], fill=(10, 10, 12, 255), outline=(32, 32, 35, 255))

        shadow_w, shadow_h = ipad_w + 140, ipad_h + 140
        shadow_img = Image.new('RGBA', (shadow_w, shadow_h), (0, 0, 0, 0))
        draw_shadow = ImageDraw.Draw(shadow_img)
        draw_shadow.rounded_rectangle([70, 70, 70 + ipad_w, 70 + ipad_h], radius=ipad_r, fill=(0, 0, 0, 115))
        shadow_blurred = shadow_img.filter(ImageFilter.GaussianBlur(36))

        shadow_x = (canvas_w - shadow_w) // 2
        shadow_y = (canvas_h - shadow_h) // 2 + 18
        canvas.paste(shadow_blurred, (shadow_x, shadow_y), shadow_blurred)

        ipad_x = (canvas_w - ipad_w) // 2
        ipad_y = (canvas_h - ipad_h) // 2
        canvas.paste(chassis, (ipad_x, ipad_y), chassis)

        canvas.convert('RGB').save('assets/images/work-koppoh-ipad.png', quality=95)
        print('Koppoh iPad mockup generated')

    # 2. WhatsApp Laptop Mockup on Plain Orange Background
    wa_src = 'assets/images/whatsapp-raw.jpg'
    if os.path.exists(wa_src):
        screen_content = Image.open(wa_src).convert('RGBA')
        canvas_w, canvas_h = 1920, 1150
        bg_color = (230, 92, 0, 255) # Plain Brand Orange #e65c00

        lid_w = 1380
        lid_h = 820
        lid_r = 20
        bezel_t = 22
        bezel_side = 20
        bezel_b = 26

        base_w = 1540
        base_h = 32
        base_r = 10

        canvas = Image.new('RGBA', (canvas_w, canvas_h), bg_color)

        lid = Image.new('RGBA', (lid_w, lid_h), (0, 0, 0, 0))
        draw_lid = ImageDraw.Draw(lid)
        draw_lid.rounded_rectangle([0, 0, lid_w, lid_h], radius=lid_r, fill=(22, 22, 24, 255), outline=(45, 45, 48, 255), width=2)

        screen_w = lid_w - (bezel_side * 2)
        screen_h = lid_h - (bezel_t + bezel_b)

        screen_surface = Image.new('RGBA', (screen_w, screen_h), (242, 246, 243, 255))
        scale = min(screen_w / screen_content.width, screen_h / screen_content.height)
        new_w = int(screen_content.width * scale)
        new_h = int(screen_content.height * scale)
        resized_content = screen_content.resize((new_w, new_h), Image.Resampling.LANCZOS)

        offset_x = (screen_w - new_w) // 2
        offset_y = (screen_h - new_h) // 2
        screen_surface.paste(resized_content, (offset_x, offset_y), resized_content)

        screen_mask = Image.new('L', (screen_w, screen_h), 0)
        draw_mask = ImageDraw.Draw(screen_mask)
        draw_mask.rounded_rectangle([0, 0, screen_w, screen_h], radius=6, fill=255)

        lid.paste(screen_surface, (bezel_side, bezel_t), screen_mask)

        cam_x = lid_w // 2
        cam_y = bezel_t // 2
        draw_lid.ellipse([cam_x - 3, cam_y - 3, cam_x + 3, cam_y + 3], fill=(10, 10, 12, 255))

        base = Image.new('RGBA', (base_w, base_h + 20), (0, 0, 0, 0))
        draw_base = ImageDraw.Draw(base)
        draw_base.rounded_rectangle([0, 0, base_w, base_h], radius=base_r, fill=(35, 35, 38, 255), outline=(55, 55, 60, 255), width=1)
        notch_w = 160
        notch_x = (base_w - notch_w) // 2
        draw_base.rounded_rectangle([notch_x, 0, notch_x + notch_w, 6], radius=3, fill=(18, 18, 20, 255))

        shadow_w = base_w + 140
        shadow_h = 240
        shadow = Image.new('RGBA', (shadow_w, shadow_h), (0, 0, 0, 0))
        draw_shadow = ImageDraw.Draw(shadow)
        draw_shadow.ellipse([40, 40, shadow_w - 40, shadow_h - 40], fill=(0, 0, 0, 125))
        shadow_blur = shadow.filter(ImageFilter.GaussianBlur(38))

        lid_x = (canvas_w - lid_w) // 2
        lid_y = (canvas_h - lid_h - base_h) // 2 + 10
        base_x = (canvas_w - base_w) // 2
        base_y = lid_y + lid_h - 6
        shadow_x = (canvas_w - shadow_w) // 2
        shadow_y = base_y - 20

        canvas.paste(shadow_blur, (shadow_x, shadow_y), shadow_blur)
        canvas.paste(lid, (lid_x, lid_y), lid)
        canvas.paste(base, (base_x, base_y), base)

        canvas.convert('RGB').save('assets/images/work-whatsapp-laptop.png', quality=95)
        print('WhatsApp laptop mockup generated')

    # 3. OPay 3D-Turned Tablet Mockup on Plain Orange Background
    opay_src = 'assets/images/opay-raw.png'
    if os.path.exists(opay_src):
        screen_content = Image.open(opay_src).convert('RGBA')
        canvas_w, canvas_h = 1920, 1150
        bg_color = (230, 92, 0, 255) # Plain Brand Orange #e65c00

        tab_w, tab_h = 1380, 800
        bezel = 28
        tab = Image.new('RGBA', (tab_w, tab_h), (0, 0, 0, 0))
        draw_tab = ImageDraw.Draw(tab)

        draw_tab.rounded_rectangle([0, 0, tab_w, tab_h], radius=32, fill=(22, 22, 24, 255), outline=(55, 55, 60, 255), width=3)

        sc_w = tab_w - (bezel * 2)
        sc_h = tab_h - (bezel * 2)
        sc_img = ImageOps.fit(screen_content, (sc_w, sc_h), method=Image.Resampling.LANCZOS)
        sc_mask = Image.new('L', (sc_w, sc_h), 0)
        draw_sc_mask = ImageDraw.Draw(sc_mask)
        draw_sc_mask.rounded_rectangle([0, 0, sc_w, sc_h], radius=16, fill=255)
        tab.paste(sc_img, (bezel, bezel), sc_mask)

        draw_tab.ellipse([tab_w // 2 - 3, bezel // 2 - 3, tab_w // 2 + 3, bezel // 2 + 3], fill=(10, 10, 12, 255))

        def find_coeffs_pure_python(pa, pb):
            matrix = []
            for (x, y), (u, v) in zip(pa, pb):
                matrix.append([x, y, 1, 0, 0, 0, -u*x, -u*y, u])
                matrix.append([0, 0, 0, x, y, 1, -v*x, -v*y, v])
            n = 8
            for i in range(n):
                max_el = abs(matrix[i][i])
                max_row = i
                for k in range(i+1, n):
                    if abs(matrix[k][i]) > max_el:
                        max_el = abs(matrix[k][i])
                        max_row = k
                matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
                for k in range(i+1, n):
                    c = -matrix[k][i] / matrix[i][i]
                    for j in range(i, n+1):
                        if i == j:
                            matrix[k][j] = 0
                        else:
                            matrix[k][j] += c * matrix[i][j]
            coeffs = [0]*8
            for i in range(n-1, -1, -1):
                coeffs[i] = matrix[i][n] / matrix[i][i]
                for k in range(i-1, -1, -1):
                    matrix[k][n] -= matrix[k][i] * coeffs[i]
            return coeffs

        target_w, target_h = 1600, 1000
        tl = (220, 130)
        tr = (1440, 70)
        br = (1490, 870)
        bl = (180, 810)

        src_pts = [(0, 0), (tab_w, 0), (tab_w, tab_h), (0, tab_h)]
        dst_pts = [tl, tr, br, bl]

        coeffs = find_coeffs_pure_python(dst_pts, src_pts)
        tab_3d = tab.transform((target_w, target_h), Image.Transform.PERSPECTIVE, coeffs, Image.Resampling.BICUBIC)

        edge_layer = Image.new('RGBA', (target_w, target_h), (0, 0, 0, 0))
        draw_edge = ImageDraw.Draw(edge_layer)
        draw_edge.polygon([(tr[0], tr[1]), (tr[0]+18, tr[1]+12), (br[0]+18, br[1]+12), (br[0], br[1])], fill=(12, 12, 14, 255))
        draw_edge.polygon([(bl[0], bl[1]), (bl[0]+14, bl[1]+14), (br[0]+18, br[1]+12), (br[0], br[1])], fill=(8, 8, 10, 255))

        shadow = Image.new('RGBA', (target_w + 200, target_h + 200), (0, 0, 0, 0))
        draw_sh = ImageDraw.Draw(shadow)
        sh_offset = (100, 100)
        draw_sh.polygon([
            (tl[0] + sh_offset[0] + 60, tl[1] + sh_offset[1] + 80),
            (tr[0] + sh_offset[0] + 70, tr[1] + sh_offset[1] + 60),
            (br[0] + sh_offset[0] + 90, br[1] + sh_offset[1] + 80),
            (bl[0] + sh_offset[0] + 40, bl[1] + sh_offset[1] + 90)
        ], fill=(0, 0, 0, 130))
        shadow_blur = shadow.filter(ImageFilter.GaussianBlur(40))

        canvas = Image.new('RGBA', (canvas_w, canvas_h), bg_color)
        off_x = (canvas_w - target_w) // 2
        off_y = (canvas_h - target_h) // 2

        canvas.paste(shadow_blur, (off_x - 100, off_y - 80), shadow_blur)
        canvas.paste(edge_layer, (off_x, off_y), edge_layer)
        canvas.paste(tab_3d, (off_x, off_y), tab_3d)

        canvas.convert('RGB').save('assets/images/work-opay-tablet.png', quality=95)
        print('OPay 3D tablet mockup generated')

    # 4. CleanDesk Phone Mockup Screen
    cd_src = 'assets/images/cleandesk-raw.png'
    if os.path.exists(cd_src):
        user_img = Image.open(cd_src).convert('RGBA')
        w, h = 768, 1376
        canvas = Image.new('RGBA', (w, h), (255, 255, 255, 255))
        draw = ImageDraw.Draw(canvas)

        # Draw CleanDesk screen with subtle top bar and dynamic island
        scale = (w - 40) / user_img.width
        new_w = int(user_img.width * scale)
        new_h = int(user_img.height * scale)
        resized = user_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        pos_x = (w - new_w) // 2
        pos_y = 70
        canvas.paste(resized, (pos_x, pos_y), resized)

        # Dynamic island / pill at top
        draw.rounded_rectangle([(w - 190)//2, 24, (w + 190)//2, 58], radius=17, fill=(18, 18, 20, 255))

        # iOS bottom indicator bar
        bar_w, bar_h = 240, 8
        bar_x = (w - bar_w) // 2
        bar_y = h - 35
        draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h], radius=4, fill=(180, 180, 180, 255))

        canvas.convert('RGB').save('assets/images/lab-cleandesk.png', quality=95)
        canvas.convert('RGB').save('assets/images/lab-promptpulse.jpg', quality=95)
        print('CleanDesk phone screen generated')

    # 5. Soda Reader Images and Phone Mockup Screen
    soda_srcs = [
        r'C:\Users\USER\.gemini\antigravity\brain\db9d8dda-9490-4bd7-b4d0-b7c963f58af5\.user_uploaded\media_1787837492400.jpg',
        r'C:\Users\USER\.gemini\antigravity\brain\db9d8dda-9490-4bd7-b4d0-b7c963f58af5\.user_uploaded\media_1787837502359.jpg',
        r'C:\Users\USER\.gemini\antigravity\brain\db9d8dda-9490-4bd7-b4d0-b7c963f58af5\.user_uploaded\media_1787837512049.jpg',
        r'C:\Users\USER\.gemini\antigravity\brain\db9d8dda-9490-4bd7-b4d0-b7c963f58af5\.user_uploaded\media_1787837520977.jpg',
        r'C:\Users\USER\.gemini\antigravity\brain\db9d8dda-9490-4bd7-b4d0-b7c963f58af5\.user_uploaded\media_1787837526969.jpg',
        r'C:\Users\USER\.gemini\antigravity\brain\db9d8dda-9490-4bd7-b4d0-b7c963f58af5\.user_uploaded\media_1787838360641.jpg',
        r'C:\Users\USER\.gemini\antigravity\brain\db9d8dda-9490-4bd7-b4d0-b7c963f58af5\.user_uploaded\media_1787838375541.jpg',
        r'C:\Users\USER\.gemini\antigravity\brain\db9d8dda-9490-4bd7-b4d0-b7c963f58af5\.user_uploaded\media_1787838381480.jpg',
    ]
    for idx, p in enumerate(soda_srcs, 1):
        if os.path.exists(p):
            im = Image.open(p).convert('RGB')
            im.save(f'assets/images/soda-{idx}.jpg', quality=95)

    if os.path.exists('assets/images/soda-1.jpg'):
        user_img = Image.open('assets/images/soda-1.jpg').convert('RGBA')
        w, h = 768, 1376
        canvas = Image.new('RGBA', (w, h), (251, 249, 245, 255))
        draw = ImageDraw.Draw(canvas)

        scale = (w - 20) / user_img.width
        new_w = int(user_img.width * scale)
        new_h = int(user_img.height * scale)
        resized = user_img.resize((new_w, new_h), Image.Resampling.LANCZOS)

        pos_x = (w - new_w) // 2
        pos_y = 35
        canvas.paste(resized, (pos_x, pos_y), resized)

        # Dynamic island pill at top
        draw.rounded_rectangle([(w - 180)//2, 18, (w + 180)//2, 50], radius=16, fill=(20, 20, 20, 255))

        # Bottom home indicator
        bar_w, bar_h = 240, 8
        bar_x = (w - bar_w) // 2
        bar_y = h - 30
        draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h], radius=4, fill=(180, 180, 180, 255))

        canvas.convert('RGB').save('assets/images/lab-soda.png', quality=95)
        canvas.convert('RGB').save('assets/images/lab-valuemetric.jpg', quality=95)
        print('Soda Reader phone screen generated')

    # 6. ContentLabAI Phone Mockup Screen
    w, h = 768, 1376
    canvas = Image.new('RGBA', (w, h), (16, 16, 18, 255))
    draw = ImageDraw.Draw(canvas)

    # Dynamic island pill
    draw.rounded_rectangle([(w - 180)//2, 18, (w + 180)//2, 50], radius=16, fill=(8, 8, 10, 255))

    # Top App Header
    draw.rounded_rectangle([48, 75, 230, 110], radius=17, fill=(230, 92, 0, 35), outline=(230, 92, 0, 180), width=1)
    
    # Title & Subtitle Card
    draw.rounded_rectangle([48, 130, w - 48, 240], radius=20, fill=(26, 26, 30, 255), outline=(42, 42, 48, 255), width=1)

    # Voice Engine Status Card (Jay Voice Model Match 98.4%)
    draw.rounded_rectangle([48, 260, w - 48, 380], radius=20, fill=(230, 92, 0, 20), outline=(230, 92, 0, 120), width=1)

    # Input Draft Source Card
    draw.rounded_rectangle([48, 400, w - 48, 570], radius=20, fill=(26, 26, 30, 255), outline=(42, 42, 48, 255), width=1)

    # Multi-Platform Output Cards (LinkedIn, X/Twitter, Substack, Google Drive Sync)
    draw.rounded_rectangle([48, 590, w - 48, 740], radius=18, fill=(24, 24, 28, 255), outline=(247, 195, 0, 100), width=1)
    draw.rounded_rectangle([48, 760, w - 48, 910], radius=18, fill=(24, 24, 28, 255), outline=(230, 92, 0, 100), width=1)
    draw.rounded_rectangle([48, 930, w - 48, 1080], radius=18, fill=(24, 24, 28, 255), outline=(60, 60, 68, 255), width=1)
    draw.rounded_rectangle([48, 1100, w - 48, 1230], radius=18, fill=(30, 30, 36, 255), outline=(0, 200, 120, 120), width=1)

    # Try drawing text with PIL font
    try:
        font_lg = ImageFont.truetype('arial.ttf', 34)
        font_md = ImageFont.truetype('arial.ttf', 24)
        font_sm = ImageFont.truetype('arial.ttf', 18)
        font_mono = ImageFont.truetype('consola.ttf', 16)

        # Header Badge
        draw.text((68, 83), "VOICE STUDIO 2.0", fill=(255, 140, 50, 255), font=font_mono)

        # Title Card
        draw.text((72, 148), "ContentLabAI", fill=(255, 255, 255, 255), font=font_lg)
        draw.text((72, 192), "One Idea -> Platform-Ready Content In My Voice", fill=(170, 170, 180, 255), font=font_sm)

        # Voice Engine
        draw.text((72, 282), "Active Voice Profile: Jay (Jennies Digital)", fill=(255, 255, 255, 255), font=font_md)
        draw.text((72, 320), "Authentic Style Fidelity: 98.4% Match · Zero Clichés", fill=(247, 195, 0, 255), font=font_sm)

        # Input Draft
        draw.text((72, 420), "SOURCE CONTENT (RAW INPUT)", fill=(230, 92, 0, 255), font=font_mono)
        draw.text((72, 455), "Why positioning beats features every single time.", fill=(255, 255, 255, 255), font=font_md)
        draw.text((72, 495), "Analyzed: 1 core thesis, 4 arguments, 3 proof points.", fill=(160, 160, 170, 255), font=font_sm)

        # Platform Cards
        draw.text((72, 610), "LINKEDIN POST FORMAT", fill=(247, 195, 0, 255), font=font_mono)
        draw.text((72, 645), "Hooks, structured bullet points, spacing & CTA", fill=(255, 255, 255, 255), font=font_md)
        draw.text((72, 685), "Status: Generated in personal voice ✓", fill=(160, 160, 170, 255), font=font_sm)

        draw.text((72, 780), "X / TWITTER THREAD", fill=(255, 140, 50, 255), font=font_mono)
        draw.text((72, 815), "Punchy 6-tweet narrative arc with takeaway", fill=(255, 255, 255, 255), font=font_md)
        draw.text((72, 855), "Status: Optimized for engagement & retweets ✓", fill=(160, 160, 170, 255), font=font_sm)

        draw.text((72, 950), "NEWSLETTER / ESSAY", fill=(180, 180, 200, 255), font=font_mono)
        draw.text((72, 985), "In-depth breakdown for Substack & blog", fill=(255, 255, 255, 255), font=font_md)
        draw.text((72, 1025), "Status: Long-form draft with narrative nuance ✓", fill=(160, 160, 170, 255), font=font_sm)

        draw.text((72, 1120), "GOOGLE DRIVE AUTO-SYNC", fill=(0, 220, 140, 255), font=font_mono)
        draw.text((72, 1155), "Delivered to: /JenniesDigital/ContentLab/2026", fill=(255, 255, 255, 255), font=font_md)
        draw.text((72, 1195), "5 files organized & ready for final review ✓", fill=(160, 160, 170, 255), font=font_sm)
    except Exception as e:
        print(f"PIL font drawing fallback: {e}")

    # Bottom iOS home bar
    bar_w, bar_h = 240, 8
    bar_x = (w - bar_w) // 2
    bar_y = h - 30
    draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h], radius=4, fill=(180, 180, 180, 255))

    canvas.convert('RGB').save('assets/images/lab-contentlabai.png', quality=95)
    canvas.convert('RGB').save('assets/images/lab-copymorph.jpg', quality=95)
    print('ContentLabAI phone screen generated')

    # 7. Creator Monetisation Laptop Mockup on Plain Orange Background
    creator_src = r'C:\Users\USER\.gemini\antigravity\brain\db9d8dda-9490-4bd7-b4d0-b7c963f58af5\.user_uploaded\media_1787839172232.png'
    if os.path.exists(creator_src):
        im = Image.open(creator_src).convert('RGBA')
        im.save('assets/images/creator-landscape-raw.png', quality=95)
        
        screen_content = im
        canvas_w, canvas_h = 1920, 1150
        bg_color = (230, 92, 0, 255) # Plain Brand Orange #e65c00

        lid_w = 1380
        lid_h = 820
        lid_r = 20
        bezel_t = 22
        bezel_side = 20
        bezel_b = 26

        base_w = 1540
        base_h = 32
        base_r = 10

        canvas = Image.new('RGBA', (canvas_w, canvas_h), bg_color)

        lid = Image.new('RGBA', (lid_w, lid_h), (0, 0, 0, 0))
        draw_lid = ImageDraw.Draw(lid)
        draw_lid.rounded_rectangle([0, 0, lid_w, lid_h], radius=lid_r, fill=(22, 22, 24, 255), outline=(45, 45, 48, 255), width=2)

        screen_w = lid_w - (bezel_side * 2)
        screen_h = lid_h - (bezel_t + bezel_b)

        screen_surface = Image.new('RGBA', (screen_w, screen_h), (18, 18, 20, 255))
        scale = min(screen_w / screen_content.width, screen_h / screen_content.height)
        new_w = int(screen_content.width * scale)
        new_h = int(screen_content.height * scale)
        resized_content = screen_content.resize((new_w, new_h), Image.Resampling.LANCZOS)

        offset_x = (screen_w - new_w) // 2
        offset_y = (screen_h - new_h) // 2
        screen_surface.paste(resized_content, (offset_x, offset_y), resized_content)

        screen_mask = Image.new('L', (screen_w, screen_h), 0)
        draw_mask = ImageDraw.Draw(screen_mask)
        draw_mask.rounded_rectangle([0, 0, screen_w, screen_h], radius=6, fill=255)

        lid.paste(screen_surface, (bezel_side, bezel_t), screen_mask)

        cam_x = lid_w // 2
        cam_y = bezel_t // 2
        draw_lid.ellipse([cam_x - 3, cam_y - 3, cam_x + 3, cam_y + 3], fill=(10, 10, 12, 255))

        base = Image.new('RGBA', (base_w, base_h + 20), (0, 0, 0, 0))
        draw_base = ImageDraw.Draw(base)
        draw_base.rounded_rectangle([0, 0, base_w, base_h], radius=base_r, fill=(35, 35, 38, 255), outline=(55, 55, 60, 255), width=1)
        notch_w = 160
        notch_x = (base_w - notch_w) // 2
        draw_base.rounded_rectangle([notch_x, 0, notch_x + notch_w, 6], radius=3, fill=(18, 18, 20, 255))

        shadow_w = base_w + 140
        shadow_h = 240
        shadow = Image.new('RGBA', (shadow_w, shadow_h), (0, 0, 0, 0))
        draw_shadow = ImageDraw.Draw(shadow)
        draw_shadow.ellipse([40, 40, shadow_w - 40, shadow_h - 40], fill=(0, 0, 0, 125))
        shadow_blur = shadow.filter(ImageFilter.GaussianBlur(38))

        lid_x = (canvas_w - lid_w) // 2
        lid_y = (canvas_h - lid_h - base_h) // 2 + 10
        base_x = (canvas_w - base_w) // 2
        base_y = lid_y + lid_h - 6
        shadow_x = (canvas_w - shadow_w) // 2
        shadow_y = base_y - 20

        canvas.paste(shadow_blur, (shadow_x, shadow_y), shadow_blur)
        canvas.paste(lid, (lid_x, lid_y), lid)
        canvas.paste(base, (base_x, base_y), base)

        canvas.convert('RGB').save('assets/images/work-creator-monetisation.png', quality=95)
        canvas.convert('RGB').save('assets/images/work-lumina.jpg', quality=95)
        print('Creator Monetisation laptop mockup generated')

# -------------------------------------------------------------
# 1. CSS GENERATOR
# -------------------------------------------------------------
def build_css():
    css = """/* ==========================================================================
   JENNIES DIGITAL - CORE DESIGN SYSTEM & STYLESHEET
   ========================================================================== */

:root {
  --brand-orange: #e65c00;
  --brand-orange-hover: #ff6e0d;
  --brand-orange-light: rgba(230, 92, 0, 0.12);
  --brand-orange-glow: rgba(230, 92, 0, 0.35);

  --brand-yellow: #f7c300;
  --brand-yellow-hover: #ffd428;
  --brand-yellow-light: rgba(247, 195, 0, 0.15);
  --brand-yellow-glow: rgba(247, 195, 0, 0.3);

  --brand-brown: #662300;
  --brand-brown-dark: #381300;
  --brand-brown-light: #8a3203;

  /* Theme Tokens (Dark Mode Default) */
  --bg-primary: #080808;
  --bg-surface: #141414;
  --bg-surface-elevated: #181818;
  --bg-card: #121212;
  --bg-card-hover: #161616;
  --bg-ink: #050505;

  --text-primary: #f5f5f7;
  --text-secondary: rgba(245, 245, 247, 0.82);
  --text-muted: rgba(245, 245, 247, 0.52);
  --text-subtle: rgba(245, 245, 247, 0.32);

  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-medium: rgba(255, 255, 255, 0.14);
  --border-strong: rgba(255, 255, 255, 0.25);
  --border-focus: var(--brand-orange);

  --nav-scrolled-bg: rgba(18, 18, 18, 0.88);
  --nav-scrolled-border: rgba(255, 255, 255, 0.12);
  --nav-link-color: rgba(245, 245, 247, 0.75);
  --nav-link-hover: #ffffff;
  --nav-active-bg: var(--brand-orange);
  --nav-active-color: #ffffff;

  --font-display: "Bricolage Grotesque", -apple-system, BlinkMacSystemFont, sans-serif;
  --font-sans: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: 'Geist Mono', monospace;

  --container-max: 1200px;
  --container-wide: 1440px;
  --radius-sm: 6px;
  --radius-md: 12px;
  --radius-lg: 18px;
  --radius-xl: 28px;
  --radius-full: 9999px;

  --shadow-sm: 0 4px 12px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 12px 32px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 24px 64px -12px rgba(0, 0, 0, 0.6);
}

/* High-Contrast Light Mode */
html.light {
  --bg-primary: #fbf9f6;
  --bg-surface: #ffffff;
  --bg-surface-elevated: #f2eee8;
  --bg-card: #ffffff;
  --bg-card-hover: #faf8f5;
  --bg-ink: #f0eae1;

  --text-primary: #111111;
  --text-secondary: #333333;
  --text-muted: #666666;
  --text-subtle: #888888;

  --border-subtle: rgba(0, 0, 0, 0.08);
  --border-medium: rgba(0, 0, 0, 0.15);
  --border-strong: rgba(0, 0, 0, 0.28);

  --nav-scrolled-bg: rgba(255, 255, 255, 0.9);
  --nav-scrolled-border: rgba(0, 0, 0, 0.1);
  --nav-link-color: #444444;
  --nav-link-hover: #000000;
  --nav-active-bg: var(--brand-orange);
  --nav-active-color: #ffffff;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-family: var(--font-sans);
  font-size: 16px;
  color: var(--text-primary);
  background-color: var(--bg-primary);
  scroll-behavior: smooth;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
  line-height: 1.6;
  transition: background-color 0.3s ease, color 0.3s ease;
}

h1, h2, h3, h4, h5, h6, .font-display {
  font-family: var(--font-display);
  font-optical-sizing: auto;
  font-variation-settings: "wdth" 100;
}

img, video {
  max-width: 100%;
  height: auto;
  display: block;
}

a {
  color: inherit;
  text-decoration: none;
  transition: color 0.2s ease, opacity 0.2s ease;
}

button {
  font-family: inherit;
  cursor: pointer;
  border: none;
  background: none;
}

.container {
  width: 100%;
  max-width: var(--container-max);
  margin-left: auto;
  margin-right: auto;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
}

.container-wide {
  width: 100%;
  max-width: var(--container-wide);
  margin-left: auto;
  margin-right: auto;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
}

/* ==========================================================================
   SITE PRELOADER
   ========================================================================== */
.site-preloader {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: #000000;
  z-index: 999999;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity 0.5s cubic-bezier(0.77, 0, 0.175, 1), transform 0.5s cubic-bezier(0.77, 0, 0.175, 1), visibility 0.5s ease;
  pointer-events: all;
}

html.light .site-preloader {
  background-color: #f8f9fa;
}

.site-preloader.loaded {
  opacity: 0;
  visibility: hidden;
  transform: translateY(-100%);
  pointer-events: none;
}

.preloader-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 2rem;
  max-width: 320px;
  width: 100%;
}

.preloader-logo-wrap {
  position: relative;
  width: 64px;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.25rem;
}

.preloader-logo {
  width: 48px;
  height: 48px;
  object-fit: contain;
  z-index: 2;
  animation: preloader-float 1.8s ease-in-out infinite alternate;
}

.preloader-pulse {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 80px;
  height: 80px;
  margin-top: -40px;
  margin-left: -40px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(230, 92, 0, 0.45) 0%, rgba(230, 92, 0, 0) 70%);
  animation: preloader-pulse 1.8s ease-in-out infinite;
}

@keyframes preloader-pulse {
  0% { transform: scale(0.75); opacity: 0.3; }
  50% { transform: scale(1.35); opacity: 0.9; }
  100% { transform: scale(0.75); opacity: 0.3; }
}

@keyframes preloader-float {
  0% { transform: translateY(0); }
  100% { transform: translateY(-5px); }
}

.preloader-brand {
  font-family: var(--font-display);
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--text-primary);
  margin-bottom: 1.5rem;
}

.preloader-bar-wrap {
  width: 100%;
  height: 3px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 4px;
  overflow: hidden;
  position: relative;
  margin-bottom: 0.85rem;
}

html.light .preloader-bar-wrap {
  background: rgba(0, 0, 0, 0.08);
}

.preloader-bar {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, var(--brand-orange) 0%, var(--brand-yellow) 100%);
  box-shadow: 0 0 14px rgba(230, 92, 0, 0.7);
  border-radius: 4px;
  transition: width 0.12s ease-out;
}

.preloader-meta {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--text-secondary);
  letter-spacing: 0.05em;
}

.preloader-status {
  text-transform: uppercase;
}

.preloader-percent {
  color: var(--brand-orange);
  font-weight: 600;
}

/* ==========================================================================
   NAVIGATION BAR
   ========================================================================== */
.site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  pointer-events: none;
  width: 100%;
}

.nav-wrapper-outer {
  width: 100%;
  max-width: 820px;
  margin: 0 auto;
  padding: 14px 1rem 0;
}

.nav-bar-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 10px 14px;
  border-radius: var(--radius-full);
  pointer-events: auto;
  border: 1px solid transparent;
  background: transparent;
  backdrop-filter: none;
  -webkit-backdrop-filter: none;
  transition: background-color 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease, backdrop-filter 0.4s ease, padding 0.3s ease;
}

.site-header.scrolled .nav-bar-inner,
.site-header.subpage-nav .nav-bar-inner {
  background: var(--nav-scrolled-bg);
  border-color: var(--nav-scrolled-border);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35);
  padding: 8px 12px;
}

html.light .site-header.scrolled .nav-bar-inner,
html.light .site-header.subpage-nav .nav-bar-inner {
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
}

.nav-brand {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.2rem 0.4rem;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1.0625rem;
  letter-spacing: -0.02em;
  color: var(--text-primary);
}

.nav-logo-wrap {
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  overflow: hidden;
}

.nav-logo-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.nav-menu {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
}

.nav-link {
  display: inline-flex;
  align-items: center;
  padding: 0.35rem 0.8rem;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--nav-link-color);
  border-radius: var(--radius-full);
  transition: all 0.2s ease;
}

.nav-link:hover {
  color: var(--nav-link-hover);
  background: var(--brand-orange-light);
}

.nav-link.active {
  background: var(--nav-active-bg);
  color: var(--nav-active-color);
  font-weight: 600;
}

.nav-actions {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.theme-toggle-btn,
.mobile-menu-btn {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-full);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--text-primary);
  border: 1px solid var(--border-medium);
  background: var(--bg-surface-elevated);
  cursor: pointer;
  padding: 0;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  flex-shrink: 0;
}

.theme-toggle-btn svg,
.mobile-menu-btn svg {
  width: 18px;
  height: 18px;
  display: block;
  stroke: currentColor;
  stroke-width: 2.2;
}

.theme-toggle-btn:hover,
.mobile-menu-btn:hover {
  color: var(--brand-orange);
  border-color: var(--brand-orange);
  background: var(--brand-orange-light);
  transform: translateY(-1px);
}

.mobile-menu-btn {
  display: none;
}

.nav-say-hi-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.35rem 0.85rem;
  height: 36px;
  border-radius: var(--radius-full);
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text-primary);
  border: 1px solid var(--border-medium);
  background: var(--bg-surface-elevated);
  transition: all 0.2s ease;
}

.nav-say-hi-btn:hover {
  border-color: var(--brand-orange);
  background: var(--brand-orange-light);
  color: #ffffff;
  transform: translateY(-1px);
}

html.light .nav-say-hi-btn:hover {
  color: var(--brand-orange);
}

.mobile-nav-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(8, 8, 8, 0.96);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  z-index: 999;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
}

html.light .mobile-nav-overlay {
  background: rgba(251, 249, 246, 0.97);
}

.mobile-nav-overlay.open {
  display: flex;
}

.mobile-nav-link {
  font-family: var(--font-display);
  font-size: 1.85rem;
  font-weight: 700;
  color: var(--text-primary);
  transition: all 0.2s ease;
}

.mobile-nav-link.active,
.mobile-nav-link:hover {
  color: var(--brand-orange);
}

/* ==========================================================================
   HERO SECTION
   ========================================================================== */
.hero-section {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: flex-end;
  justify-content: flex-start;
  padding-bottom: 6rem;
  padding-top: 8rem;
  overflow: hidden;
}

.hero-bg-container {
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
}

.hero-character-stage {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-character-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 20%;
  z-index: 1;
}

.hero-gradient-overlay {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: linear-gradient(180deg, rgba(8, 8, 8, 0.1) 0%, rgba(8, 8, 8, 0.45) 55%, var(--bg-primary) 100%);
  pointer-events: none;
}

html.light .hero-gradient-overlay {
  background: linear-gradient(180deg, rgba(251, 249, 246, 0.1) 0%, rgba(251, 249, 246, 0.5) 55%, var(--bg-primary) 100%);
}

.hero-ambient-glow {
  position: absolute;
  top: 20%;
  right: 10%;
  width: 520px;
  height: 520px;
  background: radial-gradient(circle, rgba(230, 92, 0, 0.3) 0%, rgba(247, 195, 0, 0.12) 50%, transparent 75%);
  filter: blur(90px);
  pointer-events: none;
  z-index: 2;
}

.hero-content {
  position: relative;
  z-index: 10;
  width: 100%;
  max-width: var(--container-wide);
  margin: 0 auto;
  padding: 0 2rem;
}

.hero-title {
  font-family: var(--font-display);
  font-size: clamp(3rem, 5.8vw, 5.85rem);
  font-weight: 800;
  line-height: 1.06;
  letter-spacing: -0.035em;
  color: var(--text-primary);
  max-width: 95vw;
  margin-bottom: 2rem;
}

.title-accent {
  background: linear-gradient(135deg, var(--brand-orange) 0%, var(--brand-yellow) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-actions {
  display: inline-flex;
  align-items: center;
  gap: 1rem;
}

.btn-primary-hero {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.85rem 1.75rem;
  border-radius: var(--radius-full);
  background: var(--text-primary);
  color: var(--bg-primary);
  font-weight: 600;
  font-size: 0.9375rem;
  transition: background-color 0.25s ease, color 0.25s ease, box-shadow 0.25s ease;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
}

.btn-primary-hero:hover {
  background: var(--brand-orange);
  color: #ffffff;
  box-shadow: 0 12px 28px rgba(230, 92, 0, 0.4);
}

.btn-secondary-hero {
  display: inline-flex;
  align-items: center;
  padding: 0.85rem 1.75rem;
  border-radius: var(--radius-full);
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-medium);
  color: var(--text-primary);
  font-weight: 500;
  font-size: 0.9375rem;
  transition: border-color 0.25s ease, background-color 0.25s ease;
}

.btn-secondary-hero:hover {
  border-color: var(--brand-yellow);
  background: var(--brand-yellow-light);
}

/* ==========================================================================
   SHARED SECTION HEADERS
   ========================================================================== */
.section-work,
.section-labs,
.section-about,
.section-blog {
  padding: 7rem 0;
  position: relative;
  background-color: var(--bg-primary);
}

.section-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 2rem;
  margin-bottom: 3.5rem;
}

.tag-label {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--brand-orange);
  margin-bottom: 0.6rem;
}

.section-title {
  font-family: var(--font-display);
  font-size: clamp(2rem, 4vw, 3.25rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  color: var(--text-primary);
  line-height: 1.1;
}

.section-subtitle {
  max-width: 24rem;
  color: var(--text-secondary);
  font-size: 0.9375rem;
}

/* ==========================================================================
   SELECTED WORK GRID - STRICT UNIFORM SIZING & ELLIPSIS CLAMPING
   ========================================================================== */
.work-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
}

.work-card {
  display: flex;
  flex-direction: column;
  height: 540px; /* Strict uniform height */
  background: var(--bg-card);
  border-radius: var(--radius-lg);
  border: 1px solid var(--border-subtle);
  overflow: hidden;
  position: relative;
  transition: border-color 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
}

.work-card:hover {
  border-color: var(--brand-orange);
  box-shadow: 0 16px 40px rgba(230, 92, 0, 0.15);
  background: var(--bg-card-hover);
}

.work-card-media {
  position: relative;
  height: 270px;
  width: 100%;
  flex-shrink: 0;
  background: #000000;
  overflow: hidden;
}

.work-card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.work-card-meta {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  flex-grow: 1;
  justify-content: space-between;
}

.work-meta-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--brand-orange);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.work-title {
  font-family: var(--font-display);
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.3;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  height: 2.6em;
  margin: 0.15rem 0;
}

.work-card:hover .work-title {
  color: var(--brand-orange);
}

.work-description {
  font-size: 0.875rem;
  color: var(--text-secondary);
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  height: 3em;
}

.work-metric-highlight {
  margin-top: auto;
  padding-top: 0.6rem;
  font-family: var(--font-mono);
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--brand-yellow);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

html.light .work-metric-highlight {
  color: var(--brand-brown);
}

/* ==========================================================================
   LABS SECTION
   ========================================================================== */
.labs-title {
  font-family: var(--font-display);
  font-size: clamp(2rem, 4vw, 3.25rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  color: var(--text-primary);
  line-height: 1.1;
}

.labs-accent {
  background: linear-gradient(135deg, var(--brand-orange) 0%, var(--brand-yellow) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.labs-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-top: 3.5rem;
}

.lab-card {
  display: flex;
  flex-direction: column;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 1.75rem;
  transition: border-color 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
}

.lab-card:hover {
  border-color: var(--brand-yellow);
  box-shadow: 0 16px 40px rgba(247, 195, 0, 0.15);
  background: var(--bg-card-hover);
}

.lab-phone-frame {
  width: 100%;
  aspect-ratio: 9 / 16;
  max-height: 380px;
  margin: 0 auto 1.5rem;
  background: #000000;
  border-radius: 36px;
  padding: 8px;
  border: 3px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
  overflow: hidden;
}

.lab-phone-inner {
  width: 100%;
  height: 100%;
  border-radius: 28px;
  overflow: hidden;
}

.lab-phone-inner img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Infinite Carousel / Marquee for Lab Case Studies */
.marquee-container {
  width: 100%;
  overflow: hidden;
  position: relative;
  margin: 2.5rem 0;
  padding: 1.5rem 0;
  -webkit-mask-image: linear-gradient(to right, transparent 0%, black 6%, black 94%, transparent 100%);
  mask-image: linear-gradient(to right, transparent 0%, black 6%, black 94%, transparent 100%);
}

.marquee-track {
  display: flex;
  gap: 1.75rem;
  width: max-content;
  animation: marquee-scroll 45s linear infinite;
}

.marquee-track:hover {
  animation-play-state: paused;
}

@keyframes marquee-scroll {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(calc(-50% - 0.875rem));
  }
}

.carousel-phone-card {
  width: 220px;
  height: 440px;
  flex-shrink: 0;
  background: #000000;
  border-radius: 32px;
  padding: 6px;
  border: 2px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.4);
  overflow: hidden;
  transition: transform 0.3s ease, border-color 0.3s ease;
}

.carousel-phone-card:hover {
  transform: translateY(-6px);
  border-color: var(--brand-orange);
}

.carousel-phone-card img {
  width: 100%;
  height: 100%;
  border-radius: 26px;
  object-fit: cover;
}

.lab-app-title {
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.4rem;
}

.lab-app-title svg {
  color: var(--text-muted);
  transition: color 0.25s ease;
}

.lab-card:hover .lab-app-title svg {
  color: var(--brand-yellow);
}

.lab-app-desc {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin-bottom: 0.75rem;
}

.lab-app-tag {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--brand-orange);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

/* ==========================================================================
   ABOUT SECTION
   ========================================================================== */
.about-grid {
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 4rem;
  align-items: flex-start;
  margin-top: 2rem;
}

.scroll-color-text {
  font-family: var(--font-display);
  font-size: clamp(1.3rem, 2.5vw, 2rem);
  font-weight: 600;
  line-height: 1.4;
  letter-spacing: -0.02em;
  color: var(--text-muted);
}

.scroll-color-text .word {
  transition: color 0.25s ease;
}

.scroll-color-text .word.highlighted {
  color: var(--text-primary);
}

.scroll-color-text .word.brand-highlight.highlighted {
  color: var(--brand-orange);
}

.about-pills-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin-top: 2.5rem;
}

.about-badge-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.45rem 0.95rem;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 500;
  border-radius: var(--radius-full);
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  color: var(--text-secondary);
}

html.light .about-badge-pill {
  color: var(--text-primary);
  background: #ffffff;
  border-color: rgba(0, 0, 0, 0.1);
}

.about-sidebar-text {
  font-size: 1.0625rem;
  color: var(--text-secondary);
  line-height: 1.7;
  margin-bottom: 2rem;
}

.about-cta-group {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.btn-about-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.85rem 1.75rem;
  border-radius: var(--radius-full);
  background: var(--brand-orange);
  color: #ffffff;
  font-weight: 600;
  font-size: 0.9375rem;
  transition: background-color 0.25s ease, box-shadow 0.25s ease;
}

.btn-about-primary:hover {
  background: var(--brand-orange-hover);
  box-shadow: 0 10px 24px rgba(230, 92, 0, 0.35);
}

.btn-about-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.85rem 1.75rem;
  border-radius: var(--radius-full);
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-medium);
  color: var(--text-primary);
  font-weight: 500;
  font-size: 0.9375rem;
  transition: border-color 0.25s ease, background-color 0.25s ease;
}

.btn-about-secondary:hover {
  border-color: var(--brand-yellow);
  background: var(--brand-yellow-light);
}

/* ==========================================================================
   SUBJECT MATTER / BLOG SECTION
   ========================================================================== */
.blog-grid-2col {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
}

.blog-static-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 2.25rem;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  transition: border-color 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
}

.blog-static-card:hover {
  border-color: var(--brand-orange);
  box-shadow: 0 16px 40px rgba(230, 92, 0, 0.12);
  background: var(--bg-card-hover);
}

.blog-card-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  margin-bottom: 1.25rem;
  flex-wrap: wrap;
}

.blog-badges-wrap {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  flex-wrap: wrap;
}

.blog-category-badge {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--brand-orange);
  background: var(--brand-orange-light);
  border: 1px solid var(--brand-orange);
  padding: 0.2rem 0.65rem;
  border-radius: var(--radius-full);
}

.blog-format-tag {
  font-family: var(--font-mono);
  font-size: 0.6875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-secondary);
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-medium);
  padding: 0.2rem 0.6rem;
  border-radius: var(--radius-full);
}

.blog-read-time {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--text-muted);
}

.blog-card-title {
  font-family: var(--font-display);
  font-size: 1.35rem;
  font-weight: 700;
  line-height: 1.25;
  color: var(--text-primary);
  margin-bottom: 0.75rem;
}

.blog-title-link {
  color: inherit;
  text-decoration: none;
  transition: color 0.2s ease;
}

.blog-title-link:hover,
.blog-static-card:hover .blog-title-link {
  color: var(--brand-orange);
}

.blog-card-excerpt {
  font-size: 0.9375rem;
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.blog-card-footer {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-top: 1.25rem;
  border-top: 1px solid var(--border-subtle);
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--brand-orange);
}

.read-more-link {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  color: var(--brand-orange);
  transition: transform 0.2s ease;
}

.blog-static-card:hover .read-more-link {
  transform: translateX(4px);
}

.blog-filter-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 2.75rem;
}

.blog-tab-btn {
  font-family: var(--font-mono);
  font-size: 0.8125rem;
  font-weight: 500;
  padding: 0.45rem 1.1rem;
  border-radius: var(--radius-full);
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-medium);
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s ease;
}

.blog-tab-btn:hover {
  border-color: var(--brand-orange);
  color: var(--text-primary);
  background: var(--brand-orange-light);
}

.blog-tab-btn.active {
  background: var(--brand-orange);
  border-color: var(--brand-orange);
  color: #ffffff;
  font-weight: 600;
}

.blog-view-all-cta {
  display: flex;
  justify-content: center;
  margin-top: 3rem;
}

/* ==========================================================================
   FOOTER / CONTACT SECTION
   ========================================================================== */
.site-footer {
  background: var(--bg-primary);
  border-top: 1px solid var(--border-subtle);
  padding: 6rem 0 3rem;
  position: relative;
  overflow: hidden;
}

.footer-hero-link {
  display: inline-block;
  font-family: var(--font-display);
  font-size: clamp(3.5rem, 10vw, 9rem);
  font-weight: 800;
  letter-spacing: -0.04em;
  line-height: 0.95;
  margin-bottom: 5rem;
}

.footer-hero-link span {
  display: inline-flex;
  align-items: center;
  gap: 1.5rem;
  background: linear-gradient(135deg, #e65c00 0%, #f7c300 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  transition: all 0.3s ease;
}

.footer-arrow-icon {
  width: clamp(3.5rem, 9vw, 7.5rem);
  height: clamp(3.5rem, 9vw, 7.5rem);
  color: #f7c300;
  stroke: #f7c300;
  -webkit-text-fill-color: initial;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.3s ease;
}

.footer-hero-link:hover .footer-arrow-icon {
  transform: translate(14px, -14px);
  color: #e65c00;
  stroke: #e65c00;
}

.footer-meta-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 3rem;
  padding-bottom: 4rem;
  border-bottom: 1px solid var(--border-subtle);
}

.meta-label {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--text-muted);
  margin-bottom: 0.85rem;
}

.footer-social-links {
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
}

.footer-social-links a {
  font-size: 0.9375rem;
  color: var(--text-secondary);
  transition: color 0.2s ease;
}

.footer-social-links a:hover {
  color: var(--brand-orange);
}

.footer-bottom-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 2.5rem;
  font-size: 0.8125rem;
  color: var(--text-muted);
}

.status-badge-live {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--brand-yellow);
  letter-spacing: 0.08em;
}

html.light .status-badge-live {
  color: var(--brand-brown);
}

/* ==========================================================================
   CASE STUDY SUBPAGE & DEVICE MOCKUP STYLING
   ========================================================================== */
.page-hero {
  padding-top: 11.5rem;
  padding-bottom: 6rem;
}

.page-title {
  font-family: var(--font-display);
  font-size: clamp(2.5rem, 5.5vw, 4.25rem);
  font-weight: 800;
  letter-spacing: -0.035em;
  color: var(--text-primary);
  line-height: 1.12;
  margin-bottom: 1.5rem;
}

.page-description {
  font-size: 1.1875rem;
  color: var(--text-secondary);
  max-width: 48rem;
  line-height: 1.7;
}

.article-content {
  max-width: 840px;
  margin: 0 auto;
  font-size: 1.125rem;
  line-height: 1.85;
  color: var(--text-secondary);
}

.article-content h2 {
  font-family: var(--font-display);
  font-size: 2.15rem;
  font-weight: 800;
  letter-spacing: -0.025em;
  color: var(--text-primary);
  margin-top: 5rem;
  margin-bottom: 1.75rem;
  line-height: 1.25;
}

.article-content h3 {
  font-family: var(--font-display);
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-top: 3.5rem;
  margin-bottom: 1.25rem;
}

.article-content h4 {
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-top: 2rem;
  margin-bottom: 0.75rem;
}

.article-content p {
  margin-bottom: 2rem;
}

.article-content ul, 
.article-content ol {
  margin-bottom: 2.5rem;
  padding-left: 1.75rem;
}

.article-content li {
  margin-bottom: 0.85rem;
  line-height: 1.75;
}

.article-content strong {
  color: var(--text-primary);
}

.back-nav-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-mono);
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--brand-orange);
  margin-bottom: 2rem;
  transition: transform 0.2s ease;
}

.back-nav-btn:hover {
  transform: translateX(-3px);
  text-decoration: underline;
}

/* DEVICE ON PLAIN ORANGE STAGE */
.device-orange-stage {
  margin: 3.5rem 0 1.5rem;
  border-radius: var(--radius-xl);
  overflow: hidden;
  background: var(--brand-orange);
  padding: 3.5rem 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 20px 50px rgba(230, 92, 0, 0.25);
}

.device-stage-img {
  width: 100%;
  max-width: 1060px;
  height: auto;
  display: block;
}

.cs-meta-bar {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
  gap: 1.5rem;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1.5rem 2rem;
  margin-top: 2rem;
  margin-bottom: 3.5rem;
}

.cs-meta-item-label {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  text-transform: uppercase;
  color: var(--text-muted);
  letter-spacing: 0.08em;
  margin-bottom: 0.35rem;
}

.cs-meta-item-value {
  font-size: 0.9375rem;
  font-weight: 600;
  color: var(--text-primary);
}

.cs-warning-banner {
  display: flex;
  align-items: flex-start;
  gap: 0.85rem;
  background: rgba(247, 195, 0, 0.08);
  border: 1px solid rgba(247, 195, 0, 0.3);
  border-radius: var(--radius-md);
  padding: 1.15rem 1.65rem;
  margin: 1.5rem 0 2rem;
  font-size: 0.9375rem;
  color: var(--text-secondary);
}

.cs-resources-box {
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-medium);
  border-radius: var(--radius-lg);
  padding: 2rem 2.25rem;
  margin: 1.75rem 0 4rem;
  box-shadow: var(--shadow-sm);
}

.cs-resources-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 0.75rem;
}

.cs-resources-title {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-primary);
}

.cs-resources-title svg {
  color: var(--brand-orange);
}

.cs-resources-badge {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.25rem 0.65rem;
  border-radius: var(--radius-full);
  background: var(--brand-orange-light);
  color: var(--brand-orange);
  border: 1px solid var(--brand-orange);
}

.cs-resources-desc {
  font-size: 0.95rem;
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.cs-resources-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

@media (max-width: 768px) {
  .cs-resources-grid {
    grid-template-columns: 1fr;
  }
}

.cs-resource-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.15rem 1.25rem;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  transition: all 0.25s ease;
  text-decoration: none;
}

.cs-resource-item:hover {
  border-color: var(--brand-orange);
  background: var(--bg-surface-elevated);
  transform: translateY(-2px);
}

.cs-resource-icon {
  font-size: 1.35rem;
  flex-shrink: 0;
}

.cs-resource-info {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  flex-grow: 1;
}

.cs-resource-name {
  font-family: var(--font-display);
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.35;
}

.cs-resource-item:hover .cs-resource-name {
  color: var(--brand-orange);
}

.cs-resource-tag {
  font-family: var(--font-mono);
  font-size: 0.725rem;
  color: var(--text-muted);
}

.cs-resource-arrow {
  font-family: var(--font-mono);
  font-size: 1.1rem;
  color: var(--text-muted);
  transition: transform 0.2s ease, color 0.2s ease;
}

.cs-resource-item:hover .cs-resource-arrow {
  transform: translate(2px, -2px);
  color: var(--brand-orange);
}

.cs-insight-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 2.25rem 2.5rem;
  margin-bottom: 2rem;
  transition: border-color 0.25s ease;
}

.cs-insight-card:hover {
  border-color: var(--brand-orange);
}

.cs-insight-num {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--brand-orange);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 0.4rem;
}

.cs-insight-title {
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.75rem;
  line-height: 1.3;
}

.cs-insight-body {
  font-size: 1rem;
  color: var(--text-secondary);
  line-height: 1.7;
}

.cs-doc-link-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.85rem 1.65rem;
  border-radius: var(--radius-full);
  background: var(--brand-orange-light);
  border: 1px solid var(--brand-orange);
  color: var(--text-primary);
  font-family: var(--font-mono);
  font-size: 0.875rem;
  font-weight: 600;
  margin-top: 1.5rem;
  margin-bottom: 3.5rem;
  transition: all 0.25s ease;
}

.cs-doc-link-btn:hover {
  background: var(--brand-orange);
  color: #ffffff;
}

.cs-comparison-table {
  width: 100%;
  border-collapse: collapse;
  margin: 2rem 0 3.5rem;
  font-size: 0.9375rem;
}

.cs-comparison-table th, 
.cs-comparison-table td {
  padding: 1.15rem 1.25rem;
  border: 1px solid var(--border-subtle);
  text-align: left;
  line-height: 1.7;
}

.cs-comparison-table th {
  background: var(--bg-surface-elevated);
  font-family: var(--font-mono);
  font-size: 0.75rem;
  text-transform: uppercase;
  color: var(--brand-orange);
}

.cs-pillar-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.75rem;
  margin: 2.5rem 0 3.5rem;
}

.cs-pillar-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 1.75rem 2rem;
}

.cs-pillar-tag {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--brand-orange);
  margin-bottom: 0.45rem;
}

.cs-pillar-name {
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-primary);
}

/* ==========================================================================
   RESPONSIVE MEDIA QUERIES
   ========================================================================== */
@media (max-width: 1024px) {
  .work-grid,
  .labs-grid,
  .about-grid,
  .blog-grid-2col {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }

  .work-card {
    height: auto;
  }

  .device-orange-stage {
    padding: 2rem 1rem;
  }

  .footer-meta-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
}

@media (max-width: 768px) {
  /* Navigation */
  .nav-wrapper-outer {
    padding: 8px 0.75rem 0;
  }

  .nav-bar-inner {
    padding: 8px 12px;
  }

  .nav-brand {
    font-size: 0.95rem;
    gap: 0.35rem;
  }

  .nav-menu,
  .nav-say-hi-btn {
    display: none;
  }

  .mobile-menu-btn {
    display: flex;
  }

  /* Section Headers */
  .section-header {
    flex-direction: column;
    align-items: flex-start;
    text-align: left;
    gap: 0.6rem;
    margin-bottom: 2rem;
  }

  .section-title,
  .labs-title {
    font-size: clamp(2.1rem, 8vw, 2.75rem);
    line-height: 1.12;
  }

  .section-subtitle {
    max-width: 100%;
    font-size: 1rem;
    line-height: 1.55;
    text-align: left;
  }

  /* Hero Section */
  .hero-section {
    min-height: calc(100vh - 20px);
    padding-top: 5rem;
    padding-bottom: 2.75rem;
    justify-content: flex-end;
  }

  .hero-title {
    font-size: clamp(2.1rem, 8.2vw, 3rem);
    line-height: 1.1;
    max-width: 100%;
    margin-bottom: 1.5rem;
  }

  .hero-cta-group {
    width: 100%;
    display: flex;
    flex-direction: row;
    gap: 0.75rem;
  }

  .btn-primary-hero,
  .btn-secondary-hero {
    flex: 1;
    padding: 0.85rem 1rem;
    font-size: 0.9rem;
    justify-content: center;
    text-align: center;
  }

  /* Work Grid & Cards */
  .work-grid {
    grid-template-columns: 1fr;
    gap: 1.75rem;
    margin-top: 1.75rem;
  }

  .work-card {
    height: auto;
    border-radius: var(--radius-lg);
  }

  .work-card-media {
    height: 240px;
  }

  .work-card-meta {
    padding: 1.5rem 1.25rem 1.75rem;
    gap: 0.6rem;
  }

  .work-title {
    font-size: 1.25rem;
    line-height: 1.35;
  }

  .work-description {
    font-size: 0.925rem;
    line-height: 1.5;
  }

  .work-meta-header {
    font-size: 0.75rem;
  }

  /* Labs Section */
  .labs-grid {
    grid-template-columns: 1fr;
    gap: 1.75rem;
    margin-top: 1.75rem;
  }

  .lab-card {
    padding: 1.75rem 1.25rem 1.5rem;
  }

  .lab-phone-frame {
    max-width: 250px;
    height: 380px;
  }

  /* About Section */
  .section-about {
    padding: 4rem 0;
  }

  .scroll-color-text {
    font-size: clamp(1.35rem, 5.5vw, 1.85rem);
    line-height: 1.45;
  }

  .about-pills-row {
    gap: 0.5rem;
    margin-top: 1.5rem;
  }

  .about-badge-pill {
    font-size: 0.8rem;
    padding: 0.35rem 0.7rem;
  }

  .about-sidebar-text {
    font-size: 1.05rem;
    line-height: 1.6;
    margin-top: 1.5rem;
  }

  .about-cta-group {
    width: 100%;
    flex-direction: column;
    gap: 0.75rem;
  }

  .btn-about-primary,
  .btn-about-secondary {
    width: 100%;
    justify-content: center;
  }

  /* Page Headers for subpages */
  .page-hero {
    padding-top: 7rem;
    padding-bottom: 3.5rem;
  }

  .page-title {
    font-size: clamp(2rem, 7.8vw, 2.85rem);
    line-height: 1.15;
  }

  .page-description {
    font-size: 1.05rem;
    line-height: 1.6;
  }

  /* Blog Filter Tabs Horizontal Scroll */
  .blog-filter-tabs {
    overflow-x: auto;
    white-space: nowrap;
    padding-bottom: 0.5rem;
    -webkit-overflow-scrolling: touch;
    display: flex;
    gap: 0.5rem;
  }

  .blog-tab-btn {
    flex-shrink: 0;
  }

  /* Case study detail tables and pillars */
  .cs-comparison-table {
    display: block;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    white-space: nowrap;
  }

  .cs-pillar-grid {
    grid-template-columns: 1fr;
  }

  /* Footer */
  .footer-hero-link {
    font-size: clamp(2.75rem, 12vw, 5rem);
  }

  .footer-meta-grid {
    grid-template-columns: 1fr;
    gap: 1.75rem;
    padding: 2.5rem 0;
  }

  .footer-social-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem 1.25rem;
  }

  .footer-bottom-row {
    flex-direction: column;
    gap: 0.75rem;
    align-items: flex-start;
  }
}

@media (max-width: 480px) {
  .hero-title {
    font-size: 2rem;
  }

  .hero-cta-group {
    flex-direction: column;
  }

  .btn-primary-hero,
  .btn-secondary-hero {
    width: 100%;
  }

  .work-card-media {
    height: 200px;
  }
}
"""
    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print('style.css created successfully')

# -------------------------------------------------------------
# 2. JS GENERATOR
# -------------------------------------------------------------
def build_js():
    js = """/* ==========================================================================
   JENNIES DIGITAL - CORE JAVASCRIPT
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initPreloader();
  initThemeToggle();
  initScrollNav();
  initMobileMenu();
  initScrollColorText();
  initLiveClock();
  initCopyEmail();
  initBlogFilter();
});

/* Preloader Controller */
function initPreloader() {
  const preloader = document.getElementById('sitePreloader');
  const bar = document.getElementById('preloaderBar');
  const percent = document.getElementById('preloaderPercent');
  const status = document.getElementById('preloaderStatus');
  if (!preloader) return;

  let current = 0;
  let isReady = false;

  const interval = setInterval(() => {
    if (!isReady && current < 88) {
      current += Math.floor(Math.random() * 7) + 3;
      if (current > 88) current = 88;
    } else if (isReady) {
      current += 8;
      if (current >= 100) {
        current = 100;
        clearInterval(interval);
        if (bar) bar.style.width = '100%';
        if (percent) percent.innerText = '100%';
        if (status) status.innerText = 'READY';
        setTimeout(() => {
          preloader.classList.add('loaded');
        }, 250);
      }
    }
    if (bar) bar.style.width = current + '%';
    if (percent) percent.innerText = current + '%';
  }, 35);

  function markReady() {
    isReady = true;
  }

  if (document.readyState === 'complete') {
    markReady();
  } else {
    window.addEventListener('load', markReady);
  }

  // Safety fallback after 1.6s
  setTimeout(markReady, 1600);
}

/* Theme Manager */
function initThemeToggle() {
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  if (!themeToggleBtn) return;

  const savedTheme = localStorage.getItem('jd_theme');
  const isLight = savedTheme === 'light';
  
  if (isLight) {
    document.documentElement.classList.add('light');
  } else {
    document.documentElement.classList.remove('light');
  }
  updateThemeIcon(isLight);

  themeToggleBtn.addEventListener('click', () => {
    const currentlyLight = document.documentElement.classList.toggle('light');
    localStorage.setItem('jd_theme', currentlyLight ? 'light' : 'dark');
    updateThemeIcon(currentlyLight);
  });
}

function updateThemeIcon(isLight) {
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  if (!themeToggleBtn) return;
  themeToggleBtn.innerHTML = isLight
    ? `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`
    : `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4.5"></circle><line x1="12" y1="1.5" x2="12" y2="4"></line><line x1="12" y1="20" x2="12" y2="22.5"></line><line x1="4.22" y1="4.22" x2="6" y2="6"></line><line x1="18" y1="18" x2="19.78" y2="19.78"></line><line x1="1.5" y1="12" x2="4" y2="12"></line><line x1="20" y1="12" x2="22.5" y2="12"></line><line x1="4.22" y1="19.78" x2="6" y2="18"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`;
}

/* Seamless Scroll Nav Transition */
function initScrollNav() {
  const header = document.querySelector('.site-header');
  if (!header || header.classList.contains('subpage-nav')) return;

  function onScroll() {
    if (window.scrollY > 24) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* Mobile Menu */
function initMobileMenu() {
  const btn = document.getElementById('mobileMenuBtn');
  const overlay = document.getElementById('mobileNavOverlay');
  if (!btn || !overlay) return;

  btn.addEventListener('click', () => {
    const isOpen = overlay.classList.toggle('open');
    btn.innerHTML = isOpen
      ? `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>`
      : `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="3.5" y1="6.5" x2="20.5" y2="6.5"></line><line x1="3.5" y1="12" x2="20.5" y2="12"></line><line x1="3.5" y1="17.5" x2="20.5" y2="17.5"></line></svg>`;
  });
}

/* Scroll Color Text Reveal */
function initScrollColorText() {
  const container = document.getElementById('scrollColorTextContainer');
  if (!container) return;

  const rawText = container.innerText.trim();
  const words = rawText.split(/\\s+/);

  container.innerHTML = words.map((word, i) => {
    const cleanWord = word.toLowerCase().replace(/[^a-z0-9]/g, '');
    const prevClean = (words[i-1] || '').toLowerCase().replace(/[^a-z0-9]/g, '');
    const nextClean = (words[i+1] || '').toLowerCase().replace(/[^a-z0-9]/g, '');

    const isProductMarketing = (cleanWord === 'product' && nextClean === 'marketing') || (cleanWord === 'marketing' && prevClean === 'product');
    const isProductIdeas = (cleanWord === 'product' && nextClean === 'ideas') || (cleanWord === 'ideas' && prevClean === 'product');
    const isPMM = cleanWord === 'pmm';
    const isAI = cleanWord === 'ai';

    if (isProductMarketing || isProductIdeas || isPMM || isAI) {
      return `<span class="word brand-highlight">${word}</span>`;
    }
    return `<span class="word">${word}</span>`;
  }).join(' ');

  const wordSpans = container.querySelectorAll('.word');

  function update() {
    const rect = container.getBoundingClientRect();
    const windowHeight = window.innerHeight;
    const startOffset = windowHeight * 0.85;
    const endOffset = windowHeight * 0.25;
    const progress = Math.min(Math.max((startOffset - rect.top) / (startOffset - endOffset), 0), 1);
    const highlightCount = Math.floor(progress * wordSpans.length);

    wordSpans.forEach((span, i) => {
      span.classList.toggle('highlighted', i <= highlightCount);
    });
  }

  window.addEventListener('scroll', update, { passive: true });
  update();
}

/* Lagos Live Clock */
function initLiveClock() {
  const clock = document.getElementById('liveClockWidget');
  if (!clock) return;

  function tick() {
    const now = new Date();
    try {
      const timeStr = new Intl.DateTimeFormat('en-US', {
        timeZone: 'Africa/Lagos',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true
      }).format(now);
      clock.textContent = `Lagos (GMT+1): ${timeStr}`;
    } catch (e) {
      clock.textContent = 'Lagos, Nigeria (GMT+1)';
    }
  }

  tick();
  setInterval(tick, 1000);
}

/* Copy Email */
function initCopyEmail() {
  const btn = document.getElementById('copyEmailBtn');
  if (!btn) return;

  btn.addEventListener('click', (e) => {
    e.preventDefault();
    navigator.clipboard.writeText('hello@jenniesdigital.com').then(() => {
      const orig = btn.innerHTML;
      btn.innerHTML = '✓ Copied to clipboard!';
      setTimeout(() => {
        btn.innerHTML = orig;
      }, 2500);
    });
  });
}

/* Blog Filter for blog.html */
function initBlogFilter() {
  const tabs = document.querySelectorAll('.blog-tab-btn');
  const cards = document.querySelectorAll('.blog-static-card[data-category]');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const filter = tab.dataset.filter?.toLowerCase() || 'all';

      cards.forEach(card => {
        const cat = card.dataset.category?.toLowerCase() || '';
        if (filter === 'all' || cat === filter) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}
"""
    with open('assets/js/main.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print('main.js created successfully')

# -------------------------------------------------------------
# 3. NAVIGATION & FOOTER TEMPLATES
# -------------------------------------------------------------
def get_header(active_nav='home', root_prefix='', is_homepage=False):
    extra_class = '' if is_homepage else 'subpage-nav'
    return f"""  <!-- SITE PRELOADER -->
  <div id="sitePreloader" class="site-preloader" aria-hidden="true">
    <div class="preloader-content">
      <div class="preloader-logo-wrap">
        <img src="{root_prefix}assets/logo-transparent.png" alt="Logo" class="preloader-logo">
        <div class="preloader-pulse"></div>
      </div>
      <div class="preloader-brand">Jennies Digital</div>
      <div class="preloader-bar-wrap">
        <div id="preloaderBar" class="preloader-bar"></div>
      </div>
      <div class="preloader-meta">
        <span id="preloaderStatus" class="preloader-status">INITIALIZING</span>
        <span id="preloaderPercent" class="preloader-percent">0%</span>
      </div>
    </div>
  </div>

  <!-- NAVIGATION BAR (EXACT MICHAEL TSIRAKIS CLONE) -->
  <header class="site-header {extra_class}">
    <div class="nav-wrapper-outer">
      <div class="nav-bar-inner">
        <!-- Brand Logo & Name -->
        <a href="/" class="nav-brand" aria-label="Jennies Digital">
          <div class="nav-logo-wrap">
            <img src="{root_prefix}assets/logo-transparent.png" alt="Logo" class="nav-logo-img">
          </div>
          <span>Jennies Digital</span>
        </a>

        <!-- Center Menu -->
        <nav class="nav-menu" aria-label="Primary Navigation">
          <a href="/" class="nav-link {'active' if active_nav=='home' else ''}">Home</a>
          <a href="/work" class="nav-link {'active' if active_nav=='work' else ''}">Work</a>
          <a href="/lab" class="nav-link {'active' if active_nav=='lab' else ''}">Lab</a>
          <a href="/blog" class="nav-link {'active' if active_nav=='blog' else ''}">Blog</a>
          <a href="{root_prefix}assets/documents/JENNIFER%20OHAERI-EHIEM%20_%20PRODUCT%20MARKETING%20MANAGER.pdf" class="nav-link" target="_blank" rel="noopener noreferrer">Resume</a>
        </nav>

        <!-- Right Actions: Theme Toggle & Say Hi Pill Button -->
        <div class="nav-actions">
          <button type="button" id="themeToggleBtn" class="theme-toggle-btn" aria-label="Toggle theme" title="Toggle theme">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4.5"></circle><line x1="12" y1="1.5" x2="12" y2="4"></line><line x1="12" y1="20" x2="12" y2="22.5"></line><line x1="4.22" y1="4.22" x2="6" y2="6"></line><line x1="18" y1="18" x2="19.78" y2="19.78"></line><line x1="1.5" y1="12" x2="4" y2="12"></line><line x1="20" y1="12" x2="22.5" y2="12"></line><line x1="4.22" y1="19.78" x2="6" y2="18"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
          </button>

          <a href="/#contact" class="nav-say-hi-btn">
            <span>Say Hi</span>
            <span aria-hidden="true">👋</span>
          </a>

          <button type="button" id="mobileMenuBtn" class="mobile-menu-btn" aria-label="Open mobile menu">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="3.5" y1="6.5" x2="20.5" y2="6.5"></line><line x1="3.5" y1="12" x2="20.5" y2="12"></line><line x1="3.5" y1="17.5" x2="20.5" y2="17.5"></line></svg>
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Mobile Menu Overlay -->
  <div id="mobileNavOverlay" class="mobile-nav-overlay" aria-hidden="true">
    <a href="/" class="mobile-nav-link {'active' if active_nav=='home' else ''}">Home</a>
    <a href="/work" class="mobile-nav-link {'active' if active_nav=='work' else ''}">Work</a>
    <a href="/lab" class="mobile-nav-link {'active' if active_nav=='lab' else ''}">Lab</a>
    <a href="/blog" class="mobile-nav-link {'active' if active_nav=='blog' else ''}">Blog</a>
    <a href="{root_prefix}assets/documents/JENNIFER%20OHAERI-EHIEM%20_%20PRODUCT%20MARKETING%20MANAGER.pdf" class="mobile-nav-link" target="_blank" rel="noopener noreferrer">Resume</a>
    <a href="/#contact" class="mobile-nav-link">Say Hi 👋</a>
  </div>
"""

def get_footer(root_prefix=''):
    return f"""  <!-- FOOTER / CONTACT SECTION (COLORED SAY HELLO) -->
  <footer id="contact" class="site-footer">
    <div class="container-wide">
      <a href="mailto:hello@jenniesdigital.com" class="footer-hero-link">
        <span>
          Say hello
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="footer-arrow-icon"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
        </span>
      </a>

      <div class="footer-meta-grid">
        <div class="footer-meta-item">
          <div class="meta-label">Email</div>
          <a href="mailto:hello@jenniesdigital.com" id="copyEmailBtn" title="Click to copy email">
            hello@jenniesdigital.com
          </a>
        </div>

        <div class="footer-meta-item">
          <div class="meta-label">Elsewhere</div>
          <div class="footer-social-links">
            <a href="https://www.linkedin.com/in/jennifer-ohaeri-ehiem" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            <a href="https://x.com/jenniesdigital" target="_blank" rel="noopener noreferrer">Twitter (X)</a>
            <a href="https://www.instagram.com/jenniesdigital" target="_blank" rel="noopener noreferrer">Instagram</a>
            <a href="https://substack.com/@jenniesdigital" target="_blank" rel="noopener noreferrer">Substack</a>
          </div>
        </div>

        <div class="footer-meta-item">
          <div class="meta-label">Local Time &amp; Status</div>
          <p id="liveClockWidget">Lagos (GMT+1): Loading...</p>
        </div>
      </div>

      <div class="footer-bottom-row">
        <span>© 2026 Jennies Digital · Designed &amp; built with passion.</span>
        <span class="status-badge-live">
          🟢 Available for PMM roles and projects
        </span>
      </div>
    </div>
  </footer>
"""

# -------------------------------------------------------------
# 4. HOMEPAGE GENERATOR
# -------------------------------------------------------------
def build_index():
    header = get_header(active_nav='home', root_prefix='', is_homepage=True)
    footer = get_footer(root_prefix='')
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Jennies Digital — Jennifer | Product Marketing Manager for AI, SaaS and Tech Brands</title>
  <meta name="description" content="Hi, I'm Jennifer. Product Marketing Manager for AI, SaaS and Tech Brands.">
  <meta name="theme-color" content="#e65c00">
  <link rel="icon" type="image/png" href="assets/logo-transparent.png">

  <!-- Google Fonts: Bricolage Grotesque, Roboto, Geist Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,100,200..800&family=Geist+Mono:wght@400;500;600&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="assets/css/style.css">

  <script>
    (() => {{
      try {{
        const t = localStorage.getItem('jd_theme') || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
        if (t === 'light') document.documentElement.classList.add('light');
      }} catch (e) {{}}
    }})();
  </script>
</head>
<body>

{header}

  <main>
    <!-- HERO SECTION WITH REAL MP4 VIDEO ANIMATION -->
    <section id="home" class="hero-section">
      <div class="hero-bg-container">
        <div class="hero-character-stage">
          <video 
            id="heroVideo" 
            class="hero-character-video" 
            autoplay 
            muted 
            loop 
            playsinline 
            poster="assets/images/hero-poster.jpg">
            <source src="assets/images/new-hero-character.mp4" type="video/mp4">
          </video>
        </div>
        <div class="hero-ambient-glow"></div>
        <div class="hero-gradient-overlay"></div>
      </div>

      <!-- Hero Typography -->
      <div class="hero-content">
        <h1 class="hero-title">
          Hi, I'm <span class="title-accent">Jennifer</span>.<br>
          Product Marketing Manager for AI, SaaS and Tech Brands.
        </h1>

        <div class="hero-actions">
          <a href="#work" class="btn-primary-hero">
            <span>View my work</span>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"></path><path d="m19 12-7 7-7-7"></path></svg>
          </a>
          <a href="#about" class="btn-secondary-hero">
            About me
          </a>
        </div>
      </div>
    </section>

    <!-- SELECTED WORK SECTION -->
    <section id="work" class="section-work">
      <div class="container">
        <div class="section-header">
          <div>
            <span class="tag-label">Portfolio</span>
            <h2 class="section-title">Selected work</h2>
          </div>
          <p class="section-subtitle">
            Work I'm most proud of — landing pages, research studies, positioning, messaging, GTM campaigns and all the good stuff.
          </p>
        </div>

        <div class="work-grid">
          <!-- Case Study 1: Koppoh Finance -->
          <a href="/work/koppoh" class="work-card">
            <div class="work-card-media">
              <img src="assets/images/work-koppoh-ipad.png" alt="Launching Koppoh Finance Case Study" class="work-card-img" loading="lazy">
            </div>
            <div class="work-card-meta">
              <div class="work-meta-header">
                <span>FINANCE SAAS SME</span>
                <span>KOPPOH FINANCE</span>
              </div>
              <h3 class="work-title">
                Launching Koppoh Finance: A Product Marketing Strategy to Go From Product Concept to Go-to-Market
              </h3>
              <p class="work-description">
                A speculative product marketing case study exploring how Koppoh could launch a financing solution for African MSMEs.
              </p>
              <div class="work-metric-highlight">
                ⚡ Speculative / Mock Project
              </div>
            </div>
          </a>

          <!-- Case Study 2: WhatsApp Teams -->
          <a href="/work/whatsapp" class="work-card">
            <div class="work-card-media">
              <img src="assets/images/work-whatsapp-laptop.png" alt="WhatsApp Teams Case Study" class="work-card-img" loading="lazy">
            </div>
            <div class="work-card-meta">
              <div class="work-meta-header">
                <span>SAAS · B2B MESSAGING</span>
                <span>WHATSAPP TEAMS</span>
              </div>
              <h3 class="work-title">
                WhatsApp Teams: Turning the world's most familiar messaging app into lightweight team communication
              </h3>
              <p class="work-description">
                A product marketing case study on the possibility of WhatsApp spreading to new markets
              </p>
              <div class="work-metric-highlight">
                ⚡ Speculative / Mock Project
              </div>
            </div>
          </a>

          <!-- Case Study 3: OPay Positioning -->
          <a href="/work/opay" class="work-card">
            <div class="work-card-media">
              <img src="assets/images/work-opay-tablet.png" alt="OPay: Beyond Beyond Banking Case Study" class="work-card-img" loading="lazy">
            </div>
            <div class="work-card-meta">
              <div class="work-meta-header">
                <span>FINTECH · BRAND POSITIONING</span>
                <span>OPAY NIGERIA</span>
              </div>
              <h3 class="work-title">
                OPay: Beyond “Beyond Banking” - Reframing a super-app around the job it actually helps customers accomplish.
              </h3>
              <p class="work-description">
                What should OPay actually own in the market, and how should its homepage communicate that value more clearly?
              </p>
              <div class="work-metric-highlight">
                ⚡ Speculative / Mock Project
              </div>
            </div>
          </a>

          <!-- Case Study 4: Africa's Creator Monetisation Landscape -->
          <a href="/work/creator-monetisation" class="work-card">
            <div class="work-card-media">
              <img src="assets/images/work-creator-monetisation.png" alt="Africa's Creator Monetisation Landscape" class="work-card-img" loading="lazy">
            </div>
            <div class="work-card-meta">
              <div class="work-meta-header">
                <span>CREATOR ECONOMY · MARKET RESEARCH</span>
                <span>COMPETITIVE ANALYSIS</span>
              </div>
              <h3 class="work-title">
                Africa's Creator Monetisation Landscape
              </h3>
              <p class="work-description">
                A competitive analysis of four platforms shaping how African creators make money online.
              </p>
              <div class="work-metric-highlight">
                ⚡ Market Research · Competitive Intelligence
              </div>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- LABS SECTION -->
    <section id="labs" class="section-labs">
      <div class="container-wide">
        <div class="section-header">
          <div>
            <span class="tag-label">Labs</span>
            <h2 class="labs-title">
              Tools I built,<br>
              <span class="labs-accent">designed &amp; shipped.</span>
            </h2>
          </div>
          <p class="section-subtitle">
            Little experiments where I do it all - design, code, copy, and ship.
          </p>
        </div>

        <div class="labs-grid">
          <!-- Lab 1: CleanDesk -->
          <a href="/lab/cleandesk" class="lab-card">
            <div class="lab-phone-frame">
              <div class="lab-phone-inner">
                <img src="assets/images/lab-cleandesk.png" alt="CleanDesk App" loading="lazy">
              </div>
            </div>
            <div class="lab-app-title">
              <span>CleanDesk</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
            <p class="lab-app-desc">
              An AI-powered workspace that turns messy thoughts into organized, actionable work.
            </p>
            <div class="lab-app-tag">WEB APP · AI TOOL · 2026</div>
          </a>

          <!-- Lab 2: Soda Reader -->
          <a href="/lab/soda-reader" class="lab-card">
            <div class="lab-phone-frame">
              <div class="lab-phone-inner">
                <img src="assets/images/lab-soda.png" alt="Soda Reader App" loading="lazy">
              </div>
            </div>
            <div class="lab-app-title">
              <span>Soda Reader</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
            <p class="lab-app-desc">
              A reading app designed to make reading addictive again and help readers actually remember what they read.
            </p>
            <div class="lab-app-tag">WEB APP · AI READING · 2026</div>
          </a>

          <!-- Lab 3: ContentLabAI -->
          <a href="/lab/contentlabai" class="lab-card">
            <div class="lab-phone-frame">
              <div class="lab-phone-inner">
                <img src="assets/images/lab-contentlabai.png" alt="ContentLabAI App" loading="lazy">
              </div>
            </div>
            <div class="lab-app-title">
              <span>ContentLabAI</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
            <p class="lab-app-desc">
              An AI content workflow that turns one idea into platform-ready content in my voice.
            </p>
            <div class="lab-app-tag">AI WORKFLOW · CONTENT STUDIO · 2026</div>
          </a>
        </div>
      </div>
    </section>

    <!-- ABOUT SECTION -->
    <section id="about" class="section-about">
      <div class="container">
        <span class="tag-label">About</span>

        <div class="about-grid">
          <div>
            <div id="scrollColorTextContainer" class="scroll-color-text">
              My friends call me Jennie. I’m the kind of person who sees a product and immediately starts wondering, Why would anyone choose to use this? That curiosity is what led me to product marketing. When I’m not being a PMM, I’m usually experimenting with AI, building random product ideas, learning something new, or reading a book I probably didn’t need to buy... again.
            </div>

            <div class="about-pills-row">
              <span class="about-badge-pill">📍 Global Remote</span>
              <span class="about-badge-pill">🚀 2+ Years in Marketing</span>
              <span class="about-badge-pill">☕ 3 Energy Drinks deep</span>
              <span class="about-badge-pill">📈 Highly Motivated</span>
              <span class="about-badge-pill">🌍 Law, Tech &amp; AI</span>
            </div>
          </div>

          <div>
            <p class="about-sidebar-text">
              I think of Product Marketing less like descriptive copywriting and more like cognitive architecture. The most enduring products win because their mere being and messaging creates immediate clarity in a noisy world.
            </p>

            <div class="about-cta-group">
              <a href="#contact" class="btn-about-primary">
                <span>Let's talk</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
              </a>
              <a href="assets/documents/JENNIFER%20OHAERI-EHIEM%20_%20PRODUCT%20MARKETING%20MANAGER.pdf" class="btn-about-secondary" target="_blank" rel="noopener noreferrer">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 15V3"></path><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><path d="m7 10 5 5 5-5"></path></svg>
                <span>Download resume</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SUBJECT MATTER (BLOG SECTION) -->
    <section id="blog" class="section-blog">
      <div class="container">
        <div class="section-header">
          <div>
            <span class="tag-label">Blog &amp; Insights</span>
            <h2 class="section-title">Subject Matter</h2>
          </div>
          <p class="section-subtitle">
            My perspectives on technology, business, law, people, and things I find remotely interesting.
          </p>
        </div>

        <div class="blog-grid-2col">
          <!-- Latest Article 1 -->
          <article class="blog-static-card" data-category="Technology">
            <div>
              <div class="blog-card-top">
                <div class="blog-badges-wrap">
                  <span class="blog-category-badge">Technology</span>
                  <span class="blog-format-tag">Essay</span>
                </div>
                <span class="blog-read-time">August 2026 · 6 min read</span>
              </div>
              <h3 class="blog-card-title">
                <a href="/blog/the-death-of-feature-first-messaging" class="blog-title-link">The Death of Feature-First Messaging: How to Position AI Products in 2026</a>
              </h3>
              <p class="blog-card-excerpt">
                Why listing parameter counts and latency benchmark numbers fails to convert enterprise buyers, and how leading AI companies structure their narrative around business cognitive leverage.
              </p>
            </div>
            <div class="blog-card-footer">
              <a href="/blog/the-death-of-feature-first-messaging" class="read-more-link">
                Full read
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
              </a>
            </div>
          </article>

          <!-- Latest Article 2 -->
          <article class="blog-static-card" data-category="Business">
            <div>
              <div class="blog-card-top">
                <div class="blog-badges-wrap">
                  <span class="blog-category-badge">Business</span>
                  <span class="blog-format-tag">Research</span>
                </div>
                <span class="blog-read-time">July 2026 · 8 min read</span>
              </div>
              <h3 class="blog-card-title">
                <a href="/blog/why-most-ai-saas-launches-fail" class="blog-title-link">Why Most AI SaaS Launches Fail: The Zero-to-One GTM Playbook</a>
              </h3>
              <p class="blog-card-excerpt">
                Deconstructing the common pitfalls of AI launches and the exact 5-stage framework to guarantee day-one traction, press coverage, and enterprise pipeline generation.
              </p>
            </div>
            <div class="blog-card-footer">
              <a href="/blog/why-most-ai-saas-launches-fail" class="read-more-link">
                Full read
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
              </a>
            </div>
          </article>
        </div>

        <div class="blog-view-all-cta">
          <a href="/blog" class="btn-secondary-hero">
            <span>View all Subject Matter articles</span>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-left: 0.4rem;"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </a>
        </div>
      </div>
    </section>
  </main>

{footer}

  <script src="assets/js/main.js"></script>
</body>
</html>
"""
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('index.html created successfully')

# -------------------------------------------------------------
# 5. WORK PAGES & DEDICATED CASE STUDIES (KOPPOH, WHATSAPP, OPAY)
# -------------------------------------------------------------
def build_work_pages():
    header = get_header(active_nav='work', root_prefix='')
    footer = get_footer(root_prefix='')

    html_work = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Selected Work — Jennies Digital</title>
  <link rel="icon" type="image/png" href="assets/logo-transparent.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,100,200..800&family=Geist+Mono:wght@400;500;600&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
  <script>
    (() => {{
      try {{
        const t = localStorage.getItem('jd_theme') || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
        if (t === 'light') document.documentElement.classList.add('light');
      }} catch (e) {{}}
    }})();
  </script>
</head>
<body>
{header}

  <main class="page-hero">
    <div class="container">
      <span class="tag-label">Portfolio</span>
      <h1 class="page-title">Selected Work</h1>
      <p class="page-description">
        Dive into a collection of my best work.
      </p>

      <div class="work-grid" style="margin-top: 3.5rem;">
        <!-- Koppoh Finance -->
        <a href="/work/koppoh" class="work-card">
          <div class="work-card-media">
            <img src="assets/images/work-koppoh-ipad.png" alt="Launching Koppoh Finance" class="work-card-img">
          </div>
          <div class="work-card-meta">
            <div class="work-meta-header">
              <span>FINANCE SAAS SME</span>
              <span>KOPPOH FINANCE</span>
            </div>
            <h3 class="work-title">
              Launching Koppoh Finance: A Product Marketing Strategy to Go From Product Concept to Go-to-Market
            </h3>
            <p class="work-description">
              A speculative product marketing case study exploring how Koppoh could launch a financing solution for African MSMEs.
            </p>
            <div class="work-metric-highlight">⚡ Speculative / Mock Project</div>
          </div>
        </a>

        <!-- WhatsApp Teams -->
        <a href="/work/whatsapp" class="work-card">
          <div class="work-card-media">
            <img src="assets/images/work-whatsapp-laptop.png" alt="WhatsApp Teams" class="work-card-img">
          </div>
          <div class="work-card-meta">
            <div class="work-meta-header">
              <span>SAAS · B2B MESSAGING</span>
              <span>WHATSAPP TEAMS</span>
            </div>
            <h3 class="work-title">
              WhatsApp Teams: Turning the world's most familiar messaging app into lightweight team communication
            </h3>
            <p class="work-description">
              A product marketing case study on the possibility of WhatsApp spreading to new markets
            </p>
            <div class="work-metric-highlight">⚡ Speculative / Mock Project</div>
          </div>
        </a>

        <!-- OPay Positioning -->
        <a href="/work/opay" class="work-card">
          <div class="work-card-media">
            <img src="assets/images/work-opay-tablet.png" alt="OPay: Beyond Beyond Banking" class="work-card-img">
          </div>
          <div class="work-card-meta">
            <div class="work-meta-header">
              <span>FINTECH · BRAND POSITIONING</span>
              <span>OPAY NIGERIA</span>
            </div>
            <h3 class="work-title">
              OPay: Beyond “Beyond Banking” - Reframing a super-app around the job it actually helps customers accomplish.
            </h3>
            <p class="work-description">
              What should OPay actually own in the market, and how should its homepage communicate that value more clearly?
            </p>
            <div class="work-metric-highlight">⚡ Speculative / Mock Project</div>
          </div>
        </a>

        <!-- Case Study 4: Africa's Creator Monetisation Landscape -->
        <a href="/work/creator-monetisation" class="work-card">
          <div class="work-card-media">
            <img src="assets/images/work-creator-monetisation.png" alt="Africa's Creator Monetisation Landscape" class="work-card-img">
          </div>
          <div class="work-card-meta">
            <div class="work-meta-header">
              <span>CREATOR ECONOMY · MARKET RESEARCH</span>
              <span>COMPETITIVE ANALYSIS</span>
            </div>
            <h3 class="work-title">
              Africa's Creator Monetisation Landscape
            </h3>
            <p class="work-description">
              A competitive analysis of four platforms shaping how African creators make money online.
            </p>
            <div class="work-metric-highlight">⚡ Market Research · Competitive Intelligence</div>
          </div>
        </a>
      </div>
    </div>
  </main>

{footer}
  <script src="assets/js/main.js"></script>
</body>
</html>
"""
    with open('work.html', 'w', encoding='utf-8') as f:
        f.write(html_work)

    h_cs = get_header(active_nav='work', root_prefix='../', is_homepage=False)
    ft_cs = get_footer(root_prefix='../')

    # -------------------------------------------------------------
    # DEDICATED OPAY CASE STUDY PAGE
    # -------------------------------------------------------------
    opay_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>OPay: Beyond “Beyond Banking” — Jennies Digital</title>
  <meta name="description" content="Reframing a super-app around the job it actually helps customers accomplish.">
  <link rel="icon" type="image/png" href="../assets/logo-transparent.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,100,200..800&family=Geist+Mono:wght@400;500;600&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <script>
    (() => {{
      try {{
        const t = localStorage.getItem('jd_theme') || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
        if (t === 'light') document.documentElement.classList.add('light');
      }} catch (e) {{}}
    }})();
  </script>
</head>
<body>
{h_cs}

  <main class="page-hero">
    <div class="container">
      <div>
        <a href="/work" class="back-nav-btn">← Back to Selected Work</a>
      </div>

      <div class="cs-header" style="margin-top: 1rem; margin-bottom: 3.5rem;">
        <span class="tag-label">FINTECH · BRAND POSITIONING · OPAY NIGERIA</span>
        <h1 class="page-title" style="font-size: clamp(2.35rem, 4.8vw, 3.75rem); max-width: 960px; margin-top: 0.5rem; margin-bottom: 1.5rem;">
          OPay: Beyond “Beyond Banking” - Reframing a super-app around the job it actually helps customers accomplish.
        </h1>
        <p class="page-description" style="font-size: 1.25rem; max-width: 780px;">
          What should OPay actually own in the market, and how should its homepage communicate that value more clearly?
        </p>
      </div>

      <!-- METADATA BAR -->
      <div class="cs-meta-bar">
        <div>
          <div class="cs-meta-item-label">Role</div>
          <div class="cs-meta-item-value">Product Marketing Manager</div>
        </div>
        <div>
          <div class="cs-meta-item-label">Project Type</div>
          <div class="cs-meta-item-value">Speculative / Mock</div>
        </div>
        <div>
          <div class="cs-meta-item-label">Industry</div>
          <div class="cs-meta-item-value">Fintech</div>
        </div>
        <div>
          <div class="cs-meta-item-label">Market</div>
          <div class="cs-meta-item-value">Nigeria</div>
        </div>
        <div>
          <div class="cs-meta-item-label">Scope</div>
          <div class="cs-meta-item-value">Research · Messaging · Copywriting · Landing Page Rewrite</div>
        </div>
      </div>

      <!-- 3D TURNED TABLET MOCKUP ON PLAIN ORANGE BACKGROUND -->
      <div class="device-orange-stage">
        <img src="../assets/images/work-opay-tablet.png" alt="OPay on 3D Tablet Mockup" class="device-stage-img">
      </div>

      <!-- DISCLAIMER BANNER DIRECTLY UNDER THE PHOTO -->
      <div class="cs-warning-banner">
        <span style="font-size: 1.35rem;">⚠️</span>
        <span><strong>Disclaimer:</strong> Please note that this is just a mock project and is not affiliated with the brand itself.</span>
      </div>

      <!-- RESOURCES SECTION (OFFICIAL PLATFORM & MOCK REDESIGN) -->
      <div class="cs-resources-box">
        <div class="cs-resources-header">
          <div class="cs-resources-title">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            <span>Project Resources &amp; Live Links</span>
          </div>
          <span class="cs-resources-badge">2 Resources</span>
        </div>
        <p class="cs-resources-desc">Compare the original live OPay platform with the interactive redesigned homepage prototype:</p>
        
        <div class="cs-resources-grid">
          <a href="https://www.opayweb.com/" target="_blank" rel="noopener noreferrer" class="cs-resource-item">
            <div class="cs-resource-icon">🌐</div>
            <div class="cs-resource-info">
              <span class="cs-resource-name">OPay Official Website &amp; App</span>
              <span class="cs-resource-tag">Live Platform · Baseline Product (opayweb.com)</span>
            </div>
            <span class="cs-resource-arrow">↗</span>
          </a>

          <a href="https://opay-nigeria-mock.vercel.app/" target="_blank" rel="noopener noreferrer" class="cs-resource-item" style="border-color: var(--brand-orange); background: var(--brand-orange-light);">
            <div class="cs-resource-icon">🚀</div>
            <div class="cs-resource-info">
              <span class="cs-resource-name" style="color: var(--brand-orange);">Rewritten OPay Mock Landing Page</span>
              <span class="cs-resource-tag">Live Prototype · Positioning Redesign (opay-nigeria-mock.vercel.app)</span>
            </div>
            <span class="cs-resource-arrow" style="color: var(--brand-orange);">↗</span>
          </a>
        </div>
      </div>

      <!-- EDITORIAL CONTENT -->
      <div class="article-content" style="margin-top: 2rem;">
        
        <h2>01. The challenge</h2>
        <p>
          OPay’s homepage features its popular tagline, “Beyond Banking”. And this makes sense for us, the long-time users of this product, but for someone who has never come across the app before, "Beyond Banking" is… too broad. And this is a problem. So I asked: <em>what should OPay actually own in the customer's mind, and how should its homepage communicate that value more clearly?</em>
        </p>
        <p>
          You see, OPay is Nigeria's largest mobile money operator with <strong>50M+ users, $358B in annual transaction value, and $536M in revenue</strong>. The product works. The scale is undeniable.
        </p>
        <p>
          But its homepage leads with "We are Beyond Banking," a positioning that tells you what OPay is not (a bank) without telling you what it is.
        </p>
        <p>
          The question now isn't whether OPay is a good product. The question is whether OPay's messaging helps a new visitor understand that it is, and why they should choose it.
        </p>
        <p>So I did some digging.</p>

        <h2>02. Product Context</h2>
        
        <h3>What is OPay (for the newbies)?</h3>
        <p>
          OPay Digital Services Limited is a fintech company focused on financial services for Nigeria's mass market. It was co-founded in 2017 by Opera (the Norwegian browser company, now NASDAQ-listed as OPRA) and Balder Investment Inc. Its origins trace back to PayCom, a small mobile money platform incubated by Telnet Nigeria since 2007 in response to CBN's push for mobile money. Opera acquired a controlling stake in PayCom in 2018, rebranded it as OPay, and launched in August 2018.
        </p>

        <h3>What does it offer?</h3>
        <div style="overflow-x: auto;">
          <table class="cs-comparison-table">
            <thead>
              <tr>
                <th>Consumer Products</th>
                <th>Merchant / Business</th>
                <th>Infrastructure</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>
                  • Digital wallet &amp; transfers<br>
                  • Bill payments (electricity, cable, airtime)<br>
                  • Debit cards (Verve, Visa, Mastercard)<br>
                  • OWealth (SEC-regulated MMF)<br>
                  • Savings (SafeBox, Spend &amp; Save, Fixed)<br>
                  • OKash / OPay Credit (nano-loans)
                </td>
                <td>
                  • POS terminals (900K+ dispatched)<br>
                  • Business app (inventory, settlement)<br>
                  • Mini POS for mobile agents<br>
                  • Merchant subscriptions<br>
                  • QR payments
                </td>
                <td>
                  • 2M+ agent service points<br>
                  • USSD banking (*955#)<br>
                  • NIBSS NIP interbank rails
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>Where does it operate?</h3>
        <p>
          Nigeria (88% of revenue), Indonesia (10%), Egypt (1.6%), Pakistan. CBN Mobile Money Operator + Microfinance Bank licenses. National license upgraded in January 2026.
        </p>

        <h3>What does OPay appear to want to become?</h3>
        <p>
          OPay's stated ambition is <strong>1 billion users, 10 million merchants, 1 million jobs by 2031</strong>. Its tagline, "Beyond Banking" shows it positioning itself not as a bank but as comprehensive digital financial infrastructure. Its CEO describes the mission: <em>"We are not just processing payments; we are driving financial inclusion at scale."</em> The company calls this its "Frontier Manifesto," positioning OPay as foundational economic infrastructure aligned with Nigeria's goal of a $1T GDP by 2030.
        </p>

        <h2>03. Messaging Audit</h2>
        <p>I did a deep audit of its current homepage.</p>

        <h3>Homepage Teardown</h3>
        <div style="overflow-x: auto;">
          <table class="cs-comparison-table">
            <thead>
              <tr>
                <th>Section</th>
                <th>What OPay currently says</th>
                <th>My observation</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Hero headline</strong></td>
                <td>"We are Beyond Banking"</td>
                <td>Tells you what OPay isn't (a bank). Doesn't tell you what it is or why you should care.</td>
              </tr>
              <tr>
                <td><strong>Subheadline</strong></td>
                <td>"With a mission to make financial services more inclusive through technology, OPay is dedicated to providing secure, easy-to-use &amp; affordable financial services. We offer super-fast user experience, amazing incentive packages on transfers and airtime/data top-ups, innovative products that earn amazing daily interest on your balance, reliable debit card with no charges, and the best resolution experience."</td>
                <td>Generic. Every fintech claims "secure, easy, affordable." No differentiation.</td>
              </tr>
              <tr>
                <td><strong>Extended subheadline</strong></td>
                <td>"...your one-stop payment services platform and more"</td>
                <td>A feature list disguised as a positioning statement.</td>
              </tr>
              <tr>
                <td><strong>Products</strong></td>
                <td>Three cards: Fund/Transfer/Pay Bills, Debit Card, OWealth</td>
                <td>Organized by feature, not by customer need. Missing: agent network, business tools, USSD.</td>
              </tr>
              <tr>
                <td><strong>Trust signals</strong></td>
                <td>CBN license badge, NDIC insurance</td>
                <td>Legitimate but standard. Every licensed fintech has these.</td>
              </tr>
              <tr>
                <td><strong>Security section</strong></td>
                <td>"Your Security and Privacy are our priority" — fraud protection, PCI DSS, account locking</td>
                <td>Standard industry language. No proof that OPay is more secure than alternatives.</td>
              </tr>
              <tr>
                <td><strong>Customer service</strong></td>
                <td>"We are here to provide 24/7 quick customer service"</td>
                <td>Directly contradicted by customer evidence. Support is the #1 complaint gathered from OPay users. Promising this without proof damages credibility.</td>
              </tr>
              <tr>
                <td><strong>CTA</strong></td>
                <td>App Store + Google Play download buttons, QR code</td>
                <td>App download is the obvious action, but no reason why to download vs. competitors.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>After auditing the home page, I ran the 5-Second Test</h3>
        <p>Can a new visitor immediately understand:</p>
        <table class="cs-comparison-table">
          <thead>
            <tr>
              <th>Question</th>
              <th>Answer</th>
              <th>Verdict</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>What is this?</td>
              <td>"Beyond Banking" vague</td>
              <td><span style="color: #ff4d4d; font-weight: 700;">Weak</span></td>
            </tr>
            <tr>
              <td>Who is it for?</td>
              <td>Unclear, no audience signal</td>
              <td><span style="color: #ff4d4d; font-weight: 700;">Weak</span></td>
            </tr>
            <tr>
              <td>What problem does it solve?</td>
              <td>Implied: financial services, but vague</td>
              <td><span style="color: #ff4d4d; font-weight: 700;">Weak</span></td>
            </tr>
            <tr>
              <td>Why should I choose it?</td>
              <td>"Secure, easy, affordable" could be anyone</td>
              <td><span style="color: #ff4d4d; font-weight: 700;">Weak</span></td>
            </tr>
            <tr>
              <td>What should I do next?</td>
              <td>Download the app</td>
              <td><span style="color: var(--brand-yellow); font-weight: 700;">Passable</span></td>
            </tr>
          </tbody>
        </table>
        <p><strong>Score: 1/5.</strong> A new visitor would struggle to articulate why OPay exists or why it's different from PalmPay, Kuda, or Moniepoint.</p>

        <h3>What works vs. What doesn't</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin: 2rem 0 3.5rem;">
          <div style="background: var(--bg-surface-elevated); padding: 1.75rem; border-radius: var(--radius-md); border-left: 4px solid #22c55e;">
            <strong style="color: #22c55e;">What works:</strong>
            <ul style="margin-top: 1rem; margin-bottom: 0; padding-left: 1.2rem; font-size: 0.9375rem;">
              <li>CBN license + NDIC badge provide legitimate trust signals</li>
              <li>App store ratings (4.5/5 on Google Play, 1.1M+ ratings) provide implicit social proof</li>
              <li>Product cards are clean and visually clear</li>
              <li>Security section exists (even if generic)</li>
            </ul>
          </div>

          <div style="background: var(--bg-surface-elevated); padding: 1.75rem; border-radius: var(--radius-md); border-left: 4px solid #ef4444;">
            <strong style="color: #ef4444;">What doesn't:</strong>
            <ul style="margin-top: 1rem; margin-bottom: 0; padding-left: 1.2rem; font-size: 0.9375rem;">
              <li>"Beyond Banking" communicates nothing about customer value</li>
              <li>No audience signal — doesn't speak to consumers or businesses</li>
              <li>No competitive differentiation ("secure, easy, affordable")</li>
              <li>Missing OPay's actual moat: the agent network, offline capability, speed</li>
              <li>Contradicts customer experience (claims "24/7 quick customer service")</li>
              <li>No personality, no cultural resonance, no Nigerian voice</li>
              <li>Products organized by feature, not by customer job</li>
            </ul>
          </div>
        </div>

        <h2>04. Customer &amp; Competitive Research</h2>
        <p>I looked at what users are actually saying in order to figure out what would ultimately resonate with them.</p>

        <h3>What Real Customers Say</h3>
        <p>
          Research across 30+ sources (Google Play 1.1M+ ratings, Apple App Store 301K ratings, Trustpilot 93 reviews, PissedConsumer 7.9K reviews, Nairaland, X/Twitter, court records, CBN regulatory data) reveals:
        </p>

        <div style="overflow-x: auto;">
          <table class="cs-comparison-table">
            <thead>
              <tr>
                <th>Customer evidence</th>
                <th>Theme</th>
                <th>The implication</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>"Fast payments and settlement, I like my experience" 135+ Liners.com reviews mention "fast transfers"</td>
                <td><strong>Speed</strong></td>
                <td>OPay's #1 equity is transaction speed. This is the strongest brand association.</td>
              </tr>
              <tr>
                <td>"This is one bank app I use for day to day transactions because they are swift, efficient and reliable"</td>
                <td><strong>Daily driver</strong></td>
                <td>OPay has achieved "default financial app" status for millions.</td>
              </tr>
              <tr>
                <td>"OPay has been saving guys from unwarranted deductions from the commercial banks for years"</td>
                <td><strong>Anti-bank sentiment</strong></td>
                <td>OPay grows partly because users are fleeing bank frustration.</td>
              </tr>
              <tr>
                <td>"OPay is the go-to app for instant transfers, bill payments, and everyday transactions"</td>
                <td><strong>Default utility</strong></td>
                <td>OPay is perceived as infrastructure, like electricity, you notice it when it fails.</td>
              </tr>
              <tr>
                <td>"Customer service is very poor but the network is superb" viral X/Twitter quote, Aug 2026</td>
                <td><strong>Speed-support gap</strong></td>
                <td>The product works brilliantly. The support doesn't. This is OPay's core brand tension.</td>
              </tr>
              <tr>
                <td>"Absolute crooks, scammers with the worst customer service EVER. They are currently holding on to over 250k of my money" Trustpilot</td>
                <td><strong>Support failure</strong></td>
                <td>When money is stuck, users describe OPay with criminal language.</td>
              </tr>
              <tr>
                <td>"My account has been restricted for absolutely no reason and they're asking me to get a court order" X/Twitter, Aug 2026</td>
                <td><strong>Account freezes</strong></td>
                <td>3 Federal High Court judgments found OPay acted illegally in freezing accounts.</td>
              </tr>
              <tr>
                <td>"I'll always rate them over all these thieves commercial banks. Opay is a testament that all other banks can be stress free"</td>
                <td><strong>OPay vs banks</strong></td>
                <td>OPay's primary comparison set is traditional banks, not other fintechs.</td>
              </tr>
              <tr>
                <td>"OPay bu baba" (OPay is the boss) Nairaland user</td>
                <td><strong>Cultural endorsement</strong></td>
                <td>Deep Nigerian slang endorsement. OPay has cultural presence.</td>
              </tr>
              <tr>
                <td>"Use OPay for what it is: Nigeria's most accessible daily financial tool. Do not use it as your only financial tool" Brands.ng</td>
                <td><strong>Essential but incomplete</strong></td>
                <td>Sophisticated users see OPay as necessary but insufficient, needs pairing with a "real bank."</td>
              </tr>
              <tr>
                <td>Agent network described as "practical banking branches" in areas without bank branches</td>
                <td><strong>Financial inclusion</strong></td>
                <td>OPay agents fill real infrastructure gaps. This is not convenience; it's access.</td>
              </tr>
              <tr>
                <td>"Smart play in 2026: use Kuda as your bank, PalmPay for rewards, OPay as backup for agent cash-out and USSD" — divplanet</td>
                <td><strong>Multi-app strategy</strong></td>
                <td>OPay's competitive position is "best at one specific job," not "best overall."</td>
              </tr>
              <tr>
                <td>4.5/5 on Google Play (millions of happy daily users) vs. 2.4/5 on Trustpilot (users who hit failure modes)</td>
                <td><strong>Dual reality</strong></td>
                <td>Two different OPays exist: everyday use = excellent; problem resolution = terrible.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div style="background: var(--bg-surface-elevated); border-left: 4px solid var(--brand-orange); padding: 2rem 2.25rem; border-radius: 0 var(--radius-lg) var(--radius-lg) 0; margin: 2.5rem 0 3.5rem;">
          <div class="cs-meta-item-label" style="color: var(--brand-orange); font-weight: 700; margin-bottom: 0.5rem;">My Key Customer Finding</div>
          <p style="font-size: 1.15rem; font-weight: 500; color: var(--text-primary); margin: 0; line-height: 1.7;">
            OPay's product works brilliantly 99% of the time. Transaction speed is the #1 praised attribute. When the 1% fails—card disputes, account freezes, device lockouts—there is no reliable path to resolution. The gap between product performance and support quality is OPay's most dangerous competitive vulnerability.
          </p>
          <p style="font-size: 1rem; color: var(--text-secondary); margin-top: 1rem; margin-bottom: 0;">
            This paradox is the single most important insight from the research. It means OPay cannot credibly claim "we're here for you" or "24/7 support" when the evidence contradicts it. But it can credibly own speed, scale, and accessibility.
          </p>
        </div>

        <h3>What Customers Actually Use OPay For</h3>
        <table class="cs-comparison-table">
          <thead>
            <tr>
              <th>Use case</th>
              <th>Evidence strength</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>P2P transfers to family/friends across Nigeria</td>
              <td><strong>HIGH</strong> — original and remaining core use case</td>
            </tr>
            <tr>
              <td>Daily spending (bills, airtime, data)</td>
              <td><strong>HIGH</strong> — consistent across all sources</td>
            </tr>
            <tr>
              <td>POS/agent cash-in/cash-out</td>
              <td><strong>HIGH</strong> — fills real infrastructure gap for unbanked</td>
            </tr>
            <tr>
              <td>Small business payments (QR, POS)</td>
              <td><strong>MODERATE</strong> — growing but secondary</td>
            </tr>
            <tr>
              <td>Savings (OWealth, SafeBox)</td>
              <td><strong>MODERATE</strong> — noticed but not primary reason to join</td>
            </tr>
            <tr>
              <td>Credit (OKash)</td>
              <td><strong>GROWING</strong> — 4.6M quarterly borrowers, but collection practices damage brand</td>
            </tr>
          </tbody>
        </table>

        <h3>Competitive Messaging Map</h3>
        <div style="overflow-x: auto;">
          <table class="cs-comparison-table">
            <thead>
              <tr>
                <th>Dimension</th>
                <th>OPay</th>
                <th>PalmPay</th>
                <th>Moniepoint</th>
                <th>Kuda</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Category claim</strong></td>
                <td>"Beyond Banking"</td>
                <td>"Nigeria's leading digital bank"</td>
                <td>"Africa's fastest growing financial institution"</td>
                <td>"The digital bank built for Nigerians"</td>
              </tr>
              <tr>
                <td><strong>Hero message</strong></td>
                <td>"We are Beyond Banking"</td>
                <td>"Say yes to more"</td>
                <td>"Simple solutions to power your business"</td>
                <td>"More from your money, More for your life"</td>
              </tr>
              <tr>
                <td><strong>Target audience</strong></td>
                <td>Unclear</td>
                <td>Mass-market consumers</td>
                <td>Business owners/merchants</td>
                <td>Young, digitally-savvy Nigerians</td>
              </tr>
              <tr>
                <td><strong>Core promise</strong></td>
                <td>Secure, easy, affordable</td>
                <td>Reliable + rewarding</td>
                <td>All-in-one business toolkit</td>
                <td>Fee-free banking + more from money</td>
              </tr>
              <tr>
                <td><strong>Key differentiator</strong></td>
                <td>Scale (60M users) but not featured</td>
                <td>99.95% reliability + cashback</td>
                <td>Pidgin voice + business-first</td>
                <td>Direct comparison to traditional banks</td>
              </tr>
              <tr>
                <td><strong>Tone</strong></td>
                <td>Corporate, generic</td>
                <td>Confident, aspirational</td>
                <td>Pragmatic, Pidgin-inflected</td>
                <td>Clean, modern, aspirational</td>
              </tr>
              <tr>
                <td><strong>Primary CTA</strong></td>
                <td>Download app (QR code)</td>
                <td>Download app</td>
                <td>"Open an Account"</td>
                <td>"Download Kuda"</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>Where Each Competitor Wins</h3>
        <ul>
          <li><strong>PalmPay:</strong> Reliability + rewards. Claims a 99.95% success rate. Cashback as acquisition engine.</li>
          <li><strong>Moniepoint:</strong> Business-first identity. Only major fintech that speaks Pidgin. Owns the merchant story.</li>
          <li><strong>Kuda:</strong> Fee-free banking + lifestyle positioning. Direct comparison table against traditional banks. Premium tier for engaged users.</li>
          <li><strong>OPay:</strong> Scale + physical infrastructure. 60M users. 2M+ agents. But messaging doesn't communicate this.</li>
        </ul>

        <h3>White Space in the Market</h3>
        <table class="cs-comparison-table">
          <thead>
            <tr>
              <th>Unclaimed territory</th>
              <th>Evidence</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>No one owns "speed"</strong></td>
              <td>Everyone claims reliability; nobody claims fastest</td>
            </tr>
            <tr>
              <td><strong>No one owns financial education</strong></td>
              <td>Moniepoint blogs, but nobody owns it as positioning</td>
            </tr>
            <tr>
              <td><strong>No one speaks to multi-app users</strong></td>
              <td>Every fintech pretends users only use one app</td>
            </tr>
            <tr>
              <td><strong>No one owns the agent network story</strong></td>
              <td>OPay has 2M+ agents but barely mentions it on homepage</td>
            </tr>
            <tr>
              <td><strong>No one claims "most accessible"</strong></td>
              <td>OPay's offline/USSD/agent capability is unmatched but invisible</td>
            </tr>
          </tbody>
        </table>

        <h2>05. The Insights from the Research</h2>

        <h3>The Messaging Gap</h3>
        <p><strong>What OPay currently communicates:</strong><br>
        <em>"We are a financial platform that does many things. We are not a bank."</em></p>

        <p><strong>What customers actually value:</strong><br>
        <em>"OPay is fast. It works when banks don't. It's everywhere - agents, USSD, app. It's my default for moving money daily."</em></p>

        <p><strong>What the competitive landscape communicates:</strong><br>
        PalmPay = reliable + rewarding | Moniepoint = business tools | Kuda = free banking</p>

        <p><strong>Where the disconnect is:</strong><br>
        OPay's "Beyond Banking" positioning is an internal strategic statement (we're more than a bank), not a customer-facing value proposition. It communicates ambition, not value. So it should not be used on a homepage created for conversion.</p>
        <p>
          Meanwhile, OPay's actual competitive advantages—speed, scale, physical accessibility, offline capability—are either buried or invisible on the homepage. The things customers love most about OPay are the things OPay barely mentions.
        </p>

        <h3>What OPay should own instead:</h3>
        <p>
          Among the evidence analyzed, OPay's strongest, most defensible, and most differentiated position is not "Beyond Banking." It is the intersection of three things no competitor can easily replicate at the moment:
        </p>
        <ul>
          <li><strong>Speed</strong> — "fast" is the #1 word customers use about OPay</li>
          <li><strong>Reach</strong> — 60M users + 2M agents + USSD = Nigeria's most accessible financial platform</li>
          <li><strong>Simplicity</strong> — "no stories" (Nigerian endorsement for "it just works")</li>
        </ul>
        <p>
          <strong>So, essentially:</strong> OPay's messaging doesn't communicate what OPay's customers already know. The homepage should say what users say, not what the company aspires to be.
        </p>

        <h2>06. Positioning Strategy</h2>
        <p>Let’s reframe OPay.</p>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin: 2rem 0 3rem;">
          <div style="background: var(--bg-surface-elevated); padding: 1.75rem; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
            <span class="cs-meta-item-label">Current Positioning</span>
            <div style="font-size: 1.25rem; font-weight: 700; color: var(--text-muted); margin-top: 0.5rem;">"Beyond Banking"</div>
            <p style="font-size: 0.875rem; color: var(--text-muted); margin-top: 0.5rem; margin-bottom: 0;">A vague claim about what OPay is not, rather than a specific statement about what it does for customers.</p>
          </div>

          <div style="background: var(--brand-orange-light); padding: 1.75rem; border-radius: var(--radius-md); border: 1px solid var(--brand-orange);">
            <span class="cs-meta-item-label" style="color: var(--brand-orange);">Proposed Positioning</span>
            <div style="font-size: 1.25rem; font-weight: 700; color: var(--brand-orange); margin-top: 0.5rem;">"Nigeria's fastest way to move money."</div>
            <p style="font-size: 0.875rem; color: var(--text-primary); margin-top: 0.5rem; margin-bottom: 0;">A sharp, customer-proven position owning the #1 attribute users praise.</p>
          </div>
        </div>

        <h3>Why change?</h3>
        <p>Because "Beyond Banking" fails in three key areas:</p>
        <ul>
          <li><strong>Clarity:</strong> Can a new visitor understand what OPay does? No.</li>
          <li><strong>Differentiation:</strong> Could PalmPay or Kuda say the same thing? Yes.</li>
          <li><strong>Customer truth:</strong> Does it reflect what users actually value? No.</li>
        </ul>
        <p><strong>"Nigeria's fastest way to move money" passes all three:</strong></p>
        <ul>
          <li><strong>Clarity:</strong> Instantly communicates what OPay does and why.</li>
          <li><strong>Differentiation:</strong> No competitor claims "fastest." PalmPay claims "reliable." Kuda claims "free." Moniepoint claims "simple." Speed is unclaimed.</li>
          <li><strong>Customer truth:</strong> "Fast" is the #1 word in OPay customer language. 135+ reviews mention speed. This is the brand's strongest equity.</li>
        </ul>

        <h3>What customer insight supports it?</h3>
        <ul>
          <li>135+ Liners.com reviews mention "fast transfers" as the primary positive attribute</li>
          <li>"Swift, efficient, reliable" is how users describe OPay vs. banks</li>
          <li>OPay's 99.9% first-attempt transaction success rate is verified by the company</li>
          <li>During Nigeria's 2023 cash scarcity, OPay delivered when banks couldn't; speed created permanent switchers</li>
          <li>"The network is superb" — even frustrated users acknowledge OPay's transaction speed</li>
        </ul>

        <h3>What competitive gap does it address?</h3>
        <p>Every competitor claims "reliable" or "secure." Nobody claims "fastest."</p>
        <ul>
          <li>PalmPay: Claims 99.95% success rate (reliability)</li>
          <li>Kuda: Claims fee-free banking (cost)</li>
          <li>Moniepoint: Claims simple solutions (ease)</li>
          <li>OPay: Claims "Beyond Banking" (category blur)</li>
        </ul>
        <p><strong>Speed is the white space. And OPay has the evidence to support it.</strong></p>

        <h3>What does OPay get permission to own in the customer's mind?</h3>
        <ul>
          <li><em>"The app that doesn't waste your time"</em> — relevant to every daily transaction</li>
          <li><em>"The backup that's faster than your primary"</em> — relevant to multi-app users</li>
          <li><em>"Money that moves as fast as life in Nigeria"</em> — culturally resonant</li>
          <li><em>Scale as proof</em> — 60M users choosing OPay = social proof that it's the fastest</li>
        </ul>

        <h2>07. Messaging Makeover</h2>

        <h3>The Message House</h3>
        <div style="background: var(--bg-surface-elevated); padding: 1.5rem 2rem; border-radius: var(--radius-lg); border: 1px solid var(--border-subtle); margin-bottom: 2rem;">
          <div class="cs-meta-item-label" style="color: var(--brand-orange); font-weight: 700;">Core Message</div>
          <p style="font-size: 1.35rem; font-family: var(--font-display); font-weight: 700; color: var(--text-primary); margin: 0.35rem 0 0;">
            OPay is Nigeria's fastest way to move money, and the most accessible.
          </p>
        </div>

        <div class="cs-pillar-grid">
          <div class="cs-pillar-card">
            <div class="cs-pillar-tag">PILLAR 1 · SPEED</div>
            <div class="cs-pillar-name">Money moves fast on OPay.</div>
            <ul style="font-size: 0.9375rem; color: var(--text-secondary); margin-top: 0.75rem; margin-bottom: 0; padding-left: 1.2rem; line-height: 1.6;">
              <li>99.9% first-attempt transaction success rate</li>
              <li>Free OPay-to-OPay instant transfers</li>
              <li>"Fast payments and settlement" — #1 customer praise</li>
              <li>Sub-second processing on wallet-to-wallet transfers</li>
            </ul>
          </div>

          <div class="cs-pillar-card">
            <div class="cs-pillar-tag">PILLAR 2 · REACH</div>
            <div class="cs-pillar-name">OPay is everywhere you are.</div>
            <ul style="font-size: 0.9375rem; color: var(--text-secondary); margin-top: 0.75rem; margin-bottom: 0; padding-left: 1.2rem; line-height: 1.6;">
              <li>2M+ agent and merchant service points nationwide</li>
              <li>Works on any phone via USSD (*955#) — no internet required</li>
              <li>60M+ users across Nigeria</li>
              <li>Agents in every state — "practical banking branches"</li>
            </ul>
          </div>
        </div>

        <div class="cs-pillar-card" style="margin-bottom: 3.5rem;">
          <div class="cs-pillar-tag">PILLAR 3 · SIMPLICITY</div>
          <div class="cs-pillar-name">No stories. Just money that works.</div>
          <ul style="font-size: 0.9375rem; color: var(--text-secondary); margin-top: 0.75rem; margin-bottom: 0; padding-left: 1.2rem; line-height: 1.6;">
            <li>Open account in minutes, no paperwork</li>
            <li>Free transfers to any bank</li>
            <li>Pay bills, buy airtime, manage savings — all in one app</li>
            <li>"No stories" — the highest Nigerian endorsement for a financial service</li>
          </ul>
        </div>

        <h3>Supporting Messages</h3>
        <ul>
          <li><strong>For everyday Nigerians:</strong> “Send money to anyone, pay any bill, access your money anywhere, all without the drama of traditional banks.”</li>
          <li><strong>For merchants:</strong> “Accept payments instantly. Settle same day. No wahala.”</li>
          <li><strong>For agents:</strong> “Earn daily. OPay agents are Nigeria's most trusted financial service points.”</li>
        </ul>

        <h3>Objections &amp; Responses</h3>
        <table class="cs-comparison-table">
          <thead>
            <tr>
              <th>Objection</th>
              <th>Response</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>"OPay's customer service is bad"</strong></td>
              <td>Acknowledge the gap exists. Position speed + accessibility as the primary value, not support. Address support separately as an operational improvement, not a messaging claim.</td>
            </tr>
            <tr>
              <td><strong>"I use Kuda/PalmPay for banking"</strong></td>
              <td>OPay isn't trying to be your bank. It's the fastest way to move money; use it alongside your bank.</td>
            </tr>
            <tr>
              <td><strong>"Is OPay safe?"</strong></td>
              <td>CBN-licensed. NDIC-insured (MFB). PCI DSS compliant. 60M users. But don't lead with security; every competitor claims it.</td>
            </tr>
          </tbody>
        </table>

        <p style="font-size: 0.9375rem; color: var(--text-muted); font-style: italic;">
          Note: Customer support quality would need to improve for this positioning to be fully credible long-term. The messaging makeover is about leading with OPay's genuine strengths; it does not resolve the support gap.
        </p>

        <h2>Homepage Rewrite</h2>
        <p>After the research and positioning, I came up with a new landing page copy for OPay:</p>

        <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin: 2rem 0 3.5rem;">
          <a href="https://www.opayweb.com/" target="_blank" rel="noopener noreferrer" class="cs-doc-link-btn" style="margin: 0; background: var(--bg-surface-elevated); border-color: var(--border-medium);">
            Current OPay Homepage (opayweb.com) →
          </a>
          <a href="https://opay-nigeria-mock.vercel.app/" target="_blank" rel="noopener noreferrer" class="cs-doc-link-btn" style="margin: 0; background: var(--brand-orange); color: #ffffff;">
            Rewritten Homepage (opay-nigeria-mock.vercel.app) →
          </a>
        </div>

        <h2>08. Measurement</h2>
        <p>If OPay implemented this, here’s what I would measure:</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.75rem; margin: 2.5rem 0 3.5rem;">
          <div class="cs-insight-card" style="margin-bottom: 0;">
            <div class="cs-insight-num">Comprehension</div>
            <ul style="padding-left: 1.2rem; font-size: 0.9375rem; color: var(--text-secondary); line-height: 1.7;">
              <li>Describe OPay after viewing</li>
              <li>Identify "speed" as core value</li>
              <li>Distinguish from PalmPay/Kuda</li>
            </ul>
          </div>

          <div class="cs-insight-card" style="margin-bottom: 0;">
            <div class="cs-insight-num">Performance</div>
            <ul style="padding-left: 1.2rem; font-size: 0.9375rem; color: var(--text-secondary); line-height: 1.7;">
              <li>CTA click-through rate</li>
              <li>Sign-up completion rate</li>
              <li>Bounce rate reduction</li>
              <li>Time on page</li>
            </ul>
          </div>

          <div class="cs-insight-card" style="margin-bottom: 0;">
            <div class="cs-insight-num">Perception</div>
            <ul style="padding-left: 1.2rem; font-size: 0.9375rem; color: var(--text-secondary); line-height: 1.7;">
              <li>Association with "fast"</li>
              <li>Reliability vs. competitors</li>
              <li>Consideration set inclusion</li>
              <li>Differentiation score</li>
            </ul>
          </div>

          <div class="cs-insight-card" style="margin-bottom: 0;">
            <div class="cs-insight-num">Outcomes</div>
            <ul style="padding-left: 1.2rem; font-size: 0.9375rem; color: var(--text-secondary); line-height: 1.7;">
              <li>New user acquisition rate</li>
              <li>Monthly active user growth</li>
              <li>Transaction volume per user</li>
              <li>Agent network growth</li>
            </ul>
          </div>
        </div>

        <p style="font-size: 1rem; color: var(--text-muted); font-style: italic; margin-bottom: 4rem;">
          These are proposed success metrics, not results. I have no evidence that this redesign would produce specific conversion or revenue improvements. The hypothesis is that clearer messaging leads to higher comprehension, which leads to better acquisition — but this would need testing.
        </p>

        <div style="border-top: 1px solid var(--border-subtle); padding-top: 2.5rem; margin-top: 4rem;">
          <div class="tag-label">SPECULATIVE PROJECT</div>
          <p style="font-size: 0.9375rem; color: var(--text-muted); line-height: 1.7;">
            This is an independent PMM case study based on public market research, user reviews, and product positioning analysis. OPay is a registered trademark of OPay Digital Services Limited / Opera. All strategic frameworks, teardowns, and copy rewrites are my own.
          </p>
        </div>

      </div>
    </div>
  </main>

{ft_cs}
  <script src="../assets/js/main.js"></script>
</body>
</html>
"""
    with open('work/opay.html', 'w', encoding='utf-8') as f:
        f.write(opay_html)

    # -------------------------------------------------------------
    # DEDICATED KOPPOH FINANCE CASE STUDY PAGE
    # -------------------------------------------------------------
    koppoh_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Launching Koppoh Finance: A Product Marketing Strategy — Jennies Digital</title>
  <meta name="description" content="A speculative product marketing case study exploring how Koppoh could launch a financing solution for African MSMEs.">
  <link rel="icon" type="image/png" href="../assets/logo-transparent.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,100,200..800&family=Geist+Mono:wght@400;500;600&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <script>
    (() => {{
      try {{
        const t = localStorage.getItem('jd_theme') || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
        if (t === 'light') document.documentElement.classList.add('light');
      }} catch (e) {{}}
    }})();
  </script>
</head>
<body>
{h_cs}

  <main class="page-hero">
    <div class="container">
      <div>
        <a href="/work" class="back-nav-btn">← Back to Selected Work</a>
      </div>

      <div class="cs-header" style="margin-top: 1rem; margin-bottom: 3.5rem;">
        <span class="tag-label">FINANCE SAAS SME · KOPPOH FINANCE</span>
        <h1 class="page-title" style="font-size: clamp(2.35rem, 4.8vw, 3.75rem); max-width: 900px; margin-top: 0.5rem; margin-bottom: 1.5rem;">
          Launching Koppoh Finance: A Product Marketing Strategy to Go From Product Concept to Go-to-Market
        </h1>
        <p class="page-description" style="font-size: 1.25rem; max-width: 780px;">
          A speculative product marketing case study exploring how Koppoh could launch a financing solution for African MSMEs.
        </p>
      </div>

      <!-- METADATA BAR -->
      <div class="cs-meta-bar">
        <div>
          <div class="cs-meta-item-label">Role</div>
          <div class="cs-meta-item-value">Product Marketing Manager</div>
        </div>
        <div>
          <div class="cs-meta-item-label">Project Type</div>
          <div class="cs-meta-item-value">Speculative / Mock</div>
        </div>
        <div>
          <div class="cs-meta-item-label">Industry</div>
          <div class="cs-meta-item-value">Fintech / SME Finance</div>
        </div>
        <div>
          <div class="cs-meta-item-label">Market</div>
          <div class="cs-meta-item-value">Africa / Nigeria-first</div>
        </div>
        <div>
          <div class="cs-meta-item-label">Scope</div>
          <div class="cs-meta-item-value">Research · Positioning · Messaging · GTM · Launch</div>
        </div>
      </div>

      <!-- IPAD MOCKUP ON PLAIN ORANGE BACKGROUND -->
      <div class="device-orange-stage">
        <img src="../assets/images/work-koppoh-ipad.png" alt="Koppoh Finance on iPad Mockup" class="device-stage-img">
      </div>

      <!-- DISCLAIMER BANNER DIRECTLY UNDER THE PHOTO -->
      <div class="cs-warning-banner">
        <span style="font-size: 1.35rem;">⚠️</span>
        <span><strong>Disclaimer:</strong> Please note that this is just a mock project and is not affiliated with the brand itself.</span>
      </div>

      <!-- RESOURCES SECTION (ALL PROJECT DELIVERABLES & STRATEGY DOCUMENTS) -->
      <div class="cs-resources-box">
        <div class="cs-resources-header">
          <div class="cs-resources-title">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            <span>Project Resources &amp; Strategic Documents</span>
          </div>
          <span class="cs-resources-badge">7 Deliverables</span>
        </div>
        <p class="cs-resources-desc">Explore the complete collection of product marketing deliverables, research reports, mock landing page, and frameworks created for this project:</p>
        
        <div class="cs-resources-grid">
          <a href="https://koppoh-finance.vercel.app" target="_blank" rel="noopener noreferrer" class="cs-resource-item" style="border-color: var(--brand-orange); background: var(--brand-orange-light);">
            <div class="cs-resource-icon">🌐</div>
            <div class="cs-resource-info">
              <span class="cs-resource-name" style="color: var(--brand-orange);">Mock Koppoh Finance Website</span>
              <span class="cs-resource-tag">Live Prototype · Interactive Redesign (koppoh-finance.vercel.app)</span>
            </div>
            <span class="cs-resource-arrow" style="color: var(--brand-orange);">↗</span>
          </a>

          <a href="../assets/documents/Koppoh%20Finance%20-%20Product%20One%20Pager.pdf" target="_blank" rel="noopener noreferrer" class="cs-resource-item">
            <div class="cs-resource-icon">📄</div>
            <div class="cs-resource-info">
              <span class="cs-resource-name">Product One-Pager Document</span>
              <span class="cs-resource-tag">PDF · Feature &amp; Capability Architecture</span>
            </div>
            <span class="cs-resource-arrow">↗</span>
          </a>

          <a href="../assets/documents/The%20Koppoh%20Finance%20Customer.pdf" target="_blank" rel="noopener noreferrer" class="cs-resource-item">
            <div class="cs-resource-icon">🎯</div>
            <div class="cs-resource-info">
              <span class="cs-resource-name">Customer Discovery &amp; Personas</span>
              <span class="cs-resource-tag">PDF · Field Insights &amp; Trust Analysis</span>
            </div>
            <span class="cs-resource-arrow">↗</span>
          </a>

          <a href="../assets/documents/Koppoh%20Finance%20--%20Market%20%26%20Competitive%20Research.pdf" target="_blank" rel="noopener noreferrer" class="cs-resource-item">
            <div class="cs-resource-icon">📊</div>
            <div class="cs-resource-info">
              <span class="cs-resource-name">Market &amp; Competitive Research</span>
              <span class="cs-resource-tag">PDF · $32.2B Financing Gap Teardown</span>
            </div>
            <span class="cs-resource-arrow">↗</span>
          </a>

          <a href="../assets/documents/Koppoh%20Finance%20Positioning%20Document.pdf" target="_blank" rel="noopener noreferrer" class="cs-resource-item">
            <div class="cs-resource-icon">🧭</div>
            <div class="cs-resource-info">
              <span class="cs-resource-name">Positioning Document</span>
              <span class="cs-resource-tag">PDF · Category Framing &amp; Strategic Slot</span>
            </div>
            <span class="cs-resource-arrow">↗</span>
          </a>

          <a href="../assets/documents/Koppoh%20Finance%20Messaging%20Framework.pdf" target="_blank" rel="noopener noreferrer" class="cs-resource-item">
            <div class="cs-resource-icon">💬</div>
            <div class="cs-resource-info">
              <span class="cs-resource-name">Messaging Framework</span>
              <span class="cs-resource-tag">PDF · 3 Strategic Pillars &amp; Proof Points</span>
            </div>
            <span class="cs-resource-arrow">↗</span>
          </a>

          <a href="../assets/documents/Go-To-Market%20Strategy%20for%20Koppoh%20Finance%20(1).pdf" target="_blank" rel="noopener noreferrer" class="cs-resource-item">
            <div class="cs-resource-icon">🚀</div>
            <div class="cs-resource-info">
              <span class="cs-resource-name">Go-To-Market Launch Strategy</span>
              <span class="cs-resource-tag">PDF · Full 5-Stage GTM Architecture</span>
            </div>
            <span class="cs-resource-arrow">↗</span>
          </a>
        </div>
      </div>

      <!-- EDITORIAL CONTENT -->
      <div class="article-content" style="margin-top: 2rem;">
        
        <h2>What is Koppoh?</h2>
        <p>
          Koppoh is a business growth ecosystem designed to help African MSMEs build, finance, and grow their businesses. It brings together different services that address major challenges businesses face, including <strong>Koppoh Academy</strong>, which helps entrepreneurs develop and structure their businesses; <strong>Koppoh Finance</strong>, which helps businesses access suitable financing; <strong>Koppoh Fundraise</strong>, which connects businesses seeking growth capital with investors, VCs, and strategic partners; and <strong>Koppoh Media</strong>. Koppoh Academy is currently listed as live, while others including Koppoh Finance are coming soon.
        </p>

        <h2>So What Did I Do?</h2>
        <p>
          In this project, I took Koppoh Finance, one of the products listed as ‘coming soon’ in the ecosystem and I brought it to life on paper.
        </p>

        <h2>What Was The Challenge?</h2>
        <p>
          Koppoh had positioned Finance as a forthcoming product within its broader ecosystem for helping African MSMEs grow. But the public product definition was limited.
        </p>
        <p>
          I approached the project as a PMM preparing an early-stage product for launch: <em>Who should Koppoh Finance serve first? What problem should it own? How should it differentiate? And how could the product be brought to market?</em>
        </p>

        <h2>What I was given vs. what I had to figure out</h2>
        <table class="cs-comparison-table">
          <thead>
            <tr>
              <th>Known Facts</th>
              <th>Unknown Facts (To Figure Out)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                • Koppoh's stated mission<br>
                • Existing ecosystem<br>
                • Public description of Finance<br>
                • Target market
              </td>
              <td>
                • Specific customer segment (ICP)<br>
                • End-to-end product experience<br>
                • Core value proposition<br>
                • Competitive positioning &amp; messaging<br>
                • Launch &amp; GTM strategy
              </td>
            </tr>
          </tbody>
        </table>

        <h2>My Approach</h2>
        <div style="background: var(--bg-surface-elevated); padding: 2rem 2.25rem; border-radius: var(--radius-lg); border: 1px solid var(--border-subtle); margin: 2.5rem 0 3.5rem; font-family: var(--font-mono); font-size: 1rem; line-height: 2; color: var(--brand-orange);">
          1. Product Definition<br>
          ↓<br>
          2. Customer + Market Research<br>
          ↓<br>
          3. Positioning &amp; Messaging<br>
          ↓<br>
          4. Live Landing Page Creation<br>
          ↓<br>
          5. GTM Strategy
        </div>

        <h2>Defined the Product</h2>
        <p>
          As an early-stage product, most of the moving pieces had not yet been solidified. So, I created a one-pager product document listing the standard facts about this product that would create something tangible to work on for the rest of the project. There, I clarified things like what is Koppoh Finance? What does the product actually do? What are its major features and capabilities? And many more pieces.
        </p>

        <a href="../assets/documents/Koppoh%20Finance%20-%20Product%20One%20Pager.pdf" target="_blank" rel="noopener noreferrer" class="cs-doc-link-btn">
          View Product One-Pager Document →
        </a>

        <h2>The Customer</h2>
        <p>
          I extensively researched the customers Koppoh Finance would be built to serve. What did the research tell me?
        </p>

        <div class="cs-insight-card">
          <div class="cs-insight-num">Insight 01</div>
          <div class="cs-insight-title">HOSTILE FINANCING PATHS</div>
          <p class="cs-insight-body">The core pain is not lack of money, it is that every available route for the MSME is hostile: banks reject on documentation; loan apps charge 30–260% APR with harassment; loan sharks demand 10–30%/month.</p>
        </div>

        <div class="cs-insight-card">
          <div class="cs-insight-num">Insight 02</div>
          <div class="cs-insight-title">51% TRUST EXHAUSTION</div>
          <p class="cs-insight-body">Over 51% of informal MSMEs have stopped seeking formal financing entirely (up from 30% in prior years) according to a 2026 economic policy and academic research study on SME survival and credit exclusion in Nigeria. The market suffers from a deep trust exhaustion crisis.</p>
        </div>

        <div class="cs-insight-card">
          <div class="cs-insight-num">Insight 03</div>
          <div class="cs-insight-title">INFORMAL DOMINANCE</div>
          <p class="cs-insight-body">MSMEs survive on family/friends, esusu/rotating savings, and cooperatives. These community rails are the true alternatives Koppoh competes against.</p>
        </div>

        <div class="cs-insight-card">
          <div class="cs-insight-num">Insight 04</div>
          <div class="cs-insight-title">THE NEED TO BE SEEN</div>
          <p class="cs-insight-body">The deepest emotional wound is feeling invisible to institutions ('banks don't see my potential'), combined with an awareness vacuum around non-debt financing models.</p>
        </div>

        <div class="cs-insight-card">
          <div class="cs-insight-num">Insight 05</div>
          <div class="cs-insight-title">THE DOCUMENTATION ROOT CAUSE</div>
          <p class="cs-insight-body">67% of bank rejections stem directly from lack of collateral and unbankable documentation, not unviable businesses according to the IFC. Loan readiness is the actual job to solve.</p>
        </div>

        <a href="../assets/documents/The%20Koppoh%20Finance%20Customer.pdf" target="_blank" rel="noopener noreferrer" class="cs-doc-link-btn">
          View Customer Discovery Report →
        </a>

        <h2>The Opportunity</h2>
        <p>
          I took an aerial view of the market Koppoh Finance was to operate in. Who are we up against? And what field are we playing in? Here's what I found.
        </p>

        <div class="cs-insight-card">
          <div class="cs-insight-num">Insight 01</div>
          <div class="cs-insight-title">THERE IS A $32.2B MARKET GAP AND IT IS REAL</div>
          <p class="cs-insight-body">Nigeria alone has a $32.2B unmet MSME financing gap (according to IFC). The fintech SME lending platform segment is growing at ~19% CAGR, projected to reach $1.2B by 2031. This is not a niche. It is the foundational market opportunity.</p>
        </div>

        <div class="cs-insight-card">
          <div class="cs-insight-num">Insight 02</div>
          <div class="cs-insight-title">DIRECT LENDING IS CROWDED, CONSOLIDATING, AND COMING FOR KOPPOH'S SEGMENT</div>
          <p class="cs-insight-body">Moniepoint, FairMoney, OPay, Carbon, and Branch are all pushing into SME working capital. They are better-funded, faster, and already distributing. The origination lane is full.</p>
        </div>

        <div class="cs-insight-card">
          <div class="cs-insight-num">Insight 03</div>
          <div class="cs-insight-title">THE FACILITATOR LANE IS ALMOST COMPLETELY EMPTY</div>
          <p class="cs-insight-body">Nobody at scale owns the role of helping MSMEs become loan-ready, then matching them to fair capital. This is Koppoh's uncontested strategic slot and it maps directly onto what customers say they actually want.</p>
        </div>

        <div class="cs-insight-card">
          <div class="cs-insight-num">Insight 04</div>
          <div class="cs-insight-title">TRUST IS THE ACTUAL COMPETITIVE AXIS NOT INTEREST RATES</div>
          <p class="cs-insight-body">51% of informal businesses have stopped borrowing entirely (up from 30%). FCCPC enforcement resumed in July 2026. Branch is rebranding around dignity. The market is now competing on trustworthiness, not just APR.</p>
        </div>

        <div class="cs-insight-card">
          <div class="cs-insight-num">Insight 05</div>
          <div class="cs-insight-title">THE WINDOW IS REAL BUT NARROWING FAST</div>
          <p class="cs-insight-body">Better-funded lenders are already moving upstream toward the 'structured but blocked' SME segment that Koppoh targets. The Academy gives Koppoh a head start. Speed is the strategic variable.</p>
        </div>

        <a href="../assets/documents/Koppoh%20Finance%20--%20Market%20%26%20Competitive%20Research.pdf" target="_blank" rel="noopener noreferrer" class="cs-doc-link-btn">
          View Market &amp; Competitive Research Report →
        </a>

        <h2>Positioning</h2>
        <p>
          Once I knew who I was targeting and what market we were operating in, the next question was: what should Koppoh Finance mean to them? Here's what I got.
        </p>

        <div style="background: var(--bg-surface-elevated); border-left: 4px solid var(--brand-orange); padding: 2rem 2.25rem; border-radius: 0 var(--radius-lg) var(--radius-lg) 0; margin: 2.5rem 0 3.5rem;">
          <div class="cs-meta-item-label" style="color: var(--brand-orange); font-weight: 700; margin-bottom: 0.75rem;">Positioning Statement</div>
          <p style="font-size: 1.15rem; font-weight: 500; color: var(--text-primary); line-height: 1.7; margin: 0;">
            “For growth-motivated Nigerian MSME founders who are rejected by banks and exploited by predatory lenders, Koppoh Finance is a business finance readiness and matching platform that fixes the documentation gap and connects them to fair, fit-for-purpose capital. Unlike digital lenders who just approve or reject, Koppoh makes you fundable first, then matches you to the right lender.”
          </p>
        </div>

        <a href="../assets/documents/Koppoh%20Finance%20Positioning%20Document.pdf" target="_blank" rel="noopener noreferrer" class="cs-doc-link-btn">
          View Positioning Document →
        </a>

        <h2>And then I distilled that into messaging pillars</h2>

        <div class="cs-pillar-grid">
          <div class="cs-pillar-card">
            <div class="cs-pillar-tag">PILLAR 1 · READINESS</div>
            <div class="cs-pillar-name">Get Fundable</div>
            <p style="font-size: 0.9375rem; color: var(--text-secondary); margin-top: 0.5rem; line-height: 1.6;">We fix the documentation gap and others that keep you from getting capital.</p>
          </div>
          <div class="cs-pillar-card">
            <div class="cs-pillar-tag">PILLAR 2 · MATCHING</div>
            <div class="cs-pillar-name">Get Matched</div>
            <p style="font-size: 0.9375rem; color: var(--text-secondary); margin-top: 0.5rem; line-height: 1.6;">We connect you to the right lender for your business, not just any lender.</p>
          </div>
          <div class="cs-pillar-card">
            <div class="cs-pillar-tag">PILLAR 3 · TRUST</div>
            <div class="cs-pillar-name">Be Treated Right</div>
            <p style="font-size: 0.9375rem; color: var(--text-secondary); margin-top: 0.5rem; line-height: 1.6;">We built a relationship with you before we ever talked about money.</p>
          </div>
          <div class="cs-pillar-card">
            <div class="cs-pillar-tag">PILLAR 4 · DIGNITY</div>
            <div class="cs-pillar-name">Be Seen</div>
            <p style="font-size: 0.9375rem; color: var(--text-secondary); margin-top: 0.5rem; line-height: 1.6;">You have a real business. We treat it like one. No humiliation. No begging.</p>
          </div>
        </div>

        <a href="../assets/documents/Koppoh%20Finance%20Messaging%20Framework.pdf" target="_blank" rel="noopener noreferrer" class="cs-doc-link-btn">
          View Messaging Document →
        </a>

        <h2>Landing Page</h2>
        <p>
          I translated the positioning and messaging into a conversion-focused landing page designed around the customer's primary problem and decision barriers.
        </p>

        <a href="https://koppoh-finance.vercel.app" target="_blank" rel="noopener noreferrer" class="cs-doc-link-btn" style="background: var(--brand-orange); color: #ffffff;">
          Visit live mockup (koppoh-finance.vercel.app) →
        </a>

        <h2>GTM Strategy</h2>
        <p>
          Then I asked… <em>How do we get this product into the hands of the right customers?</em> The answer was this proposed GTM Strategy.
        </p>

        <a href="../assets/documents/Go-To-Market%20Strategy%20for%20Koppoh%20Finance%20(1).pdf" target="_blank" rel="noopener noreferrer" class="cs-doc-link-btn">
          View GTM Strategy →
        </a>

        <h2>Success Measurement</h2>
        <p>
          <strong>Proposed success criteria:</strong><br>
          Because Koppoh Finance has not yet launched commercially, no performance results are being claimed. I therefore defined the metrics I would use to evaluate the launch.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.75rem; margin: 2.5rem 0 3.5rem;">
          <div class="cs-insight-card" style="margin-bottom: 0;">
            <div class="cs-insight-num">Launch</div>
            <ul style="padding-left: 1.2rem; font-size: 0.9375rem; color: var(--text-secondary); line-height: 1.7;">
              <li>Academy members reached</li>
              <li>Finance waitlist sign-ups</li>
              <li>Finance enrollment</li>
              <li>Readiness journey completion</li>
            </ul>
          </div>

          <div class="cs-insight-card" style="margin-bottom: 0;">
            <div class="cs-insight-num">Financing Outcomes</div>
            <ul style="padding-left: 1.2rem; font-size: 0.9375rem; color: var(--text-secondary); line-height: 1.7;">
              <li>Businesses matched</li>
              <li>Capital disbursements</li>
              <li>Time to funding</li>
              <li>Match-to-disbursement rate</li>
            </ul>
          </div>

          <div class="cs-insight-card" style="margin-bottom: 0;">
            <div class="cs-insight-num">Customer Experience</div>
            <ul style="padding-left: 1.2rem; font-size: 0.9375rem; color: var(--text-secondary); line-height: 1.7;">
              <li>Net Promoter Score (NPS)</li>
              <li>Customer feedback</li>
              <li>Repeat financing intent</li>
              <li>Referral rate</li>
            </ul>
          </div>

          <div class="cs-insight-card" style="margin-bottom: 0;">
            <div class="cs-insight-num">Business Performance</div>
            <ul style="padding-left: 1.2rem; font-size: 0.9375rem; color: var(--text-secondary); line-height: 1.7;">
              <li>Customer acquisition cost</li>
              <li>Funnel conversion rates</li>
              <li>Revenue contribution</li>
              <li>Repeat usage</li>
            </ul>
          </div>
        </div>

        <p style="font-size: 1rem; color: var(--text-muted); font-style: italic; margin-bottom: 4rem;">
          Because Koppoh Finance is not a product I launched commercially, these are proposed success metrics rather than observed results.
        </p>

        <div style="border-top: 1px solid var(--border-subtle); padding-top: 2.5rem; margin-top: 4rem;">
          <div class="tag-label">SPECULATIVE PROJECT</div>
          <p style="font-size: 0.9375rem; color: var(--text-muted); line-height: 1.7;">
            This is an independent PMM case study based on publicly available information about Koppoh. Product decisions, positioning, messaging and GTM recommendations are my own.
          </p>
        </div>

      </div>
    </div>
  </main>

{ft_cs}
  <script src="../assets/js/main.js"></script>
</body>
</html>
"""
    with open('work/koppoh.html', 'w', encoding='utf-8') as f:
        f.write(koppoh_html)

    # -------------------------------------------------------------
    # DEDICATED WHATSAPP TEAMS CASE STUDY PAGE
    # -------------------------------------------------------------
    whatsapp_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>WhatsApp Teams: Turning the world's most familiar messaging app into lightweight team communication — Jennies Digital</title>
  <meta name="description" content="A product marketing case study on the possibility of WhatsApp spreading to new markets.">
  <link rel="icon" type="image/png" href="../assets/logo-transparent.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,100,200..800&family=Geist+Mono:wght@400;500;600&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <script>
    (() => {{
      try {{
        const t = localStorage.getItem('jd_theme') || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
        if (t === 'light') document.documentElement.classList.add('light');
      }} catch (e) {{}}
    }})();
  </script>
</head>
<body>
{h_cs}

  <main class="page-hero">
    <div class="container">
      <div>
        <a href="/work" class="back-nav-btn">← Back to Selected Work</a>
      </div>

      <div class="cs-header" style="margin-top: 1rem; margin-bottom: 3.5rem;">
        <span class="tag-label">SAAS · PRODUCT STRATEGY · WHATSAPP TEAMS</span>
        <h1 class="page-title" style="font-size: clamp(2.35rem, 4.8vw, 3.75rem); max-width: 960px; margin-top: 0.5rem; margin-bottom: 1.5rem;">
          WhatsApp Teams: Turning the world's most familiar messaging app into lightweight team communication
        </h1>
        <p class="page-description" style="font-size: 1.25rem; max-width: 780px;">
          A product marketing case study on the possibility of WhatsApp spreading to new markets
        </p>
      </div>

      <!-- METADATA BAR -->
      <div class="cs-meta-bar">
        <div>
          <div class="cs-meta-item-label">Role</div>
          <div class="cs-meta-item-value">Product Marketing Manager</div>
        </div>
        <div>
          <div class="cs-meta-item-label">Project Type</div>
          <div class="cs-meta-item-value">Speculative / Mock</div>
        </div>
        <div>
          <div class="cs-meta-item-label">Industry</div>
          <div class="cs-meta-item-value">SaaS</div>
        </div>
        <div>
          <div class="cs-meta-item-label">Market</div>
          <div class="cs-meta-item-value">Global</div>
        </div>
        <div>
          <div class="cs-meta-item-label">Scope</div>
          <div class="cs-meta-item-value">Research · Customer Discovery · Positioning · Messaging</div>
        </div>
      </div>

      <!-- LAPTOP MOCKUP ON PLAIN ORANGE BACKGROUND -->
      <div class="device-orange-stage">
        <img src="../assets/images/work-whatsapp-laptop.png" alt="WhatsApp Teams on Laptop Mockup" class="device-stage-img">
      </div>

      <!-- DISCLAIMER BANNER DIRECTLY UNDER THE PHOTO -->
      <div class="cs-warning-banner">
        <span style="font-size: 1.35rem;">⚠️</span>
        <span><strong>Disclaimer:</strong> Please note that this is just a mock project and is not affiliated with the brand itself.</span>
      </div>

      <!-- RESOURCES SECTION (OFFICIAL PLATFORM REFERENCE) -->
      <div class="cs-resources-box">
        <div class="cs-resources-header">
          <div class="cs-resources-title">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            <span>Project Resources &amp; Industry Reference</span>
          </div>
          <span class="cs-resources-badge">1 Resource</span>
        </div>
        <p class="cs-resources-desc">Explore the baseline official messaging platform referenced in this product marketing case study:</p>
        
        <div class="cs-resources-grid" style="grid-template-columns: 1fr;">
          <a href="https://www.whatsapp.com/about" target="_blank" rel="noopener noreferrer" class="cs-resource-item">
            <div class="cs-resource-icon">💬</div>
            <div class="cs-resource-info">
              <span class="cs-resource-name">WhatsApp Official Platform</span>
              <span class="cs-resource-tag">Official Product &amp; Mission · SMS Replacement &amp; E2E Baseline (whatsapp.com/about)</span>
            </div>
            <span class="cs-resource-arrow">↗</span>
          </a>
        </div>
      </div>

      <!-- EDITORIAL CONTENT -->
      <div class="article-content" style="margin-top: 2rem;">
        
        <h2>The challenge</h2>
        <p>
          WhatsApp dominates personal messaging with over 3B users globally, but teams all around the world often use a mixture of WhatsApp, Slack, email and a host of other tools to coordinate work. In this project, I explored whether WhatsApp could fill a gap and credibly enter the team communication category and what it would need to change to do so. In essence, I tried to answer the question: <em>Can WhatsApp turn the world's most familiar messaging behavior into a new category of work communication?</em>
        </p>

        <h2>First, What is WhatsApp?</h2>
        
        <h3>What is the product?</h3>
        <p>
          WhatsApp is a free, cross-platform instant messaging and voice/video calling app owned by Meta Platforms. It supports text messaging, voice messages, video messages, voice and video calls, file sharing, group chats of up to 1,024 people and Status, which are like stories.
        </p>

        <h3>What problem does it solve?</h3>
        <p>
          WhatsApp was built as an SMS replacement, solving the problem of expensive, limited, platform-dependent text messaging, as stated by WhatsApp itself on its <a href="https://www.whatsapp.com/about" target="_blank" rel="noopener noreferrer" style="color: var(--brand-orange); text-decoration: underline;">About page</a>. SMS has 160-character limits, no read receipts and poor media support. WhatsApp provides free, rich, reliable, cross-platform messaging tied to a phone number.
        </p>

        <h3>Who currently uses it?</h3>
        <p>
          Over 3 billion monthly active users across 180+ countries use it, making it the world's most popular messaging app (as reported by Meta in May 2025 and also cited on Wikipedia). It is the de facto standard for messaging in markets like India, Brazil, much of Africa, and across Europe and Latin America.
        </p>

        <h3>What do people love about it?</h3>
        <ul>
          <li><strong>Simplicity:</strong> Tied to your phone number, no account creation, no usernames (until the recent username reservation rollout in June 2026). Profile is just a name, photo, and short status.</li>
          <li><strong>Cross-platform reliability:</strong> Works equally well on iPhone, Android, Mac, Windows, and web browsers.</li>
          <li><strong>End-to-end encryption:</strong> All messages, calls, photos, and videos are encrypted.</li>
          <li><strong>Rich media support:</strong> Full-resolution photos, videos, documents, stickers, GIFs, voice messages.</li>
          <li><strong>Global reach and network effects:</strong> The sheer scale means almost everyone you know is already on it.</li>
        </ul>

        <h3>But what are its weaknesses at the moment?</h3>
        <ul>
          <li><strong>Meta ownership erodes trust:</strong> User sentiment has shifted from "trusted default messenger" to "grudgingly necessary Meta product." <em>(Malwarebytes, Jan 2026)</em></li>
          <li><strong>Privacy concerns despite encryption:</strong> An international lawsuit filed in Jan 2026 alleges Meta can store, analyze, and access private communications despite E2E encryption claims. <em>(Bloomberg, Jan 25, 2026)</em></li>
          <li><strong>Client-side security vulnerabilities:</strong> Researchers at Black Hat Asia 2026 warned that WhatsApp's E2E encryption protects servers but leaves users exposed to client-side spyware attacks, metadata leakage, and device enumeration. <em>(Computer Weekly, Apr 2026)</em></li>
          <li><strong>View Once bypass:</strong> A fourth bypass method for the View Once feature was discovered in March 2026; Meta declined to patch it, citing modified client use. <em>(SecurityWeek, Mar 2026)</em></li>
          <li><strong>Business messaging intrusion:</strong> Companies now use WhatsApp to promote services, flooding personal chat views with promotional messages. <em>(Digital Trends, May 2026)</em></li>
          <li><strong>Media compression:</strong> WhatsApp compresses photos and videos by default, reducing quality. <em>(Digital Trends, May 2026)</em></li>
          <li><strong>Account lockout issues:</strong> Aug 2026 saw mass account disabling events where users were locked out with no clear recourse. <em>(TechCrunch, Aug 3, 2026)</em></li>
          <li><strong>No significant revenue for Meta:</strong> WhatsApp Business Platform monetization remains modest relative to user scale; ads creeping into Status area. <em>(Digital Trends, May 2026)</em></li>
        </ul>

        <h3>What are its core capabilities?</h3>
        <ul>
          <li>Text, voice, and video messaging/calling (1:1 and groups)</li>
          <li>End-to-end encryption (Signal protocol)</li>
          <li>Cross-platform (iOS, Android, Windows, Mac, web)</li>
          <li>Group chats up to 1,024 people</li>
          <li>File and media sharing</li>
          <li>Status (ephemeral stories)</li>
          <li>WhatsApp Business (small business app and enterprise Cloud API)</li>
          <li>Channels (broadcast feature for businesses/creators)</li>
          <li>Meta AI assistant integration (LLaMA 4)</li>
          <li>Username reservations (rolling out June 2026)</li>
          <li>WhatsApp Plus subscription (cosmetic/organizational features, launched May 2026)</li>
        </ul>

        <h3>What is the company's current positioning?</h3>
        <p>
          <em>"Simple, reliable, private messaging and calling for free, available all over the world."</em> The company emphasizes privacy, simplicity, and global accessibility as core values.
        </p>

        <h3>What category does the market put it in?</h3>
        <p>
          Instant messaging / social communication platform. Competes with iMessage (1.3B users), WeChat (1.26B), Telegram (1B), Signal (70M), Viber (260M), LINE (217M), KakaoTalk (57M).
        </p>

        <h3>What does the company say its future is?</h3>
        <p>WhatsApp's trajectory points toward becoming a comprehensive communication and business platform:</p>
        <ul>
          <li><strong>Business monetization:</strong> WhatsApp Business Platform for enterprise customer service and conversational commerce.</li>
          <li><strong>AI integration:</strong> Meta AI assistant available in-app for questions and task completion.</li>
          <li><strong>Creator/business broadcast:</strong> Channels feature for reaching large audiences.</li>
          <li><strong>Premium features:</strong> WhatsApp Plus subscription for cosmetic and organizational features.</li>
          <li><strong>Username system:</strong> Moving beyond phone-number-only identity.</li>
          <li><strong>Parental controls:</strong> Parent-managed accounts for children's safety.</li>
        </ul>

        <h2>My approach to reframing WhatsApp</h2>

        <h2>01 — The Market Opportunity</h2>
        <p><strong>Could WhatsApp realistically win in the market as a team communication software?</strong></p>

        <h3>Current Market Size &amp; Growth</h3>
        <table class="cs-comparison-table">
          <thead>
            <tr>
              <th>Metric</th>
              <th>Value</th>
              <th>Source</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Team messaging market (2025)</td>
              <td><strong>$25.4B</strong></td>
              <td>MarketIntelo, 2026</td>
            </tr>
            <tr>
              <td>Projected (2034)</td>
              <td><strong>$57.8B</strong> (9.8% CAGR)</td>
              <td>MarketIntelo, 2026</td>
            </tr>
            <tr>
              <td>Team collaboration software (2025)</td>
              <td><strong>$40.2B</strong></td>
              <td>Grand View Research, 2026</td>
            </tr>
            <tr>
              <td>Projected (2033)</td>
              <td><strong>$85.2B</strong> (9.7% CAGR)</td>
              <td>Grand View Research, 2026</td>
            </tr>
            <tr>
              <td>Instant messaging market (2026)</td>
              <td><strong>$78.4B</strong></td>
              <td>MarkWide Research, 2026</td>
            </tr>
            <tr>
              <td>Projected IM market (2035)</td>
              <td><strong>$173.1B</strong> (9.2% CAGR)</td>
              <td>MarkWide Research, 2026</td>
            </tr>
          </tbody>
        </table>

        <h3>Why should WhatsApp take this opportunity?</h3>
        <p>
          WhatsApp has <strong>3.3 billion MAU</strong> [DemandSage, 2026] and processes <strong>100–150 billion messages/day</strong> [Axis Intelligence, 2026], yet generates only <strong>~$1.18 ARPU/year</strong> vs. Instagram's $46.78 and Facebook's $206.59 [Axis Intelligence, 2026]. This is the single largest monetization gap in consumer tech.
        </p>
        <p>
          <strong>The killer insight:</strong> WhatsApp is already the default work messenger for millions of small teams globally; it's just terrible at it. As Homebase noted, <em>"a WhatsApp group is often the only channel that actually reaches them during a shift"</em> [Homebase, 2026]. The product just needs to formalize what's already happening.
        </p>
        <p>
          WhatsApp's WhatsApp Business API hit $2B ARR by Q4 2025 and is now at an annualized ~$3.54B run rate [Meta Q1 2026 SEC filing]. But current business tools are built for customer-facing messaging (B2B2C), not internal team collaboration (B2B). A dedicated "Teams" product captures the internal communication budget that small teams currently spend on Slack, Teams, or Discord.
        </p>
        <p>
          SMBs represent ~90% of all businesses globally [OECD], and the overwhelming majority are micro-businesses with &lt;10 employees. The beachhead segment likely represents 30–40% of total addressable market by volume but only ~10–15% by revenue.
        </p>

        <h3>Competitive Landscape</h3>
        <div style="overflow-x: auto;">
          <table class="cs-comparison-table">
            <thead>
              <tr>
                <th>Platform</th>
                <th>Pricing</th>
                <th>Free Tier</th>
                <th>Key Strengths</th>
                <th>Key Weaknesses</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Slack</strong></td>
                <td>$7.25–$15/user/mo</td>
                <td>90-day history, 10 integrations</td>
                <td>2,600+ integrations, search, developer culture</td>
                <td>Expensive at scale; no read-only users; 90-day history cap</td>
              </tr>
              <tr>
                <td><strong>MS Teams</strong></td>
                <td>$0 (bundled w/ M365) or $4/user/mo</td>
                <td>Limited free</td>
                <td>Deep Microsoft integration, meetings, compliance</td>
                <td>Bloated UX, enterprise-heavy</td>
              </tr>
              <tr>
                <td><strong>Discord</strong></td>
                <td>Free / $2.99–$9.90/mo Nitro</td>
                <td>Most features free</td>
                <td>Always-on voice channels, free unlimited messaging</td>
                <td>Gaming reputation, no threaded conversations</td>
              </tr>
              <tr>
                <td><strong>Signal</strong></td>
                <td>Free</td>
                <td>Full app free</td>
                <td>Gold-standard encryption, non-profit trust</td>
                <td>~40M MAU, no business features, no channels/bots</td>
              </tr>
              <tr>
                <td><strong>Telegram</strong></td>
                <td>Free / $4.99 Premium</td>
                <td>Full app free</td>
                <td>1B MAU, 200K groups, bots, 2GB files</td>
                <td>E2E encryption only in Secret Chats</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div style="background: var(--bg-surface-elevated); padding: 1.75rem 2rem; border-radius: var(--radius-lg); border: 1px solid var(--border-subtle); margin: 2rem 0 3rem;">
          <strong style="color: var(--brand-orange);">Key competitive weakness to exploit:</strong>
          <p style="margin-top: 0.5rem; margin-bottom: 0;">
            Slack's per-user pricing is structurally hostile to small teams. A 10-person team paying $8.75/user/mo = $1,050/yr just for chat. WhatsApp Teams will be at $4.99/mo flat = $60/yr. That's a 94% cost savings. <em>(This is simply my hypothesis. Proper pricing research will have to be conducted).</em>
          </p>
        </div>

        <h3>Can WhatsApp Win?</h3>
        <p>
          In my opinion, yes, for the beachhead. WhatsApp's zero-install distribution (3.3B users already have it), mobile-first design, phone-number identity, and end-to-end encryption give it undeniable advantages for 2–20 person teams. Plus, many teams already use it for similar purposes around the world. It will struggle to displace Slack in 50+ person teams with established tooling. But the play is land-and-expand within the WhatsApp-native workflow, not feature-parity with Slack.
        </p>

        <h2>02 — Customer discovery</h2>
        <p><strong>Who would benefit the most from a product like this?</strong></p>
        <p>Small teams that need fast, low-friction communication but find Slack/Teams overkill:</p>
        <ul>
          <li><strong>Startup teams (2–15 people):</strong> Early-stage companies where everyone wears multiple hats. They don't have IT departments, don't need enterprise compliance, and communicate constantly across time zones. WhatsApp is already their default for personal communication.</li>
          <li><strong>Agencies and freelance collectives:</strong> Creative teams, marketing agencies, and consulting pods of 3–12 people who collaborate with clients and each other. Need fast, informal communication with external parties.</li>
          <li><strong>Remote-first micro teams:</strong> Distributed teams of 2–8 people who work asynchronously. Need reliable cross-platform messaging without onboarding friction.</li>
          <li><strong>Student organizations:</strong> University clubs, Greek organizations, and student government bodies with 5–20 active members. Already use WhatsApp for personal coordination; would benefit from separation of personal and organizational communication.</li>
          <li><strong>Family businesses and small retail:</strong> Mom-and-pop shops, family restaurants, small retail operations with 3–10 employees. Owner uses WhatsApp for everything; wants light separation of business and personal messages.</li>
        </ul>

        <h3>Pain Points</h3>
        <table class="cs-comparison-table">
          <thead>
            <tr>
              <th>Pain Point</th>
              <th>Detail</th>
              <th>Source</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Slack pricing</strong></td>
              <td>"The pricing structure kills our use case" — passive readers cost the same as active users</td>
              <td>r/Slack, multiple threads</td>
            </tr>
            <tr>
              <td><strong>Slack 90-day limit</strong></td>
              <td>Free plan only shows 90 days of history</td>
              <td>Slack pricing page</td>
            </tr>
            <tr>
              <td><strong>Tool fragmentation</strong></td>
              <td>"Half my day is just switching between apps"</td>
              <td>r/SaaS, 2025</td>
            </tr>
            <tr>
              <td><strong>WhatsApp Business limits</strong></td>
              <td>5 devices max, no assignment tracking, no chat routing</td>
              <td>Respond.io, BoldDesk</td>
            </tr>
            <tr>
              <td><strong>Enterprise bloat</strong></td>
              <td>MS Teams has too many features for small teams</td>
              <td>StackPicks, 2025</td>
            </tr>
            <tr>
              <td><strong>Onboarding friction</strong></td>
              <td>"We can't get people to adopt a new tool — everyone already has WhatsApp"</td>
              <td>Startup forums</td>
            </tr>
          </tbody>
        </table>

        <h2>03 — Beachhead</h2>
        <p><strong>Which team segment should WhatsApp target first?</strong></p>

        <h3>Ideal Customer Profile (ICP)</h3>
        <table class="cs-comparison-table">
          <thead>
            <tr>
              <th>Attribute</th>
              <th>Detail</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Company size</strong></td>
              <td>3–15 employees</td>
            </tr>
            <tr>
              <td><strong>Industry</strong></td>
              <td>Marketing/creative agencies, dev shops, consulting, design studios, startups</td>
            </tr>
            <tr>
              <td><strong>Revenue</strong></td>
              <td>$50K–$5M ARR</td>
            </tr>
            <tr>
              <td><strong>Location</strong></td>
              <td>India, Brazil, US (remote-first), UK, Southeast Asia</td>
            </tr>
            <tr>
              <td><strong>Current tools</strong></td>
              <td>WhatsApp groups + Google Docs/Sheets + occasional Zoom or Google Meet</td>
            </tr>
            <tr>
              <td><strong>Tech sophistication</strong></td>
              <td>Low-medium; no IT department, no DevOps</td>
            </tr>
            <tr>
              <td><strong>Budget for comms tools</strong></td>
              <td>$0–$200/month</td>
            </tr>
            <tr>
              <td><strong>Decision maker</strong></td>
              <td>Founder/CEO or ops lead</td>
            </tr>
            <tr>
              <td><strong>Trigger event</strong></td>
              <td>Just hired employee #3–5; existing WhatsApp groups are getting chaotic</td>
            </tr>
          </tbody>
        </table>

        <h3>Jobs to Be Done (JTBD)</h3>
        <div style="background: var(--bg-surface-elevated); border-left: 4px solid var(--brand-orange); padding: 1.75rem 2rem; border-radius: 0 var(--radius-lg) var(--radius-lg) 0; margin: 2rem 0 2.5rem;">
          <div class="cs-meta-item-label" style="color: var(--brand-orange); font-weight: 700; margin-bottom: 0.5rem;">Primary JTBD</div>
          <p style="font-size: 1.1rem; font-weight: 500; color: var(--text-primary); margin: 0; line-height: 1.6;">
            “When my small team needs to coordinate on our work or client work, help me keep all conversations, both internal and with clients, in one place I already use, so I can respond fast without switching apps or paying per person.”
          </p>
        </div>

        <p><strong>Supporting JTBDs:</strong></p>
        <ul>
          <li>“When a new team member joins, help me get them productive immediately without downloading a new app”</li>
          <li>“When I need to assign a client conversation to the right team member, help me do that without duplicating replies”</li>
          <li>“When I need to find a past conversation or file, help me search across all team chats”</li>
          <li>“When I need to share a quick update with the whole team, help me do it reliably without email lag”</li>
        </ul>

        <h2>04 — Product strategy</h2>
        <p><strong>What should WhatsApp Teams actually be?</strong></p>
        <p>
          My recommendation is to extend functionality. That is, create a new workspace mode within the existing WhatsApp app. Think <strong>"WhatsApp Workspaces"</strong> toggled from the same app.
        </p>
        <p>
          <em>Why not a new app?</em> Because the #1 advantage is zero-install; a separate app kills this.
        </p>

        <h3>Features that could be added to the Workspaces:</h3>
        <ul>
          <li>Channels &amp; Threads for structured topics</li>
          <li>Chat Assignment &amp; Ownership tracking</li>
          <li>Search Across Workspaces &amp; Better organization</li>
          <li>File Sharing over 2GB for elevated plans</li>
          <li>Voice/Video Call Huddles for Teams and Call scheduling features</li>
          <li>End-to-End Encryption for Businesses</li>
          <li>Lightweight integrations with key tools (Gmail, Google Drive, Notion, etc.)</li>
        </ul>

        <h3>Suggested Pricing</h3>
        <table class="cs-comparison-table">
          <thead>
            <tr>
              <th>Plan</th>
              <th>Subscription</th>
              <th>Includes</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Team</strong></td>
              <td>$4.99/mo flat</td>
              <td>1 Workspace, up to 25 members, advanced search, chat assignment</td>
            </tr>
            <tr>
              <td><strong>Business</strong></td>
              <td>$14.99/mo flat</td>
              <td>Unlimited members, unlimited storage, API access, admin analytics</td>
            </tr>
          </tbody>
        </table>
        <p>
          <strong>Why flat-rate:</strong> Slack's per-user model is its #1 competitive vulnerability. A 10-person team at $4.99/mo flat vs. $87.50/mo on Slack = 94% cost savings.
        </p>

        <h2>05 — Positioning</h2>
        <p><strong>Why WhatsApp Teams instead of Slack or others?</strong></p>

        <h3>Competitive Alternatives Out There</h3>
        <ul>
          <li><strong>Slack</strong> — the gold standard for team messaging</li>
          <li><strong>Microsoft Teams</strong> — free if already on M365</li>
          <li><strong>Discord</strong> — free, used by startups</li>
          <li><strong>Consumer WhatsApp groups</strong> — the status quo (free, broken)</li>
          <li><strong>Telegram</strong> — free, feature-rich</li>
        </ul>

        <h3>Unique Attributes of WhatsApp Teams</h3>
        <ul>
          <li>3.3B users with the app already installed — zero distribution friction</li>
          <li>Mobile-native from day one — not a desktop app that added mobile</li>
          <li>End-to-end encryption by default — not opt-in</li>
          <li>Phone number identity — no new username/password</li>
          <li>Cross-platform consistency — works identically everywhere</li>
          <li>Personal + work in one app — context switching without app switching</li>
        </ul>

        <h3>Value this Product Provides</h3>
        <ul>
          <li><strong>Zero onboarding cost</strong> — teams productive in minutes, not days</li>
          <li><strong>Instant network effects</strong> — every contact already reachable</li>
          <li><strong>Lower total cost of ownership</strong> — no per-user pricing, no training, no IT setup</li>
          <li><strong>Works for frontline workers</strong> — no email/laptop required</li>
        </ul>

        <h3>Best-Fit Customers for this Product</h3>
        <p>
          Small teams (2–20) who already communicate on WhatsApp, can't justify per-user pricing, don't need deep integrations, and want simplicity over feature-richness.
        </p>

        <h3>Market Frame for our Customers</h3>
        <p>
          Primary: Team messaging / lightweight collaboration.
        </p>

        <div style="background: var(--bg-surface-elevated); border-left: 4px solid var(--brand-orange); padding: 2rem 2.25rem; border-radius: 0 var(--radius-lg) var(--radius-lg) 0; margin: 2.5rem 0 3.5rem;">
          <div class="cs-meta-item-label" style="color: var(--brand-orange); font-weight: 700; margin-bottom: 0.75rem;">Positioning Statement</div>
          <p style="font-size: 1.15rem; font-weight: 500; color: var(--text-primary); line-height: 1.7; margin: 0;">
            “For small teams that have outgrown WhatsApp group chats but don't need complex workplace software, WhatsApp Teams is a lightweight team communication workspace that brings the familiarity and immediacy of WhatsApp to work.”
          </p>
        </div>

        <p><strong>Suggested competitive positioning:</strong></p>
        <p style="font-size: 1.1rem; font-style: italic; color: var(--text-primary);">
          “Slack gives teams powerful collaboration tools. WhatsApp Teams gives small teams the simplest possible way to work together.”
        </p>

        <h2>Message House</h2>
        <div style="background: var(--bg-surface-elevated); padding: 1.5rem 2rem; border-radius: var(--radius-lg); border: 1px solid var(--border-subtle); margin-bottom: 2rem;">
          <div class="cs-meta-item-label" style="color: var(--brand-orange); font-weight: 700;">Core Promise</div>
          <p style="font-size: 1.35rem; font-family: var(--font-display); font-weight: 700; color: var(--text-primary); margin: 0.35rem 0 0;">
            Work together. As easily as you chat.
          </p>
        </div>

        <table class="cs-comparison-table">
          <thead>
            <tr>
              <th>Pillar</th>
              <th>Message</th>
              <th>Proof Point</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Familiar</strong></td>
              <td>Your team already knows how to use it. No new communication system to learn. No new app. No new login. No training.</td>
              <td>3.3B users; #1 messaging app in 100+ countries</td>
            </tr>
            <tr>
              <td><strong>Focused</strong></td>
              <td>Keep work separate from your personal conversations. One WhatsApp. A dedicated space for work.</td>
              <td>Separate Workspace accounts</td>
            </tr>
            <tr>
              <td><strong>Work-Smart Organization</strong></td>
              <td>Channels, assignment, search, everything your team needs, nothing it doesn't.</td>
              <td>Solves #1 WhatsApp Business limitation</td>
            </tr>
            <tr>
              <td><strong>Private by Default</strong></td>
              <td>End-to-end encrypted. Your work conversations stay yours.</td>
              <td>Default E2E encryption; stronger than Telegram</td>
            </tr>
            <tr>
              <td><strong>Connected</strong></td>
              <td>Stay close to your team wherever they work. Mobile-first, cross-platform communication.</td>
              <td>Mobile-first. Easy access platform</td>
            </tr>
          </tbody>
        </table>

        <h2>Conclusion</h2>
        <p>
          WhatsApp doesn't need to become another Slack to thrive in this market category. It needs to solve a problem Slack was built to solve in a way only WhatsApp can. The research I undertook suggests that an opportunity exists between the informality of consumer group chats and the complexity of traditional workplace collaboration tools.
        </p>
        <p>
          WhatsApp Teams addresses that social vs work gap by turning an existing behavior into a purpose-built work experience. That is, keeping WhatsApp's familiarity, speed and accessibility while introducing the structure needed for teams to collaborate effectively on it.
        </p>
        <p>
          My strategic recommendation is therefore not to compete with Slack feature-for-feature, but to own lightweight team communication for teams that have outgrown the group chat but aren't ready for heavyweight workplace software.
        </p>
        <p style="font-size: 1.2rem; font-weight: 600; color: var(--brand-orange); margin-top: 2rem;">
          The opportunity isn't to make WhatsApp more like Slack. It's to make work feel as easy as WhatsApp.
        </p>

        <div style="border-top: 1px solid var(--border-subtle); padding-top: 2.5rem; margin-top: 4rem;">
          <div class="tag-label">SPECULATIVE PROJECT</div>
          <p style="font-size: 0.9375rem; color: var(--text-muted); line-height: 1.7;">
            This is an independent PMM case study based on public market research, industry benchmarks, and product strategy. WhatsApp is a trademark of Meta Platforms, Inc. Product decisions, positioning, messaging, and strategic recommendations are my own.
          </p>
        </div>

      </div>
    </div>
  </main>

{ft_cs}
  <script src="../assets/js/main.js"></script>
</body>
</html>
"""
    with open('work/whatsapp.html', 'w', encoding='utf-8') as f:
        f.write(whatsapp_html)

    # Lumina study
    s = {
        'slug': 'lumina',
        'tag': 'HealthTech, Clinical AI · 2019–2021',
        'title': 'Modernizing Clinical Diagnostics at Scale',
        'img': '../assets/images/work-lumina.jpg',
        'metrics': '⚡ 52 Hospital Deployments · 69% Speedup · 1.2M+ Records',
        'challenge': 'Healthcare providers were skeptical of black-box AI algorithms and demanded rigorous clinical validation, interpretability, and compliance before adopting diagnostic assistance tools.',
        'strategy': 'Crafted a trust-first clinical messaging framework emphasizing "Clinician-in-the-Loop Intelligence". Authored peer-reviewed whitepapers, co-developed reference case studies with leading research hospitals, and tailored physician-specific onboarding tutorials.',
        'impact': 'Secured 52 hospital network deployments in year one, expedited FDA fast-track clearance review, and cut patient diagnostic review times by 69%.'
    }
    h = get_header(active_nav='work', root_prefix='../', is_homepage=False)
    ft = get_footer(root_prefix='../')
    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{s['title']} — Jennies Digital</title>
  <link rel="icon" type="image/png" href="../assets/logo-transparent.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,100,200..800&family=Geist+Mono:wght@400;500;600&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <script>
    (() => {{
      try {{
        const t = localStorage.getItem('jd_theme') || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
        if (t === 'light') document.documentElement.classList.add('light');
      }} catch (e) {{}}
    }})();
  </script>
</head>
<body>
{h}

  <main class="page-hero">
    <div class="container">
      <div>
        <a href="/work" class="back-nav-btn">← Back to Selected Work</a>
      </div>
      <span class="tag-label">{s['tag']}</span>
      <h1 class="page-title">{s['title']}</h1>
      
      <div style="margin: 2.5rem 0; border-radius: var(--radius-lg); overflow: hidden; border: 1px solid var(--border-medium);">
        <img src="{s['img']}" alt="{s['title']}" style="width: 100%; height: auto; max-height: 520px; object-fit: cover;">
      </div>

      <div class="article-content">
        <div style="padding: 1.25rem 1.75rem; background: var(--bg-surface-elevated); border-radius: var(--radius-md); border: 1px solid var(--border-subtle); margin-bottom: 2.5rem; font-family: var(--font-mono); font-size: 0.9375rem; color: var(--brand-orange);">
          {s['metrics']}
        </div>

        <h2>1. The Strategic Challenge</h2>
        <p>{s['challenge']}</p>

        <h2>2. Go-To-Market &amp; Positioning Strategy</h2>
        <p>{s['strategy']}</p>

        <h2>3. Quantified Business Impact</h2>
        <p>{s['impact']}</p>
      </div>
    </div>
  </main>

{ft}
  <script src="../assets/js/main.js"></script>
</body>
</html>
"""
    with open(f"work/{s['slug']}.html", 'w', encoding='utf-8') as f:
        f.write(page_html)

    # -------------------------------------------------------------
    # DEDICATED AFRICA'S CREATOR MONETISATION LANDSCAPE CASE STUDY PAGE
    # -------------------------------------------------------------
    creator_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Africa's Creator Monetisation Landscape — Jennies Digital</title>
  <meta name="description" content="A competitive analysis of four platforms shaping how African creators make money online.">
  <link rel="icon" type="image/png" href="../assets/logo-transparent.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,100,200..800&family=Geist+Mono:wght@400;500;600&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <script>
    (() => {{
      try {{
        const t = localStorage.getItem('jd_theme') || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
        if (t === 'light') document.documentElement.classList.add('light');
      }} catch (e) {{}}
    }})();
  </script>
</head>
<body>
{h_cs}

  <main class="page-hero">
    <div class="container">
      <div>
        <a href="/work" class="back-nav-btn">← Back to Selected Work</a>
      </div>

      <div class="cs-header" style="margin-top: 1rem; margin-bottom: 3.5rem;">
        <span class="tag-label">CREATOR ECONOMY · MARKET RESEARCH · 2026</span>
        <h1 class="page-title" style="font-size: clamp(2.35rem, 4.8vw, 3.75rem); max-width: 960px; margin-top: 0.5rem; margin-bottom: 1.5rem;">
          Africa's Creator Monetisation Landscape
        </h1>
        <p class="page-description" style="font-size: 1.25rem; max-width: 780px;">
          A competitive analysis of four platforms shaping how African creators make money online.
        </p>
      </div>

      <!-- Hero Visual -->
      <div style="margin: 2.5rem 0; border-radius: var(--radius-lg); overflow: hidden; border: 1px solid var(--border-medium); box-shadow: 0 20px 50px rgba(0,0,0,0.4);">
        <img src="../assets/images/work-creator-monetisation.png" alt="Africa's Creator Monetisation Landscape" style="width: 100%; height: auto; display: block;">
      </div>

      <!-- Action Button / Presentation Link -->
      <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 16px; padding: 2rem; margin: 3rem 0; display: flex; flex-direction: column; md:flex-row; justify-content: space-between; align-items: center; gap: 1.5rem;">
        <div>
          <h3 style="font-size: 1.3rem; margin-bottom: 0.35rem; color: var(--text-primary);">Deep-Dive Competitive Research Deck</h3>
          <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">
            Full teardown deck covering pricing, feature matrices, distribution moats, and strategic positioning of Selar, Mainstack, Nestuge, and Coachli.
          </p>
        </div>
        <a href="../assets/documents/Africa's Creator Monetization landscape.pdf" target="_blank" class="btn-primary-hero" style="white-space: nowrap; padding: 0.9rem 1.75rem;">
          <span>VIEW THE PRESENTATION ▶</span>
        </a>
      </div>

      <div class="article-content">
        <!-- Overview Paragraph -->
        <p style="font-size: 1.2rem; line-height: 1.7; color: var(--text-primary); margin-bottom: 2.5rem;">
          I analyzed four major creator monetisation platforms: <strong>Selar</strong>, <strong>Mainstack</strong>, <strong>Nestuge</strong>, and <strong>Coachli</strong>, to understand how they differentiate, who they serve, and where opportunities exist in an increasingly competitive market.
        </p>

        <!-- The Question -->
        <div class="case-study-section">
          <h2>The question</h2>
          <div style="background: linear-gradient(135deg, rgba(230, 92, 0, 0.12) 0%, rgba(247, 195, 0, 0.12) 100%); border: 1px solid rgba(230, 92, 0, 0.3); border-radius: 12px; padding: 1.75rem 2rem; margin: 1.5rem 0; font-family: var(--font-display); font-size: 1.35rem; font-weight: 700; color: var(--text-primary); text-align: center; line-height: 1.5;">
            How are African creator platforms positioning themselves in a rapidly growing but still underdeveloped monetisation market?
          </div>
        </div>

        <!-- Market Stats Grid -->
        <div class="case-study-section">
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.25rem; margin: 2rem 0;">
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 14px; padding: 1.75rem; text-align: center;">
              <div style="font-family: var(--font-display); font-size: 2.75rem; font-weight: 800; color: var(--brand-orange); line-height: 1;">$5.1B</div>
              <div style="color: var(--text-secondary); font-size: 0.95rem; margin-top: 0.6rem; font-weight: 500;">African creator economy, 2025</div>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 14px; padding: 1.75rem; text-align: center;">
              <div style="font-family: var(--font-display); font-size: 2.75rem; font-weight: 800; color: var(--brand-yellow); line-height: 1;">$29.8B</div>
              <div style="color: var(--text-secondary); font-size: 0.95rem; margin-top: 0.6rem; font-weight: 500;">Projected value by 2032</div>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 14px; padding: 1.75rem; text-align: center;">
              <div style="font-family: var(--font-display); font-size: 2.75rem; font-weight: 800; color: #ff5252; line-height: 1;">60%</div>
              <div style="color: var(--text-secondary); font-size: 0.95rem; margin-top: 0.6rem; font-weight: 500;">of creators earning less than $100/month</div>
            </div>
          </div>
        </div>

        <!-- The Competitive Landscape -->
        <div class="case-study-section">
          <h2>The competitive landscape</h2>
          <p style="color: var(--text-secondary); margin-bottom: 1.5rem;">
            This is where I'd make your existing presentation do the heavy lifting.
          </p>

          <div style="overflow-x: auto; margin: 1.5rem 0; border: 1px solid var(--border-subtle); border-radius: 14px; background: var(--bg-card);">
            <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem;">
              <thead>
                <tr style="border-bottom: 1px solid var(--border-medium); background: var(--bg-surface);">
                  <th style="padding: 1.1rem 1.25rem; font-weight: 700; color: var(--text-primary); font-family: var(--font-mono); font-size: 0.85rem; text-transform: uppercase;">Platform</th>
                  <th style="padding: 1.1rem 1.25rem; font-weight: 700; color: var(--text-primary); font-family: var(--font-mono); font-size: 0.85rem; text-transform: uppercase;">Positioning</th>
                  <th style="padding: 1.1rem 1.25rem; font-weight: 700; color: var(--text-primary); font-family: var(--font-mono); font-size: 0.85rem; text-transform: uppercase;">Best for</th>
                  <th style="padding: 1.1rem 1.25rem; font-weight: 700; color: var(--text-primary); font-family: var(--font-mono); font-size: 0.85rem; text-transform: uppercase;">Differentiator</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom: 1px solid var(--border-subtle);">
                  <td style="padding: 1.25rem; font-weight: 700; color: var(--brand-orange); font-size: 1.05rem;">Selar</td>
                  <td style="padding: 1.25rem; color: var(--text-primary);"><span style="display: inline-block; padding: 0.2rem 0.6rem; border-radius: 4px; background: rgba(230, 92, 0, 0.12); color: var(--brand-orange); font-weight: 600;">Commerce-first</span></td>
                  <td style="padding: 1.25rem; color: var(--text-secondary);">Digital product sellers</td>
                  <td style="padding: 1.25rem; color: var(--text-primary);">Affiliate network + established trust</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-subtle);">
                  <td style="padding: 1.25rem; font-weight: 700; color: var(--text-primary); font-size: 1.05rem;">Mainstack</td>
                  <td style="padding: 1.25rem; color: var(--text-primary);"><span style="display: inline-block; padding: 0.2rem 0.6rem; border-radius: 4px; background: rgba(247, 195, 0, 0.12); color: var(--brand-yellow); font-weight: 600;">Brand-led</span></td>
                  <td style="padding: 1.25rem; color: var(--text-secondary);">Brand-conscious creators</td>
                  <td style="padding: 1.25rem; color: var(--text-primary);">Aesthetic storefront experience</td>
                </tr>
                <tr style="border-bottom: 1px solid var(--border-subtle);">
                  <td style="padding: 1.25rem; font-weight: 700; color: #448aff; font-size: 1.05rem;">Nestuge</td>
                  <td style="padding: 1.25rem; color: var(--text-primary);"><span style="display: inline-block; padding: 0.2rem 0.6rem; border-radius: 4px; background: rgba(68, 138, 255, 0.12); color: #448aff; font-weight: 600;">Automation/community</span></td>
                  <td style="padding: 1.25rem; color: var(--text-secondary);">Creators building systems</td>
                  <td style="padding: 1.25rem; color: var(--text-primary);">Community + automated workflows</td>
                </tr>
                <tr>
                  <td style="padding: 1.25rem; font-weight: 700; color: #b388ff; font-size: 1.05rem;">Coachli</td>
                  <td style="padding: 1.25rem; color: var(--text-primary);"><span style="display: inline-block; padding: 0.2rem 0.6rem; border-radius: 4px; background: rgba(179, 136, 255, 0.12); color: #b388ff; font-weight: 600;">Service/expertise</span></td>
                  <td style="padding: 1.25rem; color: var(--text-secondary);">Coaches &amp; experts</td>
                  <td style="padding: 1.25rem; color: var(--text-primary);">Booking + live service delivery</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Key Insight -->
        <div class="case-study-section">
          <h2>Key insight</h2>
          <div style="background: var(--bg-card); border-left: 4px solid var(--brand-orange); border-radius: 0 14px 14px 0; padding: 1.75rem; margin: 1.5rem 0;">
            <p style="margin: 0; color: var(--text-primary); font-size: 1.15rem; line-height: 1.6; font-weight: 500;">
              These platforms aren't really selling the same thing. They're competing around <strong>different ways of building an online business</strong>.
            </p>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1.25rem; margin-top: 1.5rem;">
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--brand-orange); margin-bottom: 0.35rem; font-weight: 600;">COMMERCE</div>
              <h3 style="font-size: 1.2rem; color: var(--text-primary); margin: 0 0 0.5rem;">Selar</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Focuses on frictionless checkout, currency flexibility, and affiliate distribution for product creators.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--brand-yellow); margin-bottom: 0.35rem; font-weight: 600;">BRAND</div>
              <h3 style="font-size: 1.2rem; color: var(--text-primary); margin: 0 0 0.5rem;">Mainstack</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Focuses on sleek aesthetics, customizable link-in-bio storefronts, and premium visual identity.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <div style="font-family: var(--font-mono); font-size: 0.85rem; color: #448aff; margin-bottom: 0.35rem; font-weight: 600;">AUTOMATION</div>
              <h3 style="font-size: 1.2rem; color: var(--text-primary); margin: 0 0 0.5rem;">Nestuge</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Focuses on automated membership management, event gating, and community engagement infrastructure.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <div style="font-family: var(--font-mono); font-size: 0.85rem; color: #b388ff; margin-bottom: 0.35rem; font-weight: 600;">EXPERTISE</div>
              <h3 style="font-size: 1.2rem; color: var(--text-primary); margin: 0 0 0.5rem;">Coachli</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Focuses on calendar integration, paid 1:1 sessions, webinars, and high-touch knowledge consultations.</p>
            </div>
          </div>
        </div>

        <!-- What I Learned -->
        <div class="case-study-section">
          <h2>What I learned</h2>
          <div style="background: var(--bg-card); border-left: 4px solid var(--brand-orange); border-radius: 0 12px 12px 0; padding: 1.75rem; margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: var(--brand-orange); margin-bottom: 0.5rem;">Features don't create differentiation on their own. Positioning does.</h3>
            <p style="margin: 0; color: var(--text-primary); line-height: 1.7;">
              Looking across these four platforms showed me how products with increasingly similar feature sets can create very different market positions by choosing a specific customer, problem, and value proposition to own.
            </p>
          </div>
          <div style="background: var(--bg-card); border-left: 4px solid var(--brand-yellow); border-radius: 0 12px 12px 0; padding: 1.75rem;">
            <h3 style="font-size: 1.15rem; color: var(--brand-yellow); margin-bottom: 0.5rem;">Looking beyond direct feature comparisons</h3>
            <p style="margin: 0; color: var(--text-primary); line-height: 1.7;">
              It also reinforced the importance of looking beyond direct feature comparisons. Understanding why a product exists, who it is really for, and what alternative it is competing against can reveal opportunities that a simple competitor matrix misses.
            </p>
          </div>
        </div>
      </div>
    </div>
  </main>

{ft_cs}
  <script src="../assets/js/main.js"></script>
</body>
</html>
"""
    with open('work/creator-monetisation.html', 'w', encoding='utf-8') as f:
        f.write(creator_html)

    print('Work pages generated')

# -------------------------------------------------------------
# 6. LAB PAGES
# -------------------------------------------------------------
def build_lab_pages():
    header = get_header(active_nav='lab', root_prefix='')
    footer = get_footer(root_prefix='')

    html_lab = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lab Experiments — Jennies Digital</title>
  <link rel="icon" type="image/png" href="assets/logo-transparent.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,100,200..800&family=Geist+Mono:wght@400;500;600&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
  <script>
    (() => {{
      try {{
        const t = localStorage.getItem('jd_theme') || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
        if (t === 'light') document.documentElement.classList.add('light');
      }} catch (e) {{}}
    }})();
  </script>
</head>
<body>
{header}

  <main class="page-hero">
    <div class="container">
      <span class="tag-label">Lab &amp; Tools</span>
      <h1 class="page-title">Tools I Built, Designed &amp; Shipped</h1>
      <p class="page-description">
        Little experiments where I do it all - design, code, copy, and ship.
      </p>

      <div class="labs-grid" style="margin-top: 3.5rem;">
        <!-- Lab 1: CleanDesk -->
        <a href="/lab/cleandesk" class="lab-card">
          <div class="lab-phone-frame">
            <div class="lab-phone-inner">
              <img src="assets/images/lab-cleandesk.png" alt="CleanDesk" loading="lazy">
            </div>
          </div>
          <div class="lab-app-title">
            <span>CleanDesk</span>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
          </div>
          <p class="lab-app-desc">An AI-powered workspace that turns messy thoughts into organized, actionable work.</p>
          <div class="lab-app-tag">WEB APP · AI TOOL · 2026</div>
        </a>

        <!-- Lab 2: Soda Reader -->
        <a href="/lab/soda-reader" class="lab-card">
          <div class="lab-phone-frame">
            <div class="lab-phone-inner">
              <img src="assets/images/lab-soda.png" alt="Soda Reader" loading="lazy">
            </div>
          </div>
          <div class="lab-app-title">
            <span>Soda Reader</span>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
          </div>
          <p class="lab-app-desc">A reading app designed to make reading addictive again and help readers actually remember what they read.</p>
          <div class="lab-app-tag">WEB APP · AI READING · 2026</div>
        </a>

        <!-- Lab 3: ContentLabAI -->
        <a href="/lab/contentlabai" class="lab-card">
          <div class="lab-phone-frame">
            <div class="lab-phone-inner">
              <img src="assets/images/lab-contentlabai.png" alt="ContentLabAI" loading="lazy">
            </div>
          </div>
          <div class="lab-app-title">
            <span>ContentLabAI</span>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
          </div>
          <p class="lab-app-desc">An AI content workflow that turns one idea into platform-ready content in my voice.</p>
          <div class="lab-app-tag">AI WORKFLOW · CONTENT STUDIO · 2026</div>
        </a>
      </div>
    </div>
  </main>

{footer}
  <script src="assets/js/main.js"></script>
</body>
</html>
"""
    with open('lab.html', 'w', encoding='utf-8') as f:
        f.write(html_lab)

    labs = [
        {
            'slug': 'cleandesk',
            'old_slug': 'promptpulse',
            'tag': 'WEB APP · AI TOOL · 2026',
            'title': 'CleanDesk',
            'subtitle': 'An AI-powered workspace that turns messy thoughts into organized, actionable work.',
            'img': '../assets/images/lab-cleandesk.png',
            'custom_content': """
      <div class="article-content" style="max-width: 820px; margin: 0 auto;">
        <div class="case-study-section">
          <h2>Watch it in action</h2>
          <div style="position: relative; padding-bottom: 62.5%; height: 0; border-radius: 16px; overflow: hidden; border: 1px solid var(--border-subtle); box-shadow: 0 20px 40px rgba(0,0,0,0.3); margin: 1.5rem 0;">
            <iframe src="https://www.loom.com/embed/87b49d390b3b42cda2f4e9cbaeb65e11?hide_owner=true&amp;hide_share=true&amp;hide_title=true&amp;hideEmbedTopBar=true" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
          </div>
        </div>

        <div class="case-study-section">
          <h2>The idea</h2>
          <p>I built CleanDesk around a simple observation: most productivity tools make you do the organizing first. You have to decide what something is, where it belongs, how important it is, and when it needs to happen before the tool can actually help.</p>
          <p>I wanted to reverse that. CleanDesk starts with the mess; the thoughts, tasks, ideas, and obligations in your head, and uses AI to help make sense of them.</p>
        </div>

        <div class="case-study-section">
          <h2>How it works</h2>
          <div style="display: grid; grid-template-columns: 1fr; gap: 1.25rem; margin: 1.5rem 0;">
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.1rem; margin-bottom: 0.5rem;">01 — Dump</h3>
              <p style="margin: 0; color: var(--text-secondary);">Write down what's on your mind naturally, without worrying about structure.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.1rem; margin-bottom: 0.5rem;">02 — Understand</h3>
              <p style="margin: 0; color: var(--text-secondary);">AI interprets the input and identifies projects, tasks, priorities, and dates.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.1rem; margin-bottom: 0.5rem;">03 — Organize</h3>
              <p style="margin: 0; color: var(--text-secondary);">Your messy thoughts become a structured workspace you can edit and manage.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.1rem; margin-bottom: 0.5rem;">04 — Follow through</h3>
              <p style="margin: 0; color: var(--text-secondary);">Use tasks, calendar integration, reminders, and productivity tracking to actually get the work done.</p>
            </div>
          </div>

          <div style="background: linear-gradient(135deg, rgba(230, 92, 0, 0.12) 0%, rgba(247, 195, 0, 0.12) 100%); border: 1px solid rgba(230, 92, 0, 0.3); border-radius: 12px; padding: 1.25rem 1.75rem; margin: 2rem 0; text-align: center; font-weight: 600; color: var(--text-primary); font-family: var(--font-display); font-size: 1.1rem;">
            Messy thoughts <span style="color: var(--brand-orange);">→</span> AI <span style="color: var(--brand-orange);">→</span> Organized workspace <span style="color: var(--brand-orange);">→</span> Action
          </div>
        </div>

        <div class="case-study-section">
          <h2>The stack</h2>
          <p><strong>Built with:</strong></p>
          <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1rem;">
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">Vercel</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">Supabase</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">Antigravity</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">Codex</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">ChatGPT</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">Google Workspace</span>
          </div>
        </div>

        <div class="case-study-section">
          <h2>What I built</h2>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-top: 1.5rem;">
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">AI task organization</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Built the workflow that transforms unstructured thoughts into structured projects and tasks.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">Task management</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Created task creation, priorities, deadlines, statuses, and drag-and-drop organization.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">Project workspaces</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Built dedicated project spaces where users can manage tasks and keep notes in context.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">Calendar integration</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Connected tasks and deadlines to the user's calendar.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">Email reminders</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Built reminders to help users stay on top of upcoming work.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">Productivity tracking</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Added stats that give users visibility into their activity and progress.</p>
            </div>
          </div>
        </div>

        <div class="case-study-section">
          <h2>What I learned</h2>
          <div style="background: var(--bg-card); border-left: 4px solid var(--brand-orange); border-radius: 0 12px 12px 0; padding: 1.75rem; margin-bottom: 1.5rem;">
            <p style="margin: 0; color: var(--text-primary); line-height: 1.7;">
              There are a lot of brands clamouring to add AI to their software and products. But AI is only valuable when it removes meaningful friction. Building CleanDesk taught me that the interesting question isn't <em>“Where can I add AI?”</em> It's <strong>“What work can AI actually take off the user's plate?”</strong> The core value of CleanDesk isn't that it uses AI. It's that the AI removes the cognitive effort of turning a messy brain dump into an organized plan.
            </p>
          </div>
          <div style="background: var(--bg-card); border-left: 4px solid var(--brand-yellow); border-radius: 0 12px 12px 0; padding: 1.75rem;">
            <p style="margin: 0; color: var(--text-primary); line-height: 1.7;">
              Building the product also changed how I think about product marketing. I had to think beyond what the product says it does and understand what is happening underneath the interface, where the user gets value, where the experience can break and what makes the product meaningfully different. The value of a product is that it solves the user's problem, not that it's fancy or 'high tech'.
            </p>
          </div>
        </div>
      </div>
"""
        },
        {
            'slug': 'soda-reader',
            'old_slug': 'valuemetric',
            'tag': 'WEB APP · AI READING · 2026',
            'title': 'Soda Reader',
            'subtitle': 'A reading app designed to make reading addictive again and help readers actually remember what they read.',
            'img': '../assets/images/lab-soda.png',
            'custom_content': """
      <div class="article-content" style="max-width: 820px; margin: 0 auto;">
        <!-- WATCH IT IN ACTION: Infinite Slow-Moving Marquee Carousel -->
        <div class="case-study-section">
          <h2>Watch it in action</h2>
          <p style="color: var(--text-secondary); margin-bottom: 1.5rem;">Explore the mobile screens and interaction flows of the Soda Reader experience.</p>
          <div class="marquee-container">
            <div class="marquee-track">
              <!-- Set 1 -->
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-1.jpg" alt="Bookshelf & Streak Calendar" loading="lazy">
              </div>
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-2.jpg" alt="Explore & Personalized Picks" loading="lazy">
              </div>
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-3.jpg" alt="Your Library & Bookshelves" loading="lazy">
              </div>
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-4.jpg" alt="Reading History & Ratings" loading="lazy">
              </div>
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-5.jpg" alt="Add a Book Modal" loading="lazy">
              </div>
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-6.jpg" alt="My Book Wall & Profile" loading="lazy">
              </div>
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-7.jpg" alt="Monthly Reading Summary" loading="lazy">
              </div>
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-8.jpg" alt="Goals & Challenges" loading="lazy">
              </div>

              <!-- Set 2 (Duplicate for continuous seamless infinite loop) -->
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-1.jpg" alt="Bookshelf & Streak Calendar" loading="lazy">
              </div>
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-2.jpg" alt="Explore & Personalized Picks" loading="lazy">
              </div>
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-3.jpg" alt="Your Library & Bookshelves" loading="lazy">
              </div>
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-4.jpg" alt="Reading History & Ratings" loading="lazy">
              </div>
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-5.jpg" alt="Add a Book Modal" loading="lazy">
              </div>
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-6.jpg" alt="My Book Wall & Profile" loading="lazy">
              </div>
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-7.jpg" alt="Monthly Reading Summary" loading="lazy">
              </div>
              <div class="carousel-phone-card">
                <img src="../assets/images/soda-8.jpg" alt="Goals & Challenges" loading="lazy">
              </div>
            </div>
          </div>
        </div>

        <!-- The Idea -->
        <div class="case-study-section">
          <h2>The idea</h2>
          <p>I built Soda around a problem I kept seeing: people don't necessarily stop loving books because they stop caring about reading. They struggle to maintain the habit, discover what to read next, and remember what they just read.</p>
          <p>Most reading products focus on helping people consume books. I wanted to explore what a product designed around enjoying, sustaining, and remembering the reading experience could look like.</p>
          <p>That led to Soda: a reading platform designed to make reading feel more engaging while helping readers build a lasting relationship with what they read.</p>
        </div>

        <!-- The Research -->
        <div class="case-study-section">
          <h2>The research</h2>
          <p>Before building, I wanted to understand why people read less, what existing reading products were missing, and where there might be an opportunity to build something meaningfully different.</p>
          <p>I looked through:</p>
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 1.5rem 0;">
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem; text-align: center;">
              <div style="font-family: var(--font-display); font-size: 2rem; font-weight: 800; color: var(--brand-orange);">70+</div>
              <div style="color: var(--text-secondary); font-size: 0.95rem; margin-top: 0.25rem;">Reddit posts analyzed</div>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem; text-align: center;">
              <div style="font-family: var(--font-display); font-size: 2rem; font-weight: 800; color: var(--brand-yellow);">27</div>
              <div style="color: var(--text-secondary); font-size: 0.95rem; margin-top: 0.25rem;">App Store reviews teardown</div>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem; text-align: center;">
              <div style="font-family: var(--font-display); font-size: 2rem; font-weight: 800; color: var(--text-primary);">12</div>
              <div style="color: var(--text-secondary); font-size: 0.95rem; margin-top: 0.25rem;">In-depth survey responses</div>
            </div>
          </div>
        </div>

        <!-- What I found -->
        <div class="case-study-section">
          <h2>What I found</h2>
          <div style="display: grid; grid-template-columns: 1fr; gap: 1.25rem; margin: 1.5rem 0;">
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.15rem; margin-bottom: 0.5rem;">Reading isn't just a discovery problem</h3>
              <p style="margin: 0; color: var(--text-secondary); line-height: 1.6;">People can find books. The harder problem is maintaining the motivation to actually read them.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.15rem; margin-bottom: 0.5rem;">Lapsed readers are an overlooked opportunity</h3>
              <p style="margin: 0; color: var(--text-secondary); line-height: 1.6;">There is a large group of people who want to read more but have fallen out of the habit.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.15rem; margin-bottom: 0.5rem;">Fiction retention is underserved</h3>
              <p style="margin: 0; color: var(--text-secondary); line-height: 1.6;">Existing tools often focus on productivity, highlights, notes, or knowledge retention rather than helping fiction readers remember and engage with what they read.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.15rem; margin-bottom: 0.5rem;">People want reading to feel personal</h3>
              <p style="margin: 0; color: var(--text-secondary); line-height: 1.6;">Discovery, recommendations, mood, progress, and social identity can make the experience feel more like their reading life.</p>
            </div>
          </div>
        </div>

        <!-- The opportunity -->
        <div class="case-study-section">
          <h2>The opportunity</h2>
          <div style="background: linear-gradient(135deg, rgba(230, 92, 0, 0.12) 0%, rgba(247, 195, 0, 0.12) 100%); border: 1px solid rgba(230, 92, 0, 0.3); border-radius: 12px; padding: 1.5rem 2rem; margin: 1.5rem 0; font-family: var(--font-display); font-size: 1.25rem; font-weight: 700; color: var(--text-primary); text-align: center;">
            Make reading feel less like a task and more like a habit people want to return to.
          </div>
        </div>

        <!-- Who I built it for -->
        <div class="case-study-section">
          <h2>Who I built it for</h2>
          <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 16px; padding: 2rem; margin: 1.5rem 0;">
            <div style="display: inline-block; padding: 0.25rem 0.75rem; background: var(--brand-orange-light); border: 1px solid rgba(230, 92, 0, 0.3); border-radius: 6px; font-family: var(--font-mono); font-size: 0.85rem; color: var(--brand-orange); font-weight: 600; margin-bottom: 0.75rem;">
              PRIMARY AUDIENCE
            </div>
            <h3 style="font-size: 1.4rem; color: var(--text-primary); margin-bottom: 0.5rem;">Lapsed Readers</h3>
            <p style="color: var(--text-secondary); margin-bottom: 1.5rem;">People who used to read regularly but have gradually fallen out of the habit and want to get back into it.</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.25rem;">
              <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 1.25rem;">
                <div style="color: var(--brand-orange); font-weight: 600; font-size: 0.9rem; margin-bottom: 0.35rem;">THEIR PROBLEM</div>
                <p style="margin: 0; color: var(--text-primary); font-style: italic;">“I want to read more, but I can't seem to stick with it.”</p>
              </div>
              <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 1.25rem;">
                <div style="color: var(--brand-yellow); font-weight: 600; font-size: 0.9rem; margin-bottom: 0.35rem;">WHAT THEY NEED</div>
                <p style="margin: 0; color: var(--text-primary);">Motivation, discovery, accountability, and a more engaging reading experience.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- How it works -->
        <div class="case-study-section">
          <h2>How it works</h2>
          <div style="background: linear-gradient(135deg, rgba(230, 92, 0, 0.12) 0%, rgba(247, 195, 0, 0.12) 100%); border: 1px solid rgba(230, 92, 0, 0.3); border-radius: 12px; padding: 1.25rem 1.75rem; margin: 1.5rem 0; text-align: center; font-weight: 600; color: var(--text-primary); font-family: var(--font-display); font-size: 1.1rem;">
            Discover <span style="color: var(--brand-orange);">→</span> Read <span style="color: var(--brand-orange);">→</span> Track <span style="color: var(--brand-orange);">→</span> Reflect <span style="color: var(--brand-orange);">→</span> Return
          </div>

          <div style="display: grid; grid-template-columns: 1fr; gap: 1.25rem; margin-top: 1.5rem;">
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.1rem; margin-bottom: 0.5rem;">Discover</h3>
              <p style="margin: 0; color: var(--text-secondary);">Personalized book discovery based on your own interests, categories, mood, and reading behavior, not based on what's popular online.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.1rem; margin-bottom: 0.5rem;">Read</h3>
              <p style="margin: 0; color: var(--text-secondary);">A built-in reading experience that keeps the reading activity inside Soda. As well as a companion experience where you can put your phone in focus mode and read a physical book and track the time too as well as leave notes.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.1rem; margin-bottom: 0.5rem;">Track</h3>
              <p style="margin: 0; color: var(--text-secondary);">Streaks, reading time, history, progress, and your personal library.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.1rem; margin-bottom: 0.5rem;">Reflect</h3>
              <p style="margin: 0; color: var(--text-secondary);">Ratings, moods, notes, and eventually AI-powered recall/conversation around books.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.1rem; margin-bottom: 0.5rem;">Return</h3>
              <p style="margin: 0; color: var(--text-secondary);">Personalized recommendations, notifications, and progress loops designed to give readers a reason to come back.</p>
            </div>
          </div>
        </div>

        <!-- What I built -->
        <div class="case-study-section">
          <h2>What I built</h2>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-top: 1.5rem;">
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">Reading experience</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Built the core reading interface and book library experience.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">Personalized discovery</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Designed the Explore experience around helping readers discover books relevant to them.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">Reading habit system</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Built streaks that had generous grace periods, timers, history, progress tracking, and reading activity.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">Reader profiles</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Created profiles, public and private book walls, avatars, personal ratings, and mood-based reading identity.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">Search &amp; library</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Built book discovery through title, author, and category search alongside personal library management.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">AI reading features</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Explored AI-powered recall and book conversation as part of the product experience.</p>
            </div>
          </div>
        </div>

        <!-- The positioning -->
        <div class="case-study-section">
          <h2>The positioning</h2>
          <p>Reading apps already exist. So the question wasn't simply <em>“How do I make another reading app?”</em></p>
          <p>It was: <strong>“Why would someone choose Soda instead of Kindle, Goodreads, Audible, Readwise, or simply reading a book on their own?”</strong></p>
          
          <h3 style="font-size: 1.2rem; color: var(--text-primary); margin: 1.75rem 0 0.75rem;">The direction</h3>
          <p>Soda isn't trying to be another place to store books. It's designed to make the act of reading itself more engaging.</p>
          
          <div style="background: var(--bg-card); border-left: 4px solid var(--brand-orange); border-radius: 0 12px 12px 0; padding: 1.75rem; margin: 1.5rem 0;">
            <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--brand-orange); margin-bottom: 0.5rem; text-transform: uppercase;">Positioning Statement</div>
            <p style="margin: 0; color: var(--text-primary); font-size: 1.1rem; line-height: 1.6; font-weight: 500;">
              “For people who want to read more but struggle to make reading stick, Soda is a reading companion that works at your pace and turns reading into a habit worth returning to anytime without guilt.”
            </p>
          </div>
        </div>

        <!-- The stack -->
        <div class="case-study-section">
          <h2>The stack</h2>
          <p><strong>Built with:</strong></p>
          <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1rem;">
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">Vercel</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">Supabase</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">Antigravity</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">Codex</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">ChatGPT</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">Google Workspace</span>
          </div>
        </div>

        <!-- What I learned -->
        <div class="case-study-section">
          <h2>What I learned</h2>
          <div style="background: var(--bg-card); border-left: 4px solid var(--brand-orange); border-radius: 0 12px 12px 0; padding: 1.75rem; margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.1rem; color: var(--brand-orange); margin-bottom: 0.5rem;">Building a full product from scratch doesn't mean starting with features</h3>
            <p style="margin: 0; color: var(--text-primary); line-height: 1.7;">
              Soda taught me how much product direction can change when you spend time understanding the user's actual problem first. I started with the broad idea of making reading more fun, but research pushed me toward a more specific opportunity: people who want to read but have lost the habit. The desire is there but the motivation isn't because of guilt, time, social pressure and other factors.
            </p>
          </div>
          <div style="background: var(--bg-card); border-left: 4px solid var(--brand-yellow); border-radius: 0 12px 12px 0; padding: 1.75rem;">
            <h3 style="font-size: 1.1rem; color: var(--brand-yellow); margin-bottom: 0.5rem;">Differentiation through underserved problems</h3>
            <p style="margin: 0; color: var(--text-primary); line-height: 1.7;">
              It also taught me that differentiation isn't necessarily about inventing something nobody has seen before. It can come from combining familiar capabilities around an underserved problem and giving the product a clearer reason to exist.
            </p>
          </div>
        </div>
      </div>
"""
        },
        {
            'slug': 'contentlabai',
            'old_slug': 'copymorph',
            'tag': 'AI WORKFLOW · CONTENT STUDIO · 2026',
            'title': 'ContentLabAI',
            'subtitle': 'An AI content workflow that turns one idea into platform-ready content in my voice.',
            'img': '../assets/images/lab-contentlabai.png',
            'custom_content': """
      <div class="article-content" style="max-width: 820px; margin: 0 auto;">
        <!-- WATCH THE WORKFLOW ▶ -->
        <div class="case-study-section">
          <h2>WATCH THE WORKFLOW ▶</h2>
          <div style="position: relative; padding-bottom: 62.5%; height: 0; border-radius: 16px; overflow: hidden; border: 1px solid var(--border-subtle); box-shadow: 0 20px 40px rgba(0,0,0,0.3); margin: 1.5rem 0;">
            <iframe src="https://www.loom.com/embed/8aa6b76e6b294625bee11e5748beb4d1?hide_owner=true&amp;hide_share=true&amp;hide_title=true&amp;hideEmbedTopBar=true" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
          </div>
        </div>

        <!-- The Idea -->
        <div class="case-study-section">
          <h2>The idea</h2>
          <p>Creating content for multiple platforms often means taking the same idea and repeatedly rewriting it for different formats, audiences, and platform constraints.</p>
          <p>I wanted to remove that repetitive work without making the content feel generic or obviously AI-generated.</p>
          <p>So I built ContentLabAI to take a single piece of content, or even a rough content idea, and turn it into multiple platform-specific formats while preserving my writing style and voice.</p>
        </div>

        <!-- How it works -->
        <div class="case-study-section">
          <h2>How it works</h2>
          <div style="display: grid; grid-template-columns: 1fr; gap: 1.25rem; margin: 1.5rem 0;">
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.1rem; margin-bottom: 0.5rem;">01 — Input</h3>
              <p style="margin: 0; color: var(--text-secondary);">I provide a finished piece of content or a rough idea.</p>
            </div>
            <div style="text-align: center; color: var(--brand-orange); font-size: 1.25rem; margin: -0.5rem 0;">↓</div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.1rem; margin-bottom: 0.5rem;">02 — Understand</h3>
              <p style="margin: 0; color: var(--text-secondary);">The workflow analyzes the topic, context, structure, and my established writing style.</p>
            </div>
            <div style="text-align: center; color: var(--brand-orange); font-size: 1.25rem; margin: -0.5rem 0;">↓</div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.1rem; margin-bottom: 0.5rem;">03 — Repurpose</h3>
              <p style="margin: 0; color: var(--text-secondary);">AI transforms the source into different formats tailored to each platform.</p>
            </div>
            <div style="text-align: center; color: var(--brand-orange); font-size: 1.25rem; margin: -0.5rem 0;">↓</div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.1rem; margin-bottom: 0.5rem;">04 — Review</h3>
              <p style="margin: 0; color: var(--text-secondary);">The outputs are generated for review and refinement rather than blindly published.</p>
            </div>
            <div style="text-align: center; color: var(--brand-orange); font-size: 1.25rem; margin: -0.5rem 0;">↓</div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="color: var(--brand-orange); font-size: 1.1rem; margin-bottom: 0.5rem;">05 — Deliver</h3>
              <p style="margin: 0; color: var(--text-secondary);">Finished content is automatically organized and sent to Google Drive.</p>
            </div>
          </div>

          <div style="background: linear-gradient(135deg, rgba(230, 92, 0, 0.12) 0%, rgba(247, 195, 0, 0.12) 100%); border: 1px solid rgba(230, 92, 0, 0.3); border-radius: 12px; padding: 1.25rem 1.75rem; margin: 2rem 0; text-align: center; font-weight: 600; color: var(--text-primary); font-family: var(--font-display); font-size: 1.05rem;">
            Idea / Draft <span style="color: var(--brand-orange);">→</span> Voice Analysis <span style="color: var(--brand-orange);">→</span> Platform Transformation <span style="color: var(--brand-orange);">→</span> Review <span style="color: var(--brand-orange);">→</span> Google Drive Sync
          </div>
        </div>

        <!-- What I built -->
        <div class="case-study-section">
          <h2>What I built</h2>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-top: 1.5rem;">
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">Voice system</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Created instructions and context designed to make the outputs sound like me, rather than generic AI content.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">Content transformation</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Built the workflow that takes one source idea and adapts it into different content formats.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">Platform-specific generation</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Designed separate outputs around the requirements and conventions of different platforms.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">Automated delivery</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Connected the workflow to Google Drive so completed content is automatically organized and delivered.</p>
            </div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.5rem;">
              <h3 style="font-size: 1.1rem; color: var(--text-primary); margin-bottom: 0.5rem;">End-to-end workflow</h3>
              <p style="margin: 0; color: var(--text-secondary); font-size: 0.95rem;">Connected the individual AI steps into one repeatable process instead of manually running each task.</p>
            </div>
          </div>
        </div>

        <!-- The stack -->
        <div class="case-study-section">
          <h2>The stack</h2>
          <p><strong>Built with:</strong></p>
          <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin: 1rem 0 1.75rem;">
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">Google Drive</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">ChatGPT</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">Codex</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">Google Docs</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">Google Cloud Console</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: var(--bg-card); border: 1px solid var(--border-subtle); font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-primary);">VSCode</span>
          </div>

          <p><strong>AI concepts used:</strong></p>
          <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1rem;">
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: rgba(230, 92, 0, 0.1); border: 1px solid rgba(230, 92, 0, 0.3); font-family: var(--font-mono); font-size: 0.85rem; color: var(--brand-orange);">workflow orchestration</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: rgba(230, 92, 0, 0.1); border: 1px solid rgba(230, 92, 0, 0.3); font-family: var(--font-mono); font-size: 0.85rem; color: var(--brand-orange);">prompt/system design</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: rgba(230, 92, 0, 0.1); border: 1px solid rgba(230, 92, 0, 0.3); font-family: var(--font-mono); font-size: 0.85rem; color: var(--brand-orange);">structured outputs</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: rgba(230, 92, 0, 0.1); border: 1px solid rgba(230, 92, 0, 0.3); font-family: var(--font-mono); font-size: 0.85rem; color: var(--brand-orange);">context injection</span>
            <span class="tag-pill" style="padding: 0.5rem 1rem; border-radius: 9999px; background: rgba(230, 92, 0, 0.1); border: 1px solid rgba(230, 92, 0, 0.3); font-family: var(--font-mono); font-size: 0.85rem; color: var(--brand-orange);">automation</span>
          </div>
        </div>

        <!-- What I learned -->
        <div class="case-study-section">
          <h2>What I learned</h2>
          <div style="background: var(--bg-card); border-left: 4px solid var(--brand-orange); border-radius: 0 12px 12px 0; padding: 1.75rem; margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.1rem; color: var(--brand-orange); margin-bottom: 0.5rem;">Automation is only useful when the system understands the job it's automating</h3>
            <p style="margin: 0; color: var(--text-primary); line-height: 1.7;">
              Building ContentLabAI taught me that simply asking AI to “turn this into a LinkedIn post” isn't enough. Good automation requires context, clear instructions, constraints, platform-specific goals, and a way to evaluate the output.
            </p>
          </div>
          <div style="background: var(--bg-card); border-left: 4px solid var(--brand-yellow); border-radius: 0 12px 12px 0; padding: 1.75rem;">
            <h3 style="font-size: 1.1rem; color: var(--brand-yellow); margin-bottom: 0.5rem;">Preserving authentic voice at scale</h3>
            <p style="margin: 0; color: var(--text-primary); line-height: 1.7;">
              I also learned that preserving voice is much harder than generating content. But once achieved, it can skyrocket productivity.
            </p>
          </div>
        </div>
      </div>
"""
        }
    ]

    for l in labs:
        h = get_header(active_nav='lab', root_prefix='../', is_homepage=False)
        ft = get_footer(root_prefix='../')
        
        if 'custom_content' in l:
            content_section = l['custom_content']
        else:
            content_section = f"""
      <div class="article-content" style="max-width: 820px; margin: 0 auto;">
        <h2>About the Experiment</h2>
        <p>{l.get('desc', '')}</p>
        
        <h2>Key Capabilities</h2>
        <ul>
          <li>Interactive parameter tuning and dynamic visual graphing.</li>
          <li>Zero-latency client-side evaluations and exportable reports.</li>
          <li>Built with modern web standards and sleek haptic interactions.</li>
        </ul>
      </div>
"""

        sub_title_html = f'<p class="page-description" style="max-width: 800px; margin: 0 0 2.5rem; color: var(--text-secondary);">{l["subtitle"]}</p>' if 'subtitle' in l else ''

        page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{l['title']} — Jennies Digital Lab</title>
  <link rel="icon" type="image/png" href="../assets/logo-transparent.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,100,200..800&family=Geist+Mono:wght@400;500;600&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <script>
    (() => {{
      try {{
        const t = localStorage.getItem('jd_theme') || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
        if (t === 'light') document.documentElement.classList.add('light');
      }} catch (e) {{}}
    }})();
  </script>
</head>
<body>
{h}

  <main class="page-hero">
    <div class="container">
      <div>
        <a href="/lab" class="back-nav-btn">← Back to Lab</a>
      </div>
      <span class="tag-label">{l['tag']}</span>
      <h1 class="page-title">{l['title']}</h1>
      {sub_title_html}
      
      <div style="display: flex; justify-content: center; margin: 3rem 0;">
        <div class="lab-phone-frame" style="max-width: 320px; max-height: 520px;">
          <div class="lab-phone-inner">
            <img src="{l['img']}" alt="{l['title']}">
          </div>
        </div>
      </div>

      {content_section}
    </div>
  </main>

{ft}
  <script src="../assets/js/main.js"></script>
</body>
</html>
"""
        with open(f"lab/{l['slug']}.html", 'w', encoding='utf-8') as f:
            f.write(page_html)
        if 'old_slug' in l:
            with open(f"lab/{l['old_slug']}.html", 'w', encoding='utf-8') as f:
                f.write(page_html)

    print('Lab pages generated')

# -------------------------------------------------------------
# 7. BLOG PAGES (Subject Matter)
# -------------------------------------------------------------
def build_blog_pages():
    header = get_header(active_nav='blog', root_prefix='')
    footer = get_footer(root_prefix='')

    articles = [
        {
            'slug': 'the-death-of-feature-first-messaging',
            'category': 'Technology',
            'tag': 'Essay',
            'date': 'August 2026',
            'readTime': '6 min read',
            'title': 'The Death of Feature-First Messaging: How to Position AI Products in 2026',
            'excerpt': 'Why listing parameter counts and latency benchmark numbers fails to convert enterprise buyers, and how leading AI companies structure their narrative around business cognitive leverage.',
            'content': """
              <p>For the past three years, the tech industry has been obsessed with model specs: context window sizes, parameter counts, and benchmark evaluations on MMLU. But in 2026, enterprise buyers don't buy model weights—they buy outcome velocity.</p>
              
              <h2>1. The Shift From "What It Does" to "What It Unlocks"</h2>
              <p>When positioning an AI product, feature-level messaging creates friction. An enterprise buyer hearing "We offer a 128k context window multi-agent framework" has to mentally translate that into their P&L statement. When you reframe to "Automate 85% of tier-1 customer underwriting in 12 seconds with audit-grade explainability," the purchasing decision becomes instantaneous.</p>

              <h2>2. The Three Pillars of Modern AI Product Marketing</h2>
              <ul>
                <li><strong>Deterministic Safety:</strong> Proving how your AI guarantees boundary control and prevents hallucinations in critical operational paths.</li>
                <li><strong>Workflow Integration:</strong> Showing that employees don't need to learn a new tool—your AI operates natively where they already live.</li>
                <li><strong>Time-to-Value (TTV):</strong> Compressing time-to-first-magic from weeks of custom prompt tuning to under 4 minutes of self-serve setup.</li>
              </ul>

              <h2>3. The Takeaway for Founders &amp; PMMs</h2>
              <p>Stop marketing technology and start marketing superpowers. The most enduring AI companies are not those with the highest parameter density, but those with the clearest articulation of human leverage.</p>
            """
        },
        {
            'slug': 'why-most-ai-saas-launches-fail',
            'category': 'Business',
            'tag': 'Research',
            'date': 'July 2026',
            'readTime': '8 min read',
            'title': 'Why Most AI SaaS Launches Fail: The Zero-to-One GTM Playbook',
            'excerpt': 'Deconstructing the common pitfalls of AI launches and the exact 5-stage framework to guarantee day-one traction, press coverage, and enterprise pipeline generation.',
            'content': """
              <p>Launching an AI product today is louder and more competitive than any previous software cycle. A great product launch is not an announcement—it is the orchestration of an inevitable movement.</p>

              <h2>The 5-Stage Zero-to-One GTM Framework</h2>
              <p><strong>Stage 1: The Private Alpha Beta-Testing Core.</strong> Limit your first 50 users to high-intent power users who provide daily feedback on friction points.</p>
              <p><strong>Stage 2: The Provocative Category Manifesto.</strong> Write an essay challenging the status quo of your industry. Don't just launch a tool; launch a perspective.</p>
              <p><strong>Stage 3: The Interactive Sandbox Playground.</strong> Remove authentication friction. Allow visitors to experience the core value in the browser before asking for an email.</p>
              <p><strong>Stage 4: Co-Marketing With Design Partners.</strong> Launch alongside 3 recognizable enterprise logos whose quotes validate your ROI.</p>
              <p><strong>Stage 5: The Multi-Channel Distribution Blitz.</strong> Coordinate Product Hunt, LinkedIn executive thought leadership, niche newsletter sponsorships, and technical deep-dives on the same morning.</p>
            """
        },
        {
            'slug': 'fintech-licensing-and-regulatory-moats',
            'category': 'Law',
            'tag': 'Research',
            'date': 'June 2026',
            'readTime': '7 min read',
            'title': 'Fintech Licensing & Regulatory Moats: A PMM Breakdown of Open Banking',
            'excerpt': 'How regulatory frameworks and compliance structures create defensible go-to-market advantages for emerging financial platforms.',
            'content': """
              <p>In heavily regulated environments like African fintech, regulation is often perceived solely as a bottleneck. However, from a product marketing standpoint, compliance is the ultimate trust moat.</p>

              <h2>1. Compliance as Positioning</h2>
              <p>When selling to institutional partners and enterprises, possessing direct CBN licensing or audited tier-1 payment infrastructure transforms risk-averse buyers into eager adopters. Messaging that emphasizes regulatory certainty beats feature checklists every time.</p>

              <h2>2. The Strategic Value of Open Banking Protocols</h2>
              <p>With standardized API frameworks emerging across the continent, products that position themselves as connective interoperability layers will capture exponential platform distribution.</p>
            """
        },
        {
            'slug': 'lessons-from-obviously-awesome',
            'category': 'Books',
            'tag': 'Review',
            'date': 'May 2026',
            'readTime': '5 min read',
            'title': 'Lessons from "Obviously Awesome": Finding the Strategic Context That Sells',
            'excerpt': 'Why great products fail when placed in the wrong market category, and how deliberate framing transforms buyer perception.',
            'content': """
              <p>April Dunford's classic framework on positioning remains the definitive guide for product marketers. The central insight is simple yet profound: context determines how value is judged.</p>

              <h2>Core Takeaways</h2>
              <ul>
                <li><strong>Competitive Alternatives:</strong> What would customers do if your product didn't exist? (Often it is an Excel sheet or manual email).</li>
                <li><strong>Unique Attributes:</strong> Capabilities you possess that alternatives cannot match.</li>
                <li><strong>Value to the Customer:</strong> Translating features into measurable business outcomes.</li>
                <li><strong>Target Customer Segment:</strong> Who cares the most about that specific value?</li>
                <li><strong>Market Category:</strong> The frame of reference that makes your value obvious.</li>
              </ul>
            """
        },
        {
            'slug': 'cognitive-architecture-vs-copywriting',
            'category': 'Ideas',
            'tag': 'Note',
            'date': 'May 2026',
            'readTime': '4 min read',
            'title': 'Cognitive Architecture vs. Descriptive Copywriting in Tech',
            'excerpt': 'Product marketing is less about decorative words and more about structuring the mental model a customer uses to navigate choice.',
            'content': """
              <p>Descriptive copywriting tells a customer what a product does. Cognitive architecture shapes how a customer thinks about their entire problem space.</p>
              <p>When you define the problem better than anyone else, the customer instinctively assumes you have the best solution.</p>
            """
        },
        {
            'slug': 'the-shift-toward-dignity-in-digital-finance',
            'category': 'Culture',
            'tag': 'Essay',
            'date': 'April 2026',
            'readTime': '6 min read',
            'title': 'The Shift Toward Dignity in Digital Finance & Consumer Trust',
            'excerpt': 'Exploring how trust exhaustion and predatory friction have reshaped consumer expectations across modern financial products.',
            'content': """
              <p>In emerging digital ecosystems, consumer trust is fragile. Products that win long-term are not those with the flashiest growth hacks, but those that treat user agency, transparent pricing, and data privacy with utmost dignity.</p>
            """
        },
        {
            'slug': 'founder-led-marketing-in-the-early-days',
            'category': 'People',
            'tag': 'Essay',
            'date': 'March 2026',
            'readTime': '6 min read',
            'title': 'Founder-Led Marketing: How Early-Stage Teams Win Hearts',
            'excerpt': 'Why early customers buy the founder before they buy the software, and how to harness authentic storytelling before scaling a marketing team.',
            'content': """
              <p>Before an early-stage startup has brand recognition or enterprise case studies, its single greatest marketing asset is the founder's conviction. Personal narrative, public learning, and transparent building create an emotional bond that corporate marketing cannot replicate.</p>
            """
        }
    ]

    html_blog = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Subject Matter — Jennies Digital Blog</title>
  <link rel="icon" type="image/png" href="assets/logo-transparent.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,100,200..800&family=Geist+Mono:wght@400;500;600&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
  <script>
    (() => {{
      try {{
        const t = localStorage.getItem('jd_theme') || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
        if (t === 'light') document.documentElement.classList.add('light');
      }} catch (e) {{}}
    }})();
  </script>
</head>
<body>
{header}

  <main class="page-hero">
    <div class="container">
      <span class="tag-label">Blog &amp; Insights</span>
      <h1 class="page-title">Subject Matter</h1>
      <p class="page-description">
        My perspectives on technology, business, law, people, and things I find remotely interesting.
      </p>

      <div class="blog-filter-tabs" style="margin-top: 2.5rem;">
        <button type="button" class="blog-tab-btn active" data-filter="all">All</button>
        <button type="button" class="blog-tab-btn" data-filter="technology">Technology</button>
        <button type="button" class="blog-tab-btn" data-filter="business">Business</button>
        <button type="button" class="blog-tab-btn" data-filter="law">Law</button>
        <button type="button" class="blog-tab-btn" data-filter="books">Books</button>
        <button type="button" class="blog-tab-btn" data-filter="ideas">Ideas</button>
        <button type="button" class="blog-tab-btn" data-filter="people">People</button>
        <button type="button" class="blog-tab-btn" data-filter="culture">Culture</button>
      </div>

      <div class="blog-grid-2col">
"""
    for a in articles:
        html_blog += f"""        <article class="blog-static-card" data-category="{a['category']}">
          <div>
            <div class="blog-card-top">
              <div class="blog-badges-wrap">
                <span class="blog-category-badge">{a['category']}</span>
                <span class="blog-format-tag">{a['tag']}</span>
              </div>
              <span class="blog-read-time">{a['date']} · {a['readTime']}</span>
            </div>
            <h2 class="blog-card-title">
              <a href="/blog/{a['slug']}" class="blog-title-link">{a['title']}</a>
            </h2>
            <p class="blog-card-excerpt">{a['excerpt']}</p>
          </div>
          <div class="blog-card-footer">
            <a href="/blog/{a['slug']}" class="read-more-link">
              Full read
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </a>
          </div>
        </article>
"""
    html_blog += f"""      </div>
    </div>
  </main>

{footer}
  <script src="assets/js/main.js"></script>
</body>
</html>
"""
    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(html_blog)

    for i, a in enumerate(articles):
        h = get_header(active_nav='blog', root_prefix='../', is_homepage=False)
        ft = get_footer(root_prefix='../')
        
        # Determine 2 next recommended articles
        next_articles = [articles[(i + 1) % len(articles)], articles[(i + 2) % len(articles)]]
        
        read_next_cards_html = ""
        for na in next_articles:
            read_next_cards_html += f"""          <article class="blog-static-card" data-category="{na['category']}">
            <div>
              <div class="blog-card-top">
                <div class="blog-badges-wrap">
                  <span class="blog-category-badge">{na['category']}</span>
                  <span class="blog-format-tag">{na['tag']}</span>
                </div>
                <span class="blog-read-time">{na['date']} · {na['readTime']}</span>
              </div>
              <h3 class="blog-card-title" style="font-size: 1.2rem;">
                <a href="/blog/{na['slug']}" class="blog-title-link">{na['title']}</a>
              </h3>
              <p class="blog-card-excerpt" style="font-size: 0.875rem; margin-bottom: 1.25rem;">{na['excerpt']}</p>
            </div>
            <div class="blog-card-footer">
              <a href="/blog/{na['slug']}" class="read-more-link">
                Full read
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
              </a>
            </div>
          </article>
"""

        page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{a['title']} — Subject Matter</title>
  <link rel="icon" type="image/png" href="../assets/logo-transparent.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,100,200..800&family=Geist+Mono:wght@400;500;600&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/style.css">
  <script>
    (() => {{
      try {{
        const t = localStorage.getItem('jd_theme') || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
        if (t === 'light') document.documentElement.classList.add('light');
      }} catch (e) {{}}
    }})();
  </script>
</head>
<body>
{h}

  <main class="page-hero">
    <div class="container">
      <div>
        <a href="/blog" class="back-nav-btn">← Back to Subject Matter</a>
      </div>
      <div class="blog-card-top" style="max-width: 760px; margin: 0 auto 1.25rem;">
        <div class="blog-badges-wrap">
          <span class="blog-category-badge">{a['category']}</span>
          <span class="blog-format-tag">{a['tag']}</span>
        </div>
        <span class="blog-read-time">{a['date']} · {a['readTime']}</span>
      </div>
      <h1 class="page-title" style="max-width: 760px; margin: 0 auto 2.5rem; font-size: clamp(2rem, 4.5vw, 3.25rem);">{a['title']}</h1>
      
      <div class="article-content">
        {a['content']}
      </div>

      <!-- READ NEXT SECTION -->
      <section class="read-next-section" style="max-width: 820px; margin: 5rem auto 0; padding-top: 3.5rem; border-top: 1px solid var(--border-subtle);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 2rem; flex-wrap: wrap; gap: 1rem;">
          <div>
            <span class="tag-label">Continue Reading</span>
            <h2 style="font-family: var(--font-display); font-size: 1.75rem; font-weight: 700; margin: 0.25rem 0 0; color: var(--text-primary);">Read Next</h2>
          </div>
          <a href="/blog" class="read-more-link" style="font-weight: 600;">
            All articles
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </a>
        </div>

        <div class="blog-grid-2col">
{read_next_cards_html}        </div>
      </section>
    </div>
  </main>

{ft}
  <script src="../assets/js/main.js"></script>
</body>
</html>
"""
        with open(f"blog/{a['slug']}.html", 'w', encoding='utf-8') as f:
            f.write(page_html)

    print('Blog pages generated')

def build_vercel_json():
    with open('vercel.json', 'w', encoding='utf-8') as f:
        f.write('{\n  "cleanUrls": true,\n  "trailingSlash": false\n}\n')
    print('vercel.json created successfully')

if __name__ == '__main__':
    build_vercel_json()
    generate_mockups()
    build_css()
    build_js()
    build_index()
    build_work_pages()
    build_lab_pages()
    build_blog_pages()
    print('OPAY CASE STUDY & SELECTED WORK CUSTOMIZATION COMPLETED!')
