import { useState } from "react";
import "./index.css";

import UploadSection from "./components/UploadSection";
import ChatWindow from "./components/ChatWindow";

function App() {
  const [uploadMessage, setUploadMessage] = useState("");
  const handleUpload = (files: File[]) => {
    if (files.length === 1) {
      setUploadMessage(`${files[0].name} uploaded successfully!`);
    } else {
      setUploadMessage(`${files.length} files uploaded successfully!`);
    }
  };

  return (
    <div className="app">
      <h1>Document Q&A</h1>

      <UploadSection onUpload={handleUpload} />
      {uploadMessage && <p className="upload-message">✅ {uploadMessage}</p>}
      <ChatWindow />
    </div>
  );
}

export default App;
