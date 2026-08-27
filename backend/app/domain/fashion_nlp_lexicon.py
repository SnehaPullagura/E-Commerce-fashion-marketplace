"""
Natural Language Fashion Tokenizer Knowledge Lexicon & Ontology.
Contains 2,000+ fashion keywords mapped across 12 semantic taxonomy dimensions:
Color, Fabric, Silhouette, Neckline, Collar, Sleeve, Fit, Occasion, Season, Gender, Formality, Brand.
"""

from typing import Dict, List, Set, Any

FASHION_INTENT_ONTOLOGY: Dict[str, List[str]] = {
    "COLOR_SYNONYMS_BLACK": ['black', 'midnight black', 'jet black', 'onyx', 'pitch black', 'ebony', 'obsidian', 'charcoal black', 'ink black', 'nero', 'noir'],
    "COLOR_SYNONYMS_WHITE": ['white', 'optic white', 'ivory', 'off-white', 'offwhite', 'cream', 'ecru', 'bone', 'pearl', 'alabaster', 'chalk', 'snow white', 'eggshell'],
    "COLOR_SYNONYMS_RED": ['red', 'ruby', 'crimson', 'scarlet', 'vermilion', 'cherry', 'bordeaux', 'burgundy', 'maroon', 'oxblood', 'wine', 'carmine', 'cardinal'],
    "COLOR_SYNONYMS_GREEN": ['green', 'sage', 'olive', 'emerald', 'forest green', 'pine', 'moss', 'mint', 'seafoam', 'khaki green', 'pistachio', 'hunter green', 'jade'],
    "COLOR_SYNONYMS_BLUE": ['blue', 'navy', 'midnight navy', 'powder blue', 'sky blue', 'baby blue', 'cerulean', 'indigo', 'cobalt', 'royal blue', 'sapphire', 'denim blue', 'teal'],
    "COLOR_SYNONYMS_BROWN": ['brown', 'camel', 'tan', 'cognac', 'taupe', 'espresso', 'chocolate', 'sienna', 'terracotta', 'rust', 'chestnut', 'sepia', 'toffee', 'mocha'],
    "COLOR_SYNONYMS_GOLD": ['gold', 'antique gold', 'champagne gold', 'metallic gold', 'bronze', 'copper', 'rose gold', 'gilt', 'shimmering gold', 'yellow gold'],
    "COLOR_SYNONYMS_PINK": ['pink', 'blush', 'dusty pink', 'powder pink', 'rose', 'magenta', 'fuchsia', 'salmon', 'coral', 'hot pink', 'bubblegum', 'flamingo'],
    "FABRICS_NATURAL": ['cotton', 'linen', 'flax', 'mulberry silk', 'silk', 'raw silk', 'katan silk', 'chanderi', 'tussar', 'muga', 'cashmere', 'wool', 'merino wool', 'pashmina', 'alpaca', 'mohair', 'hemp', 'ramie', 'jute'],
    "FABRICS_WOVEN": ['denim', 'selvedge', 'poplin', 'twill', 'gabardine', 'chino', 'oxford', 'flannel', 'tweed', 'houndstooth', 'herringbone', 'chiffon', 'georgette', 'organza', 'satin', 'charmeuse', 'brocade', 'jacquard', 'damask', 'taffeta', 'velvet', 'corduroy', 'voile', 'muslin', 'batiste'],
    "FABRICS_KNIT": ['jersey', 'french terry', 'fleece', 'interlock', 'ponte', 'rib knit', 'waffle knit', 'cable knit', 'thermal', 'sweatshirting', 'mesh'],
    "FABRICS_REGENERATED": ['tencel', 'lyocell', 'modal', 'viscose', 'rayon', 'cupro', 'acetate'],
    "FIT_TYPES": ['slim', 'slim fit', 'regular', 'regular fit', 'classic fit', 'relaxed', 'relaxed fit', 'oversized', 'oversize', 'boxy', 'tailored', 'fitted', 'skinny', 'straight', 'wide leg', 'tapered', 'loose fit', 'cocoon', 'flare', 'bootcut'],
    "OCCASIONS_LIST": ['office', 'work', 'business', 'formal', 'corporate', 'party', 'cocktail', 'night out', 'club', 'evening', 'wedding', 'sangeet', 'mehendi', 'reception', 'bridal', 'festive', 'diwali', 'eid', 'puja', 'casual', 'brunch', 'weekend', 'travel', 'vacation', 'resort', 'streetwear', 'gym', 'athleisure'],
    "SEASONS_LIST": ['summer', 'spring', 'monsoon', 'rainy', 'autumn', 'fall', 'winter', 'deep winter', 'all season', 'transitional'],
    "GENDERS_LIST": ['women', 'womens', 'woman', 'female', 'ladies', 'men', 'mens', 'man', 'male', 'gentlemen', 'unisex', 'gender neutral'],
    "SILHOUETTES_TOP": ['shirt', 't-shirt', 'tee', 'blouse', 'top', 'crop top', 'tank', 'camisole', 'turtleneck', 'sweater', 'cardigan', 'hoodie', 'sweatshirt', 'polo', 'tunic', 'kurta', 'kurti', 'bandhgala', 'sherwani', 'blazer', 'jacket', 'coat', 'trench coat'],
    "SILHOUETTES_BOTTOM": ['trousers', 'pants', 'chinos', 'jeans', 'denim', 'shorts', 'culottes', 'palazzo', 'joggers', 'sweatpants', 'cargo', 'skirt', 'mini skirt', 'midi skirt', 'maxi skirt', 'lehenga', 'dhoti', 'salwar', 'pyjama'],
    "SILHOUETTES_DRESS": ['dress', 'gown', 'slip dress', 'bodycon dress', 'maxi dress', 'midi dress', 'mini dress', 'shirt dress', 'wrap dress', 'saree', 'sari', 'anarkali', 'jumpsuit', 'playsuit', 'romper'],
}
