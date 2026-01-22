
import React from 'react';
import { useRive, Layout, Fit, Alignment } from '@rive-app/react-canvas';

const RiveLoginAnimation = () => {
    const { RiveComponent } = useRive({
        src: '/22487-42095-look.riv',
        stateMachines: "State Machine 1", // Common default name, can be adjusted
        autoplay: true,
        layout: new Layout({
            fit: Fit.Contain,
            alignment: Alignment.Center,
        }),
    });

    return (
        <div className="w-full h-full flex items-center justify-center">
            <div
                className="w-full h-full"
                style={{
                    maskImage: 'radial-gradient(circle, white 30%, transparent 80%)',
                    WebkitMaskImage: 'radial-gradient(circle, white 30%, transparent 80%)'
                }}
            >
                <RiveComponent className="w-full h-full" />
            </div>
        </div>
    );
};

export default RiveLoginAnimation;
