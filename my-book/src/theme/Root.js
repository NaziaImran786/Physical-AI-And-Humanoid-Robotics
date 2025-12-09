import React from 'react';

// IMPORT PATH YAHAN THEEK KAREIN: AAKHRI MEIN '/Chatbot' HATA DEIN
import Chatbot from '../components/Chatbot'; 

// Default implementation, that you can customize
function Root({children}) {
  return (
    <>
      {children}
      <Chatbot />
    </>
  );
}

export default Root;