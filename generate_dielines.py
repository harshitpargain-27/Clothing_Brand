"""
MEEN MANIFESTATION - Packaging Engineering & Dieline Blueprint Generator
Generates technical vector dielines for manufacturing & print packaging factories.
"""

def generate_bag_dieline():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 900" width="1400" height="900">
  <defs>
    <style>
      .cut-line { stroke: #D9381E; stroke-width: 1.5; fill: none; }
      .crease-line { stroke: #2A6F97; stroke-width: 1.2; stroke-dasharray: 6 4; fill: none; }
      .foil-block { fill: #B49A70; opacity: 0.85; }
      .dimension-line { stroke: #666666; stroke-width: 0.8; marker-end: url(#arrow); marker-start: url(#arrow); }
      .label-text { font-family: 'Montserrat', sans-serif; font-size: 10px; fill: #333333; }
      .title-text { font-family: 'Cinzel', serif; font-size: 16px; fill: #252525; font-weight: 700; }
    </style>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#666666" />
    </marker>
  </defs>

  <!-- Canvas Background -->
  <rect width="1400" height="900" fill="#FCFAF6" />

  <!-- Title & Production Metadata -->
  <text x="60" y="50" class="title-text">MEEN MANIFESTATION // LUXURY SHOPPING BAG DIELINE BLUEPRINT</text>
  <text x="60" y="75" class="label-text" font-weight="600">BAG SPECIFICATION: MEDIUM VERTICAL LUXURY BOUTIQUE TOTE (320 × 400 × 120 MM)</text>
  <text x="60" y="92" class="label-text">STOCK: 320GSM FEDRIGONI MATERICA COTTON / IVORY • FINISH: MATTE WATER-BASED VARNISH + HOT FOIL STAMPING (KURZ 429)</text>

  <!-- Legend -->
  <g transform="translate(900, 40)">
    <line x1="0" y1="10" x2="40" y2="10" class="cut-line" />
    <text x="50" y="14" class="label-text">SOLID RED: CUTTING LINE (DIE CUT)</text>

    <line x1="0" y1="30" x2="40" y2="30" class="crease-line" />
    <text x="50" y="34" class="label-text">DASHED BLUE: CREASE / FOLD LINE</text>

    <rect x="0" y="44" width="40" height="12" fill="#B49A70" opacity="0.8" />
    <text x="50" y="54" class="label-text">GOLD ZONE: FOIL EMBOSSING BLOCK</text>
  </g>

  <!-- Main Dieline Sheet Schematic -->
  <!-- Flattened Dieline consists of: Glue Flap (30mm) | Left Gusset (120mm) | Front Face (320mm) | Right Gusset (120mm) | Back Face (320mm) -->
  <!-- Vertical: Top Turn-in (50mm) | Body Height (400mm) | Bottom Flaps (90mm) -->
  <g transform="translate(100, 160)">
    <!-- Base Dieline Box -->
    <!-- Top Turn-in Fold Line -->
    <line x1="30" y1="60" x2="1150" y2="60" class="crease-line" />
    <!-- Bottom Crease Line -->
    <line x1="30" y1="540" x2="1150" y2="540" class="crease-line" />

    <!-- 1. Glue Flap (0 to 30) -->
    <polygon points="0,75 30,60 30,540 0,525" class="cut-line" fill="#F0EDE6" />
    <text x="15" y="300" class="label-text" transform="rotate(-90 15,300)" text-anchor="middle">GLUE FLAP (30mm)</text>

    <!-- 2. Left Gusset (30 to 190, width 160) -->
    <rect x="30" y="60" width="160" height="480" fill="none" stroke="none" />
    <!-- Vertical Gusset Center Crease -->
    <line x1="110" y1="60" x2="110" y2="540" class="crease-line" />
    <line x1="190" y1="0" x2="190" y2="620" class="crease-line" />
    <text x="110" y="300" class="label-text" text-anchor="middle">LEFT GUSSET (120mm)</text>

    <!-- 3. Front Face Panel (190 to 610, width 420) -->
    <rect x="190" y="60" width="420" height="480" fill="#FFFFFF" opacity="0.6" />
    <line x1="610" y1="0" x2="610" y2="620" class="crease-line" />
    <text x="400" y="140" class="label-text" font-weight="700" text-anchor="middle" font-size="12">FRONT FACE (320mm)</text>

    <!-- Rope Handle Eyelet / Ribbon Slots (2 positions) -->
    <circle cx="310" cy="110" r="6" stroke="#252525" stroke-width="1.5" fill="none" />
    <circle cx="490" cy="110" r="6" stroke="#252525" stroke-width="1.5" fill="none" />
    <text x="400" y="114" class="label-text" text-anchor="middle" font-size="8">PUNCH HOLES Ø6mm (REINFORCED CARD BACKING)</text>

    <!-- Hot Stamping Foil Area on Front Panel -->
    <rect x="300" y="220" width="200" height="180" rx="4" class="foil-block" />
    <text x="400" y="295" font-family="'Cinzel', serif" font-size="20" fill="#FFFFFF" text-anchor="middle" font-weight="700">MM</text>
    <text x="400" y="330" font-family="'Cinzel', serif" font-size="11" fill="#FFFFFF" text-anchor="middle" letter-spacing="0.2em">MEEN MANIFESTATION</text>
    <text x="400" y="350" font-family="'Montserrat', sans-serif" font-size="7" fill="#FFFFFF" text-anchor="middle" letter-spacing="0.2em">FOIL STAMPING BLOCK (HOT DIE 0.4MM RELIEF)</text>

    <!-- 4. Right Gusset (610 to 770, width 160) -->
    <line x1="690" y1="60" x2="690" y2="540" class="crease-line" />
    <line x1="770" y1="0" x2="770" y2="620" class="crease-line" />
    <text x="690" y="300" class="label-text" text-anchor="middle">RIGHT GUSSET (120mm)</text>

    <!-- 5. Back Face Panel (770 to 1190, width 420) -->
    <rect x="770" y="60" width="380" height="480" fill="#FFFFFF" opacity="0.6" />
    <!-- Back Punch Holes -->
    <circle cx="880" cy="110" r="6" stroke="#252525" stroke-width="1.5" fill="none" />
    <circle cx="1060" cy="110" r="6" stroke="#252525" stroke-width="1.5" fill="none" />
    <text x="970" y="300" class="label-text" text-anchor="middle">BACK FACE (320mm)</text>

    <!-- Outer Perimeter Cut Lines -->
    <!-- Top Cut -->
    <line x1="30" y1="0" x2="1150" y2="0" class="cut-line" />
    <!-- Right Cut -->
    <line x1="1150" y1="0" x2="1150" y2="620" class="cut-line" />
    <!-- Bottom Slits and Base Flaps -->
    <line x1="30" y1="620" x2="1150" y2="620" class="cut-line" />
    <!-- Flap cuts between panels at bottom -->
    <line x1="190" y1="540" x2="190" y2="620" class="cut-line" />
    <line x1="610" y1="540" x2="610" y2="620" class="cut-line" />
    <line x1="770" y1="540" x2="770" y2="620" class="cut-line" />

    <!-- Gusset Bottom Triangle Creases for automatic folding -->
    <line x1="30" y1="540" x2="110" y2="620" class="crease-line" />
    <line x1="190" y1="540" x2="110" y2="620" class="crease-line" />
    <line x1="610" y1="540" x2="690" y2="620" class="crease-line" />
    <line x1="770" y1="540" x2="690" y2="620" class="crease-line" />
  </g>

  <!-- Technical Engineering Notes -->
  <g transform="translate(100, 800)">
    <text x="0" y="0" class="label-text" font-weight="700">MANUFACTURING NOTES:</text>
    <text x="0" y="16" class="label-text">1. Reinforced greyboard inserts (800gsm) glued into top turn-in and bottom base for maximum structural rigidity.</text>
    <text x="0" y="32" class="label-text">2. Handle: 14mm thick round braided herringbone cotton cord, 480mm length, hand-knotted concealed inside turn-in.</text>
    <text x="0" y="48" class="label-text">3. Maximum load capacity: 8.5 kg. Internal glue: Water-based archival hotmelt.</text>
  </g>
</svg>'''
    with open("assets/packaging/01_luxury_shopping_bag_dieline.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_box_dieline():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 950" width="1400" height="950">
  <defs>
    <style>
      .cut-line { stroke: #D9381E; stroke-width: 1.5; fill: none; }
      .crease-line { stroke: #2A6F97; stroke-width: 1.2; stroke-dasharray: 6 4; fill: none; }
      .magnet-zone { fill: #E7C27D; stroke: #B49A70; stroke-width: 1.2; stroke-dasharray: 2 2; }
      .board-panel { fill: #EDE8DF; stroke: #CBC2B0; stroke-width: 1; }
      .label-text { font-family: 'Montserrat', sans-serif; font-size: 10px; fill: #333333; }
      .title-text { font-family: 'Cinzel', serif; font-size: 16px; fill: #252525; font-weight: 700; }
    </style>
  </defs>

  <rect width="1400" height="950" fill="#FCFAF6" />

  <text x="60" y="50" class="title-text">MEEN MANIFESTATION // RIGID CLAMSHELL MAGNETIC BOX BLUEPRINT</text>
  <text x="60" y="75" class="label-text" font-weight="600">BOX TYPE: 3-PIECE BOOK-STYLE CLAMSHELL RIGID BOX WITH HIDDEN MAGNETIC FLAP</text>
  <text x="60" y="92" class="label-text">DIMENSIONS: 380 × 280 × 90 MM • GREYBOARD: 1800GSM KAPPA BOARD • WRAP: 135GSM G.F SMITH COLORPLAN CASHMERE</text>

  <!-- Dieline Schematic: 3 Cover Panels (Back Lid, Spine, Front Base, Front Magnetic Flap) -->
  <g transform="translate(100, 150)">
    <!-- OUTER COVER WRAP (ONE PIECE FLAT SHEET) -->
    <!-- Magnetic Closure Lip (40mm) -->
    <rect x="0" y="40" width="60" height="380" class="board-panel" />
    <circle cx="30" cy="150" r="10" class="magnet-zone" />
    <circle cx="30" cy="310" r="10" class="magnet-zone" />
    <text x="30" y="230" class="label-text" transform="rotate(-90 30,230)" text-anchor="middle" font-size="8">MAGNETIC LIP (NEODYMIUM N52)</text>

    <!-- Crease Line -->
    <line x1="60" y1="0" x2="60" y2="460" class="crease-line" />

    <!-- Top Lid Panel (380mm × 280mm) -->
    <rect x="60" y="40" width="380" height="380" class="board-panel" />
    <text x="250" y="100" class="label-text" font-weight="700" text-anchor="middle">TOP LID PANEL (380 × 280 MM)</text>
    <!-- Foil Stamped MM Monogram Area -->
    <rect x="200" y="160" width="100" height="100" rx="4" fill="#B49A70" opacity="0.8" />
    <text x="250" y="215" font-family="'Cinzel', serif" font-size="16" fill="#FFFFFF" text-anchor="middle" font-weight="700">MM</text>
    <text x="250" y="235" font-family="'Cinzel', serif" font-size="8" fill="#FFFFFF" text-anchor="middle">MEEN MANIFESTATION</text>
    <text x="250" y="280" class="label-text" text-anchor="middle" font-size="7.5">FOIL STAMPING DIE RECESS (0.3MM)</text>

    <!-- Spine Crease 1 -->
    <line x1="440" y1="0" x2="440" y2="460" class="crease-line" />

    <!-- Box Spine Panel (92mm) -->
    <rect x="440" y="40" width="95" height="380" class="board-panel" />
    <text x="487" y="230" class="label-text" transform="rotate(-90 487,230)" text-anchor="middle">SPINE PANEL (92MM)</text>

    <!-- Spine Crease 2 -->
    <line x1="535" y1="0" x2="535" y2="460" class="crease-line" />

    <!-- Base Floor Panel (380mm × 280mm) -->
    <rect x="535" y="40" width="380" height="380" class="board-panel" />
    <text x="725" y="230" class="label-text" font-weight="700" text-anchor="middle">BASE FLOOR PANEL (GLUED TO INNER TRAY)</text>

    <!-- Outer Wrap Paper Turn-in Margins (20mm perimeter all around) -->
    <rect x="-20" y="20" width="955" height="420" rx="2" class="cut-line" />
    <text x="475" y="15" class="label-text" text-anchor="middle" fill="#D9381E">20MM PAPER WRAP TURN-IN WITH MITRED 45° CORNERS</text>
  </g>

  <!-- INNER TRAY ASSEMBLY (BOTTOM RIGHT SCHEMATIC) -->
  <g transform="translate(100, 640)">
    <rect x="0" y="0" width="1180" height="230" rx="4" fill="#FFFFFF" stroke="#CBC2B0" stroke-width="1" />
    <text x="30" y="30" class="title-text" font-size="13">INNER TRAY CONSTRUCTION &amp; VELVET CUSHION SPECIFICATIONS</text>
    
    <text x="30" y="60" class="label-text">1. Rigid Tray walls: 4-side folded kappa board with concealed V-groove 90° precision routing.</text>
    <text x="30" y="80" class="label-text">2. Lining: 0.8mm plush Ivory micro-suede velvet laminated to recycled EVA foam base.</text>
    <text x="30" y="100" class="label-text">3. Pull tab: 25mm double-faced champagne satin ribbon anchored securely under base plate.</text>
    <text x="30" y="120" class="label-text">4. Neodymium Magnet polarity: Pair A (Lid flap) + Pair B (Tray front wall), pull force 2.4 kg for distinct luxury acoustic snap.</text>
    <text x="30" y="140" class="label-text">5. Tolerances: Tray to lid clearance 1.5mm per side to ensure smooth air-cushioned vacuum opening feel.</text>

    <!-- Small Vector Visual of the Magnet Snap -->
    <g transform="translate(850, 40)">
      <circle cx="50" cy="50" r="30" fill="none" stroke="#B49A70" stroke-width="2" />
      <circle cx="50" cy="50" r="16" fill="#B49A70" />
      <text x="50" y="54" font-family="'Montserrat', sans-serif" font-size="10" fill="#FFFFFF" font-weight="700" text-anchor="middle">SNAP</text>
      <text x="50" y="100" class="label-text" text-anchor="middle" font-size="8">ACOUSTIC DAMPENED</text>
    </g>
  </g>
</svg>'''
    with open("assets/packaging/02_rigid_clothing_box_dieline.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def generate_tags_and_labels_dieline():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">
  <defs>
    <style>
      .cut-line { stroke: #D9381E; stroke-width: 1.5; fill: none; }
      .crease-line { stroke: #2A6F97; stroke-width: 1.2; stroke-dasharray: 4 3; fill: none; }
      .label-text { font-family: 'Montserrat', sans-serif; font-size: 10px; fill: #333333; }
      .title-text { font-family: 'Cinzel', serif; font-size: 15px; fill: #252525; font-weight: 700; }
    </style>
  </defs>

  <rect width="1200" height="800" fill="#FCFAF6" />
  <text x="60" y="50" class="title-text">MEEN MANIFESTATION // HANG TAG &amp; WOVEN LABEL ENGINEERING BLUEPRINT</text>

  <!-- Hang Tag Dieline -->
  <g transform="translate(80, 110)">
    <rect x="0" y="0" width="300" height="560" rx="8" class="cut-line" />
    <circle cx="150" cy="40" r="4.5" stroke="#D9381E" stroke-width="1.5" fill="none" />
    
    <!-- Gilded Beveled Edge Specification -->
    <rect x="10" y="10" width="280" height="540" rx="4" fill="none" stroke="#B49A70" stroke-width="1.5" stroke-dasharray="3 3" />
    <text x="150" y="100" class="label-text" font-weight="700" text-anchor="middle">HANG TAG CUT SIZE: 55 × 125 MM</text>
    <text x="150" y="120" class="label-text" text-anchor="middle">SUBSTRATE: 650GSM DUPLEX BOARD</text>
    <text x="150" y="140" class="label-text" text-anchor="middle">CHAMPAGNE GILDED EDGES (HOT BEVEL)</text>
    <text x="150" y="160" class="label-text" text-anchor="middle">BRASS EYELET Ø5MM</text>

    <text x="150" y="600" class="label-text" font-weight="700" text-anchor="middle">DIELINE SPEC: HANG TAG DUPLEX</text>
  </g>

  <!-- Woven Neck Label Specification -->
  <g transform="translate(500, 110)">
    <!-- End Fold Label -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="450" height="180" class="cut-line" />
      <!-- Left & Right Fold Lines -->
      <line x1="35" y1="0" x2="35" y2="180" class="crease-line" />
      <line x1="415" y1="0" x2="415" y2="180" class="crease-line" />
      <text x="17" y="95" class="label-text" transform="rotate(-90 17,95)" text-anchor="middle" font-size="8">END FOLD (7mm)</text>
      <text x="432" y="95" class="label-text" transform="rotate(-90 432,95)" text-anchor="middle" font-size="8">END FOLD (7mm)</text>
      <text x="225" y="70" class="label-text" font-weight="700" text-anchor="middle">WOVEN NECK LABEL // END-FOLD FLAT</text>
      <text x="225" y="90" class="label-text" text-anchor="middle">CUT SIZE: 80 × 35 MM | FINISHED: 66 × 35 MM</text>
      <text x="225" y="110" class="label-text" text-anchor="middle">WEAVE: HIGH DEFINITION 100D/2 DAMASK JACQUARD</text>
      <text x="225" y="130" class="label-text" text-anchor="middle">HEAT-SEALED ULTRASONIC EDGES (NO FRAY)</text>
    </g>

    <!-- Center Loop Fold Label -->
    <g transform="translate(0, 240)">
      <rect x="0" y="0" width="220" height="300" class="cut-line" />
      <line x1="0" y1="150" x2="220" y2="150" class="crease-line" />
      <line x1="0" y1="30" x2="220" y2="30" class="crease-line" stroke="#888888" />
      <text x="110" y="20" class="label-text" text-anchor="middle" font-size="8">SEAM ALLOWANCE (8mm)</text>
      <text x="110" y="90" class="label-text" font-weight="700" text-anchor="middle">CENTER LOOP FOLD</text>
      <text x="110" y="110" class="label-text" text-anchor="middle">CUT: 35 × 70 MM</text>
      <text x="110" y="130" class="label-text" text-anchor="middle">FINISHED: 35 × 30 MM</text>
      <text x="110" y="220" class="label-text" text-anchor="middle">BACK: CARE / SYMBOLS</text>
    </g>

    <!-- Micro Pip Label -->
    <g transform="translate(260, 240)">
      <rect x="0" y="0" width="160" height="140" class="cut-line" />
      <line x1="0" y1="70" x2="160" y2="70" class="crease-line" />
      <text x="80" y="45" class="label-text" font-weight="700" text-anchor="middle">HEM / SLEEVE PIP TAB</text>
      <text x="80" y="110" class="label-text" text-anchor="middle">FOLD OVER SEAM</text>
    </g>
  </g>
</svg>'''
    with open("assets/packaging/03_clothing_hang_tag_dieline.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def main():
    print("Generating technical dielines...")
    generate_bag_dieline()
    generate_box_dieline()
    generate_tags_and_labels_dieline()
    print("Dielines successfully generated!")

if __name__ == "__main__":
    main()

