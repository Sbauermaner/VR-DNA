import React from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";

function DNA3DViewer({ stretchFactor }) {
  return (
    <Canvas>
      <OrbitControls />
      <ambientLight />
      <mesh scale={[1, 1, stretchFactor]}>
        <cylinderGeometry args={[0.1, 0.1, 5, 32]} />
        <meshStandardMaterial color="blue" />
      </mesh>
    </Canvas>
  );
}

export default DNA3DViewer;
