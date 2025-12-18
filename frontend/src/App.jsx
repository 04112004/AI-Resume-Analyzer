import { useState } from "react";
import ResumeUpload from "./components/ResumeUpload";
import JobDescription from "./components/JobDescription";
import ResultCard from "./components/ResultCard";
import { analyzeResume } from "./api/resumeApi";
import "./styles/app.css";

function App() {
  const [resume, setResume] = useState(null);
  const [jobDesc, setJobDesc] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!resume || !jobDesc) {
      alert("Upload resume and job description");
      return;
    }

    setLoading(true);
    const data = await analyzeResume(resume, jobDesc);
    setResult(data);
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>AI Resume Analyzer</h1>

      <ResumeUpload setResume={setResume} />
      <br />

      <JobDescription jobDesc={jobDesc} setJobDesc={setJobDesc} />

      <button onClick={handleAnalyze}>
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>

      <ResultCard result={result} />
    </div>
  );
}

export default App;
