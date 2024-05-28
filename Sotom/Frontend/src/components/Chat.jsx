import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import TypingAnimation from './TypingAnimation';
import '../styles/Chat.css';

function Chat() {
    const [mensaje, setMensaje] = useState('');
    const [mensajesChat, setMensajesChat] = useState([]);
    const [botEscribiendo, setBotEscribiendo] = useState(false);
    const chatRef = useRef(null);

    const handleEnviarMensaje = async () => {
        if (mensaje.trim() !== '') {
            try {
                setMensajesChat(prevMensajes => [...prevMensajes, { usuario: 'Usuario', mensaje }]);
                setMensaje('');
                setBotEscribiendo(true);
                const response = await axios.get(`http://127.0.0.1:8000/predictGPT2?input_string=${mensaje}`);
                const respuestaBot = response.data.prediction;
                setMensajesChat(prevMensajes => [...prevMensajes, { usuario: 'Bot', mensaje: <TypingAnimation text={respuestaBot} delay={1} chatRef={chatRef} /> }]);
                setBotEscribiendo(false);
            } catch (error) {
                console.error('Error al obtener respuesta del bot:', error);
            }
        }
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            handleEnviarMensaje();
        }
    };

    useEffect(() => {
        const lastMessage = chatRef.current.lastElementChild;
        if (lastMessage) {
            lastMessage.scrollIntoView({ behavior: 'smooth' });
        }
    }, [mensajesChat]);

    return (
        <div className="flex justify-center items-center h-screen flex-1" style={{ backgroundColor: '#212121' }}>
            <div className="flex flex-col h-full w-full lg:w-1/2">
                <div className="flex-1 overflow-y-auto p-4" ref={chatRef}>
                    <div className="flex flex-col h-full">
                        {mensajesChat.map((msg, index) => (
                            <div key={index} className={`p-2 rounded-lg mb-4 text-gray-300`}>
                                <div className="flex">
                                    <div className={`bg-${msg.usuario === 'Usuario' ? 'blue' : 'green'}-500 rounded-full w-8 h-8 flex items-center justify-center text-white mr-2 min-w-8`}>
                                        {msg.usuario === 'Usuario' ? 'U' : 'B'}
                                    </div>
                                    <div>
                                        <p className="font-semibold">{msg.usuario}</p>
                                        <p className="break-words">{msg.mensaje}</p>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
                <div className="h-16 flex items-center justify-between p-4">
                    <div className="flex-1 relative">
                        <input
                            type="text"
                            placeholder="Escribe tu mensaje..."
                            className="px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:border-blue-500 w-full pr-20"
                            value={mensaje}
                            onChange={(e) => setMensaje(e.target.value)}
                            onKeyDown={handleKeyDown}
                        />
                        <button
                            onClick={handleEnviarMensaje}
                            className="absolute inset-y-0 right-0 px-4 py-2 bg-blue-500 text-white rounded-r-lg hover:bg-blue-600 focus:outline-none focus:bg-blue-600"
                        >
                            {botEscribiendo ? <i className="animate-spin material-icons">autorenew</i> : <i className="material-icons">send</i>}
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Chat;
