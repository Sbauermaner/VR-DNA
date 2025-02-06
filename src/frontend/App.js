import React, { useState } from "react";
import DNA3DViewer from "./components/DNA3DViewer";
import ControlPanel from "./components/ControlPanel";
import AnalysisResults from "./components/AnalysisResults";

function App() {
  const [stretchFactor, setStretchFactor] = useState(1.0);
  const [analysisData, setAnalysisData] = useState(null);

  const handleStretchChange = (factor) => {
    setStretchFactor(factor);
  };

  const runAIAnalysis = async () => {
    const response = await fetch("http://localhost:5000/analyze_stretch", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ stretch_values: [stretchFactor] }),
    });
    const data = await response.json();
    setAnalysisData(data);
  };

  return (
    <div className="app-container">
      <h1>🔬 VR-DNA Laboratory</h1>
      <DNA3DViewer stretchFactor={stretchFactor} />
      <ControlPanel onStretchChange={handleStretchChange} onAnalyze={runAIAnalysis} />
      {analysisData && <AnalysisResults data={analysisData} />}
    </div>
  );
}

export default App;
