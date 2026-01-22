import { useRive, Layout, Fit, Alignment } from '@rive-app/react-canvas';

const RiveDashboardCharacter = () => {
    const { RiveComponent } = useRive({
        src: '/13393-25338-mouse-tracking.riv',
        stateMachines: "State Machine 1", // "Click me" usually implies a State Machine is needed
        autoplay: true,
        layout: new Layout({
            fit: Fit.Contain,
            alignment: Alignment.Center,
        }),
    });

    return (
        <div className="w-full h-full flex items-center justify-center overflow-hidden">
            <div
                className="w-full h-full flex items-center justify-center arrow-pointer"
                style={{
                    maskImage: 'radial-gradient(circle, black 30%, transparent 70%)',
                    WebkitMaskImage: 'radial-gradient(circle, black 30%, transparent 70%)'
                }}
            >
                <RiveComponent className="w-full h-full" style={{ minHeight: '200px', transform: 'scale(4)' }} />
            </div>
        </div>
    );
};

export default RiveDashboardCharacter;
