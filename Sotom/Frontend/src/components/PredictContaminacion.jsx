import React, { useState } from 'react';
import PredictSection from './PredictContaminacion/PredictSection';
import ResultSection from './PredictContaminacion/ResultSection';
import ImageSection from './PredictContaminacion/ImageSection';
import imagedaynext from '../assets/daynext.png';
import imagetwodaysnext from '../assets/twodaysnext.png';

function PredictContaminacion() {
    const [fecha, setFecha] = useState('');
    const [imagen, setImagen] = useState(null);
    const [mostrarResultados, setMostrarResultados] = useState(false);

    const handleFechaChange = (e) => {
        setFecha(e.target.value);
        setMostrarResultados(false); // Ocultar los resultados cuando se cambia la fecha
    };

    const handlePredictClick = () => {
        if (fecha) {
            const fechaSeleccionada = new Date(fecha);
            const hoy = new Date();
            const diferenciaDias = Math.floor((fechaSeleccionada - hoy) / (1000 * 60 * 60 * 24));

            if (diferenciaDias === 0) {
                setImagen(imagedaynext);
            } else if (diferenciaDias === 1) {
                setImagen(imagetwodaysnext);
            } else {
                setImagen(null);
            }

            setMostrarResultados(true); // Mostrar los resultados después de hacer clic en predecir
        }
    };

    return (
        <div className="flex flex-1 h-screen flex-col items-center gap-2 p-10 bg-gray-100">
            <PredictSection
                fecha={fecha}
                handleFechaChange={handleFechaChange}
                handlePredictClick={handlePredictClick}
            />
            {mostrarResultados && (
                <>
                    <ResultSection fecha={fecha} />
                    <ImageSection imagen={imagen} />
                </>
            )}
        </div>
    );
}

export default PredictContaminacion;
