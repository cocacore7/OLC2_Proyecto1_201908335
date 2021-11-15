import React,{useState, useRef} from 'react'
import axios from 'axios'
import NavBar from "../Componentes/NavBar"
import "../css/Analisis.css"
import Editor from "@monaco-editor/react";
import { Button } from 'semantic-ui-react'

function Analisis() {
    const [salidai,setsalidai] = useState("// Salida Interpretada")
    const [salidac,setsalidac] = useState("// Salida Compilada")
    const [salidam,setsalidam] = useState("// Optimizacion Mirilla")

    function handleEditorChange(value, event) {
        localStorage.setItem('CA',value);
    }

    const EnviarCodigoI = async()=> {
        let Contenido = {
            Texto: localStorage.getItem('CA')
        }
        let contenido = await axios.post("http://localhost:4200/Analizador",Contenido)
        localStorage.setItem('Dot',contenido.data["Dot"])
        localStorage.setItem('TS',contenido.data["TS"])
        localStorage.setItem('TE',contenido.data["TE"])
        setsalidai(contenido.data["Salida"])
    }

    const EnviarCodigoC = async()=> {
        let Contenido = {
            Texto: localStorage.getItem('CA')
        }
        let contenido = await axios.post("http://localhost:4000/Compilador",Contenido)
        localStorage.setItem('TO',contenido.data["TO"])
        localStorage.setItem('TS',contenido.data["TS"])
        localStorage.setItem('TE',contenido.data["TE"])
        setsalidac(contenido.data["Salida"])
    }

    const EnviarCodigoM = async()=> {
        let Contenido = {
            Texto: localStorage.getItem('CA')
        }
        let contenido = await axios.post("http://localhost:4000/OptimizadorMirilla",Contenido)
        localStorage.setItem('TO', JSON.stringify(contenido.data["TO"]))
        console.log(localStorage.getItem('TO'))
        setsalidam(contenido.data["Salida"])
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
                <h1>Entrada Analizador
                    <Button floated='right' color='green' onClick={EnviarCodigoI}>Interpretar</Button>
                    <Button floated='right' color='blue' onClick={EnviarCodigoC}>Compilar</Button>
                </h1>
                <Editor
                    height="85vh"
                    defaultLanguage="julia"
                    defaultValue="// Entrada"
                    path="Consola1"
                    theme="vs-dark"
                    onChange={handleEditorChange}
                />
            </div>            
            
            <div className="salidai">
                <h1>Salida Interpretada</h1>
                <Editor
                    height="85vh"
                    defaultLanguage="julia"
                    defaultValue="// Optimizacion Bloques"
                    path="Consola4"
                    value={salidai}
                    theme="vs-dark"
                />
            </div>

            <div className="salidac">
                <h1>Salida Compilada
                    <Button floated='right' color='green' onClick={EnviarCodigoM}>Optimizar Mirilla</Button>
                </h1>
                <Editor
                    height="85vh"
                    defaultLanguage="go"
                    path="Consola2"
                    theme="vs-dark"
                    value={salidac}
                    onChange={handleEditorChange}
                />
            </div>
            
            <div className="SalidaM">
                <h1>Optimizacion Mirilla</h1>
                <Editor
                    height="85vh"
                    defaultLanguage="go"
                    defaultValue="// Optimizacion Mirilla"
                    path="Consola3"
                    value={salidam}
                    theme="vs-dark"
                />
            </div>
        </div>
        </>
    )
}

export default Analisis
