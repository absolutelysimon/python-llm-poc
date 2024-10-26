import React, { useState } from "react";
import SpeechRecognition, {
  useSpeechRecognition,
} from "react-speech-recognition";
import {
  Button,
  TextField,
  IconButton,
  Typography,
  Paper,
  Box,
} from "@mui/material";
import MicIcon from "@mui/icons-material/Mic";
import StopIcon from "@mui/icons-material/Stop";
import SendIcon from "@mui/icons-material/Send";
import httpService from "./services/httpService";

const ChatInterface = () => {
  const {
    transcript,
    listening,
    resetTranscript,
    browserSupportsSpeechRecognition,
  } = useSpeechRecognition();

  const [userInput, setUserInput] = useState("");
  const [isListening, setIsListening] = useState(listening);
  const [messages, setMessages] = useState([]);

  if (!browserSupportsSpeechRecognition) {
    return (
      <Typography color="error">
        Browser doesn't support speech recognition.
      </Typography>
    );
  }

  const handleStartListening = () => {
    resetTranscript();
    setUserInput("");
    SpeechRecognition.startListening({ continuous: true });
    setIsListening(true);
  };

  const handleStopListening = () => {
    SpeechRecognition.stopListening();
    setIsListening(false);
  };

  const resetInput = () => {
    setUserInput("");
    resetTranscript();
    SpeechRecognition.stopListening();
    setIsListening(false);
  };

  const handleSendInput = async () => {
    try {
      handleStopListening();
      resetTranscript();
      const finalInput = transcript || userInput;
      if (finalInput) {
        setMessages((prevMessages) => [
          ...prevMessages,
          { text: finalInput, isUser: true },
        ]);
        setUserInput("");
      }
      const response = await httpService.post("/api/endpoint", {
        text: finalInput,
      });
      console.log("Response from API:", response.data);
    } catch (error) {
      console.error("Error sending input:", error);
      resetInput();
    }
  };

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        height: "100vh",
        padding: "20px",
        backgroundColor: "#f5f5f5",
      }}
    >
      <Paper
        elevation={3}
        sx={{
          flex: 1,
          overflowY: "auto",
          padding: "10px",
          backgroundColor: "#fff",
          borderRadius: "10px",
        }}
      >
        <Typography variant="h5" align="center" gutterBottom>
          Chat
        </Typography>
        {messages?.map((msg, index) => (
          <Typography
            key={index}
            align={msg.isUser ? "right" : "left"}
            sx={{
              marginBottom: "10px",
              padding: "10px",
              backgroundColor: msg.isUser ? "#e3f2fd" : "#f1f1f1",
              borderRadius: "10px",
            }}
          >
            {msg.text}
          </Typography>
        ))}
        {transcript && (
          <Typography
            align="left"
            sx={{
              marginBottom: "10px",
              padding: "10px",
              backgroundColor: "#e3f2fd",
              borderRadius: "10px",
            }}
          >
            {transcript}
          </Typography>
        )}
      </Paper>

      <Box sx={{ display: "flex", alignItems: "center", marginTop: "10px" }}>
        <TextField
          label="Type your message..."
          variant="outlined"
          fullWidth
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          sx={{ marginRight: "10px" }}
        />
        <IconButton
          color={isListening ? "secondary" : "primary"}
          onClick={isListening ? handleStopListening : handleStartListening}
        >
          {isListening ? <StopIcon /> : <MicIcon />}
        </IconButton>
        <Button
          variant="contained"
          color="primary"
          endIcon={<SendIcon />}
          onClick={handleSendInput}
        >
          Send
        </Button>
      </Box>
    </Box>
  );
};

export default ChatInterface;
