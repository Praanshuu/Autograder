
import React from 'react';
import { useRive, useStateMachineInput, Layout, Fit, Alignment } from '@rive-app/react-canvas';

const RiveLoginAnimation = () => {
    // We need the canvas ref to dispatch events to it manually
    const { rive, RiveComponent, canvas: canvasRef } = useRive({
        src: '/22487-42095-look.riv',
        stateMachines: "State Machine 1", // Common default name, can be adjusted
        autoplay: true,
        layout: new Layout({
            fit: Fit.Contain,
            alignment: Alignment.Center,
        }),
    });

    // State machine inputs:
    // Based on debugging, we only have "hover" (boolean/trigger) and "press"
    // No "mouseX" or "mouseY" inputs exist, which confirms why direct input mapping failed.
    const hoverInput = useStateMachineInput(rive, "State Machine 1", "hover");

    React.useEffect(() => {
        if (!rive || !RiveComponent) return;

        // Debugging: Verify we are running this effect
        // console.log("Rive Event Proxy Effect Active");

        const handleMouseMove = (e) => {
            // 1. Ensure the state machine thinks we are hovering
            if (hoverInput) {
                hoverInput.value = true;
            }

            // 2. Proxy the event to the canvas
            // The Rive runtime listens to events on the canvas element internally.
            // By dispatching a new event on the canvas with the global coordinates, 
            // we trick Rive into tracking the mouse globally as if the canvas covered the screen.

            // We use the canvas ref from useRive
            const canvas = canvasRef.current;

            if (canvas) {
                // Construct a new PointerEvent. 
                // We pass clientX/clientY directly. Rive handles the offset calculation relative to canvas rect internally.
                // We need to simulate a 'pointermove' which Rive listens to.
                const event = new PointerEvent('pointermove', {
                    bubbles: true,
                    cancelable: true,
                    view: window,
                    clientX: e.clientX,
                    clientY: e.clientY,
                    pointerType: 'mouse',
                    isPrimary: true
                });

                canvas.dispatchEvent(event);
            }
        };

        window.addEventListener('mousemove', handleMouseMove);

        return () => {
            window.removeEventListener('mousemove', handleMouseMove);
        };
    }, [rive, hoverInput, canvasRef]); // Added canvasRef to dependency

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
