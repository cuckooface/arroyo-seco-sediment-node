# Position sheets: every editable value lives here.
# build.py reads this file; rearrange the pile-up by changing PILEUP only.
# Units are inches. Sheet origin is the top-left corner; x runs right, y runs down.

SHEET_W, SHEET_H = 11.0, 8.5        # 8.5 x 11 landscape
MARGIN = 0.25
DPI = 300

# Optional single line on the pile-up. Set to None to leave the sheet text-free.
QUOTE = "There is no wild here. The landscape is what we keep doing to it."
QUOTE_POS = (4.15, 0.42)            # left edge, baseline

POSITION = (
    "Push into the artificial, not between. The Arroyo Seco is fully engineered: dams, "
    "channelization, debris basins, yearly sediment removal. The only living landscape in "
    "Los Angeles is a maintained one. Maintenance that is hidden gets abandoned; made public, "
    "it becomes productive culture."
)
MATERIAL = (
    "Landscape becomes manufactured material. Sediment becomes earth, earth becomes printed "
    "ceramic. Tiles printed each year from that year's sediment form a facade that records "
    "the watershed in bands, like a geological core."
)
MAYNE_PROMPT = "What if every building maintained its own water?"
MAYNE = [
    ("For", "Distributed responsibility scales maintenance citywide."),
    ("Against", "Private on-site systems are hidden maintenance, the kind that gets abandoned. "
                "Sediment is a watershed problem no single building can solve."),
    ("Synthesis", "Buildings maintain their own rain. Public nodes handle what no building can "
                  "(sediment, debris, treatment) and make that work visible. Two scales, one system."),
]

