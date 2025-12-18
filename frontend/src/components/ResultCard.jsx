function ResultCard({ result }) {
  if (!result) return null;

  return (
    <div className="result-card">
      <h3>Analysis Result</h3>

      <p><b>Score:</b> {result.score}%</p>

      <div className="progress-bar">
        <div
          className="progress-fill"
          style={{ width: `${result.score}%` }}
        ></div>
      </div>

      <p><b>Feedback:</b> {result.feedback}</p>

      {/* Matched Skills */}
      <h4 style={{ marginTop: "15px" }}>✅ Matched Skills</h4>
      {result.matched_skills && result.matched_skills.length > 0 ? (
        <div className="skill-container">
          {result.matched_skills.map((skill, index) => (
            <span key={index} className="skill-tag matched">
              {skill}
            </span>
          ))}
        </div>
      ) : (
        <p>No matched skills</p>
      )}

      {/* Missing Skills */}
      <h4 style={{ marginTop: "15px" }}>❌ Missing Skills</h4>
      {result.missing_skills && result.missing_skills.length > 0 ? (
        <div className="skill-container">
          {result.missing_skills.map((skill, index) => (
            <span key={index} className="skill-tag missing">
              {skill}
            </span>
          ))}
        </div>
      ) : (
        <p>No missing skills 🎉</p>
      )}
      {/* AI Improvement Tips */}
<h4 style={{ marginTop: "20px" }}>🤖 AI Improvement Tips</h4>

{result.ai_tips && result.ai_tips.length > 0 ? (
  <ul>
    {result.ai_tips.map((tip, index) => (
      <li key={index} style={{ marginBottom: "6px" }}>
        {tip}
      </li>
    ))}
  </ul>
) : (
  <p>No improvement tips 🎉</p>
)}

    </div>
  );
}

export default ResultCard;


