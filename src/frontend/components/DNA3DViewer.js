import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";

function DNA3DViewer() {
    return (
        <Canvas>
            <ambientLight />
            <mesh position={[0, 0, 0]}>
                <sphereGeometry args={[1, 32, 32]} />
                <meshStandardMaterial color="purple" />
            </mesh>
            <OrbitControls />
        </Canvas>
    );
}

export default DNA3DViewer;
