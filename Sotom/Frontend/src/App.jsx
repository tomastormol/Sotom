import React, { useState } from 'react';
import Chat from './components/Chat';
import Menu from './components/Menu';
import PredictContaminacion from './components/PredictContaminacion';
import { PowerBI } from './components/PowerBI';
import { Yolo } from './components/Yolo';

function App() {
  const [opcionSeleccionada, setOpcionSeleccionada] = useState(null);

  const handleOptionClick = (opcion) => {
    setOpcionSeleccionada(opcion);
  };

  return (
    <div className="flex flex-col md:flex-row h-screen">
      {/* Sidebar */}
      <Menu handleOptionClick={handleOptionClick} />
      {/* Main Section */}
      <div className="flex-1 flex justify-center">
        {opcionSeleccionada === 'Predict de contaminacio' ? (
          <PredictContaminacion />
        ) : opcionSeleccionada === 'Power BI' ? (
          <PowerBI />
        ) : opcionSeleccionada === 'Yolo' ? (
          <Yolo />
        ) : (
          <Chat />
        )}
      </div>
    </div>
  );
}

export default App;
