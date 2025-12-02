canvas.put_pixel(x, y, color)  #Base du projet = La toile blanche sur laquelle on dessine.


CanvasToViewport(x, y) {      # Conversion de 2D vers 3D
    retourner (x * Vw / Cw, y * Vh / Ch, d)
}