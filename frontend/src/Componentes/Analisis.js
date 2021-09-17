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

    function handleEditorDidMount(editor, monaco){
        editorRef.current = editor;
    }

    const EnviarCodigo = async()=> {
        settexto(editorRef.current.getValue());
        let Contenido = {
            Texto: texto
        }
        //let contenido = await axios.post("https://backcompi.herokuapp.com/Analizador",Contenido)
        let contenido = await axios.post("http://localhost:4000/Analizador",Contenido)
        localStorage.setItem('Dot',contenido.data["Dot"])
        setsalida(contenido.data["Salida"])
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
                    onMount={handleEditorDidMount}
                />
            </div>

            <div className="Salida">
                <h1>Salida</h1>
                <Editor
                    height="85vh"
                    defaultLanguage="julia"
                    path="Consola2"
                    theme="vs-dark"
                    value={salida}
                />
            </div>
        </div>
        </>
    )
}

export default Analisis
