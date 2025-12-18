import axios from "axios";

export const analyzeResume = async (resume, jobDesc) => {
  const formData = new FormData();
  formData.append("file", resume);
  formData.append("job_desc", jobDesc);

  const response = await axios.post(
    "https://ai-resume-analyzer-backend-kqgq.onrender.com/analyze/",
    formData
  );

  return response.data;
};