# Each reference. Image file is images/<id>.jpg (or .png/.jpeg/.tif).
#   aspect  : width / height of the frame the image is cropped into (cover fit)
#   focus   : (fx, fy) 0..1, which part of the source to keep when cropping
#   info    : Information block lines on the reference page
#   project : how the reference bears on the Arroyo Seco position
REFERENCES = [
    dict(id="BASE", group="BASE", aspect=1.43, focus=(0.5, 0.5),
         title="Los Angeles River channelization under construction",
         author="U.S. Army Corps of Engineers", year="late 1930s",
         image="Historic black and white construction photo of the concrete channel.",
         info=["U.S. Army Corps of Engineers with LA County Flood Control",
               "Begun after the March 1938 flood",
               "By 1960 most of the river and the Arroyo Seco run in concrete"],
         caption="The landscape is engineered. There is no \"natural\" Arroyo to restore.",
         project="Sets the ground for the whole position. Restoration assumes a prior nature to "
                 "return to. In the Arroyo Seco that nature was replaced by a flood control "
                 "machine eighty years ago, so the only honest move is to design the machine's "
                 "upkeep, not to hide it under planting."),
    dict(id="F1", group="FOR", aspect=1.33, focus=(0.5, 0.4),
         title="Touch Sanitation", author="Mierle Laderman Ukeles", year="1979 to 1980",
         image="Ukeles shaking hands with a New York City sanitation worker.",
         info=["Performance across all 59 New York sanitation districts",
               "Ukeles shook hands with every sanitation worker, roughly 8,500 people",
               "\"Thank you for keeping New York City alive\"",
               "Follows Manifesto for Maintenance Art 1969!"],
         caption="Maintenance labor made public becomes culture, not invisible service.",
         project="The founding text for the argument that visibility creates a constituency. "
                 "Work that the public sees and thanks is harder to defund. The sheet places it "
                 "on top of the material sequence because labor is what turns sediment into "
                 "material: nothing in the loop happens without a crew."),
    dict(id="F2", group="FOR", aspect=1.45, focus=(0.5, 0.5),
         title="Chand Baori stepwell", author="Abhaneri, Rajasthan", year="9th century",
         image="Wide view of the geometric stepped walls.",
         info=["Stepwell of about 3,500 steps over thirteen levels",
               "Collective water storage, bathing and gathering space",
               "Stepwells fell out of use when piped water and tube wells arrived"],
         caption="Collective water infrastructure that fell into neglect once piped water made "
                 "the work invisible. The thesis as historical evidence.",
         project="Proof that civic water architecture can be monumental and social, and proof "
                 "of the failure mode. When the work moved into pipes, the public stopped "
                 "seeing it, and the structure lost its constituency. The same thing happened "
                 "behind Devil's Gate Dam from 1994 to 2009."),
    dict(id="F3", group="FOR", aspect=1.40, focus=(0.5, 0.5),
         title="A Tour of the Monuments of Passaic, New Jersey", author="Robert Smithson",
         year="1967",
         image="Pipes discharging into the Passaic River (The Fountain Monument).",
         info=["Photo essay published in Artforum, December 1967",
               "Instamatic photographs of a bridge, pumping derrick and outfall pipes",
               "Introduces \"ruins in reverse\": structures that rise into ruin"],
         caption="Infrastructure read as monument; entropy and sediment as cultural subject.",
         project="Gives permission to read a debris basin or outfall as a monument rather than "
                 "an eyesore. Smithson treats entropy as the real subject of the landscape, "
                 "which is the condition of a watershed that fills with sediment every winter."),
    dict(id="F4", group="FOR / MATERIAL", aspect=0.72, focus=(0.5, 0.5),
         title="Lake varve core", author="Annual sediment layers", year="",
         image="Tight crop of a banded sediment core.",
         info=["A varve is one year of lake sediment: a light summer silt and a dark winter clay",
               "Counted like tree rings to date climate and flood events",
               "Method from Gerard De Geer's Swedish clay varve chronology (1912)"],
         caption="Sediment as a time record. Source for a facade that archives each year's "
                 "sediment.",
         project="The model for the facade. If each year's sediment is printed into that year's "
                 "tiles, the elevation becomes a core sample of the Arroyo: fire years, wet "
                 "years and lapses in maintenance all read as bands. Paired at equal scale with "
                 "M3 on the pile-up."),
    dict(id="M1", group="MATERIAL", aspect=1.30, focus=(0.5, 0.5),
         title="Ricola Kräuterzentrum", author="Herzog & de Meuron with Martin Rauch",
         year="2014",
         image="Close-up of the rammed earth wall strata.",
         info=["Herb processing center, Laufen, Switzerland",
               "Prefabricated rammed earth blocks made from regional excavated earth",
               "Strata and erosion left visible as the finish"],
         caption="Excavated earth refined into construction that shows its own making.",
         project="Step one of the material sequence: excavated earth, normally hauled away as "
                 "waste, becomes a wall. The banding is a record of how it was made, which is "
                 "the quality the sediment tiles should keep."),
    dict(id="M2", group="MATERIAL", aspect=1.33, focus=(0.5, 0.5),
         title="Mud Frontiers", author="Rael San Fratello / Emerging Objects", year="2019 to 2020",
         image="Printer extruding local soil in the field.",
         info=["3D printed adobe structures in the San Luis Valley and the U.S.-Mexico borderlands",
               "Portable clay printer fed with soil dug on site",
               "Links printing to traditional adobe craft"],
         caption="Site earth printed directly into form. Proof that local soil can be printed.",
         project="Step two: shows that raw local earth can go straight into a printer without an "
                 "industrial clay body. The test the node's lab would run on Arroyo sediment "
                 "each year before it is printed."),
    dict(id="M3", group="MATERIAL", aspect=0.72, focus=(0.5, 0.5),
         title="Ceramic House", author="Studio RAP", year="2023",
         image="Raking-light close-up of printed tile relief (not the full elevation).",
         info=["Shopfront facade, Amsterdam",
               "Thousands of individually 3D printed, glazed ceramic tiles",
               "Each tile computed and printed as a unique piece"],
         caption="Uniquely 3D printed ceramic facade. Direct precedent for a sediment tile facade.",
         project="Step three and the direct precedent. Proves a facade of unique printed tiles "
                 "is buildable today. The position adds what Studio RAP does not: the clay "
                 "comes from the watershed, and its variation is data, not ornament."),
    dict(id="C1", group="AGAINST", aspect=1.50, focus=(0.5, 0.5),
         title="Manifesto of the Third Landscape", author="Gilles Clément", year="2004",
         image="Overgrown abandoned lot.",
         info=["Manifeste du Tiers paysage, Paris, 2004",
               "The third landscape: abandoned and unmanaged ground",
               "Argues these spaces are refuges for biodiversity"],
         caption="Value in unmanaged land. The position the thesis argues against.",
         project="The strongest counter-position. Clément would say leave the basin alone and "
                 "let it go wild. In the Arroyo Seco, abandonment does not produce wilderness; "
                 "it produces a full reservoir and a debris flow. Placed at the bottom edge, "
                 "partly buried."),
    dict(id="C2", group="AGAINST", aspect=1.45, focus=(0.5, 0.5),
         title="Earthships", author="Michael Reynolds", year="1970s onward",
         image="Earthship exterior in the desert.",
         info=["Greater World community, Taos, New Mexico",
               "Tire and earth walls, rainwater catchment, on-site greywater and power",
               "Designed to operate fully off the grid"],
         caption="Total self-sufficiency per building, zero civic life. The isolation risk of "
                 "\"every building maintains its own water.\"",
         project="Mayne's prompt taken to the limit. Each house looks after itself and owes "
                 "nothing to anyone else, so maintenance never becomes a shared or public act. "
                 "The position keeps the self-reliance and rejects the isolation."),
    dict(id="C3", group="AGAINST / MAYNE", aspect=0.80, focus=(0.5, 0.5),
         title="Bullitt Center", author="Miller Hull Partnership", year="2013",
         image="Building exterior or its rainwater system (alt: Roman impluvium).",
         info=["Seattle; certified under the Living Building Challenge",
               "Roof rainwater stored in a basement cistern and treated for use on site",
               "Composting toilets; greywater treated on the building"],
         caption="A building that handles its own water on site. The strongest case for Mayne's "
                 "distributed model, and its limit: the work stays private.",
         project="Where the synthesis comes from. The building handles its own rain well, but "
                 "the cistern is in the basement and the work is invisible. It cannot take on "
                 "sediment, debris or a watershed. That is the job of the public node."),
]

