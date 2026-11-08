"""
MEEN MANIFESTATION - Haute Couture Extensions & Accessory Suite Generator
Generates vectors for:
- Asset 09: Tailored Garment Carrier / Dust Cover Bag
- Asset 10: Luxury Gifting Ribbon & Boutique Invoice Folio
- Asset 11: Bespoke Garment Hardware (Horn Buttons, Brass Zippers, NFC Passport)
"""

import os
from generate_packaging_suite import get_foil_defs, get_mm_monogram

def generate_garment_bag():
    defs = get_foil_defs()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1300" width="1000" height="1300">
  {defs}
  <rect width="1000" height="1300" fill="#F8F7F3" />

  <!-- Presentation Header -->
  <text x="70" y="60" font-family="'Cinzel', serif" font-size="14" fill="#252525" letter-spacing="0.25em" font-weight="700">EXTENDED ATELIER // LUXURY SUIT &amp; OVERCOAT GARMENT CARRIER</text>
  <text x="70" y="85" font-family="'Montserrat', sans-serif" font-size="9" fill="#7A7265" letter-spacing="0.15em">SPECIFICATION: 100% ORGANIC HEAVYWEIGHT IVORY COTTON DUCK • POLISHED BRASS HARDWARE • LEATHER TRIM HANDLES</text>

  <!-- Garment Carrier Hanging on Coat Hanger -->
  <g transform="translate(200, 130)">
    <!-- Shadow -->
    <rect x="25" y="40" width="550" height="1020" rx="20" fill="#14120E" opacity="0.12" filter="url(#softShadow)" />

    <!-- Wooden Luxury Hanger Peak Top -->
    <path d="M 180 30 C 230 -20, 370 -20, 420 30 L 520 80 L 80 80 Z" fill="#D3C9B8" stroke="#B8AD99" stroke-width="1.2" />
    <circle cx="300" cy="-30" r="22" fill="none" stroke="url(#champagneFoil)" stroke-width="4" />
    <line x1="300" y1="-8" x2="300" y2="10" stroke="url(#champagneFoil)" stroke-width="4" />

    <!-- Garment Bag Main Body (Ivory #F8F7F3 Canvas) -->
    <rect x="0" y="70" width="600" height="980" rx="14" fill="#FBF9F5" stroke="#E3DC CE" stroke-width="1.5" />
    <rect x="0" y="70" width="600" height="980" rx="14" fill="url(#fineGrain)" />

    <!-- Fine Tailoring Perimeter Seam Stitching (Double Stitch) -->
    <rect x="14" y="84" width="572" height="952" rx="10" fill="none" stroke="#D3C9B8" stroke-width="1.2" stroke-dasharray="4 4" />
    <rect x="20" y="90" width="560" height="940" rx="8" fill="none" stroke="#D3C9B8" stroke-width="0.8" stroke-dasharray="4 4" opacity="0.6" />

    <!-- Center Champagne Brass Zipper Column -->
    <rect x="296" y="90" width="8" height="920" fill="#EDE7DC" />
    <!-- Zipper Teeth Simulation -->
    <line x1="297" y1="90" x2="297" y2="1010" stroke="#8E7348" stroke-width="1.5" stroke-dasharray="2 2" />
    <line x1="303" y1="90" x2="303" y2="1010" stroke="#8E7348" stroke-width="1.5" stroke-dasharray="2 2" />

    <!-- Champagne Brass Zipper Pull Tab with MM Monogram -->
    <g transform="translate(292, 340)">
      <rect x="0" y="0" width="16" height="24" rx="3" fill="url(#champagneFoil)" filter="url(#cardShadow)" />
      <rect x="3" y="18" width="10" height="32" rx="2" fill="url(#champagneFoil)" />
      {get_mm_monogram(x=-1, y=20, scale=0.1, color="#252525", show_accents=False)}
    </g>

    <!-- Translucent Identity Card Pocket on Left Breast -->
    <rect x="60" y="140" width="140" height="90" rx="3" fill="#FFFFFF" opacity="0.8" stroke="#D3C9B8" stroke-width="1" />
    <text x="75" y="165" font-family="'Cinzel', serif" font-size="8" fill="#252525" font-weight="700">CLIENT ARCHIVE</text>
    <text x="75" y="180" font-family="'Montserrat', sans-serif" font-size="6.5" fill="#B49A70">ID: MM-2026-VIP</text>
    <text x="75" y="195" font-family="'Montserrat', sans-serif" font-size="6" fill="#888888">PERPETUAL OVERCOAT</text>

    <!-- Centered Brand Embroidery / Foil Print -->
    <g transform="translate(0, 480)">
      <circle cx="300" cy="50" r="85" fill="none" stroke="url(#champagneFoilSoft)" stroke-width="1" opacity="0.4" />
      <circle cx="300" cy="50" r="92" fill="none" stroke="url(#champagneFoilSoft)" stroke-width="0.5" stroke-dasharray="3 3" opacity="0.5" />
      
      <!-- MM Monogram -->
      {get_mm_monogram(x=222, y=5, scale=0.85, color="url(#champagneFoil)")}

      <!-- Brand Typography -->
      <text x="300" y="125" font-family="'Cinzel', serif" font-size="18" fill="#252525" letter-spacing="0.36em" text-anchor="middle" font-weight="600">MEEN MANIFESTATION</text>
      <line x1="240" y1="145" x2="360" y2="145" stroke="url(#champagneFoilHoriz)" stroke-width="1" />
      <text x="300" y="168" font-family="'Montserrat', sans-serif" font-size="8" fill="#B49A70" letter-spacing="0.4em" text-anchor="middle" font-weight="500">NOT JUST FASHION. A STATEMENT OF IDENTITY.</text>
      <text x="300" y="195" font-family="'Montserrat', sans-serif" font-size="6.5" fill="#A89E8D" letter-spacing="0.35em" text-anchor="middle">ATELIER PARIS • MILANO</text>
    </g>

    <!-- Bottom Leather Carry Handles & Fold-Over Brass Eyelets -->
    <g transform="translate(0, 960)">
      <!-- Reinforced Leather Trim Bar -->
      <rect x="180" y="20" width="240" height="20" rx="4" fill="#C5B59D" stroke="#A89880" stroke-width="1" />
      <circle cx="210" cy="30" r="6" fill="url(#champagneFoil)" />
      <circle cx="390" cy="30" r="6" fill="url(#champagneFoil)" />
      <!-- Arch Leather Handle -->
      <path d="M 240 20 C 240 -30, 360 -30, 360 20" fill="none" stroke="#A89880" stroke-width="14" stroke-linecap="round" />
      <path d="M 240 20 C 240 -30, 360 -30, 360 20" fill="none" stroke="#C5B59D" stroke-width="10" stroke-linecap="round" />
      <text x="300" y="65" font-family="'Montserrat', sans-serif" font-size="7" fill="#888172" letter-spacing="0.2em" text-anchor="middle">FOLD-AND-CARRY TRAVEL SYSTEM</text>
    </g>
  </g>
</svg>'''
    with open("assets/packaging/09_luxury_garment_bag_cover.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_ribbon_and_folio():
    defs = get_foil_defs()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 850" width="1200" height="850">
  {defs}
  <rect width="1200" height="850" fill="#F8F7F3" />

  <text x="70" y="60" font-family="'Cinzel', serif" font-size="14" fill="#252525" letter-spacing="0.25em" font-weight="700">EXTENDED ATELIER // LUXURY GIFT RIBBON &amp; INVOICE FOLIO</text>
  <text x="70" y="85" font-family="'Montserrat', sans-serif" font-size="9" fill="#7A7265" letter-spacing="0.15em">SPECIFICATION: 25MM DOUBLE-FACED SILK SATIN RIBBON • 350GSM BOUTIQUE INVOICE WALLET</text>

  <!-- LEFT: 25MM LUXURY SATIN RIBBON ROLL & FLUID DRAPING -->
  <g transform="translate(80, 140)">
    <!-- Wooden / Acrylic Spool Core -->
    <ellipse cx="140" cy="180" rx="90" ry="24" fill="#14120E" opacity="0.12" filter="url(#softShadow)" />
    <!-- Spool Body -->
    <rect x="70" y="60" width="140" height="120" rx="6" fill="url(#champagneFoil)" filter="url(#cardShadow)" />
    <!-- Ribbon Layers on Spool -->
    <line x1="70" y1="80" x2="210" y2="80" stroke="#FFFFFF" stroke-width="0.8" opacity="0.6" />
    <line x1="70" y1="100" x2="210" y2="100" stroke="#FFFFFF" stroke-width="0.8" opacity="0.6" />
    <line x1="70" y1="120" x2="210" y2="120" stroke="#FFFFFF" stroke-width="0.8" opacity="0.6" />
    <line x1="70" y1="140" x2="210" y2="140" stroke="#FFFFFF" stroke-width="0.8" opacity="0.6" />
    <line x1="70" y1="160" x2="210" y2="160" stroke="#FFFFFF" stroke-width="0.8" opacity="0.6" />

    <!-- Spool Flange Rim -->
    <ellipse cx="140" cy="60" rx="75" ry="18" fill="#F8F7F3" stroke="#D3C9B8" stroke-width="1.5" />
    <circle cx="140" cy="60" r="14" fill="url(#champagneFoil)" />

    <!-- Fluid Draping Ribbon Strip -->
    <path d="M 190 120 C 260 120, 280 280, 360 280 C 440 280, 420 420, 500 420" fill="none" stroke="url(#champagneFoil)" stroke-width="38" filter="url(#cardShadow)" />
    <path d="M 190 120 C 260 120, 280 280, 360 280 C 440 280, 420 420, 500 420" fill="none" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="4 6" opacity="0.5" />

    <!-- Text along the Ribbon -->
    <g transform="translate(240, 200) rotate(42)">
      <text x="0" y="0" font-family="'Cinzel', serif" font-size="8" fill="#252525" letter-spacing="0.25em" font-weight="700">MEEN MANIFESTATION</text>
    </g>
    <g transform="translate(370, 340) rotate(35)">
      <text x="0" y="0" font-family="'Cinzel', serif" font-size="8" fill="#252525" letter-spacing="0.25em" font-weight="700">A STATEMENT OF IDENTITY</text>
    </g>

    <text x="140" y="480" font-family="'Montserrat', sans-serif" font-size="10" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">25MM DOUBLE-FACED SATIN GIFT RIBBON</text>
    <text x="140" y="500" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#A89E8D" letter-spacing="0.1em" text-anchor="middle">WOVEN SELVEDGE • GOLD STAMPED TYPOGRAPHY</text>
  </g>

  <!-- RIGHT: BOUTIQUE INVOICE & CERTIFICATE FOLIO -->
  <g transform="translate(640, 140)">
    <!-- Shadow -->
    <rect x="20" y="20" width="460" height="520" rx="8" fill="#14120E" opacity="0.12" filter="url(#softShadow)" />

    <!-- Folio Outer Shell (Beige #EDE8DF 350gsm Card) -->
    <rect x="0" y="0" width="460" height="520" rx="8" fill="url(#beigeBoxGrad)" stroke="#CBC2B0" stroke-width="1.5" />
    <rect x="0" y="0" width="460" height="520" rx="8" fill="url(#fineGrain)" />

    <!-- Delicate Blind Embossed Border -->
    <rect x="22" y="22" width="416" height="476" rx="4" fill="none" stroke="url(#champagneFoilSoft)" stroke-width="0.8" opacity="0.4" />

    <!-- Centered MM Monogram Foil Stamped -->
    {get_mm_monogram(x=175, y=90, scale=0.72, color="url(#champagneFoil)")}

    <text x="230" y="200" font-family="'Cinzel', serif" font-size="17" fill="#252525" letter-spacing="0.34em" text-anchor="middle" font-weight="600">MEEN MANIFESTATION</text>
    <line x1="170" y1="218" x2="290" y2="218" stroke="url(#champagneFoilHoriz)" stroke-width="1" />
    <text x="230" y="238" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#B49A70" letter-spacing="0.4em" text-anchor="middle">ATELIER CLIENT RECORD</text>

    <!-- Inner Slip Pocket Flap -->
    <path d="M 22 360 L 438 360 L 438 498 L 22 498 Z" fill="#F8F7F3" stroke="#D3C9B8" stroke-width="1" />
    <path d="M 22 360 L 230 410 L 438 360" fill="none" stroke="#D3C9B8" stroke-width="1" />
    
    <!-- Protruding Certificate of Authenticity -->
    <rect x="60" y="300" width="340" height="120" rx="2" fill="#FFFFFF" stroke="#E3DC CE" stroke-width="0.8" filter="url(#cardShadow)" />
    <text x="230" y="330" font-family="'Cinzel', serif" font-size="9" fill="#252525" letter-spacing="0.25em" text-anchor="middle" font-weight="700">CERTIFICATE OF SARTORIAL AUTHENTICITY</text>
    <text x="230" y="348" font-family="'Montserrat', sans-serif" font-size="7" fill="#888888" letter-spacing="0.15em" text-anchor="middle">PIECE N°: 014 / 100 • ARCHIVE 2026</text>
    <line x1="140" y1="360" x2="320" y2="360" stroke="#B49A70" stroke-width="0.6" stroke-dasharray="2 2" />

    <text x="230" y="580" font-family="'Montserrat', sans-serif" font-size="10" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">BOUTIQUE RECEIPT &amp; CERTIFICATE WALLET</text>
    <text x="230" y="600" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#A89E8D" letter-spacing="0.1em" text-anchor="middle">350GSM RIGID WALLET WITH PRECISION DIE-CUT POCKET</text>
  </g>
</svg>'''
    with open("assets/packaging/10_luxury_ribbon_and_receipt_folio.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_hardware_and_buttons():
    defs = get_foil_defs()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 850" width="1100" height="850">
  {defs}
  <rect width="1100" height="850" fill="#F8F7F3" />

  <text x="70" y="60" font-family="'Cinzel', serif" font-size="14" fill="#252525" letter-spacing="0.25em" font-weight="700">EXTENDED ATELIER // BESPOKE GARMENT HARDWARE &amp; TRIMS</text>
  <text x="70" y="85" font-family="'Montserrat', sans-serif" font-size="9" fill="#7A7265" letter-spacing="0.15em">SPECIFICATION: NATURAL WATER BUFFALO HORN • MOTHER-OF-PEARL • CHAMPAGNE BRASS PINS &amp; NFC MICROCHIP</text>

  <!-- 1. BESPOKE HORN OVERCOAT BUTTON (30MM) -->
  <g transform="translate(140, 200)">
    <circle cx="90" cy="90" r="85" fill="#14120E" opacity="0.14" filter="url(#softShadow)" />
    <!-- Button Face (Matte Charcoal Buffalo Horn with subtle natural grain) -->
    <circle cx="80" cy="80" r="80" fill="#2B2825" stroke="#1E1C1A" stroke-width="2" />
    <circle cx="80" cy="80" r="68" fill="none" stroke="#3D3833" stroke-width="1.5" />

    <!-- Deep Inscribed Monogram Rim -->
    <text x="80" y="35" font-family="'Cinzel', serif" font-size="9" fill="#B49A70" letter-spacing="0.3em" text-anchor="middle">MEEN</text>
    <text x="80" y="140" font-family="'Cinzel', serif" font-size="9" fill="#B49A70" letter-spacing="0.3em" text-anchor="middle">MANIFESTATION</text>

    <!-- 4 Button Thread Holes with Beveled Recesses -->
    <circle cx="65" cy="70" r="7" fill="#181614" stroke="#443F3A" stroke-width="1" />
    <circle cx="95" cy="70" r="7" fill="#181614" stroke="#443F3A" stroke-width="1" />
    <circle cx="65" cy="95" r="7" fill="#181614" stroke="#443F3A" stroke-width="1" />
    <circle cx="95" cy="95" r="7" fill="#181614" stroke="#443F3A" stroke-width="1" />

    <!-- Thread Stitch (Champagne Lurex Thread) -->
    <line x1="65" y1="70" x2="95" y2="95" stroke="#B49A70" stroke-width="2.5" />
    <line x1="95" y1="70" x2="65" y2="95" stroke="#B49A70" stroke-width="2.5" />

    <text x="80" y="200" font-family="'Montserrat', sans-serif" font-size="10" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">30MM COAT BUTTON</text>
    <text x="80" y="218" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#A89E8D" letter-spacing="0.1em" text-anchor="middle">NATURAL BUFFALO HORN</text>
  </g>

  <!-- 2. BESPOKE MOTHER-OF-PEARL SHIRT BUTTON (12MM) -->
  <g transform="translate(460, 200)">
    <circle cx="90" cy="90" r="65" fill="#14120E" opacity="0.10" filter="url(#softShadow)" />
    <!-- Button Face (Lustrous White Mother-of-Pearl with Champagne Iridescence) -->
    <circle cx="80" cy="80" r="60" fill="url(#champagneFoilSoft)" stroke="#DDD5C5" stroke-width="1.5" />
    <circle cx="80" cy="80" r="50" fill="#FFFFFF" opacity="0.85" />
    <circle cx="80" cy="80" r="42" fill="none" stroke="#C5B8A5" stroke-width="0.8" />

    <!-- Micro Inscribed Rim -->
    <text x="80" y="48" font-family="'Cinzel', serif" font-size="7" fill="#8E7348" letter-spacing="0.25em" text-anchor="middle">MEEN</text>
    <text x="80" y="122" font-family="'Cinzel', serif" font-size="7" fill="#8E7348" letter-spacing="0.25em" text-anchor="middle">MANIFESTATION</text>

    <!-- Holes -->
    <circle cx="70" cy="75" r="5" fill="#D3C9B8" />
    <circle cx="90" cy="75" r="5" fill="#D3C9B8" />
    <circle cx="70" cy="90" r="5" fill="#D3C9B8" />
    <circle cx="90" cy="90" r="5" fill="#D3C9B8" />

    <line x1="70" y1="75" x2="90" y2="75" stroke="#FFFFFF" stroke-width="2" />
    <line x1="70" y1="90" x2="90" y2="90" stroke="#FFFFFF" stroke-width="2" />

    <text x="80" y="200" font-family="'Montserrat', sans-serif" font-size="10" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">12MM SHIRT BUTTON</text>
    <text x="80" y="218" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#A89E8D" letter-spacing="0.1em" text-anchor="middle">AUSTRALIAN MOTHER-OF-PEARL</text>
  </g>

  <!-- 3. NFC DIGITAL AUTHENTICATION SARTORIAL CHIP -->
  <g transform="translate(760, 200)">
    <rect x="15" y="15" width="160" height="160" rx="12" fill="#14120E" opacity="0.10" filter="url(#softShadow)" />
    <!-- Silicone / Epoxy Encapsulated Micro NFC Tag sewn into inner label -->
    <rect x="0" y="0" width="160" height="160" rx="12" fill="#252525" stroke="url(#champagneFoil)" stroke-width="1.5" />
    
    <!-- Copper / Gold Antenna Coil Spiral Graphic -->
    <rect x="14" y="14" width="132" height="132" rx="8" fill="none" stroke="url(#champagneFoilSoft)" stroke-width="1" opacity="0.5" />
    <rect x="22" y="22" width="116" height="116" rx="6" fill="none" stroke="url(#champagneFoilSoft)" stroke-width="1" opacity="0.6" />
    <rect x="30" y="30" width="100" height="100" rx="4" fill="none" stroke="url(#champagneFoilSoft)" stroke-width="1" opacity="0.7" />

    <!-- Center MM Monogram & NFC Waves -->
    {get_mm_monogram(x=38, y=40, scale=0.48, color="url(#champagneFoil)")}
    
    <text x="80" y="125" font-family="'Montserrat', sans-serif" font-size="7" fill="url(#champagneFoil)" letter-spacing="0.2em" text-anchor="middle" font-weight="700">ENCRYPTED NFC</text>

    <text x="80" y="200" font-family="'Montserrat', sans-serif" font-size="10" fill="#736A5B" letter-spacing="0.2em" text-anchor="middle" font-weight="600">SARTORIAL NFC PASSPORT</text>
    <text x="80" y="218" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#A89E8D" letter-spacing="0.1em" text-anchor="middle">IP68 WASHABLE ATELIER CHIP</text>
  </g>

  <!-- TECHNICAL BLUEPRINT DIAGRAM AT BOTTOM -->
  <g transform="translate(100, 520)">
    <rect x="0" y="0" width="900" height="230" rx="6" fill="#FFFFFF" stroke="#DDD6C8" stroke-width="1" />
    <text x="30" y="32" font-family="'Cinzel', serif" font-size="12" fill="#252525" letter-spacing="0.2em" font-weight="700">TECHNICAL MANUFACTURING SPECIFICATIONS FOR HARDWARE</text>
    
    <text x="30" y="65" font-family="'Montserrat', sans-serif" font-size="8.5" fill="#333333">1. Horn Buttons: Carved from ethically sourced Asian water buffalo horn; matte satin tumble finish; laser-etched lettering with champagne lacquer fill.</text>
    <text x="30" y="90" font-family="'Montserrat', sans-serif" font-size="8.5" fill="#333333">2. Mother-of-Pearl: Pinctada Maxima oyster shell; 4.0mm caliper thickness with beveled rim for buttonhole fluidity.</text>
    <text x="30" y="115" font-family="'Montserrat', sans-serif" font-size="8.5" fill="#333333">3. NFC Chip: NTAG213 cryptographic chip; tuned to 13.56 MHz; encased in medical-grade TPU to withstand 90°C dry cleaning and pressing.</text>
    <text x="30" y="140" font-family="'Montserrat', sans-serif" font-size="8.5" fill="#333333">4. Brass Hardware: Lead-free architectural brass with micro-clearcoat galvanic champagne gold finish (passes 48h salt-spray anti-tarnish test).</text>
  </g>
</svg>'''
    with open("assets/packaging/11_bespoke_hardware_and_buttons.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def main():
    print("Generating haute couture extensions...")
    generate_garment_bag()
    generate_ribbon_and_folio()
    generate_hardware_and_buttons()
    print("Haute couture extensions generated successfully!")

if __name__ == "__main__":
    main()

