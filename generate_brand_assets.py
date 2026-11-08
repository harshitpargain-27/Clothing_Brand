"""
MEEN MANIFESTATION - Luxury Brand Identity Vector Generator
Generates pristine vector SVGs for all 8 packaging & label touchpoints, logos, and dielines.
"""

import os
import math

def get_foil_gradient_defs():
    return '''
    <defs>
      <!-- Champagne Gold Foil Gradients -->
      <linearGradient id="champagneFoil" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#E5D6BA" />
        <stop offset="25%" stop-color="#B49A70" />
        <stop offset="45%" stop-color="#F3E9D2" />
        <stop offset="70%" stop-color="#A5895E" />
        <stop offset="85%" stop-color="#CBB590" />
        <stop offset="100%" stop-color="#8E7348" />
      </linearGradient>

      <linearGradient id="champagneFoilHoriz" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#9C8054" />
        <stop offset="20%" stop-color="#D9C7A7" />
        <stop offset="40%" stop-color="#F5EFE0" />
        <stop offset="60%" stop-color="#B49A70" />
        <stop offset="80%" stop-color="#E2D4BE" />
        <stop offset="100%" stop-color="#8C7146" />
      </linearGradient>

      <linearGradient id="champagneFoilDiag" x1="0%" y1="100%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#8A7046" />
        <stop offset="25%" stop-color="#C9B48F" />
        <stop offset="50%" stop-color="#FFF8E7" />
        <stop offset="75%" stop-color="#B49A70" />
        <stop offset="100%" stop-color="#967B50" />
      </linearGradient>

      <!-- Soft Luxury Shadow Filters -->
      <filter id="softShadow" x="-10%" y="-10%" width="130%" height="130%">
        <feDropShadow dx="0" dy="12" stdDeviation="24" flood-color="#000000" flood-opacity="0.08" />
        <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000000" flood-opacity="0.05" />
      </filter>

      <filter id="deepShadow" x="-20%" y="-20%" width="140%" height="140%">
        <feDropShadow dx="0" dy="25" stdDeviation="35" flood-color="#14120E" flood-opacity="0.16" />
        <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#14120E" flood-opacity="0.08" />
      </filter>

      <filter id="foilGleam" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="1.5" result="blur" />
        <feColorMatrix type="matrix" values="1 0 0 0 0.8  0 1 0 0 0.7  0 0 1 0 0.5  0 0 0 1.2 0"/>
        <feMerge>
          <feMergeNode />
          <feMergeNode in="SourceGraphic" />
        </feMerge>
      </filter>

      <!-- Emboss & Deboss Filters -->
      <filter id="blindDeboss" x="-10%" y="-10%" width="120%" height="120%">
        <feOffset dx="-1" dy="-1" in="SourceAlpha" result="offsetNeg"/>
        <feOffset dx="1" dy="1" in="SourceAlpha" result="offsetPos"/>
        <feFlood flood-color="#FFFFFF" flood-opacity="0.8" result="lightFlood"/>
        <feFlood flood-color="#000000" flood-opacity="0.25" result="shadowFlood"/>
        <feComposite in="lightFlood" in2="offsetNeg" operator="in" result="highlight"/>
        <feComposite in="shadowFlood" in2="offsetPos" operator="in" result="shadow"/>
        <feMerge>
          <feMergeNode in="highlight"/>
          <feMergeNode in="shadow"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>

      <!-- Subtle Paper Texture Pattern -->
      <pattern id="paperTexture" width="100" height="100" patternUnits="userSpaceOnUse">
        <rect width="100" height="100" fill="#F8F7F3" />
        <circle cx="15" cy="15" r="0.6" fill="#000000" opacity="0.03" />
        <circle cx="85" cy="45" r="0.8" fill="#000000" opacity="0.02" />
        <circle cx="45" cy="85" r="0.5" fill="#000000" opacity="0.035" />
        <circle cx="65" cy="25" r="0.7" fill="#000000" opacity="0.025" />
        <circle cx="30" cy="60" r="0.6" fill="#000000" opacity="0.03" />
      </pattern>

      <pattern id="beigeBoxTexture" width="100" height="100" patternUnits="userSpaceOnUse">
        <rect width="100" height="100" fill="#EDE8DF" />
        <circle cx="20" cy="30" r="0.7" fill="#000000" opacity="0.03" />
        <circle cx="70" cy="80" r="0.8" fill="#000000" opacity="0.035" />
        <circle cx="50" cy="15" r="0.5" fill="#000000" opacity="0.025" />
      </pattern>
    </defs>
    '''

