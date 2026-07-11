import api from "../api";

export const queryDocument = async (question: string) => {
  const response = await api.post("/query/", {
    question,
  });

  return response.data;
};