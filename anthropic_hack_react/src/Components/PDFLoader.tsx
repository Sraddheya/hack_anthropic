import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const PdfUploader: React.FC = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const fileList = event.target.files;
    if (fileList) {
      const file: File = fileList[0];
      if (file.type === 'application/pdf') {
        setSelectedFile(file);
      } else {
        alert('Please upload a PDF file.');
      }
    }
  };

  const handleFileSubmit = () => {
    if (selectedFile) {
      const reader = new FileReader();
      reader.onload = (event) => {
        // Do whatever you want with the file data (e.g., upload to a server, store in state, etc.)
        const uploadedFileData = event.target?.result;
        console.log('Uploaded File Data:', uploadedFileData);
        // Example: Send the file data to the server
        // uploadFileToServer(uploadedFileData);
      };
      reader.readAsDataURL(selectedFile);
    } else {
      alert('Please select a file to upload.');
    }
  };

  return (
    <div className="container mt-4">
      <div className="row">
        <div className="col-6 offset-3">
          <input type="file" className="form-control mb-3" accept=".pdf" onChange={handleFileUpload} />
          <button className="btn btn-primary" onClick={handleFileSubmit}>
            Upload PDF
          </button>
        </div>
      </div>
    </div>
  );
};

export default PdfUploader;
