function ResumeUpload({ setResume }) {
  return (
    <div>
      <label>Upload Resume (PDF)</label><br />
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setResume(e.target.files[0])}
      />
    </div>
  );
}

export default ResumeUpload;
