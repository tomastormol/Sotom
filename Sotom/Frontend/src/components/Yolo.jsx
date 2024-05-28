import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Skeleton from './Skeleton';

export const Yolo = () => {
    const [images, setImages] = useState([]);
    const [totalCarsDetected, setTotalCarsDetected] = useState(0);
    const [imagesLoaded, setImagesLoaded] = useState(false);

    useEffect(() => {
        const fetchImages = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/images`);
                setImages(response.data.images);
                setTotalCarsDetected(response.data.total_cars_detected);
                setImagesLoaded(true);
            } catch (error) {
                console.error('Error fetching images:', error);
            }
        };

        fetchImages();
    }, []);

    const imagePath = 'http://127.0.0.1:8000/images/';

    if (!imagesLoaded) {
        return (
            <div className="p-4 flex-1 overflow-scroll">
                <Skeleton />
            </div>
        );
    }

    const getEmissionMessage = () => {
        if (totalCarsDetected < 20) {
            return { message: 'baja', className: 'text-green-500' };
        } else if (totalCarsDetected <= 40) {
            return { message: 'moderada', className: 'text-orange-500' };
        } else if (totalCarsDetected <= 60) {
            return { message: 'alta', className: 'text-red-500' };
        } else {
            return { message: 'muy alta', className: 'text-purple-700 font-bold' };
        }
    };

    const emissionData = getEmissionMessage();

    return (
        <div className="p-4 flex-1 overflow-scroll">
            <h1 className="text-2xl font-bold mb-4">Datos de Contaminación</h1>
            <h2 className="text-xl mb-4">Total de coches detectados: {totalCarsDetected}</h2>
            <h3 className="text-lg mb-4">
                La emisión de los contaminantes es{' '}
                <span className={emissionData.className}>{emissionData.message}</span>
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 gap-4">
                {images.map((image, index) => (
                    <div key={index} className="rounded-lg overflow-hidden shadow-lg">
                        <img
                            src={`${imagePath}${image}`}
                            alt={`Image ${index + 1}`}
                            className="w-full h-80"
                        />
                    </div>
                ))}
            </div>
        </div>
    );
};
