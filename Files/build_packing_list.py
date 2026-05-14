#!/usr/bin/env python3
"""3xploreWithUs - Expedition Truck Packing List: Family of 3 + Dog Edition"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

BASE     = "/sessions/optimistic-awesome-carson/mnt/3xploreWithUs/Website"
FONT_DIR = f"{BASE}/Roboto/static"
TYPO_OTF = f"{BASE}/TypoGraphica_demo.otf"
LOGO_B   = f"{BASE}/EditingElements/logo_black.png"
OUTPUT   = "/sessions/optimistic-awesome-carson/mnt/outputs/3xWU_PackingList_FamilyDogEdition.pdf"

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
pdfmetrics.registerFont(TTFont('Typo', TYPO_OTF))

DARK   = HexColor('#0D1515')
DARK2  = HexColor('#131C1C')
DARK3  = HexColor('#1A2626')
TEAL   = HexColor('#1A9090')
TEALLT = HexColor('#5AC8C8')
SAND   = HexColor('#D4A96A')
SANDLT = HexColor('#EDD9A3')
RED    = HexColor('#B84A2F')
TEXTLT = HexColor('#EDE8DC')
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
# Each section: title, colour, intro (optional), outro (optional), subtitle (optional)
# Each item: (name, note, is_optional)


SECTIONS = [

  # 1 ── KITCHEN AND COOKING ──────────────────────────────────────────────────
  { "title": "Kitchen and Cooking", "colour": TEAL,
    "intro": "Per family of up to 4. Less is more -- we keep only what we actually cook with.",
    "outro": "What we removed: Too many plates/bowls, big rice cooker, excessive gadgets.",
    "items": [
      ("Induction or gas cooktop",
       "Induction off solar is cleaner and safer. We use gas because it came with our setup.", False),
      ("2 good knives (chef's + paring)",
       "2 quality knives beat 8 cheap ones.", False),
      ("Cast iron skillet",
       "Indestructible and doubles as a baking dish.", False),
      ("1 medium pot + 1 large pot",
       "Covers 95% of meals.", False),
      ("4x plates + 4x bowls",
       "Lightweight, unbreakable. One per person is enough.", False),
      ("4x mugs + 4x sets of cutlery",
       "Extra teaspoons -- we use them constantly.", False),
      ("Cutting board, spatula, tongs, whisk",
       "Wooden or metallic if possible.", False),
      ("1 larger stainless steel or wooden bowl",
       "For salads and mixing. More sustainable and durable than collapsible plastic.", False),
      ("Coffee setup: Moka Pot + USB-C grinder",
       "Whatever your ritual is, protect it.", False),
      ("Small electric kettle",
       "Electric if you have the power, otherwise boil water in a pot.", False),
      ("Lighter",
       "We always have a couple of lighters as well as matches.", False),
      ("Food storage: airtight containers, various sizes",
       "Glass or stainless steel preferred over plastic.", False),
      ("Dishwashing: biodegradable soap, brush, cloth/tea towels",
       "Avoid sponges -- they go mouldy fast.", False),
      ("Trash system: small bin + compost bag",
       "Our bin is 20L. Small enough to fit most bins but big enough for daily use.", False),
      ("Spices and oil in small containers",
       "Our favourites: salt, pepper, cinnamon, cumin, paprika, oregano, Italian herbs, turmeric, bay leaves.", False),
      ("12V fridge/freezer",
       "We run a 90L fridge and a separate 32L freezer. "
       "Upright fridges never give enough freezer space -- a dedicated freezer is a game-changer.", False),
      ("Pantry staples",
       "Tinned: tomatoes, tuna, beans, lentils, corn. "
       "Dried: pasta, oats, rice, flour, couscous, soy protein, chia seeds. "
       "Fresh: onion, garlic, eggs, wraps. The backbone of fast meals anywhere.", False),
    ],
  },

  # 2 ── CLOTHING AND PERSONAL ITEMS ─────────────────────────────────────────
  { "title": "Clothing and Personal Items", "colour": TEAL,
    "intro": "Per person. A small, functional wardrobe that works across climates without excess bulk.",
    "items": [
      ("6 versatile tops",
       "Easily matched. Black is best -- white is not ideal if you wash all colours together.", False),
      ("2 merino wool mid-layers",
       "One merino does the work of three synthetics.", False),
      ("1 heavy outer layer",
       "Down jacket for cold nights.", False),
      ("1 waterproof jacket", "", False),
      ("3 jeans/pants + 3-4 shorts", "", False),
      ("1 versatile smart pair",
       "For cities and border crossings.", False),
      ("10 merino/cotton/bamboo underwear",
       "Merino is best but most expensive.", False),
      ("8 pairs of merino socks", "", False),
      ("1 pair running shoes", "", False),
      ("1 pair sturdy walking/hiking shoes",
       "We use our Blundstones almost daily and hike in running shoes.", False),
      ("1 pair sandals", "", False),
      ("Swim gear", "", False),
      ("Sun hat + warm beanie",
       "Pack for both climates, always.", False),
      ("Quality sunglasses", "", False),
      ("Baby clothes",
       "Size up -- pack 2 sizes ahead, they grow fast.", False),
      ("Baby blankets + lightweight sleeping bag", "", False),
      ("Laundry: dirty laundry bag, travel detergent, Scrubba Bag",
       "The Scrubba Bag was a game changer in Australia -- extends time between laundromat trips.", False),
    ],
  },

  # 3 ── TOILETRIES AND FIRST AID ────────────────────────────────────────────
  { "title": "Toiletries and First Aid", "colour": TEAL,
    "intro": None,
    "items": [
      ("Solid shampoo + conditioner bars",
       "No spill risk, less waste, last longer, takes up less space.", False),
      ("Solid soap bar",
       "No spill risk, less waste, last longer.", False),
      ("Bamboo toothbrushes + toothpaste", "", False),
      ("Natural deodorant", "", False),
      ("Sunscreen (high SPF)", "", False),
      ("Lip balm with SPF",
       "Often forgotten, always needed.", False),
      ("Menstrual cup / reusable pads", "", False),
      ("Tweezers + nail kit", "", False),
      ("Baby toiletries",
       "Gentle wash, nappy cream, natural moisturiser.", False),
      ("Comprehensive first aid kit",
       "Build your own rather than buying a cheap pre-made one.", False),
      ("Prescription medications + surplus",
       "Always carry more than you think you need.", False),
      ("Pain relief (paracetamol + ibuprofen)", "", False),
      ("Antihistamines (tablets + cream)", "", False),
      ("Rehydration sachets",
       "More useful than expected -- especially with a baby.", False),
      ("Wound care supplies",
       "Bandages, steri-strips, antiseptic, sterile gauze.", False),
      ("Tick removal tool",
       "Especially important if you have a dog.", False),
      ("SAM splint",
       "Lightweight and can immobilise any limb.", False),
      ("Emergency foil blanket",
       "Weighs nothing. Worth everything.", False),
      ("Digital thermometer",
       "Essential with a baby.", False),
      ("Infant paracetamol + saline nasal drops", "", False),
    ],
  },

  # 4 ── BABY GEAR ───────────────────────────────────────────────────────────
  { "title": "Baby Gear", "colour": TEAL,
    "subtitle": "New Parent Overlanding Edition",
    "intro": "Prioritise multi-use and compact items. Less is better when space is limited.",
    "items": [
      ("Compact travel bassinet or bedside sleeper",
       "Plan for this when designing your interior. The space needs to adapt as the baby grows.", False),
      ("Car seat, properly mounted",
       "Check approval requirements for every country you enter.", False),
      ("Structured baby carrier + wrap/sling",
       "Two types for different ages. We bought two second-hand -- "
       "one each so neither of us has to readjust every time.", False),
      ("Portable nappy bag", "", False),
      ("Cloth nappy system + wet bags",
       "Practical with solar-powered washing; reduces waste and ongoing cost.", False),
      ("Baby clothes + muslin cloths x4+",
       "Muslin wraps: blanket, sun shade, cover, change mat -- the most versatile baby item.", False),
      ("Bottles, steriliser, breast pump (if needed)", "", False),
      ("Breastfeeding support items",
       "Pillow, nipple cream, breast pads.", False),
      ("Baby first aid and medicines",
       "Thermometer, infant paracetamol, saline nasal drops, rehydration sachets.", False),
      ("Baby nail scissors + file", "", False),
      ("Dummies + clip attachments",
       "They disappear. Have spares.", False),
      ("Soft books, rattles, teething items",
       "Keep minimal.", False),
      ("Portable high chair or booster seat", "", False),
      ("Picnic blanket / play mat",
       "A good picnic blanket works as a play mat and stays useful long after the baby stage.", False),
    ],
  },

  # 5 ── DOG GEAR ────────────────────────────────────────────────────────────
  { "title": "Dog Gear", "colour": SAND,
    "subtitle": "Rocket's Kit",
    "intro": None,
    "items": [
      ("Dog bed",
       "Their own space in the truck keeps them settled.", False),
      ("Food and water bowls", "", False),
      ("Spill-proof water bowl for the cab", "", False),
      ("Dry food storage + treats",
       "We buy in bulk -- saves money and means we only need to restock 2-3 times a year.", False),
      ("Harness, leash, long line",
       "Long lead for campsites where you want them to roam freely.", False),
      ("Dog first aid kit",
       "Tick remover, paw balm, bandages, gauze, antiseptic, vet wrap.", False),
      ("Poop bags + portable waste container",
       "Lots of poop bags.", False),
      ("Brush / grooming tools", "", False),
      ("Favourite toys (2-3)", "", False),
      ("Dog towel / blanket",
       "We have at least two dog towels for when he's wet and dirty.", False),
      ("Flea and tick prevention",
       "Essential in Australia and the tropics. We have an annual supply of his monthly pills.", False),
      ("Pet Passport and vaccination records",
       "Essential for border crossings.", False),
      ("FAVN rabies titre test paperwork",
       "Required for Australia re-entry and several other countries.", False),
      ("Cooling mat for the cab",
       "For hot climates.", True),
    ],
  },

  # 6 ── RECOVERY AND OFF-ROAD ───────────────────────────────────────────────
  { "title": "Recovery and Off-Road", "colour": RED,
    "intro": None,
    "items": [
      ("Synthetic rope", "", False),
      ("Soft shackles + tree trunk protector", "", False),
      ("Snatch straps + kinetic rope",
       "Properly rated -- not a cheap tow rope.", False),
      ("Traction boards (aluminium, MaxTrax or similar)",
       "Sand, mud, snow -- changes everything.", False),
      ("Shovel (foldable)", "", False),
      ("Tyre repair kit + 12V compressor", "", False),
      ("Hi-Lift jack + base plate",
       "Standard jack is useless in soft ground.", False),
      ("2 full-size spare tyres",
       "One is a necessity; two is peace of mind. Our second spare is currently "
       "not on the truck -- shame on us.", False),
    ],
  },

  # 7 ── TOOLS AND VEHICLE MAINTENANCE ──────────────────────────────────────
  { "title": "Tools and Vehicle Maintenance", "colour": RED,
    "intro": "Adjust spares and tools to your specific vehicle.",
    "items": [
      ("Comprehensive tool kit",
       "Make sure you know what you need for your vehicle.", False),
      ("Multimeter + electrical tools, wire, fuses, connectors",
       "Electrical gremlins will happen. Be ready.", False),
      ("Vehicle-specific spares: filters, belts, hoses, fuses", "", False),
      ("WD-40, duct tape, zip ties, wire",
       "Will save you more times than you expect.", False),
      ("Tyre pressure gauge + deflator", "", False),
      ("Engine oil + coolant", "", False),
      ("Torque wrench", "", False),
      ("Head torch",
       "For working under the truck at night.", False),
      ("Work gloves",
       "For dirty jobs, recovery, firewood.", False),
      ("Spare bolts and screws",
       "You never know when they come in handy.", False),
      ("Spare ratchet straps", "", False),
    ],
  },

  # 8 ── LIVING AND COMFORT ──────────────────────────────────────────────────
  { "title": "Living and Comfort", "colour": TEAL,
    "intro": None,
    "items": [
      ("Quality sleeping bags / duvet setup",
       "We have a 3-in-1 duvet for all seasons. If that's still not warm enough, "
       "we put a throw on top.", False),
      ("Fitted sheets (x2)",
       "Right size for your mattress. Take 2 so one can be washed while you use the other.", False),
      ("Good mattress or topper", "", False),
      ("2 lightweight camp chairs",
       "You use these every single day.", False),
      ("Compact folding table",
       "Eating off your lap gets old fast.", False),
      ("Awning",
       "For shade and rain protection.", False),
      ("Lanterns + string lights",
       "Makes camp feel like home. Underrated.", False),
      ("Outdoor mat",
       "Keeps the truck floor clean.", False),
      ("Fire kit: lighter, waterproof matches, firestarter", "", False),
      ("Water filter or purification tablets",
       "Backup when the tank runs low.", False),
      ("Jerry cans (water + fuel)",
       "Capacity depends on your range requirements.", False),
      ("Books, cards, games",
       "Our favourites: backgammon, Monopoly Deal, Uno, and a normal card deck. "
       "We both have a Kindle -- takes up way less room than physical books. "
       "Not quite the same feeling but a good compromise.", False),
      ("Blackout window covers",
       "Essential in cities and for babies. Doubles as privacy screening.", True),
      ("Baby sleeping setup (bassinet or co-sleeper)",
       "Plan the space when designing your interior.", True),
      ("Hammock",
       "Lightest luxury item you will ever pack. We never used ours in the Troopy "
       "so we have not brought it in the truck yet.", True),
      ("Outdoor shower", "", True),
      ("Outdoor kitchen / BBQ", "", True),
    ],
  },

  # 9 ── SAFETY AND EMERGENCY ────────────────────────────────────────────────
  { "title": "Safety and Emergency", "colour": RED,
    "intro": None,
    "items": [
      ("Fire extinguishers (cab + living area)",
       "Mounted and accessible at all times.", False),
      ("Carbon monoxide + smoke detectors", "", False),
      ("Satellite communicator (Garmin inReach or similar)",
       "Non-negotiable with a baby in remote areas. Two-way messaging from anywhere.", False),
      ("USB-C headlamps x2",
       "One per person, always.", False),
      ("Emergency cash",
       "Cards fail. Cash is universal.", False),
    ],
  },

  # 10 ── ELECTRONICS AND POWER ─────────────────────────────────────────────
  { "title": "Electronics and Power", "colour": TEAL,
    "intro": None,
    "items": [
      ("Electric set-up that suits your needs",
       "Mounted solar panels, portable ones, battery, USB charging outlets. "
       "We may create a separate detailed guide on how to work out what you need "
       "and how to wire it all up.", False),
      ("Laptop + chargers", "", False),
      ("Starlink",
       "Game-changer for remote connectivity and working on the road.", False),
      ("Camera kit + drone", "", False),
      ("External hard drives",
       "For footage backup. Keep one copy off-site if possible.", False),
      ("Multi-country power adapter set", "", False),
    ],
  },

  # 11 ── DOCUMENTS AND ADMIN ────────────────────────────────────────────────
  { "title": "Documents and Admin", "colour": TEAL,
    "intro": None,
    "items": [
      ("Passports (including baby)",
       "Check validity -- many countries require 6+ months remaining.", False),
      ("Vehicle documents + Carnet de Passage",
       "Originals and copies.", False),
      ("International driving permits (both drivers)", "", False),
      ("Birth certificate + baby's certified copies", "", False),
      ("Travel insurance policy documents", "", False),
      ("Vaccination records (family and Rocket)", "", False),
      ("Emergency cash + digital backups",
       "Cards fail. Cash is universal. Cloud storage + USB backup.", False),
      ("Printed emergency contacts list",
       "Do not rely only on your phone.", False),
    ],
  },

  # 12 ── NAVIGATION ─────────────────────────────────────────────────────────
  { "title": "Navigation", "colour": TEAL,
    "intro": None,
    "items": [
      ("Offline maps: OsmAnd / Maps.me",
       "Download before leaving signal range.", False),
      ("Dedicated GPS device",
       "Phone dies. GPS does not.", False),
      ("Compass",
       "Irreplaceable when electronics fail.", False),
      ("Local SIM cards",
       "Buy on arrival in each country.", False),
      ("Satellite communicator",
       "Like Garmin inReach. Two-way messaging from anywhere. See Safety section.", False),
      ("Paper road atlas",
       "When data fails, paper works.", True),
    ],
  },
]

# ── SEASONAL AND TIPS ─────────────────────────────────────────────────────────
SEASONAL_SECTION = [
  {
    "label": "Australia (Hot / Wet Season)",
    "colour": TEAL,
    "items": [
      "Extra insect protection, shade solutions, water storage",
      "Fly nets -- there are flies absolutely everywhere",
      "Light clothing + quick-dry items",
    ]
  },
  {
    "label": "Europe (Cold / Rainy / Winter)",
    "colour": TEALLT,
    "items": [
      "Heavy insulation layers, good waterproofing",
      "Snow chains or socks (if needed)",
      "More heating solutions + dehumidifier",
    ]
  },
]

FINAL_TIPS = [
  ("Weight is everything",
   "Prioritise multi-purpose items. Test everything on short trips first."),
  ("With a baby",
   "Focus on quick setup and teardown systems. Every minute counts at camp."),
]

FINAL_THOUGHTS = (
    "Weight and space management is always important when camping. We regularly do 'purge rounds' "
    "and remove items we haven't used in months. This list is what works for us -- use it as a "
    "starting point and adapt it to your own truck, climate, and family. Feel free to share your "
    "thoughts, recommendations and ideas with us. We're always keen to learn."
)

INTRO_TEXT = (
    "After 30,000+ km across Australia and now preparing for full-time family life in Europe, "
    "this is our refined, real-world packing list. We focus on minimalism with redundancy -- "
    "only keeping what we actually use. We try to live sustainably by reducing the use of "
    "plastic, synthetics and single-use items. This list continues to evolve as our daughter grows."
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
    return 'sec_' + title.replace(' ', '_').replace('/', '_').lower()


def draw_section(sec):
    cur_sec[0] = sec['title']
    acc      = sec.get('colour', TEAL)
    subtitle = sec.get('subtitle')
    outro    = sec.get('outro')

    hdr_h = 44 + (17 if subtitle else 0) + (32 if sec.get('intro') else 0)
    ensure(hdr_h + item_height(*sec['items'][0][:2]) * 2)

    y = cur_y[0]

    # Bookmark this position for TOC links and PDF outline
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
        if not opt:
            draw_item(name, note, False)

    opt_items = [(n, nt) for n, nt, o in sec['items'] if o]
    if opt_items:
        ensure(28)
        cv.setFillColor(LINE)
        cv.rect(M + 8, cur_y[0], CW - 16, 0.8, fill=1, stroke=0)
        cur_y[0] -= 10
        draw_label('optional', M + 8, cur_y[0], MUTED)
        cur_y[0] -= 14
        for name, note in opt_items:
            draw_item(name, note, True)

    if outro:
        ensure(28)
        outro_lines = txt_lines(outro, 'RI', 8.5, CW - 20)
        box_h = len(outro_lines) * 13 + 12
        cv.setFillColor(PALE)
        cv.roundRect(M + 8, cur_y[0] - box_h, CW - 16, box_h, 3, fill=1, stroke=0)
        iy = cur_y[0] - 10
        cv.setFont('RI', 8.5)
        cv.setFillColor(MUTED)
        for l in outro_lines:
            cv.drawString(M + 16, iy, l)
            iy -= 13
        cur_y[0] -= box_h + 4

    cur_y[0] -= 14


def draw_intro_block():
    intro_lines = txt_lines(INTRO_TEXT, 'RL', 9, CW - 28)
    box_h = 16 + 15 + 14 + len(intro_lines) * 12 + 14
    ensure(box_h + 20)
    y = cur_y[0]
    cv.setFillColor(PALE)
    cv.roundRect(M, y - box_h, CW, box_h, 4, fill=1, stroke=0)
    cv.setFillColor(TEAL)
    cv.rect(M, y - box_h, 3, box_h, fill=1, stroke=0)
    iy = y - 14
    draw_label('Steyr 12M18 Expedition Camper', M + 12, iy, TEAL)
    iy -= 16
    cv.setFont('RB', 10)
    cv.setFillColor(BDARK)
    cv.drawString(M + 12, iy, 'Jason, Mareike, our daughter and Rocket')
    iy -= 15
    cv.setFont('RL', 9)
    cv.setFillColor(MUTED)
    for l in intro_lines:
        cv.drawString(M + 12, iy, l)
        iy -= 12
    cur_y[0] = y - box_h - 22


def draw_seasonal():
    ensure(50)
    y = cur_y[0]

    cv.bookmarkHorizontalAbsolute('sec_seasonal_variations', y + 4)
    cv.addOutlineEntry('Seasonal Variations', 'sec_seasonal_variations', level=0)

    cv.setFillColor(TEAL)
    cv.rect(M + 8, y, CW - 16, 2.5, fill=1, stroke=0)
    y -= 10
    cv.setFont('RCB', 20)
    cv.setFillColor(DARK)
    cv.drawString(M + 8, y - 16, 'SEASONAL VARIATIONS')
    y -= 38
    cur_y[0] = y

    for data in SEASONAL_SECTION:
        n_lines = sum(len(txt_lines(i, 'R', 9.5, CW - 36)) for i in data['items'])
        needed = 18 + n_lines * 13 + 12
        ensure(needed)
        y = cur_y[0]
        cv.setFillColor(data['colour'])
        cv.circle(M + 12, y + 3.5, 3.5, fill=1, stroke=0)
        cv.setFont('RCB', 10)
        cv.setFillColor(DARK)
        cv.drawString(M + 22, y, data['label'])
        y -= 16
        for item in data['items']:
            lines = txt_lines(item, 'R', 9.5, CW - 36)
            cv.setFillColor(MUTED)
            cv.circle(M + 22, y + 3, 2, fill=1, stroke=0)
            cv.setFont('R', 9.5)
            cv.setFillColor(BDARK)
            for l in lines:
                cv.drawString(M + 30, y, l)
                y -= 13
        y -= 8
        cur_y[0] = y

    cur_y[0] -= 14


def draw_final_tips():
    ensure(50)
    y = cur_y[0]

    cv.bookmarkHorizontalAbsolute('sec_final_tips', y + 4)
    cv.addOutlineEntry('Final Tips', 'sec_final_tips', level=0)

    cv.setFillColor(SAND)
    cv.rect(M + 8, y, CW - 16, 2.5, fill=1, stroke=0)
    y -= 10
    cv.setFont('RCB', 20)
    cv.setFillColor(DARK)
    cv.drawString(M + 8, y - 16, 'FINAL TIPS')
    y -= 38
    cur_y[0] = y

    for heading, note in FINAL_TIPS:
        note_lines = txt_lines(note, 'R', 9, CW - 28) if note else []
        ih = 14 + len(note_lines) * 12 + 8
        ensure(ih)
        y = cur_y[0]
        cv.setFont('RCB', 10)
        cv.setFillColor(TEAL)
        cv.drawString(M + 8, y, heading + ':')
        y -= 14
        if note_lines:
            cv.setFont('R', 9)
            cv.setFillColor(MUTED)
            for l in note_lines:
                cv.drawString(M + 22, y, l)
                y -= 12
        cur_y[0] = y - 6

    cur_y[0] -= 14


def draw_final_thoughts():
    """Closing personal note before the back cover."""
    ensure(100)
    y = cur_y[0]

    # Teal accent bar
    cv.setFillColor(TEAL)
    cv.rect(M + 8, y, CW - 16, 2.5, fill=1, stroke=0)
    y -= 32
    cur_y[0] = y  # sync so body text starts below the bar

    # Body text
    body_lines = txt_lines(FINAL_THOUGHTS, 'RL', 10, CW - 20)
    cv.setFont('RL', 10)
    cv.setFillColor(BDARK)
    for l in body_lines:
        ensure(14)
        cv.drawString(M + 8, cur_y[0], l)
        cur_y[0] -= 14

    cur_y[0] -= 10

    # Sign-off
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
    cur_y[0] -= 20


def draw_toc():
    """Clickable table of contents page."""
    ROW_H   = 26        # height per entry
    NUM_W   = 30        # width for the section number column
    ARROW_W = 18        # right-side arrow

    # Build entry list: all SECTIONS + seasonal + tips
    entries = [(s['title'], sec_key(s['title'])) for s in SECTIONS]
    entries.append(('Seasonal Variations', 'sec_seasonal_variations'))
    entries.append(('Final Tips',          'sec_final_tips'))

    # Page chrome
    draw_chrome('Contents')

    y = USABLE_TOP

    # TOC heading
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

    # Entries
    for i, (title, key) in enumerate(entries):
        is_special = title in ('Seasonal Variations', 'Final Tips')
        row_top    = y
        row_bot    = y - ROW_H

        # Alternating very light background
        if i % 2 == 0:
            cv.setFillColor(PALE)
            cv.roundRect(M + 8, row_bot, CW - 16, ROW_H, 2, fill=1, stroke=0)

        # Number
        num_str = str(i + 1).zfill(2)
        cv.setFont('RC', 9)
        cv.setFillColor(OPTCLR if is_special else MUTED)
        cv.drawString(M + 14, y - 16, num_str)

        # Title — teal to signal clickability
        cv.setFont('RCB' if not is_special else 'R', 10.5 if not is_special else 10)
        cv.setFillColor(TEAL if not is_special else MUTED)
        cv.drawString(M + 14 + NUM_W, y - 16, title)

        # Arrow
        cv.setFont('RC', 9)
        cv.setFillColor(TEALLT)
        cv.drawRightString(W - M - 8, y - 16, '>')

        # Thin separator line
        cv.setFillColor(LINE)
        cv.rect(M + 8, row_bot, CW - 16, 0.5, fill=1, stroke=0)

        # Invisible clickable rectangle over the whole row
        cv.linkAbsolute('', key, Rect=(M + 8, row_bot, W - M - 8, row_top))

        y -= ROW_H

    # Bottom note
    y -= 6
    cv.setFont('RI', 8)
    cv.setFillColor(MUTED)
    cv.drawCentredString(W / 2, y, 'Sections marked optional are nice-to-haves, not essentials.')


# ══════════════════════════════════════════════════════════════════════════════
# COVER PAGE
# ══════════════════════════════════════════════════════════════════════════════
cv.setFillColor(DARK)
cv.rect(0, 0, W, H, fill=1, stroke=0)
cv.setFillColor(TEAL)
cv.rect(0, 0, 5, H, fill=1, stroke=0)

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

ph_top = H - 80
ph_h   = 230
cv.setFillColor(DARK3)
cv.roundRect(M, ph_top - ph_h, CW, ph_h, 3, fill=1, stroke=0)
cv.setFont('RC', 8)
cv.setFillColor(MUTED)
cv.drawCentredString(W / 2, ph_top - ph_h / 2, '[ REPLACE WITH YOUR PHOTO ]')

ey = ph_top - ph_h - 18
draw_label('3xploreWithUs  .  Free Download', M + 8, ey, TEALLT)

ty = ey - 50
cv.setFont('RB', 34)
cv.setFillColor(CREAM)
cv.drawString(M + 8, ty, 'EXPEDITION TRUCK')
cv.setFont('RB', 34)
cv.setFillColor(SANDLT)
cv.drawString(M + 8, ty - 40, 'PACKING LIST')
cv.setFillColor(SAND)
cv.rect(M + 8, ty - 54, 68, 3, fill=1, stroke=0)

cv.setFont('RCB', 11)
cv.setFillColor(SANDLT)
cv.drawString(M + 8, ty - 74, 'Family of 3 + Dog Edition')
cv.setFont('R', 9)
cv.setFillColor(MUTED)
cv.drawString(M + 8, ty - 94, '12 categories  .  150+ items  .  Real-world tested')

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

next_page('Packing List')
draw_intro_block()

for sec in SECTIONS:
    draw_section(sec)

draw_seasonal()
draw_final_tips()
draw_final_thoughts()

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
