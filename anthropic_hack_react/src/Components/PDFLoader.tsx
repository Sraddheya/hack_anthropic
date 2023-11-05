import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';

// const PdfUploader: React.FC = () => {
//   const [selectedFile, setSelectedFile] = useState<File | null>(null);

//   const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
//     const fileList = event.target.files;
//     if (fileList) {
//       const file: File = fileList[0];
//       if (file.type === 'application/pdf') {
//         setSelectedFile(file);
//       } else {
//         alert('Please upload a PDF file.');
//       }
//     }
//   };

//   const handleFileSubmit = async () => {
//     if (selectedFile) {
//       try {
//         const formData = new FormData();
//         formData.append('pdfFile', selectedFile);

//         const response = await fetch('http://localhost:5000/upload', {
//           method: 'POST',
//           body: formData,
//         });

//         if (response.ok) {
//           // Handle success
//           console.log('PDF file uploaded successfully');
//         } else {
//           // Handle errors
//           console.error('Error uploading PDF file');
//         }
//       } catch (error) {
//         // Handle network errors
//         console.error('Network error:', error);
//       }
//     } else {
//       alert('Please select a file to upload.');
//     }
//   };

// //   const handleFileSubmit = async () => {
// //     if (selectedFile) {
// //         const formData = new FormData();
// //         formData.append('file', selectedFile);

// //       try {
// //         const response = await axios.post('http://localhost:5000/upload', formData, {
// //           headers: {
// //             'Content-Type': 'multipart/form-data'
// //           }
// //         });
// //         console.log('File uploaded:', response.data);
// //       } catch (error) {
// //         console.error('Error uploading file:', error);



//     //   const reader = new FileReader();
//     //   reader.onload = (event) => {
//     //     // Do whatever you want with the file data (e.g., upload to a server, store in state, etc.)
//     //     const uploadedFileData = event.target?.result;
//     //     console.log('Uploaded File Data:', uploadedFileData);
//     //     // Example: Send the file data to the server
//     //     // uploadFileToServer(uploadedFileData);
//     //   };
//     //   reader.readAsDataURL(selectedFile);
//     // } else {
//     //   alert('Please select a file to upload.');
//     // }

//   return (
//     <div className="container mt-4">
//       <div className="row">
//         <div className="col-6 offset-3">
//           <input type="file" className="form-control mb-3" accept=".pdf" onChange={handleFileUpload} />
//           <button className="btn btn-primary" onClick={handleFileSubmit}>
//             Upload PDF
//           </button>
//         </div>
//       </div>
//     </div>
//   );
// };

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
