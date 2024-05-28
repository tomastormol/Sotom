import React from 'react';

export const PowerBI = () => {
    return (
        <div style={{ width: '100%', height: '100vh', display: 'flex', justifyContent: 'center', alignItems: 'center' }} id='test'>
            <iframe
                src="/test.html"
                style={{ width: '100%', height: '100vh', border: 'none' }}
                title="Power BI"
            />
        </div>
    );
};
