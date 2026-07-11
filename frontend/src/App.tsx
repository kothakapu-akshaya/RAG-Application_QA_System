import { useState } from "react";
import "./index.css";

import UploadSection from "./components/UploadSection";
import DocumentList from "./components/DocumentList";
import ChatWindow from "./components/ChatWindow";

type Document = {
  id: string;
  name: string;
};

function App() {
  const [documents, setDocuments] = useState<Document[]>([]);

  const handleUpload = (files: File[]) => {
    const uploadedDocuments = files.map((file) => ({
      id: crypto.randomUUID(),
      name: file.name,
    }));

    setDocuments((prev) => [...prev, ...uploadedDocuments]);
  };
  const handleDelete = (id: string) => {
    setDocuments((prev) => prev.filter((doc) => doc.id !== id));
  };

  return (
    <div className="app">
      <h1>Document Q&A</h1>

      <UploadSection onUpload={handleUpload} />

      <DocumentList documents={documents} onDelete={handleDelete} />

      <ChatWindow />
    </div>
  );
}

export default App;
