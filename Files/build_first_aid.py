#!/usr/bin/env python3
"""3xploreWithUs - First Aid Kit: Newborn Edition"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

BASE     = "/sessions/optimistic-awesome-carson/mnt/3xploreWithUs/Website"
FONT_DIR = f"{BASE}/Roboto/static"
LOGO_B   = f"{BASE}/EditingElements/logo_black.png"
OUTPUT   = "/sessions/optimistic-awesome-carson/mnt/outputs/3xWU_FirstAidKit_NewbornEdition.pdf"

_fonts = {
    'R':   'Roboto-Regular.ttf',
    'RL':  'Roboto-Light.ttf',
    'RB':  'Roboto-Bold.ttf',
    'RI':  'Roboto-Italic.ttf',
    'RC':  'Roboto_Condensed-Regular.ttf',
    'RCB': 'Roboto_Condensed-Bold.ttf',
}
for name, file in _fonts.items():
    pdfmetrics.registerFont(TTFont(name, f"{FONT_DIR}/{file}"))

DARK   = HexColor('#0D1515')
DARK2  = HexColor('#131C1C')
DARK3  = HexColor('#1A2626')
TEAL   = HexColor('#1A9090')
TEALLT = HexColor('#5AC8C8')
SAND   = HexColor('#D4A96A')
SANDLT = HexColor('#EDD9A3')
RED    = HexColor('#B84A2F')
MUTED  = HexColor('#72888A')
CREAM  = HexColor('#F5F2EC')
PALE   = HexColor('#FAF7F2')
BDARK  = HexColor('#1A2020')
LINE   = HexColor('#DDD8CE')
OPTCLR = HexColor('#9AACAC')

W, H = A4
M    = 46
CW   = W - 2 * M

HEADER_H   = 54
USABLE_TOP = H - HEADER_H - 2 - 16
FOOTER_MIN = 55

# ── CONTENT ───────────────────────────────────────────────────────────────────

INTRO_TEXT = (
    "Focus on compact, multi-use items that address heat, sun, minor rashes, congestion "
    "from dry air or pollen, and the inevitable nappy changes on the go. "
    "Pharmacies (Apotheke / Pharmacie / Farmacia) are everywhere in Europe and well-stocked "
    "-- you can restock easily without carrying everything from home."
)

# Checklist sections: (name, note, is_optional)
CHECKLIST_SECTIONS = [
  { "title": "Essentials", "colour": TEAL,
    "subtitle": "Grab-and-go bag",
    "intro": None,
    "items": [
      ("Digital rectal thermometer + forehead backup",
       "Rectal is most accurate for young babies. Good to know: a rectal temp of 38 degrees C "
       "(100.4 F) or higher in a baby under 3 months is worth getting checked promptly.", False),
      ("Infant paracetamol (e.g. Calpol or equivalent)",
       "Get dosing advice from your paediatrician before you leave. "
       "Ibuprofen is usually suitable after 3-6 months.", False),
      ("Nasal saline drops + bulb syringe / aspirator",
       "A huge help with travel congestion from dry air and pollen.", False),
      ("Zinc oxide nappy rash cream (e.g. Sudocrem)",
       "Heat and long stretches in the car seat tend to mean more rashes. Worth being generous with this one.", False),
      ("Fragrance-free moisturiser + petroleum jelly", "", False),
      ("Sterile gauze, small adhesive bandages, medical tape, antiseptic wipes",
       "", False),
      ("Antibiotic ointment for minor cuts", "", False),
      ("Oral rehydration sachets (ORS / Pedialyte-style)",
       "For tummy upset from heat or new foods.", False),
      ("Tweezers, nail clippers / emery board, cotton swabs", "", False),
      ("Alcohol-free hand sanitiser + disposable gloves", "", False),
      ("Mineral sunscreen SPF 30+ (after 6 months)",
       "No direct sun for babies under 6 months -- hats, light clothing and shade do the job before then.", False),
      ("After-sun / aloe gel (baby-safe) + calamine lotion",
       "For sunburn, bites, and general skin irritation.", False),
      ("Insect repellent: DEET-free or picaridin formula",
       "Check with your pharmacist for infant-safe options. Best avoided on very young babies.", False),
    ],
  },
  { "title": "Natural & Home Remedies", "colour": SANDLT,
    "subtitle": "Gentle first-line support",
    "intro": (
        "These work alongside conventional medicine, not instead of it. "
        "Good for everyday comfort, settling, and prevention -- all suitable for newborns unless noted."
    ),
    "items": [
      ("Calendula cream",
       "Plant-based and gentle on newborn skin. Great for nappy rash, redness, and general irritation -- "
       "a softer everyday option alongside zinc oxide.", False),
      ("Probiotic drops (e.g. BioGaia Protectis / L. reuteri)",
       "Solid evidence for reducing colic and fussing in breastfed babies. Worth starting early.", False),
      ("Coconut oil (virgin, unrefined)",
       "Multi-use: dry skin, cradle cap massage, mild nappy rash. Also doubles as a gentle nappy-change balm.", False),
      ("Fennel drops or alcohol-free gripe water",
       "Traditional support for wind and colic discomfort. Look for alcohol-free, sugar-free formulas -- "
       "easy to find at any European Apotheke.", False),
      ("Vitamin D drops",
       "Recommended for all breastfed babies from birth. Easy to forget on the road -- "
       "pack it with the morning routine so it becomes a habit.", False),
      ("Lavender essential oil (diluted, or a pre-made baby calm roll-on)",
       "A little on a muslin near the sleep space can help settle and calm. "
       "Never apply neat to newborn skin.", False),
      ("Arnica cream or gel",
       "Parent use. For bumps and bruises from van life. A small tube goes a long way.", False),
    ],
  },
  { "title": "Van-Specific Extras", "colour": SAND,
    "subtitle": None,
    "intro": None,
    "items": [
      ("Reusable ice packs or instant cold packs",
       "For minor bumps or cooling in hot weather.", False),
      ("LED headlamp / torch",
       "Night checks without waking everyone up.", False),
      ("Emergency mylar blanket + extra muslin cloths", "", False),
      ("Newborn CPR and choking guide",
       "A small printed card or downloaded app. Worth knowing before you need it.", False),
      ("Baby health records + EHIC card",
       "European Health Insurance Card covers necessary medical care across EU. "
       "Check it has not expired. Keep with insurance details and paediatrician contacts.", False),
    ],
  },
]

# Text-only section: bullet points, no checkboxes
REMINDERS = [
  ("Fever in a newborn under 3 months",
   "A rectal temp of 38 degrees C (100.4 F) or higher in the first three months is worth taking seriously "
   "and getting checked -- especially if you are off the beaten path. Have a plan before you need one."),
  ("Hand hygiene and crowd exposure",
   "Good hand hygiene and a bit of caution around crowds in the early weeks makes a real difference."),
  ("Umbilical cord care",
   "Keep it clean and dry. Fold the nappy down below it until it falls off naturally."),
  ("Safe sleep",
   "Flat, firm surface. Back sleeping. No loose bedding -- this is especially worth thinking through in a van."),
  ("Feeding plan",
   "Breastfeeding on demand or careful formula hygiene (boiled/cooled water or ready-to-feed). "
   "It helps to have a backup plan for travel delays or hot weather."),
  ("Before leaving Germany",
   "A thorough well-baby check before you go, vaccinations confirmed on track, and a quick chat "
   "with your paediatrician or midwife about your route. Many practices offer telehealth follow-ups "
   "so you can check in from the road."),
]

CLOSING_TEXT = (
    "This list is a starting point, not a substitute for medical advice. "
    "Trust your instincts -- you know your baby better than anyone. "
    "When something feels off, find a pharmacy or doctor. "
    "European healthcare is excellent and more accessible than you might think."
)

# ── RENDERER ──────────────────────────────────────────────────────────────────
cv      = rl_canvas.Canvas(OUTPUT, pagesize=A4)
pg_num  = 0
cur_y   = [USABLE_TOP]
cur_sec = ['']


def txt_lines(text, font, size, max_w):
    if not text.strip():
        return []
    words, result, line = text.split(), [], ''
    for w in words:
        test = (line + ' ' + w).strip()
        if cv.stringWidth(test, font, size) <= max_w:
            line = test
        else:
            if line:
                result.append(line)
            line = w
    if line:
        result.append(line)
    return result


def draw_label(text, x, y, colour):
    cv.setFont('RCB', 7)
    cv.setFillColor(colour)
    cx = x
    for ch in text.upper():
        cv.drawString(cx, y, ch)
        cx += cv.stringWidth(ch, 'RCB', 7) + 2.5


def draw_chrome(section=''):
    cv.setFillColor(CREAM)
    cv.rect(0, H - HEADER_H, W, HEADER_H, fill=1, stroke=0)
    cv.setFillColor(LINE)
    cv.rect(0, H - HEADER_H, W, 1, fill=1, stroke=0)
    cv.setFillColor(TEAL)
    cv.rect(0, H - HEADER_H - 2, W, 2, fill=1, stroke=0)
    try:
        cv.drawImage(LOGO_B, M, H - 46, width=130, height=32,
                     mask='auto', preserveAspectRatio=True)
    except:
        pass
    if section:
        spaced = '  '.join(section.upper())
        cv.setFont('RCB', 7)
        cv.setFillColor(MUTED)
        cv.drawRightString(W - M, H - 34, spaced)
    cv.setFillColor(TEAL)
    cv.rect(0, 55, 5, H - 111, fill=1, stroke=0)
    cv.setFillColor(LINE)
    cv.rect(M, 34, CW, 0.8, fill=1, stroke=0)
    cv.setFont('RC', 7.5)
    cv.setFillColor(MUTED)
    cv.drawString(M, 20, 'www.3xplorewithus.com')
    cv.setFont('R', 7)
    cv.setFillColor(MUTED)
    cv.drawCentredString(W / 2, 20, 'Made with love by 3xploreWithUs')
    cv.setFont('RCB', 7.5)
    cv.setFillColor(MUTED)
    cv.drawRightString(W - M, 20, str(pg_num))


def next_page(section=''):
    global pg_num
    cv.showPage()
    pg_num += 1
    cur_sec[0] = section or cur_sec[0]
    draw_chrome(cur_sec[0])
    cur_y[0] = USABLE_TOP


def ensure(needed):
    if cur_y[0] - needed < FOOTER_MIN:
        next_page()


def item_height(name, note):
    nw = CW - 30
    nl = max(len(txt_lines(name, 'RCB', 10, nw - 18)), 1)
    notl = len(txt_lines(note, 'R', 9, nw)) if note else 0
    return nl * 13 + notl * 13 + 9


def draw_item(name, note, optional=False):
    ih = item_height(name, note)
    ensure(ih)
    y = cur_y[0]
    cv.setStrokeColor(OPTCLR if optional else MUTED)
    cv.setLineWidth(0.7)
    cv.roundRect(M + 8, y - 8, 8, 8, 1.5, fill=0, stroke=1)
    nl = txt_lines(name, 'RCB', 10, CW - 30)
    cv.setFont('RCB', 10)
    cv.setFillColor(OPTCLR if optional else BDARK)
    iy = y
    for l in nl:
        cv.drawString(M + 22, iy, l)
        iy -= 13
    if note:
        notl = txt_lines(note, 'R', 9, CW - 28)
        cv.setFont('R', 9)
        cv.setFillColor(MUTED)
        for l in notl:
            cv.drawString(M + 22, iy, l)
            iy -= 13
    cur_y[0] -= ih


def sec_key(title):
    return 'sec_' + title.replace(' ', '_').replace('/', '_').replace('-', '_').lower()


def draw_checklist_section(sec):
    cur_sec[0] = sec['title']
    acc      = sec.get('colour', TEAL)
    subtitle = sec.get('subtitle')

    hdr_h = 44 + (17 if subtitle else 0) + (28 if sec.get('intro') else 0)
    ensure(hdr_h + item_height(*sec['items'][0][:2]) * 2)

    y = cur_y[0]
    key = sec_key(sec['title'])
    cv.bookmarkHorizontalAbsolute(key, y + 4)
    cv.addOutlineEntry(sec['title'], key, level=0)

    cv.setFillColor(acc)
    cv.rect(M + 8, y, CW - 16, 2.5, fill=1, stroke=0)
    y -= 10
    cv.setFont('RCB', 20)
    cv.setFillColor(DARK)
    cv.drawString(M + 8, y - 16, sec['title'].upper())
    y -= 34
    if subtitle:
        cv.setFont('RI', 9)
        cv.setFillColor(MUTED)
        cv.drawString(M + 8, y, subtitle)
        y -= 17
    if sec.get('intro'):
        for l in txt_lines(sec['intro'], 'RL', 9.5, CW - 20):
            cv.setFont('RL', 9.5)
            cv.setFillColor(MUTED)
            cv.drawString(M + 8, y, l)
            y -= 14
        y -= 2
    cur_y[0] = y - 5

    for name, note, opt in sec['items']:
        draw_item(name, note, opt)

    cur_y[0] -= 14


def draw_reminders():
    ensure(50)
    y = cur_y[0]

    cv.bookmarkHorizontalAbsolute('sec_reminders', y + 4)
    cv.addOutlineEntry('Key Medical Reminders', 'sec_reminders', level=0)

    cv.setFillColor(RED)
    cv.rect(M + 8, y, CW - 16, 2.5, fill=1, stroke=0)
    y -= 10
    cv.setFont('RCB', 20)
    cv.setFillColor(DARK)
    cv.drawString(M + 8, y - 16, 'KEY MEDICAL REMINDERS')
    y -= 34
    cv.setFont('RL', 9.5)
    cv.setFillColor(MUTED)
    cv.drawString(M + 8, y, 'A few things worth having in the back of your mind before you head off.')
    y -= 20
    cur_y[0] = y

    for heading, note in REMINDERS:
        note_lines = txt_lines(note, 'R', 9, CW - 28)
        ih = 14 + len(note_lines) * 12 + 10
        ensure(ih)
        y = cur_y[0]

        # Red dot marker
        cv.setFillColor(RED)
        cv.circle(M + 12, y + 3, 3, fill=1, stroke=0)
        cv.setFont('RCB', 10)
        cv.setFillColor(DARK)
        cv.drawString(M + 22, y, heading)
        y -= 14

        cv.setFont('R', 9)
        cv.setFillColor(MUTED)
        for l in note_lines:
            cv.drawString(M + 22, y, l)
            y -= 12
        cur_y[0] = y - 6

    cur_y[0] -= 14


def draw_intro_block():
    intro_lines = txt_lines(INTRO_TEXT, 'RL', 9.5, CW - 28)
    box_h = 16 + len(intro_lines) * 13 + 14
    ensure(box_h + 20)
    y = cur_y[0]
    cv.setFillColor(PALE)
    cv.roundRect(M, y - box_h, CW, box_h, 4, fill=1, stroke=0)
    cv.setFillColor(TEAL)
    cv.rect(M, y - box_h, 3, box_h, fill=1, stroke=0)
    iy = y - 14
    cv.setFont('RL', 9.5)
    cv.setFillColor(BDARK)
    for l in intro_lines:
        cv.drawString(M + 12, iy, l)
        iy -= 13
    cur_y[0] = y - box_h - 20


def draw_closing():
    ensure(80)
    y = cur_y[0]

    cv.setFillColor(TEAL)
    cv.rect(M + 8, y, CW - 16, 2.5, fill=1, stroke=0)
    y -= 28
    cur_y[0] = y

    closing_lines = txt_lines(CLOSING_TEXT, 'RL', 10, CW - 20)
    cv.setFont('RL', 10)
    cv.setFillColor(BDARK)
    for l in closing_lines:
        ensure(14)
        cv.drawString(M + 8, cur_y[0], l)
        cur_y[0] -= 14

    cur_y[0] -= 12
    ensure(44)
    cv.setFont('RB', 10)
    cv.setFillColor(TEAL)
    cv.drawString(M + 8, cur_y[0], 'Safe travels,')
    cur_y[0] -= 16
    cv.setFont('RCB', 11)
    cv.setFillColor(DARK)
    cv.drawString(M + 8, cur_y[0], 'Jason, Mareike, our daughter and Rocket')
    cur_y[0] -= 14
    cv.setFont('RC', 9)
    cv.setFillColor(MUTED)
    cv.drawString(M + 8, cur_y[0], '3xplorewithus.com')


def draw_toc():
    draw_chrome('Contents')
    y = USABLE_TOP

    cv.setFillColor(TEAL)
    cv.rect(M + 8, y, CW - 16, 2.5, fill=1, stroke=0)
    y -= 10
    cv.setFont('RCB', 20)
    cv.setFillColor(DARK)
    cv.drawString(M + 8, y - 16, 'CONTENTS')
    y -= 34

    cv.setFont('RL', 8.5)
    cv.setFillColor(MUTED)
    cv.drawString(M + 8, y, 'Tap or click any section to jump directly.')
    y -= 22

    ROW_H = 26
    entries = [(s['title'], sec_key(s['title'])) for s in CHECKLIST_SECTIONS]
    entries.append(('Key Medical Reminders', 'sec_reminders'))

    for i, (title, key) in enumerate(entries):
        row_bot = y - ROW_H
        if i % 2 == 0:
            cv.setFillColor(PALE)
            cv.roundRect(M + 8, row_bot, CW - 16, ROW_H, 2, fill=1, stroke=0)
        num_str = str(i + 1).zfill(2)
        cv.setFont('RC', 9)
        cv.setFillColor(MUTED)
        cv.drawString(M + 14, y - 16, num_str)
        cv.setFont('RCB', 10.5)
        cv.setFillColor(TEAL)
        cv.drawString(M + 44, y - 16, title)
        cv.setFont('RC', 9)
        cv.setFillColor(TEALLT)
        cv.drawRightString(W - M - 8, y - 16, '>')
        cv.setFillColor(LINE)
        cv.rect(M + 8, row_bot, CW - 16, 0.5, fill=1, stroke=0)
        cv.linkAbsolute('', key, Rect=(M + 8, row_bot, W - M - 8, y))
        y -= ROW_H


# ══════════════════════════════════════════════════════════════════════════════
# COVER PAGE
# ══════════════════════════════════════════════════════════════════════════════
cv.setFillColor(DARK)
cv.rect(0, 0, W, H, fill=1, stroke=0)
cv.setFillColor(TEAL)
cv.rect(0, 0, 5, H, fill=1, stroke=0)

# Cream header strip
cv.setFillColor(CREAM)
cv.rect(0, H - 60, W, 60, fill=1, stroke=0)
cv.setFillColor(TEAL)
cv.rect(0, H - 62, W, 2, fill=1, stroke=0)
try:
    cv.drawImage(LOGO_B, M + 8, H - 50, width=140, height=36,
                 mask='auto', preserveAspectRatio=True)
except:
    pass
draw_label('Free Download', W - M - 90, H - 36, TEAL)

# Photo placeholder
ph_top = H - 80
ph_h   = 230
cv.setFillColor(DARK3)
cv.roundRect(M, ph_top - ph_h, CW, ph_h, 3, fill=1, stroke=0)
cv.setFont('RC', 8)
cv.setFillColor(MUTED)
cv.drawCentredString(W / 2, ph_top - ph_h / 2, '[ REPLACE WITH YOUR PHOTO ]')

# Eyebrow
ey = ph_top - ph_h - 18
draw_label('3xploreWithUs  .  Free Download', M + 8, ey, TEALLT)

# Main title
ty = ey - 44
cv.setFont('RB', 34)
cv.setFillColor(CREAM)
cv.drawString(M + 8, ty, 'FIRST AID KIT')
cv.setFont('RB', 34)
cv.setFillColor(SANDLT)
cv.drawString(M + 8, ty - 40, 'NEWBORN EDITION')
cv.setFillColor(SAND)
cv.rect(M + 8, ty - 50, 68, 3, fill=1, stroke=0)

cv.setFont('RCB', 10)
cv.setFillColor(SANDLT)
cv.drawString(M + 8, ty - 68, 'European Overlanding with a Newborn')
cv.setFont('R', 9)
cv.setFillColor(MUTED)
cv.drawString(M + 8, ty - 86, '4 sections  .  Real-world tested  .  2026 Edition')

# Bottom strip
cv.setFillColor(DARK2)
cv.rect(0, 0, W, 88, fill=1, stroke=0)
cv.setFillColor(SAND)
cv.rect(0, 88, W, 1, fill=1, stroke=0)
cv.setFont('RCB', 9)
cv.setFillColor(TEALLT)
cv.drawString(M + 8, 62, 'JASON, MAREIKE and ROCKET')
cv.setFont('RL', 9)
cv.setFillColor(MUTED)
cv.drawString(M + 8, 46, 'Living life on the road, one border at a time')
cv.setFont('RC', 8)
cv.setFillColor(MUTED)
cv.drawRightString(W - M, 62, '2026 Edition')
cv.setFont('RCB', 9)
cv.setFillColor(SAND)
cv.drawRightString(W - M, 46, 'www.3xplorewithus.com')
cv.setFillColor(TEAL)
cv.rect(0, 0, W, 7, fill=1, stroke=0)

# ══════════════════════════════════════════════════════════════════════════════
# CONTENT PAGES
# ══════════════════════════════════════════════════════════════════════════════
next_page('Contents')
draw_toc()

next_page('First Aid Kit')
draw_intro_block()

for sec in CHECKLIST_SECTIONS:
    draw_checklist_section(sec)

draw_reminders()
draw_closing()

# ══════════════════════════════════════════════════════════════════════════════
# BACK COVER
# ══════════════════════════════════════════════════════════════════════════════
cv.showPage()

cv.setFillColor(DARK)
cv.rect(0, 0, W, H, fill=1, stroke=0)
cv.setFillColor(TEAL)
cv.rect(0, 0, 5, H, fill=1, stroke=0)

cv.setFont('RB', 340)
cv.setFillColor(DARK2)
cv.drawCentredString(W / 2 + 10, H / 2 - 150, 'X')

cv.setFillColor(CREAM)
cv.rect(0, H - 60, W, 60, fill=1, stroke=0)
cv.setFillColor(TEAL)
cv.rect(0, H - 62, W, 2, fill=1, stroke=0)
try:
    cv.drawImage(LOGO_B, M + 8, H - 50, width=140, height=36,
                 mask='auto', preserveAspectRatio=True)
except:
    pass

cv.setFont('RL', 11)
cv.setFillColor(MUTED)
cv.drawCentredString(W / 2, H - 88, 'Living life on the road, one border at a time.')
cv.setFillColor(SAND)
cv.rect(W / 2 - 44, H - 104, 88, 2, fill=1, stroke=0)

cv.setFont('RCB', 24)
cv.setFillColor(CREAM)
cv.drawCentredString(W / 2, H / 2 + 48, 'FOLLOW THE JOURNEY')
cv.setFont('RC', 10.5)
cv.setFillColor(TEALLT)
cv.drawCentredString(W / 2, H / 2 + 24, '@3xplorewithus  .  YouTube  .  Instagram')
cv.setFont('RCB', 14)
cv.setFillColor(SANDLT)
cv.drawCentredString(W / 2, H / 2 + 2, 'www.3xplorewithus.com')

cv.setFillColor(DARK3)
cv.rect(M + 30, H / 2 - 48, CW - 60, 1, fill=1, stroke=0)
cv.setFont('RI', 9.5)
cv.setFillColor(SAND)
cv.drawCentredString(W / 2, H / 2 - 66, 'Want more in-depth guides? Join our Patreon -- coming soon.')

cv.setFillColor(MUTED)
cv.rect(M + 60, 118, CW - 120, 1, fill=1, stroke=0)
cv.setFont('R', 8.5)
cv.setFillColor(TEALLT)
cv.drawCentredString(W / 2, 96, 'Made with love by 3xploreWithUs')
cv.setFont('R', 8)
cv.setFillColor(MUTED)
cv.drawCentredString(W / 2, 78, 'Free to share with anyone who loves adventure.')
cv.drawCentredString(W / 2, 62, '(c) 2026 3xploreWithUs - not for commercial resale')
cv.setFillColor(TEAL)
cv.rect(0, 0, W, 7, fill=1, stroke=0)

cv.showPage()
cv.save()
print('Done:', OUTPUT)
print(f'Pages: {pg_num + 2} total (cover + {pg_num} content + back cover)')
