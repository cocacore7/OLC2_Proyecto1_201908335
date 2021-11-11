Errores = []
Simbolos = []
Mirrila = []
Bloques = []


def GraficaError(err):
    contador = 1
    grafo = "digraph G { bgcolor=\"yellow:red\"\n"
    grafo += "node [shape=filled];\n"
    grafo += "a0 [label=<\n"
    grafo += "<TABLE border=\"10\" cellspacing=\"10\" cellpadding=\"10\" style=\"rounded\" bgcolor=\"/rdylgn11/1:/rdylgn11/11\" gradientangle=\"315\">\n"
    grafo += "<TR>\n"
    grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">"+"NO."+"</TD>\n"
    grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">"+"DESCRIPCION"+"</TD>\n"
    grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">"+"LINEA"+"</TD>\n"
    grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">"+"COLUMNA"+"</TD>\n"
    grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">"+"FECHA Y HORA"+"</TD>\n"
    grafo += "</TR>\n"
    for i in err:
        grafo += "<TR>\n"
        grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">" + str(contador)+"</TD>\n"
        contador += 1
        grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">" + i["Descripcion"] + "</TD>\n"
        grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">" + i["Linea"] + "</TD>\n"
        grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">" + i["Columna"] + "</TD>\n"
        grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">" + i["Fecha"] + "</TD>\n"
        grafo += "</TR>\n"
    grafo += "</TABLE>>];\n"
    grafo += "}\n"
    return grafo


def GraficaTS(simb):
    grafo = "digraph G { bgcolor=\"yellow:red\"\n"
    grafo += "node [shape=filled];\n"
    grafo += "a0 [label=<\n"
    grafo += "<TABLE border=\"10\" cellspacing=\"10\" cellpadding=\"10\" style=\"rounded\" bgcolor=\"/rdylgn11/1:/rdylgn11/11\" gradientangle=\"315\">\n"
    grafo += "<TR>\n"
    grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">"+"NOMBRE"+"</TD>\n"
    grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">"+"TIPO"+"</TD>\n"
    grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">"+"AMBITO"+"</TD>\n"
    grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">"+"LINEA"+"</TD>\n"
    grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">"+"COLUMNA"+"</TD>\n"
    grafo += "</TR>\n"
    for i in simb:
        grafo += "<TR>\n"
        grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">" + i["Nombre"] + "</TD>\n"
        grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">" + i["Tipo"] + "</TD>\n"
        grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">" + i["Ambito"] + "</TD>\n"
        grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">" + i["Linea"] + "</TD>\n"
        grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">" + i["Columna"] + "</TD>\n"
        grafo += "</TR>\n"
    grafo += "</TABLE>>];\n"
    grafo += "}\n"
    return grafo


def GraficaTO(simb):
    grafo = "digraph G { bgcolor=\"yellow:red\"\n"
    grafo += "node [shape=filled];\n"
    grafo += "a0 [label=<\n"
    grafo += "<TABLE border=\"10\" cellspacing=\"10\" cellpadding=\"10\" style=\"rounded\" bgcolor=\"/rdylgn11/1:/rdylgn11/11\" gradientangle=\"315\">\n"
    grafo += "<TR>\n"
    grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">"+"TIPO DE OPTIMIZACION"+"</TD>\n"
    grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">"+"REGLA APLICADA"+"</TD>\n"
    grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">"+"EXP ORIGINAL"+"</TD>\n"
    grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">"+"EXP OPTIMIZADA"+"</TD>\n"
    grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">"+"FILA"+"</TD>\n"
    grafo += "</TR>\n"
    for i in simb:
        grafo += "<TR>\n"
        grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">" + i["Tipo"] + "</TD>\n"
        grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">" + i["Regla"] + "</TD>\n"
        grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">" + i["ExpOr"] + "</TD>\n"
        grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">" + i["ExpOp"] + "</TD>\n"
        grafo += "<TD border=\"3\"  bgcolor=\"/rdylgn11/1:/rdylgn11/2\">" + i["Fila"] + "</TD>\n"
        grafo += "</TR>\n"
    grafo += "</TABLE>>];\n"
    grafo += "}\n"
    return grafo
