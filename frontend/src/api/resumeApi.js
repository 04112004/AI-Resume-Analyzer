import axios from "axios";

const API_BASE_URL = "https://ai-resume-analyzer-backend-kgqq.onrender.com";

export const analyzeResume = async (resume, jobDesc) => {
  const formData = new FormData();
  formData.append("file", resume);
  formData.append("job_desc", jobDesc);

  const response = await axios.post(
    `${API_BASE_URL}/analyze/`,
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};
