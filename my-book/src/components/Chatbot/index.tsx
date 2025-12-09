// D:\...\my-book\src\components\Chatbot\index.tsx

import React, { useState, useCallback, useMemo } from 'react';
import axios from 'axios';

// FastAPI Server URL (jo 8000 par chal raha hai)
const API_URL = 'http://localhost:8000/chat';

// Simple Message Component
const Message: React.FC<{ sender: 'user' | 'bot'; text: string }> = ({ sender, text }) => {
  return (
    <div style={{
      textAlign: sender === 'user' ? 'right' : 'left',
      margin: '8px 0',
    }}>
      <span style={{
        display: 'inline-block',
        padding: '10px 15px',
        borderRadius: '18px',
        maxWidth: '85%',
        // Styling fix for readability
        backgroundColor: sender === 'user' ? '#DCECF7' : '#F0F0F0', // Light Blue or Light Gray
        color: '#000000', // Ensure text is black
        wordBreak: 'break-word',
      }}>
        {text}
      </span>
    </div>
  );
};

const Chatbot: React.FC = () => {
  // Chat window khula hai ya band?
  const [isOpen, setIsOpen] = useState(false); 
  const [messages, setMessages] = useState<{ sender: 'user' | 'bot'; text: string }[]>([
      { sender: 'bot', text: 'Hello! How can I help you today?' } // Initial bot message
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  // Icon par click karne par khule/band ho
  const toggleChat = useCallback(() => {
    setIsOpen(prev => !prev);
  }, []);

  // API Call aur Message Sending Logic
  const handleSend = useCallback(async () => {
    if (!input.trim() || loading) return;

    const userMessage = input.trim();
    // 1. User message ko add karein
    setMessages(prev => [...prev, { sender: 'user', text: userMessage }]);
    setInput('');
    setLoading(true);

    try {
      // API Call
      const response = await axios.post(API_URL, { message: userMessage });
      const botResponse = response.data.response || "Server did not provide a response.";
      
      // 2. Bot ka jawab add karein
      setMessages(prev => [...prev, { sender: 'bot', text: botResponse }]);
    } catch (error) {
      console.error("API Error:", error);
      setMessages(prev => [...prev, { sender: 'bot', text: "Error: Could not connect to the backend API at http://localhost:8000/chat" }]);
    } finally {
      setLoading(false);
    }
  }, [input, loading]);

  const handleKeyPress = useCallback((e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && !loading) {
      handleSend();
    }
  }, [handleSend, loading]);

  // Dynamic Styles (inline styling)
  const chatWindowStyle: React.CSSProperties = useMemo(() => ({
    position: 'fixed',
    bottom: '90px', /* Icon se upar */
    right: '20px',
    zIndex: 1000,
    backgroundColor: 'white',
    border: '1px solid #ccc',
    borderRadius: '12px',
    boxShadow: '0px 6px 16px rgba(0, 0, 0, 0.2)',
    width: '350px',
    height: '500px',
    display: 'flex',
    flexDirection: 'column',
    transition: 'transform 0.3s ease-in-out, opacity 0.3s ease-in-out',
    transform: isOpen ? 'translateY(0)' : 'translateY(100%)',
    opacity: isOpen ? 1 : 0,
    pointerEvents: isOpen ? 'auto' : 'none', // Band hone par clicks ko ignore karega
    overflow: 'hidden',
  }), [isOpen]);

  const toggleButtonStyle: React.CSSProperties = {
    position: 'fixed',
    bottom: '20px',
    right: '20px',
    width: '60px',
    height: '60px',
    borderRadius: '50%',
    backgroundColor: '#2e8555', // Primary Docusaurus color
    color: 'white',
    fontSize: '24px',
    border: 'none',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.3)',
    cursor: 'pointer',
    zIndex: 1001,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  };

  return (
    <>
      {/* 1. Toggle Button (Icon) */}
      <button 
        style={toggleButtonStyle} 
        onClick={toggleChat}
        title={isOpen ? "Close Chatbot" : "Open Chatbot"}
      >
        {isOpen ? '✖' : '🤖'} {/* Bot icon ya X icon */}
      </button>

      {/* 2. Main Chat Window */}
      <div style={chatWindowStyle}>
        
        {/* Header */}
        <div style={{ padding: '10px', backgroundColor: '#2e8555', color: 'white', borderTopLeftRadius: '12px', borderTopRightRadius: '12px' }}>
          Panasversity AI Assistant
        </div>

        {/* Message Area */}
        <div style={{ flexGrow: 1, padding: '15px', overflowY: 'auto', backgroundColor: '#f9f9f9' }}>
          {messages.map((msg, index) => (
              <Message key={index} sender={msg.sender} text={msg.text} />
          ))}

          {/* Loading Indicator */}
          {loading && <Message sender="bot" text="Bot is typing..." />}
        </div>

        {/* Input Field */}
        <div style={{ padding: '10px', borderTop: '1px solid #ddd', display: 'flex', gap: '5px' }}>
          <input
            type="text"
            placeholder={loading ? "Waiting for response..." : "Type your message..."}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            style={{
              flexGrow: 1,
              padding: '10px',
              borderRadius: '6px',
              border: '1px solid #ccc',
              backgroundColor: 'white',
              color: 'black'
            }}
            disabled={loading}
          />
          <button 
            onClick={handleSend} 
            disabled={loading || !input.trim()}
            style={{ 
              padding: '10px 15px', 
              backgroundColor: '#2e8555', 
              color: 'white', 
              border: 'none', 
              borderRadius: '6px',
              cursor: (loading || !input.trim()) ? 'not-allowed' : 'pointer'
            }}
          >
            Send
          </button>
        </div>
      </div>
    </>
  );
};

export default Chatbot;