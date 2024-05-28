import React from 'react';

function ResultSection({ fecha }) {

    const formatearFecha = (fecha) => {
        const opciones = { day: '2-digit', month: '2-digit', year: 'numeric' };
        const fechaObj = new Date(fecha);
        return fechaObj.toLocaleDateString('es-ES', opciones);
    };

    return (
        <div className="bg-white w-full p-6 shadow-md rounded-lg">
            {/* Contenido del componente de resultados */}
            <h2 className="text-xl font-semibold text-gray-800 mb-4">Resultados de la predicción</h2>
            <p className="text-gray-700">El día {formatearFecha(fecha)} habrá una contaminación de 'x'</p>
        </div>
    );
}

export default ResultSection;
