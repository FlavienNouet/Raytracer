# Initialisation de la toile et des paramètres de la vue
O = (0, 0, 0)

pour x = -Cw/2 à Cw/2 {
    pour y = -Ch/2 à Ch/2 {
        D = CanvasToViewport(x, y)
        couleur = TraceRay(O, D, 1, inf)
        canvas.PutPixel(x, y, couleur)
    }
}

#Extension du raytracer => positionnement de la caméra
pour x dans [-Cw/2, Cw/2] {
    pour y dans [-Ch/2, Ch/2] {
       D = caméra.rotation * CanvasToViewport(x, y)
       couleur = TraceRay(caméra.position, D, 1, inf)
        canvas.PutPixel(x, y, couleur)
    }
}