# Pile-up placement. Listed bottom to top (later entries sit on top).
#   x, y : centre of the frame (in)    w : frame width (in); height comes from aspect
#   rot  : degrees, positive = counter-clockwise
#   muted: 0..1, how far the image is washed toward white (BASE only)
PILEUP = [
    dict(id="BASE", x=5.50, y=4.20, w=11.4, rot=-0.6, muted=0.55, border=False),
    dict(id="F3",   x=2.45, y=4.95, w=4.30, rot=-2.0),
    dict(id="C3",   x=9.55, y=4.55, w=2.20, rot=2.5),
    dict(id="C2",   x=8.80, y=1.80, w=3.20, rot=-1.5),
    dict(id="F2",   x=1.55, y=1.25, w=2.90, rot=2.5),
    dict(id="C1",   x=8.05, y=7.75, w=3.70, rot=1.0),   # bleeds off the bottom edge
    dict(id="F4",   x=2.80, y=2.55, w=1.30, rot=-1.0),  # paired with M3 at matching scale
    dict(id="M3",   x=4.20, y=2.55, w=1.30, rot=1.0),
    dict(id="M1",   x=6.95, y=6.25, w=2.30, rot=-2.5),
    dict(id="M2",   x=5.60, y=4.35, w=2.40, rot=1.5),
    dict(id="F1",   x=4.45, y=5.75, w=2.40, rot=-3.5),  # on top, over the material sequence
]
