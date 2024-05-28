import React from 'react';

function Menu({ handleOptionClick }) {
    return (
        <div className="md:w-[260px] bg-[#171717] text-white">
            <div className="p-4">
                <h1 className="text-xl font-bold mb-4">Menú</h1>
                <ul>
                    <li className="mb-2"><a href="#" className={`text-blue-300 hover:text-blue-400`} onClick={() => handleOptionClick('Sotom Chat')}>Sotom Chat</a></li>
                    <li className="mb-2"><a href="#" className={`text-blue-300 hover:text-blue-400`} onClick={() => handleOptionClick('Predict de contaminacio')}>Predict de contaminacio</a></li>
                    <li className="mb-2"><a href="#" className={`text-blue-300 hover:text-blue-400`} onClick={() => handleOptionClick('Power BI')}>Power BI</a></li>
                    <li className="mb-2"><a href="#" className={`text-blue-300 hover:text-blue-400`} onClick={() => handleOptionClick('Yolo')}>Yolo</a></li>
                </ul>
            </div>
        </div>
    );
}

export default Menu;
