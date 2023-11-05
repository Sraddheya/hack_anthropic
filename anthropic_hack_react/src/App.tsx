import React from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Signup from "./Components/Signup";
import PDFUploader from "./Components/PDFLoader";

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/PDFloader" Component={PDFUploader} />
        <Route path="/" Component={Signup} />
      </Routes>
    </Router>
  );
};

export default App;
