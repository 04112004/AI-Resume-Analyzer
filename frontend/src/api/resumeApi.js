import axios from "axios";

export const analyzeResume = async (resume, jobDesc) => {
  const formData = new FormData();
  formData.append("file", resume);
  formData.append("job_desc", jobDesc);

  const response = await axios.post(
    "http://127.0.0.1:8000/analyze/",
    formData
  );

  return response.data;
};
