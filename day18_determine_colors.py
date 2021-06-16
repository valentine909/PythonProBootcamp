import colorgram
SPECTRA = [(237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103),
           (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177)]


def extract_colors(number_of_colors):
    return colorgram.extract('day18_image.jpg', number_of_colors)


if __name__ == '__main__':
    hirst_colors = extract_colors(30)
    spectra = []
    for color in hirst_colors:
        if 0.005 < color.proportion < 0.5:
            spectra.append((color.rgb.r, color.rgb.g, color.rgb.b))
    print(spectra)
