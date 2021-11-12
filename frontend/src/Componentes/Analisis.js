import React,{useState, useRef} from 'react'
import axios from 'axios'
import NavBar from "../Componentes/NavBar"
import "../css/Analisis.css"
import Editor from "@monaco-editor/react";
import { Button } from 'semantic-ui-react'

function Analisis() {
    const editorRef = useRef(null)
    const [texto,settexto] = useState("")
    const [salida,setsalida] = useState("// Salida")
    const [salidam,setsalidam] = useState("// Optimizacion Mirilla")
    const [salidab,setsalidab] = useState("// Optimizacion Bloques")

    function handleEditorChange(value, event) {
        localStorage.setItem('CA',value);
      }

    const EnviarCodigo = async()=> {
        let Contenido = {
            Texto: localStorage.getItem('CA')
        }
        //let contenido = await axios.post("https://backcompi.herokuapp.com/Compilador",Contenido)
        let contenido = await axios.post("http://localhost:4000/Compilador",Contenido)
        localStorage.setItem('TO',contenido.data["TO"])
        localStorage.setItem('TS',contenido.data["TS"])
        localStorage.setItem('TE',contenido.data["TE"])
        setsalida(contenido.data["Salida"])
    }

    const EnviarCodigoM = async()=> {
        let Contenido = {
            Texto: localStorage.getItem('CA')
        }
        //let contenido = await axios.post("https://backcompi.herokuapp.com/OptimizadorMirilla",Contenido)
        let contenido = await axios.post("http://localhost:4000/OptimizadorMirilla",Contenido)
        localStorage.setItem('TO',contenido.data["TO"])
        setsalidam(contenido.data["Salida"])
    }

    const EnviarCodigoB = async()=> {
        let Contenido = {
            Texto: localStorage.getItem('CA')
        }
        //let contenido = await axios.post("https://backcompi.herokuapp.com/OptimizadorBloques",Contenido)
        let contenido = await axios.post("http://localhost:4000/OptimizadorBloques",Contenido)
        localStorage.setItem('TE',contenido.data["TE"])
        setsalidab(contenido.data["Salida"])
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
                    defaultLanguage="julia"
                    defaultValue="// Entrada"
                    path="Consola1"
                    theme="vs-dark"
                    onChange={handleEditorChange}
                />
            </div>

            <div className="Salida">
                <h1>Salida 
                    <Button floated='right' color='green' onClick={EnviarCodigoM}>Optimizar Mirilla</Button>
                    <Button floated='right' color='red'   onClick={EnviarCodigoB}>Optimizar Bloques</Button>
                </h1>
                <Editor
                    height="85vh"
                    defaultLanguage="go"
                    path="Consola2"
                    theme="vs-dark"
                    value={salida}
                    onChange={handleEditorChange}
                />
            </div>
            <br/>
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
            
            <div className="SalidaB">
                <h1>Optimizacion Bloques</h1>
                <Editor
                    height="85vh"
                    defaultLanguage="go"
                    defaultValue="// Optimizacion Bloques"
                    path="Consola4"
                    value={salidab}
                    theme="vs-dark"
                />
            </div>
        </div>
        </>
    )
}

export default Analisis
