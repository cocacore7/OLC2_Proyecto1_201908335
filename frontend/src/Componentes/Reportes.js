import React,{useEffect,useState} from 'react'
import NavBar from "../Componentes/NavBar"
import "../css/Reportes.css"
import { Graphviz } from 'graphviz-react';
import { Table } from 'semantic-ui-react'
import { Button } from 'semantic-ui-react'

function Reportes() {
    const [filas, setfilas] = useState([])

    const Cargar = async()=> {
        let Fil = JSON.parse(localStorage.getItem('TO'))
        if (Fil!=null){
            setfilas(Fil)
        }
    }

    if (filas["Filas"] == undefined){
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
                        <Button floated='right' color='green' onClick={Cargar}>Cargar Datos</Button>
                        <div className="item">
                            <Table celled>
                                <Table.Header>
                                    <Table.Row>
                                    <Table.HeaderCell>TIPO DE OPTIMIZACION</Table.HeaderCell>
                                    <Table.HeaderCell>REGLA APLICADA</Table.HeaderCell>
                                    <Table.HeaderCell>EXP ORIGINAL</Table.HeaderCell>
                                    <Table.HeaderCell>EXP OPTIMIZADA</Table.HeaderCell>
                                    <Table.HeaderCell>FILA</Table.HeaderCell>
                                    </Table.Row>
                                </Table.Header>
                                <Table.Body>
                                </Table.Body>
                            </Table>
                        </div>
                        <div className="ui inverted divider" />

                        <div className="item">
                            <div className="ui big segment rounded image">
                                <Graphviz 
                                    dot={localStorage.getItem('Dot')}
                                    options={{zoom:true,height: 2000,width: 2000}} 
                                />
                            </div>
                            <div className="content">
                            <h1 style={{color: '#00FFFF'}}>Arbol Sintactico</h1>
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
    }else{
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
                        <Button floated='right' color='green' onClick={Cargar}>Cargar Datos</Button>
                        <div className="item">
                            <Table celled>
                                <Table.Header>
                                    <Table.Row>
                                    <Table.HeaderCell>TIPO DE OPTIMIZACION</Table.HeaderCell>
                                    <Table.HeaderCell>REGLA APLICADA</Table.HeaderCell>
                                    <Table.HeaderCell>EXP ORIGINAL</Table.HeaderCell>
                                    <Table.HeaderCell>EXP OPTIMIZADA</Table.HeaderCell>
                                    <Table.HeaderCell>FILA</Table.HeaderCell>
                                    </Table.Row>
                                </Table.Header>
                                <Table.Body>
                                    {filas["Filas"].map((row, index) => (
                                        <Table.Row key={index}>
                                            <Table.Cell>{row.Tipo}</Table.Cell>
                                            <Table.Cell>{row.Regla}</Table.Cell>
                                            <Table.Cell>{row.ExpOr}</Table.Cell>
                                            <Table.Cell>{row.ExpOp}</Table.Cell>
                                            <Table.Cell>{row.Fila}</Table.Cell>
                                        </Table.Row>
                                    ))}
                                </Table.Body>
                            </Table>
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
}

export default Reportes
