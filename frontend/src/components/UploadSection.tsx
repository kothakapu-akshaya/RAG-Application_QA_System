import { useState } from "react";

type UploadSectionProps = {
  onUpload: (files: File[]) => void;
};

function UploadSection({ onUpload }: UploadSectionProps) {
  const [selectedFiles, setSelectedFiles] = useState<File[]>([]);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (!event.target.files) return;

    setSelectedFiles(Array.from(event.target.files));
    console.log(Array.from(event.target.files));
  };

  const handleUploadClick = () => {
    if (selectedFiles.length === 0) return;

    onUpload(selectedFiles);

    setSelectedFiles([]);
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
