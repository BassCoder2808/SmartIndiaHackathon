import what3words

geocoder = what3words.Geocoder("C0044PN1")

# Convert to 3 words
res = geocoder.convert_to_3wa(what3words.Coordinates(19.210159, 72.836128))
print(res)

# convert to coordinates
# res = geocoder.convert_to_coordinates('prom.cape.pump')
# print(res)

# # grid section
# sw = what3words.Coordinates(52.207988,0.116126)
# ne = what3words.Coordinates(52.208867,0.117540)
# bb = what3words.BoundingBox(sw, ne)

# res = geocoder.grid_section(bb)
# print(res)