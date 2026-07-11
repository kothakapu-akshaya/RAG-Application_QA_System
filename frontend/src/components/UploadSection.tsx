import { useState } from "react";
import { uploadDocument } from "../services/upload";

type UploadSectionProps = {
  onUpload: (files: File[]) => void;
};

function UploadSection({ onUpload }: UploadSectionProps) {
  const [selectedFiles, setSelectedFiles] = useState<File[]>([]);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (!event.target.files) return;

    setSelectedFiles(Array.from(event.target.files));
  };
  const handleUploadClick = async () => {
  if (selectedFiles.length === 0) return;

  try {
    for (const file of selectedFiles) {
      await uploadDocument(file);
    }

    onUpload(selectedFiles);

    setSelectedFiles([]);
  } catch (error) {
    console.error("Upload failed:", error);

    // Temporary until backend is running
    onUpload(selectedFiles);

    alert("Backend not available. Files added locally.");

    setSelectedFiles([]);
  }
};
  return (
    <section>
      <h2>Upload Documents</h2>

      <div className="upload-section">
        <input type="file" multiple accept=".pdf" onChange={handleFileChange} />

        <button
          onClick={handleUploadClick}
          disabled={selectedFiles.length === 0}
        >
          Upload
        </button>
      </div>

      {selectedFiles.length > 0 && (
        <div className="selected-files">
          <h3>Selected Files</h3>

          <ul>
            {selectedFiles.map((file) => (
              <li key={file.name}>{file.name}</li>
            ))}
          </ul>
        </div>
      )}
    </section>
  );
}

export default UploadSection;
