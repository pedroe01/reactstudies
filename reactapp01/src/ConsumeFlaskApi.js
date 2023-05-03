import React, { useState, useEffect } from 'react';

export default function FlaskApi(){

    const [msg, setMsg] = useState();

    const getApiData = async () => {
        const response = await fetch(
          "http://localhost:5000/flaskapi"
        ).then((response) => response.json());

        setMsg(response);
        };

        useEffect(() => {
            getApiData();
        }, []);
        return (
            <div className="app">
                {msg && msg.map(msg => (
                    <div className="item-container">
                        <p>Aluno: {msg.aluno}</p>
                        <p>Turma: {msg.turma}</p>
                        <p>RA: {msg.ra}</p>
                        <p>Disciplina: {msg.disciplina}</p>
                        <p>Atividade: {msg.atividade}</p>
                        </div>
                ))}
            </div>);
}
