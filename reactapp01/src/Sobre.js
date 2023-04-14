import React from "react";
import { Link, useLocation } from 'react-router-dom'

export default function Sobre (){
    const location = useLocation();
    return (
        <div>
            <h1>Path: {location.pathname}</h1>
            <Link to="/">retornar a página inicial</Link>
        </div>
    );
}