def get_mm_monogram_path(x=0, y=0, scale=1.0, color="url(#champagneFoil)"):
    """
    Returns an exquisite architectural luxury interlocking MM monogram.
    Designed with high-fashion proportions: classical serifs, razor vertexes,
    harmonious overlapping geometry and balanced optical weight.
    """
    return f'''
    <g transform="translate({x}, {y}) scale({scale})" class="mm-monogram-symbol">
      <!-- First M (Left Architecture) -->
      <!-- Left Stem -->
      <path d="M 28 92 L 36 92 L 36 28 L 28 28 L 28 22 L 50 22 L 50 28 L 43 28 L 43 86 L 43 92 Z" fill="{color}" />
      <!-- Left Diagonal Down -->
      <polygon points="41,25 72,82 77,82 49,25" fill="{color}" />
      <!-- Left Diagonal Up -->
      <polygon points="73,82 78,82 105,25 99,25" fill="{color}" />
      <!-- First M Right Stem -->
      <path d="M 98 22 L 120 22 L 120 28 L 112 28 L 112 86 L 119 86 L 119 92 L 98 92 L 98 86 L 105 86 L 105 28 L 98 28 Z" fill="{color}" />

      <!-- Second M (Interlocking Right Architecture, offset X=50) -->
      <!-- Second M Left Stem (Intertwines behind/across) -->
      <path d="M 78 22 L 100 22 L 100 28 L 92 28 L 92 86 L 99 86 L 99 92 L 78 92 L 78 86 L 85 86 L 85 28 L 78 28 Z" fill="{color}" opacity="0.95" />
      <!-- Second M Diagonal Down -->
      <polygon points="91,25 122,82 127,82 99,25" fill="{color}" />
      <!-- Second M Diagonal Up -->
      <polygon points="123,82 128,82 155,25 149,25" fill="{color}" />
      <!-- Second M Right Stem -->
      <path d="M 148 22 L 170 22 L 170 28 L 162 28 L 162 86 L 169 86 L 169 92 L 148 92 L 148 86 L 155 86 L 155 28 L 148 28 Z" fill="{color}" />

      <!-- Center Geometric Luxury Medallion Accent Accent Lines -->
      <line x1="24" y1="98" x2="174" y2="98" stroke="{color}" stroke-width="0.75" stroke-dasharray="2 4" opacity="0.6"/>
    </g>
    '''

def create_primary_logos():
    print("Generating primary logo assets...")
    foil_defs = get_foil_gradient_defs()

    # 1. MM Monogram Primary (Champagne Foil)
    svg_monogram = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="800" height="800">
  {foil_defs}
  <rect width="400" height="400" fill="#F8F7F3" />
  <!-- Subtle circular luxury border ring -->
  <circle cx="200" cy="200" r="160" fill="none" stroke="url(#champagneFoil)" stroke-width="1.5" opacity="0.4" />
  <circle cx="200" cy="200" r="168" fill="none" stroke="url(#champagneFoil)" stroke-width="0.5" stroke-dasharray="3 3" opacity="0.5" />
  
  <!-- Centered MM Monogram -->
  {get_mm_monogram_path(x=101, y=145, scale=1.0, color="url(#champagneFoil)")}

  <!-- Micro Brand Subtext -->
  <text x="200" y="275" font-family="'Cinzel', 'Playfair Display', 'Didot', 'Georgia', serif" font-size="12" fill="#B49A70" letter-spacing="0.38em" text-anchor="middle" font-weight="500">MEEN MANIFESTATION</text>
  <text x="200" y="295" font-family="'Montserrat', 'Helvetica Neue', 'Arial', sans-serif" font-size="7.5" fill="#756A59" letter-spacing="0.42em" text-anchor="middle">HAUTE COUTURE • EST. 2026</text>
