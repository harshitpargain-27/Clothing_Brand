"""
MEEN MANIFESTATION - Circular Stitched Medallion Seal Generator
Replaces the MM monogram with the user's official circular stitched celestial fish seal.
"""

from generate_meen_fish_vector import get_defs_with_blush, get_celestial_fish_svg

def get_circular_seal_svg(cx=200, cy=200, r=180, scale=1.0, color="url(#champagneFoil)", text_color="#252525"):
    """
    Returns the exact circular stitched luxury seal uploaded by user:
    - Outer solid circle
    - Inner dashed couture stitch line
    - Inner solid hairline circle
    - Celestial golden fish with blush fill and sparkle stars
    - Dotted baseline divider
    - 'MEEN MANIFESTATION' typography across the lower section
    """
    return f'''
    <g transform="translate({cx - 200 * scale}, {cy - 200 * scale}) scale({scale})" class="meen-circular-stitched-seal">
      <!-- Outer Solid Ring -->
      <circle cx="200" cy="200" r="185" fill="none" stroke="{color}" stroke-width="2.5" />
      
      <!-- Middle Dashed Couture Stitching Ring -->
      <circle cx="200" cy="200" r="172" fill="none" stroke="{color}" stroke-width="1.8" stroke-dasharray="7 5" />
      
      <!-- Inner Solid Hairline Ring -->
      <circle cx="200" cy="200" r="162" fill="none" stroke="{color}" stroke-width="1.2" />

      <!-- Center Celestial Golden Fish -->
      {get_celestial_fish_svg(x=95, y=55, scale=0.72, color=color, show_sparkles=True)}

      <!-- Dotted Baseline Divider -->
      <line x1="85" y1="318" x2="315" y2="318" stroke="{color}" stroke-width="1" stroke-dasharray="2 3" opacity="0.8" />

      <!-- MEEN MANIFESTATION Brand Typography -->
      <text x="200" y="348" font-family="'Cinzel', 'Playfair Display', 'Didot', 'Georgia', serif" font-size="20.5" fill="{text_color}" letter-spacing="0.22em" text-anchor="middle" font-weight="600">MEEN MANIFESTATION</text>
    </g>
    '''

def create_circular_seal_assets():
    defs = get_defs_with_blush()

    # 1. Standalone Circular Stitched Seal (Foil on Ivory)
    svg_seal_foil = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="1000" height="1000">
  {defs}
  <rect width="500" height="500" fill="#FAF8F5" />
  {get_circular_seal_svg(cx=250, cy=250, r=185, scale=1.18, color="url(#champagneFoil)", text_color="#252525")}
  <!-- Tiny subtle sparkle stars outside rim -->
  <g transform="translate(460, 460) scale(0.4)">
    <path d="M 0 -18 Q 0 0 18 0 Q 0 0 0 18 Q 0 0 -18 0 Q 0 0 0 -18 Z" fill="#B49A70" opacity="0.4" />
  </g>
</svg>'''
    with open("assets/logos/meen_circular_seal_logo.svg", "w", encoding="utf-8") as f:
        f.write(svg_seal_foil)

    # 2. Standalone Circular Seal in Pure Gold Foil
    svg_seal_pure_gold = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="1000" height="1000">
  {defs}
  <rect width="500" height="500" fill="#FAF8F5" />
  {get_circular_seal_svg(cx=250, cy=250, r=185, scale=1.18, color="url(#champagneFoil)", text_color="url(#champagneFoil)")}
</svg>'''
    with open("assets/logos/meen_official_monogram_seal.svg", "w", encoding="utf-8") as f:
        f.write(svg_seal_pure_gold)

    # 3. Charcoal Monochrome Version for technical specs
    svg_seal_charcoal = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="1000" height="1000">
  {defs}
  <rect width="500" height="500" fill="#FFFFFF" />
  {get_circular_seal_svg(cx=250, cy=250, r=185, scale=1.18, color="#252525", text_color="#252525")}
</svg>'''
    with open("assets/logos/meen_circular_seal_charcoal.svg", "w", encoding="utf-8") as f:
        f.write(svg_seal_charcoal)

    print("Circular stitched medallion seal SVGs generated successfully!")

if __name__ == "__main__":
    create_circular_seal_assets()

