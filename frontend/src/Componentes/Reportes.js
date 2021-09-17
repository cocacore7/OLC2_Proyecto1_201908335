import React from 'react'
import NavBar from "../Componentes/NavBar"
import "../css/Reportes.css"
import { Graphviz } from 'graphviz-react';

function Reportes() {

    return (
        <>
            <NavBar 
                colores={["red","green","yellow"]}
                opciones={["Inicio","Analisis","Reportes"]}
                url={["/Inicio","/Analisis","/Reportes"]}
                activo={"yellow"}
            />
            <div className="Reportes">
                <br/>

                <div className="ui inverted segment container items">
                    <div className="item">
                        <div className="ui big segment rounded image">
                            <Graphviz 
                                dot={localStorage.getItem('Dot')}
                                options={{zoom:true,height: 2000,width: 2000}} 
                            />
                        </div>
                        <div className="content">
                        <h1 style={{color: '#00FFFF'}}>Arbol De Analisis Sintactico</h1>
                        </div>
                    </div>
                    <div className="ui inverted divider" />

                    <div className="item">
                        <div className="ui big segment rounded image">
                            <Graphviz 
                                dot={localStorage.getItem('TS')}
                                options={{zoom:true,height: 2000,width: 2000}} 
                            />
                        </div>
                        <div className="content">
                        <h1 style={{color: '#00FFFF'}}>Tabla De Simbolos</h1>
                        </div>
                    </div>
                    <div className="ui inverted divider" />

                    <div className="item">
                        <div className="ui big segment rounded image">
                            <Graphviz 
                                dot={localStorage.getItem('TE')}
                                options={{zoom:true,height: 2000,width: 2000}} 
                            />
                        </div>
                        <div className="content">
                        <h1 style={{color: '#00FFFF'}}>Tabla De Errores</h1>
                        </div>
                    </div>
                </div>

                <br/>
            </div>
        </>
    )
}

export default Reportes