</svg>'''
    with open("assets/logos/mm_monogram_champagne_foil.svg", "w", encoding="utf-8") as f:
        f.write(svg_monogram)

    # 2. MM Monogram Charcoal
    svg_monogram_charcoal = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="800" height="800">
  {foil_defs}
  <rect width="400" height="400" fill="#FFFFFF" />
  <circle cx="200" cy="200" r="160" fill="none" stroke="#252525" stroke-width="1.2" opacity="0.8" />
  <circle cx="200" cy="200" r="166" fill="none" stroke="#252525" stroke-width="0.5" stroke-dasharray="2 3" opacity="0.4" />
  {get_mm_monogram_path(x=101, y=145, scale=1.0, color="#252525")}
  <text x="200" y="275" font-family="'Cinzel', 'Playfair Display', 'Didot', 'Georgia', serif" font-size="12" fill="#252525" letter-spacing="0.38em" text-anchor="middle" font-weight="500">MEEN MANIFESTATION</text>
  <text x="200" y="295" font-family="'Montserrat', 'Helvetica Neue', 'Arial', sans-serif" font-size="7.5" fill="#555555" letter-spacing="0.42em" text-anchor="middle">HAUTE COUTURE • EST. 2026</text>
</svg>'''
    with open("assets/logos/mm_monogram_charcoal.svg", "w", encoding="utf-8") as f:
        f.write(svg_monogram_charcoal)

    # 3. Horizontal Wordmark
    svg_wordmark = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="1200" height="320">
  {foil_defs}
  <rect width="1200" height="320" fill="#F8F7F3" />
  
  <!-- Subtle Decorative Rules -->
  <line x1="160" y1="80" x2="1040" y2="80" stroke="url(#champagneFoilHoriz)" stroke-width="1" opacity="0.3" />
  <line x1="160" y1="240" x2="1040" y2="240" stroke="url(#champagneFoilHoriz)" stroke-width="1" opacity="0.3" />

  <!-- Monogram Accent in Left Center -->
  {get_mm_monogram_path(x=180, y=105, scale=0.85, color="url(#champagneFoil)")}

  <!-- Brand Typography -->
  <text x="360" y="160" font-family="'Cinzel', 'Playfair Display', 'Didot', 'Georgia', serif" font-size="44" fill="#252525" letter-spacing="0.32em" font-weight="500">MEEN MANIFESTATION</text>
  <text x="363" y="200" font-family="'Montserrat', 'Helvetica Neue', 'Arial', sans-serif" font-size="14" fill="#B49A70" letter-spacing="0.48em" font-weight="400">NOT JUST FASHION. A STATEMENT OF IDENTITY.</text>
</svg>'''
    with open("assets/logos/meen_manifestation_wordmark.svg", "w", encoding="utf-8") as f:
        f.write(svg_wordmark)

    # 4. Full Vertical Brand Lockup
    svg_vertical_lockup = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  {foil_defs}
  <rect width="800" height="800" fill="#F8F7F3" />
  
  <rect x="50" y="50" width="700" height="700" fill="none" stroke="#EDE8DF" stroke-width="1.5" />
  <rect x="62" y="62" width="676" height="676" fill="none" stroke="url(#champagneFoil)" stroke-width="0.75" stroke-dasharray="4 4" opacity="0.4" />

  <!-- Central MM Monogram -->
  {get_mm_monogram_path(x=301, y=260, scale=2.0, color="url(#champagneFoil)")}

  <!-- Typography -->
  <text x="400" y="520" font-family="'Cinzel', 'Playfair Display', 'Didot', 'Georgia', serif" font-size="34" fill="#252525" letter-spacing="0.36em" text-anchor="middle" font-weight="600">MEEN MANIFESTATION</text>
  
  <line x1="330" y1="555" x2="470" y2="555" stroke="url(#champagneFoilHoriz)" stroke-width="1.2" />
  
  <text x="400" y="590" font-family="'Montserrat', 'Helvetica Neue', 'Arial', sans-serif" font-size="13" fill="#B49A70" letter-spacing="0.44em" text-anchor="middle" font-weight="500">NOT JUST FASHION. A STATEMENT OF IDENTITY.</text>

  <text x="400" y="670" font-family="'Montserrat', 'Helvetica Neue', 'Arial', sans-serif" font-size="9" fill="#888888" letter-spacing="0.35em" text-anchor="middle">PARIS • MILANO • NEW YORK • LONDON</text>
</svg>'''
    with open("assets/logos/full_lockup_vertical.svg", "w", encoding="utf-8") as f:
        f.write(svg_vertical_lockup)

create_primary_logos()

