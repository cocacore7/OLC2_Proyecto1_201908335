import React from 'react';
import axios from 'axios'
import NavBar from "../Componentes/NavBar"
import "../css/Analisis.css"
import Editor from "@monaco-editor/react";
import { Button } from 'semantic-ui-react'

function Analisis() {

    const EnviarCodigo = async()=> {
        let Contenido = {
            Texto: "console.log(\"Hola\" == \"aloH\");console.log(\"a\" == \"a\");console.log(3 < 5);console.log(7*5+1);console.log(\"El CACAS\");"
        }
        let contenido = await axios.post("http://localhost:4000/Analizador",Contenido)
        console.log(contenido.data)
    }

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
                <h1>Entrada <Button floated='right' color='blue' onClick={EnviarCodigo}>Compilar</Button></h1>
                <Editor
                    height="85vh"
                    defaultLanguage="Python"
                    defaultValue="// Entrada"
                    theme="vs-dark"
                />
            </div>

            <div className="Salida">
                <h1>Salida</h1>
                <Editor
                    height="85vh"
                    defaultLanguage="Python"
                    defaultValue="// Salida"
                    theme="vs-dark"
                />
            </div>
            
        </div>
        </>
    )
}

export default Analisis
