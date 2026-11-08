"""
MEEN MANIFESTATION - Luxury Packaging & Label Suite
REPLACES the MM Monogram with the Official Circular Stitched Medallion Seal across all 8 assets.
"""

from generate_meen_fish_vector import get_defs_with_blush
from generate_meen_circular_seal import get_circular_seal_svg

# -------------------------------------------------------------
# ASSET 1: LUXURY SHOPPING BAG (Circular Stitched Medallion Seal)
# -------------------------------------------------------------
def generate_updated_shopping_bag():
    defs = get_defs_with_blush()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1200" width="1000" height="1200">
  {defs}
  <rect width="1000" height="1200" fill="#ECE7DE" />
  
  <!-- Backdrop subtle pedestal shadow -->
  <ellipse cx="500" cy="1120" rx="380" ry="32" fill="#1A1815" opacity="0.12" filter="url(#softShadow)" />

  <!-- 3D Bag Side Gusset Perspective -->
  <polygon points="210,320 270,270 270,970 210,1050" fill="#E2DDD1" />
  <line x1="240" y1="295" x2="240" y2="1010" stroke="#B8B0A0" stroke-width="1.2" stroke-dasharray="1 1" opacity="0.6"/>

  <!-- Bag Main Front Body (Matte Ivory #F8F7F3) -->
  <polygon points="270,270 790,270 790,990 270,990" fill="#F8F7F3" filter="url(#softShadow)" />

  <!-- Top Turned In Flap & Crease -->
  <line x1="270" y1="271" x2="790" y2="271" stroke="#FFFFFF" stroke-width="2" />
  <line x1="270" y1="330" x2="790" y2="330" stroke="#E3DDCF" stroke-width="0.8" opacity="0.7" />

  <!-- Braided Cotton Rope Handles -->
  <path d="M 400 270 C 400 70, 660 70, 660 270" fill="none" stroke="#DCD5C5" stroke-width="17" stroke-linecap="round" />
  <circle cx="410" cy="330" r="8" fill="url(#champagneFoil)" />
  <circle cx="650" cy="330" r="8" fill="url(#champagneFoil)" />
  <path d="M 410 330 C 410 110, 650 110, 650 330" fill="none" stroke="#EFE9DC" stroke-width="18" stroke-linecap="round" filter="url(#softShadow)" />
  <path d="M 410 330 C 410 110, 650 110, 650 330" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="4 4" opacity="0.6" />

  <!-- BRANDING: CIRCULAR STITCHED CELESTIAL FISH MEDALLION SEAL -->
  <g transform="translate(530, 600)">
    <!-- The Medallion Seal -->
    {get_circular_seal_svg(cx=0, cy=0, r=185, scale=0.95, color="url(#champagneFoil)", text_color="#252525")}

    <!-- Dividing Rule in Champagne Gold Foil -->
    <line x1="-120" y1="190" x2="120" y2="190" stroke="url(#champagneFoilHoriz)" stroke-width="1.2" />

    <!-- Brand Slogan -->
    <text x="0" y="218" font-family="'Montserrat', sans-serif" font-size="10" fill="#B49A70" letter-spacing="0.38em" text-anchor="middle" font-weight="500">NOT JUST FASHION. A STATEMENT OF IDENTITY.</text>

    <!-- Base Origin -->
    <text x="0" y="325" font-family="'Montserrat', sans-serif" font-size="8" fill="#A89E8D" letter-spacing="0.35em" text-anchor="middle">DESIGNED BY HARSHIT PARGAIN</text>
  </g>

  <!-- Technical Spec Watermark -->
  <text x="50" y="60" font-family="'Cinzel', serif" font-size="14" fill="#252525" letter-spacing="0.25em" font-weight="700">ASSET 01 // LUXURY SHOPPING BAG</text>
  <text x="50" y="85" font-family="'Montserrat', sans-serif" font-size="9" fill="#7A7265" letter-spacing="0.15em">SPECIFICATION: 320GSM MATTE IVORY • CIRCULAR STITCHED CELESTIAL FISH SEAL • COTTON ROPE HANDLES</text>
</svg>'''
    with open("assets/packaging/01_luxury_shopping_bag_front.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# ASSET 2: PREMIUM RIGID CLOTHING BOX (Circular Stitched Seal)
# -------------------------------------------------------------
def generate_updated_clothing_box():
    defs = get_defs_with_blush()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" width="1200" height="900">
  {defs}
  <rect width="1200" height="900" fill="#F8F7F3" />

  <text x="80" y="70" font-family="'Cinzel', serif" font-size="14" fill="#252525" letter-spacing="0.25em" font-weight="700">ASSET 02 // PREMIUM RIGID CLOTHING BOX</text>
  <text x="80" y="95" font-family="'Montserrat', sans-serif" font-size="9" fill="#7A7265" letter-spacing="0.15em">SPECIFICATION: 1800GSM RIGID GREYBOARD • LINEN-FINISH BEIGE #EDE8DF • CIRCULAR STITCHED FOIL SEAL • VELVET LINING</text>

  <!-- LEFT: CLOSED RIGID CLOTHING BOX -->
  <g transform="translate(60, 140)">
    <rect x="30" y="40" width="460" height="580" rx="6" fill="#14120E" opacity="0.12" filter="url(#softShadow)" />
    <rect x="20" y="30" width="460" height="580" rx="6" fill="#EDE8DF" stroke="#DDD6C8" stroke-width="1.5" />

    <!-- Magnetic Flap Closure -->
    <line x1="460" y1="30" x2="460" y2="610" stroke="#C5BDAE" stroke-width="1.5" />
    <circle cx="470" cy="320" r="4" fill="url(#champagneFoil)" />

    <!-- Subtle Beveled Lid Frame Line -->
    <rect x="45" y="55" width="410" height="530" rx="3" fill="none" stroke="url(#champagneFoil)" stroke-width="0.8" opacity="0.35" />

    <!-- Centered Circular Stitched Celestial Fish Medallion Seal (Foil Stamped) -->
    {get_circular_seal_svg(cx=250, cy=300, r=185, scale=0.72, color="url(#champagneFoil)", text_color="#252525")}

    <line x1="190" y1="445" x2="310" y2="445" stroke="url(#champagneFoilHoriz)" stroke-width="0.8" />
    <text x="250" y="468" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#B49A70" letter-spacing="0.4em" text-anchor="middle">A STATEMENT OF IDENTITY</text>

    <text x="250" y="660" font-family="'Montserrat', sans-serif" font-size="11" fill="#736A5B" letter-spacing="0.25em" text-anchor="middle" font-weight="600">FIG 2.1 — EXTERIOR CLOSED MAGNETIC PRESENTATION</text>
  </g>

  <!-- RIGHT: OPEN BOX INTERIOR PRESENTATION -->
  <g transform="translate(620, 140)">
    <rect x="30" y="40" width="480" height="580" rx="6" fill="#14120E" opacity="0.14" filter="url(#softShadow)" />
    <rect x="20" y="30" width="480" height="580" rx="6" fill="#D9D2C4" stroke="#B8B0A0" stroke-width="1.5" />

    <rect x="35" y="45" width="450" height="550" rx="4" fill="#F8F7F3" stroke="#DDD6CA" stroke-width="1" />

    <!-- Folded Garment in Tissue Paper -->
    <rect x="50" y="60" width="420" height="520" rx="3" fill="#FFFFFF" />

    <!-- Repeating Circular Stitched Seals on Tissue -->
    {get_circular_seal_svg(cx=120, cy=110, r=185, scale=0.28, color="#B49A70", text_color="#B49A70")}
    {get_circular_seal_svg(cx=260, cy=110, r=185, scale=0.28, color="#B49A70", text_color="#B49A70")}
    {get_circular_seal_svg(cx=400, cy=110, r=185, scale=0.28, color="#B49A70", text_color="#B49A70")}

    {get_circular_seal_svg(cx=190, cy=200, r=185, scale=0.28, color="#B49A70", text_color="#B49A70")}
    {get_circular_seal_svg(cx=330, cy=200, r=185, scale=0.28, color="#B49A70", text_color="#B49A70")}

    {get_circular_seal_svg(cx=120, cy=290, r=185, scale=0.28, color="#B49A70", text_color="#B49A70")}
    {get_circular_seal_svg(cx=260, cy=290, r=185, scale=0.28, color="#B49A70", text_color="#B49A70")}
    {get_circular_seal_svg(cx=400, cy=290, r=185, scale=0.28, color="#B49A70", text_color="#B49A70")}

    <polygon points="50,60 470,60 470,580" fill="#FAF8F5" opacity="0.55" />

    <!-- Charcoal Woven Ribbon Belt across Folded Garment -->
    <rect x="50" y="300" width="420" height="42" fill="#252525" filter="url(#softShadow)" />
    <line x1="50" y1="300" x2="470" y2="300" stroke="url(#champagneFoil)" stroke-width="0.8" />
    <line x1="50" y1="342" x2="470" y2="342" stroke="url(#champagneFoil)" stroke-width="0.8" />
    <text x="260" y="326" font-family="'Cinzel', serif" font-size="11" fill="url(#champagneFoil)" letter-spacing="0.32em" text-anchor="middle" font-weight="600">MEEN MANIFESTATION</text>

    <!-- Embossed Circular Stitched Medallion Foil Sticker Seal -->
    <g transform="translate(260, 321)">
      <circle cx="0" cy="0" r="38" fill="url(#goldSheen)" filter="url(#softShadow)" />
      {get_circular_seal_svg(cx=0, cy=0, r=185, scale=0.19, color="#FFFFFF", text_color="#FFFFFF")}
    </g>

    <text x="260" y="660" font-family="'Montserrat', sans-serif" font-size="11" fill="#736A5B" letter-spacing="0.25em" text-anchor="middle" font-weight="600">FIG 2.2 — INTERIOR UNBOXING &amp; CIRCULAR FOIL SEAL</text>
  </g>
</svg>'''
    with open("assets/packaging/02_rigid_clothing_box_presentation.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# ASSET 3: CLOTHING HANG TAGS (Circular Stitched Seal)
# -------------------------------------------------------------
def generate_updated_hang_tags():
    defs = get_defs_with_blush()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 850" width="1100" height="850">
  {defs}
  <rect width="1100" height="850" fill="#F8F7F3" />

  <text x="70" y="60" font-family="'Cinzel', serif" font-size="14" fill="#252525" letter-spacing="0.25em" font-weight="700">ASSET 03 // CLOTHING HANG TAGS (DOUBLE-SIDED)</text>
  <text x="70" y="85" font-family="'Montserrat', sans-serif" font-size="9" fill="#7A7265" letter-spacing="0.15em">SPECIFICATION: 650GSM DUPLEX BOARD • BEVELED GILDED CHAMPAGNE EDGES • CIRCULAR STITCHED MEDALLION SEAL</text>

  <!-- Waxed Cord & Safety Pin -->
  <path d="M 285 140 C 285 90, 480 70, 550 90 C 620 110, 815 90, 815 140" fill="none" stroke="#DDD2C0" stroke-width="3" filter="url(#softShadow)" />
  <g transform="translate(530, 75) rotate(-15)">
    <rect x="0" y="0" width="45" height="7" rx="3" fill="url(#champagneFoil)" />
    <circle cx="6" cy="3.5" r="5" fill="none" stroke="url(#champagneFoil)" stroke-width="2" />
    <line x1="6" y1="3.5" x2="42" y2="3.5" stroke="#8E7348" stroke-width="1.5" />
    <text x="24" y="5.5" font-family="'Cinzel', serif" font-size="4" fill="#252525" font-weight="700">MEEN</text>
  </g>

  <!-- FRONT OF HANG TAG -->
  <g transform="translate(150, 140)">
    <rect x="-3" y="-3" width="276" height="526" rx="10" fill="url(#champagneFoil)" filter="url(#softShadow)" />
    <rect x="0" y="0" width="270" height="520" rx="8" fill="#F8F7F3" />

    <circle cx="135" cy="40" r="14" fill="url(#champagneFoil)" />
    <circle cx="135" cy="40" r="8" fill="#F8F7F3" stroke="#8A7046" stroke-width="1.2" />

    <rect x="18" y="70" width="234" height="425" rx="4" fill="none" stroke="url(#champagneFoil)" stroke-width="0.8" opacity="0.4" />

    <!-- Centered Circular Stitched Medallion Seal -->
    {get_circular_seal_svg(cx=135, cy=240, r=185, scale=0.55, color="url(#champagneFoil)", text_color="#252525")}

    <line x1="95" y1="365" x2="175" y2="365" stroke="url(#champagneFoilHoriz)" stroke-width="1" />
    <text x="135" y="388" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#B49A70" letter-spacing="0.42em" text-anchor="middle" font-weight="500">A STATEMENT OF IDENTITY</text>

    <text x="135" y="445" font-family="'Cinzel', serif" font-size="9" fill="#888173" letter-spacing="0.3em" text-anchor="middle">COLLECTION 01</text>
    <text x="135" y="465" font-family="'Montserrat', sans-serif" font-size="7" fill="#AAA191" letter-spacing="0.32em" text-anchor="middle">AUTUMN / WINTER 2026</text>

    <text x="135" y="555" font-family="'Montserrat', sans-serif" font-size="10" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">FRONT — CIRCULAR MEDALLION SEAL</text>
  </g>

  <!-- BACK OF HANG TAG -->
  <g transform="translate(680, 140)">
    <rect x="-3" y="-3" width="276" height="526" rx="10" fill="url(#champagneFoil)" filter="url(#softShadow)" />
    <rect x="0" y="0" width="270" height="520" rx="8" fill="#F8F7F3" />

    <circle cx="135" cy="40" r="14" fill="url(#champagneFoil)" />
    <circle cx="135" cy="40" r="8" fill="#F8F7F3" stroke="#8A7046" stroke-width="1.2" />

    <text x="135" y="85" font-family="'Cinzel', serif" font-size="11" fill="#252525" letter-spacing="0.3em" text-anchor="middle" font-weight="600">MEEN MANIFESTATION</text>
    <line x1="25" y1="100" x2="245" y2="100" stroke="#DDD6C8" stroke-width="0.8" />

    <text x="28" y="125" font-family="'Montserrat', sans-serif" font-size="7" fill="#8C8373" letter-spacing="0.2em">COLLECTION</text>
    <text x="28" y="142" font-family="'Cinzel', serif" font-size="10.5" fill="#252525" letter-spacing="0.1em" font-weight="600">MANIFESTATION N° 01</text>

    <text x="28" y="170" font-family="'Montserrat', sans-serif" font-size="7" fill="#8C8373" letter-spacing="0.2em">ARTICLE / STYLE</text>
    <text x="28" y="187" font-family="'Cinzel', serif" font-size="10" fill="#252525">TAILORED COAT // MM-014</text>

    <!-- Size Matrix -->
    <text x="28" y="218" font-family="'Montserrat', sans-serif" font-size="7" fill="#8C8373" letter-spacing="0.2em">GARMENT SIZE</text>
    <g transform="translate(26, 226)">
      <rect x="0" y="0" width="38" height="28" rx="2" fill="#FFFFFF" stroke="#DDD6C8" stroke-width="0.8" />
      <text x="19" y="18" font-family="'Montserrat', sans-serif" font-size="9" fill="#999999" text-anchor="middle">XS</text>
      <rect x="44" y="0" width="38" height="28" rx="2" fill="#FFFFFF" stroke="#DDD6C8" stroke-width="0.8" />
      <text x="63" y="18" font-family="'Montserrat', sans-serif" font-size="9" fill="#999999" text-anchor="middle">S</text>
      <rect x="88" y="0" width="38" height="28" rx="2" fill="#252525" stroke="url(#champagneFoil)" stroke-width="1.2" />
      <text x="107" y="19" font-family="'Montserrat', sans-serif" font-size="10" fill="#F8F7F3" text-anchor="middle" font-weight="700">M</text>
      <rect x="132" y="0" width="38" height="28" rx="2" fill="#FFFFFF" stroke="#DDD6C8" stroke-width="0.8" />
      <text x="151" y="18" font-family="'Montserrat', sans-serif" font-size="9" fill="#999999" text-anchor="middle">L</text>
      <rect x="176" y="0" width="38" height="28" rx="2" fill="#FFFFFF" stroke="#DDD6C8" stroke-width="0.8" />
      <text x="195" y="18" font-family="'Montserrat', sans-serif" font-size="9" fill="#999999" text-anchor="middle">XL</text>
    </g>

    <text x="28" y="280" font-family="'Montserrat', sans-serif" font-size="7" fill="#8C8373" letter-spacing="0.2em">COMPOSITION</text>
    <text x="28" y="296" font-family="'Montserrat', sans-serif" font-size="8.5" fill="#252525" font-weight="500">100% ITALIAN CASHMERE</text>
    <text x="28" y="310" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#756D60">LINING: 100% MULBERRY SILK</text>

    <!-- QR Code & Digital Passport -->
    <g transform="translate(28, 332)">
      <rect x="0" y="0" width="85" height="85" fill="#FFFFFF" stroke="#DDD6C8" stroke-width="1" />
      <rect x="8" y="8" width="24" height="24" fill="#252525" />
      <rect x="12" y="12" width="16" height="16" fill="#FFFFFF" />
      <rect x="15" y="15" width="10" height="10" fill="#252525" />
      <rect x="53" y="8" width="24" height="24" fill="#252525" />
      <rect x="57" y="12" width="16" height="16" fill="#FFFFFF" />
      <rect x="60" y="15" width="10" height="10" fill="#252525" />
      <rect x="8" y="53" width="24" height="24" fill="#252525" />
      <rect x="12" y="57" width="16" height="16" fill="#FFFFFF" />
      <rect x="15" y="60" width="10" height="10" fill="#252525" />
      <rect x="36" y="10" width="6" height="18" fill="#252525" />
      <rect x="36" y="34" width="14" height="6" fill="#252525" />
      <rect x="54" y="36" width="22" height="6" fill="#252525" />
      <rect x="38" y="46" width="6" height="20" fill="#252525" />
      <rect x="52" y="50" width="18" height="12" fill="#252525" />

      <text x="96" y="24" font-family="'Montserrat', sans-serif" font-size="7" fill="#252525" font-weight="700">SCAN TO VERIFY</text>
      <text x="96" y="38" font-family="'Montserrat', sans-serif" font-size="6.5" fill="#888173">DIGITAL PASSPORT &amp;</text>
      <text x="96" y="50" font-family="'Montserrat', sans-serif" font-size="6.5" fill="#888173">CERTIFICATE OF</text>
      <text x="96" y="62" font-family="'Montserrat', sans-serif" font-size="6.5" fill="#888173">AUTHENTICITY</text>
      <text x="96" y="78" font-family="'Montserrat', sans-serif" font-size="6" fill="#B49A70" font-weight="600">ID: MEEN-2026-90412</text>
    </g>

    <line x1="25" y1="440" x2="245" y2="440" stroke="#DDD6C8" stroke-width="0.8" />
    <text x="135" y="465" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#857C6D" letter-spacing="0.25em" text-anchor="middle">CRAFTED IN ITALY</text>
    <text x="135" y="480" font-family="'Montserrat', sans-serif" font-size="6.5" fill="#A8A193" letter-spacing="0.2em" text-anchor="middle">WWW.MEENMANIFESTATION.COM</text>

    <text x="135" y="555" font-family="'Montserrat', sans-serif" font-size="10" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">BACK — AUTHENTICITY &amp; SIZING</text>
  </g>
</svg>'''
    with open("assets/packaging/03_clothing_hang_tags_duplex.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# ASSET 4: CLOTHING NECK LABELS (Circular Stitched Seal)
# -------------------------------------------------------------
def generate_updated_neck_labels():
    defs = get_defs_with_blush()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 800" width="1100" height="800">
  {defs}
  <rect width="1100" height="800" fill="#F8F7F3" />

  <text x="70" y="60" font-family="'Cinzel', serif" font-size="14" fill="#252525" letter-spacing="0.25em" font-weight="700">ASSET 04 // CLOTHING NECK LABELS (WOVEN FABRIC)</text>
  <text x="70" y="85" font-family="'Montserrat', sans-serif" font-size="9" fill="#7A7265" letter-spacing="0.15em">SPECIFICATION: HIGH-DEFINITION DAMASK JACQUARD • WOVEN CIRCULAR STITCHED SEAL • ZERO-CHAFE EDGES</text>

  <!-- LABEL 1: PRIMARY CHARCOAL DAMASK MAIN LABEL -->
  <g transform="translate(100, 140)">
    <rect x="-30" y="-20" width="540" height="280" rx="8" fill="#EDE8DF" stroke="#DDD6C8" stroke-width="1" />
    <text x="-15" y="0" font-family="'Montserrat', sans-serif" font-size="8" fill="#A8A090" letter-spacing="0.2em">GARMENT INNER COLLAR YOKE</text>

    <rect x="40" y="30" width="400" height="180" rx="3" fill="#252525" filter="url(#softShadow)" />

    <line x1="49" y1="35" x2="49" y2="205" stroke="#EDE8DF" stroke-width="1.2" stroke-dasharray="3 3" opacity="0.8" />
    <line x1="431" y1="35" x2="431" y2="205" stroke="#EDE8DF" stroke-width="1.2" stroke-dasharray="3 3" opacity="0.8" />

    <!-- Woven Circular Stitched Medallion Seal -->
    {get_circular_seal_svg(cx=240, cy=105, r=185, scale=0.38, color="url(#champagneFoil)", text_color="url(#champagneFoil)")}

    <line x1="180" y1="172" x2="300" y2="172" stroke="url(#champagneFoilHoriz)" stroke-width="0.8" />
    <text x="240" y="190" font-family="'Montserrat', sans-serif" font-size="7" fill="#C5B293" letter-spacing="0.4em" text-anchor="middle">MADE IN ITALY</text>

    <text x="240" y="245" font-family="'Montserrat', sans-serif" font-size="10" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">SPEC A — PRIMARY CHARCOAL DAMASK MAIN LABEL (65mm × 35mm)</text>
  </g>

  <!-- LABEL 2: MINIMALIST IVORY WOVEN MAIN LABEL -->
  <g transform="translate(620, 140)">
    <rect x="-30" y="-20" width="460" height="280" rx="8" fill="#E6E0D5" stroke="#DDD6C8" stroke-width="1" />
    <text x="-15" y="0" font-family="'Montserrat', sans-serif" font-size="8" fill="#A8A090" letter-spacing="0.2em">SILK SHIRT / LIGHTWEAR COLLAR</text>

    <rect x="30" y="30" width="340" height="180" rx="3" fill="#F8F7F3" filter="url(#softShadow)" />
    <line x1="42" y1="35" x2="42" y2="205" stroke="#C5BDAE" stroke-width="1.2" stroke-dasharray="3 3" />
    <line x1="358" y1="35" x2="358" y2="205" stroke="#C5BDAE" stroke-width="1.2" stroke-dasharray="3 3" />

    {get_circular_seal_svg(cx=200, cy=105, r=185, scale=0.38, color="#252525", text_color="#252525")}

    <line x1="150" y1="172" x2="250" y2="172" stroke="#B49A70" stroke-width="0.8" />
    <text x="200" y="190" font-family="'Montserrat', sans-serif" font-size="6.5" fill="#B49A70" letter-spacing="0.4em" text-anchor="middle" font-weight="600">EST. 2026</text>

    <text x="200" y="245" font-family="'Montserrat', sans-serif" font-size="10" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">SPEC B — IVORY / CHARCOAL SILK LINING LABEL (55mm × 35mm)</text>
  </g>

  <!-- SIZE TAB & CARE LABELS -->
  <g transform="translate(100, 470)">
    <g transform="translate(80, 20)">
      <rect x="0" y="0" width="70" height="110" rx="2" fill="#252525" filter="url(#softShadow)" />
      <line x1="0" y1="12" x2="70" y2="12" stroke="#FFFFFF" stroke-width="1" stroke-dasharray="2 2" opacity="0.6" />
      <text x="35" y="60" font-family="'Montserrat', sans-serif" font-size="20" fill="url(#champagneFoil)" text-anchor="middle" font-weight="700">M</text>
      <text x="35" y="90" font-family="'Montserrat', sans-serif" font-size="6" fill="#888888" letter-spacing="0.2em" text-anchor="middle">EUR 48</text>
      <text x="35" y="145" font-family="'Montserrat', sans-serif" font-size="8" fill="#736A5B" letter-spacing="0.1em" text-anchor="middle" font-weight="600">SIZE TAB</text>
    </g>

    <g transform="translate(260, 20)">
      <rect x="0" y="0" width="130" height="210" rx="3" fill="#FFFFFF" stroke="#DDD6C8" stroke-width="0.8" filter="url(#softShadow)" />
      <line x1="0" y1="14" x2="130" y2="14" stroke="#BBB2A2" stroke-width="1.2" stroke-dasharray="2 2" />
      <text x="65" y="38" font-family="'Cinzel', serif" font-size="8" fill="#252525" letter-spacing="0.2em" text-anchor="middle" font-weight="600">MEEN MANIFESTATION</text>
      <line x1="20" y1="46" x2="110" y2="46" stroke="#252525" stroke-width="0.5" />
      <text x="15" y="68" font-family="'Montserrat', sans-serif" font-size="6.5" fill="#252525" font-weight="600">SHELL: 100% CASHMERE</text>
      <text x="15" y="80" font-family="'Montserrat', sans-serif" font-size="6" fill="#555555">LINING: 100% SILK</text>
      <text x="15" y="130" font-family="'Montserrat', sans-serif" font-size="5.5" fill="#555555">DRY CLEAN ONLY</text>
      <text x="65" y="185" font-family="'Montserrat', sans-serif" font-size="6" fill="#B49A70" letter-spacing="0.15em" text-anchor="middle" font-weight="600">RN 98214</text>
      <text x="65" y="245" font-family="'Montserrat', sans-serif" font-size="8" fill="#736A5B" letter-spacing="0.1em" text-anchor="middle" font-weight="600">CARE LABEL</text>
    </g>

    <g transform="translate(540, 40)">
      <rect x="0" y="0" width="120" height="60" rx="2" fill="#252525" filter="url(#softShadow)" />
      {get_circular_seal_svg(cx=60, cy=30, r=185, scale=0.12, color="url(#champagneFoil)", text_color="url(#champagneFoil)")}
      <text x="60" y="95" font-family="'Montserrat', sans-serif" font-size="8" fill="#736A5B" letter-spacing="0.1em" text-anchor="middle" font-weight="600">SLEEVE PIP TAB</text>
    </g>
  </g>
</svg>'''
    with open("assets/packaging/04_clothing_neck_labels_woven.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# ASSET 5: THANK-YOU CARD (Circular Stitched Seal)
# -------------------------------------------------------------
def generate_updated_thank_you_card():
    defs = get_defs_with_blush()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1150 850" width="1150" height="850">
  {defs}
  <rect width="1150" height="850" fill="#F8F7F3" />

  <text x="70" y="60" font-family="'Cinzel', serif" font-size="14" fill="#252525" letter-spacing="0.25em" font-weight="700">ASSET 05 // LUXURY THANK-YOU CARD &amp; ENVELOPE</text>
  <text x="70" y="85" font-family="'Montserrat', sans-serif" font-size="9" fill="#7A7265" letter-spacing="0.15em">SPECIFICATION: 450GSM GMUND HEAVY COTTON • CIRCULAR STITCHED FOIL SEAL • MATCHING ENVELOPE WITH WAX SEAL</text>

  <!-- FRONT OF CARD -->
  <g transform="translate(80, 140)">
    <rect x="15" y="15" width="450" height="300" rx="4" fill="#14120E" opacity="0.10" filter="url(#softShadow)" />
    <rect x="0" y="0" width="450" height="300" rx="4" fill="#F8F7F3" stroke="#E6E0D2" stroke-width="1.2" />

    <rect x="20" y="20" width="410" height="260" rx="2" fill="none" stroke="url(#champagneFoil)" stroke-width="0.8" opacity="0.4" />

    <!-- Centered Circular Stitched Medallion Seal -->
    {get_circular_seal_svg(cx=225, cy=135, r=185, scale=0.52, color="url(#champagneFoil)", text_color="#252525")}

    <line x1="165" y1="230" x2="285" y2="230" stroke="url(#champagneFoilHoriz)" stroke-width="1" />
    <text x="225" y="250" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#B49A70" letter-spacing="0.45em" text-anchor="middle">A STATEMENT OF IDENTITY</text>

    <text x="225" y="340" font-family="'Montserrat', sans-serif" font-size="10" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">CARD FRONT</text>
  </g>

  <!-- BACK OF CARD -->
  <g transform="translate(600, 140)">
    <rect x="15" y="15" width="450" height="300" rx="4" fill="#14120E" opacity="0.10" filter="url(#softShadow)" />
    <rect x="0" y="0" width="450" height="300" rx="4" fill="#F8F7F3" stroke="#E6E0D2" stroke-width="1.2" />

    <rect x="20" y="20" width="410" height="260" rx="2" fill="none" stroke="url(#champagneFoil)" stroke-width="0.8" opacity="0.3" />

    <!-- Micro Circular Seal -->
    {get_circular_seal_svg(cx=225, cy=48, r=185, scale=0.18, color="url(#champagneFoil)", text_color="url(#champagneFoil)")}

    <text x="225" y="115" font-family="'Cinzel', 'Playfair Display', 'Georgia', serif" font-size="13" fill="#252525" letter-spacing="0.12em" text-anchor="middle" font-style="italic">
      "Thank you for being part of our manifestation."
    </text>

    <line x1="180" y1="145" x2="270" y2="145" stroke="url(#champagneFoilHoriz)" stroke-width="0.8" />

    <text x="225" y="180" font-family="'Montserrat', sans-serif" font-size="10.5" fill="#252525" letter-spacing="0.28em" text-anchor="middle" font-weight="500">
      WEAR YOUR IDENTITY.
    </text>
    <text x="225" y="204" font-family="'Montserrat', sans-serif" font-size="10.5" fill="#B49A70" letter-spacing="0.28em" text-anchor="middle" font-weight="600">
      MANIFEST YOUR STYLE.
    </text>

    <text x="225" y="255" font-family="'Cinzel', serif" font-size="8" fill="#999182" letter-spacing="0.35em" text-anchor="middle">MEEN MANIFESTATION • HAUTE COUTURE</text>

    <text x="225" y="340" font-family="'Montserrat', sans-serif" font-size="10" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">CARD BACK (MANIFESTO)</text>
  </g>

  <!-- COMPANION ENVELOPE -->
  <g transform="translate(340, 500)">
    <rect x="15" y="15" width="470" height="250" rx="4" fill="#14120E" opacity="0.12" filter="url(#softShadow)" />
    <rect x="0" y="0" width="470" height="250" rx="4" fill="#EDE8DF" stroke="#D8D1C2" stroke-width="1.2" />

    <polygon points="0,0 235,140 470,0" fill="#F8F7F3" stroke="#D8D1C2" stroke-width="0.8" />
    <polygon points="20,0 235,128 450,0" fill="#F2ECE0" />
    
    <!-- Circular Stitched Gold Wax Seal -->
    <g transform="translate(235, 140)">
      <circle cx="0" cy="0" r="28" fill="url(#goldSheen)" filter="url(#softShadow)" />
      {get_circular_seal_svg(cx=0, cy=0, r=185, scale=0.14, color="#FFFFFF", text_color="#FFFFFF")}
    </g>

    <text x="235" y="295" font-family="'Montserrat', sans-serif" font-size="10" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">COMPANION ENVELOPE WITH EMBOSSED STITCHED WAX SEAL</text>
  </g>
</svg>'''
    with open("assets/packaging/05_thank_you_card_front_back.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# ASSET 6: ARCHIVAL TISSUE PAPER (Circular Stitched Seal Pattern)
# -------------------------------------------------------------
def generate_updated_tissue_paper():
    defs = get_defs_with_blush()
    
    pattern_items = []
    for row in range(4):
        for col in range(5):
            cx = col * 200 + (100 if row % 2 == 1 else 0) + 50
            cy = row * 170 + 80
            pattern_items.append(get_circular_seal_svg(cx=cx, cy=cy, r=185, scale=0.32, color="#B49A70", text_color="#B49A70"))

    pattern_svg_content = "\n".join(pattern_items)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 850" width="1100" height="850">
  {defs}
  <rect width="1100" height="850" fill="#F8F7F3" />

  <text x="70" y="60" font-family="'Cinzel', serif" font-size="14" fill="#252525" letter-spacing="0.25em" font-weight="700">ASSET 06 // LUXURY TISSUE PAPER &amp; PACKAGING SEAL</text>
  <text x="70" y="85" font-family="'Montserrat', sans-serif" font-size="9" fill="#7A7265" letter-spacing="0.15em">SPECIFICATION: 24GSM ARCHIVAL ACID-FREE TISSUE • REPEATING CIRCULAR STITCHED SEAL • 35MM EMBOSSED FOIL SEAL</text>

  <g transform="translate(100, 130)">
    <rect x="20" y="20" width="900" height="600" rx="4" fill="#14120E" opacity="0.10" filter="url(#softShadow)" />
    <rect x="0" y="0" width="900" height="600" rx="4" fill="#FFFFFF" stroke="#E8E4DA" stroke-width="1.2" />

    <!-- Repeating Watermark Pattern at 22% Opacity -->
    <g opacity="0.24">
      {pattern_svg_content}
    </g>

    <rect x="0" y="0" width="900" height="600" fill="url(#fishBlushGrad)" opacity="0.04" />

    <!-- Overlapping Fold Detail -->
    <polygon points="580,240 880,240 880,540 580,540" fill="#FAF9F6" stroke="#E5DEC8" stroke-width="1" opacity="0.85" filter="url(#softShadow)" />
    <g transform="translate(580, 240)" opacity="0.25">
      {get_circular_seal_svg(cx=150, cy=150, r=185, scale=0.55, color="#B49A70", text_color="#B49A70")}
    </g>

    <!-- 35mm Champagne Foil Circular Seal Sticker -->
    <g transform="translate(580, 390)">
      <circle cx="0" cy="0" r="44" fill="url(#goldSheen)" filter="url(#softShadow)" />
      {get_circular_seal_svg(cx=0, cy=0, r=185, scale=0.22, color="#FFFFFF", text_color="#FFFFFF")}
    </g>
  </g>
</svg>'''
    with open("assets/packaging/06_tissue_paper_pattern.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# ASSET 7: SHIPPING BOX (Circular Stitched Seal)
# -------------------------------------------------------------
def generate_updated_shipping_box():
    defs = get_defs_with_blush()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" width="1200" height="900">
  {defs}
  <rect width="1200" height="900" fill="#F8F7F3" />

  <text x="70" y="60" font-family="'Cinzel', serif" font-size="14" fill="#252525" letter-spacing="0.25em" font-weight="700">ASSET 07 // DURABLE LUXURY SHIPPING BOX &amp; BRANDED TAPE</text>
  <text x="70" y="85" font-family="'Montserrat', sans-serif" font-size="9" fill="#7A7265" letter-spacing="0.15em">SPECIFICATION: REINFORCED RIGID FLUTE E-COMMERCE SHIPPER • NATURAL BEIGE KRAFT • CIRCULAR STITCHED SEAL BRANDING</text>

  <!-- LEFT: CLOSED SHIPPER -->
  <g transform="translate(60, 130)">
    <rect x="20" y="20" width="480" height="420" rx="4" fill="#14120E" opacity="0.12" filter="url(#softShadow)" />
    <rect x="0" y="0" width="480" height="420" rx="4" fill="#EDE8DF" stroke="#CBC2B0" stroke-width="1.5" />

    <line x1="240" y1="0" x2="240" y2="420" stroke="#BBB09D" stroke-width="1.5" />

    <!-- Custom Water-Activated Sealing Tape (Banner Lockup) -->
    <rect x="205" y="0" width="70" height="420" fill="#F8F7F3" stroke="#D3C9B8" stroke-width="0.8" filter="url(#softShadow)" />
    <g transform="translate(240, 210) rotate(90)">
      <text x="0" y="-8" font-family="'Cinzel', serif" font-size="11" fill="#252525" letter-spacing="0.28em" text-anchor="middle" font-weight="600">MEEN MANIFESTATION</text>
      <text x="0" y="8" font-family="'Montserrat', sans-serif" font-size="6.5" fill="#B49A70" letter-spacing="0.32em" text-anchor="middle" font-weight="600">A STATEMENT OF IDENTITY</text>
    </g>

    <!-- Circular Stitched Seal in Charcoal on Box Flap Corner -->
    {get_circular_seal_svg(cx=80, cy=70, r=185, scale=0.32, color="#252525", text_color="#252525")}

    <!-- Shipping Courier Label -->
    <rect x="38" y="270" width="140" height="110" rx="3" fill="#FFFFFF" stroke="#D8D0C0" stroke-width="1" />
    <text x="48" y="300" font-family="'Montserrat', sans-serif" font-size="7" fill="#252525" font-weight="700">EXPRESS LUXURY COURIER</text>
    <text x="48" y="320" font-family="'Montserrat', sans-serif" font-size="6" fill="#888888">DESIGNED BY HARSHIT PARGAIN</text>
    <text x="48" y="355" font-family="'Montserrat', sans-serif" font-size="6.5" fill="#B49A70" font-weight="600">TRK 8492-MM-VIP</text>

    <text x="240" y="470" font-family="'Montserrat', sans-serif" font-size="11" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">FIG 7.1 — CLOSED SHIPPER WITH CIRCULAR SEAL BRANDING</text>
  </g>

  <!-- RIGHT: OPEN SHIPPER WITH UNBOXING REVEAL -->
  <g transform="translate(620, 130)">
    <rect x="20" y="20" width="500" height="420" rx="4" fill="#14120E" opacity="0.14" filter="url(#softShadow)" />
    <rect x="0" y="0" width="500" height="420" rx="4" fill="#D8CFBD" stroke="#B8AE9A" stroke-width="1.5" />

    <polygon points="0,0 500,0 470,-110 30,-110" fill="#F8F7F3" stroke="#DDD6C8" stroke-width="1" />
    <g transform="translate(0, -60)">
      {get_circular_seal_svg(cx=250, cy=-20, r=185, scale=0.22, color="url(#champagneFoil)", text_color="url(#champagneFoil)")}
      <text x="250" y="25" font-family="'Cinzel', serif" font-size="12" fill="#252525" letter-spacing="0.32em" text-anchor="middle" font-weight="600">WELCOME TO YOUR MANIFESTATION</text>
      <text x="250" y="42" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#B49A70" letter-spacing="0.35em" text-anchor="middle">WEAR YOUR IDENTITY. MANIFEST YOUR STYLE.</text>
    </g>

    <rect x="25" y="20" width="450" height="380" rx="3" fill="#EDE8DF" />
    <rect x="50" y="45" width="400" height="330" rx="4" fill="#F8F7F3" stroke="#DDD6CA" stroke-width="1.2" filter="url(#softShadow)" />
    {get_circular_seal_svg(cx=250, cy=180, r=185, scale=0.48, color="url(#champagneFoil)", text_color="#252525")}
    <text x="250" y="305" font-family="'Montserrat', sans-serif" font-size="6.5" fill="#B49A70" letter-spacing="0.4em" text-anchor="middle">A STATEMENT OF IDENTITY</text>

    <text x="250" y="470" font-family="'Montserrat', sans-serif" font-size="11" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">FIG 7.2 — UNBOXING REVEAL WITH CIRCULAR SEAL</text>
  </g>
</svg>'''
    with open("assets/packaging/07_shipping_box_closed_and_open.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# -------------------------------------------------------------
# ASSET 8: SOCIAL MEDIA BRANDING SUITE (Circular Stitched Seal)
# -------------------------------------------------------------
def generate_updated_social_media():
    defs = get_defs_with_blush()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 950" width="1200" height="950">
  {defs}
  <rect width="1200" height="950" fill="#F8F7F3" />

  <text x="70" y="55" font-family="'Cinzel', serif" font-size="14" fill="#252525" letter-spacing="0.25em" font-weight="700">ASSET 08 // SOCIAL MEDIA BRANDING SUITE</text>
  <text x="70" y="80" font-family="'Montserrat', sans-serif" font-size="9" fill="#7A7265" letter-spacing="0.15em">INSTAGRAM PROFILE ARCHITECTURE • CIRCULAR STITCHED SEAL AVATAR • LAUNCH TEMPLATES • STORY ANNOUNCEMENTS</text>

  <!-- 8.1 INSTAGRAM PROFILE FRAME -->
  <g transform="translate(60, 110)">
    <rect x="0" y="0" width="340" height="600" rx="28" fill="#FFFFFF" stroke="#E3DC CE" stroke-width="1.5" filter="url(#softShadow)" />
    
    <text x="170" y="42" font-family="'Montserrat', sans-serif" font-size="11" fill="#252525" font-weight="700" letter-spacing="0.05em" text-anchor="middle">meenmanifestation</text>
    <circle cx="245" cy="38" r="5" fill="#B49A70" />
    <path d="M 243 38 L 244.5 40 L 247 36" fill="none" stroke="#FFFFFF" stroke-width="1" />

    <!-- Avatar with Circular Stitched Medallion Seal -->
    <circle cx="60" cy="95" r="32" fill="url(#champagneFoil)" />
    <circle cx="60" cy="95" r="30" fill="#FAF8F5" />
    {get_circular_seal_svg(cx=60, cy=95, r=185, scale=0.15, color="#B49A70", text_color="#252525")}

    <g transform="translate(130, 90)">
      <text x="20" y="0" font-family="'Montserrat', sans-serif" font-size="12" fill="#252525" font-weight="700" text-anchor="middle">18</text>
      <text x="20" y="14" font-family="'Montserrat', sans-serif" font-size="8" fill="#888888" text-anchor="middle">posts</text>
      <text x="80" y="0" font-family="'Montserrat', sans-serif" font-size="12" fill="#252525" font-weight="700" text-anchor="middle">142K</text>
      <text x="80" y="14" font-family="'Montserrat', sans-serif" font-size="8" fill="#888888" text-anchor="middle">followers</text>
      <text x="145" y="0" font-family="'Montserrat', sans-serif" font-size="12" fill="#252525" font-weight="700" text-anchor="middle">6</text>
      <text x="145" y="14" font-family="'Montserrat', sans-serif" font-size="8" fill="#888888" text-anchor="middle">following</text>
    </g>

    <g transform="translate(25, 148)">
      <text x="0" y="0" font-family="'Cinzel', serif" font-size="10.5" fill="#252525" font-weight="700" letter-spacing="0.1em">MEEN MANIFESTATION</text>
      <text x="0" y="14" font-family="'Montserrat', sans-serif" font-size="8" fill="#B49A70" font-weight="600">Haute Couture &amp; Luxury Fashion House</text>
      <text x="0" y="28" font-family="'Montserrat', sans-serif" font-size="8" fill="#444444" font-style="italic">Not Just Fashion. A Statement of Identity.</text>
      <text x="0" y="42" font-family="'Montserrat', sans-serif" font-size="8" fill="#666666">Designed by Harshit Pargain</text>
      <text x="0" y="56" font-family="'Montserrat', sans-serif" font-size="8" fill="#B49A70" font-weight="600">meenmanifestation.com</text>
    </g>

    <g transform="translate(25, 222)">
      <rect x="0" y="0" width="138" height="26" rx="4" fill="#252525" />
      <text x="69" y="17" font-family="'Montserrat', sans-serif" font-size="9" fill="#FFFFFF" font-weight="600" text-anchor="middle">Follow</text>
      <rect x="148" y="0" width="138" height="26" rx="4" fill="#EDE8DF" />
      <text x="217" y="17" font-family="'Montserrat', sans-serif" font-size="9" fill="#252525" font-weight="600" text-anchor="middle">Message</text>
    </g>

    <!-- Story Highlights -->
    <g transform="translate(25, 265)">
      <circle cx="22" cy="20" r="19" fill="none" stroke="url(#champagneFoil)" stroke-width="1.2" />
      <circle cx="22" cy="20" r="16" fill="#F8F7F3" />
      <text x="22" y="23" font-family="'Cinzel', serif" font-size="7" fill="#252525" text-anchor="middle" font-weight="700">01</text>
      <text x="22" y="47" font-family="'Montserrat', sans-serif" font-size="7" fill="#666666" text-anchor="middle">Collection</text>

      <circle cx="82" cy="20" r="19" fill="none" stroke="url(#champagneFoil)" stroke-width="1.2" />
      <circle cx="82" cy="20" r="16" fill="#F8F7F3" />
      {get_circular_seal_svg(cx=82, cy=20, r=185, scale=0.08, color="#B49A70", text_color="none")}
      <text x="82" y="47" font-family="'Montserrat', sans-serif" font-size="7" fill="#666666" text-anchor="middle">Manifesto</text>

      <circle cx="142" cy="20" r="19" fill="none" stroke="url(#champagneFoil)" stroke-width="1.2" />
      <circle cx="142" cy="20" r="16" fill="#F8F7F3" />
      <text x="142" y="23" font-family="'Cinzel', serif" font-size="6.5" fill="#252525" text-anchor="middle">CRAFT</text>
      <text x="142" y="47" font-family="'Montserrat', sans-serif" font-size="7" fill="#666666" text-anchor="middle">Atelier</text>

      <circle cx="202" cy="20" r="19" fill="none" stroke="url(#champagneFoil)" stroke-width="1.2" />
      <circle cx="202" cy="20" r="16" fill="#F8F7F3" />
      <rect x="196" y="14" width="12" height="12" fill="none" stroke="#252525" stroke-width="0.8" />
      <text x="202" y="47" font-family="'Montserrat', sans-serif" font-size="7" fill="#666666" text-anchor="middle">Packaging</text>

      <circle cx="262" cy="20" r="19" fill="none" stroke="url(#champagneFoil)" stroke-width="1.2" />
      <circle cx="262" cy="20" r="16" fill="#F8F7F3" />
      <text x="262" y="23" font-family="'Cinzel', serif" font-size="6" fill="#252525" text-anchor="middle">PRESS</text>
      <text x="262" y="47" font-family="'Montserrat', sans-serif" font-size="7" fill="#666666" text-anchor="middle">Editorial</text>
    </g>

    <!-- Grid Preview -->
    <g transform="translate(20, 335)">
      <rect x="0" y="0" width="96" height="96" fill="#EDE8DF" />
      {get_circular_seal_svg(cx=48, cy=48, r=185, scale=0.22, color="url(#champagneFoil)", text_color="#252525")}
      <rect x="101" y="0" width="96" height="96" fill="#252525" />
      <text x="149" y="48" font-family="'Cinzel', serif" font-size="7" fill="#F8F7F3" text-anchor="middle">MANIFEST</text>
      <text x="149" y="58" font-family="'Montserrat', sans-serif" font-size="5" fill="#B49A70" text-anchor="middle">YOUR STYLE</text>
      <rect x="202" y="0" width="96" height="96" fill="#F8F7F3" />
      <circle cx="250" cy="48" r="22" fill="url(#champagneFoil)" />
      <rect x="0" y="101" width="96" height="96" fill="#F4EFE7" />
      <text x="48" y="152" font-family="'Cinzel', serif" font-size="8" fill="#252525" text-anchor="middle">N° 01</text>
      <rect x="101" y="101" width="96" height="96" fill="#EDE8DF" />
      <rect x="202" y="101" width="96" height="96" fill="#252525" />
      {get_circular_seal_svg(cx=250, cy=149, r=185, scale=0.22, color="url(#champagneFoil)", text_color="url(#champagneFoil)")}
    </g>

    <text x="170" y="635" font-family="'Montserrat', sans-serif" font-size="10" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">8.1 — INSTAGRAM PROFILE ARCHITECTURE</text>
  </g>

  <!-- 8.2 PRODUCT LAUNCH TEMPLATE -->
  <g transform="translate(440, 110)">
    <rect x="0" y="0" width="340" height="340" fill="#F8F7F3" stroke="#E3DC CE" stroke-width="1.2" filter="url(#softShadow)" />
    <rect x="18" y="18" width="304" height="304" fill="none" stroke="url(#champagneFoil)" stroke-width="0.8" opacity="0.4" />

    {get_circular_seal_svg(cx=170, cy=110, r=185, scale=0.45, color="url(#champagneFoil)", text_color="#252525")}

    <text x="170" y="215" font-family="'Cinzel', serif" font-size="13" fill="#252525" letter-spacing="0.32em" text-anchor="middle" font-weight="600">THE ICONIC CASHMERE COAT</text>
    <line x1="130" y1="230" x2="210" y2="230" stroke="url(#champagneFoilHoriz)" stroke-width="1" />
    <text x="170" y="248" font-family="'Montserrat', sans-serif" font-size="7" fill="#B49A70" letter-spacing="0.38em" text-anchor="middle">COLLECTION 01 // MANIFESTATION</text>

    <text x="170" y="280" font-family="'Cinzel', serif" font-size="8.5" fill="#252525" letter-spacing="0.2em" text-anchor="middle" font-style="italic">"A Statement of Identity."</text>
    <text x="170" y="305" font-family="'Montserrat', sans-serif" font-size="6.5" fill="#A89E8D" letter-spacing="0.3em" text-anchor="middle">MEENMANIFESTATION.COM</text>
    <text x="170" y="375" font-family="'Montserrat', sans-serif" font-size="10" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">8.2 — FEED PRODUCT LAUNCH TEMPLATE (1:1)</text>
  </g>

  <!-- 8.3 STORY TEMPLATE (9:16) -->
  <g transform="translate(820, 110)">
    <rect x="0" y="0" width="320" height="568" rx="16" fill="#252525" filter="url(#softShadow)" />
    <rect x="15" y="15" width="290" height="538" rx="12" fill="none" stroke="url(#champagneFoil)" stroke-width="0.8" opacity="0.35" />

    <text x="160" y="80" font-family="'Cinzel', serif" font-size="11" fill="url(#champagneFoil)" letter-spacing="0.35em" text-anchor="middle" font-weight="600">MEEN MANIFESTATION</text>
    <text x="160" y="98" font-family="'Montserrat', sans-serif" font-size="6.5" fill="#AAAAAA" letter-spacing="0.4em" text-anchor="middle">HAUTE COUTURE</text>

    {get_circular_seal_svg(cx=160, cy=200, r=185, scale=0.55, color="url(#champagneFoil)", text_color="url(#champagneFoil)")}

    <text x="160" y="325" font-family="'Cinzel', serif" font-size="18" fill="#F8F7F3" letter-spacing="0.25em" text-anchor="middle" font-weight="500">COLLECTION 01</text>
    <line x1="110" y1="345" x2="210" y2="345" stroke="url(#champagneFoilHoriz)" stroke-width="1" />
    <text x="160" y="370" font-family="'Cinzel', serif" font-size="14" fill="url(#champagneFoil)" letter-spacing="0.3em" text-anchor="middle" font-style="italic">The Reveal</text>
    <text x="160" y="410" font-family="'Montserrat', sans-serif" font-size="8" fill="#EDE8DF" letter-spacing="0.35em" text-anchor="middle">AUTUMN / WINTER 2026</text>

    <g transform="translate(95, 480)">
      <rect x="0" y="0" width="130" height="34" rx="17" fill="url(#champagneFoil)" />
      <text x="65" y="21" font-family="'Montserrat', sans-serif" font-size="8" fill="#252525" letter-spacing="0.2em" text-anchor="middle" font-weight="700">EXPLORE TEASER</text>
    </g>

    <text x="160" y="615" font-family="'Montserrat', sans-serif" font-size="10" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">8.3 — STORY CAMPAIGN TEMPLATE (9:16)</text>
  </g>
</svg>'''
    with open("assets/social/08_social_media_branding_suite.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def update_all_packaging():
    print("Replacing MM monogram with the Official Circular Stitched Medallion Seal across all 8 assets...")
    generate_updated_shopping_bag()
    generate_updated_clothing_box()
    generate_updated_hang_tags()
    generate_updated_neck_labels()
    generate_updated_thank_you_card()
    generate_updated_tissue_paper()
    generate_updated_shipping_box()
    generate_updated_social_media()
    print("All 8 packaging assets successfully updated with the circular stitched medallion seal!")

if __name__ == "__main__":
    update_all_packaging()
