import React from "react";

function AnalysisResults({ data }) {
  return (
    <div className="analysis-results">
      <h2>📊 Результаты анализа</h2>
      <p>Риск мутации: {data.mutation_risk * 100}%</p>
    </div>
  );
}

export default AnalysisResults;
