import React from 'react';

const ImageSection = ({ imagen }) => {
    if (!imagen) return null;
    return (
        <div className="w-full overflow-scroll rounded-2xl">
            <img
                src={imagen}
                alt="Imagen"
                className="w-full"
            />
        </div>
    );
}

export default ImageSection;
