import React from 'react';
import BrowserOnly from '@docusaurus/BrowserOnly';
import Chatbot from '../components/Chatbot'; 

function Root({children}) {
  return (
    <>
      {children}
      <BrowserOnly>
        {() => <Chatbot />}
      </BrowserOnly>
    </>
  );
}

export default Root;