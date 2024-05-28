import React from 'react';

const Skeleton = () => {
    const skeletonLines = (
        <div className="animate-pulse flex space-x-4 mb-4">
            <div className="flex-1 space-y-4 py-1">
                <div className="h-6 bg-gray-400 rounded w-2/6"></div>
                <div className="h-4 bg-gray-300 rounded w-2/6"></div>
                <div className="h-4 bg-gray-300 rounded w-2/6"></div>
            </div>
        </div>
    );

    const skeletonImages = (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 gap-4">
            {Array.from({ length: 9 }).map((_, index) => (
                <div key={index} className="animate-pulse rounded-lg overflow-hidden shadow-lg">
                    <div className="w-full h-80 bg-gray-300"></div>
                </div>
            ))}
        </div>
    );

    return (
        <div className="p-4 flex-1 overflow-scroll">
            {skeletonLines}
            {skeletonImages}
        </div>
    );
};

export default Skeleton;
