import React from "react";

function ControlPanel({ onStretchChange, onAnalyze }) {
  return (
    <div className="control-panel">
      <h2>🔧 Управление ДНК</h2>
      <input
        type="range"
        min="0.8"
        max="1.5"
        step="0.01"
        onChange={(e) => onStretchChange(parseFloat(e.target.value))}
      />
      <button onClick={onAnalyze}>📊 Запустить анализ</button>
    </div>
  );
}

export default ControlPanel;
