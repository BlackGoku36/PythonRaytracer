def write_color(file, color):
    file.write("{0:d} {1:d} {2:d}\n".format(
        int(color.x*255), int(color.y*255), int(color.z*255)
    ))
