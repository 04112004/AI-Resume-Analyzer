function JobDescription({ jobDesc, setJobDesc }) {
  return (
    <div>
      <label>Job Description</label><br />
      <textarea
        rows="6"
        cols="50"
        value={jobDesc}
        onChange={(e) => setJobDesc(e.target.value)}
        placeholder="Paste job description here..."
      />
    </div>
  );
}

export default JobDescription;
