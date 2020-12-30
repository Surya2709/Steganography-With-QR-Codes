def extract_shapekey(c):
    d=c.split(",")
    e=d[0]
    f=d[1]
    g=e.split("(")
    h=f.split(")")
    part_1=g[1]
    part_2=h[0]
    shapekey=(int(part_1),int(part_2))
    return shapekey