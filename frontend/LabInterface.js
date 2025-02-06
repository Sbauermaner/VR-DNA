import React, { useState } from "react";

function LabInterface() {
    const [dnaSequence, setDnaSequence] = useState("");
    const [result, setResult] = useState(null);

    const analyzeDNA = async () => {
        const response = await fetch("http://localhost:5000/analyze_dna", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ dna_sequence: dnaSequence }),
        });
        const data = await response.json();
        setResult(data);
    };

    return (
        <div>
            <h1>🔬 VR-DNA Laboratory</h1>
            <input type="text" onChange={(e) => setDnaSequence(e.target.value)} />
            <button onClick={analyzeDNA}>📊 Анализировать</button>
            {result && <p>Риск мутации: {result.mutation_risk * 100}%</p>}
        </div>
    );
}

export default LabInterface;
