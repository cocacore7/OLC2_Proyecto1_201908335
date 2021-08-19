import React from 'react'
import NavBar from "../Componentes/NavBar"
import "../css/Analisis.css"
import Editor, { DiffEditor, useMonaco, loader } from "@monaco-editor/react";
import { Button } from 'semantic-ui-react'

function Analisis() {
    return (
        <>
        <NavBar 
            colores={["red","green","yellow"]}
            opciones={["Inicio","Analisis","Reportes"]}
            url={["/Inicio","/Analisis","/Reportes"]}
            activo={"green"}
        />
        <div className="Analisis">
            <div className="Entrada">
                <h1>Entrada <Button floated='right' color='blue'>Compilar</Button></h1>
                <Editor
                    height="85vh"
                    defaultLanguage="javascript"
                    defaultValue="// some comment"
                    theme="vs-dark"
                />
            </div>

            <div className="Salida">
                <h1>Salida</h1>
                <Editor
                    height="85vh"
                    defaultLanguage="javascript"
                    defaultValue="// some comment"
                    theme="vs-dark"
                />
            </div>
            
        </div>
        </>
    )
}

export default Analisis
