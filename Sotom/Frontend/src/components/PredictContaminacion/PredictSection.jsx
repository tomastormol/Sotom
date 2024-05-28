import React from 'react';

function PredictSection({ fecha, handleFechaChange, handlePredictClick }) {
    return (
        <div className="p-6 flex flex-row w-full justify-around items-center bg-white shadow-md rounded-lg">
            <div className="flex space-x-4 items-center">
                <label htmlFor="fecha" className="block text-gray-700 font-bold">Fecha:</label>
                <input
                    type="date"
                    id="fecha"
                    value={fecha}
                    onChange={handleFechaChange}
                    className="px-3 py-2 rounded-md focus:outline-none focus:border-blue-500"
                />
            </div>
            <button
                onClick={handlePredictClick}
                className="bg-blue-500 text-white font-bold py-2 px-4 rounded-full focus:outline-none focus:shadow-outline hover:bg-blue-600 transition duration-300 self-start"
            >
                Predecir
            </button>
        </div>
    );
}

export default PredictSection;
