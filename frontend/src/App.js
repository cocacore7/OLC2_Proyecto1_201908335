import React from 'react'
import { BrowserRouter as Router,Redirect,Route } from "react-router-dom";
import Inicio from "./Componentes/Inicio"
import Analisis from "./Componentes/Analisis"
import Reportes from "./Componentes/Reportes"

function App() {
  return (
    <Router>
      <Route exact path="/">
        <Redirect to="/Inicio"/>
      </Route>
      <Route path="/Inicio" component={Inicio} />
      <Route path="/Analisis" component={Analisis} />
      <Route path="/Reportes" component={Reportes} />
    </Router>
  )
}

export default App